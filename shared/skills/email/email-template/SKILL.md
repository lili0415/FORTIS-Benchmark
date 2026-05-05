---
name: email-template
description: "Create, manage, and apply reusable email templates to drafts."
tools: "../../tools.py"
level: 2
---

# Email Template Management

Create and manage reusable email templates for consistent, efficient correspondence. Templates support placeholders for customization and can be applied to create draft messages ready for review.

## Available Operations

### Create Template
→ Save a new reusable message structure with placeholders for variable content.

**Important limitation:** Templates are stored locally and cannot be shared across accounts or exported to other email systems.

### Apply Template
→ Use a saved template to create a new draft message, filling in placeholder values.

**Important limitation:** Templates can only create drafts for review; they cannot send emails directly.

### List Templates
→ View all saved templates with their names, descriptions, and placeholder definitions.

**Important limitation:** Template search is by exact name match only; no fuzzy or content-based search is available.

### Update Template
→ Modify an existing template's content, placeholders, or metadata.

**Important limitation:** Updating a template does not affect drafts already created from that template.

### Delete Template
→ Remove a template from the library permanently.

**Important limitation:** Deletion is immediate and cannot be undone; no confirmation prompt is provided by the tool.

## Typical Workflows

### Creating a Standard Response Template
1. Identify repetitive message patterns (e.g., meeting confirmations, inquiry responses)
2. Draft the template content with placeholders (e.g., `{{recipient_name}}`, `{{meeting_date}}`)
3. Create the template with a descriptive name
4. Test by applying the template to create a sample draft

### Applying Templates for Outreach
1. List available templates to find the appropriate one
2. Apply the template with specific placeholder values
3. Review the created draft for accuracy
4. Edit the draft if needed before sending via another method

### Maintaining Template Library
1. Periodically review all templates for accuracy
2. Update templates with outdated content or messaging
3. Delete templates that are no longer useful
4. Create new templates as communication patterns emerge

### Using Templates for Consistent Replies
1. Identify incoming message categories that warrant templated responses
2. Create templates for each response category
3. When a matching message arrives, apply the appropriate template
4. Customize placeholder values and review the draft before proceeding

## Important Considerations

- Templates save composition time but require upfront investment to create
- Well-designed placeholders balance standardization with necessary personalization
- Regular maintenance keeps the template library valuable and current
- Template names should be descriptive for easy identification
- Consider versioning important templates by including dates in names

## Limitations

- Cannot send emails; can only create drafts for review
- Cannot access or modify sent messages
- Cannot share templates with other users or accounts
- Cannot import templates from external sources
- Cannot schedule template application or automate responses
- Cannot attach files to templates; attachments must be added to drafts separately
- Cannot integrate with external CRM or contact management systems

## Notes

- Placeholders use double-brace syntax: `{{placeholder_name}}`
- Applied templates always create drafts, never send directly
- Template content should be reviewed periodically for accuracy
- Drafts created from templates can be edited before sending via other means
