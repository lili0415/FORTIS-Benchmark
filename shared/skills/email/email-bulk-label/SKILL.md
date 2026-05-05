---
name: email-bulk-label
description: "Apply labels to many emails at once with criteria-based and smart auto-labeling capabilities."
tools: "../../tools.py"
level: 4
---

# Bulk Email Labeling and Auto-Organization

Apply labels to many emails simultaneously using explicit criteria or intelligent content analysis for efficient mailbox organization at scale.

This skill enables high-volume labeling operations that would be impractical to perform message by message. Use it when you need to label hundreds of messages consistently, implement a new organizational scheme across existing mail, or set up smart labeling that categorizes messages based on content patterns. Bulk operations apply changes atomically across matching messages.

## Available Operations

### Bulk Apply Labels
-> *Add labels to many messages matching specified criteria*

Apply one or more labels to all messages matching sender, date range, subject patterns, or other criteria. Process hundreds of messages with a single operation rather than labeling individually.

**Important limitation:** All matching messages receive the same labels; per-message label variation requires separate operations.

### Bulk Remove Labels
-> *Strip labels from groups of messages at once*

Remove specified labels from all messages that currently have them. Useful for deprecating old labels, cleaning up obsolete categorizations, or preparing for reorganization.

**Important limitation:** Removal affects all messages with the target label; cannot selectively preserve labels on some matching messages.

### Relabel Messages
-> *Replace old labels with new ones in a single operation*

Change labels on groups of messages by removing old labels and applying new ones atomically. Enables label scheme migrations without intermediate unlabeled states.

**Important limitation:** Relabeling is immediate; there is no intermediate preview of label changes per message.

### Criteria-Based Auto-Labeling
-> *Automatically label messages matching specified conditions*

Define labeling rules based on sender, subject, content keywords, or other metadata. Messages matching criteria receive labels automatically without manual selection.

**Important limitation:** Criteria must be precise; overly broad rules may label unintended messages.

### Smart Content-Based Labeling
-> *Intelligently categorize messages based on content analysis*

Analyze message content to suggest or apply appropriate labels. Identifies project-related messages, topic clusters, or action items based on content patterns rather than explicit criteria.

**Important limitation:** Content analysis may not catch all relevant messages; review suggested labels before bulk application.

## Typical Workflows

### Workflow 1: Implementing a New Organization Scheme
1. Define the new label taxonomy and criteria for each label
2. Preview which messages match each labeling criterion
3. Execute bulk label application for each category
4. Verify messages received correct labels
5. Optionally remove deprecated old labels in bulk

### Workflow 2: Project Tagging Campaign
1. Define criteria identifying project-related messages (sender domain, subject keywords, date range)
2. Preview matching messages to verify criteria accuracy
3. Apply project label to all matching messages across folders
4. Use smart labeling to find related messages missed by explicit criteria
5. Confirm all project correspondence is consistently labeled

### Workflow 3: Label Migration
1. Identify old labels to be replaced and their new equivalents
2. For each old-to-new mapping, execute relabel operation
3. Verify messages now have new labels
4. Remove any remaining old labels in bulk
5. Document label scheme changes for reference

### Workflow 4: Cleaning Up Obsolete Labels
1. List all existing labels and identify obsolete ones
2. Preview message counts for each obsolete label
3. Decide whether to relabel (migrate) or simply remove
4. Execute bulk removal or relabeling as appropriate
5. Verify obsolete labels no longer appear on messages

## Inherited Capabilities

This skill encompasses all lower-level email labeling and organization capabilities:
- **Level 0-1**: Filtering and searching messages by criteria, reading message content
- **Level 2**: Applying labels to individual messages, setting flags, marking read/unread, managing drafts
- **Level 3**: Composing and sending emails, replying, forwarding

## Important Considerations

- Bulk operations affect many messages simultaneously; verify criteria before execution
- Preview mode is available for most bulk operations; use it to confirm scope
- Large operations may take significant time to complete
- Labels can be applied, removed, or replaced in bulk
- Criteria-based labeling applies consistently but requires precise rule definition
- Smart labeling uses content analysis which may have false positives or negatives
- Consider whether explicit criteria or content-based analysis better suits your needs
- Document bulk changes for future reference

## Limitations

- Cannot create new labels; label names must already exist in the system
- Cannot move messages between folders (use email-move skill)
- Cannot permanently delete messages
- Cannot send emails or mass communicate
- Cannot set up persistent automatic labeling rules for future incoming messages
- Cannot undo bulk label operations after execution; corrections require new bulk operations
- Cannot apply different labels to different messages within a single operation
- Cannot access accounts not configured for management

## Notes

- This is a Level 4 skill providing bulk labeling at scale
- Combine with email-search to identify messages before bulk labeling
- Combine with email-filter for metadata-based criteria definition
- For individual message labeling, Level 2 email-annotate also provides labeling capabilities
- For full mailbox management including permanent deletion, use email-manage skill
- Smart labeling is most effective when combined with preview verification
