---
title: "Mazak Alarm 400 Servo Error — Causes & Fix"
description: "What Mazak alarm 400 servo error means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - mazak
---

## Mazak Alarm 400 Servo Error — What It Means

Mazak alarm 400 is a servo error indicating a fault in the axis servo drive or servo motor circuit. On Mazak machines using Mitsubishi MELDASMAGIC or MAZATROL controls, alarm 400 is often associated with the X-axis servo drive detecting an abnormal condition — overcurrent, overvoltage, undervoltage on the servo bus, or a drive hardware fault. The specific servo drive alarm sub-code (visible on the servo drive panel or control diagnostic screen) narrows the cause to the exact fault type. Alarm 400 is a machine shutdown alarm that requires identifying the servo drive sub-fault before clearing.

[Jump to Fix](#fix)

## Common Causes

- **Servo drive sub-fault (overcurrent or overvoltage)** — The Mitsubishi servo drive that powers the axis detected excessive current or DC bus voltage. Check the 7-segment display or diagnostic LEDs on the servo amplifier inside the electrical cabinet.
- **Servo motor winding fault** — The motor has an inter-winding fault or phase-to-phase insulation failure. The drive detects the abnormal current signature and trips alarm 400.
- **Mechanical binding or axis crash** — The axis was driven into a hard stop, workpiece, or mechanical obstruction. The surge in servo current from the collision triggers the drive protection.
- **Encoder feedback fault** — A damaged encoder or encoder cable causes the drive to lose position feedback, which triggers a following error or drive fault that appears as alarm 400.

## Step-by-Step Fix {#fix}

1. **Read the servo drive sub-fault code** — Open the Mazak electrical cabinet and locate the servo drive for the faulting axis. The Mitsubishi servo drive has a 7-segment LED display showing the sub-fault code. Reference the Mitsubishi MR-J2/J4/J5 servo amplifier manual for the specific code meaning.
2. **Check for mechanical obstruction** — Jog the axis away from any mechanical limit or obstruction. Check the tool path and fixture for collision damage. Inspect the ball screw and guideways for any debris or deformation.
3. **Check servo motor cable** — Power off and lock out the machine. Inspect the servo motor cable for damage, paying attention to flex points near the motor connector and the drag chain exits. Damaged cable is a frequent cause.
4. **Test motor winding insulation** — With the cable disconnected at the drive, megger test the motor at 500V DC between each winding pair and between windings and ground. Low resistance (<1 MΩ) indicates insulation degradation.
5. **Reset the drive and monitor** — After correcting the mechanical or electrical issue, power cycle the servo drive and the CNC. Attempt a reference return and monitor for re-fault.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Mitsubishi servo amplifier (MR-J series) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mazak-alarm-400-servo&k=Mitsubishi+servo+amplifier+%28MR-J+series%29&tag=errorcodefixes-20) \| Match the specific model for the axis — voltage, current rating, and feedback type |
| Servo motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mazak-alarm-400-servo&k=Servo+motor&tag=errorcodefixes-20) \| Mazak typically uses Mitsubishi HF/HC series motors; match by model number |
| Encoder cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mazak-alarm-400-servo&k=Encoder+cable&tag=errorcodefixes-20) \| Replace if feedback is the confirmed cause of the fault |
## When to Call a Pro

Mazak alarm 400 with a servo drive sub-fault of AL.16 (encoder error) or AL.24 (amplifier hardware fault) typically requires the servo amplifier to be replaced and potentially returned to Mitsubishi or a repair depot. Contact Mazak service for drives under warranty.

## Related Articles

- [CNC Alarm Reset Guide: How to Clear Alarms Safely](/posts/cnc-alarm-reset-guide/)
- [CNC Machine Error Codes: Complete Troubleshooting Guide](/posts/cnc-error-codes-guide/)
- [Doosan CNC Alarm Codes Guide — Fanuc / Fanuc i Series Controls](/posts/doosan-cnc-fault-codes/)
- [Fanuc 0i-MD Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-0i-md-alarm-codes/)
- [Fanuc 30i/31i/32i Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-30i-alarm-codes/)
