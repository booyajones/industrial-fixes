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

| [Fault](https://www.amazon.com/s?k=Fault&tag=errorcodefixe-20) | Meaning | Quick Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------- |---------|-----------|
| Safety Circuit Open | [Door, safety shoe, or limit switch open](https://www.amazon.com/s?k=Door%2C%20safety%20shoe%2C%20or%20limit%20switch%20open&tag=errorcodefixe-20) | Check door contacts and safety chain |
| [Door Fault](https://www.amazon.com/s?k=Door%20Fault&tag=errorcodefixe-20) | Door not closing or opening within time | Check door motor and operator | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Overspeed | Car exceeded rated speed | [Check governor and brake](https://www.amazon.com/s?k=Check%20governor%20and%20brake&tag=errorcodefixe-20) |  | Drive Fault | [VFD or drive system fault](https://www.amazon.com/s?k=VFD%20or%20drive%20system%20fault&tag=errorcodefixe-20) | Check drive fault code |
| [Motor Overtemperature](https://www.amazon.com/s?k=Motor%20Overtemperature&tag=errorcodefixe-20) | Motor thermal protection tripped | Allow motor to cool, check brake drag | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Encoder Fault | Speed feedback error | [Check encoder wiring](https://www.amazon.com/s?k=Check%20encoder%20wiring&tag=errorcodefixe-20) |  | Leveling Fault | [Car not leveling at floor](https://www.amazon.com/s?k=Car%20not%20leveling%20at%20floor&tag=errorcodefixe-20) | Check floor sensors and brake |
| [Buffer Contact](https://www.amazon.com/s?k=Buffer%20Contact&tag=errorcodefixe-20) | Pit buffer switch triggered | Inspect pit and buffer | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Governor Switch | Centrifugal governor tripped | [Reset governor, check speed](https://www.amazon.com/s?k=Reset%20governor%2C%20check%20speed&tag=errorcodefixe-20) |  | Emergency Stop | [Emergency stop button pressed](https://www.amazon.com/s?k=Emergency%20stop%20button%20pressed&tag=errorcodefixe-20) | Reset E-stop, check circuit |

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
| [Door contact (mechanical)](https://www.amazon.com/s?k=Door%20contact%20(mechanical)&tag=errorcodefixe-20) | Replace when worn |
| [Door operator belt/coupling](https://www.amazon.com/s?k=Door%20operator%20belt%2Fcoupling&tag=errorcodefixe-20) | Replace on door fault |
| [Encoder](https://www.amazon.com/s?k=Encoder&tag=errorcodefixe-20) | Replace on feedback fault |
| [Brake coil](https://www.amazon.com/s?k=Brake%20coil&tag=errorcodefixe-20) | Replace on drag or release fault |
| [Drive module](https://www.amazon.com/s?k=Drive%20module&tag=errorcodefixe-20) | Replace on repeated drive faults |

## When to Call a Pro
**Elevator maintenance and repair must be performed by licensed elevator mechanics (NAEC or equivalent certification).** Bypassing safety circuits or working in elevator pits and on top of cars without proper training is extremely dangerous.

