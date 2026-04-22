---
title: "Haas Alarm 119 — Spindle Not At Speed Causes & Fix"
description: "What Haas alarm 119 means, why the spindle fails to reach commanded speed, and how to fix it step by step."
pubDatetime: 2026-04-22T15:00:00Z
modDatetime: 2026-04-22T15:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - cnc
  - haas
---

## Haas Alarm 119 — What It Means

Alarm 119 (SPINDLE NOT AT SPEED) on a Haas CNC means the spindle failed to reach the commanded RPM within the allowable time window after an S command was issued. Haas's spindle drive monitors actual spindle speed via encoder feedback and compares it to the commanded speed; if the actual speed does not come within the "at-speed" tolerance band (typically ±2–5% of setpoint) within several seconds, alarm 119 fires. The machine halts to prevent a tool engagement at the wrong speed.

[Jump to Fix](#fix)

## Common Causes

- **Spindle motor overload or overcurrent** — Aggressive cuts, a dull tool, or a heavy workpiece increase spindle load; if the drive cannot maintain speed against the load, the RPM drops and alarm 119 fires.
- **Spindle drive fault** — An underlying drive alarm (overheat, DC bus fault, or feedback loss) prevents the drive from commanding sufficient torque to reach setpoint. Check the spindle drive LED indicators in the control cabinet.
- **Worn or slipping spindle belt** — On belt-driven machines, a stretched or glazed belt slips under load, and the actual encoder-measured RPM lags the commanded speed.
- **Spindle encoder signal loss** — If the spindle encoder feedback is noisy or intermittent, the drive receives incorrect speed data and the CNC cannot confirm "at speed," triggering alarm 119 even when the spindle is running.
- **Low DC bus voltage** — A supply voltage sag to the spindle drive reduces available torque, preventing full acceleration to setpoint especially at high RPMs.

## Step-by-Step Fix {#fix}

1. **Reset and test at low RPM** — Press RESET and issue a low-speed spindle command (e.g., S500 M03 in MDI). If the spindle starts normally at low speed but alarms at high speed, the issue is load or drive-related.
2. **Check the spindle drive for sub-alarms** — Open the control cabinet and inspect the spindle drive module for any lit fault LEDs or displayed sub-codes. A secondary drive fault is the most common root cause of alarm 119.
3. **Inspect the spindle belt** — On belt-driven spindles, access the belt compartment (usually behind the spindle head cover). Check belt tension and look for glazing, cracks, or obvious wear. Adjust or replace as needed.
4. **Check spindle encoder signal** — Inspect the encoder cable for damage and verify the connectors are secure at both ends. A shielded cable pulled away from its strain relief is a common failure point.
5. **Monitor spindle load** — Run the spindle at progressive speeds and monitor the spindle load meter on the Haas display. Load exceeding 100% at light mechanical load indicates a drive or mechanical restriction problem.
6. **Verify input power quality** — Measure the three-phase supply to the machine. Low or unbalanced voltage reduces spindle drive output torque.
7. **Reset and test** — After repairs, run the spindle through its full RPM range (S500, S1000, S3000, max RPM) and confirm "at speed" is achieved without alarm at each step.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Spindle belt | Haas OEM; match machine model and spindle size |
| Spindle encoder | Replace if signal is noisy or absent at the drive |
| Spindle drive (vector drive module) | Match machine and spindle HP rating |

## When to Call a Pro

If alarm 119 is caused by a spindle drive fault or a motor winding issue, contact the Haas Factory Outlet (HFO). Spindle motor replacement and drive parameter re-commissioning are beyond routine maintenance scope.
