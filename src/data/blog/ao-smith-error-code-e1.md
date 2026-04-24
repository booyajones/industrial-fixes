---
title: "A.O. Smith Water Heater E1 Error Code — Sensor Fault Guide"
description: "A.O. Smith water heater E1 error means a temperature sensor fault. This guide covers gas and electric models, sensor testing, and how to fix or replace the sensor."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - ao-smith
  - water-heater
  - error-code
  - sensor
---

## A.O. Smith Water Heater E1 Error — Sensor Fault

**E1 on an A.O. Smith water heater** indicates a **temperature sensor fault** — the control system has detected the water temperature sensor is reading out of range, shorted, or open circuit. This is common on A.O. Smith Voltex (heat pump), Signature Series, and Proline XE electric water heaters.

*Note: A.O. Smith gas water heaters with LED flash codes use a different numbering system — E1 typically appears on models with digital displays or EcoNet-connected models.*

## A.O. Smith Models That Show E1

| Model Series | E1 Meaning |
|---|---|
| Voltex (AHPT series) | Upper temperature sensor fault |
| Signature 900 (HPTU) | Temperature sensor or heat pump sensor |
| ProLine XE (ELDS, ELD) | Element or sensor fault |
| Vertex (GPVH) | Gas control sensor fault |

## Where Are the Sensors?

A.O. Smith water heaters typically have:
1. **Upper tank sensor** — on the upper section, monitors hot water at top of tank
2. **Lower tank sensor** — on the lower section
3. **Inlet/outlet sensors** (heat pump models) — monitor refrigerant circuit temperatures
4. **Ambient sensor** (Voltex) — measures room temperature for heat pump mode

E1 usually means the **upper tank sensor** has failed.

## Testing the Temperature Sensor

The sensors are NTC thermistors that change resistance with temperature:

| Temperature | Expected Resistance |
|---|---|
| 32°F (0°C) | ~32,650 ohms |
| 68°F (20°C) | ~12,490 ohms |
| 77°F (25°C) | ~10,000 ohms |
| 120°F (49°C) | ~3,600 ohms |

**To test:**
1. Turn off circuit breaker to the water heater
2. Locate the sensor on the tank (usually a small clip-on or immersion probe connected by 2 wires)
3. Disconnect the sensor leads
4. Set multimeter to ohms
5. Measure across the two sensor leads at known room temperature
6. Compare to table — if reading is 0 (shorted) or OL (open), replace the sensor

## Why Sensors Fail

- **Thermal cycling stress** — 20+ years of heat/cool cycles crack the sensor housing
- **Scale buildup** — hard water scale coats the sensor well, slowing thermal response
- **Age** — sensors in the 8–15 year range commonly fail
- **Surge damage** — lightning strike or voltage spike can damage the sensing circuit

## Replacing the E1 Sensor

For most A.O. Smith models:
1. Turn off circuit breaker and shut off cold water supply
2. Connect a hose to the drain valve and drain 2–3 gallons (enough to lower water below sensor)
3. Disconnect the two sensor wires
4. Unscrew the sensor (may be threaded into a port) or unclip (clip-style)
5. Install new sensor — hand tighten, then 1/4 turn with wrench
6. Reconnect wires, restore water and power

**OEM sensors:** Order by model number from A.O. Smith parts (AO Smith part #s start with 100, 9000 series). Universal NTC sensors with matching resistance curves can also work.

## E1 on A.O. Smith Voltex Heat Pump Heaters

On Voltex models, E1 can also indicate a refrigerant circuit sensor fault. If the error appears only in heat pump mode (not electric resistance mode), the issue is likely the evaporator or discharge temperature sensor in the refrigerant circuit. This typically requires a certified refrigerant technician.

## What Happens If You Ignore E1

The water heater will continue heating but may:
- Use default temperature targets (may over-heat or under-heat)
- Disable heat pump mode and fall back to resistance heating (higher energy cost)
- Eventually lock out entirely if the sensor reading drifts dangerously

Don't ignore E1 — a $25–50 sensor replacement avoids a potential burnout of the control board ($200+) if the heater overheats due to bad sensor data.

## Parts Reference

| Part | Cost |
|---|---|
| NTC temperature sensor (universal) | $15–30 |
| A.O. Smith OEM sensor | $25–60 |
| Control board (if sensor input failed) | $100–250 |
