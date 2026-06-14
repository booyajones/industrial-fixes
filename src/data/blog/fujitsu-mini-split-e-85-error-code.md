---
title: "Fujitsu E:85 Error - Causes & Fix"
description: "E:85 signals a communication or DC link fault between indoor and outdoor units. Most often fixed by reseating wiring and connectors."
pubDatetime: 2026-05-31T01:18:46Z
modDatetime: 2026-05-31T01:18:46Z
author: "James Rutherford"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - fujitsu
money_part: "Fujitsu main PCB"
most_likely_cause: "Loose or miswired interconnecting wiring"
---

## Fujitsu E:85 Error — What It Means

The E:85 code on a Fujitsu mini-split indicates a communication or DC link fault in the inverter communication path between your indoor and outdoor units. This means the system has lost the DC voltage and control signals it needs to operate the inverter-controlled compressor and expansion valves. The fault typically appears at start-up when the evaporator and condenser cannot exchange data properly.

This is not a filter alarm or simple sensor issue. It points to a breakdown in the wiring, connectors, or control boards that link the two halves of your system. Without reliable communication, the unit cannot run safely and will shut down to protect itself.

[Jump to Fix](#fix)

## Common Causes

- **Loose or miswired interconnecting wiring** The wiring that runs between indoor and outdoor units is open, pinched, or connected incorrectly, breaking the communication path.
- **Loose or damaged connectors at PCBs** Molex-style plugs at the main PCB, inverter PCB, controller PCB, or external I/O PCB have vibrated loose or corroded over time.
- **Defective main, controller, or inverter PCB** One of the control boards has failed and can no longer generate or receive the DC voltage signals required for communication.
- **Incoming supply voltage out of range** Line voltage to the outdoor unit falls outside the acceptable 187 to 253 VAC window, starving the DC power supply.
- **Indoor unit type mismatch** The connected indoor head or cassette does not match the outdoor unit's configuration table, causing protocol errors.
- **Poor grounding or external voltage drop** Building wiring issues create noise or instability on the communication lines, corrupting signals between units.

## Step-by-Step Fix {#fix}

1. Power off the system completely at the breaker, wait 60 seconds, then restore power and check whether the E:85 returns after a fresh start-up.
2. Measure line voltage at the outdoor unit with a multimeter and confirm it is between 187 and 253 VAC under load during attempted operation.
3. Inspect and re-seat every connector at the indoor unit: pull each Molex plug from the main PCB, controller PCB, and any external I/O PCB, check for corrosion or bent pins, then press firmly back into place.
4. Trace the interconnecting wiring from indoor to outdoor, looking for pinched sheath, nicked insulation, loose wire nuts, or reversed polarity at terminal blocks.
5. Re-seat all connectors at the outdoor unit's inverter PCB and main PCB, then confirm that the indoor unit model matches the pairing table in your installation manual.
6. If wiring and voltage are sound, test or swap the main PCB, controller PCB, and inverter PCB one at a time, starting with the board closest to the error display.
7. After replacing any controller PCB, set the remote-control address per the installation sheet and run a full test cycle to verify communication is restored.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Fujitsu main PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-85-error-code&k=Fujitsu+main+PCB&tag=errorcodefixes-20) \| Match the part number printed on your existing board or consult your model's service manual. |
| Fujitsu controller PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-85-error-code&k=Fujitsu+controller+PCB&tag=errorcodefixes-20) \| Verify compatibility with your indoor unit type before ordering. |
| Fujitsu inverter PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-85-error-code&k=Fujitsu+inverter+PCB&tag=errorcodefixes-20) \| Found in the outdoor unit; make sure the replacement matches your condenser model. |
| Interconnecting wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-85-error-code&k=Interconnecting+wiring+harness&tag=errorcodefixes-20) \| Use only if existing wires are nicked, pinched, or show continuity faults. |

## When to Call a Pro

Call a licensed HVAC technician if you are not comfortable working with line voltage, if you lack a multimeter to verify the 187 to 253 VAC supply range, or if re-seating connectors and inspecting wiring does not clear the fault. Board-level diagnostics and inverter PCB replacement require knowledge of refrigerant handling, low-voltage DC circuits, and Fujitsu's pairing protocols. If your unit is still under warranty, professional service is usually required to preserve coverage. A tech can also verify that grounding and building wiring meet code, which is harder to assess without test equipment.
