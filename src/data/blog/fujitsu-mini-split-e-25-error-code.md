---
title: "Fujitsu Mini Split E:25 Error Code - Causes & Fix"
description: "E:25 on Fujitsu mini splits means excessive DC voltage in the inverter PFC circuit. Usually requires outdoor controller PCB replacement."
pubDatetime: 2026-05-31T01:04:03Z
modDatetime: 2026-05-31T01:04:03Z
author: "James Rutherford"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - fujitsu
---

## Fujitsu Mini Split E:25 Error Code — What It Means

E:25 (or code 25) on a Fujitsu mini split indicates a PFC circuit error in the outdoor unit. The inverter control board has detected excessive DC voltage on its power factor correction circuit. This is not a refrigerant issue or a simple communication fault. It is a power-circuit protection fault centered on the outdoor inverter PCB.

Fujitsu's troubleshooting documentation identifies the controller PCB as the defective component for this code. The fault is almost always board-level rather than a failed external sensor or refrigerant problem. Real-world diagnostics usually lead to outdoor inverter board replacement after ruling out incoming power quality issues.

[Jump to Fix](#fix)

## Common Causes

- **Defective outdoor inverter/controller PCB** The primary manufacturer-listed cause is failure of the controller PCB itself, typically in the PFC power section.
- **Abnormal DC bus voltage condition** Internal power electronics failure or damaged PFC components can push DC voltage above safe thresholds and trigger the fault.
- **Incoming power quality problems** Voltage drop, unstable supply, or site wiring issues can stress the inverter and cause the PFC circuit to fault out.
- **Loose or damaged power connectors at the outdoor board** Corroded, loose, or miswired connections to the inverter PCB can create voltage spikes that the PFC circuit detects as excessive.
- **Poor ground connection** Fujitsu guides flag ground connection issues as relevant in inverter-related faults, which can contribute to DC voltage instability.
- **Heat damage to the outdoor control board** Prolonged high ambient temperatures or poor ventilation can degrade capacitors and other PFC components on the inverter PCB.

## Step-by-Step Fix {#fix}

1. **Power-cycle the system** and confirm the fault. Turn off the circuit breaker for 60 seconds, restore power, and check whether E:25 returns during normal operation.
2. **Verify incoming line voltage** at the outdoor disconnect. Measure voltage at the outdoor unit's power terminals to confirm stable supply with no significant drop or fluctuations that could stress the inverter.
3. **Inspect all power connections** at the outdoor board. Remove the outdoor unit cover, check for loose, corroded, or heat-damaged connectors, and verify that all wiring to the inverter PCB is secure and properly routed.
4. **Check the ground connection** at the outdoor unit. Confirm that the equipment ground wire is tightly connected and that site grounding is intact.
5. **Inspect the outdoor controller PCB** for visible damage. Look for burnt components, bulging capacitors, heat discoloration, or evidence of arcing on the inverter board itself.
6. **Replace the outdoor controller/inverter PCB** if the fault persists. Fujitsu identifies the controller PCB as the defective part for code 25, so board replacement is the manufacturer-recommended repair.
7. **Test the system** after replacement. Run a full cooling and heating cycle to confirm stable operation and verify that E:25 does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Fujitsu outdoor inverter control board (controller PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-25-error-code&k=Fujitsu+outdoor+inverter+control+board+%28controller+PCB%29&tag=errorcodefixes-20) \| Model-specific. The defective component identified by Fujitsu for E:25. Verify your outdoor unit model number before ordering. |
| Wire connectors and terminals | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-25-error-code&k=Wire+connectors+and+terminals&tag=errorcodefixes-20) \| If corrosion or heat damage is found at board connections during inspection. |

## When to Call a Pro

Call a licensed HVAC technician for E:25. This fault involves high-voltage DC circuitry inside the outdoor inverter unit and requires board-level diagnosis and replacement. The outdoor inverter PCB operates at dangerous voltages and the repair demands specific model knowledge, correct part identification, refrigerant handling (if lines must be opened), and inverter commissioning after board replacement. Homeowners should not attempt to open the outdoor unit's electrical compartment or handle live inverter circuits. If you see the E:25 code and a simple power reset does not clear it, schedule professional service.
