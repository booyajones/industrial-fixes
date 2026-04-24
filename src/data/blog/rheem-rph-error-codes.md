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

Rheem RPH packaged heat pump units use an LED diagnostic indicator on the control board. Flash sequences indicate specific faults ΓÇö count flashes between 3-second pauses. Units with the EcoNet communicating system display alphanumeric codes on the thermostat.

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

### 3 Flashes ΓÇö High-Pressure Lockout
Most common summer service call on packaged units. Verify condenser fan rotation (should pull air up through the coil). Wash coil with commercial coil cleaner. Check for restricted condenser fan discharge.

### 2 Flashes ΓÇö Low Pressure
In cooling mode: check refrigerant charge using subcooling method. In heating mode: ice on outdoor coil triggers LP trip ΓÇö verify defrost system operation.

### 7 Flashes ΓÇö Defrost Fault
Confirm defrost thermostat is clipped firmly to the liquid line near the outdoor coil. Check defrost board timing pins ΓÇö jumper JP1 sets cycle time. Verify defrost terminates within 14 minutes.

### 8 Flashes ΓÇö Reversing Valve
Rheem RPH reversing valves are energized in cooling. If stuck in one position, you'll have cooling-only or heating-only operation. Measure solenoid coil resistance (typically 18ΓÇô30 ╬⌐).

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Defrost board | [Amazon](https://www.amazon.com/s?k=Defrost+board&tag=errorcodefixes-20) \| Critical ΓÇö match to exact model |
| Defrost thermostat | [Amazon](https://www.amazon.com/s?k=Defrost+thermostat&tag=errorcodefixes-20) \| Available in multiple trip temperatures |
| Run capacitor | [Amazon](https://www.amazon.com/s?k=Run+capacitor&tag=errorcodefixes-20) \| Dual-run ΓÇö test both sections |
| Reversing valve | [Amazon](https://www.amazon.com/s?k=Reversing+valve&tag=errorcodefixes-20) \| Match tonnage and refrigerant type |
| Contactor | [Amazon](https://www.amazon.com/s?k=Contactor&tag=errorcodefixes-20) \| Check for pitting and coil voltage |
| Control board | [Amazon](https://www.amazon.com/s?k=Control+board&tag=errorcodefixes-20) \| Match unit serial and model number |
> **Pro tip:** Rheem RPH units with EcoNet log fault history with timestamps. Connect EcoNet app to retrieve detailed fault history before servicing ΓÇö saves significant diagnostic time.
