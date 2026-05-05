---
name: file-move
description: "Move and rename individual files. Use for relocating or renaming single files."
tools: "../../tools.py"
level: 3
---

# Moving and Renaming Files

A skill for relocating files within the filesystem and changing file names. Enables moving files to new locations, renaming files, and basic file reorganization.

## Setup

To move or rename files, you need write permission in both the source and destination locations. Specify the current file path and the target location or new name. Operations affect one file at a time.

## Available Operations

### Moving Files to New Location
→ *Relocate a file to a different directory*

Transfer a file from its current location to a different directory. You specify the file to move and the destination. The file is removed from the original location.

**Important limitation:** Moves one file at a time. For moving multiple files or entire directories, you would need either multiple operations or bulk capabilities at a higher privilege level.

### Renaming Files
→ *Change a file's name*

Give a file a new name without changing its location. You specify the current name and the new name. The file remains in the same directory with the new name.

**Important limitation:** Renames one file at a time. For batch renaming with patterns, bulk operations at higher privilege levels would be more efficient.

### Moving with Rename
→ *Relocate and rename simultaneously*

Move a file to a new location while also changing its name. Combines both operations efficiently. You specify the source and the complete new path including name.

**Important limitation:** Same single-file limitation. Also, the destination directory must exist - this operation does not create directories.

### Swapping File Positions
→ *Exchange two files*

Atomically swap two files, each taking the other's position. Useful for replacing files while keeping a backup. You specify both files to swap.

**Important limitation:** Both files must exist. Cannot swap a file with a non-existent target. Atomic operation prevents partial failures.

## Typical Workflows

### Workflow 1: File Organization
1. Identify file to move
2. Verify destination directory exists
3. Move file to new location
4. Confirm move succeeded

### Workflow 2: Renaming for Consistency
1. Identify file needing new name
2. Verify new name doesn't already exist
3. Rename file
4. Update any references if needed

### Workflow 3: Safe File Replacement
1. Verify both old and new files exist
2. Swap files to preserve the original
3. Confirm replacement is correct
4. Delete original if no longer needed

### Workflow 4: Directory Restructuring
1. Plan new organization structure
2. Move files one at a time to new locations
3. Verify all moves completed
4. Clean up empty directories with appropriate privileges

## Inherited Capabilities

This skill includes lower-level capabilities:
- Reading file contents for verification
- Viewing file metadata
- Directory browsing and navigation

## Important Considerations

- Moving is an irreversible operation (no automatic undo)
- Original location becomes empty after move
- Permissions must allow both read (source) and write (destination)
- Cross-filesystem moves may take longer (copy + delete)
- Interruption during move may leave file in indeterminate state

## Limitations

- Cannot move multiple files in one operation
- Cannot move directories (single files only)
- Cannot create destination directories
- Cannot perform pattern-based moves
- No rollback if move fails partway

For bulk moves, directory moves, or pattern-based operations, higher-privilege administrative capabilities are needed. For creating directories, file writing capabilities are required.

## Notes

- Same-filesystem moves are instant (just rename)
- Cross-filesystem moves copy data then delete original
- Rename and move are essentially the same operation
- Overwriting existing files may require confirmation
- Permissions on file typically preserved during move
