---
title: "Fanuc Alarm 506 — Servo Following Error Fix"
author: "Dana Kowalski"
pubDatetime: 2026-04-26T18:15:00Z
modDatetime: 2026-04-26T18:15:00Z
slug: fanuc-alarm-506
featured: false
draft: false
tags:
  - fanuc
  - cnc
  - servo
  - alarm-codes
description: "Fanuc Alarm 506 is a servo following error on CNC machining centers and lathes. Learn what causes it and how to diagnose servo drives, encoders, and mechanical issues."
---

## Fanuc Alarm 506 — Servo Following Error

**Fanuc Alarm 506** appears on Fanuc 0i, 16i, 18i, 21i, 30i, and 31i CNC controls and indicates a **servo following error** — the difference between the commanded axis position and the actual (feedback) position has exceeded the allowable tolerance. When the control detects that an axis cannot keep up with the commanded trajectory, it stops motion and faults to prevent machining errors or mechanical damage.

The alarm typically displays as:

```
506 SERVO ALARM: n-AXIS FOLLOWING ERROR
```

Where *n* indicates the specific axis (X, Y, Z, A, B, etc.).

---

## What Causes Alarm 506

The following error is the gap between where the CNC *thinks* the axis is (based on the commanded move) and where the feedback device (encoder or linear scale) reports it actually is. When this gap exceeds the tolerance set in Parameter 1828 (PRM1828), the alarm triggers.

**Common causes:**
- Servo drive (amplifier) fault or failure — most common electrical cause
- Mechanical bind or excessive friction in the axis (leadscrew, linear guide, spindle taper)
- Encoder or encoder cable failure — position feedback is corrupted or lost
- Parameter 1828 set too tight relative to the machine's actual capability
- Machine tool axis has crashed and the mechanical components are damaged
- Acceleration/deceleration time constants set too aggressively
- Low or fluctuating servo bus voltage
- Axis motor has failed or has a degraded winding

---

## Step-by-Step Diagnosis {#step-by-step-fix}

### Step 1: Identify the faulted axis

The alarm message specifies which axis faulted (*n*-axis). Note whether the fault happens on a specific axis, during a specific motion type (rapid, feed, certain G-code), or at a specific machine position. This information is critical for narrowing the cause.

### Step 2: Check for mechanical binding

With the machine powered and the alarm reset (if possible), jog the affected axis slowly through its full travel. Listen and feel for:
- Unusual resistance at specific positions (indicates a damaged ballscrew or guide)
- Grinding or scraping noise (debris, scoring, or bearing failure)
- Backlash or play (worn ballscrew nut)

If the machine recently crashed, inspect the axis for bent components, broken ballscrew support bearings, or damaged linear guides.

### Step 3: Inspect the servo amplifier

Check the servo amplifier (servo drive) for fault indicator LEDs. Fanuc servo amplifiers display their own alarm codes via a 7-segment LED on the front of the unit. Common servo amplifier alarms that accompany Alarm 506 include:
- **SV401** (Servo amplifier overcurrent)
- **SV414** (Servo amplifier fault)
- **SV436** (Soft thermal — motor overloaded)

Document any servo amplifier alarm codes displayed before the main CNC control powers down the axes.

### Step 4: Check the encoder and feedback cable

1. Inspect the encoder cable from the servo motor to the servo amplifier for pinching, cuts, or damage at the cable entry points (common failure point is where the cable bends at the machine tool body).
2. Check the encoder connector at the motor and at the amplifier for bent pins, moisture, or corrosion.
3. If the machine has a dual feedback system (motor encoder + separate linear scale), check both feedback devices.
4. With the CNC in diagnostic mode, monitor the feedback position as you manually move the axis. If feedback is jumping or reading zero, the encoder or cable has failed.

### Step 5: Review relevant parameters

Key parameters related to Alarm 506:

