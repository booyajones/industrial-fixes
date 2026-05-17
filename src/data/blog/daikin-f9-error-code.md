---
title: "Daikin F9 Error Code — Heat Exchanger Temp Sensor Fault: Causes & Fix"
description: "What Daikin F9 means, why the indoor heat exchanger thermistor fails, and how to diagnose and fix F9 on Daikin mini-splits."
pubDatetime: 2026-04-22T16:00:00Z
modDatetime: 2026-04-22T16:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - daikin
---

## Daikin F9 Error Code — What It Means

Daikin error code **F9** indicates a fault with the **indoor heat exchanger temperature sensor (thermistor)**. The sensor that monitors the indoor coil temperature for freeze protection and capacity control is reading outside the expected range. F9 appears on Daikin wall-mount, ceiling cassette, and floor-console indoor units.

[Jump to Fix](#fix)

On Daikin systems, F9 specifically refers to the **indoor heat exchanger midpoint thermistor** (also called the "liquid pipe thermistor" or "coil outlet thermistor"). This is separate from the room air temperature thermistor (which causes different codes).

## Common Causes

- **Failed thermistor** — After years of exposure to condensation and refrigerant temperatures (−5°F to 130°F cycling), the NTC thermistor resistance drifts out of spec. Complete failure shows as OL (open circuit) or 0 Ω (short circuit).
- **Loose or corroded connector** — The thermistor connects to the indoor PCB via a 2-pin plug. On Daikin indoor units, this connector is typically on the right side of the PCB. Vibration from fan operation loosens the connection.
- **Thermistor physically dislodged** — The sensor is held in the indoor coil fins by a clip. If the indoor unit was serviced, cleaned, or if the filter was replaced roughly, the thermistor clip may have been pulled off the coil. A thermistor hanging in air reads incorrect temperature.
- **Moisture on PCB** — Condensation in the indoor unit can reach the PCB and corrode the thermistor input circuit.

## Step-by-Step Fix {#fix}

1. **Remove the indoor unit front panel and filter** — on Daikin FTXS and FTXB series, the front panel lifts off the bottom edge and swings up. Remove the filters.
2. **Open the indoor unit chassis** — remove the bottom and side screws (typically 3–5 Phillips screws) to access the inside of the indoor unit.
3. **Locate the heat exchanger thermistor** — it's a small cylindrical sensor (about the size of a pencil eraser) clipped into the indoor coil. It has a 2-wire lead going to the PCB.
4. **Check the clip position** — verify the thermistor is seated in the coil fins, not hanging loose. Reseat it in the clip if it's dislodged.
5. **Test resistance** — unplug the connector from the PCB and measure resistance across the two sensor wires. At room temperature (~70°F / 21°C), a Daikin indoor coil thermistor typically reads 5–7 kΩ. Reading OL or 0 Ω means replacement.
6. **Re-seat the PCB connector** — if resistance is good, clean the PCB connector with contact cleaner and re-seat firmly.
7. **Restore power and test** — if F9 clears, the repair is complete. If it persists with a good thermistor and secure connector, the PCB sensor input may be damaged.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Indoor coil thermistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-f9-error-code&k=Indoor+coil+thermistor&tag=errorcodefixes-20) \| Daikin 1845004 or model-specific; verify pin count |
| Indoor PCB | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-daikin-f9-error-code&tag=errorcodefixes-20) \| Match to full model code; F9 from bad PCB is rare |
| Contact cleaner | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-f9-error-code&k=Contact+cleaner&tag=errorcodefixes-20) \| For connector maintenance |
## When to Call a Pro
If the thermistor and connector check out but F9 persists, the indoor PCB is likely the issue. PCB replacement is feasible for those comfortable with electronics, but sourcing the correct part number from the unit's model code is essential — Daikin has many PCB variants.

## Related Articles

- [Daikin A3 Error Code — Causes & Fix](/posts/daikin-a3-error-code/)
- [Daikin Applied Chiller Fault Codes Guide — WMC / AGZ / ALZ Series](/posts/daikin-applied-fault-codes/)
- [Daikin C4 Error Code — Heat Exchanger Coil Sensor: Causes & Fix](/posts/daikin-c4-error-code/)
- [Daikin C9 Error Code — Compressor Discharge Temperature Sensor Fault](/posts/daikin-c9-error-code/)
- [Daikin E1 Error Code Fix — Indoor Sensor Fault](/posts/daikin-e1-error-code/)
