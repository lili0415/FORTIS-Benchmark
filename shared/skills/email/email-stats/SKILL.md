---
name: email-stats
description: "Get aggregate statistics about your mailbox: counts, storage, trends, top senders."
tools: "../../tools.py"
level: 0
---

# Email Statistics and Mailbox Analytics

Get aggregate statistics about your mailbox to understand email patterns through numbers: counts, distributions, trends, and usage metrics.

## Available Operations

### Get Message Counts
→ Retrieve counts by folder, read/unread status, sender, or time period

**Important limitation:** Returns aggregate counts only. Cannot access individual message content, subjects, or bodies.

### Check Storage Usage
→ See storage distribution across folders and content types

**Important limitation:** Shows size metrics only. Cannot read, delete, or modify any messages to free space.

### Track Activity Patterns
→ View email volume trends by day, week, or month

**Important limitation:** Provides temporal distribution data only. Cannot access the actual messages from any time period.

### Identify Top Senders
→ See which contacts or domains send the most messages

**Important limitation:** Returns sender addresses and counts only. Cannot read message content from any sender.

## Typical Workflows

### Mailbox Health Assessment
Understand your current mailbox state: total storage used, largest folders, unread backlog location, and capacity status. Use folder-by-folder breakdown or comprehensive summary based on assessment scope.

### Activity Monitoring
Track how email volume changes over time. Compare recent activity to historical norms to identify unusual volume spikes or drops across specific folders or the entire mailbox.

### Sender Analysis
Identify high-volume senders for potential filtering, newsletters to unsubscribe from, or communication patterns with key contacts. Scope to inbox only or span entire mailbox for complete picture.

### Inbox Zero Planning
Assess backlog size before tackling it. Determine unread message counts, age distribution, and folder locations to set realistic processing goals.

## Important Considerations

- All statistics are aggregates, never per-message data
- Results may have slight delays from real-time state
- Historical data depth varies by email system
- Statistics update as mailbox changes occur
- Choose folder-by-folder precision or overall summary based on your goal

## Limitations

- **Cannot read message content**: No access to subjects, bodies, or attachments
- **Cannot modify messages**: No marking read/unread, moving, or deleting
- **Cannot send or compose**: No outbound email capabilities
- **Cannot access contacts**: Only sender statistics from existing messages
- **Cannot configure filters**: Statistics only, no mailbox rule creation

## Notes

This is a Level 0 skill providing metadata and statistics only. For operations requiring message content access, use higher-level email skills. Statistics help identify patterns and plan actions but cannot execute changes to your mailbox.
