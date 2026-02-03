---
name: retro-analyze-transcript
description: Analyze a YouTube video transcript about retrocomputing restoration and extract knowledge into organized markdown files
arguments:
  - name: path
    description: Path to JSON file(s) or directory containing transcript JSON files
    required: true
allowed_tools:
  - Read
  - Write
  - Edit
  - Glob
  - Bash
  - AskUserQuestion
---

<objective>
Analyze the provided YouTube video transcript about retrocomputing restoration. Extract knowledge about platforms, repair techniques, and vendors. Store the knowledge in organized markdown files within the plugin's knowledge directory, reading existing knowledge first to make incremental updates only.
</objective>

<plugin_path_resolution>
The knowledge base lives within this plugin. To find it:
1. Use Glob to find the index file: `**/retro-knowledge-base/knowledge/retro/index.md`
2. Extract the base path from the result (everything up to and including `knowledge/retro/`)
3. Use that path for all subsequent file operations

**IMPORTANT**: At the start of processing (in step_0), you MUST:
1. Run: `Glob("**/retro-knowledge-base/knowledge/retro/index.md")`
2. Extract the knowledge base path from the result
3. Store this path and use it for ALL file operations

Example: If Glob returns `/Users/someone/retro-knowledge-base/knowledge/retro/index.md`,
then the knowledge base path is `/Users/someone/retro-knowledge-base/knowledge/retro/`
</plugin_path_resolution>

<input>
Read the JSON file at: $ARGUMENTS

The JSON contains:
- `id`: Video ID (use for source attribution)
- `title`: Video title
- `description`: Full description (often contains tool links)
- `channel`: Channel name
- `upload_date`: YYYYMMDD format
- `webpage_url`: Full YouTube URL
- `transcript`: The full transcript text
</input>

<workflow>

<step_0_resolve_input>
**First: Resolve the plugin knowledge base path**

1. Use Glob to find the knowledge base:
   ```
   Glob("**/retro-knowledge-base/knowledge/retro/index.md")
   ```
2. Extract the directory path from the result (remove `index.md` from the path)
3. Store this as `KNOWLEDGE_PATH` - use this for ALL subsequent file operations

**Then: Determine input type and build file list**

1. Check if $ARGUMENTS is a directory:
   - If yes: Use Glob to find all `*.json` files in that directory
   - Sort files by name for consistent ordering

2. Check if $ARGUMENTS contains multiple paths (space-separated):
   - If yes: Split into individual file paths

3. Otherwise: Treat as single file path

4. **CRITICAL**: Convert ALL paths to absolute paths (resolve any relative paths)

Make sure every item in the list is a complete, absolute filepath.

**Persist the file list to scratchpad** (prevents loss during context compaction):
Write the resolved file list to `{KNOWLEDGE_PATH}/.processing-queue.json`:
```json
{
  "knowledge_path": "/path/to/retro-knowledge-base/knowledge/retro/",
  "files": ["/absolute/path/to/file1.json", "/absolute/path/to/file2.json"],
  "total": N,
  "current_index": 0,
  "success_count": 0,
  "skipped_count": 0,
  "failed_count": 0
}
```

Report:
```
Found knowledge base at: {KNOWLEDGE_PATH}
Found {N} transcript file(s) to process:
- file1.json
- file2.json
...
Processing queue saved.
```

If no JSON files found, report error and stop.
</step_0_resolve_input>

<serial_processing>
Process each file completely and independently, one at a time.

**CRITICAL: Read from scratchpad at EACH iteration** to ensure file paths survive context compaction:

For each file iteration:
1. **Read the processing queue**: Use Glob to find `**/retro-knowledge-base/knowledge/retro/.processing-queue.json`, then read it
2. **Get current file**: Extract `files[current_index]` - this is the absolute path to process
3. **Get knowledge path**: Extract `knowledge_path` from the queue file
4. Report progress: "Processing file {current_index + 1}/{total}: {filename}"
5. Execute steps 1-8 COMPLETELY for this file
6. **Update scratchpad after completion**:
   - Increment `current_index`
   - Update the appropriate counter (`success_count`, `skipped_count`, or `failed_count`)
   - Write the updated JSON back to the scratchpad file
