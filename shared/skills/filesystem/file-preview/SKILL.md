---
name: file-preview
description: "Preview file contents without full read. Use for quick file inspection or header/footer viewing."
tools: "../../tools.py"
level: 1
---

# Quick File Inspection

A skill for rapidly examining files without loading complete contents. Enables peeking at file beginnings, sampling content, checking types, and making preliminary assessments before full reading.

## Setup

To preview files, you need read permission on the target files. Specify the file path and optionally how much content to sample. Previews are designed to be fast even on large files.

## Available Operations

### Peeking at File Start
→ *View the beginning of a file*

Quickly see the first portion of a file - typically enough to understand its structure or content type. You specify the file and optionally how many lines or bytes to preview. Fast operation regardless of total file size.

**Important limitation:** Shows only the beginning. For content elsewhere in the file, you would need to specify offsets or use full reading capabilities. The preview length has practical limits.

### Sampling File Content
→ *Get representative portions of a file*

Extract sample sections from a file - beginning, end, or specific regions. Useful for large files where full reading would be slow or unnecessary. You indicate which portions to sample.

**Important limitation:** Samples may miss relevant content between sampled regions. For comprehensive search, full reading or pattern matching across the file may be needed.

### Quick Type Detection
→ *Rapidly determine file type*

Examine file contents to detect the actual type, regardless of extension. Useful for validating files before processing or identifying unknown files. Returns type information without loading full content.

**Important limitation:** Type detection examines content signatures but may not be definitive for all formats. Some files may be misidentified or unrecognized.

### Size and Structure Overview
→ *Get quick statistics about file content*

Obtain rapid statistics: line count, character count, word count, encoding detection. Faster than reading entire file when you only need metrics. You specify which statistics you need.

**Important limitation:** Approximate for very large files in some cases. Encoding detection may be uncertain for short files or mixed encodings.

## Typical Workflows

### Workflow 1: Triaging Unknown Files
1. Detect file type to understand format
2. Preview beginning to see structure
3. Check size to assess reading feasibility
4. Decide whether to proceed with full reading

### Workflow 2: Log File Investigation
1. Preview end of log file for recent entries
2. Sample beginning for log format understanding
3. Check file size to estimate log volume
4. Proceed to full reading or searching if needed

### Workflow 3: Data File Assessment
1. Preview start to see header/schema
2. Sample middle portion for data characteristics
3. Get line count to understand data volume
4. Plan appropriate processing approach

### Workflow 4: Code File Reconnaissance
1. Preview start for imports and declarations
2. Detect file type to confirm language
3. Check size for complexity estimation
4. Proceed to full reading for detailed review

## Inherited Capabilities

This skill includes file observation capabilities:
- Directory listing and navigation
- File existence checking
- Basic metadata access

## Important Considerations

- Previewing is non-destructive
- Large file previews are fast (don't load everything)
- Binary file previews may show garbled content
- Encoding affects text display
- Line endings vary by platform

## Limitations

- Cannot show all content (by design)
- Cannot modify files
- Binary content may not display usefully
- Cannot search within previews
- Limited context around sampled regions

For complete content access, full reading capabilities are needed. For modifications, higher privileges are required. For comprehensive searches, pattern-matching across full content may be more appropriate.

## Notes

- Preview sizes balance usefulness versus speed
- Text encoding is auto-detected but may need hints
- Binary previews show hex representation
- Line-based previews may truncate long lines
- Sampling strategies trade coverage for speed
