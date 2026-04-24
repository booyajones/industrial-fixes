---
title: "GE Multilin Protective Relay Fault Codes — Troubleshooting Guide"
description: "GE Multilin protective relay fault codes and trip records for 369, 489, 750, 850, and UR series relays: causes, diagnostics, and reset procedures."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - protective-relay
  - ge-multilin
  - power-distribution
  - industrial
---

## GE Multilin Protective Relay Fault Codes — Quick Reference

GE Multilin relays (369 Motor Management, 489 Generator, 750/760 Feeder, 850 Motor, and UR Series) record trip events with cause codes that appear on the display and in the event log via the EnerVista software.

| Element | Protection Function | Common Trip Cause |
|---------|-------------------|------------------|
| 50 — Instantaneous Overcurrent | High magnitude fault current | Short circuit on protected equipment |
| 51 — Time Overcurrent | Sustained overcurrent | Overload or slow fault |
| 46 — Negative Sequence | Phase unbalance | Open phase or unbalanced load |
| 49 — Thermal Model | Thermal limit exceeded | Motor overloaded, stalls, or hot |
| 27 — Undervoltage | Voltage below threshold | Supply problem or voltage sag |
| 59 — Overvoltage | Voltage above threshold | Supply transient or regulator issue |
| 87 — Differential | Current mismatch across zone | Internal fault in transformer or motor |
| 67 — Directional OC | Fault current in wrong direction | Reverse power or backfeed |

## Most Common Trips

### Element 49 — Thermal Model Trip (369/850)
The GE Multilin 369 Motor Management Relay models motor thermal state using measured current. A thermal trip means the motor reached its modeled thermal limit. Check: Was the motor subjected to multiple consecutive starts? Did it run overloaded? Allow adequate cooling time (check the relay's thermal capacity remaining on the display) before restart.

### Element 50/51 — Overcurrent Trip
Check the event log for the fault current magnitude. A 50 (instantaneous) trip indicates a high-magnitude fault. A 51 (time overcurrent) indicates sustained overcurrent. Use the trip magnitude to narrow the fault location — a high magnitude 50 trip likely indicates a fault close to the relay; a lower value 51 indicates a more distant or sustained overload condition.

### Element 46 — Negative Sequence
Open-phase conditions, blown fuses, or severe load imbalance create negative sequence current. Check all three phase fuses and confirm all three phases are present and within 2% voltage balance.

## Reading the Event Log

Use the front panel display or EnerVista software:
1. Navigate to ACTUAL → EVENT LOG
2. View the most recent trip: element, timestamp, and measured values at time of trip
3. Compare to settings to verify the trip was appropriate

## Parts / Actions Often Needed

| Action | Notes |
|--------|-------|
| Reset trip | [Amazon](https://www.amazon.com/s?k=Reset+trip&tag=errorcodefixes-20) \| Front panel RESET after fault cleared |
| EnerVista software | [Amazon](https://www.amazon.com/s?k=EnerVista+software&tag=errorcodefixes-20) \| Required for full event log and settings |
| CT secondary check | [Amazon](https://www.amazon.com/s?k=CT+secondary+check&tag=errorcodefixes-20) \| Verify CT ratios match relay settings |
| Firmware update | [Amazon](https://www.amazon.com/s?k=Firmware+update&tag=errorcodefixes-20) \| If relay displays self-diagnostic fault |
## Jump to Fix

- **Thermal (49) trip** → Check thermal capacity on display → Allow cooling → Investigate overload
- **50/51 OC trip** → Record trip current from event log → Locate fault → Clear before reset
- **46 unbalance** → Check all three phases → Inspect fuses → Correct load imbalance

## When to Call a Pro
Protective relay settings (coordination studies, time-current curves) should be performed by a licensed protection engineer. GE Multilin service is available for firmware, calibration, and repair.
