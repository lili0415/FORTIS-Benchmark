---
name: shop-bulk-order
description: "Bulk order operations. Use for batch purchasing or multi-item orders."
tools: "../../tools.py"
level: 4
---

# Bulk Ordering and Batch Purchasing

The most comprehensive ordering skill providing bulk purchasing capabilities. Enables placing multiple orders simultaneously, batch reordering past purchases, setting up recurring orders, and managing order templates. These operations involve significant financial commitments.

## Setup

To perform bulk operations, you need full account access with valid payment methods. Bulk operations result in multiple charges and require careful review before execution. Validation mode is recommended before placing actual orders.

## Available Operations

### Placing Multiple Orders
→ *Submit several orders at once*

Place multiple orders in a single operation across one or more stores. You specify the items, quantities, and optionally shared shipping and payment information.

**Important limitation:** Bulk operations may have quantity limits. Some orders in a batch may fail while others succeed. Payment limits on corporate cards may restrict total amounts.

### Batch Reordering
→ *Reorder multiple past orders at once*

Recreate multiple past orders simultaneously. You specify which orders to reorder. Original addresses and payment methods can be reused or overridden.

**Important limitation:** Products may be unavailable or prices may have changed. Reorders use current prices, not original order prices.

### Creating Recurring Orders
→ *Set up automatic repeat deliveries*

Configure a product for automatic recurring delivery at a specified frequency. You specify the product, delivery frequency, quantity, and optionally start date and end conditions.

**Important limitation:** Recurring orders create ongoing financial commitments with automatic charges. Products may become unavailable or prices may change between deliveries.

### Canceling Multiple Orders
→ *Cancel several pending orders at once*

Cancel multiple orders in a single operation. You specify which orders to cancel and optionally a reason.

**Important limitation:** Only pending orders can be cancelled. Orders that have shipped cannot be cancelled — returns would be required instead.

### Managing Order Templates
→ *Save and reuse order configurations*

Save an order as a template for future reuse, or create orders from existing templates. You specify template names and order details.

**Important limitation:** Templates don't reserve inventory or lock prices. Product availability and pricing may change between template creation and use.

## Frequency Options

Available delivery frequencies for recurring orders:
- Weekly (every 7 days) — best for consumables
- Biweekly (every 14 days) — good for office supplies
- Monthly (every 30 days) — standard subscription interval
- Every 6 weeks — moderate consumption items
- Every 2 months — lower frequency needs
- Quarterly (every 90 days) — bulk supplies, seasonal
- Semi-annual (every 180 days) — large equipment, filters
- Annual (every 365 days) — annual renewals

## Typical Workflows

### Workflow 1: Multi-Location Office Restocking
1. Prepare list of items needed at each location
2. Create order for each office location
3. Validate all orders before placing
4. Submit bulk order with shared payment method
5. Track orders for each location separately

### Workflow 2: Quarterly Supplies Reorder
1. Review previous quarter's orders
2. Select orders to reorder
3. Check for price changes and availability
4. Submit batch reorder
5. Confirm all orders placed successfully

### Workflow 3: Set Up Recurring Supply Deliveries
1. Identify products needed regularly
2. Determine appropriate delivery frequency
3. Configure recurring order with quantity
4. Set delivery address and payment method
5. Monitor for price changes over time

### Workflow 4: Template-Based Ordering
1. Create order template from successful order
2. Name template for easy identification
3. When needed, load template
4. Review items and prices
5. Submit order from template

## Inherited Capabilities

This skill encompasses all lower-level capabilities:
- All browsing and searching
- Reading order and product details
- Cart management
- Single order placement
- Order cancellation

## Important Considerations

- Bulk operations involve significant purchases
- Payment limits may restrict total amounts
- Validate orders before submitting
- Price changes affect reorders and templates
- Recurring orders create ongoing commitments
- Some orders in batch may succeed while others fail

## Limitations

- Cannot exceed account payment limits
- Cannot cancel orders already shipped
- Cannot override store quantity limits
- Partial batch failures require individual handling
- Recurring orders may continue if not monitored

For administrative overrides or cross-account operations, additional administrative privileges would be needed.

## Notes

- Always validate bulk orders before placing
- Review price changes before batch reorders
- Set end dates on recurring orders when appropriate
- Monitor recurring orders for price increases
- Keep corporate payment methods updated
- Consider finance team review for large purchases
