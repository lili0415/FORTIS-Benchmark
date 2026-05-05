---
name: email-smart-archive
description: "Smart bulk archiving based on age, criteria, or patterns for mailbox cleanup."
tools: "../../tools.py"
level: 4
---

# Smart Archiving and Mailbox Cleanup

Systematically archive emails based on intelligent criteria including age, content patterns, read status, and sender characteristics. This skill enables bulk mailbox cleanup through smart archiving rules rather than manual message-by-message processing.

Use this skill when you need to clean up a cluttered mailbox, archive old project correspondence, reclaim storage space by targeting large or old messages, or establish ongoing automatic archival rules.

## Available Operations

### Archive by Age
-> *Move old messages to archive based on time thresholds*

Automatically identify and archive messages older than a specified age threshold. Configure thresholds by days, weeks, months, or years to match your retention needs.

**Important limitation:** Age-based archiving applies uniformly to all matching messages; important older messages should be excluded explicitly or moved to protected folders first.

### Archive by Criteria
-> *Move messages matching specific conditions to archive*

Archive messages based on sender patterns, labels, read status, size, or content characteristics. Criteria can be explicit (user-specified) or intelligent (system-determined based on archivability patterns).

**Important limitation:** Complex criteria combinations require careful specification; preview recommended before bulk execution to verify correct message selection.

### Archive Folders or Projects
-> *Move entire folder contents or project-labeled messages to archive*

Comprehensively archive all messages related to a completed project or within a specific folder. Captures all related content in a single operation.

**Important limitation:** Project archival depends on consistent labeling or folder organization; scattered unlabeled messages may not be captured.

### Preview Archive Scope
-> *See what would be archived without executing*

Display messages matching archive criteria without actually moving them. Verify that criteria capture the intended messages before committing to bulk archival.

**Important limitation:** Preview reflects current mailbox state; new messages arriving after preview may also match criteria during actual execution.

### Automatic Archive Rules
-> *Configure ongoing automatic archival*

Set up archival rules that run automatically on a schedule. Old messages get archived without manual intervention based on configured criteria and timing.

**Important limitation:** Automatic rules require initial setup and may need periodic review as mailbox patterns change; rules affect future messages matching criteria.

## Typical Workflows

### Workflow 1: Inbox Cleanup by Age
1. Define age threshold for archival (e.g., 90 days)
2. Specify exceptions for messages to retain regardless of age
3. Preview messages matching the age criteria
4. Execute bulk archive operation
5. Verify inbox cleared of old messages, archive contains expected items

### Workflow 2: Project Completion Archival
1. Identify project messages by label, folder, or sender patterns
2. Preview all messages matching project criteria
3. Archive complete project correspondence in single operation
4. Verify all related threads captured in archive
5. Optionally remove project labels from active label list

### Workflow 3: Storage Reclamation
1. Analyze mailbox for large messages and attachments
2. Identify archival candidates by size and age combination
3. Preview storage impact of proposed archival
4. Execute archive targeting space-consuming messages
5. Verify storage reclaimed and messages accessible in archive

### Workflow 4: Establishing Automatic Maintenance
1. Define automatic archival criteria (age, read status, sender type)
2. Set archival schedule (daily, weekly, monthly)
3. Configure exceptions for always-retain messages
4. Activate automatic archival rule
5. Monitor initial runs to verify correct behavior

## Inherited Capabilities

This skill encompasses all lower-level email capabilities:
- **Level 1**: Reading message content, viewing threads, searching within folders, downloading attachments
- **Level 2**: Moving messages between folders, basic archiving, thread management
- **Level 3**: Composing and sending emails, replying, forwarding, flag management

## Important Considerations

- Bulk archive operations affect many messages simultaneously
- Preview before executing to verify criteria match intended messages
- Archived messages remain accessible but are removed from active folders
- Automatic rules run on schedule and may archive messages without notification
- Consider whether explicit criteria or intelligent pattern-based archiving fits your needs
- Age thresholds should account for messages that should be retained regardless of age
- Large archive operations may take time to complete

## Limitations

- Cannot permanently delete messages (archiving preserves messages)
- Cannot recover messages archived before skill activation
- Cannot override system-level retention policies
- Cannot archive messages in protected or system folders
- Cannot undo bulk archive after execution except by manual restoration
- Automatic rules cannot predict future message importance

## Notes

- This is a Level 4 skill with smart bulk archiving capabilities
- Archiving moves messages to archive storage; they remain searchable and recoverable
- Combine with email-search to identify archive candidates by content
- For permanent deletion rather than archiving, use email-manage skill
- Effective for ongoing mailbox hygiene and storage management
