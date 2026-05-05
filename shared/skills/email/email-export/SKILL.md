---
name: email-export
description: "Export email messages, metadata, and attachments to external formats for backup or analysis."
tools: "../../tools.py"
level: 1
---

# Email Export - Extract Mailbox Data for Backup, Analysis, or Migration

Export email data from your mailbox into external file formats. This skill enables backup creation, data extraction for analysis, compliance archiving, and migration preparation. All operations are read-only and do not modify or delete any mailbox content.

## Available Operations

### Export Messages → Save emails to external file formats

Extract messages from folders and save them as mbox, eml, json, or other portable formats. Export scope ranges from individual messages to entire folders to complete mailbox dumps.

**Important limitation:** Exported files are created outside the mailbox. The original messages remain unchanged in the mailbox.

### Export Metadata → Extract message information without bodies

Pull sender, recipient, date, subject, flags, and other header information without downloading full message content. Useful for lightweight analysis or indexing.

**Important limitation:** Metadata exports do not include message bodies or attachments. For full content, use message export instead.

### Export Attachments → Save attached files separately

Extract attachments from messages and save them as standalone files. Can be combined with message export or performed independently.

**Important limitation:** Attachments are copied out; they remain attached to the original messages in the mailbox.

### Export for Compliance → Create audit-ready archives

Generate exports with chain of custody documentation, timestamps, and complete records suitable for legal discovery or regulatory compliance.

**Important limitation:** Compliance exports are point-in-time snapshots. New messages arriving after export are not included.

## Typical Workflows

### Creating Backups

Create comprehensive backups of mailbox content for disaster recovery. Consider whether to include all folders or just critical ones, whether attachments are needed, and what format supports future restoration. Mbox format is widely compatible; eml preserves individual messages as separate files.

### Exporting for Analysis

Extract data for external analysis tools. Metadata-only exports are faster and smaller when full bodies are not needed. JSON format integrates well with data analysis pipelines. Define the time period and folder scope to match analysis requirements.

### Compliance and Legal

Generate defensible records for regulatory or legal requirements. Include chain of custody metadata, cover the required time period comprehensively, and choose formats that preserve message integrity. Document the export process for audit trails.

### Migration Preparation

Prepare mailbox content for transfer to another email system. Match the export format to what the target system accepts. Decide whether to migrate everything or only recent items. Plan for duplicate handling on the destination side.

## Important Considerations

- Export formats vary in compatibility with other email systems
- Large exports require significant time and storage space
- Including attachments dramatically increases export size
- Exports are point-in-time snapshots; subsequent changes are not captured
- Choose scope (comprehensive vs. targeted) based on specific needs
- Verify export integrity after completion for critical backups

## Limitations

- Cannot modify or delete messages in the mailbox
- Cannot move messages between folders
- Cannot change message flags or status
- Cannot edit message content or headers
- Cannot send messages or create drafts
- Cannot manage mailbox structure (create/delete folders)
- Cannot perform any write operations on the mailbox

## Notes

- This is a Level 1 (read-only) skill with no mailbox modification capabilities
- All operations extract copies of data; originals remain untouched
- Export operations may be slow for large mailboxes or folders with many attachments
- Consider incremental exports for ongoing backup strategies
