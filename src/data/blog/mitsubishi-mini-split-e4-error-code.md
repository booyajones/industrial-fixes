---
title: "Mitsubishi Mini Split E4 Error - Causes & Fix"
description: "E4 on Mitsubishi mini splits can mean fan motor feedback or temperature sensor fault depending on model. Check wiring and sensor first."
pubDatetime: 2026-05-31T00:48:54Z
modDatetime: 2026-05-31T00:48:54Z
author: "James Rutherford"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - mitsubishi
---

## Mitsubishi Mini Split E4 Error — What It Means

The E4 error code on Mitsubishi mini-split systems is not universal across all models. Depending on your specific indoor and outdoor unit family, E4 may indicate a fan motor feedback fault from the indoor unit or a problem with the room temperature sensor. On some inverter platforms, E4 points to the indoor fan motor not returning the expected signal to the control board. On other non-inverter units, the same code flags a shorted, open, or disconnected temperature sensor. Because Mitsubishi Electric uses model-specific fault tables, you must verify the exact meaning of E4 against your unit's service manual or error-code lookup before starting repairs.

[Jump to Fix](#fix)

## Common Causes

- **Failed indoor fan motor or feedback circuit** On units where E4 maps to fan motor feedback, the motor itself or its tachometer signal wiring has failed and the board cannot confirm the fan is running.
- **Shorted or open room temperature sensor** On units where E4 is a sensor code, the thermistor has failed internally or reads out of range due to a short or open circuit.
- **Loose or damaged sensor connector and wiring** Corrosion, vibration, or physical damage can disconnect or intermittently break the sensor signal wire between the thermistor and the control board.
- **Faulty indoor control board** If the sensor or motor tests good but the error persists, the PCB may not be supplying the correct low voltage feed or reading feedback correctly.
- **Missing or incorrect supply voltage to sensor circuit** The board must provide a small reference voltage to the sensor or motor feedback circuit, and a failed regulator or trace can trigger E4 even when the component is intact.

## Step-by-Step Fix {#fix}

1. {'lead': "Look up your exact model's fault table", 'text': 'before you pull any covers. Mitsubishi Electric publishes model-specific error-code definitions, so confirm whether E4 means fan motor feedback or temperature sensor on your unit.'}
2. {'lead': 'Power-cycle the system', 'text': 'by switching off the breaker or disconnect for three to five minutes, then restore power and see if the code clears on its own after a reset.'}
3. {'lead': 'Inspect the relevant harness and connector', 'text': 'for the fault path your model indicates. If E4 is fan-related, check the indoor fan motor plug and wiring for loose pins or damage. If E4 is sensor-related, trace the room temperature sensor lead from the evaporator coil or return air path to the board and look for corrosion or breaks.'}
4. {'lead': 'Measure the suspect component with a multimeter', 'text': 'to confirm failure. For a temperature sensor, disconnect it and check resistance across the thermistor leads. For a fan motor fault, verify the motor runs when powered directly and check continuity on the feedback wire. Compare readings to the service manual spec if available.'}
5. {'lead': 'Check the PCB supply outputs', 'text': 'if the component and wiring test good. Use your meter to confirm the board is delivering the low-voltage reference to the sensor circuit or the expected voltage to the fan motor control terminals.'}
6. {'lead': 'Replace only the verified failed part', 'text': 'after your tests. Swap the temperature sensor if it reads open or shorted and the wiring is intact. Replace the indoor fan motor or its tachometer assembly if feedback is missing and the motor does not respond. Replace the control board only if it fails to supply correct voltage or the fault remains after known-good component substitution.'}
7. {'lead': 'Run a full test cycle', 'text': 'after the repair to confirm E4 does not return and the unit maintains set point in both cooling and heating modes.'}

## Parts Often Needed

| Part | Notes |
|------|-------|
| Indoor room temperature sensor (thermistor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-mini-split-e4-error-code&k=Indoor+room+temperature+sensor+%28thermistor%29&tag=errorcodefixes-20) \| Order by your indoor unit model number if E4 maps to sensor fault on your system. |
| Indoor fan motor assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-mini-split-e4-error-code&k=Indoor+fan+motor+assembly&tag=errorcodefixes-20) \| Required if E4 indicates fan motor feedback failure and the motor does not run or signal correctly. |
| Indoor control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-mini-split-e4-error-code&k=Indoor+control+board+%28PCB%29&tag=errorcodefixes-20) \| Replace only after verifying the sensor or motor is good but the board fails voltage supply or signal processing tests. |

## When to Call a Pro

Call a licensed HVAC technician if you cannot find your model's fault table, if you are not comfortable working inside a live mini-split control box, or if the error returns after you replace the sensor or motor. Refrigerant-circuit work and board-level diagnostics require specialized tools and EPA certification. A pro will have the exact Mitsubishi service manual, can verify refrigerant charge if the fault is actually compressor-related on certain platforms, and will warranty the repair.

## See Also

- [Mitsubishi E6 Error Code - Causes & Fix](/posts/mitsubishi-heat-pump-e6-error-code/)
- [Mitsubishi Mini Split P1 Error Code Fix](/posts/mitsubishi-p1-error-code/)
- [Mitsubishi P9 Error Code - Causes & Fix](/posts/mitsubishi-heat-pump-p9-error-code/)
- [Mitsubishi E7 Error Code - Causes & Fix](/posts/mitsubishi-heat-pump-e7-error-code/)
