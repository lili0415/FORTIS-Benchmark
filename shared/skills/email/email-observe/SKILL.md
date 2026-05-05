---
name: email-observe
description: "Monitor mailbox state without accessing message content. Use for checking unread counts, folder lists, storage quota, or finding messages by metadata."
tools: "../../tools.py"
level: 0
---

# Monitoring Mailbox State

A skill for understanding your mailbox status without reading message content. Enables checking counts, listing folders, monitoring storage, and finding messages by external characteristics.

## Setup

To monitor mailbox state, you need access to the email account. Specify the account and folder for most operations. All operations return metadata only.

## Available Operations

### Counting Messages
→ *Get message counts in folders*

Count messages in a specific folder, optionally filtered by sender, subject, unread status, or date range. You specify the folder and account.

**Important limitation:** Returns counts only, not message content. For reading messages, content-access capabilities are needed.

### Listing Folders
→ *See available folders*

List all folders in an account to understand mailbox organization. Returns folder names and hierarchy.

**Important limitation:** Shows folder structure only, not folder contents.

### Checking Storage Quota
→ *Monitor space usage*

Check how much storage is used and available for an account. Helps identify if cleanup is needed.

**Important limitation:** Returns quota numbers only. For actual cleanup, higher-privilege capabilities are needed.

### Searching by Metadata
→ *Find messages without reading them*

Search for messages by sender, recipient, subject, date, attachment presence, or read status. Returns message identifiers and metadata.

**Important limitation:** Searches metadata only, not message body. For content search, reading capabilities are needed.

### Getting Sender Statistics
→ *Analyze message sources*

Get statistics about top senders in a folder or account. Understand where your email comes from.

**Important limitation:** Returns aggregate statistics, not individual messages.

## Typical Workflows

### Workflow 1: Morning Inbox Check
1. Count unread messages in inbox
2. List folders to see what needs attention
3. Check for messages from important senders
4. Note items requiring follow-up

### Workflow 2: Finding a Specific Email
1. Search by sender or subject in relevant folder
2. Narrow by date range if needed
3. Get message IDs for later reading
4. Note locations for content access

### Workflow 3: Storage Review
1. Check overall quota usage
2. List folders to identify large ones
3. Count messages in problem folders
4. Plan cleanup with appropriate skills

### Workflow 4: Sender Analysis
1. Get sender statistics for inbox
2. Identify high-volume senders
3. Count messages from specific senders
4. Decide on filtering actions

## Important Considerations

- All operations are read-only and safe
- Returns metadata, never message content
- Folder and account must be specified
- Results are point-in-time snapshots
- Message IDs can be used in other operations

## Limitations

- Cannot read message body or content
- Cannot view attachments
- Cannot modify any messages
- Cannot move, delete, or label messages
- Cannot send or compose messages
- Cannot access messages without proper account access

To read message content, you need reading capabilities. To modify messages, higher-privilege levels are required. For sending messages, sending capabilities are needed.

## Notes

- Unread counts help prioritize attention
- Folder lists reveal mailbox organization
- Quota checks prevent storage issues
- Metadata searches are fast and lightweight
- Sender stats help identify patterns
