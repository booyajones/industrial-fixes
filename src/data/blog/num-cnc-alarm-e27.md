---
title: "NUM CNC Alarm E27 — Servo Error Causes & Fix"
description: "What NUM CNC alarm E27 means on NUM 1060/1080 series controls, why servo errors occur, and how to fix it step by step."
pubDatetime: 2026-04-22T15:00:00Z
modDatetime: 2026-04-22T15:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - num
money_part: "Encoder or linear scale read head"
---

## NUM CNC Alarm E27 — What It Means

Alarm E27 on a NUM CNC system (NUM 1060, 1080, or Flexium series) indicates a servo axis error — the control has detected a discrepancy between the commanded axis position and the actual encoder position that exceeds the configured following error tolerance. NUM (Numerical Control Systems — a French CNC manufacturer) uses the E-series alarm codes for its axis and servo faults. E27 is a following error alarm and forces an immediate axis stop. The machine requires a manual reset before axes can be jogged or a program resumed.

[Jump to Fix](#fix)

## Common Causes

- **Mechanical binding or collision** — A workpiece, fixture, or chip in the axis travel path creates resistance that exceeds the servo drive's torque capability, causing position lag to grow until E27 trips.
- **Servo drive fault** — An internal fault in the NUM servo drive (overheat, overcurrent, or a power supply fault) reduces or eliminates torque output. The axis cannot track the commanded profile and E27 fires.
- **Encoder or scale feedback fault** — A dirty linear scale, a damaged rotary encoder, or a loose feedback cable provides incorrect position data, causing the control to calculate a large (phantom) following error.
- **Following error tolerance set too tight** — The parameter controlling the allowable position deviation may have been set aggressively for the application. On high-speed cuts, even a healthy servo system may transiently exceed a very tight tolerance.
- **Low servo power supply voltage** — A degraded servo power supply rail reduces motor torque headroom. At high feed rates or during acceleration, the motor cannot keep up and E27 fires.

## Step-by-Step Fix {#fix}

1. **Identify the specific axis** — NUM alarm E27 is typically accompanied by an axis identifier (e.g., X, Y, Z). Identify which axis faulted.
2. **Inspect for mechanical obstruction** — With power off, manually move the faulted axis through its range of travel. Any binding, roughness, or hard stop indicates a mechanical problem.
3. **Check the servo drive for secondary faults** — Look at the NUM servo amplifier module associated with the faulted axis. Note any LED fault codes or display sub-alarms. A servo-level fault is often the root cause.
4. **Inspect the encoder/scale** — Check the feedback cable at both ends for secure connections. On machines with linear scales, clean the read head and scale with a lint-free cloth. Inspect for physical damage.
5. **Review following error parameters** — With access to NUM's parameter editor (NUMAGX or Flexium+ tooling), verify the following error tolerance parameter for the axis is appropriate. Increasing the tolerance slightly can filter nuisance E27 trips without masking a real problem.
6. **Check servo power supply output** — Measure the DC bus voltage of the servo power supply. A low or fluctuating reading indicates a power supply fault.
7. **Reset and test** — After addressing the cause, clear E27 and jog the axis slowly through its range. Then run a test program at low feed override before returning to production.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Encoder or linear scale read head | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-num-cnc-alarm-e27&k=Encoder+or+linear+scale+read+head&tag=errorcodefixes-20) \| Match NUM feedback specification for the axis |
| NUM servo amplifier | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-num-cnc-alarm-e27&k=NUM+servo+amplifier&tag=errorcodefixes-20) \| Match axis power rating and NUM system generation |
| Feedback cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-num-cnc-alarm-e27&k=Feedback+cable&tag=errorcodefixes-20) \| Shielded; replace if any damage or corrosion is found |
## When to Call a Pro

NUM CNC systems are common in European aerospace and precision machining environments. NUM parameter editing and servo commissioning require access to NUM's configuration tools and training. Contact NUM's technical support or a certified NUM service partner for E27 faults that recur after mechanical and feedback inspection.

## Related Articles

- [CNC Alarm Reset Guide: How to Clear Alarms Safely](/posts/cnc-alarm-reset-guide/)
- [CNC Machine Error Codes: Complete Troubleshooting Guide](/posts/cnc-error-codes-guide/)
- [Doosan CNC Alarm Codes Guide — Fanuc / Fanuc i Series Controls](/posts/doosan-cnc-fault-codes/)
- [Fanuc 0i-MD Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-0i-md-alarm-codes/)
- [Fanuc 30i/31i/32i Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-30i-alarm-codes/)
