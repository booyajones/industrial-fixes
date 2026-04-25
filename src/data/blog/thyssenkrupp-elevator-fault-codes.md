---
title: "ThyssenKrupp Elevator Fault Codes - Complete Guide"
description: "ThyssenKrupp elevator fault codes for Evolution, Synergy, and MRL systems: common alarms, causes, and reset procedures."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - thyssenkrupp
  - elevator
  - lift
---

## ThyssenKrupp Elevator Fault Codes - Quick Reference

ThyssenKrupp elevators (Evolution, Synergy, MRL, Endura, and custom traction systems) use computerized controls that log fault codes accessible via the technician's service tool or keypad.

| Fault | Meaning | Quick Fix |
|-------|---------|-----------|
| Safety Circuit Open | Door, safety shoe, or limit switch open | Check door contacts and safety chain |
| Door Fault | Door not closing or opening within time | Check door motor and operator |
| Overspeed | Car exceeded rated speed | Check governor and brake |
| Drive Fault | VFD or drive system fault | Check drive fault code |
| Motor Overtemperature | Motor thermal protection tripped | Allow motor to cool, check brake drag |
| Encoder Fault | Speed feedback error | Check encoder wiring |
| Leveling Fault | Car not leveling at floor | Check floor sensors and brake |
| Buffer Contact | Pit buffer switch triggered | Inspect pit and buffer |
| Governor Switch | Centrifugal governor tripped | Reset governor, check speed |
| Emergency Stop | Emergency stop button pressed | Reset E-stop, check circuit |

## Most Common Faults

### Safety Circuit Open
The elevator safety circuit is a series chain of normally-closed contacts: door contacts, gate switches, terminal limit switches, governor switch, pit stop switch, and others. When any contact opens, the elevator stops immediately. Use the service tool to read which safety input is open. Check door contacts first - door-related faults account for approximately 80% of elevator service calls.

### Door Fault
A door that doesn't close within the preset time (typically 5–15 seconds) triggers a door fault. Check the door operator for mechanical obstructions, verify the door motor coupling, and check the door close limit switch. On ThyssenKrupp systems with TWIN door operators, also check the door reversing device (light curtain or safety edge).

### Drive Fault
ThyssenKrupp MRL and traction systems use variable frequency drives (typically KEB, Vacon, or proprietary drives). A drive fault from the elevator's main controller should be supplemented by reading the drive's own fault code directly at the drive keypad. Common drive faults: overvoltage on deceleration (check brake resistor), overcurrent (check motor and encoder), and communication fault (check CAN or serial link).

### Leveling Fault
If the elevator car doesn't reach exact floor level within tolerance, a leveling fault prevents door opening. Check the landing zone vanes and magnetic sensors at each floor. Bent vanes or shifted sensors cause false floor detection.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Door contact (mechanical) | [Amazon](https://www.amazon.com/s?k=Door+contact+%28mechanical%29&tag=errorcodefixes-20) \| Replace when worn |
| Door operator belt/coupling | [Amazon](https://www.amazon.com/s?k=Door+operator+belt%2Fcoupling&tag=errorcodefixes-20) \| Replace on door fault |
| Encoder | [Amazon](https://www.amazon.com/s?k=Encoder&tag=errorcodefixes-20) \| Replace on feedback fault |
| Brake coil | [Amazon](https://www.amazon.com/s?k=Brake+coil&tag=errorcodefixes-20) \| Replace on drag or release fault |
| Drive module | [Amazon](https://www.amazon.com/s?k=Drive+module&tag=errorcodefixes-20) \| Replace on repeated drive faults |
## When to Call a Pro
**Elevator maintenance and repair must be performed by licensed elevator mechanics (NAEC or equivalent certification).** Bypassing safety circuits or working in elevator pits and on top of cars without proper training is extremely dangerous.

## Related Articles

- [KONE Elevator Fault Codes - Complete Guide](/posts/kone-elevator-fault-codes/)
- [Mitsubishi Elevator Fault Codes - Complete Guide](/posts/mitsubishi-elevator-fault-codes/)
- [Otis Elevator Fault Codes - Complete Guide (Gen2 / Elevonic)](/posts/otis-elevator-fault-codes/)
- [Schindler Elevator Fault Codes - Complete Guide](/posts/schindler-elevator-fault-codes/)
