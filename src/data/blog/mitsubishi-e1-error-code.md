---
title: "Mitsubishi E1 Error Code — Indoor/Outdoor Communication Fault Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-04-05T08:00:00Z
modDatetime: 2024-04-05T08:00:00Z
slug: mitsubishi-e1-error-code
featured: false
draft: false
tags:
  - hvac
  - mitsubishi
  - mini-split
  - communication
description: "Mitsubishi E1 error code means communication between the indoor and outdoor units has failed. This guide covers diagnosis and fixes for the Mitsubishi mini-split E1 fault."
---

## Error Code: Mitsubishi E1

**What it means:** Mitsubishi error code E1 indicates a communication fault between the indoor and outdoor units. Mitsubishi mini-split systems use a dedicated 2-wire or 3-wire communication bus (typically S1–S2 or S1–S2–S3 depending on the model) to send operational data, commands, and diagnostics between the indoor and outdoor controllers. When the outdoor unit's main PCB does not receive a valid communication signal from the indoor unit — or vice versa — within the expected timeframe, it faults with E1 and shuts down the system. E1 displays on the indoor unit wireless remote display.

## Common Causes

- **Wiring fault in the communication cable** — The communication wire (typically the signal cable between terminal S on both units) is the most common cause. A break, loose connection, incorrect polarity, or wire damaged during installation or by rodents will interrupt communication.
- **Incorrect wiring configuration** — Multi-zone systems with incorrect S-terminal wiring cause persistent E1. Each indoor unit in a multi-zone system must be wired to the outdoor unit's corresponding zone terminals.
- **Failed indoor PCB** — The indoor unit's control board generates the communication signal. A failed indoor PCB produces no signal, causing E1.
- **Failed outdoor main PCB** — Less common, but the outdoor board can also fail to receive or interpret the signal.
- **Power supply issue** — If either unit loses its 24V or 5V logic supply (often from the main power board), communication circuits fail.

## Diagnosis Steps

1. Power off both units completely for 30 seconds. Restore power and wait 3 minutes for the system to initialize. If E1 clears, the fault was transient — monitor for recurrence.
2. Inspect the communication wire connections at both the indoor and outdoor unit terminals. The signal wire connects to terminals labeled S or Signal on both units. Verify the wire is fully seated and the terminal screws are tight.
3. Check the communication wire for damage: inspect the full run for cuts, pinch points, or rodent damage. On multi-zone systems, verify each indoor unit's S-terminal connects to the correct outdoor unit zone terminal.
4. Use a multimeter to measure resistance between the S1 and S2 terminals at the outdoor unit with both units powered off. A short circuit (near 0 ohms) or open circuit (OL) on the signal wire indicates a wiring fault.
5. If wiring is correct and intact, power up the system and measure 24V DC or 12V DC (depending on model) on the signal wire while the system attempts startup. No voltage indicates a failed indoor PCB.

## Fix

Reconnect or replace the communication cable if damaged. Mitsubishi systems use shielded control cable for the signal wire in some commercial applications — use the same wire type as the original installation.

If wiring checks out, the fault is in a PCB. The indoor PCB is more commonly at fault than the outdoor in E1 scenarios. Mitsubishi PCBs are model-specific — order by the indoor unit model number. On multi-zone systems, swap the suspected indoor board and confirm the fault clears.

## Parts

| Part | Where to Buy |
|------|-------------|
| [Communication / control cable (per foot)](https://www.amazon.com/s?k=Communication%20%2F%20control%20cable%20(per%20foot)&tag=errorcodefixe-20) | Grainger, Amazon |
| [Indoor unit main PCB](https://www.amazon.com/s?k=Indoor%20unit%20main%20PCB&tag=errorcodefixe-20) | SupplyHouse, Grainger |
| [Outdoor main PCB](https://www.amazon.com/s?k=Outdoor%20main%20PCB&tag=errorcodefixe-20) | SupplyHouse, Grainger |

## When to Call a Technician

E1 on a multi-zone Mitsubishi system with multiple indoor units can be complex to isolate — a licensed HVAC tech with a Mitsubishi service analyzer (ME Remote or equivalent) can read fault history from each unit and isolate the failed board faster than visual inspection alone.
