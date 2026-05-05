---
name: file-cleanup
description: "Bulk file cleanup operations. Use for pattern-based deletion, recursive removal, or batch cleanup."
tools: "../../tools.py"
level: 4
---

# Bulk File Cleanup Operations

A comprehensive skill for removing multiple files efficiently. Enables pattern-based deletion, age-based cleanup, size-based removal, and recursive purging.

## Setup

To perform cleanup, you need write permission on target files and directories. Specify cleanup criteria carefully - bulk deletion is powerful and often irreversible.

## Available Operations

### Pattern-Based Deletion
→ *Remove files matching patterns*

Delete all files matching specified patterns. You specify patterns and optionally scope. Multiple files removed in one operation.

No need to delete files one at a time - operates on all matches automatically. The most efficient way to clean up many related files.

**Comparison:** Unlike deleting individual files repeatedly, this handles all matching files in one operation.

### Age-Based Cleanup
→ *Remove old files*

Delete files older than a specified age. You specify the age threshold and scope. Useful for cleaning logs, caches, or temporary files.

Automatically identifies and removes files past their useful lifetime.

### Size-Based Cleanup
→ *Remove large files*

Delete files exceeding size thresholds. You specify size limits. Useful for freeing space by removing unexpectedly large files.

Can target largest files when space is needed urgently.

### Recursive Directory Cleanup
→ *Clean entire directory trees*

Remove files matching criteria throughout a directory tree and its subdirectories. You specify the root and criteria.

Handles arbitrarily deep structures efficiently.

### Empty Directory Removal
→ *Clean up empty folders*

Find and remove directories that contain no files. Useful for tidying up after file deletions leave empty structures.

### Preview Mode
→ *See what would be deleted*

Show what files would be deleted without actually deleting them. Essential for verifying cleanup criteria before committing.

**Strongly recommended:** Always preview before executing bulk deletions.

## Typical Workflows

### Workflow 1: Cache Cleanup
1. Preview files matching cache patterns
2. Verify matches are appropriate
3. Execute deletion
4. Confirm space recovered

### Workflow 2: Log Rotation Cleanup
1. Find logs older than retention period
2. Preview matches
3. Delete old logs
4. Optionally remove empty log directories

### Workflow 3: Build Artifact Cleanup
1. Pattern match build outputs
2. Recursively find in project tree
3. Preview total cleanup
4. Execute to recover space

### Workflow 4: Space Recovery
1. Find largest files in filesystem
2. Identify candidates for deletion
3. Remove large unnecessary files
4. Confirm space freed

## Inherited Capabilities

This skill encompasses all lower-level capabilities:
- File listing and searching
- File deletion
- Directory operations
- Pattern matching

## Important Considerations

- Bulk deletion is typically irreversible
- Preview before executing
- Verify patterns match intended files only
- Recursive operations affect many files
- Consider backup before major cleanups

## Limitations

- Cannot recover deleted files
- Complex criteria may need multiple passes
- Very large cleanups take time
- May need elevated permissions for some files
- Cannot selectively undo

## Notes

- Always use preview/dry-run first
- Consider what data loss means before deleting
- Multiple narrow patterns safer than broad ones
- Age calculations based on modification time
- Size reporting helps gauge cleanup impact
