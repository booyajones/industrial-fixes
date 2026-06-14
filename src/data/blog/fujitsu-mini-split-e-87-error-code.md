---
title: "Fujitsu Mini Split E:87 Error - Causes & Fix"
description: "E:87 indicates a communication fault between indoor and outdoor units. Check wiring, power cycle the system, and inspect PCB connectors."
pubDatetime: 2026-05-31T01:19:20Z
modDatetime: 2026-05-31T01:19:20Z
author: "James Rutherford"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - fujitsu
money_part: "Fujitsu outdoor main PCB"
most_likely_cause: "Loose or damaged communication wiring"
---

## Fujitsu Mini Split E:87 Error — What It Means

E:87 on a Fujitsu mini split typically points to a communication error between the indoor evaporator unit and the outdoor condenser unit. The two halves of your system are not exchanging control signals properly. This fault category appears when the units cannot establish or maintain the electronic conversation needed to coordinate cooling or heating. Before assuming a board failure, understand that the majority of these faults in the field come from wiring problems, loose connectors, or power quality issues rather than failed electronics. Fujitsu's own troubleshooting flow for communication errors directs technicians to verify wiring integrity and power supply before replacing any circuit boards.

[Jump to Fix](#fix)

## Common Causes

- **Loose or damaged communication wiring** The low-voltage control wires running between indoor and outdoor units may have come loose at terminals, been nicked during installation, or developed breaks that interrupt signal flow.
- **Connector problems on control boards** Molex plugs and pin connectors on the indoor controller PCB, outdoor main PCB, or external I/O board can work loose from vibration or corrode in humid environments.
- **Power supply or voltage drop issues** Insufficient line voltage, a loose connection at the disconnect, or a blown fuse can prevent one unit from powering up completely and establishing communication.
- **Indoor or outdoor PCB failure** After wiring and power checks pass, the fault may be a failed main control board in the outdoor unit, a controller PCB in the indoor unit, or an inverter board component that handles signal processing.
- **Incorrect unit type or compatibility setting** If the indoor unit model or type is not correctly configured in the outdoor unit's settings, the systems cannot recognize each other and communication fails.
- **Poor grounding or electrical noise** Missing or corroded ground connections and nearby electrical interference can corrupt low-voltage control signals and trigger false communication faults.

## Step-by-Step Fix {#fix}

1. **Power cycle the entire system** by switching off the breaker or pulling the disconnect for 60 seconds, then restore power and check whether the fault clears on restart.
2. **Verify both units have power** by confirming the indoor unit display is lit and you can hear or see the outdoor unit attempting to start when you call for cooling or heating.
3. **Inspect all communication wiring** between the indoor and outdoor units for loose terminals, damaged insulation, pinched conductors, or open connections at the terminal blocks inside each unit.
4. **Check connector seating** on the indoor controller PCB and the outdoor main PCB by opening the service panels, locating the Molex or pin connectors for communication lines, and pressing each firmly into place.
5. **Measure supply voltage** at the outdoor unit's main PCB to confirm line voltage matches the nameplate rating and no significant drop occurs under load, then check for 5 V or other reference voltages at sensor/communication pins if your service manual provides test points.
6. **Verify unit compatibility settings** by consulting your installation manual to confirm the outdoor unit's DIP switches or controller settings match the indoor unit model and capacity being used.
7. **Replace the failed PCB** only after isolating the fault to a specific board through wiring, power, and connector checks. If the outdoor unit has power and correct wiring but cannot communicate, the outdoor main or inverter PCB is the likely candidate. If the indoor unit is unresponsive, replace the indoor controller PCB.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Fujitsu outdoor main PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-87-error-code&k=Fujitsu+outdoor+main+PCB&tag=errorcodefixes-20) \| Match the exact part number for your condenser model and production date, printed on the original board label. |
| Fujitsu indoor controller PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-87-error-code&k=Fujitsu+indoor+controller+PCB&tag=errorcodefixes-20) \| Verify compatibility with your evaporator model. Indoor and outdoor boards are not interchangeable. |
| Communication wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-87-error-code&k=Communication+wiring+harness&tag=errorcodefixes-20) \| Pre-terminated harnesses with Molex connectors can replace damaged field wiring if the original conductors are cut or corroded. |

## When to Call a Pro

Call a licensed HVAC technician if power cycling and visual wiring checks do not clear the fault, if you are uncomfortable working inside energized electrical panels, or if you do not have a multimeter and the experience to safely measure control voltages. Communication faults often require a service manual with model-specific connector pinouts and test voltages to isolate the failed board. Because Fujitsu fault code definitions vary by model family and controller type, a technician with access to the correct service literature and replacement part numbers will save you time and avoid incorrect board replacements. If your system is under warranty, professional diagnosis and repair may be covered.
