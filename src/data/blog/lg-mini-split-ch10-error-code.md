---
title: "LG Mini Split CH10 Error Code — Causes & Fix"
description: "What LG CH10 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T08:00:00Z
modDatetime: 2026-04-22T08:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - mini-split
  - lg
---

## LG Mini Split CH10 Error Code — What It Means

LG error code CH10 (or "C10") indicates a communication error between the indoor and outdoor units. LG mini-splits use a serial communication bus (the S-terminal or communication wire) to pass operational data between the two boards. When the indoor unit stops receiving valid data packets from the outdoor unit for more than a few seconds, it triggers CH10 and halts operation. This fault can appear on both single-zone and multi-zone LG systems. On multi-zone systems, it may affect only one indoor unit if that unit's communication line is the problem.

[Jump to Fix](#fix)

## Common Causes

- **Loose or disconnected communication wire** — The S or communication terminal at either the indoor or outdoor PCB is the first place to check. A wire that has backed out of its terminal due to vibration causes intermittent or persistent CH10.
- **Incorrect wiring during installation** — If the communication wire is connected to the wrong terminal or if the L1/L2/S wires are mixed, CH10 appears at first startup.
- **Power loss to outdoor unit** — If the outdoor unit lost power (tripped breaker, blown fuse, failed disconnect), the indoor unit loses communication and logs CH10. This is one of the most common causes.
- **Failed outdoor PCB** — A dead outdoor control board stops communicating. If the outdoor fan and compressor are both inoperative, the board is suspect.

## Step-by-Step Fix {#fix}

1. **Check outdoor unit power** — Go to the outdoor unit disconnect or breaker panel. Verify the circuit breaker hasn't tripped. If tripped, reset once and observe.
2. **Inspect communication wiring** — At both the indoor unit terminal board and the outdoor unit terminal board, confirm the communication wire (marked S, 3, or COM depending on model) is firmly seated. Loose wires are the most common cause.
3. **Verify wiring order** — Cross-reference terminals: indoor L1 → outdoor L1, indoor L2 → outdoor L2, indoor S → outdoor S. Confirm no wires are swapped.
4. **Check outdoor unit activity** — When you call for cooling or heating, does the outdoor fan try to start? Any sign of life from the outdoor unit (compressor hum, fan movement) suggests the board is alive and the issue may be in the communication line only.
5. **Reset the system** — Cut power at the breaker serving both units for 5 minutes. Restore. If CH10 clears and both units operate, the fault was transient — possibly a power glitch.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Communication wire (18 AWG, 3-conductor)](https://www.amazon.com/s?k=Communication%20wire%20(18%20AWG%2C%203-conductor)&tag=errorcodefixe-20) | Replace full run if damage is found |
| [Outdoor PCB](https://www.amazon.com/s?k=Outdoor%20PCB&tag=errorcodefixe-20) | LG part numbers are model-specific; confirm before ordering |
| [Outdoor disconnect fuse](https://www.amazon.com/s?k=Outdoor%20disconnect%20fuse&tag=errorcodefixe-20) | Check if outdoor unit has no power at all |

## When to Call a Pro

Persistent CH10 after verified correct wiring and confirmed outdoor power requires board-level testing. An LG-authorized tech can read fault history and test communication bus voltage directly.
