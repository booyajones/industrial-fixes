---
title: "Fujitsu E:13 Error Code - Causes & Fix"
description: "E:13 means outdoor signal abnormality (communication fault). Most common fix: check wiring and connectors between indoor and outdoor units."
pubDatetime: 2026-05-31T01:40:07Z
modDatetime: 2026-05-31T01:40:07Z
author: "Marcus Webb"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - fujitsu
---

## Fujitsu E:13 Error Code — What It Means

The E:13 code on Fujitsu mini-splits indicates an outdoor signal abnormality or communications fault between the indoor and outdoor units. The system cannot exchange control signals correctly, which prevents normal operation. This is primarily a wiring or electrical communication problem, not a refrigerant or mechanical issue. Some third-party sources list E:13 as an indoor fan motor fault, but Fujitsu troubleshooting materials identify it as an outdoor signal communication error.

[Jump to Fix](#fix)

## Common Causes

- **Loose or miswired interconnect wiring** The control wiring between indoor and outdoor units may be disconnected, pinched, crossed, or terminated at the wrong points.
- **Unplugged or corroded connector** Connectors at the external I/O PCB, controller PCB, or molex plugs may be partially seated, corroded, or completely unplugged.
- **Voltage drop or poor ground connection** Insufficient supply voltage or a poor ground can disrupt the low-voltage communication circuit between units.
- **Electrical noise on the circuit** External electrical interference can corrupt the signal traveling between indoor and outdoor boards.
- **Incorrect model match or address configuration** In multi-unit or linked systems, the indoor and outdoor units may be mismatched or have incorrect address settings programmed.
- **Defective control board** If all wiring and voltage checks pass, the main controller PCB or outdoor PCB may have failed internally.

## Step-by-Step Fix {#fix}

1. **Power off the system** at the breaker and wait thirty seconds, then restore power and observe whether the E:13 code returns immediately or only under load.
2. **Inspect all interconnecting wiring** from the indoor air handler to the outdoor condenser for open conductors, pinched insulation, incorrect terminal placement, and reversed polarity.
3. **Check every connector** on the external I/O PCB and controller PCB, including any molex plugs, for looseness, corrosion, or partial seating, and reseat each one firmly.
4. **Verify supply voltage** at the panel, condenser, and evaporator to confirm the system is receiving correct voltage, and look for voltage drop or fluctuations during operation.
5. **Test the ground connection** and inspect for external sources of electrical noise, such as nearby motors or VFDs sharing the circuit.
6. **Confirm system matching and configuration** if you have a multi-unit or linked setup, checking that indoor and outdoor model numbers are compatible and any address switches or settings are correct.
7. **Replace the suspect PCB** (main controller board or outdoor PCB) if all wiring, connectors, voltage, and configuration checks are good, then clear the fault and run a full cycle to verify the repair.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Fujitsu main controller PCB (indoor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-13-error-code&k=Fujitsu+main+controller+PCB+%28indoor%29&tag=errorcodefixes-20) \| Match the exact model and revision number printed on your existing board. |
| Fujitsu outdoor control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-13-error-code&k=Fujitsu+outdoor+control+board+%28PCB%29&tag=errorcodefixes-20) \| Confirm compatibility with your condenser model number before ordering. |
| Control wire (18 AWG, 3-conductor or as specified) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-13-error-code&k=Control+wire+%2818+AWG%2C+3-conductor+or+as+specified%29&tag=errorcodefixes-20) \| Use only if existing interconnect wiring is damaged or undersized. |

## When to Call a Pro

Call a licensed HVAC technician if you are uncomfortable working with line-voltage wiring or low-voltage control circuits, if the fault returns after reseating connectors and checking wiring, or if you lack a multimeter and the experience to trace communication signals between boards. Communication faults can be subtle and may require specialized diagnostic tools to isolate whether the indoor board, outdoor board, or wiring is at fault. Incorrect board replacement or miswiring can damage expensive components and void your warranty.
