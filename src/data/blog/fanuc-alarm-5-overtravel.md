---
title: "Fanuc Alarm 5 — Stored Stroke Limit 2 Overtravel"
description: "What Fanuc alarm 5 means, why a stored stroke limit 2 overtravel occurs, and how to recover the axis."
pubDatetime: 2026-04-22T11:00:00Z
modDatetime: 2026-04-22T11:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - fanuc
---

## Fanuc Alarm 5 — What It Means

Fanuc alarm 5 indicates a stored stroke limit 2 overtravel. This is similar to alarm 4 but references the second set of stored stroke limits, which is used to define an inner forbidden zone or a secondary travel boundary on Fanuc Series 0, 10, 11, 15, 16, 18, 21, and 0i controls. Stroke limit 2 is typically set to protect the machine spindle head from colliding with the table or pallet in a specific zone during tool change or pallet exchange operations.

[Jump to Fix](#fix)

## Common Causes

- **Tool change or ATC sequence positioned axis into forbidden zone** — An automatic tool changer or pallet changer commanded an axis move into the zone protected by stroke limit 2.
- **Incorrect stroke limit 2 parameters** — Parameters P1322/P1323 (or equivalent for the control series) define the stroke limit 2 boundaries and may be configured incorrectly after a machine parameter backup/restore.
- **Machine not properly referenced after E-stop** — If the control lost the reference position, it cannot correctly enforce the stroke limit 2 boundaries and may trip prematurely.
- **MDI or program move into the protected zone** — A commanded position entered manually or by the NC program entered the area defined by stroke limit 2.

## Step-by-Step Fix {#fix}

1. **Jog the axis away from the overtravel position** — Switch to Jog or MPG mode. Move the affected axis in the opposite direction from the limit that was exceeded. The alarm typically clears once the axis re-enters the valid zone.
2. **Check which stroke limit zone is active** — On the Fanuc diagnosis screen or the position display, check the current axis position against the stroke limit 2 parameters to understand which boundary was crossed.
3. **Perform a zero return** — After recovering the axis, execute a reference return (REF mode or G28 in MDI) to re-establish the machine zero reference point.
4. **Review parameters for stroke limit 2** — Navigate to the parameter pages and check P1322 and P1323 for the relevant axis. Confirm these correctly define the forbidden zone for your machine configuration.
5. **Review the ATC or pallet change sequence** — If the alarm occurred during an automatic operation, check the macro or ATC sequence logic for a command that moves the axis into the forbidden zone.
6. **Correct the NC program** — If a program move caused the alarm, edit the program to avoid the protected zone or adjust the stroke limit 2 boundaries to correctly reflect the machine's geometry.
7. **Reset and test** — Reset the alarm with the Reset key and run a test cycle to confirm alarm 5 does not recur.

## Parts Often Needed

| Part | Notes |
|------|-------|
| No parts typically required | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-5-overtravel&k=No+parts+typically+required&tag=errorcodefixes-20) \| Alarm 5 is a software boundary fault; recovery is via parameter or program correction |
| Fanuc servo drive or motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-5-overtravel&k=Fanuc+servo+drive+or+motor&tag=errorcodefixes-20) \| Only if position feedback error caused the axis to appear outside limits |
## When to Call a Pro

If alarm 5 occurs in positions that appear to be within the expected travel range, the position feedback system (encoder, linear scale) may be reporting incorrect axis position. Contact a Fanuc-certified technician for encoder and servo drive verification.

## Related Articles

- [Fanuc 0i-MD Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-0i-md-alarm-codes/)
- [Fanuc 30i/31i/32i Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-30i-alarm-codes/)
- [Fanuc Alarm 1 Overtravel — Causes & Fix](/posts/fanuc-alarm-1-overtravel/)
- [Fanuc Alarm 10 Servo Alarm — Causes & Fix](/posts/fanuc-alarm-10-servo-alarm/)
- [Fanuc Alarm 2 — Overtravel Plus Causes & Fix](/posts/fanuc-alarm-2-overtravel/)
