---
title: "SEW-Eurodrive Fault F08 — Causes & Fix"
description: "What SEW-Eurodrive fault F08 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - sew-eurodrive
---

## SEW-Eurodrive Fault F08 — What It Means

SEW-Eurodrive fault F08 is a DC link overvoltage fault (also documented as "DC bus overvoltage" in SEW's MOVITRAC and MOVIDRIVE manuals). The drive's DC bus voltage exceeded the maximum permissible level — typically around 820–840V DC on 480V class drives. Overvoltage on the DC bus is almost always caused by regenerative energy from the motor being pumped back into the drive's bus capacitors faster than the dynamic braking resistor (if installed) can dissipate it, or by a utility supply voltage that is consistently above the drive's maximum rated input.

[Jump to Fix](#fix)

## Common Causes

- **Motor decelerating too quickly (regeneration)** — When a motor driving a high-inertia load (fan, flywheel, conveyor) is commanded to decelerate faster than the load can coast, the motor acts as a generator and pumps energy back into the DC bus. If no braking resistor is installed or it's undersized, bus voltage spikes to F08 levels.
- **Braking resistor undersized or failed** — The dynamic braking resistor (connected to the brake chopper output) is responsible for dissipating regenerative energy as heat. An undersized resistor, a failed braking resistor, or a tripped thermal overprotection on the resistor leaves the bus voltage with no discharge path.
- **High incoming line voltage** — If the utility supply voltage is consistently above 480V (e.g., running at 500–510V), the DC bus at rest already sits near the maximum, and any regeneration pushes it over the F08 threshold.
- **Drive deceleration ramp too short** — The programmed deceleration time is too aggressive for the load inertia. The drive commands a fast stop, but the load's momentum overpowers the braking system.

## Step-by-Step Fix {#fix}

1. **Extend the deceleration time** — In SEW MOVITRAC B or MOVIDRIVE B parameters, increase the deceleration ramp time (parameter P135 on MOVITRAC B). Allow the load to decelerate more gradually. Start with 2–3× the current setting and reduce from there.
2. **Verify braking resistor is installed and functional** — If the drive has a brake chopper output (BK+/BK− terminals), confirm a correctly rated braking resistor is connected. Check resistor continuity and confirm the thermal protection contact is closed.
3. **Measure supply voltage at the drive input** — Check L1, L2, L3 at the drive terminals with a true-RMS voltmeter. Elevated line voltage (>500V on a 480V drive) requires either an autotransformer to reduce supply voltage or a higher voltage-rated drive.
4. **Check brake chopper operation** — During a deceleration event, measure the DC bus voltage with a scope or high-speed data logger. If the bus reaches the F08 threshold but the brake chopper never activates (no current through the braking resistor), the brake chopper circuit has failed.
5. **Upsize the braking resistor if undersized** — Calculate the required braking resistor using SEW's sizing tool (SEW DriveSize software). The resistor must handle the peak and average regenerative power of the application.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Braking resistor (correctly sized) | Use SEW DriveSize or the manual's sizing table; get peak and average power correct |
| Brake chopper transistor / module | Replace if brake chopper output is confirmed not activating during regen |
| Autotransformer (step-down) | Install at drive input if line voltage consistently exceeds drive rating |

## When to Call a Pro

If F08 occurs on a high-inertia application like a centrifuge or large conveyor and extending the decel ramp is not acceptable for the process, a regenerative drive unit (capable of feeding energy back to the utility) may be required. This is a system design decision that requires an application engineer.
