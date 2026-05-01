---
title: "Fanuc OT Alarm — Software Overtravel (All Series)"
description: "Fanuc soft OT alarm means the control hit a software travel limit, not necessarily a hard limit switch. Learn how to back off the axis and correct the underlying cause."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "Dana Kowalski"
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
| [Wrong work offset](https://www.amazon.com/s?k=Wrong+work+offset&tag=errorcodefixes-20) | Program zero shifted too far |
| [Machine lost reference return](https://www.amazon.com/s?k=Machine+lost+reference+return&tag=errorcodefixes-20) | Absolute position no longer valid |
| [Travel limit parameters wrong](https://www.amazon.com/s?k=Travel+limit+parameters+wrong&tag=errorcodefixes-20) | After battery loss or bad restore |
| [Manual jog past software limit](https://www.amazon.com/s?k=Manual+jog+past+software+limit&tag=errorcodefixes-20) | Common during setup |

## How to Clear It

1. Put the machine in JOG or HANDLE mode
2. Use overtravel cancel / OT release if your machine builder provides it
3. Jog the axis back toward the safe travel area
4. Re-reference the machine
5. Check offsets and parameters before restarting the job

## Soft OT vs. Hard OT

| [Type](https://www.amazon.com/s?k=Type&tag=errorcodefixes-20) | Meaning |
|---|---|
| [Soft OT](https://www.amazon.com/s?k=Soft+OT&tag=errorcodefixes-20) | Control/calculated limit exceeded |
| [Hard OT](https://www.amazon.com/s?k=Hard+OT&tag=errorcodefixes-20) | Physical limit switch activated |

If the alarm clears once the axis is moved back and the machine is re-homed, it was likely a true soft overtravel. If it remains, check limit switches, parameters, and absolute position status.

## Bottom Line

Fanuc soft OT alarms are usually caused by bad position data or bad setup data, not failed hardware. Back off the axis safely, re-home, and verify your work offsets.

## Related Articles

- [Fanuc 0i-MD Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-0i-md-alarm-codes/)
- [Fanuc 30i/31i/32i Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-30i-alarm-codes/)
- [Fanuc Alarm 1 Overtravel — Causes & Fix](/posts/fanuc-alarm-1-overtravel/)
- [Fanuc Alarm 10 Servo Alarm — Causes & Fix](/posts/fanuc-alarm-10-servo-alarm/)
- [Fanuc Alarm 2 — Overtravel Plus Causes & Fix](/posts/fanuc-alarm-2-overtravel/)
