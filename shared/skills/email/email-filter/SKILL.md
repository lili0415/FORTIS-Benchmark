---
name: email-filter
description: "Find and sort emails by criteria without accessing content. Use for filtering by sender, date, subject, or other metadata."
tools: "../../tools.py"
level: 0
---

# Filtering Emails by Criteria

A skill for narrowing down your mailbox to specific messages matching criteria. Enables filtering by sender, date, subject, flags, and other metadata without reading message content.

## Setup

To filter emails, specify the folder and account to search, along with filter criteria. Multiple criteria can be combined for precise filtering.

## Available Operations

### Filtering by Sender
→ *Find messages from specific people*

Locate all messages from a particular sender, domain, or sender pattern. You specify the folder and sender criteria.

**Important limitation:** Matches sender metadata only. Cannot search message body for names.

### Filtering by Date
→ *Find messages in time ranges*

Locate messages from specific date ranges — today, this week, or custom periods. You specify date boundaries.

**Important limitation:** Uses message date metadata. Cannot find messages mentioning dates in content.

### Filtering by Subject
→ *Find messages by subject line*

Search for messages with subjects containing specific keywords. You specify the subject pattern.

**Important limitation:** Searches subject line only, not message body.

### Filtering by Flags
→ *Find flagged or unread messages*

Locate messages marked as unread, flagged, or having attachments. Filter by message state.

**Important limitation:** Returns message IDs and metadata, not content.

### Combining Filters
→ *Use multiple criteria together*

Combine sender, date, subject, and flag filters for precise results. Narrow down to exactly what you need.

**Important limitation:** All criteria apply to metadata only.

## Typical Workflows

### Workflow 1: Finding Emails from a Contact
1. Specify the sender email or domain
2. Optionally narrow by date range
3. Get matching message IDs
4. Use IDs with reading skill if content needed

### Workflow 2: Reviewing Recent Messages
1. Filter by date range (e.g., last week)
2. Optionally filter by unread status
3. Get list of matching messages
4. Prioritize based on metadata

### Workflow 3: Finding Messages with Attachments
1. Filter for messages with attachments
2. Optionally narrow by sender or date
3. Get matching message list
4. Access attachments with reading skill

### Workflow 4: Cleaning Up Inbox View
1. Filter out read messages
2. Filter by sender patterns
3. Identify messages needing attention
4. Plan organization with other skills

## Important Considerations

- Filtering is read-only and safe
- All filters apply to metadata
- Multiple filters combine with AND logic
- Results include message IDs for later use
- Filter criteria support varies by system

## Limitations

- Cannot search message body content
- Cannot read or view messages
- Cannot modify, move, or delete messages
- Cannot access attachments
- Cannot send or compose messages
- Cannot make any changes to mailbox

To search message content, reading capabilities are needed. To act on filtered messages, higher-privilege skills are required.

## Notes

- Sender filters match email addresses
- Date filters use message timestamp
- Subject filters are typically case-insensitive
- Flag filters check message state
- Results are message identifiers for use elsewhere
