---
title: "Weil-McLain E04 Error Code — Causes & Fix"
description: "What Weil-McLain E04 error code means, why the sensor faults, and how to fix it step by step."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
---

## Weil-McLain E04 Error Code — What It Means

Weil-McLain E04 indicates a **temperature sensor fault** — one of the boiler's thermistors (supply, return, or DHW sensor depending on the model) is reading outside its valid range. On Weil-McLain ultra and gas-fired condensing boilers, the control monitors multiple temperature points; an open or shorted sensor on any one of them triggers E04 and shuts down the boiler to prevent uncontrolled operation. The specific sensor that failed can often be identified by consulting the boiler's display history or service menu.

[Jump to Fix](#fix)

## Common Causes

- **Failed supply or return thermistor** — The most common cause; thermistors fail open or short after years of thermal cycling.
- **Loose sensor well connection** — The thermistor bulb may have backed out of the immersion well, losing contact with the water and reading ambient air temperature.
- **Corroded connector** — Moisture in the boiler room causes corrosion at the thermistor connector pins, increasing resistance past the valid range.
- **PCB thermistor input failure** — Uncommon, but the board's input circuit for one sensor can fail while others remain functional.

## Step-by-Step Fix {#fix}

1. **Read the fault history** — Access the boiler's diagnostics menu (consult your model's installation manual). Identify which sensor is flagged: supply (S1), return (S2), or DHW (S3). This narrows your search immediately.
2. **Inspect the sensor immersion well** — The thermistor probe inserts into a brass or stainless well in the water-side piping. Confirm the probe is fully seated and the mounting nut is tight. A partially withdrawn probe reads air temp.
3. **Check the connector** — Disconnect the sensor connector at the boiler control. Inspect for corrosion, pushed-out pins, or moisture. Clean with contact cleaner.
4. **Measure thermistor resistance** — Disconnect the sensor and measure resistance at room temperature (~70°F/21°C). Weil-McLain thermistors typically read ~10 kΩ at 77°F (25°C). Consult your model's table for exact specs. Out-of-range = replace.
5. **Replace the thermistor** — Drain the relevant section of piping (or the boiler if required), remove the immersion well thermistor, install the new sensor, and tighten to the specified torque.
6. **Reset and verify** — Power cycle the boiler (off for 30 seconds) and fire it through a complete heating cycle. Confirm E04 is cleared and supply/return temps display correctly on the control.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Supply thermistor (S1) | [Amazon](https://www.amazon.com/s?i=industrial&k=Supply+thermistor+%28S1%29&tag=errorcodefixes-20) \| Weil-McLain model-specific; verify for Ultra vs. Gold/CGa series |
| Return thermistor (S2) | [Amazon](https://www.amazon.com/s?i=industrial&k=Return+thermistor+%28S2%29&tag=errorcodefixes-20) \| Match immersion well length and resistance spec |
| DHW sensor (S3) | [Amazon](https://www.amazon.com/s?i=industrial&k=DHW+sensor+%28S3%29&tag=errorcodefixes-20) \| Only on combi models with domestic hot water capability |
## When to Call a Pro

If sensor replacement doesn't clear E04, the boiler control board may have a failed input. Weil-McLain control board replacement on condensing boilers requires proper setup and parameter configuration — have a licensed heating contractor handle board replacement to ensure the boiler is commissioned correctly.

## Related Articles

- [American Water Heater Error Codes — Complete Guide](/posts/american-water-heater-error-codes/)
- [AO Smith Water Heater 3 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-3-flashes/)
- [AO Smith Water Heater 4 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-4-flashes/)
- [A.O. Smith Water Heater Error Codes Guide](/posts/ao-smith-water-heater-error-codes/)
- [Bradford White Water Heater Error Code 1 — Pilot Outage Fix](/posts/bradford-white-error-code-1/)
