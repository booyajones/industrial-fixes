---
title: "Fujitsu E:02 Error Code - Causes & Fix"
description: "E:02 means the indoor room-temperature sensor is open or missing. Most often it's a failed thermistor or loose connector at the PCB."
pubDatetime: 2026-05-31T00:58:06Z
modDatetime: 2026-05-31T00:58:06Z
author: "James Rutherford"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - fujitsu
---

## Fujitsu E:02 Error Code — What It Means

The E:02 fault on a Fujitsu mini split indicates that the indoor unit's room temperature sensor is open or missing. The controller cannot read the sensor signal, which means the system cannot measure room temperature and will not operate normally. This is different from E:03, which signals a shorted sensor. An open reading means either the thermistor itself has failed, the wiring is broken or disconnected, or the sensor was never plugged in during installation.

[Jump to Fix](#fix)

## Common Causes

- **Failed room thermistor** The temperature sensor in the indoor unit has gone open-circuit and no longer provides a valid resistance reading.
- **Loose or unplugged sensor connector** The thermistor harness is not seated properly at the indoor PCB or has vibrated loose over time.
- **Damaged sensor wiring** The wire between the sensor and the indoor controller has been cut, pinched, or corroded, creating an open circuit.
- **Sensor missing or incorrectly installed** The room thermistor was never installed in the indoor coil or return-air sensing location, or was removed during service.
- **Indoor controller PCB failure** The main board cannot read the sensor even when the sensor and wiring test good, indicating a board-level fault.

## Step-by-Step Fix {#fix}

1. **Power off the system** at the breaker or disconnect and remove the front cover of the indoor unit to access the controller board.
2. **Locate the room thermistor connector** on the indoor PCB and verify it is fully seated and not loose, damaged, or corroded.
3. **Inspect the sensor itself** where it sits in the indoor coil or return-air path and confirm it is present and properly clipped or secured in place.
4. **Disconnect the sensor plug** and measure the thermistor resistance with a multimeter across the sensor leads, comparing the reading to Fujitsu's thermistor characteristics table for your model at current room temperature.
5. **Check wiring continuity** from the sensor pins back to the PCB connector for any open circuits, breaks, or shorts to ground.
6. **Replace the room temperature sensor** if it reads open (infinite resistance) or is out of spec according to the manufacturer's table.
7. **Replace the indoor controller PCB** if the sensor and wiring both test good but the E:02 code returns after reconnecting and restoring power.
8. **Restore power** and monitor the display to confirm the fault clears and the unit resumes normal temperature sensing and operation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Fujitsu indoor room temperature sensor / thermistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-02-error-code&k=Fujitsu+indoor+room+temperature+sensor+%2F+thermistor&tag=errorcodefixes-20) \| Match to your indoor unit model number. Usually a two-pin plug-in NTC thermistor. |
| Fujitsu indoor unit controller PCB / main board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-02-error-code&k=Fujitsu+indoor+unit+controller+PCB+%2F+main+board&tag=errorcodefixes-20) \| Required only if sensor and wiring test good but fault persists. Verify board part number from your unit label. |

## When to Call a Pro

Call a qualified HVAC technician if you are not comfortable working with live electrical components, if you cannot locate or access the room sensor inside the indoor unit, or if the sensor and wiring both test normal but the fault code remains. A technician has the model-specific thermistor resistance charts, diagnostic tools, and replacement parts to pinpoint board-level faults and complete refrigerant-side work if needed. If your system is under warranty, contact an authorized Fujitsu service provider to avoid voiding coverage.
