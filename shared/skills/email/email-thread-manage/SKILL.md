---
name: email-thread-manage
description: "Manage email threads: mute, archive, snooze, merge/split conversations as units."
tools: "../../tools.py"
level: 2
---

# Email Thread Management

Manage email conversations as complete units rather than individual messages. This skill provides conversation-level control for muting, archiving, snoozing, and restructuring email threads.

## Available Operations

### Mute Threads
→ Stop notifications for busy conversations while still receiving messages

Silences notifications for high-volume discussions you do not need to actively follow. Messages continue arriving but without alerts.

**Important limitation:** Muting only affects notifications. New messages still arrive and are visible when you check the thread.

### Archive Threads
→ Move complete conversations to archive together

Removes threads from inbox while keeping them accessible. Can target specific threads or operate on threads matching criteria such as age, participants, or labels.

**Important limitation:** Archiving does not delete messages. Archived threads remain searchable and can be restored to inbox.

### Snooze Threads
→ Hide conversations temporarily until a specified time

Defers threads from view until they become relevant again. The system resurfaces snoozed threads automatically at the scheduled time.

**Important limitation:** Snooze timing depends on email provider capabilities. Some providers may have minimum or maximum snooze durations.

### Merge or Split Threads
→ Combine related conversations or separate incorrectly grouped messages

Restructures thread boundaries to fix grouping errors. Merge combines separate threads that belong together. Split separates messages incorrectly grouped in one thread.

**Important limitation:** Thread restructuring may not be supported by all email providers. Changes may not propagate to other participants' views.

### Bulk Thread Operations
→ Apply actions to multiple threads simultaneously based on criteria

Performs mute, archive, or snooze operations on multiple threads matching specified criteria rather than individual selection.

**Important limitation:** Bulk operations affect all matching threads. Review criteria carefully before executing.

## Typical Workflows

### Workflow 1: Managing High-Volume Discussion Threads

1. Identify threads generating excessive notifications
2. Assess whether you need to track replies actively
3. Apply mute to stop notifications while preserving message delivery
4. Optionally archive if the discussion is no longer inbox-relevant

### Workflow 2: Archiving Completed Project Threads

1. Identify threads related to a completed project by participants, labels, or date range
2. Review thread list to confirm all should be archived
3. Execute bulk archive operation on matching threads
4. Verify threads moved from inbox to archive

### Workflow 3: Deferring Time-Sensitive Conversations

1. Identify threads not relevant until a future date
2. Set snooze time based on when the thread becomes actionable
3. Apply snooze to remove from active view
4. Thread resurfaces automatically at scheduled time

### Workflow 4: Correcting Thread Structure Errors

1. Identify threads with incorrect message grouping
2. For incorrectly combined messages: split into separate threads
3. For incorrectly separated messages: merge into single thread
4. Verify corrected thread structure displays properly

## Important Considerations

- Thread operations affect all messages in a conversation simultaneously
- Muted threads continue receiving new messages without notification
- Snoozed threads resurface automatically at the scheduled time
- Bulk operations can affect many threads at once; verify criteria before executing
- Choose between individual thread targeting and criteria-based selection based on the scope of your task
- Thread restructuring (merge/split) changes may not sync across all email clients

## Limitations

- Cannot permanently delete threads or messages (Level 3 required)
- Cannot send or forward thread contents (Level 3 required)
- Cannot modify message content within threads
- Cannot change thread participants or recipients
- Cannot undo thread operations after execution completes
- Thread merge/split may not be supported by all email providers

## Notes

- Archiving is reversible; threads can be moved back to inbox
- Muting is useful for ongoing discussions; archiving is better for completed threads
- Snoozing provides a "set and forget" approach to deferred conversations
- Criteria-based bulk operations are more efficient than individual selection for large-scale thread management
