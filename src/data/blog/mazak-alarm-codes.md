---
title: "Mazak CNC Alarm Codes — Common Faults and Fixes"
description: "Mazak CNC alarm codes: servo alarms (1–99), spindle alarms (100–299), servo axis faults (400–499), ATC faults (600+), and PC alarms (500+) with fixes."
pubDatetime: 2026-04-22T16:00:00Z
modDatetime: 2026-04-22T16:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - cnc
  - mazak
---

## Mazak CNC Alarm Codes — Quick Reference

Mazak CNC machines (Nexus, Variaxis, Integrex, DONE IN ONE series) with Mazatrol or EIA/ISO controls display alarm codes on the control screen. Alarm categories group faults by hundred: **1–99** (servo system), **50+** (basic servo), **100–299** (spindle), **400–499** (servo axis data), **500–599** (CNC/PC system), **600+** (ATC/pallet). Mazak's Smooth controls display plain-language alarm messages in addition to numbers.

| [Alarm](https://www.amazon.com/s?k=Alarm&tag=errorcodefixe-20) | Category | Meaning | [Common Fix](https://www.amazon.com/s?k=Common%20Fix&tag=errorcodefixe-20) |  |-------|---------|---------|-----------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 1 | Servo | [Servo alarm — axis](https://www.amazon.com/s?k=Servo%20alarm%20%E2%80%94%20axis&tag=errorcodefixe-20) | Check servo drive |
| [30](https://www.amazon.com/s?k=30&tag=errorcodefixe-20) | Servo | Axis position error | [Check ballscrew; servo tuning](https://www.amazon.com/s?k=Check%20ballscrew%3B%20servo%20tuning&tag=errorcodefixe-20) |  | 50 | [Servo](https://www.amazon.com/s?k=Servo&tag=errorcodefixe-20) | Basic servo fault | Check servo amp and motor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 100 | Spindle | [Spindle alarm](https://www.amazon.com/s?k=Spindle%20alarm&tag=errorcodefixe-20) | Check spindle drive display |
| [200](https://www.amazon.com/s?k=200&tag=errorcodefixe-20) | Spindle | Spindle speed error | [Check spindle encoder](https://www.amazon.com/s?k=Check%20spindle%20encoder&tag=errorcodefixe-20) |  | 400 | [Servo](https://www.amazon.com/s?k=Servo&tag=errorcodefixe-20) | Axis data alarm | Check axis servo parameter | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 500 | PC/CNC | [PC system alarm](https://www.amazon.com/s?k=PC%20system%20alarm&tag=errorcodefixe-20) | Check control computer |
| [600](https://www.amazon.com/s?k=600&tag=errorcodefixe-20) | ATC | Tool changer fault | [Check ATC mechanism](https://www.amazon.com/s?k=Check%20ATC%20mechanism&tag=errorcodefixe-20) | ## Most Common Codes

### Alarm 1 / Alarm 30: Servo Alarm / Position Error
These are the most common Mazak alarms in production environments. Alarm 1 comes from the servo drive itself reporting a hardware fault. Alarm 30 (Axis Position Error) means the axis commanded position and actual position diverged beyond the tolerance band.

**Alarm 30 causes:** (1) ballscrew backlash or slipping coupling, (2) way lubrication failure (check lube oil level and pump), (3) servo drive fault causing the axis to lose position, (4) sudden load increase from a crash or aggressive cut.

**Diagnosis:** Check the Mazak servo drive (mounted in the control cabinet) for its own fault LEDs. On Mitsubishi MDS servo drives (used in most Mazak machines), the drive shows a detailed sub-alarm number (e.g., "21" = position error too large, "E9" = encoder data error) that helps narrow the cause.

### Alarm 50: Basic Servo Fault
The servo system failed its self-check at power-up or during operation. Check: all servo amplifier connections are secure, the servo feedback cables are undamaged, and the motor brake (if present) releases properly on power-up.

### Alarm 100–200: Spindle Alarms
Spindle alarms on Mazak machines originate in the spindle drive (also usually a Mitsubishi or Fanuc drive). Navigate to the Mazak alarm detail screen to see if a sub-alarm number is displayed. Common spindle alarms: overcurrent (spindle tool engagement too aggressive), encoder fault (spindle position encoder or speed feedback), and inverter overtemperature (spindle drive cabinet airflow blocked).

**Spindle encoder issues** are particularly common on Mazak Nexus machines after 10+ years — the spindle encoder cable develops micro-fractures from rotation and vibration. Replacing the encoder cable (routed through the spindle motor) resolves intermittent alarm 200 faults.

### Alarm 500: PC System Alarm
The control PC (running Mazatrol software) has a software or hardware fault. This often appears after a power surge or an unclean shutdown. Restart the control using the proper power-down sequence. If alarm 500 recurs, check the PC hardware (RAM, SSD/HDD, battery) in the control cabinet. Mazatrol Smooth systems run on Windows-based PCs and can suffer from disk errors after unexpected shutdowns.

### Alarm 600: ATC (Automatic Tool Changer) Fault
The tool changer failed mid-cycle. Check: (1) the ATC arm sensors (proximity switches) for correct positions, (2) hydraulic or pneumatic pressure to the ATC, (3) that the tool pot that was commanded is accessible (not obstructed), (4) that the previous tool change completed fully — a tool left in the arm causes 600 faults on the next cycle. Use the Mazak ATC manual mode to diagnose and recover the arm.

## Recovering from Servo Alarm 30 After a Crash

1. Stop all axis motion.
2. Navigate to Mazak Servo Monitor screen and note the position error for each axis.
3. If the machine was in a crash, carefully inspect all axes for mechanical damage before re-homing.
4. Use MDI jog mode to move axes to a safe position.
5. Re-home the machine (reference return) before running programs.

## Parts Often Needed | Part | [Notes](https://www.amazon.com/s?k=Notes&tag=errorcodefixe-20) |  |------|-------|
| Servo encoder cable | [Route-specific; measure length before ordering](https://www.amazon.com/s?k=Route-specific%3B%20measure%20length%20before%20ordering&tag=errorcodefixe-20) |  | Lube oil pump | [Bijur or Farval pump, machine-specific](https://www.amazon.com/s?k=Bijur%20or%20Farval%20pump%2C%20machine-specific&tag=errorcodefixe-20) |  | ATC proximity switch | [PNP or NPN — check existing wiring](https://www.amazon.com/s?k=PNP%20or%20NPN%20%E2%80%94%20check%20existing%20wiring&tag=errorcodefixe-20) |  | Servo drive | Mitsubishi MDS-B or MDS-C series, machine-specific |

## When to Call a Pro
Alarm 500 that persists after restart (Mazatrol PC failure) and ATC mechanical crashes that leave tools stuck in the arm require Mazak factory service or a Mazak-authorized technician. Running a machine with an unresolved servo position error risks further mechanical damage.
