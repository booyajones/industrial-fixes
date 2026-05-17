---
title: "Hoshizaki E4 Error Code — Causes & Fix"
description: "What Hoshizaki E4 error code means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - refrigeration
  - hoshizaki
---

## Hoshizaki E4 Error Code — What It Means

Hoshizaki error code E4 indicates an ice thickness sensor fault. The ice thickness sensor (also called the harvest sensor or thickness probe) monitors when the ice on the evaporator plate has grown to the correct harvest thickness before initiating the harvest cycle. When the E4 code appears, the control board has determined that the sensor is not functioning correctly — either reading ice present when no ice has formed, never registering ice thickness, or producing an implausible signal. This causes the machine to abort the freeze cycle prematurely or run too long, both of which can damage the unit or produce undersized ice.

[Jump to Fix](#fix)

## Common Causes

- **Mineral scale on ice thickness sensor** — Hard water mineral deposits (calcium, magnesium) accumulate on the stainless or plastic probe over time, insulating the probe tip from water contact and changing its electrical characteristics.
- **Failed ice thickness sensor** — The thermistor or conductive element inside the probe degrades and reads outside the valid range. Common on units with 3+ years of service.
- **Water flow not reaching sensor** — If the water distribution system is partially blocked, water may not be reaching the sensor probe area. The probe needs to be wetted by the water curtain to measure ice growth correctly.
- **Sensor wiring fault** — The wire from the sensor to the control board is broken, kinked, or corroded at the board connector. An open circuit creates a fault condition.

## Step-by-Step Fix {#fix}

1. **Clean the ice thickness sensor** — Mix a solution of Hoshizaki Ice Machine Cleaner (or a food-grade nickel-safe cleaner) per label directions. Circulate through the water system or manually apply to the sensor probe and evaporator plates. Rinse thoroughly with fresh water.
2. **Visually inspect the sensor and bracket** — Open the ice machine access panel. Locate the ice thickness sensor (a small probe protruding toward the ice evaporator). Check for mineral scale, physical damage, or probe displacement from its mounting bracket.
3. **Test sensor resistance** — Disconnect the sensor wire at the control board. Measure resistance across the sensor terminals. Compare against the spec in the Hoshizaki service manual. Resistance at ambient should be within the expected range for the sensor type (typically 5–15 kΩ at room temperature for NTC thermistors).
4. **Check water flow to sensor area** — Start a clean cycle and watch the water distribution during operation. Water from the distribution tube should visibly reach and flow over the sensor area. A blocked distribution hole reduces flow to the sensor.
5. **Replace sensor if readings are out of spec** — Order the Hoshizaki OEM thickness sensor for the specific model. Mounting typically involves a single screw or clip bracket. Replace the sensor and run a complete freeze/harvest cycle to confirm E4 clears.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Ice thickness sensor | [Amazon](https://www.amazon.com/s?i=industrial&k=Ice+thickness+sensor&tag=errorcodefixes-20) \| Must be OEM Hoshizaki; resistance curve is model-specific |
| Water distribution tube | [Amazon](https://www.amazon.com/s?i=industrial&k=Water+distribution+tube&tag=errorcodefixes-20) \| Replace if holes are blocked and cannot be cleared by cleaning |
| Ice machine cleaner (Hoshizaki branded) | [Amazon](https://www.amazon.com/s?i=industrial&k=Ice+machine+cleaner+%28Hoshizaki+branded%29&tag=errorcodefixes-20) \| Required for monthly/quarterly descaling in hard water areas |
## When to Call a Pro

If cleaning and sensor replacement don't clear E4, the control board's sensor input circuit may be faulty, or there may be a refrigeration system issue that's preventing ice growth entirely (meaning the sensor never sees ice because none is forming). A certified refrigeration technician can diagnose the full freeze cycle.

## Related Articles

- [Hoshizaki C-101BAH / C-201BAH Countertop Ice Maker Error Codes — Full Fault Guide](/posts/hoshizaki-c-101bah-error-codes/)
- [Hoshizaki DKM-500 Cube Dispenser Error Codes — Fault Code Diagnostic Guide](/posts/hoshizaki-dkm-500-error-codes/)
- [Hoshizaki Ice Machine E1 Error Code — Water Inlet Fix](/posts/hoshizaki-e1-error-code/)
- [Hoshizaki E2 Error Code — Harvest Fault Fix](/posts/hoshizaki-e2-error-code/)
- [Hoshizaki E3 Error Code — Causes & Fix](/posts/hoshizaki-e3-error-code/)
