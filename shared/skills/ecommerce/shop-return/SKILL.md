---
name: shop-return
description: "Process returns and refunds. Use for return requests, refund processing, or exchanges."
tools: "../../tools.py"
level: 3
---

# Processing Returns and Refunds

A skill for handling post-delivery returns, refunds, and exchanges. Enables initiating returns, tracking refund status, and arranging product exchanges. Returns involve shipping items back and processing refunds.

## Setup

To process returns, you need access to your orders. Specify which items to return and the reason. Return eligibility depends on store policy, time since delivery, and item condition.

## Available Operations

### Initiating Returns
→ *Start a return request*

Request to return items from a delivered order. You specify which items, quantities, return reason, and how you want to receive the refund.

**Important limitation:** Returns must be within the return window (typically 30 days). Some items are non-returnable (final sale, perishables, personalized items). Items must be in acceptable condition.

### Checking Return Status
→ *Track your return progress*

Get the current status of a return request including shipment tracking, inspection status, and refund processing.

**Important limitation:** Refund timing depends on when items are received and inspected. Processing typically takes 3-10 business days after receipt.

## Return Reasons

Common return reasons include:
- Wrong item received
- Wrong size or fit
- Item defective or damaged
- Not as described
- Changed mind / no longer needed
- Arrived too late
- Found better price elsewhere

## Return Status Flow

Returns progress through these stages:
- Requested — return initiated
- Approved — return authorized
- Label sent — shipping label provided
- In transit — return package shipped
- Received — item arrived at warehouse
- Inspecting — item being checked
- Completed — refund processed
- Rejected — return denied

## Refund Options

Available refund methods:
- Original payment — refund to card or method used
- Store credit — often processes faster
- Exchange — swap for different item

## Typical Workflows

### Workflow 1: Standard Return
1. Check if order is within return window
2. Initiate return with reason
3. Print prepaid shipping label
4. Ship items within deadline
5. Monitor refund processing

### Workflow 2: Size Exchange
1. Initiate return for wrong size
2. Select exchange option
3. Specify replacement item/size
4. Ship original item back
5. Receive replacement when processed

### Workflow 3: Track Refund Progress
1. Check return status
2. Verify package was delivered
3. Monitor inspection status
4. Confirm refund processing
5. Verify credit received

### Workflow 4: Defective Item Return
1. Document defect with description
2. Initiate return with defective reason
3. Ship item for inspection
4. Await verification
5. Receive full refund

## Inherited Capabilities

This skill includes order viewing capabilities:
- Order details access
- Tracking information
- Account information

## Important Considerations

- Return windows are limited
- Some items are non-returnable
- Condition affects acceptance
- Refund timing varies
- Shipping deadlines apply
- Original packaging may be required

## Limitations

- Cannot return after return window
- Cannot return non-returnable items
- Cannot guarantee exchange availability
- Cannot expedite refund processing
- Restocking fees may apply

For disputing return decisions or bulk return operations, administrative capabilities would be needed.

## Notes

- Check return policy before purchasing
- Initiate returns promptly
- Keep original packaging when possible
- Ship before deadline
- Keep tracking information
- Consider store credit for faster refunds
