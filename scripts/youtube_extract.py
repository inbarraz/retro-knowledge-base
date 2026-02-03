#!/usr/bin/env python3
"""
YouTube Extractor Tool

Extracts video transcripts and metadata from YouTube URLs, outputting a filtered JSON file per video.

Dependencies:
    - fabric: Used for transcript extraction (https://github.com/danielmiessler/fabric)
    - yt-dlp: Used for video metadata extraction (https://github.com/yt-dlp/yt-dlp)

Usage:
    python youtube_extract.py -u "https://youtube.com/watch?v=VIDEO_ID" -o /output/dir
    python youtube_extract.py -f urls.txt -o /output/dir
    python youtube_extract.py -f urls.txt -o /output/dir -d 5  # with 5 second delay between URLs
"""

import argparse
import json
import logging
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Fields to keep from yt-dlp metadata output
FIELDS_TO_KEEP = [
    "id", "title", "description", "channel_id", "channel_url", "duration", "webpage_url",
    "categories", "tags", "channel", "uploader", "uploader_id", "uploader_url",
    "upload_date", "timestamp", "availability", "webpage_url_basename", "webpage_url_domain",
    "extractor", "extractor_key", "display_id", "fulltitle", "duration_string", "epoch", "asr"
]

# Required external dependencies
REQUIRED_COMMANDS = ['fabric', 'yt-dlp']


def check_dependencies() -> bool:
    """Check if required external tools are installed."""
    missing = []
    for cmd in REQUIRED_COMMANDS:
        if shutil.which(cmd) is None:
            missing.append(cmd)

    if missing:
        logger.error(f"Missing required dependencies: {', '.join(missing)}")
        logger.error("Please install them before running this tool.")
        return False
    return True


def parse_args(args=None):
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Extract transcripts and metadata from YouTube videos.'
    )

    # Mutually exclusive group for URL input
    url_group = parser.add_mutually_exclusive_group(required=True)
    url_group.add_argument(
        '-u', '--url',
        help='Single YouTube URL to process'
    )
    url_group.add_argument(
        '-f', '--file',
        help='Path to file containing YouTube URLs (one per line)'
    )

    parser.add_argument(
        '-o', '--output-dir',
        default='.',
        help='Output directory for JSON files (default: current directory)'
    )

    parser.add_argument(
        '-d', '--delay',
        type=float,
        default=0,
        help='Seconds to wait between downloads (only applies to file mode, default: 0)'
    )

    return parser.parse_args(args)


def load_urls_from_file(filepath: str) -> list[str]:
    """
    Load URLs from a file, one per line.
    Skips empty lines and lines starting with #.
    """
    urls = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            # Skip empty lines and comments
            if line and not line.startswith('#'):
                urls.append(line)
    return urls


