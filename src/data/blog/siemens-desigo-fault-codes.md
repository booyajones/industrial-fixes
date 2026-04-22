---
title: "Siemens Desigo BMS Fault Codes - Complete Guide"
description: "Siemens Desigo CC and Desigo Insight BMS fault codes and alarms for PXC controllers and field devices: causes and diagnostic steps."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - siemens
  - desigo
  - bms
  - building-automation
---

## Siemens Desigo BMS Fault Codes - Quick Reference

Siemens Desigo building management systems use PXC (Compact), PXM (Modular), and PXA (Application) controllers with room units and field devices. Alarms appear in Desigo CC or Desigo Insight management stations.

| [Alarm](https://www.amazon.com/s?k=Alarm&tag=errorcodefixe-20) | Device | Meaning | [Quick Fix](https://www.amazon.com/s?k=Quick%20Fix&tag=errorcodefixe-20) |  |-------|--------|---------|-----------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Communication Error | PXC/PXM | [Controller offline](https://www.amazon.com/s?k=Controller%20offline&tag=errorcodefixe-20) | Check Ethernet/BACnet IP |
| [Sensor Fault](https://www.amazon.com/s?k=Sensor%20Fault&tag=errorcodefixe-20) | PXC Input | Sensor reading invalid | [Check sensor wiring](https://www.amazon.com/s?k=Check%20sensor%20wiring&tag=errorcodefixe-20) |  | Valve Fault | [AHU](https://www.amazon.com/s?k=AHU&tag=errorcodefixe-20) | Valve actuator feedback mismatch | Check actuator and wiring | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Fan Fault | AHU | [Fan status not matching command](https://www.amazon.com/s?k=Fan%20status%20not%20matching%20command&tag=errorcodefixe-20) | Check VFD/starter and status |
| [Freeze Protection Active](https://www.amazon.com/s?k=Freeze%20Protection%20Active&tag=errorcodefixe-20) | AHU | Low temperature alarm | [Check heating coil and OA damper](https://www.amazon.com/s?k=Check%20heating%20coil%20and%20OA%20damper&tag=errorcodefixe-20) |  | Filter Alarm | [AHU](https://www.amazon.com/s?k=AHU&tag=errorcodefixe-20) | Dirty air filter | Replace filter | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Room Temp High/Low | Room unit | [Room temperature fault](https://www.amazon.com/s?k=Room%20temperature%20fault&tag=errorcodefixe-20) | Check zone heating/cooling |
| [Time Program Fault](https://www.amazon.com/s?k=Time%20Program%20Fault&tag=errorcodefixe-20) | PXC | Scheduling error | [Check controller clock and program](https://www.amazon.com/s?k=Check%20controller%20clock%20and%20program&tag=errorcodefixe-20) |  | Hardware Fault | [PXC](https://www.amazon.com/s?k=PXC&tag=errorcodefixe-20) | Controller hardware error | Replace controller module | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | BACnet Comm Fault | MS/TP | [Field bus communication error](https://www.amazon.com/s?k=Field%20bus%20communication%20error&tag=errorcodefixe-20) | Check MS/TP wiring and address |

## Most Common Faults

### Communication Error (BACnet MS/TP)
Siemens PXC controllers communicate over BACnet MS/TP (RS-485) or BACnet IP. MS/TP faults occur from bus address conflicts, missing or extra terminators, or cable damage. Each device needs a unique address; verify with Siemens XWORKS or Desigo CC point browser. Add a 120-ohm terminator at each trunk end.

### Sensor Fault
Siemens Desigo PXC inputs accept Ni1000, PT1000, 0–10V, and 4–20mA signals. A sensor fault typically means a broken wire (reads full-scale or zero) or wrong input type configured in XWORKSplus. Check the raw input count in the controller's diagnostic screen.

### Freeze Protection Active
When a Desigo AHU controller detects temperatures below the freeze protection setpoint (typically 4–7°C on the preheat coil leaving air), it closes the outdoor air damper, opens the heating valve fully, and alarms. Check the preheat coil valve for freezing or failure, and verify the freezestat position and wiring.

### Hardware Fault
PXC hardware faults indicate a failed processor module, power supply, or flash memory error. Check the module status LED - a solid red LED on the PXC module indicates hardware failure. Try a cold restart (power cycle) first; if the fault persists, replace the module.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [PXC compact controller module](https://www.amazon.com/s?k=PXC%20compact%20controller%20module&tag=errorcodefixe-20) | Replace on hardware fault |
| [Room unit (QMX3.P)](https://www.amazon.com/s?k=Room%20unit%20(QMX3.P)&tag=errorcodefixe-20) | Replace on room unit fault |
| [Actuator (SQS/SKS)](https://www.amazon.com/s?k=Actuator%20(SQS%2FSKS)&tag=errorcodefixe-20) | Replace on valve fault |
| [MS/TP cable](https://www.amazon.com/s?k=MS%2FTP%20cable&tag=errorcodefixe-20) | Replace on bus faults |
| [Temperature sensor (QAP)](https://www.amazon.com/s?k=Temperature%20sensor%20(QAP)&tag=errorcodefixe-20) | Replace on sensor fault |

## When to Call a Pro
Desigo CC database configuration, PXC programming with XWORKSplus, and network integration require Siemens-trained personnel. Incorrect configuration changes can affect entire building zones simultaneously.

