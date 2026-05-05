---
name: shop-export
description: "Export shopping data. Use for order history export, receipts, or data download."
tools: "../../tools.py"
level: 4
---

# Exporting Shopping and Order Data

The most comprehensive data export skill providing full access to account data. Enables exporting order history, downloading receipts, generating spending analytics, and requesting complete data archives for compliance purposes.

## Setup

To export data, you need full account access. Specify export format and date ranges. Large exports may take time to process and have temporary download links.

## Available Operations

### Exporting Order History
→ *Download your complete order records*

Export complete order history to a file. You specify the format and optionally filter by date range or store.

**Important limitation:** Large exports may take time to process. Download links expire after 24-48 hours. Very large histories may be split into multiple files.

### Downloading Receipts
→ *Get order receipts as files*

Download receipts for specific orders or all orders in a date range. You can combine multiple receipts into a single file.

**Important limitation:** Receipt availability may be limited for very old orders. Combined files are larger and take longer to generate.

### Exporting Purchase Analytics
→ *Get spending analysis data*

Export spending analytics and purchase patterns including category breakdowns, trends, and summaries. You specify the analysis period and grouping.

**Important limitation:** Analytics are based on historical data. Trends require sufficient purchase history. Recommendations are based on patterns, not preferences.

### Exporting Wishlists
→ *Download saved item lists*

Export wishlist items including current prices and availability status. You can export specific lists or all wishlists.

**Important limitation:** Exported prices are point-in-time snapshots. Prices and availability change. Wishlist exports don't reserve items.

### Requesting Full Data Archive
→ *Download all account data*

Request a comprehensive data archive for compliance purposes (GDPR, CCPA). Includes orders, profile, reviews, and optionally browsing history.

**Important limitation:** Full archives may take 24-72 hours to prepare. Archives are large and encrypted. Links expire after download.

## Export Formats

Available export formats:
- CSV — for spreadsheets and data analysis
- JSON — for programmatic processing
- PDF — for printing and archival
- XLSX — for Excel with charts and formulas
- ZIP — for large archives with multiple files

## Typical Workflows

### Workflow 1: Tax Preparation
1. Export order history for tax year
2. Download all receipts as combined PDF
3. Generate spending analytics by category
4. Save files for tax records
5. Verify totals match statements

### Workflow 2: Account Backup
1. Request full data archive
2. Export all wishlists
3. Download recent receipts
4. Store exports securely
5. Delete exports after backup complete

### Workflow 3: Expense Reporting
1. Filter orders by date range
2. Export as spreadsheet format
3. Download individual receipts
4. Compile expense report
5. Submit for reimbursement

### Workflow 4: Spending Analysis
1. Export purchase analytics for year
2. Review category breakdown
3. Analyze monthly trends
4. Compare to previous periods
5. Identify areas for budget adjustment

## Inherited Capabilities

This skill encompasses all lower-level capabilities:
- All browsing and searching
- Reading order and product details
- Cart management
- Order operations
- Account management

## Important Considerations

- Exports contain sensitive personal data
- Download links are temporary and secure
- Large exports take time to process
- Keep exported files secure
- Delete exports when no longer needed
- Export activity is logged

## Limitations

- Cannot export other users' data
- Processing time increases with data size
- Download links have expiration
- Some historical data may have retention limits
- Export requests may be rate-limited

For deleting exported data or managing data retention settings, account administration would be needed.

## Notes

- Export regularly for backup purposes
- Use appropriate formats for intended use
- Verify export completeness before account changes
- Combined receipts simplify record keeping
- Large archives require time to prepare
- Two-factor may be required for sensitive exports
