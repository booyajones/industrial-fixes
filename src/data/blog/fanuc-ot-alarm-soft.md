---
title: "Fanuc OT Alarm — Software Overtravel (All Series)"
description: "Fanuc soft OT alarm means the control hit a software travel limit, not necessarily a hard limit switch. Learn how to back off the axis and correct the underlying cause."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - fanuc
  - cnc
  - overtravel
  - software-overtravel
  - error-code
---

## Fanuc Soft OT Alarm

A **Fanuc soft OT alarm** means the axis exceeded a **software-defined travel limit**. This is different from a hard overtravel where a physical limit switch is hit. The control stopped motion because the machine position exceeded parameter limits.

## Common Causes

| Cause | Details |
|---|---|
| Wrong work offset | Program zero shifted too far |
| Machine lost reference return | Absolute position no longer valid |
| Travel limit parameters wrong | After battery loss or bad restore |
| Manual jog past software limit | Common during setup |

## How to Clear It

1. Put the machine in JOG or HANDLE mode
2. Use overtravel cancel / OT release if your machine builder provides it
3. Jog the axis back toward the safe travel area
4. Re-reference the machine
5. Check offsets and parameters before restarting the job

## Soft OT vs. Hard OT

| Type | Meaning |
|---|---|
| Soft OT | Control/calculated limit exceeded |
| Hard OT | Physical limit switch activated |

If the alarm clears once the axis is moved back and the machine is re-homed, it was likely a true soft overtravel. If it remains, check limit switches, parameters, and absolute position status.

## Bottom Line

Fanuc soft OT alarms are usually caused by bad position data or bad setup data, not failed hardware. Back off the axis safely, re-home, and verify your work offsets.
