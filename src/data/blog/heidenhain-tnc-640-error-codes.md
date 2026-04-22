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

| [Alarm](https://www.amazon.com/s?k=Alarm&tag=errorcodefixe-20) | Meaning |
|---|---|
| [100](https://www.amazon.com/s?k=100&tag=errorcodefixe-20) | PLC not ready |
| [115](https://www.amazon.com/s?k=115&tag=errorcodefixe-20) | Axis enable missing |
| [130](https://www.amazon.com/s?k=130&tag=errorcodefixe-20) | Reference mark not found |
| [200](https://www.amazon.com/s?k=200&tag=errorcodefixe-20) | Drive fault |
| [399](https://www.amazon.com/s?k=399&tag=errorcodefixe-20) | Servo or drive communication issue |
| [601](https://www.amazon.com/s?k=601&tag=errorcodefixe-20) | Spindle fault |
| [710](https://www.amazon.com/s?k=710&tag=errorcodefixe-20) | Encoder signal fault |
| [740](https://www.amazon.com/s?k=740&tag=errorcodefixe-20) | Power interruption / control voltage issue |

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
| [Encoder cable](https://www.amazon.com/s?k=Encoder%20cable&tag=errorcodefixe-20) | Common wear/failure item |
| [Reference switch](https://www.amazon.com/s?k=Reference%20switch&tag=errorcodefixe-20) | For repeated homing issues |
| [Control power supply](https://www.amazon.com/s?k=Control%20power%20supply&tag=errorcodefixe-20) | For unstable control voltage |
| [Drive module](https://www.amazon.com/s?k=Drive%20module&tag=errorcodefixe-20) | Only after connector and supply checks |

## When to Call a Pro

The TNC 640 is usually found on expensive multi-axis equipment. Persistent drive and encoder faults should go to a Heidenhain-trained technician or the machine builder, especially if machine geometry or kinematics are involved.
