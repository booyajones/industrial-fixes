---
title: "Danfoss FC302 Alarm 49 - Causes & Fix"
description: "Alarm 49 on a Danfoss FC302 VFD means the motor speed is outside configured limits. Adjust parameters 4-11 and 4-13 to fix it."
pubDatetime: 2026-06-04T09:13:03Z
modDatetime: 2026-06-04T09:13:03Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 parameter backup module"
most_likely_cause: "Speed limits set too narrow"
---

## What this code means
Alarm 49 on the Danfoss FC302 is a speed-limit warning, not a hardware fault. The drive reports this code when the commanded or actual motor speed falls below the low limit set in parameter 4-11 (Motor Speed Low Limit) or rises above the high limit set in parameter 4-13 (Motor Speed High Limit). It is a configuration issue rather than an overtemperature, overcurrent, or power-stage failure.

The drive continues to protect the application by flagging any speed reference that exceeds the programmed operating window. In most cases the limits were set too narrowly during commissioning, or an external control signal (PID loop, process controller, or manual reference) is pushing the setpoint outside the allowed range. Correcting the speed-limit parameters or reviewing the reference source will clear the warning.

## Common Causes

- **Speed limits set too narrow** Parameters 4-11 and 4-13 define a window smaller than the application's actual operating range, so normal operation crosses the boundary.
- **External reference driving setpoint out of range** A PID loop, analog input, or fieldbus command is commanding the drive beyond the configured low or high speed threshold.
- **Parameter mismatch after commissioning** Speed limits were copied incorrectly when replacing the drive or updating settings, leaving outdated or factory-default values active.
- **Process condition forcing unexpected demand** Changes in load, pressure, or flow push the process controller to request a motor speed that violates the programmed limits.
- **Reference scaling misconfiguration** The input scaling (percent or engineering units) translates the control signal into a speed command that exceeds the limit parameters.
- **Motor feedback discrepancy** If encoder or tachometer feedback is enabled, a mismatch between actual and expected speed can trigger the limit warning under closed-loop control.

## Step-by-Step Fix {#fix}

1. **Confirm the exact alarm number** on the VFD keypad or display to verify it is Warning 49 (Speed limit) and not a different fault code.
2. **Navigate to parameter 4-11** (Motor Speed Low Limit) and record the current setting in RPM, then check parameter 4-13 (Motor Speed High Limit) and note its value.
3. **Compare the active speed reference** displayed on the keypad (or via the communications interface) against the low and high limits to identify which boundary is being crossed.
4. **Widen the speed limits** by increasing parameter 4-13 or decreasing parameter 4-11 if the application legitimately requires a broader operating range than currently configured.
5. **Review the control source** (analog input, digital setpoint, PID output, or fieldbus) and verify that the reference signal is scaled correctly and does not exceed the intended speed range.
6. **Inspect any PID or automation logic** that may be driving the speed demand, and adjust loop gains, scaling, or clamps if the controller is overshooting the limit parameters.
7. **Reset the warning** after parameter changes by cycling power or using the alarm-reset function, then monitor the drive during normal operation to confirm the speed stays within the new limits.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 parameter backup module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-49-fault-code&k=Danfoss+FC302+parameter+backup+module&tag=errorcodefixes-20) \| Optional memory card to save and restore parameter sets during commissioning or replacement. |
| Analog reference potentiometer or signal source | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-49-fault-code&k=Analog+reference+potentiometer+or+signal+source&tag=errorcodefixes-20) \| If the external speed reference is drifting or scaled incorrectly, replace or recalibrate the input device. |

## When to Call a Pro

Call a qualified drives technician or controls engineer if you cannot identify which reference source is commanding the speed outside limits, if the warning persists after widening parameters 4-11 and 4-13, or if you suspect a feedback-device fault rather than a simple configuration issue. A professional can decode the control architecture, verify analog and digital I/O scaling, and check encoder or tachometer wiring when closed-loop speed control is involved. Because Alarm 49 is a process and parameter condition rather than a component failure, most fixes require expertise in VFD programming and industrial control rather than circuit-board repair.
