---
name: email-search
description: "Search within email message bodies and attachments using text queries and filters."
tools: "../../tools.py"
level: 1
---

# Email Content Search

Search within email message bodies and attachments to find messages based on their actual content rather than just metadata.

This skill provides read-only search capabilities across email content. Use it when you need to locate messages by searching what they contain, including body text, attachment information, and complex query expressions.

## Available Operations

### Search Message Bodies
Search for specific text within email body content.

**Important limitation:** Search is read-only; cannot modify, move, or delete any messages found.

### Search with Complex Queries
Find messages using Boolean operators (AND, OR, NOT), field-specific filters, and combined criteria.

**Important limitation:** Query syntax depends on the email provider; some complex queries may require explicit folder specification.

### Search Attachments
Locate messages with attachments matching file name patterns, types, or size ranges.

**Important limitation:** Can only search attachment metadata; cannot open, download, or preview attachment contents.

### Cross-Folder Search
Search across multiple folders or the entire mailbox regardless of message location.

**Important limitation:** Broad searches may be slower; cannot guarantee complete coverage if some folders are not indexed.

## Typical Workflows

### Finding a Specific Discussion
1. Identify keywords from the conversation you remember
2. Optionally narrow by date range or folder if known
3. Execute body search with relevant terms
4. Review matching messages to locate the discussion

### Locating a Document Attachment
1. Search by attachment file name if known
2. Alternatively search body text for mentions of the document
3. Filter by sender or date range to narrow results
4. Identify the message containing the attachment

### Research Across Mailbox
1. Define topic keywords for comprehensive search
2. Execute cross-folder search spanning entire mailbox
3. Collect all matching messages regardless of folder location
4. Review results for relevant content

### Finding Action Items
1. Search body text for action-related keywords (e.g., "please review", "deadline", "action required")
2. Filter by date range to focus on recent or relevant periods
3. Review matching messages for pending tasks
4. Note relevant messages for follow-up

## Important Considerations

- Body search examines actual message content, providing more thorough results than metadata-only search
- Search effectiveness depends on email system indexing capabilities
- Complex queries use Boolean operators for precise filtering
- Results typically include match context showing where terms appear
- Consider whether targeted precision (specific folders) or broad coverage (entire mailbox) better serves your goal
- Broader searches trade speed for completeness

## Limitations

- Cannot modify, move, delete, or flag any messages
- Cannot open or download attachments
- Cannot compose, send, or reply to messages
- Cannot access messages in accounts not configured for search
- Cannot guarantee search results are exhaustive if indexing is incomplete
- Cannot perform actions on search results beyond viewing

## Notes

- This is a Level 1 skill with read-only access to email content
- Search results are for informational purposes only
- Use email-manage skill for any modifications to messages
- Search scope and speed vary by email provider capabilities
