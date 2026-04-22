---
title: "Samsung Mini-Split E5-01 Error Code — Outdoor Coil Sensor Fault"
description: "Samsung mini-split error code E5-01 means the outdoor coil temperature sensor is faulty. Learn causes, diagnostic steps, and how to fix Samsung E5-01."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "ErrorCodeFixes"
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

| [Cause](https://www.amazon.com/s?k=Cause&tag=errorcodefixe-20) | Likelihood |
|---|---|
| [Failed outdoor coil sensor](https://www.amazon.com/s?k=Failed%20outdoor%20coil%20sensor&tag=errorcodefixe-20) | Very High |
| [Sensor pulled out of coil clip](https://www.amazon.com/s?k=Sensor%20pulled%20out%20of%20coil%20clip&tag=errorcodefixe-20) | High |
| [Wiring harness loose at PCB](https://www.amazon.com/s?k=Wiring%20harness%20loose%20at%20PCB&tag=errorcodefixe-20) | High |
| [Damaged sensor wire (pinched or corroded)](https://www.amazon.com/s?k=Damaged%20sensor%20wire%20(pinched%20or%20corroded)&tag=errorcodefixe-20) | Medium |
| [Outdoor PCB analog input fault](https://www.amazon.com/s?k=Outdoor%20PCB%20analog%20input%20fault&tag=errorcodefixe-20) | Low |

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
| [Outdoor coil temperature sensor](https://www.amazon.com/s?k=Outdoor%20coil%20temperature%20sensor&tag=errorcodefixe-20) | Samsung OEM — match model (10K or 15K NTC) |
| [Sensor mounting clip](https://www.amazon.com/s?k=Sensor%20mounting%20clip&tag=errorcodefixe-20) | Small plastic clip on coil tube — check it's intact |
| [Outdoor PCB](https://www.amazon.com/s?k=Outdoor%20PCB&tag=errorcodefixe-20) | Only if sensor swap doesn't clear the fault |

## Reset Procedure

After replacing the sensor:
1. Reconnect all wiring
2. Restore power to the outdoor unit
3. E5-01 should clear on the first startup attempt
4. Verify by running a cooling cycle and monitoring outdoor coil temperature via the service menu (if available)

> **Pro tip:** Samsung mini-split sensor resistance tables are included in the installation manual. Download the manual for your model from the Samsung HVAC partner portal — it lists resistance at multiple temperatures for accurate field diagnosis.
