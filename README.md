# Retro Knowledge Base

A collaborative knowledge base for retrocomputing restoration, packaged as a Claude Code plugin.

## What's Included

- **Knowledge Base**: Curated information about vintage computer repair, organized by vendor and technique category
- **Transcript Analysis Skill**: `/retro-analyze-transcript` command to extract knowledge from YouTube video transcripts

## Installation

### For Users

```bash
# Add the marketplace
claude plugin marketplace add inbarraz/retro-knowledge-base

# Install the plugin
claude plugin install retro-knowledge-base
```

### For Contributors

```bash
# Clone the repository
git clone https://github.com/inbarraz/retro-knowledge-base
cd retro-knowledge-base

# Install locally for development
claude plugin install ./
```

## Usage

### Analyzing Transcripts

1. Download a video transcript using yt-dlp:
   ```bash
   yt-dlp --write-info-json --skip-download "https://youtube.com/watch?v=VIDEO_ID"
   ```

2. Run the analysis skill in Claude Code:
   ```
   /retro-analyze-transcript ./VIDEO_ID.info.json
   ```

3. The skill will:
   - Parse the transcript
   - Extract knowledge about platforms, repairs, and techniques
   - Present proposed changes for approval
   - Update the knowledge base files

### Browsing Knowledge

The knowledge base is organized into:

- `knowledge/retro/index.md` - Master index of processed videos
- `knowledge/retro/vendor-*.md` - Vendor-specific knowledge (76 files)
- `knowledge/retro/tech-*.md` - Technique categories (11 files):
  - `tech-crt-display.md` - CRT and monitor repair
  - `tech-diagnostics.md` - Testing and fault finding
  - `tech-storage.md` - Hard drives, floppy, SCSI
  - `tech-pcb-soldering.md` - PCB repair and soldering
  - `tech-power.md` - Power supplies and capacitors
  - `tech-cleaning.md` - Cleaning and restoration
  - `tech-peripherals.md` - Keyboards, joysticks, connectors
  - `tech-video.md` - Video capture and converters
  - `tech-memory-cpu.md` - RAM and CPU topics
  - `tech-modern-retro.md` - Modern solutions and adapters
  - `tech-misc.md` - Safety, tools, miscellaneous

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Quick Start

1. Clone and install the plugin locally
2. Download transcripts from retrocomputing YouTube videos
3. Process them with `/retro-analyze-transcript`
4. Review and commit the changes
5. Open a pull request

## License

MIT License - see [LICENSE](LICENSE) for details.
