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

| [Fault](https://www.amazon.com/s?k=Fault&tag=errorcodefixe-20) | System | Meaning | [Quick Fix](https://www.amazon.com/s?k=Quick%20Fix&tag=errorcodefixe-20) |  |-------|--------|---------|-----------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Safety Chain Open | All | [Safety circuit interrupted](https://www.amazon.com/s?k=Safety%20circuit%20interrupted&tag=errorcodefixe-20) | Check door contacts and limit switches |
| [Door Fault (DF)](https://www.amazon.com/s?k=Door%20Fault%20(DF)&tag=errorcodefixe-20) | All | Door open/close failure | [Check door operator and contacts](https://www.amazon.com/s?k=Check%20door%20operator%20and%20contacts&tag=errorcodefixe-20) |  | Drive Fault | [Gen2/LiNX](https://www.amazon.com/s?k=Gen2%2FLiNX&tag=errorcodefixe-20) | VFD or drive error | Read drive fault code | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Overspeed | All | [Governor tripped](https://www.amazon.com/s?k=Governor%20tripped&tag=errorcodefixe-20) | Reset governor, check speed |
| [Motor Encoder Fault](https://www.amazon.com/s?k=Motor%20Encoder%20Fault&tag=errorcodefixe-20) | Gen2 | Encoder feedback error | [Check encoder cable](https://www.amazon.com/s?k=Check%20encoder%20cable&tag=errorcodefixe-20) |  | Brake Fault | [Gen2](https://www.amazon.com/s?k=Gen2&tag=errorcodefixe-20) | Brake not releasing or engaging | Check brake coil and contacts | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Pit Stop Active | All | [Pit emergency stop pressed](https://www.amazon.com/s?k=Pit%20emergency%20stop%20pressed&tag=errorcodefixe-20) | Reset pit stop, inspect pit |
| [Terminal Limit](https://www.amazon.com/s?k=Terminal%20Limit&tag=errorcodefixe-20) | All | Car at extreme travel limit | [Check limit switches](https://www.amazon.com/s?k=Check%20limit%20switches&tag=errorcodefixe-20) |  | Communication Fault | [LiNX](https://www.amazon.com/s?k=LiNX&tag=errorcodefixe-20) | Controller communication error | Check CAN bus wiring | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Rescue Mode | Gen2 | [Emergency rescue triggered](https://www.amazon.com/s?k=Emergency%20rescue%20triggered&tag=errorcodefixe-20) | Return to manual control |

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
| [Door contacts (UCM rated)](https://www.amazon.com/s?k=Door%20contacts%20(UCM%20rated)&tag=errorcodefixe-20) | Replace when worn |
| [Brake coil / armature](https://www.amazon.com/s?k=Brake%20coil%20%2F%20armature&tag=errorcodefixe-20) | Replace on brake fault |
| [Motor encoder](https://www.amazon.com/s?k=Motor%20encoder&tag=errorcodefixe-20) | Replace on encoder fault |
| [Drive module (Otis regen)](https://www.amazon.com/s?k=Drive%20module%20(Otis%20regen)&tag=errorcodefixe-20) | Replace on persistent drive fault |
| [LiNX controller board](https://www.amazon.com/s?k=LiNX%20controller%20board&tag=errorcodefixe-20) | Replace on controller fault |

## When to Call a Pro
**Otis elevator systems require licensed elevator mechanics.** The LiNX controller programming is locked and accessible only to Otis-authorized personnel. Do not attempt to clear faults in the pit without proper lockout/tagout procedures.

