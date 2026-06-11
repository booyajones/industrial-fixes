---
title: "Johnson Controls Metasys BMS Fault Codes - Complete Guide"
description: "Johnson Controls Metasys building management system fault codes and alarms for NAE, NCE, and field controllers: causes and fixes."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - johnson-controls
  - metasys
  - bms
  - building-automation
money_part: "Metasys field controller (FEC/IOM)"
---

## Johnson Controls Metasys Fault Codes - Quick Reference

Johnson Controls Metasys BMS uses Network Automation Engines (NAE/NCE), Field Equipment Controllers (FEC, IOM), and Application Specific Controllers (VAV, AHU). Alarms appear on the Metasys UI, Site Control Panel, and via e-mail notifications.

| Alarm | Device | Meaning | Quick Fix |
|-------|--------|---------|-----------|
| Communication Lost | NAE/NCE | Controller offline | Check Ethernet/IP connection |
| Out of Range (OOR) | All | Sensor reading outside limits | Check sensor wiring and calibration |
| Temp High/Low Alarm | AHU/VAV | Zone temperature out of setpoint | Check equipment operation |
| Discharge Air Low | AHU | Discharge air temp too low | Check cooling coil valve |
| High Static Pressure | AHU | Duct static too high | Check VAV boxes and dampers |
| Fan Status Fail | AHU | Fan status feedback mismatch | Check fan, drive, and status input |
| Freeze Alarm | AHU | Freezestat tripped | Check heating coil and outdoor air |
| Filter Dirty | AHU | Filter DP switch activated | Replace air filter |
| Valve Override | All | Manual override active | Release override |
| Database Corrupt | NAE | NAE database error | Restore from backup |

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
| Metasys field controller (FEC/IOM) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-johnson-controls-metasys-fault&k=Metasys+field+controller+%28FEC%2FIOM%29&tag=errorcodefixes-20) \| Replace on hardware failure |
| Temperature/humidity sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-johnson-controls-metasys-fault&k=Temperature%2Fhumidity+sensor&tag=errorcodefixes-20) \| Replace on OOR alarm |
| MS/TP termination resistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-johnson-controls-metasys-fault&k=MS%2FTP+termination+resistor&tag=errorcodefixes-20) \| 120 ohm, one per trunk end |
| Actuator (damper/valve) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-johnson-controls-metasys-fault&k=Actuator+%28damper%2Fvalve%29&tag=errorcodefixes-20) \| Replace on stuck feedback |
| Freezestat | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-johnson-controls-metasys-fault&k=Freezestat&tag=errorcodefixes-20) \| Replace if trips repeatedly on reset |
## When to Call a Pro
Metasys NAE/NCE database management, firmware upgrades, and object configuration require Metasys-trained technicians. Incorrect NAE configuration can affect entire building HVAC systems simultaneously.

