---
title: "LG Mini Split CH44 Error Code - Causes & Fix"
description: "CH44 means your outdoor air temperature sensor is disconnected or shorted. Most often a loose connector or failed thermistor."
pubDatetime: 2026-05-31T00:55:10Z
modDatetime: 2026-05-31T00:55:10Z
author: "Dana Kowalski"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - lg
money_part: "LG outdoor air temperature thermistor (inlet air sensor)"
most_likely_cause: "Loose or unplugged sensor connector"
---

## LG Mini Split CH44 Error Code — What It Means

The CH44 error code on LG mini splits indicates a fault with the outdoor air temperature sensor (thermistor) circuit. This means the outdoor unit's control board cannot read the ambient outdoor air temperature because the sensor is either disconnected, has a damaged wire, or has failed internally. The sensor circuit is either open (disconnected) or shorted, preventing normal operation. This is an outdoor-unit issue, not an indoor-unit problem.

[Jump to Fix](#fix)

## Common Causes

- **Loose or unplugged sensor connector** The thermistor connector at the outdoor PCB has worked loose or was not fully seated during installation or service.
- **Damaged sensor wiring** The thermistor wire harness is cut, pinched, corroded, or has damaged insulation exposing bare wire.
- **Failed outdoor air thermistor** The thermistor itself has failed and now reads open circuit or shorted, giving out-of-range resistance values.
- **Faulty outdoor main PCB** The outdoor control board sensor input circuit has failed and cannot read the thermistor even when the sensor is good.

## Step-by-Step Fix {#fix}

1. **Power the system down completely** by turning off the breaker or disconnect switch, wait three minutes, then restore power and check if the CH44 code clears or returns.
2. **Locate the outdoor air thermistor** on the outdoor unit and trace its wiring and connector back to the outdoor main control board.
3. **Inspect the connector and wiring** for any loose pins, corrosion, damaged insulation, pinched wires, or physical damage to the sensor body.
4. **Disconnect the thermistor** from the board and use a multimeter set to kΩ (resistance) to measure the sensor at its connector pins. It should not read 0 Ω (shorted) or infinite/open. For reference, some LG thermistors read around 10 kΩ at 10°C and 4 kΩ at 30°C, but consult your model's service manual for the exact resistance table.
5. **Check the sensor circuit supply** at the board side of the connector with the sensor disconnected. Some LG outdoor boards supply around 4.5 VDC to the sensor circuit, but this is a field-observed value and not a universal spec for all models.
6. **Replace the outdoor air thermistor** if it tests open, shorted, or out of range and the wiring and connector are intact.
7. **Replace the outdoor main PCB** if the thermistor and all wiring test good but the CH44 code persists, indicating a board-level input fault.

## Parts Often Needed

| Part | Notes |
|------|-------|
| LG outdoor air temperature thermistor (inlet air sensor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch44-error-code&k=LG+outdoor+air+temperature+thermistor+%28inlet+air+sensor%29&tag=errorcodefixes-20) \| Match your outdoor unit model number and verify connector type before ordering. |
| Outdoor main PCB (control board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch44-error-code&k=Outdoor+main+PCB+%28control+board%29&tag=errorcodefixes-20) \| Only needed if the thermistor and wiring test good but the fault remains. |

## When to Call a Pro

If you are not comfortable working with live electrical circuits, measuring resistance with a multimeter, or accessing the outdoor unit control board, call a licensed HVAC technician. The outdoor unit operates on line voltage (typically 208-240 VAC) and refrigerant lines, both of which require proper safety precautions. A technician can quickly verify the sensor, harness, and board, and will have the correct OEM replacement parts and resistance tables for your specific LG model.

## See Also

- [LG DLE7400WE Dryer Problems & Error Codes](/posts/lg-dle7400we-dryer-problems/)
- [LG Dishwasher PE Error Code - Causes & Fix](/posts/lg-dishwasher-pe-error-code/)
- [LG Microwave Turntable Not Turning - Causes & Fix](/posts/lg-microwave-turntable-not-turning/)
- [LG Microwave Runs but No Heat - Causes & Fix](/posts/lg-microwave-runs-but-no-heat/)
