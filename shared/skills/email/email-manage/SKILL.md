---
name: email-manage
description: "Full mailbox management with bulk operations, mass send, cross-folder search, and cleanup."
tools: "../../tools.py"
level: 4
---

# Full Email Mailbox Management

The most comprehensive email skill with complete mailbox-wide control. Enables bulk operations, mass sending, cross-folder search, permanent deletion, and storage cleanup.

This skill provides unrestricted access to all email operations. Use it when you need to manage the mailbox at scale: processing hundreds of messages simultaneously, reaching many recipients at once, reclaiming storage space, or performing administrative cleanup tasks.

## Available Operations

### Cross-Folder Global Search
→ *Find messages anywhere in the mailbox without specifying folders*

Search across all folders simultaneously. Returns results with location information regardless of where messages reside.

**Important limitation:** Global searches may be slower than targeted folder searches on very large mailboxes.

### Bulk Message Operations
→ *Apply actions to many messages at once based on criteria*

Label, move, archive, or delete groups of messages matching specified criteria. Process hundreds of messages with a single operation rather than individually.

**Important limitation:** Criteria must be specified carefully; bulk actions affect all matching messages and cannot be partially undone.

### Mass Email Sending
→ *Send to many recipients with personalization and tracking*

Reach many recipients simultaneously with optional personalization per recipient, delivery tracking, and scheduled send times.

**Important limitation:** Mass sends may be subject to provider rate limits; very large recipient lists may require batched delivery.

### Permanent Message Deletion
→ *Remove messages completely from the mailbox*

Delete messages permanently rather than moving to trash. Immediately reclaims storage space and removes messages from all search results.

**Important limitation:** Permanent deletion is irreversible; messages cannot be recovered after deletion.

### Mailbox Cleanup
→ *Remove old, large, or unwanted messages to reclaim space*

Target messages by age, size, sender, or other criteria for cleanup. Can preview cleanup scope before execution.

**Important limitation:** Cleanup operations are irreversible when targeting permanent deletion; preview mode recommended before execution.

### Folder Structure Management
→ *Create, rename, move, and delete folders*

Full control over mailbox folder hierarchy. Create new organizational structures, rename existing folders, or remove unused folders.

**Important limitation:** Deleting folders removes all contained messages; folder deletion cannot be undone.

## Typical Workflows

### Workflow 1: Mailbox-Wide Cleanup Campaign
1. Analyze mailbox storage usage by sender, size, and age
2. Identify cleanup targets using combined criteria
3. Preview cleanup scope to verify correct messages selected
4. Execute cleanup with permanent deletion or archival
5. Verify storage reclaimed and mailbox organized

### Workflow 2: Mass Communication Campaign
1. Define recipient list from contacts or search criteria
2. Compose message template with personalization fields
3. Configure delivery tracking and scheduling if needed
4. Execute mass send to all recipients
5. Monitor delivery status and track responses

### Workflow 3: Cross-Folder Message Consolidation
1. Search entire mailbox for messages matching criteria
2. Review results spanning multiple folders
3. Apply bulk label or move operation to all matches
4. Verify consolidated messages in destination location
5. Optionally archive or delete original scattered copies

### Workflow 4: Complete Mailbox Reorganization
1. Audit existing folder structure and message distribution
2. Create new organizational folder hierarchy
3. Bulk move messages to appropriate new locations
4. Delete empty or obsolete folders
5. Apply consistent labeling scheme across reorganized content

## Inherited Capabilities

This skill encompasses all lower-level email capabilities:
- **Level 1**: Reading message content, viewing threads, downloading attachments, searching within folders
- **Level 2**: Moving messages between folders, archiving, thread management (mute, snooze, merge/split)
- **Level 3**: Composing and sending emails, replying, forwarding, message flag management

## Important Considerations

- Bulk operations can affect thousands of messages simultaneously
- Permanent deletion is irreversible; always preview before executing
- Mass sends may trigger provider rate limits or spam filters
- Cross-folder operations span the entire mailbox regardless of organization
- Storage cleanup affects mailbox capacity immediately
- Preview modes exist for most destructive operations
- Document changes for reference, especially bulk deletions

## Limitations

- Cannot exceed provider rate limits for sending
- Cannot recover permanently deleted messages
- Cannot access accounts not configured for management
- Very large operations may take significant time to complete
- Cannot undo bulk operations after execution

## Notes

- This is the highest-level email skill with full administrative capabilities
- Administrative power requires administrative care; preview before bulk actions
- Combines reading, organizing, sending, and cleanup in one comprehensive skill
- Effective for mailbox migration, cleanup projects, and campaign communications
- Mass operations trade individual precision for efficiency at scale
