---
title: "Fujitsu Mini Split E:90 Error Code - Causes & Fix"
description: "E:90 on Fujitsu mini splits typically signals a communication or control board fault. Most often fixed by checking wiring and connectors."
pubDatetime: 2026-05-31T01:20:01Z
modDatetime: 2026-05-31T01:20:01Z
author: "James Rutherford"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - fujitsu
---

## Fujitsu Mini Split E:90 Error Code — What It Means

The E:90 error code on Fujitsu mini split systems is not universally defined across all models in published service documentation, but it falls within the fault class that indicates a communication failure or control board problem between the indoor and outdoor units. This type of error typically means the system has lost the ability to send or receive signals properly, often due to wiring issues, loose connectors, or a defective circuit board. The exact meaning can vary by model, so consult your unit's service manual for confirmation.

Fujitsu's troubleshooting framework for communication and control faults points to problems with the DC communication voltage between units, addressing mismatches on multi-zone systems, or failures in the main PCB, inverter PCB, or controller components. The fault may also be triggered by sensor inputs or power supply instability that drives the control board into a protective shutdown state.

[Jump to Fix](#fix)

## Common Causes

- **Loose or disconnected wiring between indoor and outdoor units** Open circuits, poor terminal connections, or miswired interconnect cables prevent communication signals from traveling between the two halves of the system.
- **Loose connectors on the main PCB, inverter PCB, or controller board** Partially seated harness plugs, corroded pins, or broken connectors interrupt the control signals needed for normal operation.
- **Defective main control board or communication IC** Failed components on the PCB, including the communication chip or main relay, stop the board from processing or transmitting signals correctly.
- **Incorrect indoor unit type or addressing on linked systems** Configuration mismatches or wrong DIP switch settings on multi-zone setups cause the controller to reject communication with the indoor unit.
- **Unstable or low incoming power supply** Voltage drop, fluctuating supply, or grounding problems starve the control board of the stable DC voltage it needs to maintain communication.
- **Faulty sensor or thermistor sending bad input signals** An open or shorted temperature sensor can drive the control board into a fault state, triggering a communication or protection error.

## Step-by-Step Fix {#fix}

1. **Power-cycle the system completely** by turning off the breaker or disconnect for at least two minutes, then restore power and check whether the E:90 code clears or returns immediately.
2. **Inspect the interconnect wiring** between the indoor and outdoor units for loose terminals, broken insulation, open circuits, or reversed polarity, and verify continuity on all communication wires.
3. **Check every connector on the control boards** including the main PCB, inverter PCB, and any external controller or I/O boards, reseating each plug firmly and looking for corrosion, bent pins, or damaged harness clips.
4. **Measure the incoming supply voltage** at the unit and confirm it matches the nameplate specification with no excessive drop or fluctuation, and verify that grounding is solid and correctly wired.
5. **Verify indoor unit addressing and configuration** if you have a multi-zone or linked system, checking DIP switches, jumper settings, and the controller setup to confirm the indoor type matches what the outdoor unit expects.
6. **Test thermistors and sensors** by unplugging each one and measuring resistance with a multimeter, comparing the reading to the manufacturer's thermistor characteristic table for opens or shorts.
7. **Replace the main control board or inverter PCB** if all wiring, connectors, power supply, and sensors check out but the fault persists, isolating the defective board through systematic part swapping or signal testing.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Main control board (indoor or outdoor PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-90-error-code&k=Main+control+board+%28indoor+or+outdoor+PCB%29&tag=errorcodefixes-20) \| Match the board part number exactly to your indoor or outdoor model number. |
| Inverter PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-90-error-code&k=Inverter+PCB&tag=errorcodefixes-20) \| Required if diagnostics isolate the fault to the outdoor inverter section. |
| Thermistor sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-90-error-code&k=Thermistor+sensor&tag=errorcodefixes-20) \| Use OEM Fujitsu sensors matched to the location (coil, ambient, discharge) listed in your fault tree. |

## When to Call a Pro

Call a licensed HVAC technician if you are not comfortable working with live voltage, if the fault persists after you have checked all wiring and connectors, or if diagnostics point to a defective control board or inverter PCB that requires refrigerant recovery and brazing work. Communication faults can also involve addressing and configuration steps that require manufacturer-specific tools or software, especially on multi-zone systems. A qualified technician has the meters, service manuals, and board-level diagnostic skills to isolate the exact failed component and replace it without creating new problems.
