---
title: "Mitsubishi E6 AC Error Code — Causes & Fix"
description: "What Mitsubishi E6 means on AC units specifically, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T08:00:00Z
modDatetime: 2026-04-22T08:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - mini-split
  - mitsubishi
---

## Mitsubishi E6 AC Error Code — What It Means

On Mitsubishi air conditioning units (MSZ-GL, MSZ-GE, MSY, and similar cooling-only models), error code E6 indicates a communication fault between the indoor and outdoor units. The control signal wiring that carries operational commands and feedback between the two units has either lost continuity or is producing signal errors that the outdoor board can't decode. This is distinct from the E6 fault on Mitsubishi heat pump units (which involves refrigerant-side protection in some cases). On dedicated AC models, E6 is almost always a wiring or board communication issue — not a refrigerant problem.

[Jump to Fix](#fix)

## Common Causes

- **Damaged or loose control wiring** — The 3-wire or 4-wire cable connecting indoor to outdoor unit must be intact and firmly terminated. Rodent damage, chafed insulation, or vibration-loosened terminals are common culprits.
- **Incorrect wiring polarity** — If control wires were swapped during installation or a service call, the communication protocol fails and E6 is the result. Verify terminal labels match: S/1, S/2, S/3 or as marked on the outdoor PCB.
- **Failed indoor or outdoor PCB** — If wiring checks out, one of the two control boards has failed. The outdoor PCB is more commonly at fault.
- **EMI interference** — Running control wiring parallel to high-voltage power wiring in the same conduit can inject noise into the communication signal. This causes intermittent E6 on otherwise well-wired installations.

## Step-by-Step Fix {#fix}

1. **Inspect control wiring at both units** — Cut power. Open the outdoor unit control panel and the indoor unit wiring access. Check that each wire is firmly seated in its terminal. Look for any wires that have pulled back, corroded terminals, or signs of pest damage along the run.
2. **Verify wiring order** — Cross-reference your installation manual. Mitsubishi's terminal designations must match exactly: indoor terminal 1 → outdoor terminal 1, and so on. Even one swapped wire causes E6.
3. **Check for wiring damage along the run** — Trace the control cable from indoor to outdoor. Look for pinch points at wall penetrations, conduit entry points, and anywhere the cable runs outdoors and is exposed to UV or animals.
4. **Check for EMI** — If control wiring shares a conduit with 240V supply wiring, separate them. Mitsubishi requires at least 2 inches of separation or shielded cable when routed near power conductors.
5. **Reset the system** — Cut power at the breaker for 3 minutes (long enough for both boards to fully discharge). Restore power and observe. If E6 clears and the unit runs a complete cycle, wiring was the issue.

## Parts Often Needed

| Part | Notes |
|------|-------|
| 3-conductor shielded control cable (18 AWG) | [Amazon](https://www.amazon.com/s?i=industrial&k=3-conductor+shielded+control+cable+%2818+AWG%29&tag=errorcodefixes-20) \| Replace full run if damage is found anywhere along it |
| Outdoor PCB | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) \| If wiring is confirmed good and E6 persists, outdoor board is the next suspect |
| Indoor PCB | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) \| Less commonly the cause, but possible if outdoor board passes self-test |
## When to Call a Pro

If wiring is confirmed intact, polarities are correct, and E6 persists after a full power cycle, board-level diagnosis requires a Mitsubishi-authorized technician with Diamond tool access to read fault history and test communication signals.

## Related Articles

- [Mitsubishi City Multi P8 / E6 Error Codes — Causes & Fix](/posts/mitsubishi-city-multi-error-codes/)
- [Mitsubishi PEX City Multi Error Codes (Indoor Unit): Complete Guide](/posts/mitsubishi-city-multi-pex-error/)
- [Mitsubishi CNC Alarm 500 — Causes & Fix](/posts/mitsubishi-cnc-alarm-500/)
- [Mitsubishi CNC Alarm Y96 — Causes & Fix](/posts/mitsubishi-cnc-alarm-y96/)
- [Mitsubishi E1 Error Code — Indoor/Outdoor Communication Fault Fix](/posts/mitsubishi-e1-error-code/)
