---
title: "Fanuc 30i/31i/32i Alarm Code Guide — Complete Diagnostic Reference"
description: "Complete guide to Fanuc 30i, 31i, and 32i CNC alarm codes, meanings, causes, and first-step troubleshooting procedures."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "ErrorCodeFixes"
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

| [Alarm](https://www.amazon.com/s?k=Alarm&tag=errorcodefixe-20) | Meaning |
|---|---|
| [100](https://www.amazon.com/s?k=100&tag=errorcodefixe-20) | Parameter error |
| [300](https://www.amazon.com/s?k=300&tag=errorcodefixe-20) | Emergency stop |
| [350](https://www.amazon.com/s?k=350&tag=errorcodefixe-20) | I/O link communication fault |
| [401](https://www.amazon.com/s?k=401&tag=errorcodefixe-20) | Servo alarm — VRDY off |
| [409](https://www.amazon.com/s?k=409&tag=errorcodefixe-20) | Spindle serial link fault |
| [414](https://www.amazon.com/s?k=414&tag=errorcodefixe-20) | Servo alarm detail |
| [436](https://www.amazon.com/s?k=436&tag=errorcodefixe-20) | Zero position return fault |
| [500](https://www.amazon.com/s?k=500&tag=errorcodefixe-20) | Servo overcurrent |
| [700](https://www.amazon.com/s?k=700&tag=errorcodefixe-20) | Spindle alarm |
| [750](https://www.amazon.com/s?k=750&tag=errorcodefixe-20) | Serial pulse coder alarm |
| [911](https://www.amazon.com/s?k=911&tag=errorcodefixe-20) | SRAM error |
| [920](https://www.amazon.com/s?k=920&tag=errorcodefixe-20) | Servo parameter mismatch |

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
| [Encoder battery](https://www.amazon.com/s?k=Encoder%20battery&tag=errorcodefixe-20) | Prevents position loss |
| [I/O link cable](https://www.amazon.com/s?k=I%2FO%20link%20cable&tag=errorcodefixe-20) | Common issue in harsh cabinets |
| [Servo amplifier](https://www.amazon.com/s?k=Servo%20amplifier&tag=errorcodefixe-20) | For persistent VRDY/overcurrent faults |
| [Spindle interface board](https://www.amazon.com/s?k=Spindle%20interface%20board&tag=errorcodefixe-20) | OEM dependent |

## When to Call a Pro

These controls often run on high-value production equipment. Repeated 911, 920, or spindle serial alarms justify immediate involvement from a Fanuc-trained technician or the machine builder because incorrect recovery can cost parameters, offsets, and machine geometry.
