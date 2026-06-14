---
title: "Fujitsu E:41 Error Code - Causes & Fix"
description: "E:41 means indoor room temperature sensor error. Most common fix: replace the faulty room thermistor or check its connector for loose wiring."
pubDatetime: 2026-05-31T01:08:09Z
modDatetime: 2026-05-31T01:08:09Z
author: "Marcus Webb"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - fujitsu
money_part: "Indoor room thermistor"
most_likely_cause: "Failed room thermistor"
---

## Fujitsu E:41 Error Code — What It Means

The E:41 error code on a Fujitsu mini split indicates an indoor room temperature sensor error. The indoor unit's room thermistor has detected an abnormal condition or failed completely, preventing the system from accurately reading room temperature. This sensor is critical for proper operation because the unit relies on it to control heating and cooling cycles. When the control board loses communication with the thermistor or receives out-of-range readings, it triggers the E:41 fault and shuts down operation to prevent damage.

[Jump to Fix](#fix)

## Common Causes

- **Failed room thermistor** The indoor room temperature sensor itself has shorted or opened internally, which is the most common cause of this error.
- **Loose or disconnected sensor connector** The thermistor harness connector has vibrated loose, corroded, or become disconnected at the indoor unit main PCB.
- **Open or damaged sensor wiring** The thermistor harness has broken wire strands, pinched insulation, or damage between the sensor and the control board.
- **Faulty indoor main PCB** The indoor controller board has failed in the sensor circuit and no longer provides correct reference voltage or continuity path.
- **Miswired or incorrect sensor installation** The thermistor connector was plugged into the wrong terminal block or the wrong sensor type was installed during previous service.
- **PCB and indoor unit mismatch** An incorrect main PCB was installed that does not match the indoor unit type or configuration.

## Step-by-Step Fix {#fix}

1. **Power-cycle the system** by turning off the circuit breaker for at least 30 seconds, then restore power and check if the error clears (this rules out a transient glitch).
2. **Access the indoor unit** by removing the front cover and filter, then the plastic housing to expose the main control board and thermistor location (typically clipped near the evaporator coil inlet).
3. **Inspect the thermistor connector and harness** for loose connections, corrosion, or visible damage, and firmly reseat the connector at the main PCB if it appears loose.
4. **Perform a continuity check on the thermistor circuit** by disconnecting the room sensor connector and measuring continuity between pins 4 and 5 on the connector (continuity present points to main PCB failure, no continuity points to sensor failure).
5. **Perform a voltage check at CN67** by disconnecting the sensor and measuring voltage on pin 1 of CN67 at the main PCB (about 5 volts indicates sensor failure, a voltage other than 5 volts indicates main PCB failure).
6. **Replace the faulty component** (either the indoor room thermistor or the main PCB) based on your test results, routing the new sensor harness away from high-voltage wiring and securing it with the factory clips.
7. **Reassemble the indoor unit**, restore power, and run a test cycle to confirm the E:41 error has cleared and the unit is reading room temperature correctly.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Indoor room thermistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-41-error-code&k=Indoor+room+thermistor&tag=errorcodefixes-20) \| OEM Fujitsu part matched to your indoor unit model number. |
| Indoor main PCB / controller board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-41-error-code&k=Indoor+main+PCB+%2F+controller+board&tag=errorcodefixes-20) \| Match the board part number on your existing PCB label exactly. |

## When to Call a Pro

Call a qualified HVAC technician if you are not comfortable working with low-voltage wiring or cannot safely access the indoor unit control board. Professional diagnosis is especially important if both the thermistor and main PCB pass electrical tests but the error persists, or if you discover miswiring that suggests previous incorrect service. Refrigerant-side work is not required for this error, but a tech with a multimeter and Fujitsu service documentation can pinpoint the fault quickly and avoid unnecessary part replacement.