def extract_transcript(url: str) -> str | None:
    """
    Extract transcript using fabric tool.
    Returns transcript text or None on error.
    """
    try:
        result = subprocess.run(
            ['fabric', '-y', url, '--transcript'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to extract transcript for {url}: {e.stderr}")
        return None
    except FileNotFoundError:
        logger.error("fabric command not found. Please ensure fabric is installed.")
        return None


def extract_metadata(url: str, output_dir: str) -> dict | None:
    """
    Extract metadata using yt-dlp.
    Returns parsed JSON metadata or None on error.
    """
    try:
        # Run yt-dlp to get metadata JSON
        result = subprocess.run(
            ['yt-dlp', '--write-info-json', '--skip-download', '-o', '%(id)s', url],
            capture_output=True,
            text=True,
            cwd=output_dir,
            check=True
        )

        # Find the generated .info.json file
        # yt-dlp outputs the video ID in its output, or we can search for the file
        for line in result.stdout.split('\n'):
            if 'Writing video metadata' in line or '.info.json' in line:
                logger.debug(f"yt-dlp output: {line}")

        # Look for the most recently created .info.json file
        info_files = list(Path(output_dir).glob('*.info.json'))
        if not info_files:
            logger.error(f"No .info.json file found for {url}")
            return None

        # Get the most recent one
        info_file = max(info_files, key=lambda p: p.stat().st_mtime)

        with open(info_file, 'r') as f:
            metadata = json.load(f)

        # Store the info file path for cleanup
        metadata['_info_file_path'] = str(info_file)

        return metadata

    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to extract metadata for {url}: {e.stderr}")
        return None
    except FileNotFoundError:
        logger.error("yt-dlp command not found. Please ensure yt-dlp is installed.")
        return None
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse metadata JSON for {url}: {e}")
        return None


def filter_metadata(metadata: dict) -> dict:
    """Filter metadata to only include specified fields."""
    return {key: metadata[key] for key in FIELDS_TO_KEEP if key in metadata}


def merge_and_save(metadata: dict, transcript: str, output_dir: str) -> str | None:
    """
    Merge filtered metadata with transcript and save to JSON file.
    Returns the output file path or None on error.
    """
    video_id = metadata.get('id')
    if not video_id:
        logger.error("No video ID found in metadata")
        return None

    # Filter metadata fields
    filtered = filter_metadata(metadata)

    # Add transcript
    filtered['transcript'] = transcript

    # Save to file
    output_path = Path(output_dir) / f"{video_id}.json"
    with open(output_path, 'w') as f:
        json.dump(filtered, f, indent=2, ensure_ascii=False)

    return str(output_path)


def cleanup_info_file(metadata: dict) -> None:
    """Delete the intermediate .info.json file."""
    info_file = metadata.get('_info_file_path')
    if info_file and os.path.exists(info_file):
        try:
            os.remove(info_file)
            logger.debug(f"Cleaned up {info_file}")
        except OSError as e:
            logger.warning(f"Failed to cleanup {info_file}: {e}")


def process_url(url: str, output_dir: str) -> str | None:
    """
    Process a single YouTube URL.
    Returns None on success, or a failure reason string on failure.
    """
    logger.info(f"Processing: {url}")

    # Extract transcript
    transcript = extract_transcript(url)
    if transcript is None:
        reason = "transcript extraction failure"
        logger.error(f"Skipping {url} due to {reason}")
        return reason

    # Extract metadata
    metadata = extract_metadata(url, output_dir)
    if metadata is None:
        reason = "metadata extraction failure"
        logger.error(f"Skipping {url} due to {reason}")
        return reason

    # Merge and save
    output_path = merge_and_save(metadata, transcript, output_dir)
    if output_path is None:
        reason = "merge/save failure"
        logger.error(f"Skipping {url} due to {reason}")
        cleanup_info_file(metadata)
        return reason

    # Cleanup intermediate file
    cleanup_info_file(metadata)

    logger.info(f"Successfully created: {output_path}")
    return None


def main():
    """Main entry point."""
    # Check for required dependencies first
    if not check_dependencies():
        sys.exit(1)

    args = parse_args()

    # Ensure output directory exists
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Get list of URLs to process
    if args.url:
        urls = [args.url]
    else:
        try:
            urls = load_urls_from_file(args.file)
        except FileNotFoundError:
            logger.error(f"URL file not found: {args.file}")
            sys.exit(1)
        except Exception as e:
            logger.error(f"Failed to read URL file: {e}")
            sys.exit(1)

    if not urls:
        logger.warning("No URLs to process")
        sys.exit(0)

    logger.info(f"Processing {len(urls)} URL(s)")

    # Process each URL
    success_count = 0
    fail_count = 0
    failed_urls = []  # List of (url, reason) tuples

    for i, url in enumerate(urls):
        failure_reason = process_url(url, str(output_dir))
        if failure_reason is None:
            success_count += 1
        else:
            fail_count += 1
            failed_urls.append((url, failure_reason))

        # Log progress
        logger.info(f"Progress: {i + 1}/{len(urls)} processed ({success_count} succeeded, {fail_count} failed)")

        # Add delay between URLs (not after the last one)
        if args.delay > 0 and i < len(urls) - 1:
            logger.info(f"Waiting {args.delay} seconds before next URL...")
            time.sleep(args.delay)

    # Write failed URLs to file
    if failed_urls:
        failed_file = output_dir / "failed.txt"
        with open(failed_file, 'w') as f:
            for url, reason in failed_urls:
                f.write(f"{url}\t{reason}\n")
        logger.info(f"Failed URLs logged to: {failed_file}")

    # Summary
    logger.info(f"Completed: {success_count} succeeded, {fail_count} failed")

    if fail_count > 0:
        sys.exit(1)


if __name__ == '__main__':
    main()
