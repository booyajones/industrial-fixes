---
title: "Alarm 300 – CNC Spindle Drive Fault (Fanuc)"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-01-22T08:00:00Z
modDatetime: 2024-01-22T08:00:00Z
slug: cnc-alarm-300-spindle-fault
featured: false
draft: false
tags:
  - cnc
  - fanuc
  - spindle
  - alarm-codes
description: "Fanuc Alarm 300 halts the spindle immediately. This guide walks through the most common causes and how to get your machine back in cycle."
---

## What Alarm 300 Means

**Alarm 300** on Fanuc-controlled CNC machines is a **spindle speed deviation alarm**. The control expected a certain spindle speed (commanded via S-word), but the actual feedback speed differed by more than the allowable tolerance — typically 10–15% for more than 1–2 seconds.

This is a hard stop alarm. The machine will not run until the condition is cleared and reset.

## Common Causes

- Spindle encoder failure or dirty encoder disc
- Loose or broken encoder coupling between spindle motor and encoder
- Spindle drive (amplifier) fault — check drive display for sub-codes
- V-belt wear or breakage (belt-driven spindles)
- Mechanical binding in spindle bearings
- Incorrect spindle parameters (especially after board replacement)
- Coolant intrusion into encoder housing

## Diagnostic Steps

1. **Check the spindle drive display** for a sub-alarm code. Fanuc spindle amplifiers (SPM, SPMC) display their own fault codes. Common sub-codes:
   - `AL-24`: Motor overheat
   - `AL-31`: Speed deviation (confirms the 300 alarm source is in the drive)
   - `AL-41`: Encoder feedback fault

2. **Inspect the encoder and coupling.** Remove the rear cover at the top of the spindle motor. Look for cracked or slipping couplers and debris on the encoder disc.

3. **Check belt tension** (if belt-driven). A worn or broken belt will cause speed deviation under load even if the motor runs free.

4. **Run the spindle with the door open** at a low RPM (e.g., S200) and monitor actual speed on the diagnostic screen (`DGNOS` → `SERVO` → spindle feedback). If actual speed shows zero or erratic, encoder is suspect.

5. **Check parameters 4000–4099** (spindle parameters). Parameter `4020` sets max RPM; `4002` controls feedback type. If recently changed, restore from backup.

## Clearing the Fault

Fix the root cause first, then:
1. Press **RESET** on the MDI panel.
2. If the drive sub-alarm is still active, cycle power to the spindle drive (or full machine power-off for 30 seconds).
3. Run a slow spindle test: `S100 M03` in MDI mode before returning to cycle.

> **Never mask this alarm with a parameter change** (e.g., increasing deviation tolerance) without fixing the root cause. Spindle damage and scrapped parts will follow.
