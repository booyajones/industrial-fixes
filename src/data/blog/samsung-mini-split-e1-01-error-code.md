---
title: "Samsung Mini-Split E1-01 Error Code — Causes & Fix"
description: "What Samsung mini-split E1-01 means, why the outdoor temperature sensor faults, and how to fix it."
pubDatetime: 2026-04-22T10:00:00Z
modDatetime: 2026-04-22T10:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - mini-split
  - samsung
---

## Samsung Mini-Split E1-01 Error Code — What It Means

E1-01 on a Samsung mini-split (Wind-Free, AR series, and multi-zone systems) indicates an outdoor air temperature sensor fault. The control board is receiving a signal from the outdoor ambient temperature sensor that is outside the valid range — either an open circuit (sensor disconnected or broken) or a short circuit (sensor shorted). Samsung uses thermistor-type temperature sensors; the board compares the sensor resistance to a known curve and flags E1-01 when the reading is invalid.

[Jump to Fix](#fix)

## Common Causes

- **Failed outdoor temperature sensor (thermistor)** — The sensor element degrades over time, especially with UV exposure, moisture, or vibration on the outdoor unit. Open or shorted thermistors produce out-of-range readings.
- **Loose or corroded sensor connector** — The plug connecting the sensor wire to the outdoor control board can corrode or vibrate loose, breaking the circuit.
- **Damaged sensor wire** — Rodent damage, pinching by a panel edge, or UV degradation of wire insulation can break or short the sensor circuit.
- **Failed outdoor control board** — Rarely, the sensor input circuit on the board itself fails, causing false E1-01 readings even with a good sensor.

## Step-by-Step Fix {#fix}

1. **Locate the outdoor temperature sensor** — On Samsung outdoor units, the ambient temperature sensor is typically clipped to the intake area of the outdoor coil or mounted near the top of the outdoor unit chassis. It is a small probe with a 2-wire lead.
2. **Inspect the sensor and connector** — With power off, check the sensor connector on the outdoor control board for corrosion, bent pins, or a loose fit. Reseat the connector firmly.
3. **Test sensor resistance** — Disconnect the sensor from the board. Using a multimeter on resistance (ohms) mode, measure across the sensor leads. At room temperature (20–25°C), most Samsung thermistors read approximately 10–12 kΩ. Open circuit (OL) or near-zero (short) = replace the sensor.
4. **Inspect the sensor wire** — Trace the wire from the sensor to the board. Look for pinched, chewed, or cracked insulation. Repair or replace if damaged.
5. **Clear the fault and test** — After replacing the sensor or reseating the connector, restore power and power cycle the outdoor unit. Verify E1-01 does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Outdoor ambient temperature sensor | [Amazon](https://www.amazon.com/s?k=Outdoor+ambient+temperature+sensor&tag=errorcodefixes-20) \| Samsung OEM; 10 kΩ NTC thermistor; match connector |
| Sensor harness/extension wire | [Amazon](https://www.amazon.com/s?k=Sensor+harness%2Fextension+wire&tag=errorcodefixes-20) \| If wire run is damaged |
| Outdoor control board | [Amazon](https://www.amazon.com/s?k=Outdoor+control+board&tag=errorcodefixes-20) \| Only if sensor input circuit is confirmed failed on the board |
## When to Call a Pro

If sensor and wiring check out but E1-01 persists, the outdoor control board's sensor input circuit may need component-level repair or board replacement. A Samsung-authorized technician can access fault logs and confirm the board diagnosis.

## Related Articles

- [Bosch Heat Pump E1 Error Code — Causes & Fix](/posts/bosch-heat-pump-e1-error-code/)
- [Carrier 24ANA Heat Pump Error Codes — Performance Series Diagnostic Guide](/posts/carrier-24ana-heat-pump-error-codes/)
- [Carrier Heat Pump E1 Error Code — Causes & Fix](/posts/carrier-heat-pump-e1-error-code/)
- [Carrier Heat Pump E4 Error Code — Causes & Fix](/posts/carrier-heat-pump-e4-error-code/)
- [Carrier Heat Pump E5 Error Code — Defrost Fault: Causes & Fix](/posts/carrier-heat-pump-e5-error-code/)
