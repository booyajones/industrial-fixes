---
title: "Fanuc Alarm 750 — Causes & Fix"
description: "What Fanuc CNC alarm 750 means, why the spindle serial link errors, and how to fix it."
pubDatetime: 2026-04-22T10:00:00Z
modDatetime: 2026-04-22T10:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - fanuc
---

## Fanuc Alarm 750 — What It Means

Alarm 750 on a Fanuc CNC (FS0i, FS16i, FS18i, FS21i, FS30i) is a Spindle Serial Link Disconnect alarm. The CNC control cannot communicate with the spindle amplifier (SPM — Spindle Power Module) over the FSSB (Fanuc Serial Servo Bus) or JYA/JYB optical communication cable. When this serial link drops, the CNC loses all spindle control and feedback and immediately alarms.

[Jump to Fix](#fix)

## Common Causes

- **Damaged or loose optical fiber communication cable** — The JYA or JYB optical cable between the CNC main board and the spindle amplifier is fragile. A cracked, bent, or dirty fiber end causes communication errors.
- **Failed spindle amplifier (SPM)** — The SPM's communication card can fail, stopping it from responding to the CNC serial bus.
- **CNC main board communication failure** — The serial spindle output on the main CPU board can fail, causing the drive to report a serial disconnect from the CNC side.
- **Power supply issues to the SPM** — If the SPM loses its control power (24VDC) or its main AC input, it cannot participate in serial communication.

## Step-by-Step Fix {#fix}

1. **Inspect the JYA/JYB optical communication cables** — Locate the fiber optic cables connecting the CNC control cabinet to the spindle amplifier. Check both ends for:
   - Cracked or broken plastic fiber
   - Dirty connector ends (clean with IPA and a lint-free swab)
   - Loose plug connections (reseat firmly)
2. **Check SPM LED status** — Fanuc spindle amplifiers have a 7-segment or LED status display. A unit without power or with an active fault shows a specific code. No display = no power; check the 24VDC supply and MCC (main circuit) input to the SPM.
3. **Verify SPM control power** — Check 24VDC at the SPM CX1A connector. If absent, trace back to the 24VDC control power supply in the cabinet.
4. **Swap known-good communication cable** — If available, substitute the JYA/JYB cable with a known-good cable to rule out cable failure.
5. **Replace the spindle amplifier** — If the cable and power are confirmed good but alarm 750 persists, the SPM's communication card is likely failed. Replace the SPM with an OEM unit and re-parameterize.

## Parts Often Needed

| Part | Notes |
|------|-------|
| JYA/JYB optical fiber cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-750&k=JYA%2FJYB+optical+fiber+cable&tag=errorcodefixes-20) \| Fanuc OEM; do not substitute standard fiber patch cables |
| Spindle amplifier (SPM) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-750&k=Spindle+amplifier+%28SPM%29&tag=errorcodefixes-20) \| Must match Fanuc model and revision |
| 24VDC control power supply | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-750&k=24VDC+control+power+supply&tag=errorcodefixes-20) \| Replace if output is absent or out of tolerance |
## When to Call a Pro

Fanuc spindle amplifier replacement requires re-entering spindle motor parameters (SP parameters) from the backup or machine documentation. This work should be performed by a Fanuc-authorized service technician to avoid incorrect parameterization causing motor or amplifier damage.

## Related Articles

- [Fanuc 0i-MD Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-0i-md-alarm-codes/)
- [Fanuc 30i/31i/32i Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-30i-alarm-codes/)
- [Fanuc Alarm 1 Overtravel — Causes & Fix](/posts/fanuc-alarm-1-overtravel/)
- [Fanuc Alarm 10 Servo Alarm — Causes & Fix](/posts/fanuc-alarm-10-servo-alarm/)
- [Fanuc Alarm 2 — Overtravel Plus Causes & Fix](/posts/fanuc-alarm-2-overtravel/)

## See Also

- [Fanuc Alarm 2 — Overtravel Plus Causes & Fix](/posts/fanuc-alarm-2-overtravel/)
- [Fanuc Alarm 600 — Causes & Fix](/posts/fanuc-alarm-600/)
- [Fanuc Alarm 414 — Servo Axis Following Error Fix](/posts/fanuc-alarm-414/)
- [Fanuc Alarm 437 — Servo Following Error 4th Axis Causes & Fix](/posts/fanuc-alarm-437/)
