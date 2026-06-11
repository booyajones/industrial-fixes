---
title: "Fanuc Alarm 4 — Stored Stroke Limit Overtravel"
description: "What Fanuc alarm 4 means, why a stored stroke limit overtravel occurs, and how to clear the alarm and recover the axis."
pubDatetime: 2026-04-22T11:00:00Z
modDatetime: 2026-04-22T11:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - fanuc
money_part: "No parts typically required"
---

## Fanuc Alarm 4 — What It Means

Fanuc alarm 4 indicates a stored stroke limit overtravel in the negative direction (Alarm 4: Stored Stroke Limit 1 negative side). The CNC detected that the axis position reached or exceeded the software-defined travel boundary set in the stored stroke limit parameters. This is a software limit — not a physical limit switch — and stops axis motion before the machine reaches a mechanical hard stop.

[Jump to Fix](#fix)

## Common Causes

- **Workpiece or fixture placed outside the work envelope** — A setup change moved a fixture into a position that requires the tool to travel beyond the configured software limit.
- **Incorrect stored stroke limit parameters** — The stroke limit parameters (P1320/P1321 or equivalent) are set too conservatively and do not reflect the machine's actual safe travel range.
- **Reference position (zero return) not performed** — If the machine lost its reference position after a power cycle or E-stop, the stored limits may be referenced to an incorrect position and trip prematurely.
- **Axis overtravel during MDI or program execution** — A manually entered MDI command or NC program commanded the axis to a position beyond the stored limit.

## Step-by-Step Fix {#fix}

1. **Do not force axis motion** — When alarm 4 is active, do not attempt to jog the axis further in the negative direction. The machine is at or past its software boundary.
2. **Switch to MPG or jog mode** — On the operator panel, switch the mode selector to Handle (MPG) or Jog mode. Select the faulted axis.
3. **Jog the axis in the positive direction** — Move the axis away from the overtravel position (toward the positive side) until the alarm clears. On most Fanuc controls, the alarm will clear automatically once the axis moves back within the limit boundary.
4. **Perform a reference return** — After recovering the axis, perform a zero return (G28 or the REF return button on the operator panel) to confirm the machine is properly referenced.
5. **Review stored stroke limit parameters** — Navigate to the Parameter screen (typically MDI → System → Param). Review parameters 1320 (positive limit) and 1321 (negative limit) for the affected axis. Adjust if the limit is set incorrectly.
6. **Review the NC program or MDI command** — If the overtravel was caused by a program move, correct the command to stay within the work envelope.
7. **Reset and resume** — After the axis is within limits and properly referenced, reset the alarm via the Reset key and resume operation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| No parts typically required | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-4-overtravel&k=No+parts+typically+required&tag=errorcodefixes-20) \| Alarm 4 is a software limit; recovery is usually parameter or positioning correction |
| Fanuc servo amplifier | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-4-overtravel&k=Fanuc+servo+amplifier&tag=errorcodefixes-20) \| Only if servo fault accompanies the overtravel alarm |
## When to Call a Pro

If the machine repeatedly trips alarm 4 in normal operation after parameter and program correction, the axis position feedback may be drifting due to a faulty encoder or servo drive. Contact a Fanuc-certified service technician for servo system diagnostics.

## Related Articles

- [Fanuc 0i-MD Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-0i-md-alarm-codes/)
- [Fanuc 30i/31i/32i Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-30i-alarm-codes/)
- [Fanuc Alarm 1 Overtravel — Causes & Fix](/posts/fanuc-alarm-1-overtravel/)
- [Fanuc Alarm 10 Servo Alarm — Causes & Fix](/posts/fanuc-alarm-10-servo-alarm/)
- [Fanuc Alarm 2 — Overtravel Plus Causes & Fix](/posts/fanuc-alarm-2-overtravel/)

## See Also

- [Fanuc Alarm 600 — Causes & Fix](/posts/fanuc-alarm-600/)
- [Fanuc Alarm 700 Spindle Overheat — Detailed Fix Guide](/posts/fanuc-alarm-700-spindle/)
- [Fanuc Alarm 360 — APC Alarm Battery Low Causes & Fix](/posts/fanuc-alarm-360/)
- [Fanuc Alarm 430 — Servo Motor Overheat Fix](/posts/fanuc-alarm-430/)
