---
name: email-signature
description: "Create, edit, and manage email signatures for consistent, professional message endings."
tools: "../../tools.py"
level: 2
---

# Email Signature Management

Manage email signatures to ensure consistent, professional endings on your outgoing messages. This skill provides full control over signature creation, editing, defaults, and organization.

## Available Operations

### Create Signature
Create new signatures with your name, title, contact information, and custom content.

**Important limitation:** Signatures are created but not sent. Actual email sending requires Level 3 permissions.

### View Signatures
List all configured signatures and see which is set as default for new messages and replies.

**Important limitation:** Read-only access to signature configuration. Cannot view email content or message history.

### Update Signature
Modify existing signatures when contact details, titles, or disclaimers change.

**Important limitation:** Updates apply only to future messages. Previously sent emails retain their original signatures.

### Set Default Signature
Configure which signature auto-attaches to outgoing messages. Separate defaults can be set for new messages versus replies.

**Important limitation:** Setting defaults does not trigger any email sending. Signatures apply when messages are composed.

### Delete Signature
Remove signatures that are no longer needed to keep your signature library organized.

**Important limitation:** Deletion is permanent. Cannot recover deleted signatures without recreating them.

## Typical Workflows

### Creating a Professional Signature
Design a polished signature with appropriate contact information and formatting. Include name, title, phone, and email. Add company logo or social links if appropriate. Set as default for new messages.

### Managing Multiple Context Signatures
Create distinct signatures for different situations: formal business communications, internal team messages, personal correspondence. Configure appropriate defaults and switch signatures as needed when composing.

### Updating Contact Information
When job title, phone number, or other details change, update all affected signatures. Review each signature to ensure consistency. Verify default settings remain appropriate.

### Adding Compliance Disclaimers
Include required legal text or confidentiality notices. Position disclaimer appropriately within signature. Ensure compliance text appears on all relevant outgoing message types.

## Important Considerations

- Signature length affects message readability; keep content concise
- Images embedded in signatures may not display in all email clients
- HTML formatting may render differently across email platforms
- Consider mobile display when designing signature layout
- Review signatures periodically to ensure information remains accurate

## Limitations

- Cannot send emails or access email content (Level 3 required)
- Cannot recover deleted signatures
- Cannot modify signatures on already-sent messages
- Cannot access signatures on accounts you do not own
- Cannot guarantee formatting consistency across all recipient email clients

## Notes

- Default signatures attach automatically unless overridden during composition
- Multiple signatures allow matching tone and detail level to context
- Signature changes apply immediately to new compositions
- Consider both new message and reply defaults separately
