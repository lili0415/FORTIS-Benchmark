---
name: shop-delivery
description: "Schedule and manage deliveries. Use for setting delivery preferences or time slots."
tools: "../../tools.py"
level: 3
---

# Scheduling and Managing Deliveries

A skill for managing delivery options and scheduling. Enables viewing delivery options, selecting time slots, adding delivery instructions, and rescheduling deliveries. These changes affect live orders and may have time-sensitive deadlines.

## Setup

To manage deliveries, you need access to the order. Specify delivery preferences and timing. Changes must be made before shipping or rescheduling deadlines.

## Available Operations

### Viewing Delivery Options
→ *See available delivery choices*

Get available delivery options for an order including time slots, costs, and carrier information. You specify which order to check.

**Important limitation:** Options vary by location, order contents, and carrier availability. Premium options cost more. Popular time slots fill quickly.

### Selecting Delivery Slot
→ *Choose when to receive your order*

Select a specific delivery time slot for your order. You specify which slot to use from available options.

**Important limitation:** Slots have cutoff times for selection. Once a slot is full, it becomes unavailable. Selection must happen before processing begins.

### Adding Delivery Instructions
→ *Tell the carrier how to deliver*

Add or update delivery instructions for your order. You specify instructions like where to leave the package or how to access the building.

**Important limitation:** Instructions have character limits. Complex instructions may not be fully conveyed to carriers. Instructions are visible to delivery personnel.

### Rescheduling Delivery
→ *Change to a different delivery date*

Change the delivery date or time for an order. You specify the new preferred slot.

**Important limitation:** Rescheduling has deadlines — changes cannot be made close to delivery time. Some changes may incur fees. Not all orders can be rescheduled.

### Setting Safe Place
→ *Designate where to leave packages*

Specify a safe location for package delivery when you're not home. You specify the location description and whether to require photo confirmation.

**Important limitation:** Safe place waivers affect liability. Choose secure, weather-protected locations. Photo proof provides delivery confirmation.

## Delivery Types

Available delivery options typically include:
- Standard (5-7 days) — most economical
- Express (2-3 days) — faster but costlier
- Next day — premium speed option
- Same day — available in metro areas
- Scheduled — specific date and time slot
- Pickup — collect from designated location

## Typical Workflows

### Workflow 1: Schedule Convenient Delivery
1. View available delivery options
2. Find slots matching your availability
3. Select preferred time slot
4. Add delivery instructions if needed
5. Confirm scheduled delivery

### Workflow 2: Add Building Access Info
1. Access order delivery settings
2. Add building entry instructions
3. Include access code if needed
4. Provide alternative contact number
5. Verify instructions are saved

### Workflow 3: Reschedule Conflicting Delivery
1. Check current delivery schedule
2. Review available alternative slots
3. Select new delivery time
4. Confirm rescheduling accepted
5. Note any fees if applicable

### Workflow 4: Set Up Safe Place Delivery
1. Access delivery preferences
2. Describe safe delivery location
3. Request photo confirmation
4. Waive signature if appropriate
5. Verify settings are saved

## Inherited Capabilities

This skill includes order viewing capabilities:
- Order details access
- Tracking information
- Account information

## Important Considerations

- Changes have time-sensitive deadlines
- Rescheduling may incur fees
- Premium delivery costs more
- Instructions are shared with carriers
- Safe place waivers affect liability
- Access codes should be temporary if possible

## Limitations

- Cannot change delivery after shipping
- Cannot modify orders directly
- Cannot guarantee specific times
- Cannot control carrier behavior
- Rescheduling limited to available slots

For canceling orders or modifying order contents, order management capabilities would be needed. For returns after delivery, return capabilities are required.

## Notes

- Select delivery slots early for best options
- Add clear, specific instructions
- Check rescheduling deadlines before changing
- Consider weather for outdoor safe places
- Provide accurate contact information
- Keep confirmation details for reference
