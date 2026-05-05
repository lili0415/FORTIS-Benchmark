---
name: shop-checkout
description: "Process checkout and payment. Use for placing orders or completing purchases."
tools: "../../tools.py"
level: 3
---

# Processing Checkout and Payment

A skill for completing purchases through the checkout process. Enables placing orders, selecting shipping, and processing payment. These are financial transactions that cannot be easily reversed.

## Setup

To complete checkout, you need an account with valid payment and shipping information. Specify checkout options. Purchases involve financial commitment.

## Available Operations

### Placing Orders
→ *Complete a purchase*

Process checkout to place an order for cart contents. You confirm the purchase with payment and shipping selections.

**Important limitation:** Once placed, orders cannot be canceled automatically. Returns may be required. This is a financial commitment.

### Selecting Shipping
→ *Choose delivery method*

Select shipping method and delivery options during checkout. You specify speed and delivery preferences.

**Important limitation:** Shipping options and costs vary. Express options cost more.

### Applying Payment
→ *Process payment*

Complete payment for the order using saved or specified payment methods. You confirm the payment.

**Important limitation:** Payment is processed immediately. Charges appear on your account. This is irreversible.

### Reviewing Order
→ *Confirm before purchase*

Review complete order details — items, totals, shipping, payment — before final confirmation.

**Important limitation:** Final review step before commitment. Verify all details.

## Typical Workflows

### Workflow 1: Standard Checkout
1. Review cart contents
2. Select shipping method
3. Confirm payment method
4. Place order

### Workflow 2: Gift Orders
1. Review items for gifting
2. Set gift shipping address
3. Add gift message if available
4. Complete checkout

### Workflow 3: Express Checkout
1. Verify saved defaults
2. Confirm quick checkout
3. Order placed with defaults
4. Receive confirmation

### Workflow 4: Split Shipments
1. Review items requiring different shipping
2. Configure shipment options
3. Complete checkout
4. Track multiple shipments

## Inherited Capabilities

This skill includes cart and reading capabilities:
- Cart management
- Order and product details
- Account information
- Browsing and searching

## Important Considerations

- Purchases are financial commitments
- Orders cannot be easily canceled
- Payment processes immediately
- Shipping options affect delivery time
- Verify all details before confirming

## Limitations

- Cannot undo completed purchases
- Cannot modify orders after placement
- Cannot guarantee inventory until payment
- Returns require separate process
- Payment methods must be valid

For order modifications after placement, returns, or cancellation attempts, separate capabilities are needed.

## Notes

- Order confirmation sent after purchase
- Inventory reserved at checkout
- Payment authorized and captured
- Shipping estimates are approximate
- Keep order confirmation for reference
