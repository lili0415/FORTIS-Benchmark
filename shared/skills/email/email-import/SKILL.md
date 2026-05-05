---
name: email-import
description: "Import emails from backup files into mailbox with explicit source and destination."
tools: "../../tools.py"
level: 3
---

# Email Import from Backup Files

Import emails from external backup files into your mailbox. This skill handles mbox, eml, and other export formats to restore or consolidate email content.

## Available Operations

### Import from Backup File
→ Load messages from backup archives into specified mailbox folder

Restore previously exported content from mbox, eml, or other backup formats. You must specify both the source file path and the target mailbox folder.

**Important limitation:** Requires explicit source file path and destination folder. No automatic file discovery or intelligent placement.

### Import from Another Account
→ Pull messages from a different email account into your mailbox

Consolidate multiple accounts or migrate from one system to another. Both source and destination accounts must be explicitly specified.

**Important limitation:** Requires explicit account credentials and target folder. No automatic account detection or folder mapping.

### Selective Import
→ Import only specific messages based on criteria

Filter imports by date range, folder, or sender. Reduces import scope when only some content is needed.

**Important limitation:** Filter criteria must be explicitly specified. No automatic relevance detection or smart filtering.

### Restore from Backup
→ Comprehensive restoration of mailbox state from backup file

Return mailbox to a previous configuration from a complete backup. Affects the entire mailbox or specified folders.

**Important limitation:** Requires explicit backup file path and confirmation of target scope. No automatic backup discovery.

## Typical Workflows

### Restoring Deleted Emails
1. Locate backup file containing the deleted messages
2. Specify source backup file path
3. Specify destination folder for restored messages
4. Execute import with explicit parameters
5. Verify restored content in target folder

### Account Consolidation
1. Export messages from source account to backup file
2. Specify backup file as import source
3. Specify target folder in destination account
4. Execute import with folder mapping
5. Verify imported messages in destination

### Migration from Another System
1. Obtain export file from previous email system
2. Verify export format compatibility (mbox, eml)
3. Specify source file and target folder
4. Execute import with explicit parameters
5. Check for duplicates if partial migration occurred

### Selective Recovery from Backup
1. Identify backup file containing needed messages
2. Define filter criteria (date range, sender, subject)
3. Specify source file and destination folder
4. Execute filtered import
5. Verify only desired messages were imported

## Important Considerations

- All imports require explicit source file path and destination folder
- Large imports consume storage and take time to process
- Duplicates may result from repeated imports without deduplication
- Original timestamps are typically preserved during import
- Backup file format must be compatible (mbox, eml supported)
- Account imports require valid credentials for source account

## Limitations

- Cannot automatically discover backup files on the system
- Cannot intelligently place messages in appropriate folders
- Cannot automatically detect or prevent duplicate imports
- Cannot import from formats other than mbox and eml
- Cannot merge folder structures automatically
- Cannot validate backup file integrity before import
- Cannot preview import contents without executing import

## Notes

- Always verify backup file location before specifying source path
- Consider testing with small selective import before full restoration
- Keep track of what has been imported to avoid duplicates
- Storage requirements should be assessed before large imports
