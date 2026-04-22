---
title: "Daikin C9 Error Code — Compressor Discharge Temperature Sensor Fault"
description: "Daikin error code C9 means the compressor discharge temperature sensor is faulty or out of range. Learn causes, diagnostic steps, and how to fix it."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - daikin
  - mini-split
  - vrf
---

# Daikin Error Code C9 — Compressor Discharge Temperature Sensor Fault

**Error Code C9** on Daikin mini-split and VRV systems means the compressor discharge temperature sensor has failed or is reading an out-of-range value. The outdoor unit control board cannot verify safe compressor discharge temperature, so it shuts down to protect the compressor.

## Jump to Fix

- [Most Likely Cause](#most-likely-cause)
- [Diagnosis Steps](#diagnosis)
- [Parts](#parts)

## What Is the Discharge Temperature Sensor?

The discharge temperature sensor (also called the Td sensor) is mounted on the compressor discharge line or embedded in the compressor discharge fitting. It monitors the temperature of refrigerant leaving the compressor — a critical parameter for protecting the compressor from overheating. Normal discharge temperatures range from 150–220°F depending on operating conditions.

## Common Causes {#most-likely-cause}

| Cause | Likelihood |
|---|---|
| Failed discharge temperature sensor | Very High |
| Loose or corroded sensor connector | High |
| Damaged sensor wiring (pinched or chafed) | Medium |
| Outdoor PCB fault (analog input failure) | Medium |
| Actual high discharge temperature (low refrigerant) | Low |

## Step-by-Step Diagnosis {#diagnosis}

**Step 1 — Check the sensor wiring**
- Disconnect power to the outdoor unit
- Locate the Td sensor on the discharge pipe (usually a small bullet-style sensor secured with a clamp)
- Check the wiring harness connector — push in firmly to reseat
- Inspect wire for pinching, cuts, or chafing near sheet metal edges

**Step 2 — Measure sensor resistance**
Daikin discharge temperature sensors are typically NTC thermistors:
- At 77°F (25°C): approximately 5K–10K ohms (model dependent)
- Open circuit (infinite ohms): sensor failed — replace
- Short circuit (near 0 ohms): sensor shorted — replace
- Check the Daikin service manual for the exact resistance-temperature curve for your model

**Step 3 — Compare to a reference temperature**
- With power off, use an infrared thermometer on the discharge pipe near the sensor
- Compare to the sensor resistance — if temperature is room temp but resistance is wildly off, sensor is failed

**Step 4 — Check the outdoor PCB input**
- Reconnect power, put a clamp meter on the compressor, and verify actual discharge temp correlates with what the board reads in the service monitor (accessible via BRC1 or ITC)
- If the board reads a fixed or maximum value while sensor resistance is correct, the board analog input has failed

**Step 5 — Check for actual high discharge**
- If the sensor resistance tracks correctly but readings are consistently above 230°F, the high discharge is real
- Causes: low refrigerant, failed TXV, non-condensables
- Check suction pressure and superheat before replacing sensor

## Replacement Parts {#parts}

| Part | Notes |
|---|---|
| Discharge temperature sensor (Td) | Daikin part 1634898 or model-specific equivalent |
| Outdoor unit PCB | Only replace if sensor and wiring check out |
| Sensor clamp / bracket | Ensure full contact with discharge pipe |

## Reset Procedure

After replacing the sensor:
1. Reconnect all wiring
2. Power up the outdoor unit
3. C9 should clear automatically on the next startup
4. Verify by running a cooling cycle and monitoring discharge temperature in the service monitor

> **Pro tip:** When ordering a Daikin discharge sensor, always confirm the model number from the outdoor unit nameplate. Sensor resistance curves vary between Daikin model families.
