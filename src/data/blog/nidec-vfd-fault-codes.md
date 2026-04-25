---
title: "Nidec (Leroy-Somer) VFD Fault Codes — Complete Guide"
description: "Nidec VFD fault codes for Leroy-Somer VARMECA, IMfinity, and Nidec Commander series drives: fault codes, causes, and step-by-step fixes."
pubDatetime: 2026-04-22T19:00:00Z
modDatetime: 2026-04-22T19:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - nidec
  - leroy-somer
  - motor-control
---

## Nidec / Leroy-Somer VFD Fault Codes — Quick Reference

Nidec Corporation acquired Control Techniques and Leroy-Somer, producing the Commander series drives (Commander C200, C300, C600) and integrated motor-drive units (VARMECA, IMfinity). The Commander series uses the same trip code terminology as the Control Techniques Unidrive platform.

| [Trip Code](https://www.amazon.com/s?k=Trip+Code&tag=errorcodefixes-20) | Meaning | Common Cause | Quick Fix |
|-----------|---------|-------------|-----------|
| [OI.AC](https://www.amazon.com/s?k=OI.AC&tag=errorcodefixes-20) | AC output overcurrent | Short circuit; fast acceleration | Check motor; increase accel time |
| OV | DC bus overvoltage | Fast decel; high supply voltage | Increase decel; add brake resistor |
| UV | DC bus undervoltage | Low supply voltage | Check incoming power |
| OH | Drive overtemperature | Blocked cooling; high ambient | Clean fans; improve ventilation |
| Ot | Motor overtemperature | Motor overloaded; bad PTC | Check motor load and cooling |
| SCL | Serial communications loss | Fieldbus disconnected | Check comms wiring and master |
| EEF | EEPROM/parameter fault | Corrupt parameters | Reset to defaults; reprogram |
| GF | Ground fault | Motor or cable insulation fault | Megger motor; inspect cable |
| th | Thermistor input fault | PTC wiring open or short | Check thermistor wiring |
| CLO | Current clamp overload | Sustained high-current condition | Reduce load; check mechanism |
| [tunE](https://www.amazon.com/s?k=tunE&tag=errorcodefixes-20) | Autotune fail | Motor does not match entered data | Verify motor nameplate data |
| I/O | I/O module fault | Option module communication lost | Reseat module; replace if needed |

## Most Common Faults

### OI.AC — Output Overcurrent
Nidec Commander drives share the overcurrent diagnosis path with other Control Techniques drives. The OI.AC trip on a Commander C200 or C300 means instantaneous current exceeded the drive's peak current limit (approximately 180–200% of rated). 

On the Commander series, check:
- Parameter P1.07 (motor rated current) matches the motor nameplate — an incorrectly set rated current will cause OI.AC trips even on normal starting
- The output wiring from drive terminals U/T1, V/T2, W/T3 to the motor — check for phase-to-phase or phase-to-ground shorts using a multimeter in continuity mode

### OV — DC Bus Overvoltage
On the Commander C200, DC bus overvoltage trip levels are:
- 200V drives: trip at approximately 415VDC
- 400V drives: trip at approximately 830VDC

The most effective fix for most pump/fan applications is enabling "intelligent" or "voltage-dependent" deceleration, where the drive automatically extends the decel ramp to keep the DC bus within safe limits. On Commander C300: Parameter P2.40 = 1 enables this feature.

### tunE — Autotune Failure
The Commander series can perform a stationary or rotating autotune to measure motor parameters. Autotune failure (tunE trip) occurs when the motor parameters measured during the test don't match the entered motor nameplate data, or when the motor shaft moves during a stationary tune.

**Fix:**
1. Verify that all motor nameplate parameters are entered correctly (rated voltage, current, frequency, speed, power factor)
2. For stationary autotune: ensure the load is not being manually held or doesn't create a restoring torque
3. For rotating autotune: ensure the load can safely spin — do not autotune with process equipment connected that could be damaged by unexpected rotation

### VARMECA and IMfinity Integrated Motor-Drive Notes
The Nidec VARMECA (motor with integrated drive) and IMfinity series use similar trip codes but display them on a programming tool (IMARSYS software) rather than a panel-mounted keypad. For VARMECA units:
- Connect via the RJ45 service port with IMARSYS software to read trips
- Integrated drives cannot be replaced separately — a failed drive in a VARMECA unit requires either drive repair or full unit replacement
- Thermal protection is handled by both the motor's built-in PTC and the drive's model-based thermal protection

## Commander Drive Parameter Access

| [Function](https://www.amazon.com/s?k=Function&tag=errorcodefixes-20) | Key Sequence |
|----------|-------------|
| [Access parameter menus](https://www.amazon.com/s?k=Access+parameter+menus&tag=errorcodefixes-20) | Press M button |
| [Navigate to trip history](https://www.amazon.com/s?k=Navigate+to+trip+history&tag=errorcodefixes-20) | Menu 10, parameters 10.20–10.29 |
| [Reset fault](https://www.amazon.com/s?k=Reset+fault&tag=errorcodefixes-20) | Press STOP/RESET after correcting fault |
| [Factory reset](https://www.amazon.com/s?k=Factory+reset&tag=errorcodefixes-20) | Set Pr 10.33 = 1000, then press ENTER |
| [Save parameters](https://www.amazon.com/s?k=Save+parameters&tag=errorcodefixes-20) | Set Pr 00.09 = 1000 |

## When to Call a Pro
GF (ground fault) with motor insulation failure and persistent OH (overtemperature) indicating drive damage require a Nidec-authorized service provider. VARMECA integrated unit faults requiring disassembly need factory service support.
