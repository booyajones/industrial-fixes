---
title: "Senville Mini Split EC 54 - Causes & Fix"
description: "EC 54 means the compressor discharge temp sensor (TP/T5) is sending an out-of-range signal. Usually a faulty sensor or loose wire."
pubDatetime: 2026-05-31T08:36:43Z
modDatetime: 2026-05-31T08:36:43Z
author: "Dana Kowalski"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - senville
money_part: "Senville compressor discharge temperature sensor (TP/T5)"
most_likely_cause: "Failed or drifted TP/T5 sensor"
---

## Senville Mini Split EC 54 — What It Means

EC 54 on a Senville mini split indicates that the compressor discharge temperature sensor (TP or T5) is reporting a voltage outside the normal operating range. The controller shuts down the unit when it sees a sampling voltage below 0.06 V or above 4.94 V, which signals an open circuit, short, or sensor failure. This is a sensor circuit fault, not a refrigerant or compressor problem by itself.

The discharge temperature sensor is mounted on the refrigerant line leaving the compressor in the outdoor unit. When the sensor fails, becomes disconnected, or its wiring is damaged, the control board cannot monitor compressor temperature and stops operation to protect the system.

[Jump to Fix](#fix)

## Common Causes

- **Failed or drifted TP/T5 sensor** The compressor discharge temperature sensor itself has failed internally or drifted out of specification and no longer produces a valid resistance signal.
- **Loose or corroded sensor connector** The plug between the sensor leads and the outdoor PCB has become loose, corroded, or damaged, breaking the electrical path.
- **Broken or shorted sensor wiring** The wire harness running from the sensor to the control board has been pinched, cut, or shorted against metal, causing an open or short circuit.
- **Poor thermal contact at sensor location** The sensor has come loose from the discharge line or lost its thermal paste, so it cannot accurately read the pipe temperature.
- **Faulty outdoor control board** The outdoor PCB has failed and is not correctly reading the sensor voltage, even though the sensor and wiring are good.
- **Defective combined sensor assembly** On some models the discharge sensor is part of a multi-element sensor pack, and one element inside the assembly has failed.

## Step-by-Step Fix {#fix}

1. **Power-cycle the unit** by turning off the circuit breaker for two minutes, then restore power and see if the EC 54 code returns. A transient fault may clear on its own.
2. **Turn off all power** at the breaker and verify zero voltage with a tester before opening the outdoor unit cover.
3. **Locate the TP/T5 sensor** on the discharge line near the compressor outlet. Check that it is securely fastened and making good contact with the pipe.
4. **Inspect all sensor wiring and connectors** from the sensor back to the outdoor PCB for loose pins, breaks, corrosion, or pinch damage. Reconnect or clean any corroded terminals.
5. **Measure the sensor resistance** with a multimeter while the sensor is at a known temperature and compare the reading to the manufacturer's temperature-resistance chart for your model. Replace the sensor if the value is out of range.
6. **Check the sensor voltage** at the PCB connector with the sensor plugged in and the board powered. If voltage reads below 0.06 V or above 4.94 V and the sensor tests good, suspect the control board.
7. **Replace the faulty component.** If the sensor or wiring is bad, install a new TP/T5 sensor or repair the harness. If the sensor and wiring test normal but the code persists, replace the outdoor PCB.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Senville compressor discharge temperature sensor (TP/T5) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-senville-mini-split-ec-54-error-code&k=Senville+compressor+discharge+temperature+sensor+%28TP%2FT5%29&tag=errorcodefixes-20) \| Match the sensor to your exact Senville model number. Some units use a combined sensor assembly that includes T3, T4, and T5 elements. |
| Senville outdoor PCB / main control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-senville-mini-split-ec-54-error-code&k=Senville+outdoor+PCB+%2F+main+control+board&tag=errorcodefixes-20) \| Order by your model and serial number if sensor and wiring test good but the fault remains. |
| Sensor wiring harness or connector | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-senville-mini-split-ec-54-error-code&k=Sensor+wiring+harness+or+connector&tag=errorcodefixes-20) \| If the connector is damaged or corroded beyond cleaning, order the matching pigtail or harness for your outdoor unit. |

## When to Call a Pro

Call a qualified HVAC technician if you are not comfortable working with live electrical components or if the fault persists after replacing the sensor and checking all wiring. A pro can safely measure board voltages, verify the refrigeration circuit if needed, and diagnose combined sensor assemblies or control board faults. If the unit is under warranty, contact Senville or your installer before opening the outdoor unit to avoid voiding coverage.
