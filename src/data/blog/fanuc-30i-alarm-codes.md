---
title: "Fanuc 30i/31i/32i Alarm Code Guide — Complete Diagnostic Reference"
description: "Complete guide to Fanuc 30i, 31i, and 32i CNC alarm codes, meanings, causes, and first-step troubleshooting procedures."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - fanuc
  - industrial
---

## Fanuc 30i/31i/32i Alarm Codes — What They Mean

The Fanuc 30i, 31i, and 32i controls are higher-end CNC platforms used on multi-axis machining centers, lathes, grinders, and complex OEM systems. These controls generate alarms from multiple layers, including CNC kernel, servo, spindle, PMC, and machine builder ladder logic. The same numeric alarm can have different practical causes depending on the machine builder implementation.

[Jump to Fix](#fix)

## Common Fanuc 30i/31i/32i Alarm Reference

| Alarm | Meaning |
|---|---|
| 100 | Parameter error |
| 300 | Emergency stop |
| 350 | I/O link communication fault |
| 401 | Servo alarm — VRDY off |
| 409 | Spindle serial link fault |
| 414 | Servo alarm detail |
| 436 | Zero position return fault |
| 500 | Servo overcurrent |
| 700 | Spindle alarm |
| 750 | Serial pulse coder alarm |
| 911 | SRAM error |
| 920 | Servo parameter mismatch |

## Common Causes by Alarm

- **350 I/O link** — Remote I/O rack offline, fiber/cable fault, or power loss to the I/O module.
- **409 spindle serial link** — Communication loss between CNC and spindle amplifier.
- **436 zero return** — Encoder reference lost, zero return dog out of position, or parameter change.
- **920 parameter mismatch** — Servo amplifier or motor changed without matching parameters.
- **911 SRAM** — Memory corruption or battery issue. Immediate backup is critical.

## Step-by-Step Fix {#fix}

1. **Capture all alarm text and amplifier LEDs** — Fanuc diagnostics require both the CNC alarm and amplifier-side indication.
2. **For 350** — Verify remote I/O power, cabling, and diagnostic LEDs at each I/O node.
3. **For 409** — Check spindle amplifier power, serial cable seating, and builder-specific spindle interface boards.
4. **For 436** — Re-home the axis after inspecting zero return dog and encoder reference.
5. **For 920/911** — Stop making changes, back up parameters, and compare against a known-good machine backup.

## Parts Often Needed

| Part | Notes |
|---|---|
| Encoder battery | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-30i-alarm-codes&k=Encoder+battery&tag=errorcodefixes-20) \| Prevents position loss |
| I/O link cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-30i-alarm-codes&k=I%2FO+link+cable&tag=errorcodefixes-20) \| Common issue in harsh cabinets |
| Servo amplifier | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-30i-alarm-codes&k=Servo+amplifier&tag=errorcodefixes-20) \| For persistent VRDY/overcurrent faults |
| Spindle interface board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-30i-alarm-codes&k=Spindle+interface+board&tag=errorcodefixes-20) \| OEM dependent |
## When to Call a Pro

These controls often run on high-value production equipment. Repeated 911, 920, or spindle serial alarms justify immediate involvement from a Fanuc-trained technician or the machine builder because incorrect recovery can cost parameters, offsets, and machine geometry.

## Related Articles

- [Fanuc 0i-MD Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-0i-md-alarm-codes/)
- [Fanuc Alarm 1 Overtravel — Causes & Fix](/posts/fanuc-alarm-1-overtravel/)
- [Fanuc Alarm 10 Servo Alarm — Causes & Fix](/posts/fanuc-alarm-10-servo-alarm/)
- [Fanuc Alarm 2 — Overtravel Plus Causes & Fix](/posts/fanuc-alarm-2-overtravel/)
- [Fanuc Alarm 3 — Overtravel Minus Hardware Causes & Fix](/posts/fanuc-alarm-3-overtravel/)
