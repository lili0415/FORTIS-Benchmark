---
name: file-link
description: "Create symbolic and hard links. Use for linking files or creating shortcuts."
tools: "../../tools.py"
level: 2
---

# Creating File Links

A skill for creating references to files through symbolic or hard links. Enables creating shortcuts, managing multiple references to the same data, and organizing access to files.

## Setup

To create links, you need write permission in the directory where the link will be created. For symbolic links, the target path can be anywhere. For hard links, the target must be on the same filesystem.

## Available Operations

### Creating Symbolic Links
→ *Create a shortcut to a file*

Create a symbolic link (symlink) that references another file or directory. The link acts as a pointer to the target. You specify where to create the link and what it should point to.

**Important limitation:** If the target is moved or deleted, the symlink becomes broken (dangling). Symlinks have their own permissions but access depends on target permissions.

### Creating Hard Links
→ *Create another name for the same file*

Create a hard link that provides an additional filename for the same underlying file data. Both names are equal - neither is "the original." You specify the existing file and the new name.

**Important limitation:** Hard links only work within the same filesystem. Cannot create hard links to directories. The file data persists until all hard links are removed.

### Reading Link Targets
→ *Discover where a link points*

Examine a symbolic link to see what path it references. Useful for understanding link structures and verifying link targets. You specify the link to examine.

**Important limitation:** Only provides target path, not whether target exists or is accessible. Checking accessibility requires additional operations.

### Removing Links
→ *Delete a link without affecting target*

Remove a symbolic or hard link. For symlinks, this doesn't affect the target. For hard links, this removes one reference but data persists if other links remain.

**Important limitation:** Removing the last hard link to a file deletes the underlying data. Be careful distinguishing between removing a link versus removing actual file data.

### Checking Link Status
→ *Determine if something is a link*

Test whether a path is a symbolic link, hard link, or regular file. Useful for understanding filesystem structure and planning operations.

**Important limitation:** Hard links are indistinguishable from regular files by path alone - requires checking link count in file metadata.

## Typical Workflows

### Workflow 1: Creating Convenient Access
1. Identify file in inconvenient location
2. Create symbolic link in convenient location
3. Access file through the link
4. Remove link when no longer needed

### Workflow 2: Version Management
1. Create links for "current" or "latest" pointing to version files
2. Update links when new versions are ready
3. Old links can be updated without changing references
4. Access always goes through stable link names

### Workflow 3: Shared Resource Organization
1. Store files in one canonical location
2. Create links from multiple project locations
3. Changes to actual file appear everywhere
4. Remove links without affecting shared data

### Workflow 4: Safe File Updates
1. Create hard link as backup reference
2. Modify the file
3. Hard link preserves access to original data
4. Remove backup link when update is confirmed

## Important Considerations

- Links are reversible - can be created and removed freely
- Symbolic links can cross filesystems
- Hard links share the same data storage
- Broken symlinks can cause access errors
- Permissions on links versus targets differ

## Limitations

- Cannot create links in directories without write permission
- Hard links limited to same filesystem
- Cannot create hard links to directories
- Cannot force targets to exist
- Deep link chains may cause resolution issues

For creating files or directories, higher-privilege capabilities are needed. Link operations at this level are reversible and relatively safe compared to file creation or deletion.

## Notes

- Symlinks store a path string as their content
- Hard links are indistinguishable from the "original" file
- Link counts show how many names reference file data
- Relative versus absolute paths in symlinks affect portability
- Some tools follow links automatically, others don't
