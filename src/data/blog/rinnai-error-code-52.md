---
title: "Rinnai Error Code 52 — Outlet Water Temperature Sensor Fault"
description: "Rinnai tankless water heater Error Code 52 means the outlet water temperature sensor has failed. Learn causes, diagnostic steps, and the fix."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - plumbing
  - rinnai
  - tankless-water-heater
  - sensor
---

# Rinnai Error Code 52 — Outlet Water Temperature Sensor Fault

**Error Code 52** on Rinnai tankless water heaters indicates a fault with the outlet water temperature sensor (also called the outgoing hot water thermistor). The sensor has failed or is reading an out-of-range value, causing the unit to shut down to prevent scalding or heat exchanger damage.

## Jump to Fix

- [Most Likely Cause](#most-likely-cause)
- [Diagnosis Steps](#diagnosis)
- [Parts](#parts)

## Role of the Outlet Temperature Sensor

The outlet temperature sensor monitors the temperature of the water leaving the unit. This is the primary feedback for the modulating burner — if the sensor fails, the unit cannot regulate water temperature and shuts down safely with Error 52.

## Rinnai Temperature Sensor Codes

| Code | Sensor | Location |
|---|---|---|
| 52 | Outlet water temperature sensor | Outgoing hot water side |
| 53 | Inlet water temperature sensor | Incoming cold water side |
| 61 | Gas combustion fault | Not a sensor — burner issue |

## Common Causes {#most-likely-cause}

| Cause | Likelihood |
|---|---|
| Failed outlet temperature sensor | Very High |
| Corroded or loose sensor connector | High |
| Damaged sensor wire (water damage, pinching) | Medium |
| Control board analog input failure | Low |

## Step-by-Step Diagnosis {#diagnosis}

**Step 1 — Locate the outlet temperature sensor**
- The sensor is mounted on or near the outgoing water connection on the heat exchanger
- It is a small thermistor in a metal probe or clip
- Visually inspect for obvious damage, corrosion, or disconnected wires

**Step 2 — Check the wiring connector**
- Disconnect and re-seat the sensor connector at the control board
- Inspect for corrosion from condensate or water infiltration
- Clean contacts with electrical contact cleaner

**Step 3 — Measure sensor resistance**
Rinnai outlet temperature sensors are NTC thermistors:
- At 77°F (25°C): typically 10K–15K ohms (model-specific)
- Infinite resistance: sensor is open — replace
- Near-zero resistance: sensor is shorted — replace
- Resistance should decrease as temperature increases

**Step 4 — Compare to a reference**
- Take the sensor resistance reading and compare to the service manual resistance table
- Hold the sensor in your hand (roughly body temperature, ~98°F) and confirm resistance drops accordingly — confirms the sensor tracks temperature

**Step 5 — Check the control board**
- If the sensor resistance is correct but Error 52 persists, the board analog input may have failed
- This is uncommon — try a known-good replacement sensor first

## Replacement Parts {#parts}

| Part | Notes |
|---|---|
| Outlet temperature sensor | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-rinnai-error-code-52&tag=errorcodefixes-20) \| Rinnai part 100001223 or model-specific equivalent |
| Inlet temperature sensor (if confused with 53) | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-rinnai-error-code-52&tag=errorcodefixes-20) \| Rinnai part 100001222 |
| Control board | [Amazon](https://www.amazon.com/s?k=Control+board&tag=errorcodefixes-20) \| Last resort — verify sensor and wiring first |
## Reset Procedure

1. Replace the sensor
2. Reconnect all wiring
3. Press ON/OFF to power cycle the unit
4. Error 52 should clear on startup
5. Open a hot water fixture and verify stable outlet temperature

> **Note:** Rinnai Error 52 and Error 53 are often confused. Error 52 = outlet (hot water leaving the unit); Error 53 = inlet (cold water entering the unit). Both are fixed the same way — replace the failed sensor.
