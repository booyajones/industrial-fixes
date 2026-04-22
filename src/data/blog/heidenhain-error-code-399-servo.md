---
title: "Heidenhain Error Code 399 Servo Error — Causes & Fix"
description: "What Heidenhain TNC 640 error code 399 means, why a servo error occurs, and how to diagnose and recover the axis."
pubDatetime: 2026-04-22T11:00:00Z
modDatetime: 2026-04-22T11:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - cnc
  - heidenhain
---

## Heidenhain Error Code 399 — What It Means

Error 399 on a Heidenhain TNC 640 (and related iTNC/TNC series) controls indicates a servo error — the control detected a following error (lag error) on a servo axis that exceeded the allowable tolerance. This means the actual axis position fell too far behind the commanded position during motion. The machine stops and this error is displayed to prevent incorrect machining or machine damage from an axis that is not tracking the commanded path.

[Jump to Fix](#fix)

## Common Causes

- **Mechanical binding or overload on the axis** — A tight guide, contaminated ball screw, or inadequate lubrication causes excessive friction that the servo cannot overcome, creating a growing following error.
- **Insufficient servo drive gain or current limit** — If the servo drive parameters are set too conservatively, the axis cannot accelerate aggressively enough to track high-speed commanded moves.
- **Encoder feedback loss or noise** — Intermittent encoder signal causes the control to receive incorrect position feedback, making the following error calculation incorrect and tripping error 399.
- **Axis blocked by a physical obstruction** — A clamp, workpiece, or fixture physically blocking the axis creates an immediate high following error.

## Step-by-Step Fix {#fix}

1. **Clear the error and inspect for physical obstruction** — Check the full travel range of the affected axis for any physical obstruction — clamps, tooling, chip buildup, or way covers that are pinched or jammed.
2. **Manually jog the axis slowly** — After clearing the error with the TNC Reset button, manually jog the axis at very low feed rate through its full range. Listen and feel for grinding, binding, or unusual resistance.
3. **Check axis lubrication** — Verify the central lubrication system is operating and that the lubrication distributor for the affected axis is supplying oil. Dry guides create dramatically higher friction and following errors.
4. **Inspect the encoder cable and read head** — For linear encoders (Heidenhain scales), check the read head for contamination and verify the cable is not damaged. Clean the linear scale with Heidenhain-approved cleaning solution.
5. **Check servo drive parameters** — In the Heidenhain machine parameters (MP), verify the following error tolerance (machine parameter MP 1420 or equivalent) is set appropriately for the machine's speed and acceleration profile. A tolerance set too tight will cause nuisance errors.
6. **Verify servo drive operation** — Open the electrical cabinet and check the servo drive for any fault LEDs or displays. A servo drive fault may appear simultaneously with TNC error 399.
7. **Reset and test** — After addressing the mechanical or electrical cause, reset the error on the TNC, perform a reference return, and run the machine through a test cycle at reduced feed rate.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Linear encoder read head | Replace if contamination or physical damage is found |
| Encoder feedback cable | Replace if intermittent signal is confirmed |
| Ball screw support bearing | Replace if ball screw binding is due to bearing failure |
| Servo drive module | Replace if drive has a confirmed hardware fault accompanying error 399 |

## When to Call a Pro

Heidenhain servo system tuning (following error tolerance, drive gains) requires a Heidenhain-certified machine tool builder or service technician. Encoder calibration after replacement also requires proper alignment tools and Heidenhain service software.
