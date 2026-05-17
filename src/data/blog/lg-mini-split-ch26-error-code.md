---
title: "LG Mini-Split CH26 Error Code — CT Sensor Fault"
description: "LG mini-split CH26 error code means a current transformer (CT) sensor fault on the outdoor unit. Learn causes, diagnostic steps, and how to fix LG CH26."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - hvac
  - lg
  - mini-split
  - outdoor-unit
---

# LG Mini-Split CH26 Error Code — CT Sensor Fault

**Error Code CH26** on LG mini-split and multi-zone systems indicates a current transformer (CT) sensor fault on the outdoor unit. The CT sensor monitors the compressor current draw and is critical for inverter compressor protection. When the sensor fails or reads outside its expected range, CH26 is triggered.

## Jump to Fix

- [Most Likely Cause](#most-likely-cause)
- [Diagnosis Steps](#diagnosis)
- [Parts](#parts)

## What Is the CT Sensor?

The CT (current transformer) sensor is a small toroidal coil that clamps around the compressor supply wire. It measures compressor current without direct electrical contact. The outdoor PCB reads this signal to protect the compressor from overcurrent and to control inverter frequency.

## Common Causes {#most-likely-cause}

| Cause | Likelihood |
|---|---|
| CT sensor failed or disconnected | Very High |
| CT sensor wiring harness loose or broken | High |
| Outdoor PCB analog input failure | Medium |
| CT sensor mounted incorrectly (not around wire) | Medium |
| Actual compressor overcurrent (compressor fault) | Low |

## Step-by-Step Diagnosis {#diagnosis}

**Step 1 — Locate the CT sensor**
- The CT sensor is inside the outdoor unit electrical compartment
- It is a small ring or clamp around the compressor power wire (typically the black wire on single-phase units)
- Visually confirm it is seated properly and the wire passes through the center of the ring

**Step 2 — Check the connector**
- The CT sensor connects to the outdoor PCB via a small 2-pin connector
- Disconnect and re-seat the connector firmly
- Inspect the connector for corrosion or bent pins

**Step 3 — Measure CT sensor output**
- The CT sensor outputs a small AC voltage proportional to current
- With unit running and a clamp meter on the output leads: verify millivolt-range AC signal
- If no signal while compressor is running: sensor is open — replace

**Step 4 — Check wiring**
- Trace the CT sensor wiring back to the outdoor PCB
- Look for pinched, cut, or melted wire insulation near sheet metal edges
- Check for condensate dripping on the connector causing corrosion

**Step 5 — Verify compressor operation**
- If the CT sensor and wiring are good, the board analog input may have failed
- Check for other related faults: compressor overcurrent codes, inverter faults
- If compressor is actually overloaded, fix the root cause (refrigerant, voltage)

## Replacement Parts {#parts}

| Part | Notes |
|---|---|
| CT sensor (current transformer) | [Amazon](https://www.amazon.com/s?i=industrial&k=CT+sensor+%28current+transformer%29&tag=errorcodefixes-20) \| LG OEM part — match model number |
| Outdoor PCB | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) \| Only replace after confirming sensor and wiring are good |
## Reset Procedure

1. Repair or replace the CT sensor
2. Confirm connector is fully seated
3. Restore power and attempt restart
4. CH26 clears automatically on a successful startup if the sensor reads correctly

> **Note:** LG CH26 is sometimes confused with CH25 (compressor overcurrent). CH25 means the compressor actually drew too much current; CH26 means the measurement circuit itself has failed. The repair procedures are different — CH25 leads to the compressor, CH26 leads to the sensor.

## Related Articles

- [Bosch Heat Pump E1 Error Code — Causes & Fix](/posts/bosch-heat-pump-e1-error-code/)
- [Carrier 24ANA Heat Pump Error Codes — Performance Series Diagnostic Guide](/posts/carrier-24ana-heat-pump-error-codes/)
- [Carrier Heat Pump E1 Error Code — Causes & Fix](/posts/carrier-heat-pump-e1-error-code/)
- [Carrier Heat Pump E4 Error Code — Causes & Fix](/posts/carrier-heat-pump-e4-error-code/)
- [Carrier Heat Pump E5 Error Code — Defrost Fault: Causes & Fix](/posts/carrier-heat-pump-e5-error-code/)
