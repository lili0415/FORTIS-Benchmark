---
name: email-preview
description: "Preview email snippets and attachments for quick triage without loading full content."
tools: "../../tools.py"
level: 1
---

# Quick Email Content Preview

A skill for rapidly examining email messages without loading complete content. Enables viewing message snippets, checking thread status, previewing attachments, and scanning recent arrivals for efficient inbox triage.

## Setup

To preview emails, you need read access to the email account. Specify the account and folder for most operations. Previews return partial content designed for quick assessment rather than full reading.

## Available Operations

### Previewing Message Snippets
→ *View opening portions of messages*

See the first portion of a message's body - enough to understand the topic without loading everything. You specify the message identifier and optionally preview length. Fast operation useful for scanning many messages.

**Important limitation:** Shows only opening content, which may miss key information later in the message. For complete content, full reading capabilities are needed.

### Previewing Thread Status
→ *Get conversation overview without full content*

Obtain thread metadata: participant count, message count, date range, and last activity. Helps assess conversation scope before committing to full reading. You specify the thread identifier.

**Important limitation:** Returns metadata and brief snippets only, not full message bodies. For complete thread content, reading capabilities are needed.

### Previewing Attachments
→ *See attachment details without downloading*

View what files are attached to a message: names, types, sizes, and counts. Helps decide if retrieval is needed without downloading anything. You specify the message containing attachments.

**Important limitation:** Shows attachment metadata only, not file contents. For actual file content, download and reading capabilities are needed.

### Previewing Recent Arrivals
→ *Quick scan of newest messages*

Get snippets for the most recent messages in a folder. Useful for rapid inbox checks to see what's new. You specify the folder and optionally how many messages to preview.

**Important limitation:** Returns brief previews only and is limited to recent messages. For older messages or full content, other approaches are needed.

## Typical Workflows

### Workflow 1: Morning Inbox Triage
1. Preview recent arrivals in inbox
2. Identify messages requiring immediate attention
3. Check thread status for ongoing conversations
4. Note items needing full reading later

### Workflow 2: Checking for Expected Email
1. Preview recent messages in relevant folder
2. Scan snippets for expected sender or topic
3. Confirm arrival or note absence
4. Proceed to full reading if found

### Workflow 3: Thread Assessment
1. Preview thread status to see scope
2. Check participant count and activity
3. Preview latest message snippet
4. Decide whether to read full thread

### Workflow 4: Attachment Quick Check
1. Preview attachments on target message
2. Review file names, types, and sizes
3. Identify files worth downloading
4. Note download needs for later

## Important Considerations

- Previews are partial by design for efficiency
- Snippet length varies by message and approach
- Attachment previews show metadata, not content
- Thread previews summarize without full detail
- Preview operations are read-only and safe

## Limitations

- Cannot show full message content
- Cannot download or view attachment contents
- Cannot modify, move, or delete messages
- Cannot send or compose messages
- Cannot label or organize messages
- Cannot search message body content

For complete content access, full reading capabilities are needed. For modifications or organization, higher privileges are required. For sending messages, sending capabilities are needed.

## Notes

- Previews balance information versus speed
- Opening snippets may not reflect full message content
- Thread metadata helps prioritize reading time
- Attachment metadata helps prioritize downloads
- Consider whether preview or full read better fits your needs
