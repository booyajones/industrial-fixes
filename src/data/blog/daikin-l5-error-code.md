---
title: "Daikin L5 Error Code — Compressor Lock Fault"
description: "Daikin error code L5 means the compressor is locked or has failed to start. Learn the exact causes, diagnostic steps, and how to fix Daikin L5."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - daikin
  - mini-split
  - compressor
---

# Daikin Error Code L5 — Compressor Lock Fault

**Error Code L5** on Daikin inverter-driven mini-split and VRV systems means the compressor motor has failed to start (locked rotor) or has drawn excessive current during startup. The inverter drive detected that the compressor is not rotating correctly and shut down to prevent motor damage.

## Jump to Fix

- [Most Likely Cause](#most-likely-cause)
- [Diagnosis Steps](#diagnosis)
- [Parts](#parts)

## What Triggers L5

The outdoor unit inverter board monitors compressor current and feedback. L5 is triggered when:
- The compressor draws locked-rotor current (much higher than running current)
- The compressor fails to reach target speed within the startup window
- The inverter detects abnormal motor feedback signals

## Common Causes {#most-likely-cause}

| [Cause](https://www.amazon.com/s?k=Cause&tag=errorcodefixe-20) | Likelihood |
|---|---|
| [Failed compressor (seized or winding fault)](https://www.amazon.com/s?k=Failed%20compressor%20(seized%20or%20winding%20fault)&tag=errorcodefixe-20) | High |
| [Liquid refrigerant flooding compressor on startup](https://www.amazon.com/s?k=Liquid%20refrigerant%20flooding%20compressor%20on%20startup&tag=errorcodefixe-20) | High |
| [Inverter IPM (power module) fault](https://www.amazon.com/s?k=Inverter%20IPM%20(power%20module)%20fault&tag=errorcodefixe-20) | Medium |
| [Low supply voltage causing startup failure](https://www.amazon.com/s?k=Low%20supply%20voltage%20causing%20startup%20failure&tag=errorcodefixe-20) | Medium |
| [Refrigerant overcharge causing liquid slugging](https://www.amazon.com/s?k=Refrigerant%20overcharge%20causing%20liquid%20slugging&tag=errorcodefixe-20) | Medium |
| [Failed crankcase heater (causing liquid in compressor)](https://www.amazon.com/s?k=Failed%20crankcase%20heater%20(causing%20liquid%20in%20compressor)&tag=errorcodefixe-20) | Medium |
| [Outdoor PCB fault](https://www.amazon.com/s?k=Outdoor%20PCB%20fault&tag=errorcodefixe-20) | Low |

## Step-by-Step Diagnosis {#diagnosis}

**Step 1 — Check supply voltage**
- Measure L1-L2-L3 (three-phase) or L-N (single-phase) at the outdoor unit disconnect
- Voltage must be within ±10% of nameplate rating
- Low voltage on startup causes the inverter to trip L5

**Step 2 — Check crankcase heater**
- Daikin compressors in cold climates use a crankcase heater to prevent refrigerant migration
- With unit off, the crankcase heater should be energized and the compressor body should be warm to the touch
- If the heater is cold: check heater resistance (typically 60–100 ohms), check board relay
- A cold compressor with refrigerant in the oil will slug on startup and trip L5

**Step 3 — Check refrigerant pressures**
- Before startup, check static refrigerant pressure
- Excessive liquid in the compressor shows as low static pressure on the high side
- If system was off for an extended period in cold weather, wait for crankcase heater to operate (30–60 minutes) before attempting restart

**Step 4 — Check compressor winding resistance**
- Disconnect power and discharge inverter capacitors (wait 5 minutes after power off)
- Disconnect the compressor wiring at the inverter output terminals
- Measure resistance U-V, V-W, W-U (three-phase scroll): should be equal, typically 1–5 ohms
- Open winding (infinite ohms) = failed compressor
- Check insulation resistance: phase-to-ground should be >1 MΩ with a 500V megger

**Step 5 — Check the IPM (inverter power module)**
- The IPM converts DC bus voltage to variable frequency AC for the compressor
- Check for burnt or swollen components on the inverter board
- Check DC bus voltage (should be 280–400V DC for 208/240V supply)
- If compressor windings check out but L5 persists, replace the inverter PCB

## Replacement Parts {#parts}

| Part | Notes |
|---|---|
| [Crankcase heater](https://www.amazon.com/s?k=Crankcase%20heater&tag=errorcodefixe-20) | Match wattage — Daikin part varies by compressor |
| [Inverter PCB](https://www.amazon.com/s?k=Inverter%20PCB&tag=errorcodefixe-20) | High-value part — verify compressor first |
| [Compressor](https://www.amazon.com/s?k=Compressor&tag=errorcodefixe-20) | Requires refrigerant recovery — EPA 608 certified tech |

## Reset Procedure

L5 is a hard fault on most Daikin models:
1. Fix the root cause
2. Cycle power at the disconnect — wait 5 minutes for capacitors to discharge
3. Restore power — compressor should attempt startup
4. If L5 returns immediately, the compressor is failed

> **Warning:** Never attempt to restart a locked compressor repeatedly. Each restart attempt on a seized compressor pushes heat into the motor windings and worsens the failure. Diagnose first, then restart once.
