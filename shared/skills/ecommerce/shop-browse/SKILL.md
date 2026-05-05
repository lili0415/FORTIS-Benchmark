---
name: shop-browse
description: "Browse products and discover deals. Use for searching products, checking inventory, viewing ratings, or comparing prices within a store."
tools: "../../tools.py"
level: 0
---

# Browsing Products and Deals

A skill for exploring available products, checking prices, and discovering deals without making any purchases. Enables product discovery, price comparison, and inventory checking.

## Setup

To browse products, you need access to the shopping platform. Specify what you're looking for or browse by category. Browsing is read-only and makes no purchases.

## Available Operations

### Category Browsing
→ *Explore products by category*

Navigate through product categories to discover available items. You can drill down through subcategories to find specific product types.

**Important limitation:** Category structures vary by store. Some products may be in unexpected categories.

### Price Checking
→ *See current product prices*

View current prices for products including any active discounts or promotions. You specify which products to check.

**Important limitation:** Prices may change frequently. Prices shown are current but not guaranteed.

### Inventory Checking
→ *See product availability*

Check whether products are in stock and available for purchase. You specify the products to check.

**Important limitation:** Inventory can change quickly. Availability isn't guaranteed until purchase.

### Rating Viewing
→ *See product ratings and review summaries*

View aggregate ratings and review summaries for products. Helps assess product quality.

**Important limitation:** Shows summaries only. Full review text requires reading capabilities.

### Deal Discovery
→ *Find current promotions*

Discover products currently on sale or with special promotions. You can filter by category or discount level.

**Important limitation:** Deals change frequently and may have limited quantities.

## Typical Workflows

### Workflow 1: Product Discovery
1. Browse relevant categories
2. Review available products
3. Check prices and ratings
4. Note items of interest

### Workflow 2: Price Research
1. Find products of interest
2. Check current prices
3. Look for deals or discounts
4. Compare options

### Workflow 3: Availability Check
1. Identify needed products
2. Check inventory status
3. Note available options
4. Plan purchases

### Workflow 4: Deal Hunting
1. Browse current promotions
2. Filter by category or discount
3. Check deal terms
4. Note interesting offers

## Important Considerations

- Browsing is read-only and safe
- Prices and inventory change
- Deals have time limits
- Ratings reflect past experiences
- Product info may vary by store

## Limitations

- Cannot make purchases
- Cannot add to cart
- Cannot access account details
- Cannot read full reviews
- Cannot modify anything

For making purchases or accessing account information, higher-privilege capabilities are needed. For reading detailed reviews or order history, reading capabilities are required.

## Notes

- Prices may not include taxes or shipping
- Inventory shows current status
- Ratings aggregate from multiple reviewers
- Deals may have quantity limits
- Product images may vary
