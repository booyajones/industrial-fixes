---
title: "Emerson / White-Rodgers Thermostat E1 Error — Fault Code Guide"
description: "Emerson and White-Rodgers thermostat E1 error means a sensor fault or power issue. This guide covers all Emerson E1 variations and how to fix them by model."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - emerson
  - white-rodgers
  - thermostat
  - hvac
  - error-code
---

## Emerson / White-Rodgers Thermostat E1 Error

The **E1 error** on Emerson and White-Rodgers thermostats covers several different faults depending on the model series. Emerson (which acquired White-Rodgers) uses E1 to indicate:

- Indoor air temperature sensor fault
- Communication/power failure
- Sensor open or shorted

## E1 by Model Series

| Model Series | E1 Meaning |
|---|---|
| 1F80 (non-programmable) | Indoor sensor open or shorted |
| 1F86 (programmable) | Indoor sensor fault |
| 1F95 (touchscreen) | Indoor or outdoor sensor fault |
| UP500W (universal) | Sensor fault (indoor temp) |
| Sensi ST55U / ST75U | See separate Sensi guide |
| 1E78 (2-wire) | Power/low voltage |

## Indoor Sensor Fault — Most Common E1

The indoor air temperature sensor is built into the thermostat housing. It's a thermistor (temperature-sensitive resistor) that changes resistance with temperature. When the thermostat reads the sensor as open circuit (very high resistance) or short circuit (very low resistance), E1 appears.

### Causes of Sensor Fault

- **Physical damage** — thermostat dropped, cracked housing
- **Water damage** — condensation inside the unit, bathroom/laundry room installations
- **Age** — thermistors can drift or fail over time (common after 10+ years)
- **Incorrect location** — thermostat in direct sunlight, near a supply vent, or in a non-representative location

### Testing the Internal Sensor

At normal room temperature (70°F / 21°C), the sensor should read approximately:
- **10,000 ohms (10 kΩ)** on most White-Rodgers/Emerson units
- This varies by model — check the technical manual for your specific unit

To test: remove the thermostat from the wall, disconnect it from wiring, open the back panel (on models that allow it), and measure resistance across the sensor leads. If you read 0 or infinite resistance, the sensor is failed.

## What to Do When E1 Appears

**Step 1 — Note the room temperature.** If your home is genuinely outside the sensor's range (below 32°F or above 110°F), E1 may be a legitimate reading, not a fault.

**Step 2 — Remove and reattach the thermostat.** Sometimes vibration or brief power interruption triggers a temporary E1. Disconnect from wall plate for 30 seconds, reattach.

**Step 3 — Inspect for physical damage.** Look for cracks in the housing, signs of water intrusion, or burn marks. Any of these means replacement.

**Step 4 — Check wiring.** A wiring short that puts high voltage on the thermostat's sensing circuit can damage the sensor. Verify wiring is correct — only 18–24V class 2 wiring should be connected.

**Step 5 — Replace the thermostat.** Internal sensors on Emerson/White-Rodgers thermostats are not user-serviceable. If the sensor has failed, replace the unit.

## Recommended Replacements

| Model | Price | Features |
|---|---|---|
| Emerson 1F86U | $25–40 | Direct replacement, programmable |
| Emerson UP500W | $50–70 | Universal, touchscreen |
| Emerson Sensi ST75U | $70–100 | Wi-Fi, app control |
| White-Rodgers 1F78 | $15–25 | Budget, non-programmable |

## E1 vs. E2 on Emerson

- **E1** = Indoor temperature sensor fault
- **E2** = Outdoor temperature sensor fault (models with remote sensor input)
- **LL** = Low battery (some models show this instead of E-codes)

If you see E2 on an Emerson thermostat with an outdoor sensor probe, the fix is to replace the remote sensor, not the thermostat itself.
