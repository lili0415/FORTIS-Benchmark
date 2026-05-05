---
name: file-write
description: "Create and delete individual files. Use for writing new files, removing single files, or creating directories."
tools: "../../tools.py"
level: 3
---

# Creating and Deleting Files

A skill for bringing new files into existence and removing existing files. Enables creating new files with content, creating empty files, and deleting individual files.

## Setup

To create files, you need write permission in the target directory. To delete files, you need write permission on the file and containing directory. Operations affect one file at a time.

## Available Operations

### Creating Files with Content
→ *Write a new file with specified content*

Create a new file containing the content you provide. You specify the file path and the content to write. If a file already exists at that path, behavior depends on options.

**Important limitation:** Creates one file at a time. For generating multiple files, you would need multiple operations. Overwriting existing files may be permanent.

### Creating Empty Files
→ *Make a file that exists but has no content*

Create a new empty file at the specified location. Similar to "touch" but specifically for new files. Useful for placeholders or markers.

**Important limitation:** If file already exists, may update timestamp instead of failing. Cannot create in directories without write permission.

### Deleting Single Files
→ *Remove a file permanently*

Delete a specific file from the filesystem. The file is removed and its storage freed. You specify which file to delete.

**Important limitation:** Deletion is typically permanent - there is no recycle bin or undo. Deletes one file at a time only.

### Creating Directories
→ *Make new folders*

Create a new directory at the specified location. Can optionally create parent directories if they don't exist. You specify the directory path.

**Important limitation:** Cannot create directories in locations without write permission. Creating deeply nested paths may require parent creation.

### Removing Empty Directories
→ *Delete folders with no contents*

Remove a directory that is empty. The directory must contain no files or subdirectories. You specify which directory to remove.

**Important limitation:** Cannot remove directories that contain anything. For recursive deletion, administrative capabilities are needed.

## Typical Workflows

### Workflow 1: Project Initialization
1. Create project directory
2. Create necessary subdirectories
3. Create initial files with content
4. Verify structure is complete

### Workflow 2: File Generation
1. Determine content to generate
2. Create file with that content
3. Verify file was created correctly
4. Set appropriate permissions if needed

### Workflow 3: File Cleanup
1. Identify file to remove
2. Verify it's the correct file
3. Delete the file
4. Confirm deletion succeeded

### Workflow 4: Directory Organization
1. Create new organizational directories
2. Move files into appropriate directories
3. Remove now-empty directories
4. Verify new structure

## Inherited Capabilities

This skill includes lower-level capabilities:
- Reading file contents
- Editing file contents
- Viewing file metadata
- Directory browsing

## Important Considerations

- File creation consumes storage space
- Deletion is typically irreversible
- Overwriting loses previous content
- Directory creation affects organization
- Permissions apply to creation location

## Limitations

- Cannot create multiple files at once
- Cannot delete directories with contents
- Cannot recover deleted files
- Cannot create files in protected directories
- No bulk operations

For recursive deletion, bulk file operations, or administrative tasks, higher-privilege capabilities are needed.

## Notes

- File content can be any text
- Binary file creation may need special handling
- New files inherit default permissions
- Directory paths use platform-specific separators
- Relative vs absolute paths affect location