7. **Check if more files remain**: If `current_index < total`, continue to next iteration
8. Move to next file only after current file is fully complete AND scratchpad is updated

Handle errors gracefully:
- If a file fails to parse, report error, increment failed_count in scratchpad, and continue to next
- Each file is independent - one failure does not affect others
- If scratchpad file is missing mid-processing, report error and stop (data integrity issue)
</serial_processing>

<step_1_read_input>
Read the JSON file provided as argument. Parse and extract:
- Video ID for source attribution
- Title for the index
- Description for tool/link extraction
- Transcript for knowledge extraction
</step_1_read_input>

<step_1b_check_duplicate>
Check if this video has already been processed:

1. Read `{KNOWLEDGE_PATH}/index.md` if it exists
2. Search for the video ID in the "Processed Videos" table (first column)
3. If the video ID is found:
   - Use AskUserQuestion:
     - header: "Already processed"
     - question: "Video '{title}' ({video_id}) has already been processed. Re-analyze and update the knowledge base?"
     - options:
       - "Re-process" - Analyze again and merge new knowledge
       - "Skip" - Keep existing knowledge, don't re-process
   - If user selects "Skip": Stop processing and report "Skipped - video already processed"
   - If user selects "Re-process": Continue to step_2
4. If index.md doesn't exist or video ID not found: Continue to step_2
</step_1b_check_duplicate>

<step_2_check_existing_knowledge>
Check for existing knowledge files at `{KNOWLEDGE_PATH}`:

1. Use Glob to find all existing files: `{KNOWLEDGE_PATH}/*.md`
2. Read `index.md` if it exists - check if this video was already processed
3. Use Glob to find all technique category files: `{KNOWLEDGE_PATH}/tech-*.md`
4. Read relevant category files based on video content keywords (see Category Routing table in step_4)
5. Read any `vendor-*.md` files that exist
6. Check `.preferences` file for approval settings

If the directory doesn't exist, create it:
```bash
mkdir -p {KNOWLEDGE_PATH}
```

**Technique Category Files:**
- `tech-crt-display.md` - CRT, monitors, display issues
- `tech-diagnostics.md` - Testing, measurement, fault finding
- `tech-storage.md` - Hard drives, floppy, SCSI
- `tech-pcb-soldering.md` - PCB repair, soldering, wire work
- `tech-power.md` - Power supplies, capacitors, electrical
- `tech-cleaning.md` - Cleaning, restoration, maintenance
- `tech-peripherals.md` - Keyboards, joysticks, connectors
- `tech-video.md` - Video capture, converters, RGB mods
- `tech-memory-cpu.md` - RAM, CPU, overclocking
- `tech-modern-retro.md` - Modern solutions, adapters, upgrades
- `tech-misc.md` - Safety, tools, miscellaneous
</step_2_check_existing_knowledge>

<step_3_analyze_transcript>
Thoroughly analyze the transcript and description to extract:

**Platforms/Models**:
- Computer systems (Commodore 64, Apple II, IBM PC, etc.)
- Monitors (CGA, EGA, VGA monitors, specific models)
- Peripherals (disk drives, printers, modems)
- Note the vendor for each

