---
title: "Trane S8X1 Furnace Error Codes — Flash Code Diagnostic Guide"
description: "Complete guide to Trane S8X1 furnace error codes, flash sequences, what each fault means, and step-by-step repairs for the most common failures."
pubDatetime: 2026-04-22T22:00:00Z
modDatetime: 2026-04-22T22:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - trane
  - furnace
money_part: "Pressure switch hose"
---

## Trane S8X1 Furnace Error Codes — What They Mean

The Trane S8X1 is an 80% AFUE, single-stage, multi-position gas furnace in the S-Series lineup. It is a popular replacement/builder-grade unit with a straightforward single-speed PSC blower. Faults are communicated via a diagnostic LED on the control board — visible through the sight glass on the lower access door. Count the number of flashes between pauses to identify the fault.

## Trane S8X1 Flash Code Reference

| Flash Code | Meaning |
|------------|---------|
| Continuous on | Normal — no call for heat |
| Continuous off | No power to board |
| 2 flashes | System lockout — retry limit |
| 3 flashes | Pressure switch fault |
| 4 flashes | High-limit switch open |
| 5 flashes | Flame sensed without call |
| 6 flashes | 115V reversed polarity |
| 7 flashes | Gas valve error |
| 8 flashes | Weak flame signal |
| 9 flashes | Rollout switch open |
| 13 flashes | Limit cycle lockout |
| 14 flashes | Ignition lockout (3 failed attempts) |

## Common Causes by Code

- **Code 3 — Pressure switch** — On the S8X1, the most common cause is the single rubber pressure hose between the inducer housing and the pressure switch. This hose develops cracks with age. Also check the metal flue vent pipe at the exterior termination for blockage.
- **Code 4 — High limit** — The S8X1 has a single high-limit switch on the supply plenum. Dirty filter and restricted return air are the top causes. The limit opens at 200°F and resets below 130°F. If it trips repeatedly, check static pressure and blower operation.
- **Code 7 — Gas valve error** — Usually indicates the gas valve is not receiving 24V from the control board, or the board's gas valve relay has failed. Measure 24V between the W terminal and common at the gas valve during the heating call.
- **Code 8 — Weak flame** — Dirty flame sensor. The S8X1's flame sensor rod is located in the burner compartment on the right side. Clean with emery cloth. If µA signal is still below 1.0 after cleaning, replace the sensor.
- **Code 9 — Rollout** — Rollout switches are located on the burner bracket. Open rollout is a red-flag event — it means flames are exiting the heat exchanger in an abnormal direction. Cracked heat exchanger or improper gas pressure are the primary causes. Do not reset without inspection.
- **Code 14 — Ignition lockout** — Failed ignitor, weak gas pressure, or sticking gas valve. The S8X1 uses a silicon nitride hot surface ignitor at 120V.

## Step-by-Step Fix {#fix}

1. **Read the code from the LED** — Observe the flash pattern through the lower door sight glass. Two-digit codes (like 13, 14) appear as a long group of flashes.
2. **Pressure switch diagnosis (Code 3)** — Disconnect the rubber hose at the pressure switch and connect a manometer. With the inducer running, confirm the negative pressure at the switch is within the switch's rating (typically -0.65" to -0.85" W.C.). If pressure is adequate but switch won't close, replace the switch.
3. **High-limit diagnosis (Code 4)** — Pull the filter and inspect. If clean, check for blocked supply registers. Use a thermometer in the supply plenum to confirm temperatures are not exceeding 200°F at normal blower speeds.
4. **Rollout diagnosis (Code 9)** — With power off, use a flashlight and mirror to inspect the burner box and heat exchanger tubes for cracks, rust, or scale accumulation. Probe each burner orifice for blockage.
5. **Gas valve diagnosis (Code 7)** — Measure 24VAC at the gas valve terminals during heating call. If 24V is present and valve doesn't open, replace the valve. If no 24V, trace to the control board relay.
6. **Clear lockout** — Cycle the power switch on the furnace or the breaker in the electrical panel. For Code 13, power must remain on for 1 hour to automatically clear.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Pressure switch hose | [View on Amazon](https://www.amazon.com/dp/B0CPTHML1N?ascsubtag=ecf-trane-s8x1-error-codes&tag=errorcodefixes-20) \| Inexpensive; check for cracks first |
| Flame sensor | [Amazon](https://www.amazon.com/s?k=Flame+sensor&tag=errorcodefixes-20) \| ~$15; clean before replacing |
| Hot surface ignitor | [View on Amazon](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-trane-s8x1-error-codes&tag=errorcodefixes-20) \| 120V silicon nitride; confirm model compatibility |
| High-limit switch | [View on Amazon](https://www.amazon.com/dp/B0BN3TRG9R?ascsubtag=ecf-trane-s8x1-error-codes&tag=errorcodefixes-20) \| Check continuity before ordering |
| Gas valve | [View on Amazon](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-trane-s8x1-error-codes&tag=errorcodefixes-20) \| 24V Honeywell or White-Rodgers; confirm voltage |
| Control board | [Amazon](https://www.amazon.com/s?k=Control+board&tag=errorcodefixes-20) \| For Code 6 or persistent unexplained faults |
## When to Call a Pro

Gas valve replacement, heat exchanger inspection, and refrigerant-side work require licensed technicians. If the S8X1 is showing repeated rollout trips or you smell gas near the furnace, shut the unit off and call a pro immediately — do not attempt to reset and restart.
