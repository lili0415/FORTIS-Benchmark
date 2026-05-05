---
name: email-audit
description: "Audit and compliance with full mailbox export, activity logging, and backup/restore."
tools: "../../tools.py"
level: 4
---

# Email Audit and Compliance Management

Full audit and compliance capabilities for enterprise email management. This skill enables comprehensive activity logging, compliance reporting, complete mailbox exports, and backup/restore operations for regulatory, legal, and organizational requirements.

## Available Operations

### Activity Logging → Retrieve history of all email actions

Access complete audit trails of email operations including sends, receives, deletes, reads, and access events. Query logs by user, time period, action type, or affected messages.

**Important limitation:** Audit data has retention limits defined by system configuration. Historical data beyond retention period is not available.

### Compliance Reporting → Generate regulatory audit reports

Create reports meeting specific compliance requirements including GDPR, HIPAA, SOX, and organizational policies. Reports cover retention verification, access audits, and communication records.

**Important limitation:** Compliance report format and scope must match applicable regulatory requirements. Generic reports may not satisfy specific audit frameworks.

### Full Mailbox Export → Create complete mailbox archives

Export entire mailbox contents including all folders, messages, attachments, and metadata. Generate archives suitable for legal hold, eDiscovery, or complete backup purposes.

**Important limitation:** Full exports can be extremely large and time-consuming for active mailboxes. Plan for adequate storage and processing time.

### Access Audit → Track who accessed what and when

Review detailed access records showing which users accessed which messages, when access occurred, and what operations were performed. Essential for security investigations and compliance verification.

**Important limitation:** Access logging granularity depends on system configuration. Some systems log folder access only rather than individual message access.

### Backup and Restore → Create and recover mailbox backups

Create point-in-time backups of mailbox state and restore from previous backups. Supports both full mailbox backup and selective message recovery.

**Important limitation:** Restore operations overwrite current state. Verify backup integrity and target scope before restoration.

### Retention Verification → Confirm policy compliance

Validate that messages meet retention requirements. Identify compliance gaps including premature deletion and failure to purge expired content.

**Important limitation:** Retention verification requires properly configured retention policies. Results reflect policy definitions, not regulatory interpretation.

## Typical Workflows

### Workflow 1: Compliance Audit Preparation
1. Identify applicable regulatory framework and requirements
2. Define audit scope (time period, users, message types)
3. Generate compliance report matching framework specifications
4. Export supporting evidence and activity logs
5. Document chain of custody for audit submission

### Workflow 2: Security Investigation
1. Define investigation scope and time window
2. Query access audit logs for relevant activity
3. Identify anomalous access patterns or unauthorized operations
4. Export detailed activity records for affected messages
5. Generate investigation summary with findings

### Workflow 3: Legal Hold and eDiscovery
1. Receive legal hold notice with scope parameters
2. Create full mailbox export for relevant custodians
3. Generate access logs covering hold period
4. Preserve chain of custody documentation
5. Verify export completeness and integrity

### Workflow 4: Disaster Recovery
1. Identify data loss scope and affected mailboxes
2. Locate appropriate backup based on timestamp
3. Verify backup integrity before restoration
4. Execute restore operation for affected content
5. Validate restored content and confirm recovery

## Inherited Capabilities

This skill encompasses all lower-level email capabilities:
- All read operations (message content, threads, attachments)
- All search and filter operations
- All export and metadata extraction
- All tracking and delivery status
- All mailbox statistics and analytics
- All message organization (move, label, archive)
- All send and compose operations
- All folder and filter management

## Important Considerations

- Audit operations can generate very large datasets
- Chain of custody requirements apply to compliance exports
- Activity logs include timestamps in UTC
- Access may be logged at message or folder level depending on configuration
- Backup operations should be scheduled during low-activity periods
- Restore operations are destructive to current state
- Retention verification depends on properly configured policies
- Consider scope (comprehensive vs. targeted) based on audit requirements

## Limitations

- Cannot exceed system-defined audit data retention periods
- Cannot access audit logs from disconnected or archived systems
- Cannot retroactively enable logging for past events
- Cannot modify audit records (immutable by design)
- Cannot guarantee recipient-side compliance or logging
- Cannot extend retention periods beyond system configuration
- Restore operations cannot recover data not present in backups

## Notes

- This is a Level 4 skill with full administrative and audit capabilities
- All audit records are immutable and tamper-evident
- Export formats include mbox, eml, pst, and json for different use cases
- Compliance reports can be customized for specific regulatory frameworks
- Backup frequency and retention should align with organizational policy
- Large-scale operations should be monitored for performance impact
