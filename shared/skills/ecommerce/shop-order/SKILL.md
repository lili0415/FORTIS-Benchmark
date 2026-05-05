---
name: shop-order
description: "Place and manage orders. Use for ordering, reordering, or order modifications."
tools: "../../tools.py"
level: 3
---

# Placing and Managing Orders

A skill for placing new orders and managing existing ones. Enables submitting orders from cart contents and canceling pending orders. Order operations are often irreversible once processing begins — these are financial transactions.

## Setup

To place orders, you need account access with valid payment and shipping information. Specify order details during submission. Orders cannot be easily reversed once placed.

## Available Operations

### Placing Orders
→ *Submit your cart for purchase*

Submit an order from your current cart contents. You confirm the purchase with selected payment and shipping options.

**Important limitation:** Once placed, orders cannot be automatically cancelled. Payment is charged immediately. Inventory is reserved at checkout but orders are final.

### Canceling Pending Orders
→ *Stop orders before they ship*

Cancel an order that hasn't yet shipped. You specify which order to cancel and optionally provide a reason.

**Important limitation:** Only pending or confirmed orders can be cancelled. Orders that have begun processing or shipping cannot be cancelled — returns would be required instead.

## Order Status Flow

Orders progress through these statuses:
- Pending — order received, awaiting processing
- Confirmed — order confirmed, preparing to ship
- Processing — being prepared for shipment
- Shipped — handed to carrier, in transit
- Delivered — successfully received
- Cancelled — order was cancelled

Cancellation is only possible in early stages (pending, confirmed, sometimes processing).

## Typical Workflows

### Workflow 1: Standard Purchase
1. Review cart contents
2. Verify shipping address
3. Confirm payment method
4. Place order
5. Save confirmation number

### Workflow 2: Quick Reorder
1. View past order details
2. Add same items to cart
3. Verify quantities and options
4. Place new order
5. Confirm successful submission

### Workflow 3: Order Cancellation
1. Check current order status
2. Verify order is cancellable
3. Submit cancellation request
4. Confirm cancellation processed
5. Verify refund initiated

### Workflow 4: Gift Order
1. Add items to cart
2. Set gift shipping address
3. Add gift options if available
4. Place order
5. Note gift receipt for recipient

## Inherited Capabilities

This skill includes cart and viewing capabilities:
- Cart management
- Order details viewing
- Product information
- Account access

## Important Considerations

- Orders are financial commitments
- Payment processes immediately
- Cancellation windows are limited
- Shipped orders cannot be cancelled
- Returns require separate process
- Keep confirmation numbers

## Limitations

- Cannot modify orders after placement
- Cannot cancel shipped orders
- Cannot guarantee inventory until payment
- Single order per submission
- Cart required with items

For returns after delivery, return capabilities would be needed. For bulk ordering or recurring orders, administrative capabilities are required.

## Notes

- Review cart before ordering
- Verify shipping address is correct
- Check payment method before submit
- Save order confirmation number
- Check cancellation policy early
- Cancel promptly if needed
