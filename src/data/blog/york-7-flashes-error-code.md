---
title: "York 7 Flashes Error Code — Ignition Lockout Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-04-01T08:00:00Z
modDatetime: 2024-04-01T08:00:00Z
slug: york-7-flashes-error-code
featured: false
draft: false
tags:
  - hvac
  - york
  - furnace
  - ignition
description: "York 7 flashes means ignition lockout after 3 failed attempts. This guide covers diagnosis and fixes for the York furnace 7-flash ignition lockout fault."
---

## Error Code: York 7 Flashes

**What it means:** Seven flashes on a York furnace (including Coleman and Luxaire) indicates an ignition lockout. The control board made three ignition attempts — energizing the hot surface igniter, opening the gas valve, and waiting for a flame signal from the flame sensor — and failed to establish a confirmed flame each time. After the third failed attempt, the board locks out. The lockout timer on most York boards is 60 minutes, after which the board will allow one more attempt. Cycling power resets the lockout immediately.

## Common Causes

- **Dirty flame sensor** — Oxide buildup on the sensor rod prevents it from passing microamps through the flame. The board sees no flame signal, cuts the gas valve, and logs a failed attempt. Cleaning takes 5 minutes.
- **Cracked or failed igniter** — A hot surface igniter that glows dimly (cracked element) may not reach ignition temperature to light gas consistently.
- **Low gas pressure** — Manifold pressure below spec produces a flame the sensor struggles to detect, especially during cold outdoor conditions when gas density increases.
- **Faulty gas valve** — The board sends a 24V signal to the gas valve; if the valve solenoid is open internally, no gas flows.
- **Failed control board relay** — The gas valve relay on the board can fail, preventing valve energization.

## Diagnosis Steps

1. Reset lockout by cycling power. Count the diagnostic flashes to confirm it is 7 (lockout) and not a different fault.
2. Observe the ignition trial: inducer runs → igniter glows → gas valve opens (audible click) → flame lights. If flame lights and immediately extinguishes, suspect flame sensor.
3. Remove the flame sensor. Clean the rod with emery cloth or fine steel wool — 30 seconds of cleaning. Reinstall and test.
4. If igniter glows dimly or no glow: measure resistance across igniter terminals at room temp. Normal silicon nitride igniters: 40–90 ohms. Open circuit = cracked igniter, replace.
5. If igniter glows correctly and gas lights but sensor fails to hold: measure microamp signal from flame sensor at the board (typically 0.5–10 µA during flame). Below 0.5 µA = replace sensor.

## Fix

Flame sensor cleaning and igniter replacement cover the vast majority of York 7-flash faults. The flame sensor costs $15–25. The igniter for York/Coleman furnaces is typically a surface-style silicon nitride element — order by model number to confirm the correct wattage and mounting configuration.

If gas flow is absent despite a correct igniter glow, check for closed manual shutoff on the gas line. If the shutoff is open and other gas appliances work, the gas valve has failed. Replace the gas valve — this requires a licensed tech in most jurisdictions.

## Parts

| Part | Where to Buy |
|------|-------------|
| [Flame sensor](https://www.amazon.com/dp/B0CZ7M9V4D?ascsubtag=ecf-york-7-flashes-error-code&tag=errorcodefixes-20) | RepairClinic, Amazon |
| [Hot surface igniter](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-york-7-flashes-error-code&tag=errorcodefixes-20) | RepairClinic, SupplyHouse |
| [Gas valve](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-york-7-flashes-error-code&tag=errorcodefixes-20) | SupplyHouse, Grainger |

## When to Call a Technician

Flame sensor and igniter replacement are appropriate DIY repairs. Gas valve replacement requires a licensed HVAC technician. If the board is suspected, a tech with a diagnostic meter can confirm before committing to a board replacement.

## Related Articles

- [York 2 Flashes Error Code — Causes & Fix](/posts/york-2-flashes-error-code/)
- [York 3 Flashes Error Code — Causes & Fix](/posts/york-3-flashes-error-code/)
- [York 4 Flashes Error Code — Open Limit Device Fix](/posts/york-4-flashes-error-code/)
- [York 5 Flashes Error Code — Causes & Fix](/posts/york-5-flashes-error-code/)
- [York Furnace 6 Flashes Error Code — Pressure Switch Fault Fix](/posts/york-6-flashes-pressure-switch-fault/)
