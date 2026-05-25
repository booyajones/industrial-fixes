---
title: "Goodman Furnace E2 Error Code — Flame Sense Fault (Digital Display Models)"
description: "Goodman E2 error on digital display furnaces means a flame sense fault. Learn how to clean the flame sensor, test it, and fix ignition timing issues."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - goodman
  - furnace
  - hvac
  - error-code
  - flame-sensor
---

## Goodman Furnace E2 Error — Flame Sense Fault

The **E2 error code** on Goodman furnaces with digital displays (common on newer GMSS96, GCSS96, and AVPTC series units) means the **flame sensor is not detecting a flame** during the trial for ignition period. The control board lights the igniter and opens the gas valve, but the flame signal never registers — so it shuts down and stores E2.

*Note: Older Goodman furnaces with LED blink codes use flash sequences instead of E-codes. The E2 code appears on models with a digital segment display on the IFC board.*

## Why E2 Happens

| Cause | Frequency |
|---|---|
| Dirty/oxidized flame sensor rod | Very common |
| Weak igniter (not hot enough to light gas) | Common |
| Low gas pressure | Common |
| Gas valve not opening (failed coil or wiring) | Moderate |
| Flame sensor wire broken or grounded | Moderate |
| IFC board microamp circuit failed | Rare |

## How the Flame Sensor Works

The flame sensor is a metal rod that extends into the burner flame. When flame is present, it passes a small AC voltage (from the IFC) through the flame to ground — creating a DC microamp signal the board reads as "flame proven." The board expects 1–5 microamps minimum. A coated or oxidized rod can't pass this current even when the flame is burning.

## Fix Step 1 — Clean the Flame Sensor

**This fixes E2 in about 60% of cases.**

1. Turn off power to the furnace at the disconnect.
2. Locate the flame sensor — a single metal rod (usually with a white ceramic insulator) mounted in the burner area, with one yellow or orange wire attached.
3. Remove the mounting screw and slide the rod out.
4. Use fine steel wool or 400-grit emery cloth to lightly polish the metal rod. Remove any white/grey oxide coating until you see bare shiny metal.
5. Do NOT touch the cleaned rod with bare fingers (oils will re-coat it).
6. Reinstall and test.

## Fix Step 2 — Test Microamp Reading

If cleaning doesn't fix it, measure the flame sensor signal directly:

1. Set your multimeter to DC microamps (µA).
2. Break the wire going to the flame sensor and connect the meter in series.
3. Start the furnace. When the flame lights, read the meter.
4. **Normal reading: 2–6 µA DC** on most Goodman boards.
5. Under 1 µA = replace the sensor. Consistently 0 with flame burning = suspect IFC board.

## Fix Step 3 — Check Gas Pressure

Low gas pressure means a weak flame that can be hard to sense. A tech with a manometer should verify incoming pressure (7" WC for natural gas) and manifold pressure (3.5" WC standard, 10" WC for LP).

## Fix Step 4 — Check Igniter

The silicon carbide or silicon nitride igniter must reach 1800°F+ to reliably ignite gas. A cracked or weak igniter may produce enough glow to start, then gas doesn't light cleanly, then E2 trips. Visually inspect the igniter — cracks or dark spots mean replace it.

## Parts You May Need

| Part | Cost |
|---|---|
| Flame sensor (universal) | [Amazon](https://www.amazon.com/dp/B0CZ7M9V4D?ascsubtag=ecf-goodman-furnace-e2-error-code&tag=errorcodefixes-20) \| $10–20 |
| OEM Goodman flame sensor | [Amazon](https://www.amazon.com/dp/B0CZ7M9V4D?ascsubtag=ecf-goodman-furnace-e2-error-code&tag=errorcodefixes-20) \| $25–45 |
| Hot surface igniter | [Amazon](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-goodman-furnace-e2-error-code&tag=errorcodefixes-20) \| $20–50 |
| Gas valve | [Amazon](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-goodman-furnace-e2-error-code&tag=errorcodefixes-20) \| $80–200 |
| IFC board | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-goodman-furnace-e2-error-code&tag=errorcodefixes-20) \| $100–300 |
## E2 vs. E1 vs. EE2

- **E1** = Pressure switch fault (no draft sensing)
- **E2** = Flame sense fault (no flame signal)
- **EE2** = Rollout switch open (safety lockout)

Don't confuse E2 (flame sense) with the older flash-code equivalent — 6 flashes = open limit, 7 flashes = flame sense issue on LED models.

## Related Articles

- [Goodman 1 Flash Error Code — What It Means](/posts/goodman-1-flash-error-code/)
- [Goodman 2 Flash Error Code — Causes & Fix](/posts/goodman-2-flash-error-code/)
- [Goodman 3 Flash Error Code — Pressure Switch Stuck Open Fix](/posts/goodman-3-flash-error-code/)
- [Goodman 4 Flash Error Code — Causes & Fix](/posts/goodman-4-flash-error-code/)
- [Goodman 5 Flash Error Code — Causes & Fix](/posts/goodman-5-flash-error-code/)

## See Also

- [Goodman 4 Flash Error Code — Causes & Fix](/posts/goodman-4-flash-error-code/)
- [Goodman Furnace 2 Flashes — Pressure Switch Stuck Closed Fix](/posts/goodman-furnace-2-flashes/)
- [Goodman 5 Flash Error Code — Causes & Fix](/posts/goodman-5-flash-error-code/)
- [Goodman Furnace Error Codes — All Flash Codes Explained](/posts/goodman-furnace-error-codes/)
