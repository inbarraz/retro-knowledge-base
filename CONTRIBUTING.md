# Contributing to the Retro Knowledge Base

Thank you for your interest in contributing to the retrocomputing knowledge base!

## Prerequisites

- [Claude Code](https://claude.com/claude-code) installed
- Git
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for video metadata extraction
- [fabric](https://github.com/danielmiessler/fabric) for transcript extraction

### Installing Dependencies

```bash
# macOS
brew install yt-dlp
brew install fabric

# Or using pip/go
pip install yt-dlp
go install github.com/danielmiessler/fabric@latest

# Other platforms:
# yt-dlp: https://github.com/yt-dlp/yt-dlp#installation
# fabric: https://github.com/danielmiessler/fabric#installation
```

## Getting Started

### 1. Clone and Install

```bash
git clone https://github.com/inbarraz/retro-knowledge-base
cd retro-knowledge-base
claude plugin install ./
```

### 2. Download Transcripts

Use the extraction script to download video metadata and transcripts:

```bash
# Single video
python scripts/youtube_extract.py -u "https://youtube.com/watch?v=VIDEO_ID" -o transcripts/

# Multiple videos from file
python scripts/youtube_extract.py -f urls.txt -o transcripts/ -d 5
```

The `.json` file contains:
- Video metadata (title, channel, date)
- Full transcript text
- Description (often contains links to tools/parts)

### 3. Process the Transcript

Start Claude Code and run the analysis skill:

```bash
cd retro-knowledge-base
claude
```

Then in Claude Code:
```
/retro-analyze-transcript ./transcripts/VIDEO_ID.json
```

The skill will:
1. Parse the transcript
2. Extract knowledge about platforms, repairs, and techniques
3. Show you proposed changes
4. Ask for approval before modifying files
5. Update the knowledge base with proper source attribution

### 4. Review Changes

```bash
git diff                    # Review what changed
git status                  # See which files were modified/created
```

### 5. Commit and Push

```bash
git add knowledge/
git commit -m "Add knowledge from VIDEO_ID: Brief description"
git push origin your-branch
```

### 6. Open a Pull Request

Create a PR with:
- Video title and link
- Summary of knowledge added
- Any notes about uncertain extractions

## File Naming Conventions

### Vendor Files

- Lowercase with hyphens: `vendor-western-digital.md`
- Use canonical vendor names (see below)
- One file per vendor

**Common Vendor Mappings:**
| Variations | Canonical Name |
|------------|----------------|
| WDC, Western Digital Corp | `vendor-western-digital.md` |
| TI, Texas Instruments | `vendor-ti.md` |
| Radio Shack, Tandy | `vendor-tandy.md` |
| DEC, Digital Equipment | `vendor-dec.md` |

### Technique Files

Do NOT create new technique files. Use only the existing 11 categories:

| File | Topics |
|------|--------|
| `tech-crt-display.md` | CRT, monitors, display issues |
| `tech-diagnostics.md` | Testing, measurement, fault finding |
| `tech-storage.md` | Hard drives, floppy, SCSI |
| `tech-pcb-soldering.md` | PCB repair, soldering, wire work |
| `tech-power.md` | Power supplies, capacitors |
| `tech-cleaning.md` | Cleaning, restoration |
| `tech-peripherals.md` | Keyboards, joysticks, connectors |
| `tech-video.md` | Video capture, converters |
| `tech-memory-cpu.md` | RAM, CPU topics |
| `tech-modern-retro.md` | Modern solutions, adapters |
| `tech-misc.md` | Safety, tools, miscellaneous |

## Quality Standards

### Source Attribution

Every fact must have source attribution:
```markdown
- Capacitor C42 commonly fails on revision 2 boards - Source: [dQw4w9WgXcQ]
```

### No Duplicates

Before adding information, check if it already exists:
- Search existing vendor files
- Check technique category files
- The analysis skill does this automatically

### Preserve Structure

When manually editing files:
- Maintain existing section hierarchy
- Follow the established format
- Don't reorganize existing content

### Accuracy

- Only add information clearly stated in the video
- Mark uncertain information with "(unconfirmed)"
- Don't extrapolate or assume

## Manual Edits

You can also edit knowledge files directly without using the transcript skill:

1. Follow the existing file structure
2. Include source attribution (video ID or other reference)
3. Check for duplicates before adding

## Pull Request Guidelines

Your PR description should include:

- [ ] Video title and YouTube link
- [ ] Brief summary of knowledge added
- [ ] List of files modified
- [ ] Any areas of uncertainty

Example:
```
## Summary
Added knowledge from "Commodore 1541 Drive Repair" by 8-Bit Guy

## Changes
- Created vendor-commodore.md with 1541 repair info
- Updated tech-storage.md with floppy alignment techniques

## Video
https://youtube.com/watch?v=EXAMPLE_ID

## Notes
- Unsure about the exact capacitor value at 15:32, marked as unconfirmed
```

## Questions?

Open an issue if you have questions about:
- How to categorize certain knowledge
- Vendor naming conventions
- File structure
- Anything else!
