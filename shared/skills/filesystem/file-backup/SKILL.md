---
name: file-backup
description: "Backup individual files. Use for creating file copies before modifications."
tools: "../../tools.py"
level: 3
---

# Backing Up Individual Files

A skill for creating safety copies of files before modifications. Enables pre-edit backups, versioned copies, and restoration from backups.

## Setup

To create backups, you need read permission on source files and write permission in the backup location. Specify which file to back up and where to store the backup.

## Available Operations

### Creating Backups
→ *Make a safety copy before changes*

Copy a file to a backup location or with a backup name. You specify the file to back up and optionally the backup naming or location.

**Important limitation:** Backs up one file at a time. For backing up multiple files or directories, you would need multiple operations or administrative capabilities.

### Restoring from Backups
→ *Replace current file with backup version*

Copy a backup file back to the original location, replacing the current version. You specify the backup to restore and where to restore it.

**Important limitation:** Restoring overwrites the current file. If you need to keep both versions, use copy instead of restore.

### Listing Backups
→ *See what backups exist*

List backup files matching naming patterns or in backup locations. Useful for finding which versions are available for restoration.

**Important limitation:** Only shows files matching backup patterns. Backups with non-standard names may not be discovered.

### Rotating Backups
→ *Manage backup versions*

Keep a certain number of backup versions, removing older ones. You specify how many versions to retain. Helps manage backup storage.

**Important limitation:** Rotation permanently deletes older backups. Ensure retention count meets your needs before enabling rotation.

## Typical Workflows

### Workflow 1: Pre-Edit Backup
1. Identify file about to be modified
2. Create backup with timestamp or version suffix
3. Proceed with modifications
4. Restore from backup if needed

### Workflow 2: Periodic Backups
1. Create backup of important file
2. Continue working
3. Create additional backups at milestones
4. Rotate old backups when storage is limited

### Workflow 3: Restoration
1. List available backups
2. Identify correct version to restore
3. Restore backup to original location
4. Verify restoration is correct

### Workflow 4: Version Management
1. Create versioned backups over time
2. List versions when needing reference
3. Restore specific version if needed
4. Clean up old versions periodically

## Inherited Capabilities

This skill includes lower-level capabilities:
- Reading file contents
- Copying files
- Directory operations
- File listing

## Important Considerations

- Backups consume storage space
- Backup naming should be consistent
- Restoration overwrites current files
- Rotation permanently removes old versions
- Backup location should be on safe storage

## Limitations

- Cannot backup multiple files at once
- Cannot backup entire directories
- Cannot compress backups
- No incremental backups
- No automated scheduling

For directory backups, compressed archives, or bulk operations, higher-privilege capabilities are needed.

## Notes

- Common naming: filename.bak, filename.YYYYMMDD
- Backup location ideally differs from original
- Verify backups are complete after creation
- Test restoration before relying on backups
- Consider backup retention policy
