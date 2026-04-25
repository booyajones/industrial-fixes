---
title: "Carrier Greenspeed Heat Pump Error Codes: Complete Guide"
description: "Carrier Greenspeed variable speed heat pump error codes and fault diagnostics. Infinity system fault codes, causes, and technician fixes."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - carrier
  - heat-pump
  - variable-speed
---

# Carrier Greenspeed Heat Pump Error Codes

Carrier Greenspeed heat pumps (25VNA series) use the Infinity communicating system. All fault codes display on the Infinity thermostat (SYSTXCCITC01-B or similar). These units use a variable-speed inverter compressor ΓÇö fault codes include inverter-specific issues.

## Greenspeed Fault Code Table

| Code | Fault Description | Common Cause | Action |
|------|------------------|--------------|--------|
| 11 | Ignition failure (gas) | N/A for heat pump | Check system configuration |
| 24 | Low-voltage fuse blown | Short in low-voltage wiring | Check all 24 VAC wiring |
| 25 | Reversing valve fault | RV stuck or solenoid issue | Check solenoid, measure RV temps |
| 31 | High-pressure switch | Dirty coil, overcharge | Wash coil, check charge |
| 32 | Low-pressure switch | Low charge or low ambient | Check refrigerant charge |
| 33 | Limit switch lockout | Air handler fault | Check AHU filter and motor |
| 41 | Inverter drive fault | Inverter board, DC bus | Check inverter LED, DC bus voltage |
| 42 | Low DC bus voltage | Input voltage problem | Check supply voltage |
| 43 | High DC bus voltage | Input voltage spike | Check voltage and surge protection |
| 44 | Inverter over-temperature | Inverter heatsink hot | Check inverter fan, clearances |
| 45 | Compressor fault | Compressor protection tripped | Check amps, check for locked rotor |
| 51 | Outdoor coil sensor fault | Failed sensor | Check resistance at sensor |
| 52 | Outdoor ambient sensor | Failed OAT sensor | Replace sensor |
| 61 | Indoor coil sensor fault | Failed sensor at AHU | Check sensor at indoor unit |
| 65 | Communication fault | Infinity bus wiring | Check Infinity network wiring |

## Most Common Greenspeed Faults

### Code 41 ΓÇö Inverter Drive Fault
The most complex fault on Greenspeed units. Check inverter board LEDs first ΓÇö they display a secondary fault code. Measure DC bus voltage at inverter board terminals (target 300ΓÇô350 VDC on 240 VAC input). A weak capacitor or failed transistor are common causes.

### Code 31 ΓÇö High-Pressure Switch
Greenspeed units use R-410A with a high-side limit of 590 psi. Dirty condenser coils or insufficient outdoor airflow are the most common causes. Check condenser fan motor operation ΓÇö Greenspeed uses variable-speed condenser fans.

### Code 65 ΓÇö Communication Fault
The Infinity bus uses a shielded 2-wire system. Any loose connection or short causes erratic communication faults. Check all Infinity wire connections at the outdoor unit, thermostat, and indoor unit.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Inverter board | [Amazon](https://www.amazon.com/s?k=Inverter+board&tag=errorcodefixes-20) \| Carrier part number critical ΓÇö match model |
| Infinity thermostat | [Amazon](https://www.amazon.com/s?k=Infinity+thermostat&tag=errorcodefixes-20) \| Required for code display and diagnostics |
| Defrost sensor | [Amazon](https://www.amazon.com/s?k=Defrost+sensor&tag=errorcodefixes-20) \| 10k╬⌐ thermistor type |
| High-pressure switch | [Amazon](https://www.amazon.com/s?k=High-pressure+switch&tag=errorcodefixes-20) \| Match R-410A setpoint |
| Outdoor fan motor | [Amazon](https://www.amazon.com/s?k=Outdoor+fan+motor&tag=errorcodefixes-20) \| Variable speed ΓÇö match HP and RPM |
> **Pro tip:** Carrier Infinity systems retain up to 12 fault codes with timestamps. Access via thermostat ΓåÆ Menu ΓåÆ Diagnostics ΓåÆ Fault History. Review history before clearing to identify recurring issues.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)
