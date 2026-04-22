---
title: "Heidenhain TNC 640 Error Code Guide — Complete Diagnostic Reference"
description: "Complete guide to Heidenhain TNC 640 error codes, meanings, causes, and first-step troubleshooting procedures for CNC technicians."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - cnc
  - heidenhain
  - industrial
---

## Heidenhain TNC 640 Error Codes — What They Mean

The Heidenhain TNC 640 is a premium CNC control used on advanced 5-axis milling and mill-turn platforms. Heidenhain alarms are highly specific, but they still fall into a few broad categories: axis referencing, encoder feedback, drive faults, PLC/safety faults, and program logic problems. The exact alarm text on screen matters as much as the number.

[Jump to Fix](#fix)

## Common Heidenhain TNC 640 Alarm Reference

| Alarm | Meaning |
|---|---|
| 100 | PLC not ready |
| 115 | Axis enable missing |
| 130 | Reference mark not found |
| 200 | Drive fault |
| 399 | Servo or drive communication issue |
| 601 | Spindle fault |
| 710 | Encoder signal fault |
| 740 | Power interruption / control voltage issue |

## Common Causes by Alarm

- **100 PLC not ready** — Safety chain or PLC startup issue. The control is waiting for a machine-ready signal.
- **130 reference mark** — Axis has not crossed the encoder reference mark, home switch is defective, or axis movement is blocked.
- **399 drive communication** — Commonly seen when a drive module loses communication or powers down unexpectedly.
- **710 encoder fault** — Encoder cable damage, contamination, or failed measuring system.
- **740 power interruption** — Loose control transformer connection or unstable supply.

## Step-by-Step Fix {#fix}

1. **Record the exact alarm text** — Heidenhain messages are descriptive and often point directly to the subsystem.
2. **For 100/115** — Check safety relays, axis enable contactors, and machine-ready PLC bits.
3. **For 130** — Inspect reference switches and confirm axis can move freely to the reference point.
4. **For 399/710** — Check encoder and drive connectors for contamination and looseness.
5. **For 740** — Verify control voltage and inspect transformer and power supply terminals.

## Parts Often Needed

| Part | Notes |
|---|---|
| Encoder cable | Common wear/failure item |
| Reference switch | For repeated homing issues |
| Control power supply | For unstable control voltage |
| Drive module | Only after connector and supply checks |

## When to Call a Pro

The TNC 640 is usually found on expensive multi-axis equipment. Persistent drive and encoder faults should go to a Heidenhain-trained technician or the machine builder, especially if machine geometry or kinematics are involved.
