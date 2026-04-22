---
title: "Goodman GMSS96 Furnace Error Codes — Flash Code Diagnostic Guide"
description: "Complete guide to Goodman GMSS96 96% AFUE furnace error codes, flash sequences, common fault causes, and step-by-step fixes."
pubDatetime: 2026-04-22T22:00:00Z
modDatetime: 2026-04-22T22:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - goodman
  - furnace
---

## Goodman GMSS96 Furnace Error Codes — What They Mean

The Goodman GMSS96 is a 96% AFUE, single-stage, multi-speed gas furnace. It is a high-efficiency upflow/horizontal unit with a PVC flue and condensate drain system. Faults are reported through a diagnostic LED on the integrated furnace control board — flash sequences identify specific fault conditions. The LED is visible through the sight glass on the lower access door.

[Jump to Fix](#fix)

## Goodman GMSS96 Flash Code Reference

| Flash Code | Meaning |
|------------|---------|
| Continuous on | No call for heat (normal) |
| Continuous off | No power to board |
| 1 flash | Lockout — gas or ignition fault |
| 2 flashes | Pressure switch stuck open |
| 3 flashes | Pressure switch stuck closed |
| 4 flashes | Open high-limit device |
| 5 flashes | Flame sensed, gas valve not energized |
| 6 flashes | Rollout switch open |
| 7 flashes | Inducer motor fault |
| 8 flashes | Low flame signal |
| 9 flashes | Reversed 115V AC polarity |
| 10 flashes | Gas valve circuit fault |

## Common Causes by Code

- **Code 1 — Lockout** — The GMSS96 locks out after three failed ignition attempts or if flame is lost three times within one heating cycle. Check the ignitor, flame sensor, and gas pressure before resetting.
- **Code 2 — Pressure switch stuck open** — Common on the GMSS96 because of its dual heat exchanger design. The secondary heat exchanger collects condensate; a plugged drain causes the pressure switch to see positive (instead of negative) pressure and fail to close. Always check the PVC condensate drain first.
- **Code 3 — Pressure switch stuck closed** — The pressure switch contacts should open when the inducer is off. If they remain closed, the board won't start the inducer. A failed switch or a stuck contact is the usual cause.
- **Code 4 — High limit** — The GMSS96 has both a main limit switch and auxiliary limit. Dirty filter, blocked ductwork, or a failed blower motor are the primary causes. The auxiliary limit is on the secondary heat exchanger and trips if secondary drain blockage causes condensate to back up against it.
- **Code 6 — Rollout** — Manual-reset rollout switches on the GMSS96 are on the burner manifold. Rollout indicates heat exchanger crack, incorrect gas pressure, or burner blockage.
- **Code 7 — Inducer fault** — The GMSS96 monitors inducer operation. If the inducer fails to start or stalls, Code 7 appears. Confirm 120V at the inducer motor, then test winding continuity.
- **Code 8 — Weak flame** — Low µA signal from flame sensor. Clean the sensor rod with emery cloth. If signal remains below 1.0 µA, check ground continuity of the sensor wire back to the board.

## Step-by-Step Fix {#fix}

1. **Read the LED** — The GMSS96 LED is on the lower control board. Count flashes before opening anything.
2. **For Code 1** — Reset by cycling the power off for 30 seconds. Then monitor the next startup cycle closely: does the ignitor glow? Does gas ignite? Does the flame establish?
3. **For Code 2 (pressure switch open)** — Disconnect the drain line at the trap and blow through it to confirm it's clear. Check all PVC condensate fittings for cracks. Shake the pressure switch — if you hear liquid inside, condensate has entered the switch body (replace it).
4. **For Code 4** — Check both the main and auxiliary limit switch continuity with a multimeter. The auxiliary limit is located inside the unit near the secondary heat exchanger. A tripped auxiliary limit without a blower problem suggests drain backup against the limit.
5. **For Code 7** — Check inducer motor: confirm it attempts to start, listen for humming without rotation (failed capacitor), or complete silence (open motor winding or no power).
6. **For Code 8** — Remove flame sensor, clean rod with emery cloth, reinstall. Measure DC microamps in series with the sensor lead to the board. Normal is 1.5–4.0 µA.
7. **Reset and test** — After any repair, cycle the power switch, set the thermostat to heat, and run one full cycle.

## Parts Often Needed

| Part | Notes |
|------|-------|
| PVC condensate trap | Specific to GMSS96; replace if cracked or plugged |
| Flame sensor | Common; OEM or universal replacement |
| Pressure switch | Match water column rating to model (0.85" or 1.5") |
| Inducer motor | With or without housing; check wheel for debris first |
| High-limit switch | Check both main and auxiliary |
| Rollout switch | Investigate crack before replacing |

## When to Call a Pro

The GMSS96's secondary heat exchanger system is complex. Condensate-related failures can cascade into board damage if left undiagnosed. If you see repeated Code 4 trips with a clean filter, or if the unit produces a burning smell, call a licensed technician — do not operate the furnace until the secondary heat exchanger is confirmed intact.
