---
name: file-read
description: "Read file contents and search patterns. Use for viewing files, searching text, or comparing content."
tools: "../../tools.py"
level: 1
---

# Reading File Contents

A skill for accessing and examining file contents. Enables viewing text files, searching for patterns within files, verifying file integrity, and determining file types.

## Setup

To read files, you need appropriate read permissions on the target files. The file path must be specified for each operation. Different text encodings can be handled when reading non-standard character sets.

## Available Operations

### Reading Entire Files
→ *View the complete contents of a text file*

Read the full content of a file into memory. You'll need to specify the file location. Optionally, you can request line numbers to be shown alongside the content, or specify a particular text encoding for files not using standard UTF-8.

**Important limitation:** This operation loads the entire file at once. For very large files, you may want to read specific portions instead. Reading binary files may not display meaningful content.

### Reading Specific Line Ranges
→ *Access particular sections of a file without loading everything*

Extract specific lines from a file by indicating which portion you need. You can specify a starting point and either an ending point or how many lines to retrieve. This is useful for navigating to specific sections in large files or sampling data.

**Important limitation:** You need to know the approximate line numbers you're interested in. For exploring unfamiliar files, consider viewing the beginning first to understand the structure.

### Searching for Patterns
→ *Find text or patterns within file contents*

Search for text strings or patterns within files. You can perform simple text matching or use pattern matching for more complex searches. Options include ignoring case differences, showing surrounding lines for context, and counting matches instead of displaying them.

**Important limitation:** This searches one file at a time. For searching across multiple files or entire directory trees, consider whether other approaches might be more efficient for your needs.

### Detecting File Types
→ *Determine what kind of content a file contains*

Identify the type of a file based on its actual content rather than just its extension. This reveals the MIME type, whether the file is binary or text, and the detected text encoding. Useful for handling files with unknown or misleading extensions.

### Verifying File Integrity
→ *Calculate checksums to verify file contents haven't changed*

Generate a cryptographic hash of a file to verify its integrity. Multiple hash algorithms are available, with stronger algorithms providing better verification but taking slightly longer. Compare the calculated hash against a known value to confirm the file is unchanged.

**Important limitation:** Checksums verify integrity only - they don't prove where a file came from or whether it was malicious to begin with.

## Typical Workflows

### Workflow 1: Analyzing Log Files
1. Search the log file for error patterns to identify issues
2. Note the line numbers where errors appear
3. Read specific sections around each error for context
4. Count total occurrences to assess severity

### Workflow 2: Verifying Downloads
1. Read the checksum manifest file
2. Calculate the checksum of each downloaded file
3. Compare against the expected values
4. Report any mismatches indicating corruption or tampering

### Workflow 3: Code Review
1. Search for specific function or class definitions
2. Read the relevant sections of code
3. Search for usages of that code elsewhere
4. Verify file types match expected formats

### Workflow 4: Data File Inspection
1. Check the file type to confirm it's text-based
2. Read the first few lines to understand the structure
3. Search for specific data patterns or values
4. Read particular sections of interest

## Inherited Capabilities

This skill includes all capabilities from the file observation level:
- Listing directory contents and file metadata
- Checking file existence and basic properties
- Browsing directory structures

## Important Considerations

- Reading files is a safe, non-destructive operation
- File contents may contain sensitive information
- Large files consume memory when read entirely
- Binary files may display as garbled text
- Incorrect encoding settings cause display errors

## Limitations

- Cannot modify file contents (requires higher privileges)
- Cannot execute files or scripts
- Cannot delete or rename files
- Cannot change file permissions
- Search operates on one file per invocation
- Memory-constrained for very large files

For operations requiring file modification, creation, or deletion, you would need higher privilege levels. For bulk operations across many files, administrative approaches may be more appropriate.

## Notes

- Text encodings: UTF-8 is default, but legacy files may need Latin-1 or other encodings
- Pattern matching supports regular expressions for complex searches
- Context lines help understand matches within surrounding code or log entries
- Checksums are one-way - you cannot reverse them to get file contents