**Faults & Symptoms**:
- What problems were encountered
- Visual symptoms (dim screen, no display, distortion)
- Behavioral symptoms (won't boot, crashes, errors)
- Component failures (capacitors, chips, connectors)

**Diagnostic Techniques**:
- Tools used (oscilloscope, logic probe, multimeter)
- Test procedures performed
- What signals or values were measured
- How the problem was identified

**Repair Techniques**:
- What was done to fix the problem
- Component replacements
- Adjustments made
- Cleaning procedures

**Tools & Equipment**:
- Specific tool names and models mentioned
- Purchase links from the description
- How each tool was used

**Safety Information**:
- High voltage warnings
- Proper discharge procedures
- Safety equipment mentioned
</step_3_analyze_transcript>

<step_4_compute_changes>
Compare extracted knowledge against existing files:

For each piece of extracted knowledge:
1. Check if it already exists in the relevant file
2. If NEW: mark for addition
3. If EXISTING but with new details: mark for update
4. If DUPLICATE: skip

### Technique Category Routing
Route extracted techniques to appropriate category file:

| Keywords in technique | Target file |
|----------------------|-------------|
| CRT, monitor, display, screen, phosphor, flyback, yoke | tech-crt-display.md |
| diagnos*, test, measure, probe, oscilloscope, multimeter | tech-diagnostics.md |
| hard drive, floppy, disk, SCSI, storage | tech-storage.md |
| solder, PCB, trace, corrosion, wire wrap | tech-pcb-soldering.md |
| power supply, capacitor, voltage, RIFA | tech-power.md |
| clean, IPA, restoration, retrobright | tech-cleaning.md |
| keyboard, joystick, connector, cable, DIN | tech-peripherals.md |
| video capture, RGB, SCART, scan converter | tech-video.md |
| RAM, memory, CPU, overclock | tech-memory-cpu.md |
| modern, adapter, upgrade, XT-IDE, LCD | tech-modern-retro.md |
| safety, general, tool, miscellaneous | tech-misc.md |

If technique doesn't clearly match a category, use tech-misc.md

Group changes by file:
- New vendor files to create
- Existing vendor files to update
- Additions to technique category files (tech-*.md) - grouped by target category
- New entry for index.md
</step_4_compute_changes>

<step_5_present_summary>
Present a summary of proposed changes to the user:

```
## Proposed Changes for video: {title}

### New Files to Create:
- vendor-{name}.md: {brief description}

### Files to Update:
- vendor-{name}.md:
  - Adding model: {model}
  - Adding {N} diagnostic notes
  - Adding {N} repair techniques

- tech-{category}.md:
  - Adding {technique}

- index.md:
  - Adding video entry

### Knowledge Summary:
- Vendors covered: {list}
- Models mentioned: {list}
- Key techniques: {list}
- Technique categories affected: {list of tech-*.md files}
```
</step_5_present_summary>

<step_6_get_approval>
Check approval conditions:

1. Check `{KNOWLEDGE_PATH}/.preferences` for approval settings
2. If approval is disabled in preferences: Apply changes immediately

Otherwise, use AskUserQuestion (same options for every file):
- header: "Apply changes"
- question: "Apply these changes to the knowledge base?"
- options:
  - "Apply all changes" - Write all proposed changes now
  - "Review each change" - Show me each change before applying
  - "Skip this video" - Don't make any changes
  - "Always apply (disable prompts)" - Apply now and skip prompts for future videos

If "Always apply" selected, write to `{KNOWLEDGE_PATH}/.preferences`:
```
approval_required: false
```

If "Review each change" selected, present each change individually with approve/skip options.
</step_6_get_approval>

<step_7_apply_changes>
Apply the approved changes:

**For new vendor files** - Use Write tool:
Follow the vendor file template below.

**For existing vendor files** - Use Edit tool:
Add new sections or append to existing sections.

**For technique files** - Use Edit tool on appropriate tech-*.md file:
1. Identify target category using the routing table in step_4
2. Read the target category file if not already loaded
3. Use Edit tool to add new techniques under appropriate sections
4. Technique files follow existing category file structure

**For index.md** - Use Edit tool (or Write if new):
Add video to the processed list and update statistics.

Always include source attribution: `- Source: [{video_id}]`
</step_7_apply_changes>

<step_8_confirm_completion>
Report what was written/updated:

```
## Changes Applied

- Created: vendor-{name}.md
- Updated: tech-{category}.md (added {N} techniques)
- Updated: index.md

Knowledge base now contains:
- {N} vendors
- {N} total videos processed
```

When processing multiple files, keep this summary brief (1-2 lines) to avoid output clutter.
</step_8_confirm_completion>

<step_9_final_summary>
After ALL files have been processed (only when processing multiple files):

1. **Read final counts from scratchpad**: Use Glob to find and read `**/retro-knowledge-base/knowledge/retro/.processing-queue.json` to get final `success_count`, `skipped_count`, `failed_count`

2. **Report summary**:
```
## Processing Complete

Processed {success_count} of {total_files} files successfully.
Skipped: {skipped_count}
Failed: {failed_count}
```
Only show Skipped/Failed lines if count > 0.

3. **Cleanup scratchpad**: Delete the processing queue file:
```bash
rm -f {KNOWLEDGE_PATH}/.processing-queue.json
```
Report: "Cleaned up processing queue."
</step_9_final_summary>

</workflow>

<file_templates>

<vendor_file_template>
# {Vendor Name}

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| {Model} | {Category} | [{video_id}] |

## Platform-Specific Knowledge

### {Model Name}

#### Common Faults
- {fault description} - Source: [{video_id}]

#### Diagnostic Approaches
- {diagnostic technique} - Source: [{video_id}]

#### Repair Techniques
- {repair description} - Source: [{video_id}]

#### Tools & Equipment
- {tool name}: {purpose/usage} - Source: [{video_id}]

#### Aftermarket/Replacement Parts
- {part description} - Source: [{video_id}]
</vendor_file_template>

<technique_files_note>
**Note:** Technique files (tech-*.md) follow their existing category file structure.
Each category file has its own organization - read the target file before editing
to understand its section structure and add new techniques in the appropriate location.

Do NOT create new technique category files - use only the existing 11 category files:
- tech-crt-display.md, tech-diagnostics.md, tech-storage.md, tech-pcb-soldering.md
- tech-power.md, tech-cleaning.md, tech-peripherals.md, tech-video.md
- tech-memory-cpu.md, tech-modern-retro.md, tech-misc.md
</technique_files_note>

<index_file_template>
# Retro Knowledge Base Index

## Processed Videos
| Video ID | Title | Date | Vendors | Key Topics |
|----------|-------|------|---------|------------|
| {id} | {title} | {date} | {vendors} | {topics} |

## Statistics
- Total videos processed: {N}
- Vendors covered: {list}
- Last updated: {date}
</index_file_template>

</file_templates>

<vendor_identification>
Common vendors to identify (map variations to canonical names):

- **Commodore**: C64, C128, VIC-20, Amiga, PET, Plus/4, C16
- **Apple**: Apple II, IIe, IIc, IIgs, Macintosh, Lisa, Mac SE, SE/30
- **IBM**: PC, PCjr, XT, AT, PS/2, PC Junior
- **Amstrad**: CPC 464, 664, 6128, PCW
- **Sinclair**: ZX80, ZX81, ZX Spectrum, QL
- **Atari**: 400, 800, 800XL, 1200XL, ST, Falcon
- **Tandy/Radio Shack**: TRS-80, Color Computer, CoCo
- **Mitsubishi**: Monitors (often OEM for other brands)
- **Texas Instruments**: TI-99/4A
- **Coleco**: Adam, ColecoVision
- **MSX**: Various manufacturers

When a model is mentioned, identify its vendor and create/update the appropriate vendor file.
</vendor_identification>

<critical_rules>
1. **ALWAYS read existing files first** - Never overwrite knowledge
2. **ALWAYS include source attribution** - Every fact needs `- Source: [{video_id}]`
3. **NEVER duplicate information** - Check before adding
4. **Preserve existing structure** - When editing, maintain the file's organization
5. **Use Edit for existing files** - Don't rewrite entire files with Write
</critical_rules>

<success_criteria>
**Per-file processing:**
- Video transcript fully analyzed
- All relevant knowledge extracted and categorized
- Changes presented to user for approval (unless disabled)
- Knowledge files created/updated with proper attribution
- Index updated with video entry
- No existing knowledge lost or duplicated

**Multiple files (serial processing):**
- File list persisted to scratchpad JSON at start
- Scratchpad re-read at each iteration (survives context compaction)
- Each file processed completely before moving to next
- Failed files reported with clear error reasons
- Progress reported during processing (file X of Y)
- Each file gets independent approval prompt (no shortcuts)
- Summary provided at end showing success/skip/fail counts
- Graceful error handling - one file's failure doesn't stop the rest
- Scratchpad file cleaned up after all processing completes
</success_criteria>
