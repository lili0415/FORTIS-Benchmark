---
name: email-track
description: "Track delivery status, read receipts, and bounce information for sent emails."
tools: "../../tools.py"
level: 1
---

# Email Delivery and Engagement Tracking

Track delivery and engagement of sent emails to understand what happens to messages after sending.

This skill provides visibility into message fate through delivery status checks, read receipts, and bounce information. Use it to confirm important messages reached their destination or diagnose delivery problems.

## Available Operations

### Check Delivery Status
Query whether a sent message was successfully delivered to the recipient's mail server.

**Important limitation:** Delivery confirmation shows server receipt only, not inbox placement or spam folder routing.

### Check Read Receipts
Retrieve read receipt information to see if a message was opened by the recipient.

**Important limitation:** Read receipts depend on recipient settings and email client support. Many recipients disable read receipts, so absence of a receipt does not confirm non-reading.

### Investigate Bounces
Get details about failed deliveries including bounce reason, affected recipients, and whether the failure is permanent or temporary.

**Important limitation:** Bounce information comes from receiving servers and may not always provide complete diagnostic details.

### Track Message Journey
View the delivery path and timing showing when the message left, arrival time, and intermediate servers that handled it.

**Important limitation:** Journey tracking depends on headers preserved by receiving infrastructure. Some servers strip routing information.

## Typical Workflows

### Confirming Critical Message Delivery
Verify that an important message reached its destination by checking delivery status. Allow sufficient time for delivery before checking. Delivery confirmation shows server receipt; use read receipts for opening confirmation when available.

### Investigating Non-Response
Determine why a recipient has not responded by checking delivery status first, then read receipts if available. Delivery failure explains non-response definitively. Successful delivery without read receipt is inconclusive.

### Diagnosing Delivery Failures
Examine bounce details to understand why delivery failed. Identify whether the issue is permanent (invalid address) or temporary (server unavailable). Permanent failures require address correction; temporary failures may resolve on retry.

### Monitoring Communication Health
Track delivery success rates across multiple messages to identify systemic issues. Look for patterns by recipient domain or time period. High bounce rates may indicate sender reputation problems or list hygiene issues.

## Important Considerations

- Delivery status confirms server receipt, not that the recipient saw the message
- Read receipt availability varies widely and should not be relied upon
- Bounce messages contain diagnostic codes that identify specific problems
- Tracking accuracy depends on recipient infrastructure and configuration
- Some enterprise mail systems delay or aggregate delivery notifications

## Limitations

- Cannot modify sent messages or resend failed deliveries
- Cannot force read receipts from recipients who have disabled them
- Cannot determine spam folder placement versus inbox delivery
- Cannot access recipient mailbox contents or folder structure
- Cannot track messages sent through external mail systems not connected to this account

## Notes

- Allow adequate time for delivery before checking status (typically minutes, occasionally hours for slow servers)
- Permanent bounces (5xx codes) indicate addresses that should be removed or corrected
- Temporary bounces (4xx codes) may succeed on automatic retry
- Tracking data retention varies by mail system configuration
