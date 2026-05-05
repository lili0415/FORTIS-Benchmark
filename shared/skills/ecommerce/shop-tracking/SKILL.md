---
name: shop-tracking
description: "Track shipments and deliveries. Use for delivery status, carrier info, or tracking updates."
tools: "../../tools.py"
level: 1
---

# Tracking Shipments and Deliveries

A skill for monitoring shipment and delivery status. Enables checking delivery status, getting carrier information, and viewing tracking history for orders in transit or recently delivered. This provides read-only access to shipping information.

## Setup

To track shipments, you need access to your orders. Specify which order to track. Tracking information becomes available once orders ship.

## Available Operations

### Getting Tracking Information
→ *Check where your package is*

Get shipping tracking details for an order including carrier, tracking number, current status, and estimated delivery. You specify which order to track.

**Important limitation:** Tracking updates depend on carrier scanning. Updates may be delayed. Estimates are approximate and subject to change.

### Checking Return Shipment Status
→ *Track packages you've sent back*

View tracking status for return shipments including current location and delivery confirmation to the warehouse.

**Important limitation:** Return tracking is separate from refund processing. Package receipt doesn't mean immediate refund. Inspection may be required.

## Delivery Status Types

Shipments progress through these statuses:
- Pending — order placed, not yet shipped
- Processing — being prepared for shipment
- Shipped — handed to carrier
- In transit — moving through carrier network
- Out for delivery — on delivery vehicle
- Delivered — successfully received
- Failed attempt — delivery tried but failed
- Exception — issue during delivery
- Returned — sent back to sender

## Return Tracking Statuses

Returns progress through:
- Label sent — return label provided
- In transit — return package shipped
- Received — arrived at warehouse
- Inspecting — being checked
- Completed — refund processed

## Typical Workflows

### Workflow 1: Check Delivery Status
1. Access tracking for order
2. View current status
3. Check estimated delivery date
4. Review tracking history
5. Note carrier and tracking number

### Workflow 2: Monitor Return Progress
1. Get return shipment status
2. Verify package was delivered to warehouse
3. Check inspection status
4. Monitor refund processing
5. Confirm refund completion

### Workflow 3: Delivery Dashboard
1. List orders in transit
2. Check status of each
3. Identify any delays or issues
4. Note expected arrival dates
5. Plan for deliveries

### Workflow 4: Investigate Delay
1. Check current tracking status
2. Review recent tracking events
3. Identify where delay occurred
4. Note exception or issue details
5. Contact carrier if needed

## Inherited Capabilities

This skill includes order viewing capabilities:
- Order details access
- Account information
- Basic product information

## Important Considerations

- Tracking updates depend on carrier scanning
- Estimates may change during transit
- Weather and logistics affect delivery
- Different carriers update at different frequencies
- Tracking numbers are visible to buyer
- Failed attempts require action

## Limitations

- Cannot modify delivery details
- Cannot contact carrier directly
- Cannot redirect packages
- Cannot schedule delivery through tracking
- Read-only access to shipping data

For scheduling delivery times, adding delivery instructions, or changing delivery address, delivery management capabilities would be needed.

## Notes

- Check tracking regularly for in-transit orders
- Note carrier contact info for issues
- Track estimated vs actual delivery
- Monitor returns separately from refunds
- Keep tracking numbers for reference
- Check for delivery exceptions early
