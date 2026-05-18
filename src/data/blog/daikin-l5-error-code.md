---
title: "Daikin L5 Error Code — Compressor Lock Fault"
description: "Daikin error code L5 means the compressor is locked or has failed to start. Learn the exact causes, diagnostic steps, and how to fix Daikin L5."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "Marcus Webb"
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

| Cause | Likelihood |
|---|---|
| Failed compressor (seized or winding fault) | High |
| Liquid refrigerant flooding compressor on startup | High |
| Inverter IPM (power module) fault | Medium |
| Low supply voltage causing startup failure | Medium |
| Refrigerant overcharge causing liquid slugging | Medium |
| Failed crankcase heater (causing liquid in compressor) | Medium |
| Outdoor PCB fault | Low |

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
| Crankcase heater | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-l5-error-code&k=Crankcase+heater&tag=errorcodefixes-20) \| Match wattage — Daikin part varies by compressor |
| Inverter PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-l5-error-code&k=Inverter+PCB&tag=errorcodefixes-20) \| High-value part — verify compressor first |
| Compressor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-l5-error-code&k=Compressor&tag=errorcodefixes-20) \| Requires refrigerant recovery — EPA 608 certified tech |
## Reset Procedure

L5 is a hard fault on most Daikin models:
1. Fix the root cause
2. Cycle power at the disconnect — wait 5 minutes for capacitors to discharge
3. Restore power — compressor should attempt startup
4. If L5 returns immediately, the compressor is failed

> **Warning:** Never attempt to restart a locked compressor repeatedly. Each restart attempt on a seized compressor pushes heat into the motor windings and worsens the failure. Diagnose first, then restart once.

## Related Articles

- [Daikin A3 Error Code — Causes & Fix](/posts/daikin-a3-error-code/)
- [Daikin Applied Chiller Fault Codes Guide — WMC / AGZ / ALZ Series](/posts/daikin-applied-fault-codes/)
- [Daikin C4 Error Code — Heat Exchanger Coil Sensor: Causes & Fix](/posts/daikin-c4-error-code/)
- [Daikin C9 Error Code — Compressor Discharge Temperature Sensor Fault](/posts/daikin-c9-error-code/)
- [Daikin E1 Error Code Fix — Indoor Sensor Fault](/posts/daikin-e1-error-code/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [Rheem EcoNet A101 error code fix](/posts/rheem-econet-a101-error-code/)

