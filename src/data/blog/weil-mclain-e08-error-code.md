---
title: "Weil-McLain Boiler Error Code E08 — Causes & Fix"
description: "What Weil-McLain E08 DHW sensor fault means, why it trips, and how to diagnose and fix it step by step."
pubDatetime: 2026-04-22T13:00:00Z
modDatetime: 2026-04-22T13:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
---

## Weil-McLain Boiler Error Code E08 — What It Means

The Weil-McLain **E08 error code** indicates a **domestic hot water (DHW) sensor fault** — the boiler's DHW temperature sensor (thermistor) is reading outside the valid operating range. On Weil-McLain combi-boilers and systems with an indirect water heater, the DHW sensor monitors the storage tank or heat exchanger temperature. E08 fires when the sensor reads an implausibly high or low temperature, indicating the sensor has failed open (infinite resistance) or shorted (near-zero resistance). The DHW circuit is disabled while the heating (space heating) circuit may continue to function.

[Jump to Fix](#fix)

## Common Causes

- **Failed DHW thermistor** — The sensor element has drifted out of range or failed completely; it no longer reports a valid resistance value to the control board.
- **Loose or corroded sensor connection** — The sensor wire connector at the control board or the sensor well has loosened or corroded, creating an intermittent open circuit that reads as E08.
- **Water leak at the sensor well** — If the sensor well has leaked and the area has corroded, the sensor may have been damaged by moisture.
- **Sensor wire damage** — A pinched or chafed wire in the sensor harness creates an intermittent open or short that triggers E08.

## Step-by-Step Fix {#fix}

1. **Locate the DHW sensor** — On Weil-McLain combi-boilers (e.g., WM97+CT), the DHW sensor is typically located on the storage tank or secondary heat exchanger. Consult the installation manual for the exact location on your model.
2. **Check the sensor connector** — Power off the boiler. Unplug the DHW sensor connector from the control board and re-seat it firmly. Check for green corrosion on the pins and clean with electrical contact cleaner.
3. **Test the sensor resistance** — Measure resistance across the DHW sensor terminals at room temperature (~70°F). Most Weil-McLain thermistors read 10–15 kΩ at 70°F. Open (OL) or very low resistance (under 1 kΩ) = failed sensor.
4. **Inspect the sensor wire harness** — Follow the wire from the sensor to the control board, checking for pinched sections, melted insulation, or a broken wire. Repair or replace the harness if damaged.
5. **Reset the boiler** — After replacing or reconnecting the sensor, press the RESET button on the boiler control. E08 should clear when the sensor returns a valid resistance value.

## Parts Often Needed

| Part | Notes |
|------|-------|
| DHW thermistor/sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-e08-error-code&k=DHW+thermistor%2Fsensor&tag=errorcodefixes-20) \| Match exact Weil-McLain part number for your model; resistance spec is model-specific |
| Sensor wire harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-e08-error-code&k=Sensor+wire+harness&tag=errorcodefixes-20) \| Replace if wire insulation is damaged between sensor and control board |
## When to Call a Pro

If E08 persists after replacing the DHW sensor and confirming all connections are clean, the control board's sensor input circuit may have failed. Control board replacement on Weil-McLain boilers involves gas system verification — a licensed HVAC or boiler technician should perform this work.

## Related Articles

- [American Water Heater Error Codes — Complete Guide](/posts/american-water-heater-error-codes/)
- [AO Smith Water Heater 3 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-3-flashes/)
- [AO Smith Water Heater 4 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-4-flashes/)
- [A.O. Smith Water Heater Error Codes Guide](/posts/ao-smith-water-heater-error-codes/)
- [Bradford White Water Heater Error Code 1 — Pilot Outage Fix](/posts/bradford-white-error-code-1/)

## See Also

- [Weil-McLain E04 Error Code — Causes & Fix](/posts/weil-mclain-e04-error-code/)
- [Weil-McLain Boiler Error Code E02 — Ignition Failure Fix](/posts/weil-mclain-e02-ignition-failure/)
- [Weil-McLain E06 Error Code — Ignition Lockout](/posts/weil-mclain-e06-error-code/)
- [Weil-McLain E02 Error Code — Causes & Fix](/posts/weil-mclain-e02-error-code/)
