---
name: shop-account
description: "Manage account settings. Use for profile updates, preferences, or payment methods."
tools: "../../tools.py"
level: 2
---

# Managing Account Settings

A skill for managing account settings and preferences. Enables viewing and updating profile information, managing notification preferences, and configuring account settings. These are reversible modifications — profile and preference changes can be updated or reverted without permanent effects.

## Setup

To manage account settings, you need access to the customer account. Specify what settings to view or change. Account modifications are reversible but may trigger verification requirements.

## Available Operations

### Viewing Profile Information
→ *Access current account profile details*

Retrieve current profile information including name, email, phone, and membership status. You specify which account to access.

**Important limitation:** Some profile details may require additional verification to view. Sensitive information like full payment details are not exposed.

### Updating Profile Information
→ *Change profile details*

Update account profile fields including display name, email address, phone number, or birthday. You specify which fields to change and their new values.

**Important limitation:** Changing email or phone may require verification. Some fields like account ID cannot be modified. Multiple verification requests may be rate-limited.

### Viewing Preferences
→ *Check current account preferences*

Access account preference settings including language, currency, timezone, and privacy settings. You specify which account's preferences to view.

**Important limitation:** Preference options vary by store. Not all settings may be available for modification.

### Updating Preferences
→ *Change account preferences*

Modify preference settings including language, currency, timezone, shopping preferences, and privacy settings. You specify which preferences to change.

**Important limitation:** Some preference changes take effect on next session. Privacy setting changes may affect personalization features.

### Viewing Payment Methods
→ *List saved payment options*

View saved payment methods associated with the account. You can see payment types, last four digits, and default status.

**Important limitation:** This operation is read-only. Full card numbers are never exposed. Adding or removing payment methods requires higher privileges.

### Updating Notification Settings
→ *Configure how you receive updates*

Manage notification preferences for email, SMS, and push notifications. You specify which channels and notification types to enable or disable.

**Important limitation:** Order and shipping notifications cannot be completely disabled for compliance. Some changes require verification.

## Typical Workflows

### Workflow 1: Complete Profile Setup
1. View current profile information
2. Update missing fields like phone or birthday
3. Set preferred language and currency
4. Configure notification preferences
5. Review changes for accuracy

### Workflow 2: Privacy-Focused Settings
1. Review current privacy settings
2. Disable personalization features
3. Opt out of third-party data sharing
4. Minimize promotional notifications
5. Keep only essential order notifications

### Workflow 3: Contact Update
1. View current contact information
2. Update email or phone number
3. Complete verification process
4. Confirm changes are active
5. Update notification preferences if needed

### Workflow 4: Preferences Audit
1. List current preferences
2. Review notification settings
3. Check privacy configurations
4. Update outdated settings
5. Verify payment method expiration dates

## Inherited Capabilities

This skill includes viewing capabilities:
- Browsing and searching
- Product and order viewing
- Account information access

## Important Considerations

- Profile changes are reversible but logged
- Email and phone changes require verification
- Payment method details are masked for security
- Some changes may trigger security notifications
- Two-factor authentication may be required for sensitive changes

## Limitations

- Cannot add or remove payment methods
- Cannot delete the account
- Cannot change account password
- Some fields are immutable
- Verification requests may be rate-limited

For adding or removing payment methods, managing linked accounts, or account deletion, administrative capabilities would be needed.

## Notes

- Keep contact information current for order updates
- Verify email and phone for account security
- Review notification settings periodically
- Check payment method expiration dates
- Add birthday for potential promotional benefits
