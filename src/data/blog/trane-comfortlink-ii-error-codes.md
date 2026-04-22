---
title: "Trane ComfortLink II Error Codes — Common Faults and Fixes"
description: "Guide to Trane ComfortLink II communicating system error codes, what each fault means, and how to diagnose and fix the most common problems."
pubDatetime: 2026-04-22T14:00:00Z
modDatetime: 2026-04-22T14:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - trane
---

## Trane ComfortLink II Error Codes — What They Mean

Trane's ComfortLink II is a proprietary communicating system that links the thermostat, indoor unit, and outdoor unit over a two-wire communication bus. Error codes appear on the ComfortLink II thermostat display under the Service menu. Unlike older flash-code Trane furnaces, the ComfortLink II provides descriptive alphanumeric codes that pinpoint which component reported the fault and what type of failure occurred. The indoor and outdoor units each log their own codes.

[Jump to Fix](#fix)

## Most Common ComfortLink II Error Codes

| Code | Component | Meaning |
|------|-----------|---------|
| 79 | Outdoor unit | Communication loss between outdoor and indoor units |
| 126 | Indoor unit | Pressure switch open — inducer fault |
| 127 | Indoor unit | Pressure switch stuck closed |
| 128 | Indoor unit | Ignition failure |
| 174 | Outdoor unit | High discharge temperature |
| 178 | Outdoor unit | Low pressure lockout |
| 179 | Outdoor unit | High pressure lockout |
| 551 | System | ComfortLink thermostat communication fault |

## Common Causes

- **Code 79 — Communication loss** — The most frequent ComfortLink II complaint. Caused by loose wiring at the bus terminals (usually at the air handler or outdoor unit), a failed outdoor control board, or a failed thermostat.
- **Code 126 — Pressure switch open** — Same root causes as any inducer fault: blocked condensate drain, cracked pressure switch hose, failed inducer motor capacitor, or blocked flue.
- **Code 128 — Ignition failure** — Cracked hot surface ignitor, dirty flame sensor, low gas pressure, or failed gas valve.
- **Code 178/179 — Pressure lockouts** — Low or high refrigerant charge, dirty coil, failed fan, or refrigerant flow restriction. Requires gauges to distinguish the root cause.
- **Code 551 — Thermostat fault** — ComfortLink II thermostat has lost communication with the system equipment. Usually a wiring issue or a failed thermostat display unit.

## Step-by-Step Fix {#fix}

1. **Access the fault log** — On the ComfortLink II thermostat, press Menu > Service > Equipment Faults. Record all active and historical codes with timestamps. Intermittent codes (appearing only in cold or hot weather) point to refrigerant or pressure issues; persistent codes point to wiring or board failures.
2. **For Code 79** — Inspect both wires of the communication bus at the outdoor unit, the air handler/furnace, and the thermostat subbase. All connections must be tight and corrosion-free. Power cycle both units (30-second wait) after confirming wiring.
3. **For Code 126** — Check the condensate trap and drain for blockage first (pour water in, confirm flow). Then trace pressure switch hoses for cracks. Test the inducer motor for correct speed and the capacitor for correct µF value.
4. **For Code 128** — Inspect the hot surface ignitor for cracks; test resistance (40–75 ohms when cold). Clean the flame sensor rod with fine steel wool. Verify gas pressure at the manifold (natural gas: 3.5" W.C. minimum outlet pressure).
5. **For Codes 178/179** — Connect manifold gauges and compare suction/discharge pressures to the unit's pressure-temperature chart. Dirty condenser coil is the first thing to address for high pressure codes; check refrigerant charge last.
6. **Clear the fault and retest** — After repairs, clear faults from the Service menu and run a full heating or cooling cycle. Confirm the code does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ComfortLink II thermostat | For persistent Code 551 after wiring confirmed |
| Outdoor communicating control board | For persistent Code 79 with good wiring |
| Hot surface ignitor | Most common Code 128 fix |
| Pressure switch | For Code 126 that returns after drain and hose check |
| Condenser fan motor / capacitor | For Code 179 with clean coil |

## When to Call a Pro

ComfortLink II refrigerant work (Codes 178/179) requires EPA 608 certification and access to Trane's HVAC Pro app for system commissioning. Trane's variable-speed outdoor units also use inverter-driven compressors that require specialized diagnostics — standard clamp meters and multimeters don't give valid readings on the variable-frequency output side of the drive.
