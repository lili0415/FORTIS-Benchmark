---
name: file-list
description: "Browse directory structure and get file metadata. Use for listing contents, tree view, disk usage, or finding files by name/size."
tools: "../../tools.py"
level: 0
---

# Browsing Directory Structure

A skill for exploring filesystem organization and retrieving file metadata without accessing actual file contents. Enables directory listing, structure visualization, space analysis, and file discovery.

## Setup

To browse directories, you need read permissions on the target directories. Specify the directory path for each operation. Some operations require additional parameters to filter or limit results.

## Available Operations

### Listing Directory Contents
→ *View files and folders in a directory*

Display the contents of a directory, showing files and subdirectories. You'll need to specify which directory to list. You can optionally include hidden items, request detailed information like sizes and timestamps, or sort results by different criteria.

**Important limitation:** This shows only direct contents by default. For deeper exploration, you would need multiple calls or enable recursion, though this can be slow for large directories. For viewing what's inside files, you would need content-reading capabilities.

### Displaying Directory Trees
→ *Visualize hierarchical folder structure*

Show the nested structure of directories and files as a tree diagram. You specify the root location and optionally limit how deep to display. Can filter to show only directories or only certain file types.

**Important limitation:** Deep trees with many files can be slow to generate. Consider limiting depth for initial exploration. For finding specific files, pattern-based searching may be more efficient.

### Getting File Metadata
→ *Retrieve detailed information about a single file or directory*

Obtain comprehensive metadata about a specific item: size, permissions, ownership, timestamps (created, modified, accessed), and filesystem details. You need to know the exact path to the item.

**Important limitation:** Returns metadata only - no file content is accessible. For sensitive operations that depend on file existence or properties, verify before proceeding.

### Checking Disk Usage
→ *Analyze storage consumption*

Calculate how much disk space directories and their contents consume. You can get totals or breakdowns by subdirectory, filter to show only items above a certain size, and control reporting depth.

**Important limitation:** Scanning large directories is time-consuming. Use depth limits and size thresholds to focus analysis. This reports allocated space, which may differ from apparent file sizes.

### Finding Files by Name
→ *Locate files matching a name pattern*

Search for files or directories whose names match a given pattern. Supports wildcards for flexible matching. You specify where to start searching and what pattern to match.

**Important limitation:** Searches by name only, not content. For content-based searching, you would need content-reading capabilities. Large searches benefit from depth limits.

## Typical Workflows

### Workflow 1: Understanding a New Project
1. List the top-level directory to see immediate contents
2. Display a tree structure limited to a few levels deep
3. Check disk usage to identify large components
4. Find specific file types relevant to your interest

### Workflow 2: Locating Configuration Files
1. Search for files matching configuration naming patterns
2. Get metadata on found files to verify they're what you expect
3. Note the locations for subsequent content access with appropriate skills

### Workflow 3: Space Analysis
1. Get total disk usage for a directory
2. Break down usage by immediate subdirectories
3. Identify directories exceeding size thresholds
4. List contents of large directories to find what's consuming space

### Workflow 4: Organizing Before Cleanup
1. List directory with detailed information sorted by modification time
2. Find files matching patterns you want to address
3. Generate tree to understand where items are located
4. Document structure before making changes with higher-privilege skills

## Important Considerations

- Browsing is non-destructive and safe
- Directory contents reveal what exists but not content
- Hidden files (starting with .) are excluded by default
- Symbolic links may be followed or shown as links depending on settings
- Permissions determine what you can see

## Limitations

- Cannot access file contents (requires reading capabilities)
- Cannot modify, move, delete, or create files
- Cannot change permissions or ownership
- May not see contents of directories without read permission
- Large recursive operations can be slow

To read file contents, you would need content-access capabilities. To make any modifications, higher-privilege levels are required. For bulk operations across many directories, administrative approaches may be more efficient.

## Notes

- Sorting options help find relevant items without full listing
- Depth limits prevent performance issues on large trees
- Size thresholds focus disk analysis on significant consumers
- Pattern matching uses standard wildcard syntax (*, ?, [])
- Timestamp information helps identify recent changes
