---
name: file-archive
description: "Create and extract compressed archives. Use for tar, zip, or compression operations."
tools: "../../tools.py"
level: 4
---

# Creating and Extracting Archives

A comprehensive skill for working with compressed archives. Enables creating archives from files and directories, extracting archive contents, and managing archive members.

## Setup

To create archives, you need read permission on source files and write permission for the archive location. To extract, you need read permission on archives and write permission on extraction destination.

## Available Operations

### Creating Archives
→ *Bundle files into a compressed archive*

Combine multiple files and directories into a single archive file, optionally with compression. You specify what to include and the archive name. Supports various formats.

No need to specify individual compression settings - appropriate defaults based on format. The most comprehensive way to package files for storage or transfer.

**Comparison:** Unlike copying files individually, this creates a single portable package that preserves directory structure and can be compressed to save space.

### Extracting Archives
→ *Unpack archive contents*

Extract all contents from an archive to a destination directory. You specify the archive and where to extract. Directory structure is recreated.

Handles various formats automatically - just provide the archive and destination.

### Listing Archive Contents
→ *See what's in an archive without extracting*

View the files and directories contained in an archive. Shows names, sizes, and dates without extracting anything. Useful for verification before extraction.

### Adding to Archives
→ *Include additional files in existing archives*

Add new files to an existing archive. You specify the archive and files to add. Updates the archive to include new content.

**Note:** Not all formats support adding to existing archives efficiently.

### Extracting Specific Files
→ *Unpack only certain files*

Extract specific files from an archive rather than everything. You specify which files to extract. Useful for retrieving particular items from large archives.

### Compression Operations
→ *Compress or decompress individual files*

Apply compression to single files or decompress compressed files. Various compression algorithms available with different speed/size tradeoffs.

## Typical Workflows

### Workflow 1: Creating Distribution Package
1. Gather files to distribute
2. Create archive with appropriate format
3. Verify archive contents
4. Distribute the single archive file

### Workflow 2: Extracting Received Archive
1. Examine archive contents first
2. Extract to appropriate destination
3. Verify extracted files
4. Use extracted contents

### Workflow 3: Backup Archive
1. Select directories to archive
2. Create compressed archive with date suffix
3. Verify archive integrity
4. Store archive in backup location

### Workflow 4: Selective Extraction
1. List archive contents to find target files
2. Extract only needed files
3. Verify extracted files
4. Use without extracting entire archive

## Inherited Capabilities

This skill encompasses all lower-level capabilities:
- File reading and writing
- Directory operations
- File organization

## Important Considerations

- Archives consume storage space
- Compression adds processing time
- Extraction may overwrite existing files
- Some formats have size or path limitations
- Archive corruption may lose all contents

## Limitations

- Very large archives take significant time
- Some formats have format-specific limitations
- Password protection varies by format
- Not all formats support all features
- Corruption can affect entire archive

## Notes

- Common formats: zip (portable), tar.gz (Unix), 7z (high compression)
- Compression ratio depends on content type
- Text compresses well, already-compressed media doesn't
- Verify archives after creation
- Store archives safely - corruption affects all contents
