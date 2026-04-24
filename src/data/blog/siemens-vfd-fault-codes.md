---
title: "Siemens VFD Fault Codes — SINAMICS G120, V20, S120 Guide"
description: "Siemens VFD fault codes: F-codes and A-codes for SINAMICS G120, V20, S120, and Micromaster 440 drives with causes and fixes."
pubDatetime: 2026-04-22T16:00:00Z
modDatetime: 2026-04-22T16:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - siemens
---

## Siemens VFD Fault Codes — Quick Reference

Siemens SINAMICS drives use **F-codes** (faults that stop the drive) and **A-codes** (alarms that allow continued operation). Codes are displayed on the BOP-2 operator panel or via STARTER/SINAMICS Startdrive software. The Micromaster 4xx series uses slightly different fault numbering.

| Code | Drive | Meaning | Common Fix |
|------|-------|---------|-----------|
| F00001 | G120/S120 | Overcurrent | Check motor; extend ramp |
| F00002 | G120/S120 | Overvoltage | Extend decel; add brake resistor |
| F00003 | G120/S120 | Undervoltage | Check supply voltage |
| F00004 | G120/S120 | Drive overtemperature | Clean fan; check ambient |
| F00011 | G120/S120 | Motor overcurrent | Check motor FLA parameter |
| F00012 | G120 | Motor overtemperature | Check motor temp sensor |
| F00015 | G120 | Motor phase loss | Check motor cable |
| F00021 | G120/V20 | Ground fault | Megger motor and cable |
| F00051 | G120 | Parameter EEPROM fault | Save parameters; check NVRAM |
| F00052 | G120 | CU EEPROM fault | Replace Control Unit |
| F00070 | G120 | Communication fault (PROFIBUS/PN) | Check fieldbus connection |
| F1 | V20 | Overcurrent | Check motor and ramp |
| F4 | V20 | Underload | Check belt/pump; verify load |
| F001 | MM440 | Overcurrent | Reduce accel ramp; check motor |

## Most Common Codes

### F00001: Overcurrent (SINAMICS G120/S120)
The output current exceeded the configured threshold. On G120, the fault threshold depends on the selected overload category (e.g., HO — High Overload 200% for 3 sec, LO — Low Overload 110% continuous). Verify p0640 (current limit) is set appropriately. Check motor data in p0304–p0311 matches nameplate. If the motor was replaced with a different frame size, re-run the motor identification routine (p1910 = 1 then run).

### F00002: Overvoltage
Regenerative energy raised the DC bus. On G120, enable kinetic buffering (p1240) for loads that coast, or extend decel ramp (p1121). G120 drives with integrated braking chopper (Power Module PM260 or PM330) can use an external resistor — connect and enable via p1237.

### F00004: Drive Overtemperature
The drive's internal temperature (heatsink or ambient) exceeded limits. On G120 with PM230/240/250/260 Power Modules, the cooling fan is located in the PM. Pull the PM module and check the fan for dust buildup. On PM330 and larger, the fan is field-replaceable. Siemens specifies maximum 40°C ambient for rated operation; above 40°C, the drive must be derated.

### F00021: Ground Fault (G120)
Ground current detected in the output phase. Disconnect motor and megger test. On G120, also check the PM module's output terminals for moisture or arc tracking — these modules are IP20 rated and should not be exposed to condensation.

### F00070: Communication Fault (PROFIBUS/PROFINET)
The drive lost communication with the PLC/controller over the fieldbus. On G120 with PROFINET, verify the GSDML file version matches the firmware on the drive's Communication Unit (CU250S-2, CU240E-2). A version mismatch causes telegram configuration errors that appear as F00070 on startup.

### F4 (V20): Underload
SINAMICS V20 unique — the drive detected motor current significantly below expected. Common causes: belt breakage on a conveyor or fan, pump cavitation, or the motor became disconnected. Enable underload monitoring via P2195 and set trip level per application.

### F00051 / F00052: EEPROM Fault (G120)
The non-volatile memory used to store drive parameters has a fault. For F00051 (Parameter memory), try saving all parameters again (p0977 = 1). If fault persists, the CU memory may be failing — back up parameters via STARTER before the data is lost. For F00052, the Control Unit itself needs replacement.

## Acknowledging and Resetting Faults

- **BOP-2 panel:** Press the P key while the fault code is displayed.
- **Digital input:** Configure a digital input for "Fault acknowledge" in p0700.
- **STARTER software:** Use the drive control panel or fault list acknowledgment.
- **Power cycle:** Cycling 24V control power clears most faults after the cause is resolved.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Control Unit | [Amazon](https://www.amazon.com/s?k=Control+Unit&tag=errorcodefixes-20) \| G120 CU240E-2, CU250S-2 — match order code |
| Power Module fan | [Amazon](https://www.amazon.com/s?k=Power+Module+fan&tag=errorcodefixes-20) \| PM230/240 frame B–F fans available separately |
| Braking resistor | [Amazon](https://www.amazon.com/s?k=Braking+resistor&tag=errorcodefixes-20) \| SINAMICS BRT or equivalent |
| BOP-2 panel | [Amazon](https://www.amazon.com/s?k=BOP-2+panel&tag=errorcodefixes-20) \| 6SL3255-0AA00-4CA1 |
## When to Call a Pro
F00052 (CU EEPROM fault) and any fault requiring Power Module (drive output stage) replacement should be handled by Siemens-trained drive service. PM replacement on G120 drives in Panel Through-Mounting configurations also requires electrical panel work.
