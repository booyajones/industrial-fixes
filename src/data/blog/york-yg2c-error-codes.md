---
title: "York YG2C Furnace Error Codes — Flash Code Diagnostic Guide"
description: "Complete guide to York YG2C furnace error codes, flash sequences, fault causes, and step-by-step repairs for the most common HVAC failures."
pubDatetime: 2026-04-22T22:00:00Z
modDatetime: 2026-04-22T22:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - york
  - furnace
---

## York YG2C Furnace Error Codes — What They Mean

The York YG2C is a two-stage, variable-speed gas furnace in the Affinity series. It uses an ECM blower and communicates fault conditions through a diagnostic LED on the control board. The YG2C supports York's Affinity communicating thermostat, which can display readable fault descriptions. For non-communicating systems, read the LED flash code directly.

[Jump to Fix](#fix)

## York YG2C Flash Code Reference

| Flash Code | Meaning |
|------------|---------|
| 1 flash | Normal — call satisfied |
| 2 flashes | Lockout — ignition failure |
| 3 flashes | Pressure switch stuck open |
| 4 flashes | High-limit switch open |
| 5 flashes | Flame detected without call |
| 6 flashes | 115V power fault or reversed polarity |
| 7 flashes | Gas valve circuit fault |
| 8 flashes | Weak flame signal |
| 9 flashes | Rollout switch open |
| 10 flashes | Inducer or pressure switch fault (low fire) |
| 11 flashes | Blower motor fault |
| 12 flashes | Limit device lockout (repeated trips) |
| 13 flashes | Control board fault |

## Common Causes by Code

- **Code 2 — Ignition lockout** — York YG2C uses a hot surface ignitor. Check for visible cracks; measure resistance (should be 40–100 ohms). Also check low-fire gas valve operation — on first startup after ignition lockout, the valve should open on low-fire before modulating to high.
- **Code 3 — Pressure switch open** — Two-stage furnaces like the YG2C often have two pressure switches (one for low fire, one for high fire). Confirm both hoses are intact and the condensate system is draining. PVC drain clogs are the most common field cause.
- **Code 4 — High limit** — York YG2C limit switch is on the supply plenum. Check filter, return grille, and blower speed selection. Variable-speed units may have a speed table error if the control board was recently replaced — confirm taps are set correctly.
- **Code 9 — Rollout** — Manual reset required. On the YG2C, rollout switches are on the burner manifold bracket. Investigate for cracked heat exchanger before resetting.
- **Code 10 — Low-fire pressure fault** — The YG2C two-stage design requires adequate negative pressure at low-fire before advancing to high-fire. If the secondary heat exchanger condensate is backing up, Code 10 often appears before Code 3.
- **Code 11 — Blower motor fault** — ECM motor communication error. Try power-cycling for 60 seconds. If the motor still won't run, check the 5-wire communicating plug at the motor and control board.

## Step-by-Step Fix {#fix}

1. **Read the code** — Lower door sight glass. Record flash count precisely.
2. **For Code 3 / 10** — Check both pressure switch hoses. Confirm the condensate trap inside the YG2C cabinet is clear. On two-stage units, disconnect each pressure switch hose and apply known pressure with a manometer to test switch actuation at the correct threshold.
3. **For Code 4 / 12** — Replace filter. Check all supply registers. If the ECM blower starts but sounds weak, the motor speed tap may be configured too low for the installed ductwork.
4. **For Code 2** — Watch the ignitor during startup (through the sight glass if possible). It should glow orange within 30–45 seconds of a call for heat. No glow = ignitor or board issue. Glow but no flame = gas supply or valve issue.
5. **For Code 11** — Power cycle completely (off 60 seconds). Check the communications cable between the motor module and the control board. Corrosion on the low-voltage connector is a known cause on older YG2C units.
6. **For Code 9** — Find and manually reset the rollout switch (red button). Before doing so, use a flashlight to inspect the burner compartment for sooting, orange staining, or burnt insulation — signs of flame rollout.
7. **Clear and retest** — Cycle power, run a full heat cycle, confirm no code recurrence.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hot surface ignitor | York/Nordyne-specific; confirm model compatibility |
| ECM blower module | Rear of motor; test before replacing full motor |
| Pressure switch | Confirm low-fire and high-fire ratings separately |
| Rollout switch | Manual reset; investigate root cause |
| High-limit switch | Auto-reset; check continuity |
| Control board | For Code 13 or unexplained faults |

## When to Call a Pro

The YG2C's two-stage gas valve and variable-speed ECM blower are complex enough that board-level diagnosis benefits from York's proprietary tools. If you're chasing intermittent faults across multiple codes, an Affinity-compatible communicating thermostat will show detailed fault history that flash codes don't capture.
