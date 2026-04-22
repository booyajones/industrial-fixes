---
title: "Daikin U4 Error Code — Causes & Fix"
description: "What Daikin U4 error code means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - daikin
---

## Daikin U4 Error Code — What It Means

Daikin error code U4 indicates a communication fault between the indoor unit and the outdoor unit. On Daikin split and VRV/VRF systems, U4 typically means the outdoor unit stopped receiving valid serial communication from the indoor unit (or vice versa), and the system has shut down to prevent operating in an undefined state. This is different from the refrigerant-related U4 on some older Daikin VRV systems — the specific meaning varies slightly by model family, so confirm against the unit's technical manual. On most residential and light-commercial Daikin units, U4 = communication failure.

[Jump to Fix](#fix)

## Common Causes

- **Damaged or loose communication wiring** — The S/S, S1/S2, or F1/F2 communication terminals on the indoor or outdoor unit have a loose wire, corroded terminal, or broken conductor. These small-gauge wires are vulnerable to mechanical damage.
- **Power supply issue at outdoor unit** — If the outdoor unit loses its independent power feed or a breaker trips, it can no longer respond to indoor unit communication, generating U4 at the indoor unit.
- **Shielding or grounding fault** — On longer wire runs, an ungrounded or improperly shielded communication cable picks up electrical noise that corrupts the serial signal.
- **Failed indoor or outdoor control PCB** — After a power surge or extended moisture exposure, the communication transceiver on one of the PCBs may fail, preventing the handshake from completing.

## Step-by-Step Fix {#fix}

1. **Check power to the outdoor unit** — Confirm the outdoor unit's breaker or disconnect is on and the unit has voltage at the terminal block. A tripped breaker or blown fuse eliminates outdoor unit communication.
2. **Inspect F1/F2 (or S1/S2) terminals at both units** — Shut off both units. Remove the covers and locate the low-voltage terminal strip. Confirm communication wires are seated under their respective terminals and not corroded.
3. **Test wire continuity** — Use a multimeter to verify the communication wire has continuity end-to-end and no short to ground. Replace the full run if damaged.
4. **Power cycle both units in the correct order** — Restore outdoor unit power first, wait 2 minutes, then restore indoor unit power. This ensures the outdoor unit initializes before the indoor unit begins polling for communication.
5. **Check for additional fault codes on outdoor PCB** — Pull the outdoor unit service cover and look at the diagnostic LED on the control board. An independent fault on the outdoor board (e.g., fan motor, refrigerant pressure) may be the real cause and U4 is secondary.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Communication cable (shielded 2-wire) | Replace entire run; field splices cause intermittent faults |
| Indoor PCB | Replace if confirmed failed after eliminating wiring issues |
| Outdoor PCB | Replace if outdoor board damaged by surge; confirm with Daikin diagnostic tool |

## When to Call a Pro

If replacing the communication wire doesn't clear U4 and both unit boards appear functional, the fault may require Daikin's Intelligent Touch Controller or a manufacturer diagnostic tool to read fault history and confirm which unit is the communication initiator vs. responder. This diagnosis is best handled by a Daikin-certified technician.
