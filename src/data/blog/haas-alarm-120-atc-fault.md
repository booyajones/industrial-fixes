---
title: "Haas Alarm 120 ATC Fault — Causes & Fix"
description: "What Haas Alarm 120 Automatic Tool Changer fault means, why it trips, and how to clear and fix it step by step."
pubDatetime: 2026-04-22T13:00:00Z
modDatetime: 2026-04-22T13:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - cnc
  - haas
---

## Haas Alarm 120 ATC Fault — What It Means

Haas **Alarm 120** is an **Automatic Tool Changer (ATC) fault** — the tool changer did not complete its cycle within the expected time or position. The 120-series alarms (120–129) all relate to ATC motion failures, and Alarm 120 is the general ATC fault that fires when the changer stops mid-cycle or fails to confirm a position. This alarm stops the program immediately and leaves the machine in a state where the ATC arm may be mid-stroke, requiring a careful recovery sequence to avoid crashing.

[Jump to Fix](#fix)

## Common Causes

- **ATC motor or brake failure** — The ATC drive motor or its associated brake has failed, preventing the arm from completing its rotation cycle.
- **Proximity switch misalignment or failure** — ATC position is monitored by proximity sensors; a shifted or failed prox switch prevents the control from confirming the arm's position.
- **Jam in the tool changer arm or carousel** — A dropped tool, chip impaction in the tool pocket, or a bent retention knob jams the mechanical motion.
- **Low air pressure to ATC cylinder** — On machines with pneumatic ATC elements, insufficient air pressure prevents tool release or clamp mechanisms from completing their stroke.

## Step-by-Step Fix {#fix}

1. **Do NOT power cycle immediately** — With the machine in alarm, visually confirm where the ATC arm is parked. Note whether it's in the spindle, mid-stroke, or at a pocket. Understand the position before moving anything.
2. **Use the ATC RECOVERY procedure** — On Haas controls, navigate to the ATC RECOVERY menu (typically under Parameters or the ATC section of the control). Follow the on-screen steps to manually advance or retract the arm to a safe home position.
3. **Check all tool pockets for obstructions** — Inspect the carousel (or side-mount changer) for chips, a tool that has slipped in its pocket, or a retention knob that's pulling the tool loose. Remove any obstruction.
4. **Check proximity switches** — Locate the ATC position sensors (typically 2–4 prox switches). With the machine in alarm, check that each sensor's LED indicator is in the correct state for the arm's physical position. A sensor showing the wrong state points to the failed component.
5. **Verify air pressure** — Check the machine's air pressure gauge. Haas requires 85–100 PSI at the machine. Low air causes incomplete tool clamp/unclamp cycles.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ATC proximity switch | [Amazon](https://www.amazon.com/s?k=ATC+proximity+switch&tag=errorcodefixes-20) \| Replace when LED state is wrong for the arm's known position |
| ATC motor or gear drive | [Amazon](https://www.amazon.com/s?k=ATC+motor+or+gear+drive&tag=errorcodefixes-20) \| Replace when motor tests show winding fault or drive won't turn under power |
| Tool retention knob | [Amazon](https://www.amazon.com/s?k=Tool+retention+knob&tag=errorcodefixes-20) \| Replace if a tool is dropping out of the carousel pocket |
| Tool holder | [Amazon](https://www.amazon.com/s?k=Tool+holder&tag=errorcodefixes-20) \| Inspect BT/CAT holders for damage that prevents proper seating |
## When to Call a Pro

If the ATC arm is mid-stroke and manual recovery fails to advance it to a safe position, do not force the mechanism. Call Haas Factory Outlet (HFO) service — a forced recovery attempt can bend the arm or damage the carousel, turning a $500 sensor fix into a $10,000 mechanical repair.

## Related Articles

- [Haas CNC Alarm 101 — Emergency Stop Active Fix](/posts/haas-alarm-101-emergency-stop/)
- [Haas Alarm 102 — Servo Drive Fault Fix](/posts/haas-alarm-102/)
- [Haas Alarm 103 — Servo Overload Fix](/posts/haas-alarm-103/)
- [Haas Alarm 104 Feed Hold — Causes & Fix](/posts/haas-alarm-104-feed-hold/)
- [Haas Alarm 105 E-Stop — Causes & Fix](/posts/haas-alarm-105/)
