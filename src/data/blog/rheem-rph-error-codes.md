---
title: "Rheem RPH Series Packaged Unit Error Codes: Complete Guide"
description: "Rheem RPH packaged heat pump error codes and fault diagnostics. Flash codes, fault descriptions, and step-by-step technician fixes."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - rheem
  - packaged-unit
  - heat-pump
---

# Rheem RPH Series Packaged Unit Error Codes

Rheem RPH packaged heat pump units use an LED diagnostic indicator on the control board. Flash sequences indicate specific faults — count flashes between 3-second pauses. Units with the EcoNet communicating system display alphanumeric codes on the thermostat.

## RPH Flash Code Table

| Flashes | Fault Description | Common Cause | Action |
|---------|------------------|--------------|--------|
| 2 | Low-pressure lockout | Low charge or frozen coil | Check refrigerant charge |
| 3 | High-pressure lockout | Dirty coil or failed fan | Wash condenser coil |
| 4 | Open high-pressure switch | Overcharge or condenser blockage | Check subcooling |
| 5 | Open low-pressure switch | Low refrigerant, TXV issue | Inspect TXV and charge level |
| 6 | Outdoor fan motor fault | Failed motor or run capacitor | Check capacitor and motor amps |
| 7 | Defrost fault | Defrost sensor or board failure | Check sensor clip and board |
| 8 | Reversing valve stuck | Mechanical or solenoid failure | Check 24 VAC to solenoid |
| 9 | Control board failure | Internal failure | Replace control board |
| Steady ON | Normal operation or continuity | No active fault | N/A |

## Most Common RPH Faults

### 3 Flashes — High-Pressure Lockout
Most common summer service call on packaged units. Verify condenser fan rotation (should pull air up through the coil). Wash coil with commercial coil cleaner. Check for restricted condenser fan discharge.

### 2 Flashes — Low Pressure
In cooling mode: check refrigerant charge using subcooling method. In heating mode: ice on outdoor coil triggers LP trip — verify defrost system operation.

### 7 Flashes — Defrost Fault
Confirm defrost thermostat is clipped firmly to the liquid line near the outdoor coil. Check defrost board timing pins — jumper JP1 sets cycle time. Verify defrost terminates within 14 minutes.

### 8 Flashes — Reversing Valve
Rheem RPH reversing valves are energized in cooling. If stuck in one position, you'll have cooling-only or heating-only operation. Measure solenoid coil resistance (typically 18–30 Ω).

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Defrost board | Critical — match to exact model |
| Defrost thermostat | Available in multiple trip temperatures |
| Run capacitor | Dual-run — test both sections |
| Reversing valve | Match tonnage and refrigerant type |
| Contactor | Check for pitting and coil voltage |
| Control board | Match unit serial and model number |

> **Pro tip:** Rheem RPH units with EcoNet log fault history with timestamps. Connect EcoNet app to retrieve detailed fault history before servicing — saves significant diagnostic time.
