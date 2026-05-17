---
title: "Okuma LB-Series Alarm 1013 — Causes & Fix"
description: "What Okuma LB-Series Alarm 1013 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - okuma
---

## Okuma LB-Series Alarm 1013 — What It Means

Okuma Alarm 1013 on LB-Series CNC lathes (LB-3000, LB-4000, LB-6000 and similar) indicates a servo axis fault — the servo system detected an abnormal condition on one of the lathe's controlled axes (X, Z, or turret). On lathes, this most commonly affects the X and Z axes that position the cutting tool. The alarm stops all motion and spindle operation.

[Jump to Fix](#fix)

## Common Causes

- **Encoder cable damage or disconnection** — The encoder cable from the axis servo motor to the drive carries position feedback; damage or disconnection causes Alarm 1013 immediately.
- **Servo drive overcurrent** — Heavy interrupted cuts, dull tooling, or a jammed turret puts excessive current demand on the axis servo, triggering the overload protection.
- **Axis mechanical binding** — Contamination or inadequate lubrication on the lathe's cross-slide (X) or carriage (Z) guideways increases friction beyond what the servo can track.
- **Servo amplifier fault** — The axis servo amplifier has an internal fault that prevents it from delivering commanded torque.

## Step-by-Step Fix {#fix}

1. **Identify the affected axis** — The Okuma OSP display shows which axis generated Alarm 1013. Note it.
2. **Inspect axis for binding** — Move the affected axis by hand (E-stop engaged) and feel for rough motion or hard spots. Lathes should move very smoothly.
3. **Check lubrication** — Verify the automatic lubrication system is functioning and oil is reaching the guideways. LB-Series lathes have a centralized lube system.
4. **Inspect encoder cable** — Check the encoder cable from the axis motor to the drive cabinet for physical damage, particularly at the motor end where heat and oil exposure are greatest.
5. **Check servo amplifier display** — Look at the amplifier LED or display for axis-specific fault codes that provide more detail than the CNC alarm.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Servo encoder cable | [Amazon](https://www.amazon.com/s?i=industrial&k=Servo+encoder+cable&tag=errorcodefixes-20) \| Replace if damaged; must match axis motor connector |
| Servo motor encoder | [Amazon](https://www.amazon.com/s?i=industrial&k=Servo+motor+encoder&tag=errorcodefixes-20) \| Replace if cable is fine but feedback is erratic |
| Servo amplifier | [Amazon](https://www.amazon.com/s?i=industrial&k=Servo+amplifier&tag=errorcodefixes-20) \| Replace if amplifier has its own internal fault |
## When to Call a Pro

Okuma LB-Series servo system work requires factory-trained service for drive calibration and axis accuracy verification after any mechanical or electrical repair.

## Related Articles

- [CNC Alarm Reset Guide: How to Clear Alarms Safely](/posts/cnc-alarm-reset-guide/)
- [CNC Machine Error Codes: Complete Troubleshooting Guide](/posts/cnc-error-codes-guide/)
- [Doosan CNC Alarm Codes Guide — Fanuc / Fanuc i Series Controls](/posts/doosan-cnc-fault-codes/)
- [Fanuc 0i-MD Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-0i-md-alarm-codes/)
- [Fanuc 30i/31i/32i Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-30i-alarm-codes/)
