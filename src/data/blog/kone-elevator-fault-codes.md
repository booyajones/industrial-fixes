---
title: "KONE Elevator Fault Codes - Complete Guide"
description: "KONE elevator fault codes for MonoSpace, EcoDisc, and MiniSpace systems: common alarms, causes, and diagnostic steps."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - kone
  - elevator
  - lift
---

## KONE Elevator Fault Codes - Quick Reference

KONE elevators (MonoSpace, EcoDisc, MiniSpace, NanoSpace, and TravelMaster hydraulics) use the V3F16L and KONE CX/DX controller platforms. Faults are logged in the controller and accessible via KONE TKS or KONE Care service tools.

| [Fault](https://www.amazon.com/s?k=Fault&tag=errorcodefixe-20) | System | Meaning | [Quick Fix](https://www.amazon.com/s?k=Quick%20Fix&tag=errorcodefixe-20) |  |-------|--------|---------|-----------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Safety Circuit Fault | All | [Safety chain open](https://www.amazon.com/s?k=Safety%20chain%20open&tag=errorcodefixe-20) | Check door contacts and limit switches |
| [Door Fault](https://www.amazon.com/s?k=Door%20Fault&tag=errorcodefixe-20) | All | Door not closing or opening | [Check door operator and contacts](https://www.amazon.com/s?k=Check%20door%20operator%20and%20contacts&tag=errorcodefixe-20) |  | Drive Fault | [MonoSpace/EcoDisc](https://www.amazon.com/s?k=MonoSpace%2FEcoDisc&tag=errorcodefixe-20) | V3F drive alarm | Read drive keypad fault code | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Brake Fault | EcoDisc | [Brake monitoring fault](https://www.amazon.com/s?k=Brake%20monitoring%20fault&tag=errorcodefixe-20) | Check brake coil and contacts |
| [Encoder Fault](https://www.amazon.com/s?k=Encoder%20Fault&tag=errorcodefixe-20) | EcoDisc | Speed feedback error | [Check encoder and cable](https://www.amazon.com/s?k=Check%20encoder%20and%20cable&tag=errorcodefixe-20) |  | Rope Slip | [All](https://www.amazon.com/s?k=All&tag=errorcodefixe-20) | Governor rope slip detected | Check governor and rope tension | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Overload | All | [Car overloaded](https://www.amazon.com/s?k=Car%20overloaded&tag=errorcodefixe-20) | Check weighing device |
| [Buffer Switch](https://www.amazon.com/s?k=Buffer%20Switch&tag=errorcodefixe-20) | All | Pit buffer contact tripped | [Inspect pit](https://www.amazon.com/s?k=Inspect%20pit&tag=errorcodefixe-20) |  | Car Roof Emergency Stop | [All](https://www.amazon.com/s?k=All&tag=errorcodefixe-20) | Top of car E-stop pressed | Reset, inspect car top | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Unintended Car Movement | MonoSpace | [UCM detection triggered](https://www.amazon.com/s?k=UCM%20detection%20triggered&tag=errorcodefixe-20) | Check safety chain and drive |

## Most Common Faults

### Safety Circuit Fault
KONE MonoSpace and EcoDisc use an electronic safety chain where individual safety inputs are monitored by the main control board. The fault log identifies which safety contact is open. Door zone contacts (UCM) and door contacts are the most frequent causes. Use the KONE TKS tool to read the exact safety input status.

### Door Fault
KONE uses proprietary KONE door operators (KSD, KSD-2). Door fault causes include: door motor overcurrent, door obstruction reversal, and door open timeout. Check that the sill grooves are clean and the door panels move freely. On KONE 3000 series, the door motor frequency drive is integral to the door operator and can fail independently.

### V3F Drive Fault
KONE V3F16L drives use VACON power electronics. Drive fault codes on the display follow the VACON F-fault format. Common codes: F3 (input phase loss), F7 (saturation), F9 (undervoltage). Check the drive keypad fault history directly. Many V3F faults are caused by the main power supply quality, not the drive itself.

### Unintended Car Movement (UCM)
UCM detection is a mandatory safety feature on modern KONE installations. If the car moves without door zone or door fully closed, UCM triggers and requires a technician reset. Root causes: failed brake, failed door zone sensor, or drive fault. This is a safety-critical fault - do not bypass.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [KONE door contact](https://www.amazon.com/s?k=KONE%20door%20contact&tag=errorcodefixe-20) | Replace when worn |
| [KONE KSD door operator](https://www.amazon.com/s?k=KONE%20KSD%20door%20operator&tag=errorcodefixe-20) | Replace on door fault |
| [EcoDisc brake coil](https://www.amazon.com/s?k=EcoDisc%20brake%20coil&tag=errorcodefixe-20) | Replace on brake fault |
| [V3F16L drive board](https://www.amazon.com/s?k=V3F16L%20drive%20board&tag=errorcodefixe-20) | Replace on persistent drive fault |
| [Encoder (EcoDisc motor)](https://www.amazon.com/s?k=Encoder%20(EcoDisc%20motor)&tag=errorcodefixe-20) | Replace on encoder fault |

## When to Call a Pro
**KONE elevator systems require licensed elevator mechanics.** KONE Care service tools and software are proprietary. Do not attempt repair or fault reset without proper training and authorization.

