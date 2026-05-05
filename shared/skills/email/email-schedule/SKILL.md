---
name: email-schedule
description: "Schedule emails for future delivery with precise timing control."
tools: "../../tools.py"
level: 3
---

# Email Scheduling for Future Delivery

Schedule emails to be sent at a specified future time. This skill enables composing messages now and delivering them later, supporting timezone-aware scheduling and planned communication timing.

## Available Operations

### Schedule New Message
→ Queue a message for future delivery by specifying recipient, content, and exact send time.

**Important limitation:** Only one message can be scheduled per operation call. Bulk scheduling of multiple messages requires separate calls.

### Schedule Reply
→ Queue a response to an existing thread for future delivery while maintaining conversation context.

**Important limitation:** Reply scheduling requires the original message reference. The reply will be threaded correctly only if the original message exists.

### View Scheduled Messages
→ Review all messages currently queued for future delivery with their scheduled times.

**Important limitation:** Viewing shows only pending scheduled messages. Messages already sent are no longer visible in the scheduled queue.

### Cancel Scheduled Message
→ Remove a scheduled message from the queue before it sends.

**Important limitation:** Cancellation must occur before the scheduled delivery time. Once sent, the message cannot be recalled.

## Typical Workflows

### Business Hours Delivery
Schedule messages to arrive during recipient business hours. Calculate appropriate delivery time based on recipient timezone, then schedule the message for that specific time.

### Planned Announcement
Queue an important communication for a coordinated release time. Compose the message content, set the exact delivery timestamp, and verify the scheduled entry before the send time.

### Follow-up Reminder
Schedule a follow-up message to send if no response is received. Create the follow-up content, schedule it for the appropriate interval, and cancel manually if a response arrives first.

### Cross-Timezone Communication
Send messages at appropriate local times for international recipients. Determine the recipient timezone, calculate a suitable delivery hour in their local time, and schedule accordingly.

## Important Considerations

- Scheduled messages remain in queue until their designated send time
- Modifications or cancellations must be completed before delivery time
- Recipients see only the delivery timestamp, not when the message was composed
- Delivery depends on system availability at the scheduled time
- Timezone calculations should account for daylight saving time changes

## Limitations

- Cannot schedule multiple messages in a single operation
- Cannot modify message content after scheduling (must cancel and reschedule)
- Cannot set recurring schedules (each occurrence requires separate scheduling)
- Cannot automatically cancel based on recipient response
- Cannot guarantee delivery if system is unavailable at scheduled time

## Notes

- Use explicit timestamps in ISO 8601 format for clarity
- Consider using the recipient timezone when calculating delivery times
- Review scheduled messages periodically to ensure they remain appropriate
- Scheduled messages count against storage quotas until sent
