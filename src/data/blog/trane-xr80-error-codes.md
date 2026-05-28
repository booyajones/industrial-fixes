---
title: "Trane XR80 Blinking Yellow Light Codes: Full Flash-Code Fix Guide"
description: "Trane XR80 yellow LED blink patterns decoded - what each 1 through 9 flash sequence means, common causes, and the fix steps. Quick-reference table for HVAC technicians and homeowners."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - trane
---

## Trane XR80 Error Codes — What They Mean

The Trane XR80 is a single-stage 80% AFUE gas furnace that communicates faults through a status LED located behind the lower access door. The LED blinks a sequence of long and short flashes to indicate the fault code. Count the flashes, pause, then count again to confirm the code. A steady ON light means the furnace is operating normally. A steady OFF light with no power to the board is a separate power supply issue.

[Jump to Fix](#fix)

## Trane XR80 Flash Code Reference

| Flash Code | Meaning | Priority |
|------------|---------|----------|
| Steady ON | Normal operation | — |
| 1 Flash | System lockout (exceeded retry/recycle count) | High |
| 2 Flashes | Pressure switch stuck open | Medium |
| 3 Flashes | Pressure switch stuck closed | Medium |
| 4 Flashes | Open high-limit device | High |
| 5 Flashes | Flame sensed without call for heat | High |
| 6 Flashes | 115V AC power reversed (polarity fault) | Medium |
| 7 Flashes | Gas valve circuit fault or low flame signal | High |
| 8 Flashes | Low flame signal / ignition problem | High |
| 9 Flashes | Blower on-delay timeout (blower not starting) | High |

## Step-by-Step Fix {#fix}

**Code 1 — System Lockout:**
Reset the furnace by cutting power at the disconnect for 30 seconds. If it relocks immediately, the underlying fault (pressure switch, flame sensor, or gas) needs to be resolved first.

**Code 2 — Pressure Switch Stuck Open:**
Check flue/intake pipes for blockage. Inspect pressure switch hose for cracks or condensate. Test pressure switch continuity with the inducer running — it should close.

**Code 3 — Pressure Switch Stuck Closed:**
Switch contacts are welded closed or there's a wiring short. Replace the pressure switch.

**Code 4 — High Limit Open:**
Check air filter (replace if dirty), confirm all registers are open, test blower operation (run capacitor). If limit trips with adequate airflow, suspect a cracked heat exchanger.

**Code 5 — Flame Without Call:**
Gas valve is leaking or the flame sensor wire has a short to ground. Turn off the gas and call a technician.

**Code 6 — Polarity Fault:**
Check the 115V AC wiring to the furnace. The hot and neutral wires may be reversed at the disconnect or outlet. Correct polarity and reset.

**Code 7 — Gas Valve or Low Flame:**
Check gas supply pressure, clean the flame sensor, inspect the gas valve wiring. Replace gas valve if supply pressure is confirmed normal.

**Code 8 — Low Flame / Ignition:**
Clean the flame sensor rod with steel wool. Check ignitor resistance (40–100 Ω cold for silicon carbide). Verify manifold gas pressure.

**Code 9 — Blower Timeout:**
Test the run capacitor (match µF rating). Check for debris binding the blower wheel. Verify 120V at the motor.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame sensor rod | [Amazon](https://www.amazon.com/dp/B0CZ7M9V4D?ascsubtag=ecf-trane-xr80-error-codes&tag=errorcodefixes-20) \| Most codes 7 and 8 start with the sensor |
| Blower run capacitor | [Amazon](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-trane-xr80-error-codes&tag=errorcodefixes-20) \| Code 9; match µF and voltage on the capacitor label |
| Hot surface ignitor | [Amazon](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-trane-xr80-error-codes&tag=errorcodefixes-20) \| Code 8; silicon carbide, 120V |
| Draft pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-trane-xr80-error-codes&tag=errorcodefixes-20) \| Codes 2 and 3 |
| High-limit switch | [Amazon](https://www.amazon.com/dp/B0BN3TRG9R?ascsubtag=ecf-trane-xr80-error-codes&tag=errorcodefixes-20) \| Code 4; match temperature rating |
## When to Call a Pro

Code 5 (flame without call) is a gas leak/valve failure — shut off the gas and do not attempt DIY repair. Code 4 that recurs after replacing the filter and confirming airflow may indicate a cracked heat exchanger, which requires professional inspection and is a carbon monoxide hazard.

## Related Articles

- [Trane 1 Flash Error Code — Causes & Fix](/posts/trane-1-flash-error-code/)
- [Trane Error Code 126 — Ignition Lockout Fix](/posts/trane-126-error-code/)
- [Trane 2 Flashes Error Code — Causes & Fix](/posts/trane-2-flashes-error-code/)
- [Trane 3 Flashes Error Code — Pressure Switch Fault Fix](/posts/trane-3-flashes-error-code/)
- [Trane 3 Flash Pressure Switch Fault — Detailed Diagnosis Guide](/posts/trane-3-flashes-pressure-switch/)

## See Also

- [Trane XV20i/XV18 Fault 126 — Low Pressure Cutout Fix](/posts/trane-heat-pump-error-code-126/)
- [Trane Precedent Rooftop Unit Error Codes: Complete Guide](/posts/trane-precedent-error-codes/)
- [Trane 4 Flashes Error Code — Open High Limit Fix](/posts/trane-4-flashes-error-code/)
- [Trane ComfortLink II Error Codes — Common Faults and Fixes](/posts/trane-comfortlink-ii-error-codes/)
