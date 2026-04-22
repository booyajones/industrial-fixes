---
title: "Haas Alarm 118 — Spindle Orientation Fault Causes & Fix"
description: "What Haas alarm 118 means, why spindle orientation fails, and how to fix it step by step."
pubDatetime: 2026-04-22T15:00:00Z
modDatetime: 2026-04-22T15:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - cnc
  - haas
---

## Haas Alarm 118 — What It Means

Alarm 118 (SPINDLE ORIENTATION FAULT) on a Haas CNC machining center means the spindle failed to reach and hold its indexed orientation position within the required time or accuracy window. Haas uses spindle orientation for tool changes, tapping cycles with rigid tap, and any operation that requires a known spindle angle. Alarm 118 fires when the spindle drive either cannot reach the target angle or detects that the spindle has slipped out of orientation after reaching it. The machine halts and requires a reset before tool change or rigid tap operations can resume.

[Jump to Fix](#fix)

## Common Causes

- **Spindle encoder or orientation disk fault** — The spindle orientation relies on an encoder or a magnetic sensor reading a dedicated orientation disk. A dirty, misaligned, or failed sensor cannot reliably lock the spindle at the correct angle.
- **Spindle drive parameter issue** — The orientation speed, creep speed, or position window parameters in the spindle drive or Haas control may have changed or drifted, causing the drive to overshoot the target position repeatedly.
- **Belt or direct-drive issue** — On belt-driven Haas spindles, a loose or worn spindle belt causes the spindle to slip during the orientation deceleration phase, overshooting the target.
- **High spindle load or drag** — A damaged spindle bearing, insufficient lubrication, or a stuck drawbar creates mechanical drag that prevents the spindle from stopping at the correct angle.
- **Spindle drive fault** — An underlying fault in the vector drive controlling the spindle — overheat, low bus voltage, or a feedback error — prevents the drive from executing orientation correctly.

## Step-by-Step Fix {#fix}

1. **Reset and attempt manual orientation** — Press RESET, then use MDI to command M19 (spindle orient). Note whether the spindle rotates toward a position and stops cleanly or continues hunting or overshooting.
2. **Inspect the spindle orientation sensor** — The orientation sensor is typically a Hall effect sensor reading a magnetic ring or a notch in the spindle encoder. Access via the spindle belt cover (follow Haas's service manual for the specific machine model). Clean the sensor face with a dry cloth and verify the gap is within the specified range.
3. **Check the spindle encoder feedback** — A spindle that oscillates or overshoots during M19 often has encoder noise or a degraded encoder signal. Check the encoder cable connector at both the spindle head and the control cabinet for looseness or corrosion.
4. **Inspect the spindle belt** — On belt-driven machines, check belt tension and condition. A loose belt slips during orientation deceleration. Adjust tension per the Haas maintenance manual.
5. **Check spindle bearings** — With power off, manually rotate the spindle. It should spin freely with no roughness or binding. Any roughness indicates bearing wear.
6. **Review orientation parameters in the Haas service page** — Parameters 65 (Orient Speed), 136 (Orient Window), and related values may need adjustment if the orientation sensor was replaced or the machine was recently serviced.
7. **Reset and test** — After any repair, run M19 from MDI five consecutive times and confirm the spindle locks consistently at the same orientation angle.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Spindle orientation sensor (Hall effect)](https://www.amazon.com/s?k=Spindle%20orientation%20sensor%20(Hall%20effect)&tag=errorcodefixe-20) | Match Haas machine model and spindle type |
| [Spindle encoder](https://www.amazon.com/s?k=Spindle%20encoder&tag=errorcodefixe-20) | Replace if feedback signal is noisy or lost |
| [Spindle belt](https://www.amazon.com/s?k=Spindle%20belt&tag=errorcodefixe-20) | Haas OEM belt; match machine and spindle size |

## When to Call a Pro

Spindle bearing replacement and spindle drive parameter tuning should be performed by a Haas Factory Outlet (HFO) technician. Incorrect bearing preload or drive parameters can damage the spindle in production.
