---
title: "Okuma LB/LU Lathe Common Alarm Guide — OSP-P300 Series"
description: "Okuma LB and LU series CNC lathe common alarms for OSP-P300 and OSP-U100 controls: alarm descriptions, causes, and troubleshooting steps."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - okuma
  - cnc
  - lathe
  - osp
  - alarms
---

## Okuma LB/LU Lathe Common Alarm Guide

Okuma CNC lathes (LB, LU, LT, and Crown series) use the OSP-P300 (newer) or OSP-U100L (older) control. Alarms appear on the control display with a number and description.

## Alarm Number Ranges

| [Range](https://www.amazon.com/s?k=Range&tag=errorcodefixe-20) | Category |
|-------|----------|
| [1000–1099](https://www.amazon.com/s?k=1000%E2%80%931099&tag=errorcodefixe-20) | Servo system alarms |
| [1200–1299](https://www.amazon.com/s?k=1200%E2%80%931299&tag=errorcodefixe-20) | Spindle alarms |
| [1400–1499](https://www.amazon.com/s?k=1400%E2%80%931499&tag=errorcodefixe-20) | NC/system alarms |
| [1600–1799](https://www.amazon.com/s?k=1600%E2%80%931799&tag=errorcodefixe-20) | I/O and PLC alarms |
| [2000–2099](https://www.amazon.com/s?k=2000%E2%80%932099&tag=errorcodefixe-20) | Over-travel and limit alarms |
| [3000–3099](https://www.amazon.com/s?k=3000%E2%80%933099&tag=errorcodefixe-20) | Communication alarms |
| [4000–4099](https://www.amazon.com/s?k=4000%E2%80%934099&tag=errorcodefixe-20) | Tool post and turret alarms |

## Common Alarms Quick Reference

| [Alarm](https://www.amazon.com/s?k=Alarm&tag=errorcodefixe-20) | Meaning | Quick Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------- |---------|-----------|
| 1013 Servo Axis Fault | [Servo drive fault — specified axis](https://www.amazon.com/s?k=Servo%20drive%20fault%20%E2%80%94%20specified%20axis&tag=errorcodefixe-20) | Check drive and motor |
| [1050 ABS Data Error](https://www.amazon.com/s?k=1050%20ABS%20Data%20Error&tag=errorcodefixe-20) | Absolute encoder data lost | Replace encoder battery and re-home | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 1201 Spindle Drive Error | Spindle amplifier fault | [Note sub-code on drive](https://www.amazon.com/s?k=Note%20sub-code%20on%20drive&tag=errorcodefixe-20) |  | 1400 Memory Check Error | [NC program memory error](https://www.amazon.com/s?k=NC%20program%20memory%20error&tag=errorcodefixe-20) | Re-initialize or reload NC memory |
| [2000 Over Travel](https://www.amazon.com/s?k=2000%20Over%20Travel&tag=errorcodefixe-20) | Axis exceeded travel limit | Jog axis off limit, check soft limits | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 4000 Turret Fault | Turret did not index correctly | [Check hydraulic and position sensor](https://www.amazon.com/s?k=Check%20hydraulic%20and%20position%20sensor&tag=errorcodefixe-20) | ## Most Common LB/LU Alarms

### Alarm 1013 — Servo Axis Fault
The servo drive (OSP-P300 uses Okuma-specific drives) has detected a fault on the named axis. Read the drive sub-code on the amplifier display. Common causes: motor overload, encoder fault, regeneration fault, or power supply issue.

Steps:
1. Power down and back up
2. If alarm recurs, note the amplifier sub-code
3. Inspect motor encoder connector
4. Check drive for status LEDs

### Alarm 1050 — ABS Data Error
The absolute encoder battery is dead or low, and position data has been lost. Replace the encoder battery (typically 3.6V lithium on the servo amplifier or in the control cabinet). After replacement, perform the home position return per the Okuma procedure.

### Alarm 1201 — Spindle Drive Error
The spindle drive is in fault condition. Check the spindle drive (PSM/SVM) display for the sub-code. Common causes: spindle motor thermal trip, encoder issue, or heavy cutting load.

### Alarm 2000 — Over-Travel
The axis hit a travel limit (hard or soft). To recover:
1. Press ALARM RESET
2. Jog the axis back into the valid travel range using axis jog keys
3. Confirm soft limit parameters are correct

## OSP-P300 Specific Features

The OSP-P300 control includes:
- THINC (The Intelligent NC) — machine health monitoring
- Thermal deviation compensation — reduces thermal errors
- Collision avoidance system — virtual model of machine envelope

When THINC detects anomalies (vibration, thermal), it can trigger preventive alarms before hard failures occur.

## Parts Often Needed | Part | [Notes](https://www.amazon.com/s?k=Notes&tag=errorcodefixe-20) |  |------|-------|
| Encoder battery (3.6V lithium) | [Replace on ABS data errors](https://www.amazon.com/s?k=Replace%20on%20ABS%20data%20errors&tag=errorcodefixe-20) |  | Servo amplifier module | [Replace on persistent 1013 faults](https://www.amazon.com/s?k=Replace%20on%20persistent%201013%20faults&tag=errorcodefixe-20) |  | Turret hydraulic motor | [Replace on turret fault if hydraulic](https://www.amazon.com/s?k=Replace%20on%20turret%20fault%20if%20hydraulic&tag=errorcodefixe-20) |  | Spindle encoder | Replace on persistent 1201 faults |

## Jump to Fix

- **1013 servo fault** → Power cycle → Note sub-code → Inspect motor encoder
- **1050 ABS error** → Replace battery → Perform home return
- **2000 over-travel** → Jog off limit → Check soft limit parameters

## When to Call a Pro
Okuma provides technical support via their national service network. Contact 1-800-642-7659. The THINC diagnostics system gives remote access for complex troubleshooting.
