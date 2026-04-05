---
title: "Daikin U4 Error Code Fix — Communication Fault"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-09T08:00:00Z
modDatetime: 2024-03-09T08:00:00Z
slug: daikin-u4-error-code
featured: false
draft: false
tags:
  - hvac
  - daikin
  - mini-split
  - communication
  - wiring
description: "Daikin U4 error code means the indoor and outdoor units lost communication. This guide covers wiring checks, board diagnostics, and how to resolve it fast."
---

## Error Code: Daikin U4

**What it means:** U4 is a serial communication failure between the Daikin indoor unit and the outdoor unit. The indoor and outdoor units exchange data continuously over a signal wire. When that data exchange stops — whether due to a wiring fault, a board failure, or a power issue — U4 appears on the indoor unit display and both units shut down.

Unlike a refrigerant or mechanical fault, U4 means the units can no longer "talk" to each other. The fix is nearly always electrical — wiring, power, or boards.

## Common Causes

- **Broken or disconnected signal wire between units** — The F1/F2 communication wires (or S1/S2 on some models) were cut, pinched, or disconnected. This is the most common cause, especially after any construction or pest control work near the linesets.
- **Power issue at the outdoor unit** — If the outdoor unit loses its 220V/240V power supply (tripped breaker, failed disconnect, blown fuse), it can no longer transmit to the indoor unit. The indoor unit sees silence and throws U4.
- **Incorrect wiring at the terminal block** — F1/F2 terminals must match between indoor and outdoor. A single transposed wire eliminates communication entirely.
- **Failed outdoor unit PCB** — The outdoor control board is the communication master in most Daikin systems. A failed board produces U4 on the indoor display even with perfect wiring.
- **Failed indoor PCB** — Less common, but an indoor board that can't receive or process communication signals will also trigger U4.
- **Power surge damage** — A lightning strike or power surge can destroy the communication interface chips on one or both boards while leaving the main power circuits intact.

## Step-by-Step Fix

1. **Check the outdoor unit's power supply first.** Before touching wiring, go to the electrical panel and confirm the outdoor unit breaker is ON and not tripped. At the outdoor unit's local disconnect box, confirm fuses are intact (pull and test with a continuity tester) and the disconnect handle is in the ON position.

2. **Inspect terminal block wiring at both units.** Kill power at the breaker and the disconnect. At the indoor terminal block, identify the F1 and F2 terminals (or 1/2/3 depending on model). At the outdoor terminal block, confirm the matching wires from the communication cable are on the corresponding terminals. If you see F1 at indoor going to F2 at outdoor — that's the problem. Match them correctly.

3. **Check for physical wire damage.** Walk the entire run of the control wire (typically a separate 3–4 conductor cable bundled with the refrigerant lineset). Look for cuts, abrasion, or pinched sections. Pay attention to anywhere the lineset passes through walls, under doors, or is secured with metal staples.

4. **Test continuity on F1 and F2 wires.** With both units powered off and the control wires disconnected at the outdoor terminal block, use a multimeter to measure from F1 at the indoor terminal to the loose F1 wire at the outdoor side. Should show near-zero resistance. Repeat for F2. Any open circuit means wire damage.

5. **Restore power and observe outdoor unit startup.** After confirming wiring is correct and intact, restore power at the breaker and disconnect. Listen for the outdoor unit to start initializing — you should hear contactors engage and the compressor attempting to start within a minute of a heat or cool call. If the outdoor unit does nothing at all, the board or power supply is suspect.

6. **Check outdoor unit for power at the board.** With a multimeter and appropriate safety precautions (or a licensed tech), confirm 240V is reaching the outdoor unit's main terminal block. If power is present at the terminal block but the board doesn't respond, the board has failed.

7. **Power cycle both units.** If wiring is confirmed correct and power is verified, a full power cycle (breaker off for 5 minutes, then on) can clear transient U4 faults caused by momentary signal interruption.

## Parts That May Need Replacement

| Part | Where to Buy | Typical Cost |
|------|-------------|-------------|
| Outdoor main PCB (model-specific, e.g., Daikin 3P355747) | Daikin dealer, HVAC Parts Shop | $200–$500 |
| Indoor main PCB (model-specific) | Daikin dealer, HVAC Parts Shop | $150–$400 |
| Communication wire replacement (14/3 or 14/4) | Home Depot, Lowes | $0.50–$1.50/ft |
| Outdoor disconnect fuse set | Home Depot, Grainger | $5–$15 |

## When to Call a Professional

If power is confirmed at both units, wiring is correct, and U4 persists — you need a tech with Daikin service documentation and a way to read outdoor unit fault memory. Daikin's outdoor units store their own fault codes that aren't displayed on the indoor unit. A U4 on the indoor display can mask a completely different outdoor fault. A licensed Daikin dealer can pull the outdoor fault log and tell you exactly what the outdoor board was thinking when it stopped communicating. Tell the tech: "U4 comm fault, power is verified at both units, wiring checks out at both terminal blocks. I need the outdoor fault code pulled."

> **Pro tip:** On multi-zone Daikin systems, U4 on all indoor units simultaneously is a near-certain sign of an outdoor unit power or board failure. U4 on only one indoor zone points to that zone's communication wire or indoor PCB. This distinction saves hours of diagnostic time.
