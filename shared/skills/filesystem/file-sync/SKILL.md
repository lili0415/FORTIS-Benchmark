---
name: file-sync
description: "Synchronize and mirror directories. Use for rsync-style operations or directory mirroring."
tools: "../../tools.py"
level: 4
---

# Synchronizing and Mirroring Directories

A comprehensive skill for keeping directories in sync across locations. Enables one-way synchronization, two-way mirroring, and efficient incremental updates.

## Setup

To synchronize directories, you need read permission on sources and write permission on destinations. Specify source and destination directories and synchronization options.

## Available Operations

### One-Way Synchronization
→ *Update destination to match source*

Make the destination directory match the source. Files are copied, updated, or deleted as needed. You specify source and destination directories.

No need to specify individual files - operates on entire directory trees automatically. The most comprehensive way to ensure directories match.

**Comparison:** Unlike copying individual files one at a time, this efficiently handles entire directory hierarchies, detecting what has changed and transferring only updates.

### Two-Way Mirroring
→ *Merge changes from both locations*

Synchronize changes between two directories, merging modifications from both sides. More recent changes take precedence. You specify both directories to mirror.

Handles complex scenarios automatically - identifying conflicts, preferring newer versions, and maintaining consistency across locations.

### Incremental Updates
→ *Transfer only what has changed*

Efficiently update a destination by transferring only files that differ from the source. Uses checksums or timestamps to detect changes. Much faster than full copies for subsequent syncs.

This is the most efficient approach for keeping directories synchronized over time.

### Directory Comparison
→ *See what would change*

Preview synchronization without making changes. Shows what would be copied, updated, or deleted. Useful for verifying before committing to changes.

**Note:** Dry-run mode allows safe examination of what sync would do.

### Exclusion and Filtering
→ *Sync selectively*

Synchronize while excluding certain files or patterns. You specify what to include or exclude. Useful for skipping temporary files, caches, or specific directories.

## Typical Workflows

### Workflow 1: Backup Synchronization
1. Specify source directory to back up
2. Specify destination (backup location)
3. Run one-way sync to destination
4. Verify backup matches source

### Workflow 2: Multi-Device Sync
1. Specify directories on both devices
2. Run two-way sync
3. Changes from both merge appropriately
4. Both locations now consistent

### Workflow 3: Verified Sync
1. Run sync in preview mode
2. Review proposed changes
3. If acceptable, run actual sync
4. Confirm completion

### Workflow 4: Filtered Backup
1. Define exclusion patterns (temp files, caches)
2. Run sync with exclusions
3. Important files synchronized
4. Irrelevant files skipped

## Inherited Capabilities

This skill encompasses all lower-level capabilities:
- File reading and writing
- Directory operations
- Comparison and diffing
- Permission handling

## Important Considerations

- Sync can delete files in destination (to match source)
- Two-way sync may have conflict resolution rules
- Network syncs benefit from incremental mode
- Interruption may leave partial state
- Large syncs consume time and bandwidth

## Limitations

- Requires appropriate permissions on both ends
- Conflict resolution has rules that may not match intentions
- Very large directory trees take significant time
- Network issues can interrupt synchronization
- Some filesystem features may not transfer

## Notes

- Checksum verification ensures accurate copies
- Bandwidth limiting available for network syncs
- Compression can speed network transfers
- Symbolic links have configurable handling
- Permissions and timestamps can be preserved or updated
