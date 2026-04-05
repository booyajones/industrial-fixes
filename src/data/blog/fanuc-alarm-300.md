---
title: "Fanuc Alarm 300 — APC Alarm Fix (Absolute Encoder)"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-10T08:00:00Z
modDatetime: 2024-03-10T08:00:00Z
slug: fanuc-alarm-300
featured: false
draft: false
tags:
  - cnc
  - fanuc
  - alarm
  - encoder
  - servo
description: "Fanuc Alarm 300 is an APC (Absolute Pulse Coder) alarm on the absolute encoder. This guide covers battery replacement, encoder initialization, and board-level diagnosis."
---

## Error Code: Fanuc Alarm 300

**What it means:** Alarm 300 (or 300 APC ALARM: n-TH AX) is an Absolute Pulse Coder (APC) alarm. The absolute encoder on one or more servo axes has lost its position data. On Fanuc systems, absolute encoders maintain machine position even when the machine is powered off — using a small backup battery to retain the encoder count. When that battery dies, or when the encoder itself fails, the position data is lost and the control can no longer trust the machine's position.

Alarm 300 will not allow axis movement until the issue is resolved. The machine must be re-referenced (homed) after the battery is replaced.

The "n" in "n-TH AX" refers to the axis number — Alarm 300 with axis 1 = X axis, axis 2 = Y axis, axis 3 = Z axis, and so on.

## Common Causes

- **Dead or weak backup battery** — The most common cause by far. Fanuc absolute encoder batteries (3.6V lithium, typically AA-size) typically last 1–3 years. The control gives a low battery warning (Alarm 306 or similar) before the battery fully dies — if that warning was ignored, Alarm 300 follows.
- **Battery not replaced during power-off period** — If the battery is already weak and the machine is powered off for an extended period (vacation shutdown, relocation, storage), the battery can drain to nothing without the main power supply compensating.
- **Encoder cable damage** — A damaged cable between the encoder and the servo amplifier can interrupt the encoder signal, causing the control to report a position data loss.
- **Failed absolute encoder** — The encoder itself (the Pulse Coder unit attached to the servo motor) has failed internally. Less common than battery failure, but it happens, especially on motors with high hours.
- **Servo amplifier failure** — The amp can misread encoder data during a fault condition and flag it as an APC alarm.

## Step-by-Step Fix

1. **Identify which axis is affected.** The alarm display will show which axis number (n-TH AX). Note this — if it's a Z axis on a vertical machining center, extra care is needed when re-referencing because the axis needs to be supported or moved up before homing.

2. **With the machine POWERED ON, replace the backup battery.** This is critical: the battery must be replaced while the machine control is powered on. If you power off first with a dead battery, you guarantee position data loss. The backup battery is typically in a battery holder on the servo amplifier cabinet or on the CNC control unit — consult your specific Fanuc model documentation. On most Series 0i/16i/18i/21i systems, the APC battery is a ER6C 3.6V AA-size lithium cell.

3. **Locate and replace the correct battery.** On most Fanuc systems, there are two types of batteries: (a) the CNC control memory backup battery (for programs and parameters) and (b) the APC encoder backup battery (for position data). Alarm 300 means the APC battery. These are different. Confirm which battery you're replacing by checking the servo amplifier unit directly.

4. **After battery replacement, clear the alarm.** The alarm may clear on its own after battery replacement, or you may need to press RESET on the control. On some Fanuc controls, you must enter the APC ALARM CLEAR procedure: go to OFFSET/SETTING → SETTING page → set APC ALARM parameter to 0.

5. **Reference (home) the affected axes.** With the alarm cleared, the machine needs to re-establish absolute position. Perform the manual reference return (ZRN) procedure for all affected axes. The sequence varies by machine — consult the machine builder's manual for the correct reference return procedure. On most VMCs, home Z first (away from table), then X and Y.

6. **Verify position by running a known program.** After re-referencing, run a dry-run cycle of a simple known program and verify the axes move to expected positions. Compare against a part you've already cut or against machine coordinates you know.

7. **Set a battery replacement reminder.** Fanuc encoder batteries should be replaced every 1–2 years, proactively. Don't wait for Alarm 306 (low battery warning). Use the machine maintenance log.

## Parts That May Need Replacement

| Part | Where to Buy | Typical Cost |
|------|-------------|-------------|
| Fanuc APC battery (ER6C 3.6V AA Lithium, A98L-0031-0012) | Fanuc America, AutomationDirect, Amazon | $8–$20 each |
| Fanuc absolute encoder (model-specific A860-0309-T301 or equiv.) | Fanuc America, CNC parts dealers | $400–$1,200 |
| Encoder cable (model-specific) | Fanuc America, Motion Controls LLC | $80–$300 |
| Servo amplifier (model-specific) | Fanuc America, used CNC dealers | $500–$2,500 |

## When to Call a Professional

If you've replaced the battery with the machine powered on, cleared the alarm, re-referenced the axes, and Alarm 300 returns — the encoder itself is likely failing. Encoder replacement requires removal of the servo motor, encoder disassembly, and re-initialization — a job for a Fanuc-trained technician. If Alarm 300 returns on multiple axes simultaneously after battery replacement, the servo amplifier or the CNC control's encoder interface card may have failed. Tell the tech: "Alarm 300 on axis [n], battery replaced with machine powered on, alarm clears but returns within [minutes/hours/power cycles]. I need encoder or amp diagnosis."

> **Pro tip:** When replacing Fanuc APC batteries, replace ALL axis batteries at the same time, even if only one axis alarmed. They were all installed at the same time and will all fail around the same time. The cost of the batteries is trivial compared to re-referencing multiple axes after a cascade of 300 alarms on production startup.
