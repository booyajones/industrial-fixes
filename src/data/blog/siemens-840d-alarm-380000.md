---
title: "Siemens 840D Alarm 380000 — Causes & Fix"
description: "What Siemens Sinumerik 840D Alarm 380000 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - cnc
  - siemens
---

## Siemens 840D Alarm 380000 — What It Means

Alarm 380000 on the Siemens Sinumerik 840D indicates a drive enable signal is missing — the safety logic that allows the drives to energize hasn't received its enable signal. On the 840D, the NCU (Numerical Control Unit) communicates drive enable status through the DRIVE-CLiQ or X121/X122 interface; if the enable chain is broken, no axis or spindle drive can be powered.

[Jump to Fix](#fix)

## Common Causes

- **E-stop circuit not reset** — The most common cause. The emergency stop circuit is still active, preventing drive enable from being asserted.
- **Safety relay or contactor not closed** — The machine's safety relay chain (door interlocks, light curtains, safety mats) has an open element that prevents the drive enable signal.
- **DRIVE-CLiQ enable signal fault** — The enable signal transmitted over DRIVE-CLiQ from the NCU to the drive modules is not being received correctly.
- **Commissioning parameter not set** — On a newly configured or restored machine, a parameter controlling drive enable may not be correctly set.

## Step-by-Step Fix {#fix}

1. **Reset the E-stop** — Twist and release all E-stop buttons on the machine and operator panel. The E-stop chain must be fully clear before drive enable can be asserted.
2. **Check door and safety interlocks** — Verify all machine doors are fully closed and all safety devices (light curtains, safety mats) are in their normal/cleared state.
3. **Check the safety relay module** — In the control cabinet, locate the safety relay or PLCopen safety module and verify its status LEDs indicate the safety circuit is closed.
4. **Cycle the axis enable switch** — On the 840D operator panel, use the axis release key switch and press the drive reset/enable button sequence per the machine documentation.
5. **Check DRIVE-CLiQ connections** — If the above steps don't clear 380000, inspect DRIVE-CLiQ cable connections between the NCU and first drive module.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Safety relay module | Replace if safety chain won't close |
| DRIVE-CLiQ cable | Replace if enable signal transmission is interrupted |
| E-stop button | Replace if button is stuck in depressed state |

## When to Call a Pro

840D safety circuit and drive commissioning issues require Siemens-trained service. Do not bypass safety interlocks to clear Alarm 380000.
