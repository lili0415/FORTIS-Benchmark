---
name: file-admin
description: "Full admin with batch and recursive operations. Use for recursive delete, chmod -R, bulk rename, or directory tree operations."
tools: "../../tools.py"
level: 4
---

# Full Filesystem Administration

The most comprehensive filesystem skill with complete administrative capabilities. Enables recursive operations, bulk modifications, batch processing, and tree-wide changes.

## Setup

Administrative operations often require elevated permissions. Specify operations carefully - these capabilities can affect thousands of files with single commands.

## Available Operations

### Recursive Deletion
→ *Remove entire directory trees*

Delete a directory and all its contents recursively. Everything beneath the specified path is removed. You specify the path to delete.

No need to remove files individually - removes entire hierarchies in one operation. The most powerful deletion capability.

**Comparison:** Unlike single-file deletion requiring many calls, this removes everything beneath a path instantly.

### Recursive Permission Changes
→ *Modify permissions across directory trees*

Change permissions on a directory and all its contents. Apply consistent permissions throughout a hierarchy.

No need to change permissions one file at a time - applies to entire trees automatically.

### Recursive Ownership Changes
→ *Transfer ownership of entire trees*

Change owner and group on directories and all contents. Useful for access control changes across large structures.

### Bulk Renaming
→ *Rename many files with patterns*

Rename multiple files according to patterns. Transform names using search-replace, numbering, or formatting rules.

Handles hundreds of files efficiently - just specify the pattern transformation.

### Find and Process
→ *Locate and act on files*

Find files matching criteria and perform operations on them. Combines searching and acting in one workflow.

More efficient than finding first, then processing separately.

### Tree Operations
→ *Copy or move entire directory structures*

Duplicate or relocate entire directory hierarchies. Preserves structure and optionally attributes.

## Typical Workflows

### Workflow 1: Project Cleanup
1. Preview recursive deletion scope
2. Verify only intended content will be removed
3. Execute recursive deletion
4. Confirm cleanup complete

### Workflow 2: Permission Repair
1. Identify permission problems in tree
2. Plan correct permission scheme
3. Apply recursive permission changes
4. Verify access is correct

### Workflow 3: Batch Rename
1. Preview rename transformations
2. Verify names will be correct
3. Execute bulk rename
4. Confirm all files renamed

### Workflow 4: Complete Migration
1. Copy entire tree to new location
2. Adjust ownership for new context
3. Adjust permissions as needed
4. Verify migration complete

## Inherited Capabilities

This skill encompasses all lower-level capabilities:
- All file reading and writing
- All directory operations
- All permission and attribute changes
- All search and pattern matching

## Important Considerations

- Operations affect potentially thousands of files
- Many operations are irreversible
- Always preview before bulk operations
- Verify scope is correct before executing
- Consider backups before major changes

## Limitations

- Cannot exceed underlying permission limits
- Cannot affect files without proper access
- Very large trees take significant time
- Interruption may leave partial state
- Some operations cannot be undone

## Notes

- Administrative power requires administrative care
- Preview modes exist for most operations
- Recursive operations descend entire hierarchies
- Bulk operations are all-or-nothing typically
- Document what changes are made for reference
