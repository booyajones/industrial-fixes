---
title: "Rinnai Error Code 07 — Heat Exchanger High Temperature Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2026-04-26T18:15:00Z
modDatetime: 2026-04-26T18:15:00Z
slug: rinnai-error-code-07
featured: false
draft: false
tags:
  - rinnai
  - tankless
  - water-heater
  - heating
description: "Rinnai error code 07 means the secondary heat exchanger exceeded its temperature limit. Learn the causes, diagnosis steps, and fixes for non-SENSEI Rinnai models."
---

## Error Code: Rinnai Error Code 07

**What it means:** Error code 07 on Rinnai non-SENSEI tankless water heaters indicates that the secondary heat exchanger has exceeded its maximum allowable temperature. The unit's thermistor detected heat levels that could damage the heat exchanger, so the control board shut down the burner and locked out the unit as a protection measure.

This code is specific to non-SENSEI Rinnai models — the RU, V series, and older RL/RS line of condensing and non-condensing units. On these models, the secondary heat exchanger recovers additional heat from exhaust gases; when airflow through it is restricted or scale buildup reduces heat transfer, temperatures climb and code 07 results.

## Common Causes

- **Scale and mineral buildup inside the heat exchanger** — Hard water deposits coat the internal water passages of the heat exchanger over time. This insulating layer prevents heat from transferring to the water, causing the exchanger walls to overheat while the outlet water temperature actually drops. Scale is the #1 cause of code 07 on units older than 2–3 years in hard water areas.
- **Restricted airflow across the heat exchanger fins** — Lint, dust, or pet hair accumulating on the fin array reduces convective cooling from the combustion airstream. The exchanger retains heat it cannot shed, and temperatures rise.
- **Low water flow through the unit** — The minimum flow rate to activate a Rinnai burner is typically 0.26–0.75 GPM depending on model. A partially closed inlet valve, a clogged inlet filter screen, or a failing flow sensor can allow the burner to fire at full modulation with insufficient water moving through the exchanger.
- **Failed thermistor (temperature sensor)** — The thermistor monitoring the secondary heat exchanger can drift out of calibration or fail, sending a falsely elevated temperature reading that triggers lockout even when actual temperatures are normal.
- **Overfired burner** — Incorrect gas pressure, stuck-open gas valve, or wrong DIP switch settings (NG vs. LP) can cause the burner to fire hotter than designed, overwhelming the heat exchanger's capacity.

## Step-by-Step Diagnosis {#step-by-step-fix}

1. **Reset and check water flow first.** Turn the unit off and back on. Open a hot water tap fully and confirm strong flow. A weak stream or fluctuating flow points to a water supply or filter issue before any heat exchanger fault.

2. **Clean the inlet filter screen.** At the cold water inlet connection on the unit, there is a stainless mesh filter screen. Shut off the cold water supply, disconnect the inlet pipe, and remove the screen. Rinse it under running water and reinstall. A clogged screen is a frequent and easy-to-miss cause of low flow faults that lead to code 07.

3. **Inspect the heat exchanger fins.** Remove the front cover and visually inspect the fin array with a flashlight. If fins are clogged with debris, clean them with compressed air. Blow from the inside of the unit outward to push debris out through the vents.

4. **Flush and descale the heat exchanger.** If the unit is in a hard water area and more than 2 years old, descaling is almost certainly needed. Use a pump-based descaling kit to circulate food-grade white vinegar or a commercial descaling solution (like Rinnai's recommended descaler) through the heat exchanger for 45–60 minutes. This dissolves calcium and magnesium scale from the water passages.

5. **Check gas pressure.** If a manometer is available, verify static and dynamic gas pressure at the unit's gas valve test ports against the rating plate specifications. Overpressure causes the burner to overfire.

6. **Test the thermistor.** Disconnect the thermistor connector and measure resistance across its terminals with a multimeter. Compare the resistance reading to the temperature-resistance chart in the Rinnai service manual for your model. A reading that doesn't correspond to ambient temperature indicates a failed thermistor.

## How to Fix It

- **Scale buildup:** Descale the heat exchanger — this resolves the majority of code 07 faults on units 2+ years old. Install an inline water softener or scale inhibitor to prevent recurrence.
- **Dirty fins:** Clean with compressed air and consider adding an air filter to the installation if lint accumulation is a recurring problem.
- **Low flow:** Clean the inlet filter, check the pressure-balancing valve on the water heater, and confirm minimum supply pressure is met (minimum 15 PSI static).
- **Failed thermistor:** Replace the secondary heat exchanger thermistor — a simple connector-and-screw replacement accessible from the front of the unit.
- **Gas pressure:** Have a licensed technician adjust the gas regulator to spec.

## Parts You May Need {#parts-that-may-need-replacement}

| Part | Typical Cost | Where to Buy |
|------|-------------|-------------|
| Tankless Water Heater Descaling Kit | $30–$80 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-rinnai-error-code-07&k=tankless+water+heater+descaling+flush+kit&tag=errorcodefixes-20) |
| Rinnai Thermistor / Temperature Sensor | $20–$45 | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-rinnai-error-code-07&tag=errorcodefixes-20) |
| Rinnai Inlet Filter Screen | $5–$15 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-rinnai-error-code-07&k=Rinnai+tankless+water+heater+inlet+filter+screen&tag=errorcodefixes-20) |
| Rinnai Secondary Heat Exchanger | $300–$600+ | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-rinnai-error-code-07&k=Rinnai+secondary+heat+exchanger+tankless&tag=errorcodefixes-20) |
| Inline Scale Inhibitor / Water Conditioner | $25–$75 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-rinnai-error-code-07&k=inline+scale+inhibitor+tankless+water+heater&tag=errorcodefixes-20) |

## When to Call a Technician

If descaling and cleaning don't resolve code 07, the secondary heat exchanger itself may have developed a crack from thermal stress or the internal passages may be too heavily scaled to recover. Heat exchanger replacement is a significant repair — costs range from $500–$1,200 installed — and should be performed by a Rinnai-certified technician. Gas pressure adjustments also require a licensed professional with proper test equipment.

> **Pro tip:** Rinnai recommends flushing the heat exchanger with descaling solution annually in hard water areas (above 7 grains per gallon). A $40 annual flush can prevent a $600+ heat exchanger replacement. Install a whole-house water softener if your water hardness exceeds 10 GPG.

## Related Error Codes

- [Rinnai Error Code 10 — Condensate / Exhaust Blockage / Fan Fault](/posts/rinnai-error-code-10/)
- [Rinnai Error Code 14 — Thermal Fuse Fault](/posts/rinnai-error-code-14/)
- [Rinnai Error Code 33 — Heat Exchanger Outlet Temperature Fault](/posts/rinnai-error-code-33/)
- [All Rinnai Error Codes](/posts/rinnai-error-codes/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [Rheem Performance Platinum PDN tankless error codes](/posts/rheem-performance-platinum-pdn-error-codes/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Rinnai code 11 no-ignition fix](/posts/rinnai-error-code-11/)

## See Also

- [Rinnai Error Code 10 — Condensate / Exhaust Blockage / Fan Motor Fault Fix](/posts/rinnai-error-code-10/)
- [Rinnai Error Code 52 — Outlet Water Temperature Sensor Fault](/posts/rinnai-error-code-52/)
- [Rinnai Error Code 33 — Causes & Fix](/posts/rinnai-error-code-33/)
- [Rinnai Error Code 25 — Causes & Fix](/posts/rinnai-error-code-25/)
