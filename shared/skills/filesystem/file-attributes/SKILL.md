---
name: file-attributes
description: "Manage permissions and ownership. Use for chmod or chown on single files."
tools: "../../tools.py"
level: 2
---

# Managing File Permissions and Ownership

A skill for controlling access to files through permission and ownership settings. Enables modifying who can read, write, and execute files on a single-file basis.

## Setup

To modify permissions, you typically need ownership of the file or administrative privileges. To change ownership, administrative privileges are usually required. Operations affect one file at a time.

## Available Operations

### Changing File Permissions
→ *Control who can access a file*

Modify the read, write, and execute permissions for a file. Permissions can be set for the owner, group, and others. You specify the file and the desired permission settings.

**Important limitation:** Changes one file at a time. For recursive permission changes across directories, bulk administrative capabilities are needed.

### Changing File Ownership
→ *Transfer ownership to another user*

Change which user owns a file. Ownership affects who can modify permissions and may affect access. You specify the file and the new owner.

**Important limitation:** Changing ownership typically requires administrative privileges. Cannot change ownership to nonexistent users.

### Changing Group Ownership
→ *Assign file to a different group*

Change which group is associated with a file. Group membership determines access for group permissions. You specify the file and the new group.

**Important limitation:** You typically must be a member of the target group or have administrative privileges. Group must exist on the system.

### Reading Current Permissions
→ *View current access settings*

Examine the current permissions, owner, and group settings on a file. Useful for understanding current state before making changes.

**Important limitation:** Shows settings but not the effective access for specific users, which depends on their group memberships and other factors.

### Managing Extended Attributes
→ *Work with access control lists*

For systems supporting extended ACLs, manage fine-grained access beyond basic permissions. Allows specific permissions for specific users or groups.

**Important limitation:** ACL support varies by filesystem. More complex than basic permissions. May not be portable across systems.

## Typical Workflows

### Workflow 1: Securing a File
1. Check current permissions on the file
2. Remove unnecessary access (world or group)
3. Verify only intended users can access
4. Document the change if needed

### Workflow 2: Sharing with Specific Group
1. Identify the appropriate group
2. Change group ownership to that group
3. Set group read (and write if needed) permissions
4. Verify group members can access

### Workflow 3: Making Scripts Executable
1. Identify script file to run
2. Add execute permission for appropriate scope
3. Test that script can now run
4. Adjust if too broad or narrow

### Workflow 4: Restoring Permissions
1. Note or look up correct permissions
2. Apply correct permission settings
3. Verify access is as expected
4. Update ownership if also incorrect

## Inherited Capabilities

This skill includes lower-level capabilities:
- Reading file contents
- Viewing file metadata
- Directory browsing and navigation

## Important Considerations

- Permission changes take effect immediately
- Incorrect permissions can lock you out
- Ownership changes may require elevated access
- Execute permission needed for directories to enter them
- Some systems have additional security layers

## Limitations

- Cannot change permissions on files you don't own
- Cannot recursively change permissions (single file only)
- Cannot create new permission schemes beyond system support
- Ownership changes may be restricted
- Some systems override permissions with additional controls

For recursive permission changes or bulk operations, administrative capabilities at higher privilege levels are needed.

## Notes

- Numeric modes (like 755) set all permissions at once
- Symbolic modes (like u+x) modify specific permissions
- Read permission on directory lists contents
- Execute permission on directory allows entering
- Sticky bit, setuid, setgid provide special behaviors
