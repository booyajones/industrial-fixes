---
title: "Haas CNC Alarm Codes — Complete Guide (100-Series and Up)"
description: "Haas CNC alarm codes: all major alarm numbers including 100-series emergency stops, spindle alarms, servo faults, and ATC faults with fixes."
pubDatetime: 2026-04-22T16:00:00Z
modDatetime: 2026-04-22T16:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - haas
---

## Haas CNC Alarm Codes — Quick Reference

Haas CNC machines (VF series, ST lathes, HS high-speed, EC palletizers) display alarm numbers on the control screen. Alarms in the **100s** are generally E-stop/safety alarms; **110–120s** are axis and servo faults; **120–134** are spindle and coolant faults. Higher-number alarms cover ATC, pallet changer, and soft-limit conditions.

| Alarm | Meaning | Common Fix |
|-------|---------|-----------|
| 101 | E-stop pressed | Release E-stop; check wiring |
| 102 | Power supply fault | Check control cabinet power supply |
| 103 | Door interlock active | Close machine door(s) |
| 104 | Feed hold active | Clear feed hold; check wiring |
| 105 | Low lube oil | Add way lube oil; check pump |
| 106 | Low air pressure | Check shop air supply; regulator |
| 107 | High coolant temperature | Check coolant level and cooler |
| 108 | Axis servo fault | Check servo drive and motor |
| 110 | Spindle servo fault | Check spindle drive |
| 111 | X-axis fault | Check X servo and encoder |
| 112 | Y-axis fault | Check Y servo and encoder |
| 113 | Z-axis fault | Check Z servo and encoder |
| 114 | A-axis fault | Check A-axis servo |
| 115 | Spindle overload | Reduce depth of cut; check tool |
| 116 | Spindle encoder fault | Check encoder cable and disc |
| 117 | Spindle motor thermal fault | Check spindle motor temperature |
| 118 | Coolant motor fault | Check coolant pump |
| 119 | Spindle orientation fault | Check spindle encoder; orient dog |
| 120 | ATC fault | Check ATC mechanism |
| 125 | Carousel fault | Check carousel rotation and sensors |
| 134 | Spindle drive alarm | Spindle drive internal fault |

## Most Common Codes

### Alarm 101: E-Stop Pressed
The E-stop circuit is open. Check: (1) the red E-stop button on the control panel — is it pulled out? (2) all E-stop buttons around the machine (some have external buttons on doors or pedestals), (3) the E-stop chain in the control cabinet — a broken wire or relay in the E-stop safety circuit causes 101 without any button being pressed. On Haas machines with safety mats, also check the mat connectors.

### Alarm 105: Low Lube Oil
The way lube reservoir is low or the lube pump failed. Fill the reservoir with approved way lube oil (Mobil Vactra No. 2 or equivalent ISO 68 way oil). If the reservoir is full and alarm still appears, check the lube pump output — remove the outlet line and verify oil flows on command (lube is commanded at machine startup). A clogged lube distributor block is common on older machines.

### Alarm 106: Low Air Pressure
Shop air is below the minimum required (typically 85 PSI). Check the pneumatic supply regulator on the back of the machine — it should show 85–100 PSI. Also check for large air leaks from the pneumatic cylinder (drawbar release) or coolant mist manifolds. Air pressure alarms during active machining can indicate the shop compressor is undersized.

### Alarm 115: Spindle Overload
The spindle drive exceeded its current limit, usually from aggressive cutting parameters. Reduce the depth of cut, feed rate, or spindle speed. Also check: tool condition (dull tool = high force), tool stickout length (excessive reach causes chatter and load spikes), and workholding security.

### Alarm 120: ATC (Automatic Tool Changer) Fault
The tool changer failed to complete a cycle. Check: (1) hydraulic pressure on machines with hydraulic ATC — minimum 1000 PSI, (2) pocket sensor on side-mount tool changers — verify the arm is at the home position, (3) tool retention — a tool that won't release from the spindle causes ATC arm jams. On VF models with umbrella ATC, check that the carousel rotated to the correct pocket.

### Alarm 125: Carousel Fault
The tool carousel failed to index to the commanded tool pocket. Check the carousel motor, the proximity switches that detect carousel position, and verify no tools are physically obstructing carousel rotation (an oversized tool in an adjacent pocket can cause this).

### Alarm 116: Spindle Encoder Fault
The spindle encoder is not providing a clean signal. Check the encoder cable connection at the encoder and at the spindle drive. On older Haas machines, the encoder coupling (a flexible plastic disc) wears and creates intermittent signals — visible as a cracked or missing coupling when inspecting the back of the spindle motor.

## Resetting Alarms

1. Fix the root cause of the alarm.
2. Press RESET on the Haas control.
3. Press POWER UP if the machine was in an E-stop condition.
4. For servo alarms after unexpected movement, verify axis positions are correct before running a program.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Way lube oil | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-codes&k=Way+lube+oil&tag=errorcodefixes-20) \| Mobil Vactra No. 2 (ISO 68) — 1 gallon |
| Spindle encoder coupling | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-codes&k=Spindle+encoder+coupling&tag=errorcodefixes-20) \| Haas P/N for flexible disc coupling |
| ATC arm sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-codes&k=ATC+arm+sensor&tag=errorcodefixes-20) \| Proximity switch for arm home position |
| E-stop relay | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-codes&k=E-stop+relay&tag=errorcodefixes-20) \| Safety relay in control cabinet |
## When to Call a Pro
Alarms 108, 111–114 (servo faults on any axis) that persist after a power cycle indicate servo drive or motor issues that require Haas factory service or a Haas certified technician to diagnose. Haas provides phone support 24/7 for production-down situations.

## Related Articles

- [Haas CNC Alarm 101 — Emergency Stop Active Fix](/posts/haas-alarm-101-emergency-stop/)
- [Haas Alarm 102 — Servo Drive Fault Fix](/posts/haas-alarm-102/)
- [Haas Alarm 103 — Servo Overload Fix](/posts/haas-alarm-103/)
- [Haas Alarm 104 Feed Hold — Causes & Fix](/posts/haas-alarm-104-feed-hold/)
- [Haas Alarm 105 E-Stop — Causes & Fix](/posts/haas-alarm-105/)
