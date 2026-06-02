---
title: "Senville EH 60 Error Code - Causes & Fix"
description: "EH 60 means the indoor room temperature sensor (T1) is open or shorted. Most often fixed by reseating the sensor connector or replacing the T1 thermistor."
pubDatetime: 2026-05-31T07:49:58Z
modDatetime: 2026-05-31T07:49:58Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - senville
---

## Senville EH 60 Error Code — What It Means

The EH 60 code on your Senville mini split indicates that the indoor unit's T1 room temperature sensor (thermistor) has an open circuit or short circuit. The control board triggers this fault when the sensor voltage drops below 0.06 V or climbs above 4.94 V, both of which signal that the sensor is no longer delivering a valid temperature reading.

In practical terms, the indoor PCB has lost reliable communication with the thermistor that monitors room air temperature. Without this signal, the system cannot modulate compressor speed or fan operation correctly, so it shuts down and displays EH 60 to protect the equipment.

[Jump to Fix](#fix)

## Common Causes

- **Loose or unplugged sensor connector** The T1 sensor plug has backed out of its socket on the indoor PCB, breaking the electrical circuit.
- **Broken or pinched sensor harness** Wiring between the T1 thermistor and the control board has been cut, crushed, or damaged during installation or service.
- **Miswired sensor connections** The sensor leads were reversed or installed on the wrong terminals, pushing the voltage outside the expected range.
- **Failed T1 thermistor** The thermistor itself has gone open or shorted internally, no longer changing resistance in response to temperature.
- **Indoor PCB fault** The control board's sensor input circuit has failed even though the T1 thermistor and wiring are intact.

## Step-by-Step Fix {#fix}

1. **Power off the unit** at the breaker or disconnect, wait two full minutes, then restore power and check whether EH 60 clears on its own.
2. **Remove the front panel** of the indoor unit to expose the main control board and locate the T1 sensor connector, usually labeled on the PCB.
3. **Inspect and reseat** the sensor plug, making sure both the connector and the board socket are clean, dry, and fully engaged with no bent pins.
4. **Trace the sensor wiring** from the thermistor back to the board, looking for pinched insulation, broken conductors, or wire damage from mounting hardware.
5. **Measure the T1 thermistor resistance** with a multimeter set to ohms, then compare your reading to the resistance-temperature table in your model's service manual.
6. **Replace the T1 sensor** if the resistance is infinite (open), near zero (short), or outside the published curve for your unit's thermistor type.
7. **Replace the indoor PCB** if the sensor and all wiring test good but the EH 60 code persists after a power cycle.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Senville T1 room temperature sensor / thermistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-senville-mini-split-eh-60-error-code&k=Senville+T1+room+temperature+sensor+%2F+thermistor&tag=errorcodefixes-20) \| Order the sensor that matches your indoor model number to make sure the correct resistance curve. |
| Senville indoor main control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-senville-mini-split-eh-60-error-code&k=Senville+indoor+main+control+board+%28PCB%29&tag=errorcodefixes-20) \| Required only if the sensor and wiring are confirmed good but the fault remains. |

## When to Call a Pro

Call a licensed HVAC technician if you are uncomfortable working inside energized equipment or if you lack a multimeter and service manual to verify thermistor resistance. A qualified tech can quickly compare your sensor readings to the factory table, repair damaged wiring under the cowling, and flash or replace the indoor board if needed. Professional diagnosis is also the safest route when the code returns immediately after you replace the sensor, since that pattern often points to a board-level fault that requires refrigerant-side access and specialized tools.
