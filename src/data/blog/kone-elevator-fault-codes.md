---
title: "KONE Elevator Fault Codes — Complete Guide"
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

## KONE Elevator Fault Codes — Quick Reference

KONE elevators (MonoSpace, EcoDisc, MiniSpace, NanoSpace, and TravelMaster hydraulics) use the V3F16L and KONE CX/DX controller platforms. Faults are logged in the controller and accessible via KONE TKS or KONE Care service tools.

| Fault | System | Meaning | Quick Fix |
|-------|--------|---------|-----------|
| Safety Circuit Fault | All | Safety chain open | Check door contacts and limit switches |
| Door Fault | All | Door not closing or opening | Check door operator and contacts |
| Drive Fault | MonoSpace/EcoDisc | V3F drive alarm | Read drive keypad fault code |
| Brake Fault | EcoDisc | Brake monitoring fault | Check brake coil and contacts |
| Encoder Fault | EcoDisc | Speed feedback error | Check encoder and cable |
| Rope Slip | All | Governor rope slip detected | Check governor and rope tension |
| Overload | All | Car overloaded | Check weighing device |
| Buffer Switch | All | Pit buffer contact tripped | Inspect pit |
| Car Roof Emergency Stop | All | Top of car E-stop pressed | Reset, inspect car top |
| Unintended Car Movement | MonoSpace | UCM detection triggered | Check safety chain and drive |

## Most Common Faults

### Safety Circuit Fault
KONE MonoSpace and EcoDisc use an electronic safety chain where individual safety inputs are monitored by the main control board. The fault log identifies which safety contact is open. Door zone contacts (UCM) and door contacts are the most frequent causes. Use the KONE TKS tool to read the exact safety input status.

### Door Fault
KONE uses proprietary KONE door operators (KSD, KSD-2). Door fault causes include: door motor overcurrent, door obstruction reversal, and door open timeout. Check that the sill grooves are clean and the door panels move freely. On KONE 3000 series, the door motor frequency drive is integral to the door operator and can fail independently.

### V3F Drive Fault
KONE V3F16L drives use VACON power electronics. Drive fault codes on the display follow the VACON F-fault format. Common codes: F3 (input phase loss), F7 (saturation), F9 (undervoltage). Check the drive keypad fault history directly. Many V3F faults are caused by the main power supply quality, not the drive itself.

### Unintended Car Movement (UCM)
UCM detection is a mandatory safety feature on modern KONE installations. If the car moves without door zone or door fully closed, UCM triggers and requires a technician reset. Root causes: failed brake, failed door zone sensor, or drive fault. This is a safety-critical fault — do not bypass.

## Parts Often Needed

| Part | Notes |
|------|-------|
| KONE door contact | Replace when worn |
| KONE KSD door operator | Replace on door fault |
| EcoDisc brake coil | Replace on brake fault |
| V3F16L drive board | Replace on persistent drive fault |
| Encoder (EcoDisc motor) | Replace on encoder fault |

## When to Call a Pro
**KONE elevator systems require licensed elevator mechanics.** KONE Care service tools and software are proprietary. Do not attempt repair or fault reset without proper training and authorization.
