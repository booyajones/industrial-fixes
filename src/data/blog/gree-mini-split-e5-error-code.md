---
title: "Gree E5 Error Code - Causes & Fix"
description: "E5 on a Gree mini split means AC overload protection. Usually caused by compressor hard-start, low voltage, or outdoor fan faults."
pubDatetime: 2026-05-31T07:59:57Z
modDatetime: 2026-05-31T07:59:57Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - gree
---

## Gree E5 Error Code — What It Means

The E5 error code on Gree mini splits indicates AC overload protection. This fault occurs on the outdoor unit side when the system detects abnormal current draw during compressor or fan operation. Unlike simple sensor errors, E5 signals that the inverter board has shut down to prevent damage from overcurrent conditions. The problem typically stems from electrical supply issues, mechanical load problems in the compressor or fan motors, or faults in the outdoor unit's power circuitry. This is a protective shutdown, not a refrigerant or indoor-unit issue.

[Jump to Fix](#fix)

## Common Causes

- **Low or unstable line voltage** Supply voltage outside the normal 220–240 V range or flickering power causes the outdoor unit to draw excessive current during startup and triggers overload protection.
- **Compressor hard-start or locked rotor** A failing compressor that hums but won't start, or one with internal mechanical resistance, pulls far more current than normal and trips the E5 fault immediately.
- **Outdoor fan motor failure** A seized, dragging, or electrically faulty fan motor on the condenser creates abnormal load feedback to the inverter board and causes an overload condition.
- **Outdoor inverter board power-stage fault** Damaged diodes or transistors in the IPM power section of the outdoor PCB produce erratic output current to the compressor or fan, triggering protection.
- **Restricted airflow or dirty coils** Clogged outdoor or indoor heat exchangers force the compressor to work harder, increasing electrical load enough to trip the AC overload sensor.
- **Loose or corroded electrical connections** Poor contact at the compressor plug, fan harness, or board terminals creates resistance that raises current draw and heat, triggering the protection circuit.

## Step-by-Step Fix {#fix}

1. **Cut power at the breaker and wait two minutes.** Restore power and observe whether E5 returns immediately on startup or only after the compressor tries to run.
2. **Measure line voltage at the outdoor disconnect** with a multimeter while the unit attempts to start. Confirm you have stable voltage in the 220–240 V range with no significant sag or spike.
3. **Inspect both indoor and outdoor coils** for dust, debris, or blockage. Clean the heat exchangers with coil cleaner and verify that both the indoor blower and outdoor fan spin freely by hand when power is off.
4. **Check compressor and fan wiring** at the outdoor unit. Remove the service panel, examine all connectors and terminals for corrosion or looseness, and make sure harness insulation is intact.
5. **Listen to the compressor during startup.** If it hums loudly but does not start, or if the outdoor unit vibrates abnormally, measure compressor winding resistance with power off. Compare the three pin-pair readings on the compressor terminal. They should be roughly equal. Significant imbalance points to internal compressor damage.
6. **Test the outdoor fan motor.** Disconnect the fan plug and measure winding resistance. Spin the fan blade. If it drags, binds, or shows open or shorted windings, replace the motor.
7. **Inspect the outdoor inverter board** if all mechanical and supply checks pass. Look for burnt components, swollen capacitors, or damaged diodes in the IPM power section. Measure DC bus voltage on the board. For 220 V supply, expect approximately 300 V DC. If the bus voltage is absent or far out of range, replace the board or repair the power section.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Gree outdoor inverter PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-gree-mini-split-e5-error-code&k=Gree+outdoor+inverter+PCB&tag=errorcodefixes-20) \| Match by model and serial number. Controls compressor and fan. Required when IPM power section or drive circuitry is faulty. |
| Gree compressor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-gree-mini-split-e5-error-code&k=Gree+compressor&tag=errorcodefixes-20) \| Specify tonnage and refrigerant type. Replace when winding resistance is unbalanced or unit hard-starts and hums without running. |
| Gree outdoor fan motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-gree-mini-split-e5-error-code&k=Gree+outdoor+fan+motor&tag=errorcodefixes-20) \| Verify voltage and shaft diameter. Needed when motor is seized, shows abnormal resistance, or fails to spin under load. |
| Compressor wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-gree-mini-split-e5-error-code&k=Compressor+wiring+harness&tag=errorcodefixes-20) \| Order the harness for your outdoor unit model if connectors are melted, corroded, or damaged. |

## When to Call a Pro

Call a licensed HVAC technician if you lack a multimeter or are uncomfortable working with live 220–240 V circuits. Diagnosing E5 requires measuring line voltage, testing compressor windings, and inspecting inverter board components under power. Compressor and board replacement both involve refrigerant recovery, brazing or electrical soldering, and vacuum procedures that require EPA certification and specialized tools. If the fault returns after you have verified clean coils and stable voltage, professional diagnostic equipment and parts-matching expertise will save time and prevent misdiagnosis.
