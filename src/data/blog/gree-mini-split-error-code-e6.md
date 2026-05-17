---
title: "Gree Mini-Split E6 Error Code — Causes & Fix"
description: "What Gree mini-split E6 error code means, why communication errors trigger between indoor and outdoor units, and how to fix it step by step."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - mini-split
  - gree
---

## Gree Mini-Split E6 Error Code — What It Means

The Gree E6 error code indicates a **communication error between the indoor and outdoor units**. Gree mini-splits use a serial communication line (typically 3-wire: L1, L2/Neutral, and S/Signal) to pass operating data between the indoor and outdoor boards. When the indoor unit stops receiving valid data from the outdoor unit (or vice versa), E6 is stored and the system shuts down. This is one of the most common Gree fault codes and is frequently caused by wiring issues rather than board failures.

[Jump to Fix](#fix)

## Common Causes

- **Loose or miswired communication wire** — The S (signal) wire at the terminal block on either unit backs out or was incorrectly terminated during installation; this is the most common cause.
- **Communication wire damage** — Pinched, cut, or UV-degraded wire between the indoor and outdoor units breaks the signal path.
- **Power supply issue at the outdoor unit** — If the outdoor unit isn't receiving proper voltage, it can't communicate; the indoor unit sees no response and stores E6.
- **Failed indoor or outdoor PCB** — Rarely, the communication circuit on one of the boards fails; wiring and power checks must be eliminated first.

## Step-by-Step Fix {#fix}

1. **Check the communication wire terminal block** — At both the indoor and outdoor units, inspect the 3-terminal (or 4-terminal) connection block. Confirm the S/Signal wire is firmly seated in its terminal and has not backed out. Tighten all terminal screws.
2. **Verify wire labeling** — Confirm L1, L2 (or N), and S are connected to matching terminals on both ends. Miswiring L and S is a common installation error that causes E6.
3. **Inspect the wire run** — Follow the communication cable from indoor to outdoor and look for damage, pinching by the conduit, or UV cracking on exposed sections.
4. **Check outdoor unit power** — Confirm the outdoor unit has proper voltage at its disconnect. If the outdoor unit has no power, it cannot communicate.
5. **Power-cycle both units** — Turn off the breaker for 5 minutes. Restore and allow 2 minutes for the units to exchange startup communication. Check for E6.
6. **Swap S wire terminals** — On some Gree models, the S wire polarity matters. If all connections are secure, try swapping S to the adjacent terminal to rule out a wiring reversal.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Communication wire (3-conductor, 18 AWG) | [Amazon](https://www.amazon.com/s?i=industrial&k=Communication+wire+%283-conductor%2C+18+AWG%29&tag=errorcodefixes-20) \| If the existing wire is damaged; run new wire in conduit |
| Indoor or outdoor PCB | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) \| Only after eliminating all wiring and power causes |
## When to Call a Pro

If all wiring checks out and power is confirmed at both units but E6 persists after a power-cycle, one of the PCBs has a failed communication circuit. Board replacement requires matching the exact Gree model and refrigerant series — use a Gree-authorized service technician to avoid compatibility issues.

## Related Articles

- [Bosch Heat Pump E1 Error Code — Causes & Fix](/posts/bosch-heat-pump-e1-error-code/)
- [Carrier 24ANA Heat Pump Error Codes — Performance Series Diagnostic Guide](/posts/carrier-24ana-heat-pump-error-codes/)
- [Carrier Heat Pump E1 Error Code — Causes & Fix](/posts/carrier-heat-pump-e1-error-code/)
- [Carrier Heat Pump E4 Error Code — Causes & Fix](/posts/carrier-heat-pump-e4-error-code/)
- [Carrier Heat Pump E5 Error Code — Defrost Fault: Causes & Fix](/posts/carrier-heat-pump-e5-error-code/)
