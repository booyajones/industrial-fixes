---
title: "Fanuc Alarm 2 — Overtravel Plus Causes & Fix"
description: "What Fanuc alarm 2 overtravel plus means, why it triggers, and how to clear it step by step."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - cnc
  - fanuc
---

## Fanuc Alarm 2 — Overtravel Plus: What It Means

Fanuc Alarm 2 is an **Overtravel (Plus direction) hardware limit** — an axis has tripped the positive hardware overtravel limit switch. Unlike the software overtravel limits (set in parameters), the hardware OT switch is a physical limit switch wired directly to the CNC as a safety interlock. When the machine axis travels beyond the positive hardware limit, the drive cuts out and Alarm 2 is stored. The machine will not move the faulted axis in any direction except back off the limit switch using the override procedure.

[Jump to Fix](#fix)

## Common Causes

- **Manual jog or programmed move past the soft limit** — A program with incorrect coordinate values or a manual jog that inadvertently moved the axis beyond the positive mechanical boundary.
- **Soft limit not configured or set too wide** — If software overtravel limits (Parameter 1320/1321) are not set correctly, the axis can reach the hardware limit before the software limit trips.
- **Homing (reference) position lost** — After a power loss or battery failure, the machine may home incorrectly and lose its reference point, causing all subsequent moves to have wrong absolute position.
- **Defective or misadjusted OT switch** — The hardware limit switch itself has shifted position or failed in a way that triggers prematurely.

## Step-by-Step Fix {#fix}

1. **Activate OT release function** — On most Fanuc systems, press and hold the OT Release (or Hardware OT Release) function key on the MDI panel, or hold the appropriate button combination per your machine's operation manual. This temporarily overrides the hardware OT signal.
2. **Jog axis off the limit** — While holding OT release, use the handwheel or manual jog to move the axis in the **minus** direction (away from the positive hardware limit). Move just far enough to clear the limit switch — typically 5–10mm is sufficient.
3. **Release the OT release button** — Once the axis is clear, release the OT release button. Alarm 2 should clear.
4. **Verify axis position** — Check the current machine coordinate position. If the position looks incorrect relative to the known physical position, perform a machine reference (home) cycle.
5. **Check soft limit parameters** — In MDI, access Parameter mode and verify that the positive software limit (Parameter 1320 for each axis) is set inside the physical hardware limit by at least 5mm.
6. **Inspect the OT switch** — If the alarm tripped without apparent cause, check the hardware limit switch for physical shift, contamination, or cable damage.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Overtravel limit switch](https://www.amazon.com/s?k=Overtravel%20limit%20switch&tag=errorcodefixe-20) | Replace if the switch actuates at the wrong position or shows intermittent behavior |
| [Limit switch cable](https://www.amazon.com/s?k=Limit%20switch%20cable&tag=errorcodefixe-20) | If wiring to the OT switch is chafed or broken |

## When to Call a Pro

If the machine homes incorrectly after clearing Alarm 2, the absolute encoder battery may be dead or the reference mark may be lost. Incorrect homing on multi-axis machines can cause crashes — have a Fanuc-trained service engineer verify the reference point before resuming production.
