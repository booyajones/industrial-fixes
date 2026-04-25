---
title: "Trane XL20i Variable Speed Error Codes — Complete Guide"
description: "Trane XL20i variable speed heat pump error codes: all fault codes for the XL20i inverter-driven system with causes and technician-level fixes."
pubDatetime: 2026-04-22T19:00:00Z
modDatetime: 2026-04-22T19:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - trane
  - heat-pump
---

## Trane XL20i Error Codes — Quick Reference

The Trane XL20i is a variable-speed, inverter-driven heat pump that uses the ComfortLink II communicating system. Unlike single-stage units with simple LED blink codes, the XL20i reports detailed fault codes through the ComfortLink II thermostat and can store up to 10 fault history entries. Access fault history from the thermostat: Menu → Diagnostics → Fault History.

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixes-20) | Meaning | Quick Fix |
|------|---------|-----------|
| 79 | Inverter communication fault | Check communication wiring; power cycle |
| 80 | Inverter module fault | Inspect inverter board connections |
| 81 | Inverter overcurrent fault | Check for refrigerant restriction; check motor |
| 82 | Inverter overvoltage fault | Verify incoming voltage; check capacitors |
| 83 | Inverter undervoltage fault | Check power supply; check transformer |
| 90 | Compressor motor fault | Inverter-driven compressor issue |
| 91 | High-discharge temperature | Check refrigerant; check airflow |
| 92 | Low-pressure trip | Check charge; check defrost cycle |
| 93 | High-pressure trip | Check outdoor fan; clean coil |
| 94 | Outdoor fan fault | Outdoor fan motor or inverter fault |
| 95 | Indoor communication fault | Check ComfortLink bus wiring to AHU |
| 96 | Defrost sensor fault | Check defrost sensor; replace if failed |
| 97 | Ambient temperature sensor fault | Inspect outdoor ambient sensor |
| 126 | System communication loss | Check entire ComfortLink bus |

## Most Common Faults

### 79 / 126 — Communication Faults
The XL20i's inverter drive and the air handler communicate over the ComfortLink II two-wire data bus. Communication faults are the most common issues reported on XL20i systems, especially after lightning events or power surges. Power cycle the entire system: turn off the outdoor unit disconnect, the indoor unit breaker, and the thermostat for 5 minutes, then restore power. If the fault persists, inspect the data bus wiring — the bus uses two wires (+ and -) that must maintain polarity throughout the system.

### 81 — Inverter Overcurrent
The inverter module is detecting an overcurrent condition when trying to drive the variable-speed compressor. Causes include refrigerant restrictions (clogged metering device), low refrigerant charge, a failing compressor motor, or an actual inverter module failure. Because this fault has multiple causes, it requires a technician to measure pressures and motor winding resistance before condemning any specific component.

### 91 — High Discharge Temperature
The compressor discharge line temperature sensor detected overheating. On variable-speed compressors, this is almost always caused by insufficient refrigerant charge — the compressor runs at higher compression ratios to compensate, generating excess heat. It can also be caused by a blocked outdoor coil or failed outdoor fan. Check the outdoor coil for debris and verify the outdoor fan is operating.

### 92 — Low-Pressure Trip
Similar to standard heat pump low-pressure faults, this indicates suction-side pressure has dropped below the cutout point. On the XL20i, this can also be triggered by a malfunctioning defrost cycle that allows the outdoor coil to ice over completely. Verify the defrost cycle is operating: in heating mode, the outdoor coil should periodically go through a defrost (reversing valve switches, outdoor fan off, indoor coil acts as condenser for 5–15 minutes).

### 94 — Outdoor Fan Fault
The variable-speed outdoor fan on the XL20i is inverter-driven. An outdoor fan fault indicates the fan motor stalled, failed to reach target speed, or the fan inverter module has a problem. Unlike simple PSC fan motors, the XL20i's variable-speed fan cannot be tested with a simple voltage check — the fan inverter board needs to be inspected.

## XL20i Service Access Notes

- The XL20i inverter drive is located inside the outdoor unit
- High-voltage DC is present on inverter bus capacitors even after power is removed — wait 5 minutes before opening the inverter compartment
- ComfortLink II fault history stores timestamps for the last 10 faults — essential for diagnosis
- The XL20i requires Trane's Navigator or ComfortLink II service tools for full diagnostics

## When to Call a Pro
The XL20i is a complex inverter-driven system. All fault codes beyond communication wiring checks require a Trane-certified technician with ComfortLink II diagnostic training and refrigerant certification.
