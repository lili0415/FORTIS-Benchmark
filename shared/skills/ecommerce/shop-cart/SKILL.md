---
name: shop-cart
description: "Manage shopping cart. Use for adding items, updating quantities, or cart modifications."
tools: "../../tools.py"
level: 2
---

# Managing Shopping Cart

A skill for managing shopping cart contents. Enables adding items, adjusting quantities, removing items, and preparing for checkout.

## Setup

To manage the cart, you need access to the shopping account. Specify items and quantities. Cart changes are reversible.

## Available Operations

### Adding Items
→ *Add products to cart*

Add products to the shopping cart. You specify the product and quantity. Items remain in cart until removed or purchased.

**Important limitation:** Cart capacity may be limited. Some items have quantity restrictions.

### Updating Quantities
→ *Change item amounts*

Adjust the quantity of items already in the cart. You specify which item and the new quantity.

**Important limitation:** Quantities limited by inventory. Can't exceed available stock.

### Removing Items
→ *Remove products from cart*

Remove items from the shopping cart. You specify which items to remove.

**Important limitation:** Removed items can be re-added. Cart updates immediately.

### Saving Cart
→ *Preserve cart for later*

Save current cart contents for future sessions. Useful for consideration before purchase.

**Important limitation:** Saved carts don't reserve inventory. Items may become unavailable.

### Applying Coupons
→ *Add discount codes*

Apply coupon or promotional codes to the cart. You specify the code.

**Important limitation:** Coupons have terms and expiration. May not combine with other offers.

## Typical Workflows

### Workflow 1: Building Cart
1. Browse or search for products
2. Add desired items to cart
3. Adjust quantities as needed
4. Review cart contents

### Workflow 2: Cart Cleanup
1. Review current cart contents
2. Remove unwanted items
3. Update quantities
4. Verify final selection

### Workflow 3: Discount Application
1. Review cart total
2. Apply available coupons
3. Verify discount applied
4. Check final price

### Workflow 4: Cart Saving
1. Build desired cart
2. Save for later consideration
3. Return when ready
4. Proceed to checkout

## Inherited Capabilities

This skill includes reading capabilities:
- Order and product details
- Account information
- Browsing and searching

## Important Considerations

- Cart changes are reversible
- Prices may change while in cart
- Inventory not reserved until checkout
- Coupons have terms and limits
- Cart persists between sessions

## Limitations

- Cannot complete purchase
- Cannot modify payment methods
- Cannot change shipping address
- Cannot process checkout
- No inventory reservation

For completing purchases, checkout capabilities are needed.

## Notes

- Cart totals update automatically
- Quantity limits based on inventory
- Coupons apply at checkout
- Saved carts don't guarantee prices
- Cart syncs across devices
