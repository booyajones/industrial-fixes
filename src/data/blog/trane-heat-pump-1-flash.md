---
title: "Trane Heat Pump 1 Flash Error Code — Causes & Fix"
description: "What Trane heat pump 1 flash error code means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - trane
---

## Trane Heat Pump 1 Flash Error Code — What It Means

A single LED flash on a Trane heat pump control board indicates a system lockout — the unit has exceeded its allowed fault retries and has locked itself out of operation. Unlike a specific component fault code, 1 flash is the board's way of saying "I've tried and failed too many times; manual intervention required." The root cause fault occurred earlier in the sequence. To diagnose properly, you need to clear the lockout, observe what happens on the next operational attempt, and catch the specific fault before it escalates back to lockout. Common culprits include refrigerant issues, defrost board problems, and outdoor fan faults.

[Jump to Fix](#fix)

## Common Causes

- **Low refrigerant / system pressure fault** — A refrigerant leak causes the low-pressure switch to open during a heating or cooling cycle, triggering a fault that accumulates into lockout after repeated trips.
- **Defrost system fault** — The defrost board or defrost sensor fails, causing the heat pump to either attempt defrost at the wrong time or fail to complete a defrost cycle, leading to coil icing and pressure faults.
- **Outdoor fan motor failure** — Without outdoor fan operation, heat exchange is disrupted and high-pressure or low-pressure trips follow quickly, driving the unit into lockout.
- **High-pressure switch trip** — In cooling mode, a dirty condenser coil or failed outdoor fan can cause head pressure to spike and trip the high-pressure cutout, accumulating into lockout.

## Step-by-Step Fix {#fix}

1. **Clear the lockout** — Shut off the heat pump at the outdoor disconnect or breaker for at least 30 seconds. Restore power. This resets the lockout counter and allows the system to attempt another cycle.
2. **Watch the unit on next startup** — Stand at the outdoor unit and observe. Does the outdoor fan run? Does the compressor start? Are there any abnormal sounds? Note exactly when and how the unit faults on the next attempt.
3. **Check outdoor fan operation** — With the unit calling for cooling or heating, confirm the outdoor fan blade is spinning. A failed fan motor will cause rapid high-pressure or low-pressure trip depending on mode.
4. **Look for ice on the outdoor coil** — In heating mode, some frost on the outdoor coil is normal. A fully ice-encased coil that never defrosted indicates a defrost system failure.
5. **Check system pressures** — With a manifold gauge set, measure suction and discharge pressures. Low suction in heating mode indicates a refrigerant leak or a metering device problem.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Outdoor fan motor](https://www.amazon.com/s?k=Outdoor%20fan%20motor&tag=errorcodefixe-20) | Match HP, RPM, rotation direction, and shaft diameter |
| [Defrost control board](https://www.amazon.com/s?k=Defrost%20control%20board&tag=errorcodefixe-20) | Replace if defrost times out or never initiates |
| [Defrost thermostat (sensor)](https://www.amazon.com/s?k=Defrost%20thermostat%20(sensor)&tag=errorcodefixe-20) | Clip-type sensor on outdoor coil; fails open or closed |

## When to Call a Pro

Refrigerant work requires EPA 608 certification. If the lockout is being driven by a pressure fault rather than an electrical component failure, a licensed technician must inspect the refrigerant circuit, identify leaks, and recharge to the correct specification.
