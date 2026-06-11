---
title: "Fanuc CNC Alarm Codes — Complete Reference"
description: "Fanuc CNC alarm codes: servo alarms (400–499), overtravel (1–6), APC alarms (300–360), and program errors (PS alarms) with causes and fixes."
pubDatetime: 2026-04-22T16:00:00Z
modDatetime: 2026-04-22T16:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - fanuc
money_part: "Encoder battery"
---

## Fanuc CNC Alarm Codes — Quick Reference

Fanuc CNC controls (0i, 16i, 18i, 21i, 30i, 31i, 32i series) display alarm codes on the CNC operator panel with a prefix letter indicating the alarm type. **SV** = Servo alarm, **OT** = Overtravel, **APC** = Absolute position encoder alarm, **PS** = Program/parameter error, **SP** = Spindle alarm, **SYS** = System alarm.

| Code | Type | Meaning | Common Fix |
|------|------|---------|-----------|
| 1–6 | OT | Overtravel (+ or −) each axis | Release axis from hardware limit |
| 90 | — | Axis servo alarm | Check servo drive and motor |
| 300 | APC | Reference return required | Perform reference return |
| 360 | APC | Battery for absolute encoder low | Replace encoder battery |
| 400 | SV | Servo alarm — axis n | Check amplifier and motor |
| 401 | SV | Servo ready signal off | Check servo power supply |
| 411 | SV | Axis n: error too large | Servo tuning or mechanical issue |
| 414 | SV | FSSB communication fault | Check FSSB cable |
| 424 | SV | Servo motor overheat | Check motor cooling |
| 435 | SV | Axis n: overspeed | Check feedback device |
| 436 | SV | Axis n: current position error | Check scale or encoder |
| 437 | SV | Axis n: position gain error | Check servo parameters |
| 700 | SP | Spindle alarm | Check spindle drive |
| 750 | SP | Spindle feedback fault | Check spindle encoder |

## Most Common Codes

### Alarm 1–6: Overtravel
A machine axis traveled beyond its hardware limit switch. The axis is physically held at the limit. To release: (1) enter the Fanuc manual override mode (hold the OT release function key + jog in the opposite direction from the limit), (2) jog the axis back within the machine travel range. On most Fanuc 0i-F controls, hold the soft key labeled "OT Release" then jog the axis in the opposite direction.

**Do not enter programs that might re-trip the overtravel until you find why the axis went to the limit** — common causes: incorrect work offset, wrong G54/G55 selection, or a program error driving past the part boundary.

### Alarm 300: Reference Return Required
The machine lost its absolute position reference, typically after a power outage or after the control was powered with servo amplifier power off. Perform a reference return (HOME) on all axes in the correct sequence (usually Z first, then X and Y). On machines with FSSB serial encoders, this is often triggered by an encoder battery failing.

### Alarm 360: Encoder Battery Low
The battery that maintains position for the absolute encoder is low. Replace the encoder battery before the next power-off sequence — if the battery dies while the machine is powered off, absolute position is lost and a machine reference return (re-homing) will be required. Fanuc battery: A06B-6073-K001 (3V lithium, model-dependent).

### Alarm 400: Servo Alarm
The servo amplifier detected a fault on the specified axis. Press RESET and check: (1) the servo amplifier's own diagnostic LED or display for a more specific sub-code, (2) the motor and encoder cable connections, (3) motor overtemperature (hold motor housing — if hot, motor is overloaded or cooling fan has failed).

### Alarm 411: Excessive Error
The servo axis position error (difference between commanded and actual position) exceeded the parameter limit. This usually means: (1) the servo axis is losing steps mechanically (slipping coupling, worn ballscrew), (2) excessive load or friction, (3) servo gain is mistuned. Check the ballscrew preload and coupling between the motor and ballscrew.

### Alarm 414: FSSB Communication
The high-speed serial bus between the CNC control and servo amplifiers has dropped. Check the optical fiber or cable connecting the CNC card to the first servo amplifier in the chain. Also check all intermediate FSSB connections at each amplifier. A failed amplifier can break the chain for all downstream axes.

### Alarm 700: Spindle Alarm
The spindle drive reported a fault. Check the spindle drive's own fault display or LED — Fanuc spindle drives have their own detailed alarm codes beyond what the CNC shows. Common causes: spindle motor overtemperature, encoder fault, or overcurrent from a hard tool engagement.

## Clearing Alarms

Most Fanuc alarms clear with the RESET key on the MDI panel after the cause is fixed. OT alarms require the special OT Release procedure (hold release key while jogging). APC/encoder alarms may require a controlled machine reference return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Encoder battery | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-codes&k=Encoder+battery&tag=errorcodefixes-20) \| A06B-6073-K001 (3V, check model for compatible P/N) |
| FSSB fiber optic cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-codes&k=FSSB+fiber+optic+cable&tag=errorcodefixes-20) \| A66L-6001-0023 series |
| Servo amplifier | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-codes&k=Servo+amplifier&tag=errorcodefixes-20) \| A06B-6140 series (0i-D) or A06B-6141 series (0i-F) |
## When to Call a Pro
Alarm 414 (FSSB communication failure across multiple axes), SYS (system) alarms, and SP spindle alarms with no clear mechanical cause require a Fanuc-trained service engineer. Fanuc has 24-hour phone support for production-critical alarm conditions.

## Related Articles

- [Fanuc 0i-MD Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-0i-md-alarm-codes/)
- [Fanuc 30i/31i/32i Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-30i-alarm-codes/)
- [Fanuc Alarm 1 Overtravel — Causes & Fix](/posts/fanuc-alarm-1-overtravel/)
- [Fanuc Alarm 10 Servo Alarm — Causes & Fix](/posts/fanuc-alarm-10-servo-alarm/)
- [Fanuc Alarm 2 — Overtravel Plus Causes & Fix](/posts/fanuc-alarm-2-overtravel/)

## See Also

- [Fanuc Alarm 4 — Stored Stroke Limit Overtravel](/posts/fanuc-alarm-4-overtravel/)
- [Fanuc Alarm 460: Spindle Speed Error — Detailed Troubleshooting](/posts/fanuc-alarm-460-spindle/)
- [Fanuc Alarm 506 — Servo Following Error Fix](/posts/fanuc-alarm-506/)
- [Fanuc Alarm 700 — Causes & Fix](/posts/fanuc-alarm-700/)
