---
title: "Daikin C4 Error Code — Heat Exchanger Coil Sensor: Causes & Fix"
description: "What Daikin C4 means, why the coil sensor fails, and how to diagnose and fix C4 on Daikin mini-split systems."
pubDatetime: 2026-04-22T16:00:00Z
modDatetime: 2026-04-22T16:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - daikin
---

## Daikin C4 Error Code — What It Means

Daikin error code **C4** indicates an **indoor heat exchanger coil sensor fault**. The thermistor clipped to the indoor coil is reading out of range, open, or shorted. Daikin uses this sensor to monitor coil temperature for freeze protection, defrost termination logic, and capacity control.

[Jump to Fix](#fix)

## Common Causes

- **Failed indoor coil thermistor** — The NTC thermistor has drifted out of spec from age or moisture exposure.
- **Sensor slipped out of the coil fins** — If the sensor clip comes loose, the board sees inaccurate temperature and triggers C4.
- **Loose indoor PCB connector** — Vibration loosens the 2-pin thermistor connector over time.
- **Indoor PCB input fault** — Rare, but possible after moisture damage.

## Step-by-Step Fix {#fix}

1. Turn off power to the indoor unit.
2. Open the front panel and remove the filters.
3. Remove the screws holding the right-side electrical cover.
4. Locate the coil thermistor clipped into the evaporator coil.
5. Verify the sensor is fully seated in the coil fins.
6. Unplug the thermistor from the PCB and measure resistance. At room temperature, most Daikin thermistors read about 5–10 kΩ.
7. Replace the thermistor if it reads OL, 0 Ω, or far outside the expected range.
8. Re-seat the connector, restore power, and verify C4 clears.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Indoor coil thermistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-c4-error-code&k=Indoor+coil+thermistor&tag=errorcodefixes-20) \| Model-specific Daikin sensor |
| Indoor PCB | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-daikin-c4-error-code&tag=errorcodefixes-20) \| Only if thermistor and wiring test good |
## When to Call a Pro
If the sensor tests correctly but C4 returns, the indoor control board likely has a bad thermistor input circuit. A technician can confirm before you order a PCB.

## Related Articles

- [Daikin A3 Error Code — Causes & Fix](/posts/daikin-a3-error-code/)
- [Daikin Applied Chiller Fault Codes Guide — WMC / AGZ / ALZ Series](/posts/daikin-applied-fault-codes/)
- [Daikin C9 Error Code — Compressor Discharge Temperature Sensor Fault](/posts/daikin-c9-error-code/)
- [Daikin E1 Error Code Fix — Indoor Sensor Fault](/posts/daikin-e1-error-code/)
- [Daikin E3 Error Code — Causes & Fix](/posts/daikin-e3-error-code/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [Rheem EcoNet A101 error code fix](/posts/rheem-econet-a101-error-code/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Daikin U4 indoor-outdoor comm fault](/posts/daikin-error-code-u4/)

