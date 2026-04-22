---
title: "Carrier Heat Pump E6 Error Code — Outdoor Temp Sensor Fault"
description: "What Carrier E6 means on a heat pump, why the outdoor temperature sensor fails, and how to diagnose and fix it."
pubDatetime: 2026-04-22T16:00:00Z
modDatetime: 2026-04-22T16:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - carrier
---

## Carrier Heat Pump E6 Error Code — What It Means

Carrier heat pump error code **E6** indicates an **outdoor ambient temperature sensor fault**. The outdoor unit's ambient air thermistor is reporting a value outside the expected range — either stuck at a fixed resistance (failed sensor), open circuit (disconnected wire), or short circuit (damaged thermistor). E6 appears on Carrier mini-split and ductless heat pump systems.

[Jump to Fix](#fix)

## Common Causes

- **Failed outdoor ambient thermistor** — NTC thermistors degrade over time, particularly when exposed to moisture, corrosion, or physical damage. A failed thermistor reads outside the normal range and triggers E6.
- **Loose or corroded connector** — The thermistor connects to the outdoor PCB via a 2-pin connector. Vibration and condensation corrode these connectors. A high-resistance connection mimics a failed thermistor.
- **Damaged sensor wiring** — On units where the sensor wire routes near moving parts (fan blade, compressor vibration), chafing can cause intermittent open-circuit conditions.
- **Outdoor PCB fault** — Rarely, the thermistor input circuit on the outdoor control board fails. Diagnose only after replacing the thermistor.

## Step-by-Step Fix {#fix}

1. **Power off the outdoor unit** at the disconnect.
2. **Locate the outdoor ambient thermistor** — on most Carrier mini-splits (40MAQB, 38HDR, etc.), the ambient thermistor is a small probe mounted in the outdoor unit chassis near the air intake, not on the coil. It's connected to the outdoor PCB via a short 2-pin harness.
3. **Inspect the connector** — unplug and re-seat the thermistor connector on the outdoor PCB. Look for green corrosion or bent pins. If corroded, clean with electronics contact cleaner.
4. **Measure thermistor resistance** — at the thermistor connector (with it unplugged from the PCB), measure resistance with a multimeter. At room temperature (70–77°F / 21–25°C), most Carrier outdoor ambient thermistors read approximately 10 kΩ. An OL reading means open circuit (failed thermistor). A near-zero reading means short circuit.
5. **Replace the thermistor** — if resistance is out of spec, order a replacement using the outdoor unit's model number. Thermistors are typically less than $15 and are plug-and-play replacements.
6. **Restore power and test** — verify E6 clears after replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Outdoor ambient thermistor](https://www.amazon.com/s?k=Outdoor%20ambient%20thermistor&tag=errorcodefixe-20) | Carrier 338818-701 or model-specific; verify pin count |
| [Contact cleaner](https://www.amazon.com/s?k=Contact%20cleaner&tag=errorcodefixe-20) | DeoxIT D5 for connector cleaning |

## When to Call a Pro
If E6 persists after thermistor replacement, the outdoor PCB's sensor input circuit may be damaged. PCB replacement is within DIY scope for those comfortable with electronics, but verify you have the correct board part number before ordering.
