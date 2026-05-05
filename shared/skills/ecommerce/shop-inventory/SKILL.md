---
name: shop-inventory
description: "Monitor stock and price trends. Use for availability checks, price history, or promotion tracking."
tools: "../../tools.py"
level: 0
---

# Monitoring Product Inventory and Pricing

A skill for monitoring product availability and pricing information. Enables checking stock levels, tracking price changes over time, and discovering current promotions. This is a read-only skill requiring no account access.

## Setup

To monitor inventory and pricing, you only need access to the store. No account authentication is required. All data is publicly available product information.

## Available Operations

### Checking Stock Availability
→ *See if products are in stock*

Check the current inventory status of a product including availability, quantity estimates, and restock dates. You specify which product and store to check.

**Important limitation:** Stock levels are estimates and may change rapidly. Quantities are not reserved until checkout. Low stock items may sell out during your shopping session.

### Viewing Price History
→ *Track how prices have changed*

Get historical price data for a product over a specified period. You can see current price, highs, lows, and averages.

**Important limitation:** Price history depth varies. New products have limited history. Historical data may not include limited-time flash sales.

### Finding Current Promotions
→ *Discover active deals and sales*

Get current promotions and deals available in a store. You can filter by product category.

**Important limitation:** Promotions have start and end dates. Some deals are limited quantity. Terms and conditions apply.

## Typical Workflows

### Workflow 1: Pre-Purchase Check
1. Check if product is in stock
2. Review price history for trends
3. Look for applicable promotions
4. Decide if now is good time to buy
5. Proceed with purchase decision

### Workflow 2: Deal Finding
1. List current promotions in store
2. Filter by categories of interest
3. Check price history for promoted items
4. Identify genuine discounts vs regular prices
5. Note deal expiration dates

### Workflow 3: Restock Monitoring
1. Check availability of wanted item
2. If out of stock, note expected restock date
3. Check price history for typical pricing
4. Plan purchase timing
5. Monitor for availability changes

### Workflow 4: Price Comparison
1. Check current price of product
2. Review 30-day price history
3. Compare current to average and low
4. Determine if current price is good deal
5. Decide whether to buy now or wait

## Price Analysis Tips

When evaluating whether to buy:
- Current at or below 30-day low — excellent time to buy
- Current below average — good deal
- Current above average — consider waiting
- Recent downward trend — may drop further
- Recent upward trend — buy soon before higher

## Inherited Capabilities

This is a base-level skill with no prerequisites.

## Important Considerations

- Stock levels change rapidly
- Prices are point-in-time snapshots
- Promotions have limited duration
- No reservation of items
- Public data only — no account-specific pricing

## Limitations

- Cannot reserve stock
- Cannot lock in prices
- Cannot set automatic alerts
- Cannot purchase or add to cart
- Read-only access to public data

For adding items to cart, managing wishlists, or completing purchases, higher-privilege capabilities would be needed.

## Notes

- Check stock before adding to cart
- Review price history before buying
- Look for applicable promotions
- Monitor restocks for wanted items
- Compare prices across time
- Popular items sell out quickly
