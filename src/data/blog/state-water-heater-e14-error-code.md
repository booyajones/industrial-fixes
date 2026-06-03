---
title: "State Water Heater E14 Error Code - Causes & Fix"
description: "E14 signals a low-voltage control circuit fault. Most often caused by a faulty aquastat or wiring issue on terminals 7-19."
pubDatetime: 2026-05-31T15:13:05Z
modDatetime: 2026-05-31T15:13:05Z
author: "James Rutherford"
featured: false
draft: true
tags:
  - water-heater
  - state-water-heaters
---

## State Water Heater E14 Error Code — What It Means

The E14 error code indicates a disturbance on the low-voltage side of your water heater's control system. This fault is typically associated with field wiring problems, external sensors, or devices connected to the control board's low-voltage terminals. Note that E14 is not consistently documented across all State Water Heater models in manufacturer literature, so the exact definition may vary depending on your control platform. The fault is most often traced to external devices or wiring rather than the heater's internal components.

[Jump to Fix](#fix)

## Common Causes

- **Faulty dry-contact aquastat** A defective aquastat sending incorrect demand signals through the low-voltage control circuit will trigger E14.
- **Field wiring faults on terminals 7-19** Loose connections, short circuits, or damaged wiring on the low-voltage terminal strip cause control-chain disturbances.
- **Flue sensor failure** A failed or drifting flue sensor can interrupt the control circuit and generate a low-voltage fault.
- **Outdoor sensor or wiring problem** If equipped with an outdoor temperature sensor, a faulty sensor or damaged wiring will disrupt the low-voltage side.
- **X04 or X05 plug circuit issue** Intermittent connections or faults in the MCBA module plug circuits can produce E14 when the board loses continuity.
- **External control device malfunction** Any third-party device wired into the low-voltage circuit, such as zone valves or thermostats, can introduce a fault if it fails.

## Step-by-Step Fix {#fix}

1. **Reset the heater** by cycling power off for 30 seconds, then back on, and observe whether E14 returns immediately or only after the unit begins operation.
2. **Disconnect all field wiring** from terminals 7 through 19 on the control board, then reset the unit and check if the fault clears to isolate external devices.
3. **Reconnect devices one at a time**, resetting after each addition, until E14 reappears to identify the faulty device or wire run.
4. **Remove the X04 plug** from the MCBA module, reset the unit, and note whether the fault changes or disappears, indicating a problem in that circuit path.
5. **Remove the X05 plug** if the fault persists and your system has an outdoor sensor, then reset to test whether the outdoor sensor circuit is at fault.
6. **Replace the dry-contact aquastat** with a proper interface kit (such as PSRKIT-22 for Triangle Tube systems) if the water-heater demand input is identified as the source.
7. **Replace the flue sensor or outdoor sensor** if isolation steps point to one of these components, and inspect all associated wiring for damage or corrosion.

## Parts Often Needed

| Part | Notes |
|------|-------|
| PSRKIT-22 Triangle Tube IDHS aquastat kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-state-water-heater-e14-error-code&k=PSRKIT-22+Triangle+Tube+IDHS+aquastat+kit&tag=errorcodefixes-20) \| Replaces dry-contact aquastat setups when the domestic water heater input is the fault source. |
| Flue temperature sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-state-water-heater-e14-error-code&k=Flue+temperature+sensor&tag=errorcodefixes-20) \| Replace if isolation testing identifies the flue sensor circuit as the problem. |
| Outdoor temperature sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-state-water-heater-e14-error-code&k=Outdoor+temperature+sensor&tag=errorcodefixes-20) \| Required when X05 isolation points to the outdoor sensor or its wiring. |

## When to Call a Pro

Call a licensed technician if you are not comfortable working with low-voltage control wiring or if the fault persists after you have isolated and tested all field devices. A qualified service technician has the diagnostic tools and manufacturer-specific documentation to trace intermittent faults in the MCBA module, verify sensor resistance values, and replace control boards if internal circuitry is at fault. Professional help is also recommended if your water heater is still under warranty, because DIY repairs may void coverage.
