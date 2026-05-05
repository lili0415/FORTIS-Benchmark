---
name: file-copy
description: "Copy individual files. Use for single file copying with optional attribute preservation."
tools: "../../tools.py"
level: 3
---

# Copying Individual Files

A skill for creating duplicate copies of files. Enables copying files to new locations, creating backups, and duplicating content while optionally preserving attributes.

## Setup

To copy files, you need read permission on the source and write permission on the destination. Specify the source file and where to place the copy. Operations handle one file at a time.

## Available Operations

### Basic File Copy
→ *Create a copy of a file*

Duplicate a file to a new location or with a new name. You specify the source file and destination path. The original remains unchanged.

**Important limitation:** Copies one file at a time. For copying multiple files or entire directories, you would need multiple operations or bulk capabilities at higher privilege levels.

### Copy with Attribute Preservation
→ *Duplicate while keeping metadata*

Copy a file while preserving its timestamps, permissions, and ownership. Useful for creating exact duplicates including all metadata. You indicate which attributes to preserve.

**Important limitation:** Some attributes may not preserve across different filesystems. Ownership preservation may require elevated system privileges.

### Copy to New Name
→ *Duplicate with a different filename*

Create a copy with a different name, typically in the same directory. Useful for creating versions or backups. You specify the new name for the copy.

**Important limitation:** Destination must not already exist unless overwrite is intended. Same single-file limitation applies.

### Conditional Copy
→ *Copy only if conditions are met*

Copy a file only if the destination doesn't exist, or only if the source is newer than an existing destination. Prevents unnecessary overwrites.

**Important limitation:** Condition checking adds overhead. For complex conditional copying across many files, higher-privilege capabilities may be more appropriate.

## Typical Workflows

### Workflow 1: Creating Backups
1. Identify file to back up
2. Determine backup destination and naming
3. Copy file to backup location
4. Verify backup succeeded

### Workflow 2: Duplicating for Modification
1. Copy original to preserve it
2. Work with the copy
3. Compare modified copy to original if needed
4. Replace original or keep both

### Workflow 3: Distributing Files
1. Identify file to distribute
2. Copy to first destination
3. Repeat for additional destinations
4. Verify all copies complete

### Workflow 4: Version Creation
1. Copy current file with version suffix
2. Continue work on original
3. Accumulate versions as needed
4. Clean up old versions when appropriate

## Inherited Capabilities

This skill includes lower-level capabilities:
- Reading file contents
- Viewing file metadata
- Directory browsing

## Important Considerations

- Copying creates new storage usage
- Large files take time to copy
- Destination space must be sufficient
- Overwrites may be permanent
- Interrupted copies may leave partial files

## Limitations

- Cannot copy multiple files at once
- Cannot copy directories (files only)
- Cannot create destination directories
- Cannot perform pattern-based copying
- No built-in compression or transformation

For copying directories, multiple files, or pattern-based operations, higher-privilege capabilities are needed. For creating destination directories, file creation privileges are required.

## Notes

- Copy preserves content exactly
- Metadata preservation depends on options and filesystem
- Cross-filesystem copying always works but may be slower
- Space is consumed at destination
- Symbolic links may be followed or copied as links
