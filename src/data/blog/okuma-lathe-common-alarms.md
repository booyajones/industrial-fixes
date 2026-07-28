---
title: "Okuma LB/LU Lathe Common Alarm Guide — OSP-P300 Series"
description: "Okuma LB and LU series CNC lathe common alarms for OSP-P300 and OSP-U100 controls: alarm descriptions, causes, and troubleshooting steps."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - okuma
  - cnc
  - lathe
  - osp
  - alarms
money_part: "Encoder battery (3.6V lithium)"
---

## Okuma LB/LU Lathe Common Alarm Guide

Okuma CNC lathes (LB, LU, LT, and Crown series) use the OSP-P300 (newer) or OSP-U100L (older) control. Alarms appear on the control display with a number and description.

## Alarm Number Ranges

| Range | Category |
|-------|----------|
| 1000–1099 | Servo system alarms |
| 1200–1299 | Spindle alarms |
| 1400–1499 | NC/system alarms |
| 1600–1799 | I/O and PLC alarms |
| 2000–2099 | Over-travel and limit alarms |
| 3000–3099 | Communication alarms |
| 4000–4099 | Tool post and turret alarms |

## Common Alarms Quick Reference

| Alarm | Meaning | Quick Fix |
|-------|---------|-----------|
| 1013 Servo Axis Fault | Servo drive fault — specified axis | Check drive and motor |
| 1050 ABS Data Error | Absolute encoder data lost | Replace encoder battery and re-home |
| 1201 Spindle Drive Error | Spindle amplifier fault | Note sub-code on drive |
| 1400 Memory Check Error | NC program memory error | Re-initialize or reload NC memory |
| 2000 Over Travel | Axis exceeded travel limit | Jog axis off limit, check soft limits |
| 4000 Turret Fault | Turret did not index correctly | Check hydraulic and position sensor |

## Most Common LB/LU Alarms

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

## Parts Often Needed

| Part | Notes |
|------|-------|
| Encoder battery (3.6V lithium) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-okuma-lathe-common-alarms&k=Encoder+battery+%283.6V+lithium%29&tag=errorcodefixes-20) \| Replace on ABS data errors |
| Servo amplifier module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-okuma-lathe-common-alarms&k=Servo+amplifier+module&tag=errorcodefixes-20) \| Replace on persistent 1013 faults |
| Turret hydraulic motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-okuma-lathe-common-alarms&k=Turret+hydraulic+motor&tag=errorcodefixes-20) \| Replace on turret fault if hydraulic |
| Spindle encoder | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-okuma-lathe-common-alarms&k=Spindle+encoder&tag=errorcodefixes-20) \| Replace on persistent 1201 faults |
## Jump to Fix

- **1013 servo fault** → Power cycle → Note sub-code → Inspect motor encoder
- **1050 ABS error** → Replace battery → Perform home return
- **2000 over-travel** → Jog off limit → Check soft limit parameters

## When to Call a Pro
Okuma provides technical support via their national service network. Contact 1-800-642-7659. The THINC diagnostics system gives remote access for complex troubleshooting.
