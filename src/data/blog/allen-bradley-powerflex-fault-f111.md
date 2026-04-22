---
title: "Allen-Bradley PowerFlex Fault F111 — Causes & Fix"
description: "What Allen-Bradley PowerFlex fault F111 means, why motor over speed triggers, and how to fix it step by step."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - allen-bradley
---

## Allen-Bradley PowerFlex Fault F111 — What It Means

Allen-Bradley PowerFlex fault F111 is a **Motor Over Speed** fault — the drive detected that the motor exceeded the maximum allowable speed limit as defined by the over-speed parameter. On PowerFlex 40, 70, 700, and 755 series drives, the motor speed is monitored continuously; if it goes beyond the programmed over-speed threshold (typically set as a percentage above maximum frequency), F111 trips the drive to protect the motor and driven equipment from mechanical damage at excessive speeds.

[Jump to Fix](#fix)

## Common Causes

- **Over-speed trip level set too low** — The over-speed parameter (P505 or similar) is configured at a value too close to the normal operating maximum; transient speed increases during deceleration or load rejection trip it.
- **Regenerative overspeed** — During deceleration of a high-inertia load, the load drives the motor faster than commanded (regeneration); the drive sees over-speed.
- **Encoder feedback error** — On closed-loop (encoder feedback) drives, an encoder fault or noise can cause the drive to misread speed as excessively high.
- **Runaway condition** — The motor is genuinely running away due to a process or mechanical issue (e.g., a descending load on a hoist with a failed brake).

## Step-by-Step Fix {#fix}

1. **Check the over-speed limit parameter** — In Connected Components Workbench or the drive keypad, find the over-speed limit parameter (typically P505 in PF40/70 or A556 in PF755). Verify it's set to an appropriate value — typically 110–115% of maximum speed.
2. **Review the application** — Is the load high-inertia (fan, flywheel, large pump)? High-inertia loads can overshoot during decel. Consider increasing deceleration time (P036) or enabling a deceleration braking option.
3. **Enable dynamic braking or regen** — If regenerative overspeed is the cause, adding a dynamic brake resistor dissipates regenerative energy and prevents speed overshoot during deceleration.
4. **Check encoder feedback** — On Vector Control drives with encoder feedback, inspect the encoder cable for damage or routing near high-voltage wires. Verify encoder PPR parameter matches the physical encoder.
5. **Inspect the mechanical system** — Confirm the load cannot backdrive the motor. On hoists and conveyors, verify that mechanical brakes engage properly before the drive is removed from the circuit.
6. **Reset and test** — After parameter corrections, clear the fault (press Stop/Reset or cycle drive power), and run the application at reduced speed first to confirm normal operation before returning to full speed.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Dynamic brake resistor](https://www.amazon.com/s?k=Dynamic%20brake%20resistor&tag=errorcodefixe-20) | Required if regenerative overspeed is the root cause |
| [Encoder cable](https://www.amazon.com/s?k=Encoder%20cable&tag=errorcodefixe-20) | Shielded, properly routed; replace if damaged |
| [No hardware parts for parameter-only fixes](https://www.amazon.com/s?k=No%20hardware%20parts%20for%20parameter-only%20fixes&tag=errorcodefixe-20) | — |

## When to Call a Pro

If F111 occurs during a genuine runaway condition (the motor is physically overspeeding beyond control), stop the machine immediately using the E-stop. A controls engineer must investigate the mechanical brake system and process control logic before restarting.
