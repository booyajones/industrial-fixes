---
title: "Danfoss FC102 VLT HVAC Drive Fault Codes — Complete Diagnostic Reference"
description: "Complete guide to Danfoss FC102 VLT HVAC Drive fault codes, alarm causes, and step-by-step repair procedures for HVAC and industrial technicians."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - danfoss
  - hvac
  - industrial
---

## Danfoss FC102 VLT HVAC Drive Fault Codes — What They Mean

The Danfoss VLT HVAC Drive FC102 is a variable frequency drive purpose-built for HVAC applications — air handling units, cooling towers, pumps, and compressors. It is part of Danfoss's VLT product line and is one of the most widely installed HVAC drives in commercial buildings worldwide. The FC102 displays faults using the prefix "AL" (alarm) and "WA" (warning) on the LCP (Local Control Panel). Alarms stop the drive; warnings allow continued operation with a logged event.

[Jump to Fix](#fix)

## Danfoss FC102 Alarm Code Reference

| [Alarm Code](https://www.amazon.com/s?k=Alarm%20Code&tag=errorcodefixe-20) | Description |
|---|---|
| [AL 2](https://www.amazon.com/s?k=AL%202&tag=errorcodefixe-20) | Live zero fault — 4–20mA signal lost |
| [AL 4](https://www.amazon.com/s?k=AL%204&tag=errorcodefixe-20) | Mains phase loss — input phase fault |
| [AL 5](https://www.amazon.com/s?k=AL%205&tag=errorcodefixe-20) | DC link voltage high — overvoltage |
| [AL 6](https://www.amazon.com/s?k=AL%206&tag=errorcodefixe-20) | DC link voltage low — undervoltage |
| [AL 7](https://www.amazon.com/s?k=AL%207&tag=errorcodefixe-20) | DC overvoltage — transient surge |
| [AL 8](https://www.amazon.com/s?k=AL%208&tag=errorcodefixe-20) | DC undervoltage |
| [AL 9](https://www.amazon.com/s?k=AL%209&tag=errorcodefixe-20) | Inverter overloaded — I²t |
| [AL 10](https://www.amazon.com/s?k=AL%2010&tag=errorcodefixe-20) | Motor ETR overload — thermal |
| [AL 11](https://www.amazon.com/s?k=AL%2011&tag=errorcodefixe-20) | Motor thermistor overtemperature |
| [AL 12](https://www.amazon.com/s?k=AL%2012&tag=errorcodefixe-20) | Torque limit — load too high |
| [AL 13](https://www.amazon.com/s?k=AL%2013&tag=errorcodefixe-20) | Overcurrent — output short circuit |
| [AL 14](https://www.amazon.com/s?k=AL%2014&tag=errorcodefixe-20) | Earth fault — ground fault on motor output |
| [AL 16](https://www.amazon.com/s?k=AL%2016&tag=errorcodefixe-20) | Short circuit — output phases shorted |
| [AL 17](https://www.amazon.com/s?k=AL%2017&tag=errorcodefixe-20) | Control word timeout — fieldbus loss |
| [AL 18](https://www.amazon.com/s?k=AL%2018&tag=errorcodefixe-20) | Startup fault |
| [AL 25](https://www.amazon.com/s?k=AL%2025&tag=errorcodefixe-20) | Brake resistor short circuit |
| [AL 29](https://www.amazon.com/s?k=AL%2029&tag=errorcodefixe-20) | Drive overtemperature — heatsink |
| [AL 30](https://www.amazon.com/s?k=AL%2030&tag=errorcodefixe-20) | Motor phase loss |
| [AL 34](https://www.amazon.com/s?k=AL%2034&tag=errorcodefixe-20) | Fieldbus communication fault |
| [AL 47](https://www.amazon.com/s?k=AL%2047&tag=errorcodefixe-20) | 24V supply low |
| [AL 65](https://www.amazon.com/s?k=AL%2065&tag=errorcodefixe-20) | Control card overtemperature |

## Common Causes by Code

- **AL 2 — Live zero** — The 4–20mA speed reference signal has fallen below 2mA. This occurs when the BMS output card fails, a wire is disconnected, or the sensor has lost power. Check the signal at the drive terminals (AI53/AI54) with a milliammeter.
- **AL 14 — Earth fault** — One or more motor output phases has a fault to ground. This is a common fault on older motors where winding insulation has degraded. Perform a megohm test on the motor with the drive disconnected.
- **AL 17 — Control word timeout** — The drive is configured for fieldbus control (Modbus/BACnet/PROFIBUS) and has lost communication with the master controller. Check the communication cable and the BMS controller address configuration. Parameter 8-04 sets the timeout action.
- **AL 29 — Drive overtemperature** — The heatsink temperature has exceeded the trip point. Check that the drive's cooling fan is operating (audible). Verify ambient temperature and panel ventilation. Clean the heatsink fins of dust with compressed air.
- **AL 34 — Fieldbus communication** — BACnet MS/TP, PROFIBUS, or Modbus loss. Verify network termination resistors are correctly placed (only at both ends of the MS/TP bus). Check the drive's network address matches the BMS configuration.

## Step-by-Step Fix {#fix}

1. **Read the LCP** — The Danfoss FC102 LCP displays the alarm code and the alarm text simultaneously. Press the INFO button on the LCP for additional information about the active alarm. Navigate to the Alarm Log (Main Menu > Alarm Log) for the last 10 faults.
2. **For AL 14 (earth fault)** — Power down and lockout the drive. Disconnect the motor cable at the drive output terminals. Use a 500V or 1000V megohmmeter to measure insulation resistance from each motor terminal to ground — should be greater than 1 MΩ. If insulation is low, the motor requires rewinding or replacement.
3. **For AL 29 (overtemperature)** — With the drive powered (carefully), check if the internal fan is running. For IP21 drives in an electrical panel, confirm the panel has adequate ventilation. Check the heatsink fins for dust accumulation — blow out with compressed air.
4. **For AL 17 (control word timeout)** — Check BMS communication to the drive via the network. If using BACnet MS/TP, verify the drive's MS/TP address is unique on the bus and that the baud rate (parameter 8-32) matches the BMS setting.
5. **Clear and restart** — Press the RESET button on the LCP or send a reset command from the BMS. The FC102 will not auto-restart on AL faults — a reset must be commanded.

## Parts Often Needed

| Part | Notes |
|---|---|
| [LCP panel](https://www.amazon.com/s?k=LCP%20panel&tag=errorcodefixe-20) | For display faults; replaceable without drive power-off |
| [HVAC drive cooling fan](https://www.amazon.com/s?k=HVAC%20drive%20cooling%20fan&tag=errorcodefixe-20) | Internal replacement fan; fan fault causes AL 29 |
| [Motor thermistor](https://www.amazon.com/s?k=Motor%20thermistor&tag=errorcodefixe-20) | KTY or PTC; for AL 11 |
| [BACnet/IP or Modbus card](https://www.amazon.com/s?k=BACnet%2FIP%20or%20Modbus%20card&tag=errorcodefixe-20) | For fieldbus integration |
| [Complete FC102 drive](https://www.amazon.com/s?k=Complete%20FC102%20drive&tag=errorcodefixe-20) | For hardware faults or severe damage |

## When to Call a Pro

The Danfoss FC102 supports remote monitoring via the Danfoss iFJørd and Building Connect platforms. A Danfoss-authorized service center can access the full diagnostic log and configure parameters remotely. Insulation testing and motor replacement require electrical work licenses in most jurisdictions — do not attempt insulation testing without proper lockout/tagout.
