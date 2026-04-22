---
title: "Schindler Elevator Fault Codes - Complete Guide"
description: "Schindler 3100, 3300, 5300, and MRL elevator fault codes: common alarms, causes, and diagnostic steps for technicians."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - schindler
  - elevator
  - lift
---

## Schindler Elevator Fault Codes - Quick Reference

Schindler elevators (3100, 3300, 5300, 7000, and PORT technology) use the Schindler Miconic 10 and IC3/IC5 controller platforms. Faults are logged and accessible via the Schindler Diagnose Tool or keypad.

| [Fault](https://www.amazon.com/s?k=Fault&tag=errorcodefixe-20) | System | Meaning | [Quick Fix](https://www.amazon.com/s?k=Quick%20Fix&tag=errorcodefixe-20) |  |-------|--------|---------|-----------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Safety Circuit Open | All | [Safety chain interrupted](https://www.amazon.com/s?k=Safety%20chain%20interrupted&tag=errorcodefixe-20) | Check door contacts and limits |
| [Door Fault](https://www.amazon.com/s?k=Door%20Fault&tag=errorcodefixe-20) | All | Door open/close failure | [Check door operator and contacts](https://www.amazon.com/s?k=Check%20door%20operator%20and%20contacts&tag=errorcodefixe-20) |  | Drive Fault | [3300/5300](https://www.amazon.com/s?k=3300%2F5300&tag=errorcodefixe-20) | VFD or drive error | Read drive fault code | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Brake Fault | All | [Brake monitoring fault](https://www.amazon.com/s?k=Brake%20monitoring%20fault&tag=errorcodefixe-20) | Check brake coil |
| [Overload](https://www.amazon.com/s?k=Overload&tag=errorcodefixe-20) | All | Overload detected | [Check load weighing device](https://www.amazon.com/s?k=Check%20load%20weighing%20device&tag=errorcodefixe-20) |  | Encoder Fault | [All](https://www.amazon.com/s?k=All&tag=errorcodefixe-20) | Encoder feedback error | Check encoder | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Terminal Limit | All | [Car at travel limit](https://www.amazon.com/s?k=Car%20at%20travel%20limit&tag=errorcodefixe-20) | Check limit switches |
| [Communication Fault](https://www.amazon.com/s?k=Communication%20Fault&tag=errorcodefixe-20) | IC5 | Controller network fault | [Check CAN bus wiring](https://www.amazon.com/s?k=Check%20CAN%20bus%20wiring&tag=errorcodefixe-20) |  | PIT Emergency Stop | [All](https://www.amazon.com/s?k=All&tag=errorcodefixe-20) | Pit stop button pressed | Reset, inspect pit | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | UCM Detected | 3300+ | [Unintended car movement](https://www.amazon.com/s?k=Unintended%20car%20movement&tag=errorcodefixe-20) | Safety-critical: call technician |

## Most Common Faults

### Safety Circuit Open
Schindler IC3/IC5 controllers provide detailed safety input monitoring. The keypad displays which safety device opened the circuit. Door contacts are responsible for most safety circuit faults. Schindler door contacts (particularly on the 3300 series) wear at the contact surface and require periodic inspection.

### Door Fault
Schindler uses Sematic and proprietary door operators. Common door fault causes: worn door clutch, failed door drive, or blocked door track. On 3300 series, the door operator has an integral frequency drive - check the operator LED fault indicator and refer to the door operator fault table in the service manual.

### Drive Fault
Schindler 3300 and 5300 use VACON or Schindler-proprietary drives. Access the drive fault history directly at the drive keypad or via the Schindler Diagnose Tool. Common faults: overvoltage (deceleration), overcurrent (motor or brake drag), and communication errors.

### Unintended Car Movement (UCM)
Like all modern elevator systems, Schindler implements UCM protection per EN 81-20. A UCM fault is a safety-critical event requiring a complete investigation. Causes include brake failure, drive control failure, or safety circuit bypass. Do not reset and return to service without thorough inspection.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Door contact (Schindler spec)](https://www.amazon.com/s?k=Door%20contact%20(Schindler%20spec)&tag=errorcodefixe-20) | Replace when worn |
| [Door operator drive](https://www.amazon.com/s?k=Door%20operator%20drive&tag=errorcodefixe-20) | Replace on door fault |
| [Brake coil assembly](https://www.amazon.com/s?k=Brake%20coil%20assembly&tag=errorcodefixe-20) | Replace on brake fault |
| [Encoder](https://www.amazon.com/s?k=Encoder&tag=errorcodefixe-20) | Replace on feedback fault |
| [IC3/IC5 control board](https://www.amazon.com/s?k=IC3%2FIC5%20control%20board&tag=errorcodefixe-20) | Replace on controller fault |

## When to Call a Pro
**Schindler elevator systems are proprietary.** The Schindler Diagnose Tool and software are only available to Schindler-authorized personnel. All elevator maintenance must be performed by licensed elevator mechanics.

