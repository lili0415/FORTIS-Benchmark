---
name: email-move
description: "Move emails between folders and archive messages. Cannot delete permanently or send."
tools: "../../tools.py"
level: 2
---

# Moving and Archiving Email Messages

Relocate email messages between folders and archive storage to maintain an organized mailbox structure.

This skill provides folder organization capabilities including moving messages between folders, archiving for long-term storage, and recovering misplaced items from spam or trash. Use it when you need to reorganize your mailbox, clear your inbox by filing messages, or rescue items from incorrect locations.

## Available Operations

### Move Messages Between Folders
-> *Relocate messages from one folder to another*

Transfer individual messages or groups of messages from their current location to a specified destination folder. Requires knowledge of which messages to move and their target location.

**Important limitation:** Cannot delete messages permanently; moving to trash is the maximum removal action available.

### Archive Messages
-> *Transfer messages to archive storage*

Move messages to archive folders for long-term retention while clearing active folders. Archived messages remain accessible but are removed from primary working folders.

**Important limitation:** Cannot configure archive retention policies or automatic archiving rules; each archive action must be explicitly requested.

### Recover Misplaced Messages
-> *Rescue messages from spam or trash folders*

Move messages that ended up in incorrect locations back to appropriate folders. Useful for rescuing legitimate messages caught by spam filters or accidentally deleted.

**Important limitation:** Cannot recover messages that have been permanently deleted or purged from trash.

### Organize by Project or Topic
-> *Group related messages in dedicated folders*

Move related correspondence to project-specific or topic-based folders. Consolidates scattered messages for easier access and reference.

**Important limitation:** Cannot create new folders; destination folders must already exist.

## Typical Workflows

### Workflow 1: Processing Inbox Items
1. Identify messages requiring filing
2. Determine appropriate destination folder for each
3. Move messages to their designated folders
4. Verify inbox is cleared of processed items

### Workflow 2: Archiving Old Messages
1. Identify messages eligible for archiving (e.g., older than 30 days, completed projects)
2. Select messages individually or by criteria
3. Move selected messages to archive folder
4. Confirm messages are accessible in archive

### Workflow 3: Recovering from Spam/Trash
1. Locate misplaced message in spam or trash folder
2. Verify the message should be recovered
3. Move message to inbox or appropriate folder
4. Consider marking sender as safe to prevent future misfilings

### Workflow 4: Consolidating Project Correspondence
1. Identify all messages related to a specific project
2. Verify destination project folder exists
3. Move messages from various folders to the project folder
4. Review consolidated folder for completeness

## Important Considerations

- Moving a message removes it from its original location
- Trash and spam folders may have automatic cleanup policies
- Movement is reversible by moving the message again
- Batch moves are more efficient for organizing many similar messages
- Some special folders (sent, drafts) may have restrictions on incoming moves
- Cross-account moves may not be supported

## Limitations

- Cannot permanently delete messages (only move to trash)
- Cannot send, reply to, or compose new messages
- Cannot create, rename, or delete folders
- Cannot modify message content, flags, or labels
- Cannot set up automatic rules or filters for future messages
- Cannot undo moves after session ends except by moving again
- Cannot access messages without valid identifiers

## Notes

- This is a Level 2 skill with organizational but not destructive capabilities
- Combine with email-search to locate messages before moving
- For labeling without moving, use email-annotate skill
- For permanent deletion or sending, higher-level skills are required
- Special folders (trash, spam) may auto-delete messages after a retention period
