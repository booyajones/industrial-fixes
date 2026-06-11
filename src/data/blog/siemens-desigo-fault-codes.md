---
title: "Siemens Desigo BMS Fault Codes - Complete Guide"
description: "Siemens Desigo CC and Desigo Insight BMS fault codes and alarms for PXC controllers and field devices: causes and diagnostic steps."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - siemens
  - desigo
  - bms
  - building-automation
money_part: "PXC compact controller module"
---

## Siemens Desigo BMS Fault Codes - Quick Reference

Siemens Desigo building management systems use PXC (Compact), PXM (Modular), and PXA (Application) controllers with room units and field devices. Alarms appear in Desigo CC or Desigo Insight management stations.

| Alarm | Device | Meaning | Quick Fix |
|-------|--------|---------|-----------|
| Communication Error | PXC/PXM | Controller offline | Check Ethernet/BACnet IP |
| Sensor Fault | PXC Input | Sensor reading invalid | Check sensor wiring |
| Valve Fault | AHU | Valve actuator feedback mismatch | Check actuator and wiring |
| Fan Fault | AHU | Fan status not matching command | Check VFD/starter and status |
| Freeze Protection Active | AHU | Low temperature alarm | Check heating coil and OA damper |
| Filter Alarm | AHU | Dirty air filter | Replace filter |
| Room Temp High/Low | Room unit | Room temperature fault | Check zone heating/cooling |
| Time Program Fault | PXC | Scheduling error | Check controller clock and program |
| Hardware Fault | PXC | Controller hardware error | Replace controller module |
| BACnet Comm Fault | MS/TP | Field bus communication error | Check MS/TP wiring and address |

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
| PXC compact controller module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-desigo-fault-codes&k=PXC+compact+controller+module&tag=errorcodefixes-20) \| Replace on hardware fault |
| Room unit (QMX3.P) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-desigo-fault-codes&k=Room+unit+%28QMX3.P%29&tag=errorcodefixes-20) \| Replace on room unit fault |
| Actuator (SQS/SKS) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-desigo-fault-codes&k=Actuator+%28SQS%2FSKS%29&tag=errorcodefixes-20) \| Replace on valve fault |
| MS/TP cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-desigo-fault-codes&k=MS%2FTP+cable&tag=errorcodefixes-20) \| Replace on bus faults |
| Temperature sensor (QAP) | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-siemens-desigo-fault-codes&tag=errorcodefixes-20) \| Replace on sensor fault |
## When to Call a Pro
Desigo CC database configuration, PXC programming with XWORKSplus, and network integration require Siemens-trained personnel. Incorrect configuration changes can affect entire building zones simultaneously.

## Related Articles

- [Siemens Sinumerik 828D Alarm Codes Guide — Complete Diagnostic Reference](/posts/siemens-828d-alarm-codes/)
- [Siemens 840D Alarm 380000 — Causes & Fix](/posts/siemens-840d-alarm-380000/)
- [Siemens Circuit Breaker Fault Codes - Complete Guide](/posts/siemens-circuit-breaker-fault-codes/)
- [Siemens Cerberus/MXL Fire Alarm Fault Codes — Troubleshooting Guide](/posts/siemens-fire-alarm-fault-codes/)
- [Siemens G120C VFD Fault Code Guide — Complete Diagnostic Reference](/posts/siemens-g120c-fault-codes/)

## See Also

- [Siemens Sinumerik Alarm 380500 — Causes & Fix](/posts/siemens-sinumerik-alarm-380500/)
- [Siemens 840D Alarm 380000 — Causes & Fix](/posts/siemens-840d-alarm-380000/)
- [Siemens SINAMICS G120 F30002 Fault — DC Link Overvoltage Fix](/posts/siemens-sinamics-f30002-fault/)
- [Siemens Micromaster 440 Fault F002 — Overcurrent](/posts/siemens-micromaster-440-fault-f002/)
