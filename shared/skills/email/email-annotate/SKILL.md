---
name: email-annotate
description: "Mark read/unread, apply labels, set flags, and manage drafts for email organization"
tools: "../../tools.py"
level: 2
---

# Email Annotation and Organization

Mark emails with status indicators, apply labels and flags, and manage draft messages for mailbox organization.

This skill provides annotation capabilities for organizing your mailbox without moving or deleting messages. Use it when you need to mark messages as read or unread, apply categorical labels, flag items for follow-up, or create draft messages for later completion. Annotations help you track what needs attention and group related messages together.

## Available Operations

### Mark Read/Unread Status
*Control which messages appear as requiring attention*

Set messages as read or unread to manage your attention flow. Mark items read after reviewing them, or mark items unread to ensure they get follow-up attention later.

**Important limitation:** Status changes apply to individual messages; batch status updates require separate operations for each message.

### Apply Labels
*Categorize messages with custom tags*

Add labels or tags to messages for organizational grouping. Labels help you categorize messages by project, topic, priority, or any custom scheme without physically moving them to folders.

**Important limitation:** Label application does not move messages; labeled messages remain in their current folders.

### Set Flags and Stars
*Mark messages as important or needing follow-up*

Flag, star, or mark messages as important to highlight items requiring action. Flags provide visual indicators in your mailbox for tracking items that need response or review.

**Important limitation:** Flags are binary indicators only; for categorical importance levels, combine with labels.

### Manage Drafts
*Create and save work-in-progress messages*

Create draft messages for later completion. Save partially composed messages without sending, allowing you to refine content, gather information, or wait for the right time to send.

**Important limitation:** Drafts are saved locally but not sent; sending requires the email-send skill.

## Typical Workflows

### Workflow 1: Processing Inbox for Triage
1. Review messages requiring attention
2. Mark read after reviewing each message
3. Apply labels based on topic or project
4. Flag items requiring follow-up action
5. Mark messages unread if they need further review later

### Workflow 2: Project-Based Organization
1. Identify messages related to a specific project
2. Apply a consistent project label to all related messages
3. Flag high-priority items within the project
4. Create drafts for any responses needed

### Workflow 3: Creating Action Lists
1. Scan inbox for items requiring response
2. Flag all action items for visibility
3. Apply "needs-response" or similar label
4. Mark flagged items as unread to keep them visible

### Workflow 4: Preparing Responses
1. Identify messages requiring replies
2. Create draft responses to capture initial thoughts
3. Save drafts for later refinement
4. Apply "draft-pending" label to track incomplete responses

## Important Considerations

- Annotations are personal organization markers that do not affect message content
- Labels and flags persist until explicitly changed or removed
- Read/unread status affects unread message counts in folder views
- Drafts are saved locally and can be edited before sending
- Multiple labels can be applied to a single message
- Consider batch labeling for efficiency when organizing many similar messages

## Limitations

- Cannot move messages between folders (use email-move skill)
- Cannot delete messages or move to trash
- Cannot send messages (drafts require email-send skill to send)
- Cannot create or manage folders
- Cannot modify message content or attachments
- Cannot set automatic rules or filters for future messages
- Cannot access shared or delegated mailboxes

## Notes

- This is a Level 2 skill providing annotation and draft capabilities
- Combine with email-search to locate messages before annotating
- Combine with email-read to review content before labeling
- For moving messages to folders, use email-move skill
- For sending composed messages, use email-send skill
- Annotations do not affect sender-side message records
