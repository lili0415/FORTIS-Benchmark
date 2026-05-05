---
name: shop-read
description: "Read order and product details. Use for viewing order info, product specs, or account data."
tools: "../../tools.py"
level: 1
---

# Reading Order and Product Details

A skill for accessing detailed information about orders, products, and account status. Enables viewing order history, detailed product specs, and account information.

## Setup

To read shopping information, you need access to the account. Specify what information to access. Reading is non-destructive.

## Available Operations

### Order History
→ *View past orders*

Access your complete order history including items, dates, and status. You can filter by date or status.

**Important limitation:** History depth may be limited. Very old orders may have reduced detail.

### Order Details
→ *View specific order information*

Get detailed information about a specific order — items, pricing, shipping, and status. You specify which order.

**Important limitation:** Some details only available for recent orders. Tracking info may expire.

### Product Details
→ *Read full product specifications*

Access comprehensive product information — specifications, features, variants, and complete descriptions.

**Important limitation:** Product information may change. Specs reflect listing at time of viewing.

### Full Reviews
→ *Read complete customer reviews*

Access full review text, ratings, and reviewer information. You specify which product.

**Important limitation:** Reviews reflect individual experiences. Verify against multiple reviews.

### Account Information
→ *View account settings and status*

Access account information including profile, preferences, and membership status.

**Important limitation:** Some account details may require additional verification.

## Typical Workflows

### Workflow 1: Order Tracking
1. Access order history
2. Find relevant order
3. View order details
4. Check current status

### Workflow 2: Product Research
1. Find product of interest
2. Read detailed specifications
3. Review customer feedback
4. Make informed decision

### Workflow 3: Purchase History
1. Access order history
2. Filter by date or type
3. Review past purchases
4. Note patterns or needs

### Workflow 4: Account Review
1. Access account information
2. Review settings and preferences
3. Check membership status
4. Note any needed updates

## Inherited Capabilities

This skill includes browsing capabilities:
- Product browsing and discovery
- Price and inventory checking
- Deal discovery

## Important Considerations

- Reading is non-destructive
- Order history may be extensive
- Product details change over time
- Reviews are individual opinions
- Account info may be sensitive

## Limitations

- Cannot modify orders
- Cannot make purchases
- Cannot change account settings
- Cannot add reviews
- Read-only access

For modifying orders or making purchases, higher-privilege capabilities are needed.

## Notes

- Order status updates over time
- Shipping tracking varies by carrier
- Product variants may have different specs
- Review helpfulness can guide reading
- Account history comprehensive
