---
title: "Haas Alarm 116 — Causes & Fix"
description: "What Haas Alarm 116 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T14:00:00Z
modDatetime: 2026-04-22T14:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - haas
---

## Haas Alarm 116 — What It Means

Haas Alarm 116 indicates a spindle over speed fault — the spindle exceeded the maximum RPM limit programmed in the machine parameters or the commanded speed exceeded what the drive can safely deliver. Haas controls monitor spindle encoder feedback; if actual RPM exceeds the threshold, the control trips immediately to protect the spindle motor, bearings, and tooling.

[Jump to Fix](#fix)

## Common Causes

- **Spindle drive runaway** — A failing spindle drive can command full voltage to the spindle motor without proper speed feedback, causing uncontrolled overspeed.
- **Encoder feedback fault** — If the spindle encoder signal is lost or erratic, the drive may not correctly regulate speed and allows overspeed.
- **S-word programming error** — A program commanding a spindle speed above the machine's maximum RPM rating (or above the work-holding limit for the chuck) triggers Alarm 116 as a safety cutout.
- **Spindle drive parameter error** — Incorrect maximum speed parameters in the spindle drive amplifier allow speeds above the mechanical limit.

## Step-by-Step Fix {#fix}

1. **Check the program S-word** — Review the CNC program for the spindle speed command that was active when 116 tripped. If S value exceeds machine max RPM (or chuck/fixture speed limit), correct the program.
2. **Verify max RPM machine parameter** — In the Haas parameter list, check Parameter 131 (Max Spindle Speed). Confirm it's set to the machine's rated maximum and hasn't been incorrectly modified.
3. **Check spindle encoder cable** — A damaged or intermittent encoder cable causes erratic speed feedback. Inspect the cable from the spindle motor to the drive for damage.
4. **Check spindle drive** — If the drive commanded full output without speed limiting, the drive's speed regulation circuit may have failed. Review drive fault history.
5. **Power cycle and test at low RPM** — After correcting the root cause, power cycle and run a test at S500 (500 RPM) while monitoring actual spindle speed on the Haas diagnostics screen.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Spindle encoder cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-116&k=Spindle+encoder+cable&tag=errorcodefixes-20) \| Replace if damaged or intermittent signal |
| Spindle drive (servo amplifier) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-116&k=Spindle+drive+%28servo+amplifier%29&tag=errorcodefixes-20) \| If drive runaway is confirmed |
## When to Call a Pro

Spindle overspeed events can damage bearings and toolholders. After any Alarm 116 event, inspect the spindle for damage before returning to production. Haas service can perform a spindle diagnostic check.

## Related Articles

- [Haas CNC Alarm 101 — Emergency Stop Active Fix](/posts/haas-alarm-101-emergency-stop/)
- [Haas Alarm 102 — Servo Drive Fault Fix](/posts/haas-alarm-102/)
- [Haas Alarm 103 — Servo Overload Fix](/posts/haas-alarm-103/)
- [Haas Alarm 104 Feed Hold — Causes & Fix](/posts/haas-alarm-104-feed-hold/)
- [Haas Alarm 105 E-Stop — Causes & Fix](/posts/haas-alarm-105/)

## See Also

- [Haas Alarm 111 — Drive Fault](/posts/haas-alarm-111/)
- [Haas Alarm 119 — Spindle Not At Speed Causes & Fix](/posts/haas-alarm-119/)
- [Haas Alarm 108 — Causes & Fix](/posts/haas-alarm-108/)
- [Haas EC-400 Horizontal Machining Center Alarm Codes](/posts/haas-ec-400-alarm-codes/)
