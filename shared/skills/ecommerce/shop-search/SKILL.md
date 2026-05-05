---
name: shop-search
description: "Search products in stores. Use for finding items by keyword, category, barcode, or filters."
tools: "../../tools.py"
level: 0
---

# Searching for Products

A skill for finding specific products using various search methods. Enables keyword search, filtered search, barcode lookup, and category filtering.

## Setup

To search for products, you need access to the shopping platform. Specify search terms or criteria. Searching is read-only and makes no purchases.

## Available Operations

### Keyword Search
→ *Find products by search terms*

Search for products matching keywords in name, description, or attributes. You specify the search terms.

**Important limitation:** Search results depend on how products are indexed. Some relevant items might not match keyword searches.

### Filtered Search
→ *Narrow results by criteria*

Apply filters to search results — by price range, brand, rating, availability, or other attributes. You specify which filters to apply.

**Important limitation:** Filter options vary by store and category. Not all attributes are filterable.

### Barcode Lookup
→ *Find product by barcode or SKU*

Look up a specific product using its barcode, SKU, or product code. Useful for finding exact items.

**Important limitation:** Requires valid product identifier. Not all products have searchable codes.

### Category Search
→ *Search within categories*

Search for products within specific categories or subcategories. You specify the category and search terms.

**Important limitation:** Product categorization varies. Some products may be in multiple or unexpected categories.

### Similar Product Search
→ *Find related products*

Find products similar to a specified item. Useful for finding alternatives or related items.

**Important limitation:** Similarity algorithms vary. Results may include loosely related items.

## Typical Workflows

### Workflow 1: Finding Specific Products
1. Enter search keywords
2. Review initial results
3. Apply filters to narrow
4. Identify target products

### Workflow 2: Price Comparison
1. Search for product type
2. Sort by price
3. Compare options
4. Note best values

### Workflow 3: Exact Product Lookup
1. Use barcode or product code
2. Verify correct product
3. Check availability
4. Note product details

### Workflow 4: Alternative Finding
1. Find initial product
2. Search for similar items
3. Compare alternatives
4. Identify best options

## Important Considerations

- Search is read-only and safe
- Results depend on indexing
- Filters vary by category
- Sort options affect ordering
- Results may include sponsored items

## Limitations

- Cannot make purchases
- Cannot add to cart
- Cannot access account details
- Cannot modify anything
- Search scope limited to indexed products

For making purchases or managing cart, higher-privilege capabilities are needed. For detailed product information or reviews, reading capabilities are required.

## Notes

- Search results may be paginated
- Filters combine to narrow results
- Sort options help prioritize
- Sponsored products may appear in results
- Search history may affect results
