---
title: "LG Mini Split CH02 Error Code — Causes & Fix"
description: "What LG mini split CH02 error code means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - lg
---

## LG Mini Split CH02 Error Code — What It Means

LG mini split error code CH02 indicates an outdoor unit temperature sensor fault. The outdoor ambient temperature thermistor (or in some LG models, the discharge pipe temperature sensor) is reading outside its valid range or has an open/short circuit. The control board uses the outdoor ambient sensor to adjust compressor operation, defrost initiation, and capacity limits. When the sensor fails or reads an implausible value, the system shuts down to prevent operating outside its safe parameters. CH02 is almost always a sensor replacement job.

[Jump to Fix](#fix)

## Common Causes

- **Failed outdoor ambient thermistor** — The NTC thermistor element degrades over time, drifts outside calibration, or fails entirely (open or shorted). This is the most common cause of CH02 on LG mini-splits.
- **Damaged sensor wiring** — The sensor lead wire runs inside the outdoor unit cabinet and can be damaged by vibration, chafing against fan blades, or rodent activity. A partial break creates an intermittent resistance reading.
- **Moisture or corrosion at sensor connector** — The small JST or Molex connector on the thermistor can corrode in humid or coastal environments, creating a high-resistance connection the board interprets as a sensor fault.
- **Outdoor PCB fault** — Less commonly, the analog-to-digital converter channel on the outdoor control board fails, and it incorrectly reads the sensor. This is diagnosed by substituting a known-good sensor.

## Step-by-Step Fix {#fix}

1. **Locate the outdoor ambient sensor** — Open the outdoor unit service panel. The ambient temperature sensor is typically a small probe clipped to the outdoor coil fins or housed in a plastic bracket near the top of the unit. Follow the wire to identify it.
2. **Inspect the sensor connector** — Unplug the sensor connector at the outdoor PCB. Inspect both the sensor side and board side for corrosion, bent pins, or moisture. Clean with electrical contact cleaner if corroded.
3. **Test sensor resistance** — Using a multimeter on the Ω setting, measure resistance across the two thermistor leads. At 77°F (25°C), a typical NTC thermistor reads approximately 10 kΩ. Open circuit (OL) or near-zero ohms indicates a failed sensor.
4. **Check the sensor wire for damage** — Trace the wire from the sensor to the PCB. Look for cuts, pinch marks, or sections where insulation has worn through. Repair or replace as needed.
5. **Replace sensor and reset** — Install a manufacturer-matched replacement sensor, reconnect the harness, and restore power. Confirm CH02 clears on the next startup cycle.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Outdoor ambient temperature sensor | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-lg-mini-split-ch02-error-code&tag=errorcodefixes-20) \| Match the correct resistance curve; LG uses several variants |
| Sensor wire harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch02-error-code&k=Sensor+wire+harness&tag=errorcodefixes-20) \| Replace full harness if wire damage is extensive |
| Outdoor PCB | [Amazon](https://www.amazon.com/s?k=Outdoor+PCB&tag=errorcodefixes-20) \| Last resort; only after sensor and wiring are confirmed good |
## When to Call a Pro

If the replacement sensor clears CH02 temporarily but it returns within weeks, the outdoor PCB's ADC input channel may be intermittently failing. Board diagnosis and replacement require component-level familiarity with the LG control architecture.

## Related Articles

- [Bosch Heat Pump E1 Error Code — Causes & Fix](/posts/bosch-heat-pump-e1-error-code/)
- [Carrier 24ANA Heat Pump Error Codes — Performance Series Diagnostic Guide](/posts/carrier-24ana-heat-pump-error-codes/)
- [Carrier Heat Pump E1 Error Code — Causes & Fix](/posts/carrier-heat-pump-e1-error-code/)
- [Carrier Heat Pump E4 Error Code — Causes & Fix](/posts/carrier-heat-pump-e4-error-code/)
- [Carrier Heat Pump E5 Error Code — Defrost Fault: Causes & Fix](/posts/carrier-heat-pump-e5-error-code/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [LG washer error codes (complete guide)](/posts/lg-washer-error-codes/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [LG washer error code 31 (pressure / suspension fault)](/posts/lg-washer-error-code-31/)

## See Also

- [LG Washer Error Codes — Complete Fix Guide](/posts/lg-washer-error-codes/)
- [LG Mini Split CH01 Error Code — Causes & Fix](/posts/lg-mini-split-ch01-error-code/)
- [LG Mini-Split CH22 Error Code — Indoor Fan Motor Fix](/posts/lg-mini-split-ch22-error-code/)
- [LG Mini Split CH10 Error Code — Causes & Fix](/posts/lg-mini-split-ch10-error-code/)
