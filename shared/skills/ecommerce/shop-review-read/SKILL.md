---
name: shop-review-read
description: "Read product reviews and ratings. Use for viewing customer feedback or review content."
tools: "../../tools.py"
level: 1
---

# Reading Product Reviews and Ratings

A skill for accessing customer reviews and ratings. Enables viewing rating summaries, reading full review content, and analyzing customer feedback. This provides read-only access to review information to help inform purchase decisions.

## Setup

To read reviews, you need access to the store. Reviews are public information and don't require account access. Specify which product to review.

## Available Operations

### Viewing Rating Summary
→ *Get overall rating statistics*

Get aggregated rating statistics for a product including average rating, total review count, and rating distribution. You specify which product to check.

**Important limitation:** Rating summaries are aggregates. Individual review quality varies. Low review counts may not be statistically significant.

### Reading Full Reviews
→ *Access complete review content*

Get the full content of specific reviews including title, text, rating, date, and any attached photos. You specify which reviews to read.

**Important limitation:** Reviews reflect individual experiences. Verify against multiple reviews. Some reviews may be incentivized or biased.

## Typical Workflows

### Workflow 1: Quick Product Check
1. View rating summary for product
2. Check average rating and count
3. Review rating distribution
4. Read a few representative reviews
5. Make informed decision

### Workflow 2: Deep Review Analysis
1. Get product rating summary
2. Read top positive reviews
3. Read critical negative reviews
4. Identify common themes
5. Weigh pros and cons

### Workflow 3: Verified Purchase Focus
1. Retrieve sample reviews
2. Filter to verified purchases
3. Compare verified vs overall ratings
4. Focus on detailed verified reviews
5. Trust verified feedback more

### Workflow 4: Product Comparison
1. Get ratings for multiple products
2. Compare average ratings
3. Compare review counts
4. Read top reviews for each
5. Select based on feedback patterns

## Rating Distribution Analysis

When evaluating ratings:
- Mostly 4-5 stars — generally positive product
- Significant 1-2 stars — check for common complaints
- Polarized (many 5s and 1s) — product may have specific issues
- Few reviews — insufficient data for confidence
- High verified purchase rate — more trustworthy

## Inherited Capabilities

This skill includes browsing capabilities:
- Product discovery
- Search and filtering
- Basic product information

## Important Considerations

- Reviews are individual opinions
- Verified purchases are more reliable
- Low review counts lack significance
- Review dates matter for product changes
- Photos in reviews show real products
- Helpful votes indicate quality reviews

## Limitations

- Cannot post or edit reviews
- Cannot vote on review helpfulness
- Cannot report problematic reviews
- Read-only access to public data
- Cannot see private review details

For posting reviews, you need to have purchased and received the item. For reporting or voting on reviews, account interaction capabilities would be needed.

## Notes

- Check total review count for reliability
- Focus on verified purchase reviews
- Look for patterns in negative reviews
- Consider review recency
- Photos show real product condition
- Compare across similar products
