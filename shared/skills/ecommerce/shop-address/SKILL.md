---
name: shop-address
description: "Manage shipping addresses. Use for address book operations, adding or updating addresses."
tools: "../../tools.py"
level: 2
---

# Managing Shipping Addresses

A skill for managing shipping addresses in your address book. Enables adding new addresses, updating existing ones, and setting default preferences for quick checkout.

## Setup

To manage addresses, you need access to the customer account. Specify address details when adding or updating. Address operations are reversible.

## Available Operations

### Adding New Addresses
→ *Save a new shipping address*

Save a new shipping address to your address book. You specify recipient name, street address, city, postal code, country, and contact phone. You can optionally label the address and set it as default.

**Important limitation:** Address format validation may reject improperly formatted entries. Some fields like postal code have country-specific formats.

### Updating Existing Addresses
→ *Modify a saved address*

Update fields of an existing address. You specify which address to update and which fields to change.

**Important limitation:** The address must exist in your address book. Changes affect future orders using this address but not existing orders.

### Listing All Addresses
→ *View saved addresses*

List all saved addresses in your address book. You can filter by address type (shipping, billing, or both).

**Important limitation:** Large address books may be paginated. Results show summary information — use specific address lookup for full details.

### Viewing Address Details
→ *Get complete address information*

Retrieve full details of a specific address including all fields and settings. You specify which address to view.

**Important limitation:** Address details are only visible to the account owner. Some sensitive details may be partially masked.

### Setting Default Address
→ *Change which address is used by default*

Update which address is used as the default for checkout. You specify which address should become the default.

**Important limitation:** Only one address can be default per type. Setting a new default automatically removes default status from the previous one.

## Typical Workflows

### Workflow 1: Add Home and Office Addresses
1. Add home address with full details
2. Set home address as default
3. Add office address with work contact info
4. Label addresses for easy identification
5. Verify both addresses are saved correctly

### Workflow 2: Move to New Address
1. List current addresses
2. Add new address with complete details
3. Set new address as default
4. Update or remove old address
5. Verify upcoming orders use new address

### Workflow 3: Gift Recipient Setup
1. Add recipient's address with their name
2. Label as gift recipient
3. Include recipient's phone number
4. Verify address format is correct
5. Use for gift orders

### Workflow 4: Address Correction
1. View address details to identify errors
2. Update incorrect fields
3. Verify postal code format
4. Confirm changes are saved
5. Check that default status is preserved

## Address Format Guidelines

Required information for addresses:
- Recipient name (who receives the package)
- Street address (include apartment or suite)
- City name
- Postal or ZIP code (format varies by country)
- Country
- Contact phone (include country code)

Optional but recommended:
- Label for easy identification (Home, Office, etc.)
- Secondary address line if needed

## Important Considerations

- Address validation may reject invalid formats
- Postal code formats vary by country
- Phone numbers should include country codes
- Labels help identify addresses quickly
- Default address is used automatically at checkout

## Limitations

- Cannot delete addresses with this skill
- Cannot use addresses for orders directly
- Address validity is not verified against postal services
- Only one default address per type
- Addresses are isolated to your account

For removing addresses from the address book, account management capabilities would be needed. For using addresses in orders, checkout capabilities are required.

## Notes

- Keep addresses updated when moving
- Include apartment numbers in street field
- Use consistent formatting for easier management
- Verify recipient names match expected delivery
- Phone numbers help carriers reach recipients
