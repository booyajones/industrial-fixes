---
title: "Fanuc Alarm 411 — Causes & Fix"
description: "What Fanuc Alarm 411 servo error means, why it trips, and how to diagnose and fix it step by step."
pubDatetime: 2026-04-22T13:00:00Z
modDatetime: 2026-04-22T13:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - fanuc
money_part: "Encoder feedback cable"
most_likely_cause: "Encoder feedback cable fault"
---

## What this code means
Fanuc **Alarm 411** is a **Servo Alarm** — specifically a radial direction overspeed error or a velocity control error on the servo axis indicated in the alarm message. On Fanuc 0i, 16i, and 18i controls, Alarm 411 means the servo motor speed has exceeded the rated maximum or the velocity control loop has detected an error it cannot recover from. Alarm 411 frequently appears alongside Alarm 414 (servo alarm with sub-code) and Alarm 424 (following error). The alarm stops all axis motion immediately to prevent mechanical damage.

## Common Causes

- **Encoder feedback cable fault** — A damaged, loose, or intermittent encoder cable causes the servo amplifier to receive incorrect speed feedback, tripping the velocity control alarm.
- **Servo amplifier failure** — The amplifier's current control section has malfunctioned, causing the axis to overspeed momentarily before the alarm triggers.
- **Parameter mismatch** — After a battery replacement or parameter initialization, velocity and position gain parameters (CMR, speed feedback parameters) may be reset to incorrect defaults.
- **Mechanical issue causing velocity oscillation** — Loose ballscrew nut, worn servo motor coupling, or excessive backlash causes axis velocity oscillation that triggers 411.

## Step-by-Step Fix {#fix}

1. **Identify the faulted axis** — The alarm display identifies which axis (X, Y, Z) generated alarm 411. Check the corresponding servo amplifier module LED for a sub-fault code.
2. **Inspect the encoder cable** — Power off, LOTO. Reseat the encoder feedback cable at both the servo motor encoder and the amplifier CNC interface. Look for bent pins, cracked connectors, or cable damage from chip guard contact.
3. **Check servo amplifier LED code** — The servo amplifier (alpha or beta series) shows its own internal alarm code on a 7-segment display. Cross-reference this code with the amplifier maintenance manual for the specific failure.
4. **Compare current parameters to backup** — If parameters were recently changed or the machine had a power outage, compare current velocity parameters to the machine builder's backup. Parameter errors after battery replacement are a common 411 cause.
5. **Reset and jog slowly** — E-stop reset, then jog the affected axis at 1% override. If 411 fires immediately at any speed, the encoder cable or amplifier is the likely cause. If it only occurs at higher speeds, it's a parameter or mechanical issue.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Encoder feedback cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-411&k=Encoder+feedback+cable&tag=errorcodefixes-20) \| Replace if cable shows any physical damage or intermittent continuity |
| Servo amplifier module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-411&k=Servo+amplifier+module&tag=errorcodefixes-20) \| Replace when amplifier-side alarm code points to internal failure |
| Servo motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-411&k=Servo+motor&tag=errorcodefixes-20) \| Replace when encoder or motor winding tests confirm motor-side failure |
## When to Call a Pro

Alarm 411 root-cause diagnosis often requires oscilloscope-level servo trace analysis and Fanuc SERVO GUIDE software. Fanuc-certified service engineers and CNC machine tool dealers' service departments have this tooling and training.
