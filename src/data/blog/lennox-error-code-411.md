---
title: "Lennox Error Code 411 — Ignition Proving Fault Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-04-03T08:00:00Z
modDatetime: 2024-04-03T08:00:00Z
slug: lennox-error-code-411
featured: false
draft: false
tags:
  - hvac
  - lennox
  - furnace
  - ignition
description: "Lennox error code 411 means the furnace failed to prove ignition after the trial period. This guide covers diagnosis and fixes for the Lennox 411 ignition proving fault."
---

## Error Code: Lennox 411

**What it means:** Lennox error code 411 indicates an ignition proving fault — the control board energized the hot surface igniter and opened the gas valve, but the flame sensor failed to detect a confirmed flame within the ignition trial period (typically 4–7 seconds after valve opening). On iComfort-enabled furnaces, this code appears on the thermostat display. On non-connected furnaces, it appears as a 4-1-1 flash pattern on the control board LED. The furnace will retry ignition up to three times before locking out with a Code 413 or extended lockout.

## Common Causes

- **Dirty or oxidized flame sensor** — The most common cause across all brands. The sensor rod accumulates silicon oxide deposits that insulate it from the flame, blocking the microamp signal the board needs to confirm ignition. Cleaning resolves this in most cases.
- **Weak hot surface igniter** — Lennox SLP and XP furnaces use Minisit or Norton silicon nitride igniters. A partially cracked igniter may glow but fail to reach the 1800°F threshold needed to ignite gas reliably.
- **Low gas pressure at manifold** — Manifold pressure below 3.2" W.C. on natural gas or below 10" W.C. on propane produces a weak pilot flame the sensor cannot reliably detect.
- **Gas valve solenoid fault** — The gas valve receives 24V AC from the board but fails to open due to a failed solenoid coil or sticking valve body.
- **Flame sensor wire fault** — A chafed or shorted flame sensor lead can produce a false or absent signal at the board.

## Diagnosis Steps

1. Initiate a heat call and observe the ignition sequence. Listen for: inducer starts → igniter glows (30–45 seconds warmup) → gas valve clicks → flame lights. If flame lights and immediately extinguishes, the flame sensor is not detecting the flame.
2. Remove the flame sensor (typically one screw, accessible through the burner compartment). Inspect the rod — oxidized sensors appear white or gray on the metal rod. Clean with fine emery cloth or steel wool. Reinstall.
3. Measure igniter resistance: disconnect the igniter leads and measure across them. Silicon nitride igniters should read 40–90 ohms at room temperature. OL = cracked and failed — replace.
4. If igniter glows brightly and flame lights but Code 411 still appears, check the flame sensor wiring harness for damage between the sensor and the board connector.
5. Confirm gas supply pressure with a manometer at the manifold pressure tap. Adjust the gas valve regulator if pressure is outside spec.

## Fix

Flame sensor cleaning is the first action — it resolves Code 411 in the majority of cases. If cleaning doesn't hold for more than one season, replace the sensor. Lennox flame sensors cost $15–25 and are available by furnace model number.

If the igniter is the cause (dim glow, high resistance), replace it. Handle igniters only by the ceramic base — fingerprint oils cause premature failure. Lennox uses both 80V and 120V igniter circuits — confirm voltage before ordering.

Gas pressure adjustment and gas valve replacement require a licensed technician and a calibrated manometer.

## Parts

| Part | Where to Buy |
|------|-------------|
| [Flame sensor](https://www.amazon.com/s?k=Flame+sensor&tag=errorcodefixes-20) | RepairClinic, Amazon |
| [Hot surface igniter (silicon nitride)](https://www.amazon.com/s?k=Hot+surface+igniter+%28silicon+nitride%29&tag=errorcodefixes-20) | RepairClinic, SupplyHouse |
| [Gas valve](https://www.amazon.com/s?k=Gas+valve&tag=errorcodefixes-20) | SupplyHouse, Grainger |

## When to Call a Technician

Flame sensor cleaning and igniter replacement are appropriate for a confident DIYer. Gas pressure adjustment and gas valve replacement require a licensed HVAC technician and should not be attempted without proper test equipment.

## Related Articles

- [Lennox Error Code 292 — Ignition Failure Fix](/posts/lennox-292-error-code/)
- [Lennox EL296V Error Codes — Variable-Speed Furnace Diagnostic Guide](/posts/lennox-el296v-error-codes/)
- [Lennox Elite Series Furnace Error Codes — Fault Code Diagnostic Guide](/posts/lennox-elite-series-furnace-codes/)
- [Lennox 103 Error Code — Causes & Fix](/posts/lennox-error-code-103/)
- [Lennox Error Code 111 — Causes & Fix](/posts/lennox-error-code-111/)