| Parameter | Function | Notes |
|-----------|----------|-------|
| PRM1828 | In-position following error tolerance | Increase cautiously if alarm is marginal |
| PRM1826 | In-position width | |
| PRM1825 | Servo loop gain | |

**Caution:** Do not increase Parameter 1828 beyond the machine builder's specification without understanding the root cause. Increasing the tolerance masks a real problem and can lead to parts being cut out of tolerance.

### Step 6: Test the servo amplifier swap

If mechanical and encoder checks are clean, the servo amplifier is the prime suspect. Most shops have a spare amplifier for the most common axis. Swap the amplifier for the faulted axis and test. If the alarm moves to the new axis, the amplifier was not the cause. If the alarm clears, the original amplifier has failed.

---

## How to Fix Alarm 506 {#how-to-fix}

| Root Cause | Fix |
|-----------|-----|
| Mechanical binding (ballscrew, guide) | Lubricate or replace the failed mechanical component |
| Encoder cable damaged | Replace the encoder cable — never splice a servo encoder cable |
| Encoder failed | Replace the motor/encoder assembly |
| Servo amplifier failed | Replace the servo amplifier |
| Parameters incorrect after restore | Restore machine parameters from the machine builder's parameter backup |
| Following crash | Inspect all axis mechanical components; replace damaged parts |

---

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Typical Cost | Where to Buy |
|------|-------------|-------------|
| Fanuc Servo Amplifier (αi series) | $500–$2,000+ | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-506&k=Fanuc+servo+amplifier+A06B+replacement&tag=errorcodefixes-20) |
| Fanuc Encoder Cable | $80–$300 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-506&k=Fanuc+encoder+cable+servo+motor+replacement&tag=errorcodefixes-20) |
| Fanuc αi Servo Motor | $800–$3,000+ | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-506&k=Fanuc+servo+motor+alpha+i+replacement&tag=errorcodefixes-20) |
| Ballscrew Nut (machine specific) | $300–$1,500 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-506&k=CNC+ballscrew+nut+replacement+machining+center&tag=errorcodefixes-20) |

> **Important on pricing:** Fanuc servo drives are precision industrial components. Prices vary widely between new Fanuc-authorized parts, rebuilt units, and used surplus. Always verify part numbers against the machine tool builder documentation before ordering.

---

## When to Call a Technician

Servo amplifier replacement on a Fanuc-controlled machining center requires proper parameter backup, careful hardware installation, and axis tuning after replacement. If you do not have machine parameter backups on file, do not replace the servo amplifier without a Fanuc-certified technician present — a machine that powers up with incorrect parameters can make violent unexpected moves.

Mechanical repairs to ballscrews and linear guides require precision alignment tools and should be performed by the machine tool builder's service organization or a qualified rebuild shop.

> **Pro tip:** Fanuc Alarm 506 that occurs only at the end of a rapid traverse move (G00) but not during cutting feed (G01/G02/G03) is almost always an acceleration/deceleration parameter issue or a servo loop gain mismatch — not a hardware failure. Check with the machine builder before replacing any hardware.

## Related Articles

- [Fanuc Alarm 414 — Servo Amplifier Fault](/posts/fanuc-alarm-414/)
- [Fanuc Alarm 401 — Servo Ready Signal Off](/posts/fanuc-alarm-401/)
- [Fanuc Alarm 500 — Overtravel Alarm Fix](/posts/fanuc-alarm-500/)

## See Also

- [Fanuc Alarm 700 — Causes & Fix](/posts/fanuc-alarm-700/)
- [Fanuc Alarm 300 — APC Alarm Fix (Absolute Encoder)](/posts/fanuc-alarm-300/)
- [Fanuc Alarm 1 Overtravel — Causes & Fix](/posts/fanuc-alarm-1-overtravel/)
- [Fanuc Alarm 300: APC Battery Low — Absolute Encoder Battery Fix](/posts/fanuc-alarm-300-apc-battery/)
