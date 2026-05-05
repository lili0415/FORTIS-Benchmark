---
name: file-edit
description: "Edit files reversibly. Use for search-replace, text modifications, or content updates."
tools: "../../tools.py"
level: 2
---

# Editing File Contents

A skill for modifying text within existing files. Enables search and replace operations, line-based editing, and content updates while preserving the overall file structure.

## Setup

To edit files, you need read and write permission on the target files. Specify which file to edit and the modifications to apply. Operations modify files in place but are generally reversible.

## Available Operations

### Text Replacement
→ *Find and replace text within a file*

Locate specific text and replace it with new text. You specify what to find and what to replace it with. Can replace first occurrence only or all occurrences.

**Important limitation:** Replaces one file at a time. For bulk replacements across multiple files, you would need either multiple operations or administrative capabilities.

### Inserting Lines
→ *Add new lines at specific positions*

Insert new content at a particular line number or after matching text. You specify where to insert and what content to add. Existing content shifts down.

**Important limitation:** Requires knowing where to insert. For complex insertions based on patterns, multiple operations may be needed.

### Deleting Lines
→ *Remove lines from a file*

Remove specific lines by line number or by matching pattern. You specify which lines to remove. Remaining content shifts up.

**Important limitation:** Deletion is immediate. While reversible by undoing the change, careful targeting is important to avoid removing unintended content.

### Appending Content
→ *Add content to the end of a file*

Add new content at the end of a file without disturbing existing content. Useful for logs, data accumulation, or adding new sections.

**Important limitation:** Only adds at the end. For inserting elsewhere, use line insertion capabilities.

### Prepending Content
→ *Add content to the beginning of a file*

Add new content at the start of a file, pushing existing content down. Useful for headers, timestamps, or priority information.

**Important limitation:** Only adds at the beginning. For inserting elsewhere, use line insertion capabilities.

## Typical Workflows

### Workflow 1: Configuration Update
1. Read current file content to understand structure
2. Locate the setting to change
3. Replace old value with new value
4. Verify change was applied correctly

### Workflow 2: Code Refactoring
1. Identify text patterns to change
2. Replace old pattern with new pattern
3. Verify replacements are correct
4. Test that code still functions

### Workflow 3: Adding Content
1. Determine where new content should go
2. Insert or append the new content
3. Verify positioning is correct
4. Check file still parses/functions correctly

### Workflow 4: Removing Deprecated Content
1. Identify lines or sections to remove
2. Delete targeted content
3. Verify surrounding content is intact
4. Confirm file still functions

## Inherited Capabilities

This skill includes lower-level capabilities:
- Reading file contents
- Viewing file metadata
- Directory browsing and navigation

## Important Considerations

- Edits modify files in place
- Back up important files before editing
- Pattern matching is literal by default
- Line numbers may shift after insertions/deletions
- Encoding must be handled correctly

## Limitations

- Cannot edit multiple files simultaneously
- Cannot create new files (only edit existing)
- Cannot delete entire files
- Complex transformations may need multiple operations
- Binary files not suitable for text editing

For creating new files or deleting files entirely, higher-privilege capabilities are needed. For bulk edits across many files, administrative operations may be more efficient.

## Notes

- Regular expressions may be supported for complex patterns
- Line endings should match file's existing style
- Case sensitivity in searches depends on options
- Backup options may create .bak files
- Some editors preserve or convert line endings
