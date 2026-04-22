---
title: "Johnson Controls Metasys BMS Fault Codes - Complete Guide"
description: "Johnson Controls Metasys building management system fault codes and alarms for NAE, NCE, and field controllers: causes and fixes."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - johnson-controls
  - metasys
  - bms
  - building-automation
---

## Johnson Controls Metasys Fault Codes - Quick Reference

Johnson Controls Metasys BMS uses Network Automation Engines (NAE/NCE), Field Equipment Controllers (FEC, IOM), and Application Specific Controllers (VAV, AHU). Alarms appear on the Metasys UI, Site Control Panel, and via e-mail notifications.

| [Alarm](https://www.amazon.com/s?k=Alarm&tag=errorcodefixe-20) | Device | Meaning | [Quick Fix](https://www.amazon.com/s?k=Quick%20Fix&tag=errorcodefixe-20) |  |-------|--------|---------|-----------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Communication Lost | NAE/NCE | [Controller offline](https://www.amazon.com/s?k=Controller%20offline&tag=errorcodefixe-20) | Check Ethernet/IP connection |
| [Out of Range (OOR)](https://www.amazon.com/s?k=Out%20of%20Range%20(OOR)&tag=errorcodefixe-20) | All | Sensor reading outside limits | [Check sensor wiring and calibration](https://www.amazon.com/s?k=Check%20sensor%20wiring%20and%20calibration&tag=errorcodefixe-20) |  | Temp High/Low Alarm | [AHU/VAV](https://www.amazon.com/s?k=AHU%2FVAV&tag=errorcodefixe-20) | Zone temperature out of setpoint | Check equipment operation | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Discharge Air Low | AHU | [Discharge air temp too low](https://www.amazon.com/s?k=Discharge%20air%20temp%20too%20low&tag=errorcodefixe-20) | Check cooling coil valve |
| [High Static Pressure](https://www.amazon.com/s?k=High%20Static%20Pressure&tag=errorcodefixe-20) | AHU | Duct static too high | [Check VAV boxes and dampers](https://www.amazon.com/s?k=Check%20VAV%20boxes%20and%20dampers&tag=errorcodefixe-20) |  | Fan Status Fail | [AHU](https://www.amazon.com/s?k=AHU&tag=errorcodefixe-20) | Fan status feedback mismatch | Check fan, drive, and status input | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Freeze Alarm | AHU | [Freezestat tripped](https://www.amazon.com/s?k=Freezestat%20tripped&tag=errorcodefixe-20) | Check heating coil and outdoor air |
| [Filter Dirty](https://www.amazon.com/s?k=Filter%20Dirty&tag=errorcodefixe-20) | AHU | Filter DP switch activated | [Replace air filter](https://www.amazon.com/s?k=Replace%20air%20filter&tag=errorcodefixe-20) |  | Valve Override | [All](https://www.amazon.com/s?k=All&tag=errorcodefixe-20) | Manual override active | Release override | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Database Corrupt | NAE | [NAE database error](https://www.amazon.com/s?k=NAE%20database%20error&tag=errorcodefixe-20) | Restore from backup |

## Most Common Faults

### Communication Lost
A controller showing Communication Lost in Metasys means the NAE or NCE cannot reach the field controller via BACnet MS/TP (RS-485) or BACnet IP. Check the MS/TP wiring for broken wires, incorrect termination, or address conflicts. MS/TP requires a 120-ohm terminator at each end of the trunk only - extra terminators cause reflections and communication loss.

### Out of Range (OOR) Sensor
OOR alarms indicate a sensor reading outside its configured high/low limits. Causes include: failed sensor, broken wire, incorrect input configuration (0–10V vs 4–20mA), or a shorted input. Check the raw input value in Metasys - a 0% or 100% reading with a known engineering unit indicates a wiring failure.

### Fan Status Fail
Metasys AHU controllers compare the commanded fan state with the status feedback (usually a current sensor or differential pressure switch). Status Fail means the command says ON but the status says OFF, or vice versa. Check the fan drive (VFD or motor starter) and the status input wiring.

### Freeze Alarm
A freezestat in an AHU trips on low coil temperature to prevent chilled water coil freezing. The alarm latches and requires a manual reset at the freezestat. After resetting, investigate the cause: stuck outdoor air damper, heating coil valve failure, or loss of hot water supply.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Metasys field controller (FEC/IOM)](https://www.amazon.com/s?k=Metasys%20field%20controller%20(FEC%2FIOM)&tag=errorcodefixe-20) | Replace on hardware failure |
| [Temperature/humidity sensor](https://www.amazon.com/s?k=Temperature%2Fhumidity%20sensor&tag=errorcodefixe-20) | Replace on OOR alarm |
| [MS/TP termination resistor](https://www.amazon.com/s?k=MS%2FTP%20termination%20resistor&tag=errorcodefixe-20) | 120 ohm, one per trunk end |
| [Actuator (damper/valve)](https://www.amazon.com/s?k=Actuator%20(damper%2Fvalve)&tag=errorcodefixe-20) | Replace on stuck feedback |
| [Freezestat](https://www.amazon.com/s?k=Freezestat&tag=errorcodefixe-20) | Replace if trips repeatedly on reset |

## When to Call a Pro
Metasys NAE/NCE database management, firmware upgrades, and object configuration require Metasys-trained technicians. Incorrect NAE configuration can affect entire building HVAC systems simultaneously.

