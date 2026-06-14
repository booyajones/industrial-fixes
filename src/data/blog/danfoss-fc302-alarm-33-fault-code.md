---
title: "Danfoss FC302 ALARM 33 - Causes & Fix"
description: "Danfoss FC302 ALARM 33 (Inrush fault) means too many power-ups in a short time. Learn causes, diagnostic steps, and fixes."
pubDatetime: 2026-05-29T09:49:09Z
modDatetime: 2026-05-29T09:49:09Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "DC-link capacitor bank (for FC302 frame size)"
most_likely_cause: "Excessive cycling of incoming power"
---

## Danfoss FC302 ALARM 33 — What It Means

ALARM 33 on a Danfoss VLT AutomationDrive FC 301/302 is defined by the manufacturer as an Inrush fault, meaning too many power-ups have occurred within a short time. The drive detects repeated inrush events during charging of the DC link and trips to protect the internal power section.

In practical terms, something is causing the drive to cycle on and off rapidly instead of staying powered through a normal startup. The fault is not about a single component failure but about repeated charging cycles that exceed the drive's allowed sequence.

[Jump to Fix](#fix)

## Common Causes

- **Excessive cycling of incoming power** A control scheme or upstream device is repeatedly turning the drive on and off in short intervals.
- **DC-link fault to ground** An internal short or ground fault in the DC bus section triggers repeated startup attempts.
- **Unstable supply voltage** Incoming power interruptions or sags cause the drive to restart its charge cycle multiple times.
- **Control logic cycling the drive unnecessarily** PLC or relay logic is not allowing the drive to complete normal startup before cutting power again.

## Step-by-Step Fix {#fix}

1. Verify the operating history by checking logs or asking operators whether the unit has been power-cycled repeatedly in the last few minutes.
2. Let the drive sit powered off for at least 10 minutes to allow the DC link to discharge and internal components to settle if thermal stress is present.
3. Check for a DC-link fault to ground by measuring resistance from the DC bus terminals to ground with all power removed and the drive fully discharged.
4. Inspect incoming power and control wiring to confirm no external relay, contactor, or PLC is cycling the drive's main supply unnecessarily.
5. Review control logic and interlock settings to make sure the drive is allowed to complete a full startup before any shutdown command is issued.
6. Reset the fault using the drive keypad or control interface and retest with a single, clean power-up cycle.
7. Monitor the drive through several normal starts. If ALARM 33 returns with proper power-up behavior and no external cycling, treat it as an internal power-section fault and proceed to board-level diagnosis or contact factory service.

## Parts Often Needed

| Part | Notes |
|------|-------|
| DC-link capacitor bank (for FC302 frame size) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-33-fault-code&k=DC-link+capacitor+bank+%28for+FC302+frame+size%29&tag=errorcodefixes-20) \| Required if internal DC-link fault to ground is confirmed and capacitors are shorted or degraded. |
| Power section / IGBT module (FC302 frame-specific) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-33-fault-code&k=Power+section+%2F+IGBT+module+%28FC302+frame-specific%29&tag=errorcodefixes-20) \| Needed if repeated alarms persist after external cycling causes are corrected and DC-link fault is isolated. |

## When to Call a Pro

Call a qualified drive technician or contact Danfoss service if the alarm returns after you have confirmed no external cycling, allowed proper cool-down time, and verified stable incoming power. Persistent ALARM 33 with normal power-up behavior points to an internal DC-link or power-section fault that requires board-level diagnosis, high-voltage testing, and possibly factory repair. Do not attempt internal power-section work without proper training and discharge procedures.

## See Also

- [Danfoss FC302 Alarm 39 - Causes & Fix](/posts/danfoss-fc302-alarm-39-fault-code/)
- [Danfoss FC302 Alarm 34 - Causes & Fix](/posts/danfoss-fc302-alarm-34-fault-code/)
- [Danfoss FC302 Alarm 23 - Causes & Fix](/posts/danfoss-fc302-alarm-23-fault-code/)
- [Danfoss FC302 Complete Fault Code Guide — All Faults and Fixes](/posts/danfoss-fc302-complete-guide/)
