---
title: "Fanuc Alarm 6 Overtravel — Causes & Fix"
description: "What Fanuc alarm 6 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T08:00:00Z
modDatetime: 2026-04-22T08:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - cnc
  - fanuc
---

## Fanuc Alarm 6 Overtravel — What It Means

Fanuc alarm 6 means hardware overtravel — a physical limit switch on one of the machine's axes has been tripped. On Fanuc 0, 0i, 16/18/21 series controls, each linear axis has hardwired overtravel (OT) limit switches at both ends of travel. When the axis moves far enough to contact one of these switches, the control issues alarm 6 and immediately cuts servo drive power to that axis (and sometimes all axes depending on the machine builder's configuration). The alarm identifies which axis and direction: "OT+X" is positive X overtravel, "OT-Z" is negative Z overtravel, and so on.

[Jump to Fix](#fix)

## Common Causes

- **Manual jog in wrong direction** — The most common cause. An operator jogged an axis past its software limit or the machine reference position wasn't established, and the axis ran into the hardware limit switch.
- **Work offset or fixture error** — A program with an incorrect work offset can command the axis into a hardware OT position during a machining cycle.
- **Reference position not established** — If the machine was powered on without performing a reference return (homing), the software travel limits aren't enforced and a jog operation can reach the hardware limit.
- **Limit switch failure or adjustment** — A limit switch that has drifted out of position, been physically moved, or has failed closed can falsely trigger alarm 6.

## Step-by-Step Fix {#fix}

1. **Identify the overtravel direction from the alarm** — Note whether the alarm shows OT+ or OT- and which axis. This tells you which direction to move the axis to clear the limit switch.
2. **Enter overtravel release mode** — On Fanuc controls, hold the OT RELEASE key (or the equivalent machine builder key, often a dedicated key or function key on the operator panel) while jogging the axis in the direction that moves it away from the tripped limit switch. Move slowly in small increments.
3. **Move the axis off the limit switch** — Jog the axis in the direction opposite to the OT direction until the limit switch clears. You will feel resistance come off. Typically only 1–2mm of movement is needed.
4. **Release the OT RELEASE key and perform reference return** — Once off the limit, perform a manual reference return (REF/HOME) to re-establish the coordinate system.
5. **Reset the system** — Press RESET on the control after the reference return completes. Alarm 6 should clear. Investigate and correct the root cause (offset error, operator procedure, limit switch position).

## Parts Often Needed

| Part | Notes |
|------|-------|
| Overtravel limit switch | [Amazon](https://www.amazon.com/s?k=Overtravel+limit+switch&tag=errorcodefixes-20) \| OMRON or equivalent; match the NC (normally closed) contact rating |
| Limit switch mounting bracket | [Amazon](https://www.amazon.com/s?k=Limit+switch+mounting+bracket&tag=errorcodefixes-20) \| Replace if the switch was physically displaced |
## When to Call a Pro

If alarm 6 appears during automatic cycle operation with correct work offsets and a verified reference position, the limit switch position may need adjustment by the machine tool builder or an authorized Fanuc service technician.
