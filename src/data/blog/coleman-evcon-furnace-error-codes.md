---
title: "Coleman-Evcon Furnace Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to Coleman-Evcon furnace error codes, LED flash sequences, common fault causes, and step-by-step repair procedures for HVAC technicians."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - hvac
  - coleman
  - furnace
---

## Coleman-Evcon Furnace Error Codes — What They Mean

Coleman and Evcon furnaces are produced by Johnson Controls (the same manufacturer as York) and share control board designs and flash code systems with York residential furnaces. The Coleman-Evcon brand covers a range of 80%–96% AFUE models, including the DGAA, DGAB, ECOH, and TM9 series. If your furnace says "Coleman" or "Evcon" on the cabinet, this diagnostic guide applies.

[Jump to Fix](#fix)

## Coleman-Evcon Flash Code Reference

| Flash Count | Fault |
|---|---|
| 1 flash | Normal — standby |
| 2 flashes | Pressure switch stuck open |
| 3 flashes | Pressure switch stuck closed |
| 4 flashes | Open limit device |
| 5 flashes | Ignition failure lockout |
| 6 flashes | Rollout switch open |
| 7 flashes | Flame sensed without gas valve call |
| 8 flashes | Abnormal pressure switch operation during run |
| 9 flashes | Control board fault |
| Rapid flash | Low 24V control voltage |

## Common Causes by Code

- **2 flashes — Pressure switch open** — On 90%+ models, blocked condensate is the primary cause. On 80% models, check the flue pipe for blockage (bird nests are extremely common at the horizontal B-vent termination). Also check the pressure switch hose for cracks — the rubber tubing degrades over time on Coleman units.
- **3 flashes — Pressure switch stuck closed** — A condensate-flooded pressure switch hose holds the switch closed. Disconnect and drain the hose. Some Coleman models also have a secondary pressure switch that can fail in the closed position.
- **4 flashes — Limit open** — Air filter is the first check. Coleman-Evcon furnaces from the 1990s–2000s era often have undersized filter slots that get clogged faster than expected. Also check the blower wheel for debris accumulation (lint and pet hair wrap around the wheel and reduce airflow).
- **5 flashes — Ignition lockout** — Gas supply, igniter, and flame sensor are the three items to check in sequence. Coleman furnaces of this era use either a hot surface igniter (silicon carbide — more fragile) or a direct spark igniter depending on the model.
- **6 flashes — Rollout switch** — The rollout switch on Coleman furnaces is typically mounted on the burner box left side. It has a red manual reset button. Do not reset until you've checked for a blocked heat exchanger or excessive gas pressure.

## Step-by-Step Fix {#fix}

1. **Find the LED** — On most Coleman-Evcon furnaces, the diagnostic LED is on the control board, visible through a small window in the lower access panel. Some older models have the LED labeled "Fault" with a legend on the panel inside the door.
2. **For 2 flashes (pressure switch open)** — On an 80% model, go outside and look at the flue termination. A bird nest, wasp nest, or ice dam at the flue cap will cause immediate pressure switch faults. Remove the obstruction and restart.
3. **For 4 flashes (limit open)** — Replace the filter. If the filter is clean, check the blower capacitor — a weak capacitor drops blower RPM and reduces airflow below the threshold needed to prevent overtemperature. Measure capacitor µF and compare to the rating on the capacitor label.
4. **For 5 flashes (ignition lockout)** — Reset the furnace. Observe the ignition sequence through the sight glass. A silicon carbide igniter (orange colored ceramic element) should glow bright orange within 30 seconds. If it glows dim yellow, the igniter element is degraded and near failure.
5. **Low voltage (rapid flash)** — Measure 24VAC at the R-to-C terminals on the control board. If below 18VAC, disconnect all thermostat wires from the board and recheck — a shorted thermostat wire loads the transformer secondary. Replace the transformer if voltage is still low with all wires disconnected.

## Parts Often Needed

| Part | Notes |
|---|---|
| HSI igniter — silicon carbide | [Amazon](https://www.amazon.com/s?i=industrial&k=HSI+igniter+%E2%80%94+silicon+carbide&tag=errorcodefixes-20) \| Fragile; handle by wire leads only |
| Flame sensor | [Amazon](https://www.amazon.com/dp/B0CZ7M9V4D?tag=errorcodefixes-20) \| Clean with fine steel wool; rod-type |
| Pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?tag=errorcodefixes-20) \| Check hose first; Coleman-brand switches are direct replacements |
| Blower capacitor | [Amazon](https://www.amazon.com/s?i=industrial&k=Blower+capacitor&tag=errorcodefixes-20) \| Single-run capacitor on PSC motor |
| High-limit switch | [Amazon](https://www.amazon.com/dp/B0BN3TRG9R?tag=errorcodefixes-20) \| Check reset type — most Coleman are auto-reset |
| Rollout switch | [Amazon](https://www.amazon.com/dp/B0BN3TRG9R?tag=errorcodefixes-20) \| Manual reset; do not bypass |
## When to Call a Pro

Coleman-Evcon furnaces from the 1990s and early 2000s are reaching the end of their service life. A cracked heat exchanger is a serious CO risk and cannot be field-repaired — a professional inspection with a combustion analyzer is warranted on any furnace over 15 years old that is tripping rollout or limit switches repeatedly. A licensed HVAC technician should assess whether repair or replacement is the better investment.

## Related Articles

- [AirEase Furnace E1 Error Code — Causes & Fix](/posts/airease-furnace-e1-error-code/)
- [Amana Furnace 3 Flash Error Code — Causes & Fix](/posts/amana-furnace-3-flash-error-code/)
- [American Standard Furnace 3 Flash Error Code — Causes & Fix](/posts/american-standard-furnace-3-flash/)
- [AO Smith Water Heater 3 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-3-flashes/)
- [AO Smith Water Heater 4 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-4-flashes/)
