---
title: "Schneider Altivar Fault OCF — Causes & Fix"
description: "What Schneider Altivar OCF fault means, why overcurrent trips the drive, and how to fix it."
pubDatetime: 2026-04-22T10:00:00Z
modDatetime: 2026-04-22T10:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - schneider
---

## Schneider Altivar Fault OCF — What It Means

OCF (Overcurrent Fault) on a Schneider Altivar drive (ATV12, ATV320, ATV630, ATV930) indicates that the output current exceeded the instantaneous overcurrent trip threshold — typically 200–300% of the drive's rated current depending on the model. OCF is a fast hardware-level protection; it trips in microseconds (unlike OLF which is thermal and time-delayed) to prevent IGBT destruction from a hard short or sudden mechanical overload.

[Jump to Fix](#fix)

## Common Causes

- **Motor short circuit** — A winding-to-winding or winding-to-ground short in the motor causes massive instantaneous current that trips OCF immediately.
- **Output cable fault** — Phase-to-phase or phase-to-ground short in the motor cable (damaged insulation, water in a junction box, cable pinched in metal conduit).
- **Mechanical jam or seizure** — A suddenly seized load (seized bearing, jammed conveyor, blocked pump) can cause a torque spike that drives current above the trip threshold.
- **Acceleration ramp too short** — If the acceleration time is set too fast for a high-inertia load, the current spike during acceleration exceeds OCF limits.

## Step-by-Step Fix {#fix}

1. **Disconnect motor and cable from drive** — Remove the motor cable at the Altivar output terminals (U, V, W). With the cable disconnected, attempt to run the drive with no output connected. If OCF immediately trips again with no output wiring, the fault is internal to the drive.
2. **Test motor insulation** — With cable disconnected at both ends, use a 500V insulation tester (Megger) between each motor terminal pair and from each terminal to ground. Values below 1 MΩ indicate failed motor insulation.
3. **Test cable insulation** — Similarly, Megger the cable conductors to each other and to shield/armor. Replace cable if any insulation value is below 10 MΩ.
4. **Increase acceleration ramp time** — If motor and cable test good, access ATV parameter ACC (acceleration ramp time) and increase it. For high-inertia loads, a longer ramp (5–30 seconds) prevents current overshoot.
5. **Check motor coupling and load** — Confirm the mechanical load is not jammed. Manually rotate the motor shaft (power off) to confirm it turns freely.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Motor cable (VFD-rated, screened)](https://www.amazon.com/s?k=Motor%20cable%20(VFD-rated%2C%20screened)&tag=errorcodefixe-20) | Replace if insulation test fails |
| [Motor (replacement or rewind)](https://www.amazon.com/s?k=Motor%20(replacement%20or%20rewind)&tag=errorcodefixe-20) | If winding short circuit is confirmed |
| [Drive output filter (dV/dt)](https://www.amazon.com/s?k=Drive%20output%20filter%20(dV%2Fdt)&tag=errorcodefixe-20) | Reduces cable stress on long runs |

## When to Call a Pro

If the drive itself trips OCF with no output connected, the internal IGBT or driver card has failed. Drive internal repair requires Schneider-authorized service or drive replacement. Always follow lockout/tagout procedures before testing output circuits.
