---
title: "Goodman GSZC18 Heat Pump Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to Goodman GSZC18 two-stage heat pump error codes, flash sequences, common fault causes, and step-by-step fixes."
pubDatetime: 2026-04-22T22:00:00Z
modDatetime: 2026-04-22T22:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - goodman
  - heat-pump
---

## Goodman GSZC18 Heat Pump Error Codes — What They Mean

The Goodman GSZC18 is an 18 SEER, two-stage heat pump designed for use with Goodman's ComfortNet communicating system or a conventional thermostat. The outdoor control board flashes fault codes through the diagnostic LED. When paired with a ComfortNet thermostat, fault descriptions appear directly on the thermostat screen with more detail.

[Jump to Fix](#fix)

## Goodman GSZC18 Flash Code Reference

| [Flash Code](https://www.amazon.com/s?k=Flash%20Code&tag=errorcodefixe-20) | Meaning |
|------------|---------|
| [1 flash](https://www.amazon.com/s?k=1%20flash&tag=errorcodefixe-20) | High-pressure switch lockout |
| [2 flashes](https://www.amazon.com/s?k=2%20flashes&tag=errorcodefixe-20) | Low-pressure switch lockout |
| [3 flashes](https://www.amazon.com/s?k=3%20flashes&tag=errorcodefixe-20) | Outdoor ambient temperature lockout |
| [4 flashes](https://www.amazon.com/s?k=4%20flashes&tag=errorcodefixe-20) | Compressor protection (internal overload) |
| [5 flashes](https://www.amazon.com/s?k=5%20flashes&tag=errorcodefixe-20) | Defrost control fault |
| [6 flashes](https://www.amazon.com/s?k=6%20flashes&tag=errorcodefixe-20) | Outdoor fan motor fault |
| [7 flashes](https://www.amazon.com/s?k=7%20flashes&tag=errorcodefixe-20) | Low-stage high-pressure switch fault |
| [8 flashes](https://www.amazon.com/s?k=8%20flashes&tag=errorcodefixe-20) | Control board fault |
| [9 flashes](https://www.amazon.com/s?k=9%20flashes&tag=errorcodefixe-20) | Discharge temperature sensor fault |

## Common Causes by Code

- **Code 1 — High pressure lockout** — On the GSZC18, the two-stage compressor runs at low capacity first. High-pressure trips at low stage are often caused by a dirty condenser coil or an airflow problem more severe than a standard single-stage unit. Confirm the coil is clean on all four sides (the GSZC18 uses a full-wraparound coil design).
- **Code 2 — Low pressure lockout** — Low refrigerant charge is the primary cause. The GSZC18 uses R-410A and has a specific charge requirement per the installation data plate. Also check the low-pressure switch contacts.
- **Code 3 — Ambient lockout** — The GSZC18 has a low-ambient cooling lockout (below 55°F by default) and a low-ambient heating lockout (at the compressor's rated minimum). Code 3 in winter is normal operation; in summer, check the ambient sensor.
- **Code 4 — Compressor protection** — Two-stage compressors are more expensive to replace. If Code 4 appears frequently, check supply voltage (both legs), run capacitor values, and refrigerant charge before condemning the compressor.
- **Code 5 — Defrost fault** — The GSZC18 uses a time-temperature defrost board. A failed defrost termination sensor (clip-on type on the outdoor coil) is the most common cause. Also check the defrost relay on the control board.
- **Code 6 — Fan motor fault** — The GSZC18 may have an ECM or PSC outdoor fan motor depending on the model year. Check the motor capacitor, power supply, and motor winding continuity.

## Step-by-Step Fix {#fix}

1. **Read the flash code** — Access the control compartment on the side of the GSZC18 cabinet. The LED is on the control board.
2. **For Code 1** — Clean the condenser coil. Confirm fan rotation (air exits top). Check both high-pressure switch contacts with power off.
3. **For Code 2** — Connect gauges. R-410A suction pressure at 75°F ambient, cooling mode, should be approximately 110–115 PSI. Below 90 PSI indicates low charge. Perform electronic leak detection before adding refrigerant.
4. **For Code 4** — Let the unit cool for 30 minutes. Measure supply voltage at the disconnect under load — both legs to ground and leg-to-leg. Check the dual run capacitor with a capacitor meter (compare to nameplate µF rating ±6%).
5. **For Code 5** — Locate the defrost sensor on the outdoor coil (typically clipped to a U-bend near the bottom of the coil). Confirm it is making firm contact with the coil. Measure resistance and compare to the temperature-resistance chart in the service data.
6. **For Code 6** — With power off, spin the fan blade — should rotate freely. Measure capacitor µF. Check motor windings for continuity (common to each winding).
7. **Reset and monitor** — After repair, cycle power and run the unit in both heating and cooling to confirm no fault recurrence.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Dual run capacitor](https://www.amazon.com/s?k=Dual%20run%20capacitor&tag=errorcodefixe-20) | High failure rate in hot climates; check µF |
| [Defrost sensor](https://www.amazon.com/s?k=Defrost%20sensor&tag=errorcodefixe-20) | Clip-on; confirm coil contact |
| [Defrost board](https://www.amazon.com/s?k=Defrost%20board&tag=errorcodefixe-20) | If sensor is good but defrost won't initiate |
| [Contactor](https://www.amazon.com/s?k=Contactor&tag=errorcodefixe-20) | Pitted contacts cause compressor protection codes |
| [Refrigerant (R-410A)](https://www.amazon.com/s?k=Refrigerant%20(R-410A)&tag=errorcodefixe-20) | Fix leak first; EPA certification required |
| [Outdoor fan motor](https://www.amazon.com/s?k=Outdoor%20fan%20motor&tag=errorcodefixe-20) | PSC or ECM depending on model year |

## When to Call a Pro

Two-stage compressor diagnosis and refrigerant work require professional tools and certification. The GSZC18's two-stage valve and ComfortNet communication system add complexity that makes board-level diagnosis difficult without Goodman's diagnostic software.
