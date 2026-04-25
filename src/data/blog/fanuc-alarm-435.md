---
title: "Fanuc Alarm 435 — Causes & Fix"
description: "What Fanuc Alarm 435 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T14:00:00Z
modDatetime: 2026-04-22T14:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - cnc
  - fanuc
---

## Fanuc Alarm 435 — What It Means

Fanuc Alarm 435 indicates a servo following error on the Y-axis — the difference between the commanded position and the actual encoder feedback position exceeded the allowable tolerance during movement. Like Alarm 414 (X-axis) and 436 (Z-axis), this is a servo system alarm that indicates the Y-axis cannot keep up with the commanded motion profile.

[Jump to Fix](#fix)

## Common Causes

- **Y-axis mechanical binding** — A worn linear guideway, over-tightened ballscrew preload, or interference in the Y-axis travel causes resistance that the servo can't overcome within tolerance.
- **Servo drive fault** — A degraded or failing Y-axis servo amplifier reduces available torque, causing lag in position tracking.
- **Encoder cable fault** — A damaged or intermittent encoder cable causes the position feedback to drop out, instantly creating a following error.
- **Parameter error** — If the in-position tolerance or following error threshold parameters have been changed, the alarm can trigger at lower error values than previously acceptable.

## Step-by-Step Fix {#fix}

1. **Jog the Y-axis by hand** — With power off (E-stop engaged), try to move the Y-axis by hand. It should move smoothly with no rough spots or binding. Resistance indicates a mechanical issue.
2. **Check Y-axis servo drive status** — Power up and check the servo amplifier display for the Y-axis. Any fault codes on the amplifier itself narrow the diagnosis to the drive or motor.
3. **Inspect the encoder cable** — Check the Y-axis encoder cable from motor to drive for pinch points, cuts, and secure connections at both ends. Substitute a known-good cable to eliminate it.
4. **Check the Y-axis ballscrew and guideway** — Look for contamination, inadequate lubrication, or visible wear. Ensure lubrication system is functional and oil levels are correct.
5. **Reset the alarm** — Press RESET on the control panel after correcting the root cause. MDI jog the Y-axis through its full travel and confirm 435 does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Y-axis encoder cable | [Amazon](https://www.amazon.com/s?k=Y-axis+encoder+cable&tag=errorcodefixes-20) \| Replace if damaged or intermittent |
| Y-axis servo motor | [Amazon](https://www.amazon.com/s?k=Y-axis+servo+motor&tag=errorcodefixes-20) \| Replace if motor resistance tests show winding fault |
| Y-axis servo amplifier | [Amazon](https://www.amazon.com/s?k=Y-axis+servo+amplifier&tag=errorcodefixes-20) \| Replace if amplifier shows its own fault code |
## When to Call a Pro

Guideway and ballscrew repair requires precision measurement and Fanuc-trained service to restore machine accuracy after any mechanical work.

## Related Articles

- [Fanuc 0i-MD Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-0i-md-alarm-codes/)
- [Fanuc 30i/31i/32i Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-30i-alarm-codes/)
- [Fanuc Alarm 1 Overtravel — Causes & Fix](/posts/fanuc-alarm-1-overtravel/)
- [Fanuc Alarm 10 Servo Alarm — Causes & Fix](/posts/fanuc-alarm-10-servo-alarm/)
- [Fanuc Alarm 2 — Overtravel Plus Causes & Fix](/posts/fanuc-alarm-2-overtravel/)
