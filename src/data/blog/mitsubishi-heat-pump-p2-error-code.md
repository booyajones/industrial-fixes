---
title: "Mitsubishi P2 Error Code - Causes & Fix"
description: "P2 on Mitsubishi heat pumps means indoor pipe temperature sensor (TH2) failure. Most common fix: replace the thermistor or reseat CN44."
pubDatetime: 2026-05-31T08:52:59Z
modDatetime: 2026-05-31T08:52:59Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - mitsubishi
---

## Mitsubishi P2 Error Code — What It Means

P2 signals a problem with the indoor unit pipe temperature thermistor, usually identified as the TH2 sensor or liquid-pipe sensor. This thermistor monitors refrigerant pipe temperature so the control board can regulate heating and cooling cycles. When the sensor reads open, shorted, or out of specification, or when its wiring or connector fails, the indoor board cannot trust the feedback and shuts the system down with a P2 fault.

Mitsubishi Electric fault-code tables group P2 as a pipe sensor circuit error, not a compressor or outdoor-unit fault. The error can be electrical (failed thermistor, poor connector contact, damaged wire) or secondary to a refrigerant problem that forces abnormal pipe temperatures the board interprets as a sensor fault.

[Jump to Fix](#fix)

## Common Causes

- **Open or shorted pipe thermistor** The TH2 sensor itself has failed or drifted outside the resistance range the board expects.
- **Loose or corroded connector at CN44** Poor contact at the indoor board connector CN44, where the thermistor plugs in, is a frequent source of intermittent P2 faults.
- **Damaged thermistor wiring** Wire breaks, pinches, or frayed insulation between the sensor and the indoor PCB cause open or intermittent circuits.
- **Refrigerant leak or air ingress** Low refrigerant charge, leaks, or air in the circuit produce abnormal pipe temperatures that trigger sensor-error logic even when the sensor is good.
- **Failed indoor control board** If the thermistor and wiring test normal, the sensor input circuit on the indoor PCB may be defective.

## Step-by-Step Fix {#fix}

1. **Turn off power** at the disconnect or breaker and confirm the P2 code appears consistently on the indoor unit or remote before you begin diagnostics.
2. **Locate the pipe thermistor** (TH2) mounted on the indoor coil liquid or two-phase pipe and inspect it for physical damage, displacement from the pipe surface, or loose mounting hardware.
3. **Check connector CN44** on the indoor control board for loose pins, corrosion, or backed-out terminals, then unplug and reseat the connector firmly.
4. **Measure the thermistor resistance** using a multimeter at the sensor leads or board connector and compare the reading to the temperature-resistance curve in your model's service manual (if the sensor is open, shorted, or far outside spec, replace it).
5. **Inspect the wiring harness** from the thermistor back to the indoor board for cuts, pinches, or signs of rodent damage, and repair or replace any damaged wire segments.
6. **Test the refrigerant circuit** if the sensor reads plausibly but the code persists: check pressures, inspect joints for leaks, and recover, evacuate, and recharge the system if refrigerant loss or air contamination is confirmed.
7. **Replace the indoor control board** only after proving the sensor, wiring, and refrigerant side are all correct, then clear the fault and run the system through a full cycle to verify stable operation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Mitsubishi pipe temperature thermistor (TH2) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-heat-pump-p2-error-code&k=Mitsubishi+pipe+temperature+thermistor+%28TH2%29&tag=errorcodefixes-20) \| Match the part number in your unit's service manual or indoor-coil parts diagram. |
| Indoor control board (indoor PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-heat-pump-p2-error-code&k=Indoor+control+board+%28indoor+PCB%29&tag=errorcodefixes-20) \| Required only when sensor and wiring test good but the board still registers a P2 fault. |
| Thermistor wiring harness or connector repair kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-heat-pump-p2-error-code&k=Thermistor+wiring+harness+or+connector+repair+kit&tag=errorcodefixes-20) \| Use if the fault is traced to damaged wires or poor pin contact rather than the sensor body. |

## When to Call a Pro

Call a licensed HVAC technician if you are not comfortable working with live control boards, measuring thermistor resistance, or handling refrigerant. Refrigerant-side diagnostics require EPA certification, manifold gauges, recovery equipment, and vacuum pumps. Replacing the indoor board or thermistor involves removing panels and working near high-voltage connections. If the fault is intermittent or you cannot isolate whether the problem is the sensor, wiring, or refrigerant circuit, a technician with Mitsubishi-specific training and the correct service manual will save you time and prevent misdiagnosis.
