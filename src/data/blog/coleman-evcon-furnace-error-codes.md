---
title: "Coleman-Evcon Furnace Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to Coleman-Evcon furnace error codes, LED flash sequences, common fault causes, and step-by-step repair procedures for HVAC technicians."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "ErrorCodeFixes"
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

| [Flash Count](https://www.amazon.com/s?k=Flash%20Count&tag=errorcodefixe-20) | Fault |
|---|---|
| [1 flash](https://www.amazon.com/s?k=1%20flash&tag=errorcodefixe-20) | Normal — standby |
| [2 flashes](https://www.amazon.com/s?k=2%20flashes&tag=errorcodefixe-20) | Pressure switch stuck open |
| [3 flashes](https://www.amazon.com/s?k=3%20flashes&tag=errorcodefixe-20) | Pressure switch stuck closed |
| [4 flashes](https://www.amazon.com/s?k=4%20flashes&tag=errorcodefixe-20) | Open limit device |
| [5 flashes](https://www.amazon.com/s?k=5%20flashes&tag=errorcodefixe-20) | Ignition failure lockout |
| [6 flashes](https://www.amazon.com/s?k=6%20flashes&tag=errorcodefixe-20) | Rollout switch open |
| [7 flashes](https://www.amazon.com/s?k=7%20flashes&tag=errorcodefixe-20) | Flame sensed without gas valve call |
| [8 flashes](https://www.amazon.com/s?k=8%20flashes&tag=errorcodefixe-20) | Abnormal pressure switch operation during run |
| [9 flashes](https://www.amazon.com/s?k=9%20flashes&tag=errorcodefixe-20) | Control board fault |
| [Rapid flash](https://www.amazon.com/s?k=Rapid%20flash&tag=errorcodefixe-20) | Low 24V control voltage |

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
| [HSI igniter — silicon carbide](https://www.amazon.com/s?k=HSI%20igniter%20%E2%80%94%20silicon%20carbide&tag=errorcodefixe-20) | Fragile; handle by wire leads only |
| [Flame sensor](https://www.amazon.com/s?k=Flame%20sensor&tag=errorcodefixe-20) | Clean with fine steel wool; rod-type |
| [Pressure switch](https://www.amazon.com/s?k=Pressure%20switch&tag=errorcodefixe-20) | Check hose first; Coleman-brand switches are direct replacements |
| [Blower capacitor](https://www.amazon.com/s?k=Blower%20capacitor&tag=errorcodefixe-20) | Single-run capacitor on PSC motor |
| [High-limit switch](https://www.amazon.com/s?k=High-limit%20switch&tag=errorcodefixe-20) | Check reset type — most Coleman are auto-reset |
| [Rollout switch](https://www.amazon.com/s?k=Rollout%20switch&tag=errorcodefixe-20) | Manual reset; do not bypass |

## When to Call a Pro

Coleman-Evcon furnaces from the 1990s and early 2000s are reaching the end of their service life. A cracked heat exchanger is a serious CO risk and cannot be field-repaired — a professional inspection with a combustion analyzer is warranted on any furnace over 15 years old that is tripping rollout or limit switches repeatedly. A licensed HVAC technician should assess whether repair or replacement is the better investment.
