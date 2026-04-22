---
title: "Fanuc Alarm 800: APC Alarm — Causes and Fix"
description: "Fanuc Alarm 800 APC alarm: absolute pulse coder fault causes, diagnostic steps, and reset procedures for Fanuc 0i, 16i, 18i, 30i, and 31i systems."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - fanuc
  - cnc
  - alarm-800
  - apc
  - encoder
---

## Fanuc Alarm 800: APC Alarm

**Alarm Message:** APC ALARM 800  
**Full Display:** 800 APC ALARM: X AXIS or similar per axis  
**Affected Systems:** Fanuc 0i, 16i, 18i, 30i, 31i, and others with absolute encoders

The 800-series APC alarms relate to the Absolute Pulse Coder (APC) — Fanuc's absolute position encoder. These alarms indicate the encoder cannot communicate position data to the servo amplifier.

## APC Alarm 800 Sub-Codes

| Alarm | Meaning |
|-------|---------|
| 300 | APC alarm: battery voltage 0 |
| 302 | APC alarm: communication error |
| 303 | APC alarm: absolute position lost |
| 304 | APC alarm: absolute position not set |
| 305 | APC alarm: rotation count lost |
| 307 | APC alarm: battery voltage too low |
| 360 | APC alarm: APC fault |

## Most Common Cause: Battery Failure

APC encoders use a backup battery to maintain position data when the machine is powered off. When this battery fails:
- Alarm 300 or 307 — battery voltage low or zero
- After replacing the battery, the machine must be re-referenced (zero return)

**Battery location:** Usually in the electrical cabinet or on the servo amplifier itself. On some machines, each axis has its own battery. Check your machine tool builder documentation for exact location.

**Battery type:** Fanuc uses A98L-0031-0005 (3.6V lithium) or similar. Always replace with the specified Fanuc battery — third-party batteries may cause re-alarm.

## Alarm 302 — Communication Error

The APC serial communication between the encoder and the servo amplifier is interrupted. Check:
1. Encoder cable continuity — from encoder to amplifier
2. Connector seating at both ends (encoder and amplifier)
3. Cable shielding — a broken shield allows EMI interference
4. Servo amplifier encoder interface — check for damage on the port

## Alarm 303/304 — Position Lost / Not Set

The encoder lost its absolute position reference. This occurs after battery failure. After replacing the battery, perform a zero return (reference return) on the affected axis per your machine's procedure. The position is re-established on reference return.

## Zero Return Procedure (After Battery Replacement)

1. Replace battery with machine power OFF
2. Power on machine
3. Acknowledge the APC alarm
4. Perform manual zero return (REF operation) on all affected axes
5. Confirm position display matches expected machine zero

## Parts Often Needed

| Part | Notes |
|------|-------|
| Fanuc A98L-0031-0005 battery | 3.6V lithium, use Fanuc OEM |
| Encoder cable | Replace if comm error persists after battery |
| Servo amplifier (SVM) | Only if interface card confirmed damaged |

## Jump to Fix

- **Battery alarm (300/307)** → Replace battery → Re-reference axes
- **Comm error (302)** → Inspect cable → Check connectors → Re-reference
- **Position lost (303/304)** → Replace battery if needed → Perform zero return

## When to Call a Pro
APC encoder replacement on servo motors requires motor removal and precise assembly. Contact your machine tool builder or a Fanuc-certified service provider.
