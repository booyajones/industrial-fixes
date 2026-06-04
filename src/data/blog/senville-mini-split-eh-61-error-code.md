---
title: "Senville Mini Split EH 61 Error Code - Causes & Fix"
description: "EH 61 means the indoor coil temperature sensor (T2) is reading open or shorted. Most often the sensor or its wiring has failed."
pubDatetime: 2026-05-31T08:36:32Z
modDatetime: 2026-05-31T08:36:32Z
author: "Dana Kowalski"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - senville
---

## Senville Mini Split EH 61 Error Code — What It Means

EH 61 on your Senville mini split indicates an indoor coil temperature sensor (T2) error. The control board is receiving a voltage reading below 0.06 V or above 4.94 V from the T2 thermistor, which signals either an open circuit, a short, or a sensor that has drifted out of its normal resistance range. The system cannot operate safely without a reliable coil temperature reading, so it shuts down and displays the code.

The T2 sensor is mounted on the indoor unit's refrigerant piping and monitors the evaporator coil temperature during heating and cooling. When the sensor or its wiring fails, the board cannot tell if the coil is freezing, overheating, or operating normally. Senville specifies this fault as a pipe temperature sensor problem and provides a replacement part number (TS05-IDU for AURA series models) in their technical documentation.

[Jump to Fix](#fix)

## Common Causes

- **Failed T2 thermistor** The pipe-mounted temperature sensor itself has drifted out of its resistance range or failed internally, triggering the voltage fault.
- **Loose or corroded sensor connector** The plug at the indoor PCB or at the sensor itself is loose, corroded, or making intermittent contact, creating an open circuit reading.
- **Damaged sensor wiring** The two-wire harness between the T2 sensor and the indoor board has been pinched, cut, or shorted against metal during installation or service.
- **Indoor PCB input circuit fault** The control board's sensor input circuitry has failed, reading the sensor voltage incorrectly even when the sensor and wiring are good.

## Step-by-Step Fix {#fix}

1. **Power off the unit completely** at the circuit breaker, wait two full minutes, then restore power and attempt a reset. If EH 61 returns immediately, continue testing.
2. **Inspect the T2 sensor and its wiring** at the indoor unit. The sensor is a small black thermistor clipped or strapped to the refrigerant pipe near the evaporator coil. Check for physical damage, corrosion, or loose connections.
3. **Disconnect the T2 sensor plug** from the indoor PCB (note wire colors or take a photo first). Using a multimeter set to resistance, measure across the two sensor leads and compare the reading to the temperature-resistance table in your unit's service manual. Most Senville thermistors are 10 kΩ type at 25 °C, but always consult your model's published table.
4. **Check the sensor input voltage** at the indoor PCB connector with the sensor plugged in and the unit powered on. Senville defines the fault trigger as below 0.06 V or above 4.94 V. If voltage is in that fault range but the sensor resistance was correct, suspect the indoor PCB.
5. **Replace the T2 sensor** if resistance is out of range or the sensor is visibly damaged. Senville AURA models use part number TS05-IDU. Route the new sensor wiring away from sharp edges and secure the sensor firmly to the pipe.
6. **Replace the indoor PCB** only if the sensor resistance is correct, wiring is intact, and the fault voltage persists. Mark all wire connections before removal and transfer them carefully to the new board.
7. **Restore power and run a test cycle** in both cooling and heating modes to verify the error does not return and that the system cycles normally.

## Parts Often Needed

| Part | Notes |
|------|-------|
| T2 indoor coil pipe temperature sensor (TS05-IDU for AURA series) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-senville-mini-split-eh-61-error-code&k=T2+indoor+coil+pipe+temperature+sensor+%28TS05-IDU+for+AURA+series%29&tag=errorcodefixes-20) \| Verify your exact model number before ordering. The sensor is specific to your indoor unit series. |
| Indoor main control board / PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-senville-mini-split-eh-61-error-code&k=Indoor+main+control+board+%2F+PCB&tag=errorcodefixes-20) \| Required only if sensor and wiring test correctly but the fault persists. Match the board part number exactly to your indoor unit. |

## When to Call a Pro

Call a licensed HVAC technician if you are not comfortable working with live electrical connections or if you do not have a multimeter and the manufacturer's resistance table. Diagnosing EH 61 requires measuring sensor resistance and verifying PCB input voltage, both of which demand careful testing. If you replace the sensor and the code returns, the indoor PCB is likely faulty and should be replaced by a qualified technician to avoid misdiagnosis and unnecessary parts cost. Refrigerant-side work is not required for this repair, but the indoor unit cover must be removed to access the sensor and board.
