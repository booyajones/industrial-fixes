---
title: "Gree F3 Error Code - Causes & Fix"
description: "F3 on a Gree mini split means outdoor ambient temperature sensor fault. Most common fix: reseat or replace the outdoor sensor."
pubDatetime: 2026-05-31T08:37:38Z
modDatetime: 2026-05-31T08:37:38Z
author: "Marcus Webb"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - gree
money_part: "Gree outdoor ambient temperature sensor / thermistor"
most_likely_cause: "Loose or corroded sensor connector"
---

## Gree F3 Error Code — What It Means

F3 on a Gree mini split indicates an outdoor ambient temperature sensor malfunction. This is a sensor circuit fault, not a refrigerant pressure problem. The outdoor unit's ambient thermistor has either an open circuit, a short circuit, or drifted out of its normal resistance range. Gree's published error code tables list F3 as outdoor environment sensor malfunction or outdoor ambient sensor open/short circuit.

The system uses this sensor to monitor outdoor air temperature and adjust compressor operation accordingly. When the control board cannot read a valid signal from the sensor due to a wiring break, corroded connector, or failed thermistor, it throws F3 and stops the unit to prevent operation without proper temperature feedback.

[Jump to Fix](#fix)

## Common Causes

- **Loose or corroded sensor connector** The plug at the outdoor ambient sensor or at the PCB has backed out, corroded, or developed high resistance due to oxidation or moisture intrusion.
- **Damaged sensor wiring** The harness between the outdoor ambient thermistor and the control board has a cut, pinch point, or broken wire causing an open circuit.
- **Failed outdoor ambient thermistor** The sensor itself has failed open, shorted internally, or drifted out of the normal resistance range and no longer tracks temperature correctly.
- **Faulty PCB sensor input circuit** The detecting circuit on the outdoor control board that reads the sensor signal has a component-level failure, even though the sensor and wiring are intact.

## Step-by-Step Fix {#fix}

1. **Power off the unit** at the breaker or disconnect to safely access the outdoor unit.
2. **Remove the outdoor unit cover** and locate the outdoor ambient sensor, typically a small thermistor mounted near the coil or on the chassis with a two-pin connector.
3. **Inspect the sensor connector and wiring** for loose plugs, corrosion, damaged pins, cuts, or pinch points in the harness running to the PCB, then reseat the plug firmly and check for continuity from sensor to board.
4. **Measure the sensor resistance** with a multimeter by unplugging the sensor and probing its terminals, then compare the reading to the thermistor resistance-versus-temperature table in your model's service manual.
5. **Test sensor response** by warming or cooling the thermistor body (for example, with hot or cold water on the tip) and watching resistance change smoothly, confirming the sensor tracks temperature correctly.
6. **Replace the outdoor ambient sensor** with a Gree-approved thermistor of the correct value if it reads open, shorted, or out of range, or if it does not respond to temperature change.
7. **Check the outdoor PCB** if a known-good sensor still triggers F3, inspect solder joints and traces around the sensor input, and replace the control board if the detecting circuit is faulty.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Gree outdoor ambient temperature sensor / thermistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-gree-mini-split-f3-error-code&k=Gree+outdoor+ambient+temperature+sensor+%2F+thermistor&tag=errorcodefixes-20) \| Match the resistance specification to your exact model number, consult Gree's thermistor table or parts diagram. |
| Outdoor unit control board / PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-gree-mini-split-f3-error-code&k=Outdoor+unit+control+board+%2F+PCB&tag=errorcodefixes-20) \| Required only if sensor and wiring test good but the fault persists, indicating a board-level detecting-circuit failure. |

## When to Call a Pro

Call a licensed HVAC technician if you are uncomfortable working with line-voltage electrical components or if you do not have a multimeter and the manufacturer's thermistor resistance table for your model. A technician can quickly measure the sensor, compare it to the spec, and determine whether the fault is in the sensor, harness, or control board. Also call a pro if you replace the outdoor ambient sensor with the correct part and the F3 code returns, since that points to a PCB-level repair that requires board-level diagnostics or a genuine Gree replacement board.
