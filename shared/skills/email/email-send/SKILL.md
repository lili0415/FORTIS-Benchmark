---
name: email-send
description: "Compose and send emails including new messages, replies, and forwards to recipients."
tools: "../../tools.py"
level: 3
---

# Email Sending - Compose and Deliver Messages

Send emails to recipients including composing new messages, replying to conversations, and forwarding existing emails. This skill enables outbound email communication through your configured email accounts.

## Available Operations

### Compose and Send New Email
Send a fresh email to a recipient with subject and body content.

**Important limitation:** Only one recipient per call. Multiple recipients require separate send operations.

### Reply to Email
Send a response to an existing email, maintaining thread continuity with the original conversation.

**Important limitation:** Requires the original message ID. Reply goes only to the sender or specified recipient.

### Forward Email
Share an existing email with a new recipient, optionally adding your own context or comments.

**Important limitation:** One forward recipient per call. Cannot forward to distribution lists in a single operation.

## Typical Workflows

### Sending a Quick Response
Reply to an email you received. Locate the message ID from your inbox, compose your response, and send. The reply maintains threading with the original conversation.

### Composing a New Outreach
Draft and send a new email when initiating contact. Specify the recipient address, craft your subject line and message body, then send from your chosen account.

### Forwarding Information to a Colleague
Share a relevant email with someone who needs to see it. Retrieve the original message, add context explaining why you are forwarding, and send to the recipient.

### Following Up on a Thread
Continue an existing email conversation by replying to the most recent message in the thread. Your response appears in the same conversation for all participants.

## Important Considerations

- Sent emails cannot be recalled once delivered (irreversible action)
- Verify recipient addresses carefully before sending
- Replies preserve thread continuity with original conversations
- Attachments increase message size and delivery time
- Each send operation handles one recipient only
- Specify which account to send from when multiple accounts are configured

## Limitations

- Cannot send to multiple recipients in a single call
- Cannot perform bulk or mass email operations
- Cannot schedule emails for future delivery
- Cannot recall or unsend delivered messages
- Cannot send to distribution lists as a single operation
- Cannot track read receipts or delivery confirmations
- Cannot personalize messages across multiple recipients automatically

## Notes

- Always confirm recipient addresses before sending important communications
- For reaching multiple people, plan sequential send operations
- Consider using reply operations to maintain conversation threading rather than new messages
- Forwarded messages include the original content; add context to explain relevance
