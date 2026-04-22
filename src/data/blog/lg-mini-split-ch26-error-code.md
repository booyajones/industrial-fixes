---
title: "LG Mini-Split CH26 Error Code — CT Sensor Fault"
description: "LG mini-split CH26 error code means a current transformer (CT) sensor fault on the outdoor unit. Learn causes, diagnostic steps, and how to fix LG CH26."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "ErrorCodeFixes"
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

| [Cause](https://www.amazon.com/s?k=Cause&tag=errorcodefixe-20) | Likelihood |
|---|---|
| [CT sensor failed or disconnected](https://www.amazon.com/s?k=CT%20sensor%20failed%20or%20disconnected&tag=errorcodefixe-20) | Very High |
| [CT sensor wiring harness loose or broken](https://www.amazon.com/s?k=CT%20sensor%20wiring%20harness%20loose%20or%20broken&tag=errorcodefixe-20) | High |
| [Outdoor PCB analog input failure](https://www.amazon.com/s?k=Outdoor%20PCB%20analog%20input%20failure&tag=errorcodefixe-20) | Medium |
| [CT sensor mounted incorrectly (not around wire)](https://www.amazon.com/s?k=CT%20sensor%20mounted%20incorrectly%20(not%20around%20wire)&tag=errorcodefixe-20) | Medium |
| [Actual compressor overcurrent (compressor fault)](https://www.amazon.com/s?k=Actual%20compressor%20overcurrent%20(compressor%20fault)&tag=errorcodefixe-20) | Low |

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
| [CT sensor (current transformer)](https://www.amazon.com/s?k=CT%20sensor%20(current%20transformer)&tag=errorcodefixe-20) | LG OEM part — match model number |
| [Outdoor PCB](https://www.amazon.com/s?k=Outdoor%20PCB&tag=errorcodefixe-20) | Only replace after confirming sensor and wiring are good |

## Reset Procedure

1. Repair or replace the CT sensor
2. Confirm connector is fully seated
3. Restore power and attempt restart
4. CH26 clears automatically on a successful startup if the sensor reads correctly

> **Note:** LG CH26 is sometimes confused with CH25 (compressor overcurrent). CH25 means the compressor actually drew too much current; CH26 means the measurement circuit itself has failed. The repair procedures are different — CH25 leads to the compressor, CH26 leads to the sensor.
