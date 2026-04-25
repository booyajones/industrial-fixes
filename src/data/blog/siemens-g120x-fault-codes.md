---
title: "Siemens SINAMICS G120X Fault Codes: Complete Guide"
description: "Siemens SINAMICS G120X VFD fault codes and diagnostics. F-series and A-series codes, causes, and technician-level troubleshooting."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - siemens
  - industrial
  - motor-control
---

# Siemens SINAMICS G120X Fault Codes

The Siemens SINAMICS G120X is a purpose-built VFD for pump, fan, and HVAC applications rated 0.75ΓÇô630 kW. Like other SINAMICS drives, it uses F-codes (faults that require acknowledgment) and A-codes (alarms, informational). Codes display on the BOP-2 operator panel or through TIA Portal.

## G120X Fault Code Table

| Code | Fault Description | Common Cause | Action |
|------|------------------|--------------|--------|
| F00001 | Overcurrent | Motor overload, short circuit | Check motor winding, accel time |
| F00002 | Overvoltage | Regenerative energy from load | Add brake resistor or adjust ramp |
| F00003 | Undervoltage | Low supply voltage | Check input voltage |
| F00004 | Drive overtemperature | Ambient temp high, cooling blocked | Clean fins, check fan |
| F00011 | Motor overtemperature | Motor thermal model exceeded | Check motor load and cooling |
| F00012 | Overcurrent (software) | Motor current limit exceeded | Check load, increase ramp time |
| F00021 | Ground fault | Motor winding or cable ground fault | Megger test motor |
| F00025 | Load imbalance | Unbalanced motor current | Check motor winding resistance |
| F00051 | Parameter error | RAM fault or EEPROM | Restore defaults, reload parameters |
| F00052 | Power stack fault | IGBT or power module fault | Check DC bus and IGBT |
| F00101 | Power unit error | Internal fault | Contact Siemens support |
| F07801 | Motor stall | Motor jammed or locked rotor | Check mechanical load |
| F07900 | Motor blocked | No rotation detected | Check shaft and load |
| A07010 | Drive overtemperature warning | Approaching thermal limit | Improve cooling before fault |

## Most Common G120X Faults

### F00001 ΓÇö Overcurrent
Most common fault on pump and fan applications. The G120X has auto-tuning for motor data ΓÇö verify motor parameters match nameplate (P304 volts, P305 current, P307 power). Increase acceleration ramp time (P1120) to reduce inrush.

### F00004 ΓÇö Drive Overtemperature
G120X is rated -10┬░C to 50┬░C. Clean cooling fins with compressed air. The G120X has internal fans ΓÇö verify they spin up on power application. Check thermal sensor reading via diagnostics menu (r0037).

### F00021 ΓÇö Ground Fault
Perform insulation test on motor cable with megohmmeter. For long cable runs (>100m), install output reactor. Check motor frame ground connection.

### F00002 ΓÇö Overvoltage
On pump/fan applications, rapid deceleration causes motor to regenerate energy back into the drive. Extend deceleration ramp time (P1121) or install dynamic braking resistor. Check for voltage spikes on supply.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| BOP-2 operator panel | [Amazon](https://www.amazon.com/s?k=BOP-2+operator+panel&tag=errorcodefixes-20) \| Plug-in display for fault reading |
| Cooling fan | [Amazon](https://www.amazon.com/s?k=Cooling+fan&tag=errorcodefixes-20) \| Internal fan ΓÇö match G120X size |
| Power stack module | [Amazon](https://www.amazon.com/s?k=Power+stack+module&tag=errorcodefixes-20) \| Only for IGBT failure confirmed by Siemens |
| Input choke | [Amazon](https://www.amazon.com/s?k=Input+choke&tag=errorcodefixes-20) \| Reduces harmonic distortion |
| Output reactor | [Amazon](https://www.amazon.com/s?k=Output+reactor&tag=errorcodefixes-20) \| Required for long cable runs |
> **Pro tip:** G120X supports BICO (Binector-Connector) parameterization for complex control schemes. When all mechanical and electrical causes are ruled out, use STARTER or TIA Portal to export a complete parameter backup before resetting ΓÇö valuable for comparing pre- and post-fault parameters.

## Related Articles

- [Siemens Sinumerik 828D Alarm Codes Guide — Complete Diagnostic Reference](/posts/siemens-828d-alarm-codes/)
- [Siemens 840D Alarm 380000 — Causes & Fix](/posts/siemens-840d-alarm-380000/)
- [Siemens Circuit Breaker Fault Codes - Complete Guide](/posts/siemens-circuit-breaker-fault-codes/)
- [Siemens Desigo BMS Fault Codes - Complete Guide](/posts/siemens-desigo-fault-codes/)
- [Siemens Cerberus/MXL Fire Alarm Fault Codes — Troubleshooting Guide](/posts/siemens-fire-alarm-fault-codes/)
