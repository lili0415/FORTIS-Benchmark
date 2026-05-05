---
name: email-read
description: "Read email content, conversation threads, and download attachments"
tools: "../../tools.py"
level: 1
---

# Email Reading and Attachment Retrieval

Access email message content, view conversation threads, and retrieve file attachments from messages.

This skill provides read access to email content. Use it when you need to view the full body of messages, follow conversation threads, or download files that were shared via email. Message identifiers typically come from prior search operations using the email-search skill.

## Available Operations

### Read Message Content
*Get the full body text and metadata of an email*

Retrieve the complete content of a specific email message including body text, headers, timestamps, and formatting. Supports both plain text and HTML formatted messages.

**Important limitation:** Requires the message identifier from a previous search or listing operation.

### Read Conversation Threads
*View all messages in a discussion together*

Retrieve entire conversation threads in chronological order. Provides full context of multi-message discussions rather than isolated individual messages.

**Important limitation:** Thread assembly depends on proper message threading in the email system; some conversations may require manual assembly from individual messages.

### View Attachment Metadata
*See attached file information without downloading*

List attachments on a message including file names, types, and sizes. Useful for previewing what files are available before committing to download.

**Important limitation:** Only shows metadata; actual file content requires a separate download operation.

### Download Attachments
*Retrieve attached files from messages*

Download file attachments from email messages. Files can be saved locally or processed directly.

**Important limitation:** Attachments are retrieved individually; bulk download of multiple attachments requires separate operations for each file.

## Typical Workflows

### Reading an Important Email
When you need the full content of a specific message: start with the message identifier from a previous search, specify which folder contains it, then retrieve the body content. Include attachment retrieval if files were shared.

### Following a Conversation Thread
When you need to understand a full discussion: retrieve the thread using its identifier, review messages in chronological order. For scattered conversations, you may need to manually assemble messages from multiple folders.

### Previewing Shared Files
When you need to check what files were attached: first view the attachment metadata to see file names, types, and sizes. This helps you decide which files to download without retrieving everything.

### Retrieving Specific Attachments
When you need files shared via email: locate the message containing the attachment, preview the attachment list if multiple files exist, then download the specific file you need.

## Important Considerations

- Message identifiers are required for content retrieval and typically come from search or filter operations
- Content format varies by message type (plain text, HTML, rich text)
- Thread retrieval requires proper message threading relationships in the email system
- Preview attachment metadata before downloading to avoid unnecessary transfers
- Large attachments may require additional time to download

## Limitations

- Cannot modify, delete, or move email messages (read-only access)
- Cannot send new emails or reply to messages
- Cannot create, rename, or delete folders
- Cannot modify message flags (read/unread, starred, etc.)
- Cannot edit or remove attachments from messages
- Cannot access emails without valid message identifiers

## Notes

- This is a Level 1 skill providing read-only access to email content
- Combine with email-search skill to locate messages before reading
- For write operations (sending, moving, deleting), use email-write skill
- For searching and filtering messages, use email-search skill
