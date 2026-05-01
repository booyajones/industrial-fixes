---
title: "Samsung Mini-Split E5-01 Error Code — Outdoor Coil Sensor Fault"
description: "Samsung mini-split error code E5-01 means the outdoor coil temperature sensor is faulty. Learn causes, diagnostic steps, and how to fix Samsung E5-01."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - samsung
  - mini-split
  - sensor
---

# Samsung Mini-Split Error Code E5-01 — Outdoor Coil Sensor Fault

**Error Code E5-01** on Samsung mini-split systems means the outdoor heat exchanger (coil) temperature sensor has failed or is reading an out-of-range value. The outdoor unit control board cannot monitor the coil temperature required for defrost and system protection, so it shuts down.

## Jump to Fix

- [Most Likely Cause](#most-likely-cause)
- [Diagnosis Steps](#diagnosis)
- [Parts](#parts)

## Understanding Samsung's Error Code Format

Samsung mini-splits use an E#-## format:
- **E5** = Temperature sensor category
- **-01** = Outdoor coil (heat exchanger) sensor

Other E5 variants:
- E5-01 = Outdoor coil sensor
- E5-02 = Discharge pipe sensor
- E5-03 = Suction pipe sensor

## What Is the Outdoor Coil Sensor?

The outdoor coil sensor monitors the temperature of the outdoor heat exchanger coil. In heat pump mode, it signals defrost initiation. In cooling mode, it helps detect refrigerant issues. It is typically a small NTC thermistor mounted in a clip directly on the coil tube.

## Common Causes {#most-likely-cause}

| Cause | Likelihood |
|---|---|
| Failed outdoor coil sensor | Very High |
| Sensor pulled out of coil clip | High |
| Wiring harness loose at PCB | High |
| Damaged sensor wire (pinched or corroded) | Medium |
| Outdoor PCB analog input fault | Low |

## Step-by-Step Diagnosis {#diagnosis}

**Step 1 — Locate the sensor**
- The outdoor coil sensor is clipped directly onto the coil tubing inside the outdoor unit
- Visually confirm it is still seated in its clip and in contact with the coil
- Sensor fallen out of its clip reads ambient air temperature — far from expected coil temp — triggering E5-01

**Step 2 — Check the wiring connector**
- Trace the sensor wire to the outdoor PCB connector
- Disconnect and re-seat the connector firmly
- Inspect for corrosion, bent pins, or moisture in the connector housing

**Step 3 — Measure sensor resistance**
Samsung outdoor coil sensors are NTC thermistors:
- At 77°F (25°C): approximately 10K–15K ohms (check model-specific chart)
- Infinite resistance: sensor open — replace
- Near-zero resistance: sensor shorted — replace
- Resistance tracks temperature inversely (cooler = higher resistance)

**Step 4 — Check the PCB input**
- If sensor resistance is correct but E5-01 persists, the PCB analog input may have failed
- Swap in a known-good sensor to confirm board-level fault before replacing PCB

## Replacement Parts {#parts}

| Part | Notes |
|---|---|
| Outdoor coil temperature sensor | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?tag=errorcodefixes-20) \| Samsung OEM — match model (10K or 15K NTC) |
| Sensor mounting clip | [Amazon](https://www.amazon.com/s?k=Sensor+mounting+clip&tag=errorcodefixes-20) \| Small plastic clip on coil tube — check it's intact |
| Outdoor PCB | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) \| Only if sensor swap doesn't clear the fault |
## Reset Procedure

After replacing the sensor:
1. Reconnect all wiring
2. Restore power to the outdoor unit
3. E5-01 should clear on the first startup attempt
4. Verify by running a cooling cycle and monitoring outdoor coil temperature via the service menu (if available)

> **Pro tip:** Samsung mini-split sensor resistance tables are included in the installation manual. Download the manual for your model from the Samsung HVAC partner portal — it lists resistance at multiple temperatures for accurate field diagnosis.

## Related Articles

- [Bosch Heat Pump E1 Error Code — Causes & Fix](/posts/bosch-heat-pump-e1-error-code/)
- [Carrier 24ANA Heat Pump Error Codes — Performance Series Diagnostic Guide](/posts/carrier-24ana-heat-pump-error-codes/)
- [Carrier Heat Pump E1 Error Code — Causes & Fix](/posts/carrier-heat-pump-e1-error-code/)
- [Carrier Heat Pump E4 Error Code — Causes & Fix](/posts/carrier-heat-pump-e4-error-code/)
- [Carrier Heat Pump E5 Error Code — Defrost Fault: Causes & Fix](/posts/carrier-heat-pump-e5-error-code/)
