---
title: "Fanuc Alarm 400 — Causes & Fix"
description: "What Fanuc alarm 400 servo overload X-axis means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - cnc
  - fanuc
---

## Fanuc Alarm 400 — What It Means

Fanuc alarm 400 (SV0400: SERVO OVERLOAD: X AXIS) is a servo amplifier overload alarm for the X axis. The servo amplifier's thermal protection has tripped, meaning the amplifier was required to supply sustained high current — above its thermal rating — and the internal temperature limit was reached. On Fanuc Alpha and Beta series servo amplifiers, alarm 400 can also appear on other axis numbers (401=Z, 402=Y, etc. depending on axis assignment). This fault requires the underlying reason for high servo current to be identified and corrected, and the amplifier must be allowed to cool before reset.

[Jump to Fix](#fix)

## Common Causes

- **Excessive servo load from mechanical binding** — Ball screw wear, guide way contamination, insufficient lubrication, or a mechanical jam causes the servo to fight the mechanical resistance, drawing sustained high current.
- **Incorrect servo parameter settings** — Servo gain or feed-forward parameters set too aggressively cause the servo to oscillate or overcorrect, increasing average current demand.
- **Ambient temperature inside the control cabinet too high** — If the CNC cabinet cooling fan has failed or the ambient is above 40°C, servo amplifiers reach their thermal limit faster under any load.
- **Axis drive belt or coupling slip** — A slipping coupling or worn timing belt causes position error that the servo tries to correct by increasing torque output, increasing current.

## Step-by-Step Fix {#fix}

1. **Allow the servo amplifier to cool** — Do not attempt to reset alarm 400 immediately. The amplifier thermal protection must cool below the reset threshold first. Allow at least 15–30 minutes with power on and cooling fans running.
2. **Check axis mechanical resistance** — With the axis servo released (E-stop), try to manually push the axis by hand. Some resistance is normal on ballscrew axes; significant stiffness or binding indicates a mechanical problem. Check lubrication on the guideways and ballscrew.
3. **Check servo amplifier cooling** — Inspect the cooling fan on the servo amplifier itself and the cabinet cooling fans. A seized amplifier fan is a common cause of thermal overloads. Confirm airflow through the amplifier heatsink is unobstructed.
4. **Review servo parameters** — Check Fanuc servo parameters for excessive gain settings (parameters 2021, 2022, 2043, etc. for velocity loop and position loop gains). If recently changed, restore to the machine builder's default values.
5. **Check for position error oscillation** — In the servo diagnostic screen, observe the position error value during axis motion. An axis that oscillates (error swings back and forth) while stopped or during cut is fighting instability, increasing current.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Servo amplifier cooling fan](https://www.amazon.com/s?k=Servo%20amplifier%20cooling%20fan&tag=errorcodefixe-20) | Match voltage and CFM; Fanuc uses 24VDC fans on most amplifiers |
| [Ball screw nut or bearings](https://www.amazon.com/s?k=Ball%20screw%20nut%20or%20bearings&tag=errorcodefixe-20) | Replace if mechanical binding is the confirmed cause |
| [Servo amplifier module](https://www.amazon.com/s?k=Servo%20amplifier%20module&tag=errorcodefixe-20) | Replace if amplifier fails to reset after cooling and cause is identified/corrected |

## When to Call a Pro

Servo parameter adjustment on Fanuc systems requires access to parameter write mode and machine builder knowledge of the correct baseline values. Incorrect parameters can cause axis instability or crash the machine. A Fanuc-authorized service engineer should perform servo tuning if parameters are suspect.
