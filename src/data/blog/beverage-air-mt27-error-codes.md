---
title: "Beverage-Air MT27 Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to Beverage-Air MT27 commercial refrigerator error codes, diagnostic LED codes, common fault causes, and step-by-step repair procedures."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - refrigeration
  - beverage-air
  - commercial-refrigeration
---

## Beverage-Air MT27 Error Codes — What They Mean

The Beverage-Air MT27 is a 27-cubic-foot one-section commercial reach-in refrigerator from Beverage-Air's MarketMax series. It is widely used in convenience stores, delis, and grab-and-go foodservice applications. The MT27 uses Beverage-Air's electronic controller, which displays error codes on the digital temperature display panel when faults are detected. Older MT27 units may use an analog temperature control without error code capability.

[Jump to Fix](#fix)

## Beverage-Air MT27 Electronic Controller Error Code Reference

| Code | Fault |
|---|---|
| E0 | EEPROM fault — controller memory error |
| E1 | Cabinet temperature sensor fault |
| E2 | Evaporator temperature sensor fault |
| E3 | High temperature alarm — cabinet above setpoint |
| E4 | Defrost cycle timeout |
| E5 | Door open alarm |
| E6 | Low temperature alarm |
| E7 | Condenser temperature sensor fault (where equipped) |
| Hi | High temperature display — reading above display limit |
| Lo | Low temperature display — reading below display limit |

## Common Causes by Code

- **E1 — Cabinet sensor** — NTC thermistor mounted in the interior of the MT27 cabinet. A broken wire at the door hinge or a corroded terminal at the board connector causes E1. Check the sensor lead routing before replacing the sensor.
- **E3 — High temperature** — For a single-section MarketMax unit, check the condenser coil at the base of the unit — these machines accumulate dust and grease in convenience store and deli environments quickly. A 3-month cleaning schedule is appropriate in these environments.
- **E4 — Defrost timeout** — The MT27 uses an electric defrost heater in the evaporator section. If defrost runs beyond the maximum duration (typically 30–45 minutes) without the evaporator reaching defrost termination temperature, E4 triggers. Check the defrost heater continuity and the termination thermostat.
- **E5 — Door alarm** — The MT27 door alarm activates when a door is held open beyond the configured time. In grab-and-go applications this is often a nuisance alarm. Adjust the door alarm delay time in the controller configuration if appropriate.
- **E0 — EEPROM fault** — The controller has lost its stored configuration parameters. This typically occurs after a power surge or after a battery-backed EEPROM loses its backup power. The controller will need to be re-configured with the correct setpoints and defrost settings.

## Step-by-Step Fix {#fix}

1. **View the code** — The Beverage-Air MT27 digital controller displays the error code on the temperature readout. If the code alternates with a temperature reading, it's a warning. If it's displayed alone, it's a lockout.
2. **For E3 (high temperature)** — Pull the MT27 away from the wall. The condenser is typically at the bottom rear. Clean with a coil brush or vacuum — in foodservice environments, grease can bind with dust to form a hard coating that won't vacuum off; use a coil cleaner spray.
3. **For E4 (defrost timeout)** — Remove the interior back panel. Check the evaporator for ice buildup — heavy ice indicates the heater is not running. Measure heater resistance (typically 15–50 Ω). Also check the defrost timer or control relay on the board.
4. **For E1 (cabinet sensor)** — Disconnect the sensor connector at the board and measure resistance at room temperature. A reading of 8–12 kΩ at 77°F (25°C) is typical for the NTC thermistor used in Beverage-Air units.
5. **For E0 (EEPROM)** — Enter the controller setup mode (press and hold the set button for 5 seconds on most MT27 controllers) and re-enter the temperature setpoint, high/low alarm thresholds, and defrost frequency. Consult the Beverage-Air controller manual for the full parameter list.

## Parts Often Needed

| Part | Notes |
|---|---|
| Cabinet temperature sensor | NTC thermistor; Beverage-Air part |
| Defrost heater | Match wattage to existing heater |
| Defrost termination thermostat | Check cutout temperature rating |
| Electronic controller | For E0; note model-specific programming needed |
| Door gasket | Magnetic; order by door style |
| Condenser fan motor | Match RPM and blade pitch |

## When to Call a Pro

Beverage-Air MT27 units with persistent high temperature (E3) after condenser cleaning should be checked for refrigerant charge by a licensed refrigeration technician. In convenience store environments, these units often run 24/7 and are subjected to high ambient temperatures — a system that was adequate at installation may be marginal 5–10 years later as component wear accumulates.
