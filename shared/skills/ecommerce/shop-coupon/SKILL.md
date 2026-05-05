---
name: shop-coupon
description: "Manage coupons and discounts. Use for viewing, applying, or validating discount codes."
tools: "../../tools.py"
level: 2
---

# Managing Coupons and Discounts

A skill for managing promotional codes and discounts. Enables viewing available coupons, applying promotional codes to your cart, validating discount eligibility, and claiming promotional offers. These are reversible modifications — coupons can be applied and removed without permanent effects.

## Setup

To manage coupons, you need access to the customer account. Specify coupon codes when applying. Coupon operations don't commit to purchases and can be reversed.

## Available Operations

### Listing Available Coupons
→ *View your promotional codes*

List all coupons available to your account. You can filter by store or category eligibility. Results include discount type, value, expiration, and requirements.

**Important limitation:** Coupons have expiration dates and usage limits. Some are one-time use only. Availability may vary by account status or purchase history.

### Applying Coupons to Cart
→ *Add a discount code*

Apply a promotional code to your shopping cart. You specify the coupon code to use.

**Important limitation:** Most stores allow only one coupon per order. Coupons cannot be combined with other offers unless explicitly allowed. Minimum purchase requirements must be met.

### Removing Coupons from Cart
→ *Remove an applied discount*

Remove a previously applied coupon from your cart. You specify which coupon to remove.

**Important limitation:** Removing a coupon updates cart totals immediately. The coupon remains available for future use unless expired or single-use.

### Validating Coupon Codes
→ *Check if a code will work*

Check whether a coupon code is valid and what discount it provides before applying. You specify the code and optionally cart details for eligibility checking.

**Important limitation:** Validation checks current eligibility. Coupons may become invalid between validation and checkout if they expire or usage limits are reached.

### Claiming Promotional Offers
→ *Redeem a promotional coupon*

Claim a coupon from a promotional campaign or offer. You specify the promotion to claim.

**Important limitation:** Promotional offers may have limited availability. Some require specific actions or qualifications. Claimed coupons have expiration dates.

## Discount Types

Types of discounts you may encounter:
- Percentage off (e.g., 20% off cart or specific items)
- Fixed amount off (e.g., $10 off order)
- Free shipping (standard or expedited)
- Buy one get one (BOGO deals)
- Bundle discount (discount when buying multiple)
- Threshold discount (discount at cart value)

## Typical Workflows

### Workflow 1: Finding Best Discount
1. List all available coupons
2. Review cart total and contents
3. Validate eligible coupons
4. Compare potential savings
5. Apply coupon with highest discount

### Workflow 2: Checkout with Coupon
1. Review cart contents
2. Enter promotional code
3. Verify discount applied correctly
4. Confirm final total
5. Complete checkout

### Workflow 3: Coupon Discovery
1. Check available coupons for account
2. Filter by relevant categories
3. Note expiration dates
4. Claim any unclaimed offers
5. Plan purchases around best deals

### Workflow 4: Troubleshooting Invalid Coupon
1. Validate coupon to check status
2. Review error message or reason
3. Check minimum purchase requirements
4. Verify product eligibility
5. Try alternative coupon if available

## Inherited Capabilities

This skill includes cart and viewing capabilities:
- Cart management
- Product browsing
- Account information access

## Important Considerations

- Most orders accept only one coupon
- Minimum purchase requirements are common
- Product and category restrictions apply
- Coupons expire and cannot be extended
- Single-use coupons are consumed on checkout
- Promotional codes may have limited quantities

## Limitations

- Cannot create new coupons
- Cannot modify coupon terms
- Cannot combine non-stackable offers
- Cannot extend expiration dates
- Cannot recover used single-use codes

For creating coupons or bulk promotional operations, administrative capabilities would be needed.

## Notes

- Validate coupons before applying to avoid errors
- Check minimum purchase requirements early
- Review coupon expiration dates regularly
- Compare multiple coupons for best savings
- Read terms for product restrictions
- Remember one coupon per order is typical
