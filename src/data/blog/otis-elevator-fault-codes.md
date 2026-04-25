---
title: "Otis Elevator Fault Codes - Complete Guide (Gen2 / Elevonic)"
description: "Otis elevator fault codes for Gen2, Elevonic 411, and Otis 2000 systems: common alarms, causes, and diagnostic steps."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - otis
  - elevator
  - lift
---

## Otis Elevator Fault Codes - Quick Reference

Otis elevators (Gen2, Elevonic 411, Otis 2000, GeN2 Comfort, and LiNX controller systems) log faults accessible via the Otis service tool (OSCAR or LiNX service tool) or the controller's onboard diagnostic display.

| Fault | System | Meaning | Quick Fix |
|-------|--------|---------|-----------|
| Safety Chain Open | All | Safety circuit interrupted | Check door contacts and limit switches |
| Door Fault (DF) | All | Door open/close failure | Check door operator and contacts |
| Drive Fault | Gen2/LiNX | VFD or drive error | Read drive fault code |
| Overspeed | All | Governor tripped | Reset governor, check speed |
| Motor Encoder Fault | Gen2 | Encoder feedback error | Check encoder cable |
| Brake Fault | Gen2 | Brake not releasing or engaging | Check brake coil and contacts |
| Pit Stop Active | All | Pit emergency stop pressed | Reset pit stop, inspect pit |
| Terminal Limit | All | Car at extreme travel limit | Check limit switches |
| Communication Fault | LiNX | Controller communication error | Check CAN bus wiring |
| Rescue Mode | Gen2 | Emergency rescue triggered | Return to manual control |

## Most Common Faults

### Safety Chain Open (Gen2)
The Gen2 uses a monitored safety chain. The LiNX controller reads individual safety inputs via a serial safety link - unlike older relay systems, individual contacts can be identified directly on the LiNX display. Check door contacts first (UCM - unintended car movement), then gate switches and pit stop.

### Door Fault
Otis Gen2 uses a Hollister-Whitney or Wittur door operator. Door faults include: door reversal from the light curtain, door motor overcurrent, and door open time exceeded. Check that the door sill is clear of debris and the door clutch/vane engages properly at each floor landing.

### Brake Fault
Gen2 gearless machines use electromagnetic disc brakes. A brake fault means the brake monitoring contacts don't confirm the expected state (open on run, closed on stop). Check the brake contactor and the brake monitoring switch. Brake drag (brake not fully releasing) causes motor overtemperature and drive overcurrent.

### Drive Fault
Gen2 uses Otis-proprietary regenerative drives in newer installations. A drive fault code is logged on the LiNX display. Common codes: OV (overvoltage), OC (overcurrent), and thermal. The regenerative drive returns braking energy to the building - if the building supply is at high voltage, OV faults occur on deceleration.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Door contacts (UCM rated) | [Amazon](https://www.amazon.com/s?k=Door+contacts+%28UCM+rated%29&tag=errorcodefixes-20) \| Replace when worn |
| Brake coil / armature | [Amazon](https://www.amazon.com/s?k=Brake+coil+%2F+armature&tag=errorcodefixes-20) \| Replace on brake fault |
| Motor encoder | [Amazon](https://www.amazon.com/s?k=Motor+encoder&tag=errorcodefixes-20) \| Replace on encoder fault |
| Drive module (Otis regen) | [Amazon](https://www.amazon.com/s?k=Drive+module+%28Otis+regen%29&tag=errorcodefixes-20) \| Replace on persistent drive fault |
| LiNX controller board | [Amazon](https://www.amazon.com/s?k=LiNX+controller+board&tag=errorcodefixes-20) \| Replace on controller fault |
## When to Call a Pro
**Otis elevator systems require licensed elevator mechanics.** The LiNX controller programming is locked and accessible only to Otis-authorized personnel. Do not attempt to clear faults in the pit without proper lockout/tagout procedures.

## Related Articles

- [KONE Elevator Fault Codes - Complete Guide](/posts/kone-elevator-fault-codes/)
- [Mitsubishi Elevator Fault Codes - Complete Guide](/posts/mitsubishi-elevator-fault-codes/)
- [Schindler Elevator Fault Codes - Complete Guide](/posts/schindler-elevator-fault-codes/)
- [ThyssenKrupp Elevator Fault Codes - Complete Guide](/posts/thyssenkrupp-elevator-fault-codes/)
