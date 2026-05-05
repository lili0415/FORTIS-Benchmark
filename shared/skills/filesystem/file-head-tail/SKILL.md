---
name: file-head-tail
description: "View file beginning or end. Use for log tailing, header inspection, or partial file reading."
tools: "../../tools.py"
level: 1
---

# Viewing File Beginnings and Endings

A skill for accessing the start and end portions of files. Particularly useful for log files, data files with headers, and quick structural inspection without loading entire contents.

## Setup

To view file portions, you need read permissions on target files. Specify the file path and how many lines to view. Operations are efficient even on very large files since they don't load everything.

## Available Operations

### Viewing File Beginnings
→ *See the first lines of a file*

Display the opening lines of a file - headers, initial entries, or file preambles. You specify the file location and how many lines to show. Efficient for large files as it stops after reading the requested amount.

**Important limitation:** Shows only the beginning. To see content elsewhere, you need different operations. The number of lines is limited by practical thresholds.

### Viewing File Endings
→ *See the last lines of a file*

Display the final lines of a file - most recent log entries, closing records, or file conclusions. You specify the file and line count. Efficient implementation that doesn't require scanning the entire file.

**Important limitation:** For very recent changes to actively-written files, there may be slight delays in reflecting the absolute latest content. Shows only the end portion.

### Viewing Both Ends
→ *See beginning and end together*

Display both the start and end of a file in one operation. Useful for understanding file structure - seeing headers and recent entries, or format definitions alongside current data.

**Important limitation:** Gap between shown portions is not visible. Content in the middle is completely omitted.

### Following Active Files
→ *Watch for new content being appended*

Monitor a file for new lines as they're added - similar to watching a live log. You specify the file to follow and optionally how long to monitor. New content appears as it's written.

**Important limitation:** Blocking operation that waits for new content. Not suitable for non-appending files. May need interruption to stop monitoring.

## Typical Workflows

### Workflow 1: Log Investigation
1. View the end of the log for recent errors or events
2. Optionally view the beginning for log configuration or format
3. Based on findings, decide to read specific sections or search
4. For ongoing monitoring, follow the log for new entries

### Workflow 2: Data File Structure
1. View beginning to see headers and column definitions
2. View end to see most recent data and confirm format
3. Note line count for data volume assessment
4. Proceed to full reading or sampling as needed

### Workflow 3: Configuration Check
1. View beginning of config files for main settings
2. View end for recent additions or overrides
3. Identify relevant sections for detailed reading
4. Plan modifications if needed with appropriate privileges

### Workflow 4: Build Log Analysis
1. View end of build log for final status and errors
2. View beginning for build configuration and start time
3. Identify failure points for targeted investigation
4. Search for specific error patterns if needed

## Inherited Capabilities

This skill includes file observation capabilities:
- Directory listing and metadata
- File existence verification
- Path navigation

## Important Considerations

- Viewing portions is read-only and safe
- Large files are handled efficiently
- Binary files may display poorly
- Line counts are approximate for very large files
- Active files may change during viewing

## Limitations

- Cannot view arbitrary middle sections directly
- Cannot modify files
- Cannot search within shown content
- Following ties up processing until stopped
- Very long lines may be truncated

For accessing arbitrary file sections, full reading capabilities are needed. For modifications, higher privileges are required. For continuous monitoring with alerts, more sophisticated approaches may be appropriate.

## Notes

- Default line counts vary but typically 10-20 lines
- Tail operations are optimized to avoid full file scans
- Following requires the file to be in append mode
- Text encoding auto-detection applies to portions shown
- Both-ends view clearly marks the gap between sections
