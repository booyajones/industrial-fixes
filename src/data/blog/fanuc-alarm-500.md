---
title: "Fanuc Alarm 500 — Causes & Fix"
description: "What Fanuc Alarm 500 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - fanuc
---

## Fanuc Alarm 500 — What It Means

Fanuc Alarm 500 is an overtravel alarm — one or more axes traveled beyond the software overtravel limits stored in the machine parameters. Unlike hardware overtravel alarms (1-4 series), Alarm 500 is a software position check; the control detected that the commanded path would enter or has entered the software travel boundary.

[Jump to Fix](#fix)

## Common Causes

- **Machine returned to wrong reference position** — After a power cycle or battery change, if the reference return wasn't completed correctly, the machine's position understanding is wrong and normal moves trigger 500.
- **Part offset or work coordinate set incorrectly** — A work coordinate (G54-G59) or tool length offset that positions the program path outside the machine travel envelope triggers 500.
- **Program error** — A G-code program commanding a position beyond the machine's soft limits triggers 500 before the move executes.
- **Soft limit parameter changed** — Incorrect or reduced travel limits in machine parameters cause normal positions to trigger Alarm 500.

## Step-by-Step Fix {#fix}

1. **Identify which axis triggered 500** — The Fanuc alarm display shows the axis designation. Note it.
2. **Check current position vs. soft limits** — On the Fanuc position display, compare the current machine coordinate to the soft limit values in parameters (typically P1320/P1321 for positive/negative limits per axis).
3. **Re-execute reference return** — If position is uncertain after a power cycle, execute ZRN (reference return) on all axes before any other motion.
4. **Check work coordinates and offsets** — Verify G54 (or active work coordinate) and tool length offsets are correct for the current setup.
5. **Manual jog out of limit** — If the axis is inside the soft limit boundary, use the [OVR cancel] function (hold RESET and press the positive or negative axis jog button on some Fanuc versions) to jog out of the soft limit zone.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Backup battery | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-500&k=Backup+battery&tag=errorcodefixes-20) \| If position was lost due to battery failure |
## When to Call a Pro

If Alarm 500 triggers on moves that were previously fine, a parameter change or position calibration issue needs Fanuc-certified service to diagnose.

## Related Articles

- [Fanuc 0i-MD Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-0i-md-alarm-codes/)
- [Fanuc 30i/31i/32i Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-30i-alarm-codes/)
- [Fanuc Alarm 1 Overtravel — Causes & Fix](/posts/fanuc-alarm-1-overtravel/)
- [Fanuc Alarm 10 Servo Alarm — Causes & Fix](/posts/fanuc-alarm-10-servo-alarm/)
- [Fanuc Alarm 2 — Overtravel Plus Causes & Fix](/posts/fanuc-alarm-2-overtravel/)
