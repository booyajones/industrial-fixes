---
title: "Hoshizaki E9 Error Code — Causes & Fix"
description: "What Hoshizaki E9 error code means, why the evaporator temperature sensor faults, and how to diagnose and fix it."
pubDatetime: 2026-04-22T11:00:00Z
modDatetime: 2026-04-22T11:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - refrigeration
  - hoshizaki
---

## Hoshizaki E9 Error Code — What It Means

E9 on a Hoshizaki ice machine indicates a fault with the evaporator temperature sensor (also called the freezing plate thermistor or evaporator thermistor). The control board monitors this sensor to regulate the freeze cycle duration and determine when the ice sheet has reached proper thickness. When the control board detects that the sensor is reading out of range, open, or shorted, it displays E9 and halts ice production to prevent damage from an uncontrolled freeze cycle.

[Jump to Fix](#fix)

## Common Causes

- **Failed thermistor** — The evaporator sensor has failed open or short. Thermistors on commercial ice machines degrade from thermal cycling and moisture exposure over years of operation.
- **Loose sensor connector** — The thermistor plug has vibrated loose from the control board connector or from the sensor clip on the evaporator.
- **Damaged sensor wire** — The wire between the evaporator thermistor and the control board has broken or developed a high-resistance connection, especially where it passes near the evaporator frost line.
- **Faulty control board thermistor input** — The input circuit on the Hoshizaki control board has failed, misreading a good sensor as faulty.

## Step-by-Step Fix {#fix}

1. **Locate the evaporator sensor** — The E9 sensor is the thermistor clipped or attached to the evaporator (freezing grid or plate). On Hoshizaki crescent-cube machines, it is typically clipped to the evaporator manifold or inlet tube.
2. **Inspect the sensor and connector** — Check that the thermistor is properly clipped in its correct location and has not fallen out of the mounting point. Check the connector at the board for loose pins.
3. **Measure sensor resistance** — Disconnect the thermistor from the control board and measure resistance with a multimeter at the sensor leads. At 77°F (25°C), Hoshizaki evaporator thermistors typically read approximately 5–10 kΩ. An open (OL) or short (near 0Ω) confirms failure.
4. **Compare to a known good temperature** — If you have a thermometer reading of the sensor environment, cross-reference the expected resistance from the Hoshizaki service manual thermistor chart to confirm the sensor is out of spec.
5. **Replace the evaporator thermistor** — Order the Hoshizaki OEM evaporator sensor for your machine model. Clip it into the correct mounting location on the evaporator and reconnect the harness.
6. **Inspect the wiring harness** — If the sensor resistance was normal but E9 persisted, check the full harness from sensor to board for broken conductors or corroded connections.
7. **Reset and test** — Restore power and run a full ice production cycle. Confirm E9 is cleared and the machine harvests ice correctly.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Evaporator thermistor (E9 sensor) | [Amazon](https://www.amazon.com/s?k=Evaporator+thermistor+%28E9+sensor%29&tag=errorcodefixes-20) \| OEM Hoshizaki part; match to machine model number |
| Sensor wiring harness | [Amazon](https://www.amazon.com/s?k=Sensor+wiring+harness&tag=errorcodefixes-20) \| Replace if conductors are broken or connector pins corroded |
| Control board | [Amazon](https://www.amazon.com/s?k=Control+board&tag=errorcodefixes-20) \| Replace only if all sensors and wiring test good |
## When to Call a Pro

If the replacement thermistor does not clear E9, the control board input circuit has likely failed. Contact a Hoshizaki-authorized service agent for control board diagnosis and replacement.

## Related Articles

- [Hoshizaki C-101BAH / C-201BAH Countertop Ice Maker Error Codes — Full Fault Guide](/posts/hoshizaki-c-101bah-error-codes/)
- [Hoshizaki DKM-500 Cube Dispenser Error Codes — Fault Code Diagnostic Guide](/posts/hoshizaki-dkm-500-error-codes/)
- [Hoshizaki Ice Machine E1 Error Code — Water Inlet Fix](/posts/hoshizaki-e1-error-code/)
- [Hoshizaki E2 Error Code — Harvest Fault Fix](/posts/hoshizaki-e2-error-code/)
- [Hoshizaki E3 Error Code — Causes & Fix](/posts/hoshizaki-e3-error-code/)
