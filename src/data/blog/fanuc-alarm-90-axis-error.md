---
title: "Fanuc Alarm 90 — Causes & Fix"
description: "What Fanuc alarm 90 reference return incomplete means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - fanuc
---

## Fanuc Alarm 90 — What It Means

Fanuc alarm 90 (SV0090: REFERENCE RETURN INCOMPLETE) indicates that an axis required to complete reference return (home position) failed to reach its reference point within the allowed stroke or within the expected signal sequence. Most Fanuc CNCs require a reference return (G28 or manual reference operation) after power-on before they will allow automatic cycle operation. Alarm 90 fires when the CNC commanded a reference return and either the deceleration dog signal was never seen, the reference position signal never appeared, or the axis hit a travel limit before the reference point was found.

[Jump to Fix](#fix)

## Common Causes

- **Reference return deceleration dog missing or mispositioned** — The deceleration dog (a physical cam or bracket that triggers the decel LS) has come loose, shifted, or been removed. Without the decel signal, the axis overshoots the reference point and hits a limit.
- **Grid shift parameter set incorrectly** — The reference position grid shift parameter (Fanuc parameter 1850) is set to a value that moves the reference position outside the valid axis travel range.
- **Servo encoder pulse count error** — A noisy encoder, a damaged cable, or a grounding issue causes the CNC to miss the encoder reference mark (Z-pulse), and the reference position is never confirmed.
- **Axis starts reference return from a position too close to the reference point** — If the axis is very close to or past the deceleration dog when reference return is commanded, the deceleration signal logic may be missed. Jog the axis away before re-attempting.

## Step-by-Step Fix {#fix}

1. **Check the position of the reference return decel dog** — Open the machine enclosure and locate the deceleration dog for the faulting axis. It is typically a metal tab or cam mounted on the table or saddle that contacts a limit switch at a specific position. Confirm it is properly positioned and secured.
2. **Jog the axis away from the reference position** — Before re-attempting reference return, jog the axis 50–100mm away from the reference area in the positive direction to ensure the deceleration sequence can occur properly.
3. **Attempt reference return in JOG mode at slow feedrate** — Use the REF RETURN or ZRN mode on the operator panel. Watch for the decel signal in the PMC diagnostic screen (Fanuc ladder monitor: decel signal should go high when the dog is contacted).
4. **Check encoder cable and connector** — Power off the machine and inspect the encoder cable between the servo motor and the CNC. Check for cable damage, bent connector pins, and secure strain relief. Poor encoder connections are a leading cause of reference position loss.
5. **Review parameter 1850 (reference position grid shift)** — In the Fanuc parameter screen, check parameter 1850 for the affected axis. If this was recently changed, restore to the previous value or set to 0 and re-establish reference position from scratch.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Reference deceleration limit switch | [Amazon](https://www.amazon.com/dp/B0BN3TRG9R?tag=errorcodefixes-20) \| Replace if contacts are worn or switch is physically damaged |
| Encoder cable | [Amazon](https://www.amazon.com/s?i=industrial&k=Encoder+cable&tag=errorcodefixes-20) \| Replace if continuity check reveals open or intermittent conductors |
| Absolute encoder battery | [Amazon](https://www.amazon.com/s?i=industrial&k=Absolute+encoder+battery&tag=errorcodefixes-20) \| On absolute encoder systems, a dead battery causes position data loss and reference faults |
## When to Call a Pro

If the decel dog is properly positioned, the encoder cable is intact, and the CNC still fails to find the reference position, the servo encoder itself may need replacement or recalibration. This requires Fanuc parameter adjustment and machine geometry verification by a certified technician.

## Related Articles

- [Fanuc 0i-MD Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-0i-md-alarm-codes/)
- [Fanuc 30i/31i/32i Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-30i-alarm-codes/)
- [Fanuc Alarm 1 Overtravel — Causes & Fix](/posts/fanuc-alarm-1-overtravel/)
- [Fanuc Alarm 10 Servo Alarm — Causes & Fix](/posts/fanuc-alarm-10-servo-alarm/)
- [Fanuc Alarm 2 — Overtravel Plus Causes & Fix](/posts/fanuc-alarm-2-overtravel/)
