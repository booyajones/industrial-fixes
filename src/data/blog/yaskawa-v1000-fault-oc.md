---
title: "Yaskawa V1000 OC Fault — Overcurrent"
description: "Yaskawa V1000 VFD OC fault means overcurrent has been detected. Learn the causes, how to diagnose OCA, OCb, and OC fault types, and how to fix the Yaskawa V1000 OC fault."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
  - v1000
  - overcurrent
---

# Yaskawa V1000 Fault OC — Overcurrent

The **OC fault** on the Yaskawa V1000 compact inverter drive means the drive's output current has exceeded the overcurrent trip level — approximately 200% of the drive's rated current for an instantaneous trip. The drive shuts down immediately to protect the output transistors and motor.

## V1000 OC Fault Variants

| Fault Code | Description |
|---|---|
| OC | Overcurrent — general |
| OCA | Overcurrent during acceleration |
| OCb | Overcurrent during deceleration |
| OCC | Overcurrent during constant speed |
| OC | Overcurrent at stop or startup |

The specific variant tells you when in the cycle the overcurrent occurred, which helps identify the cause.

## Jump to Fix

- [Most Likely Cause](#most-likely-cause)
- [Diagnosis Steps](#diagnosis)
- [Parameters](#parameters)

## Common Causes {#most-likely-cause}

| Cause | Fault Type | Likelihood |
|---|---|---|
| Acceleration ramp too short | OCA | Very High |
| Motor stall (mechanical load jam) | OCC | High |
| Deceleration ramp too short | OCb | High |
| Short circuit in motor cable | OCA/OCC | Medium |
| Failed output IGBT | OCA | Medium |
| V/f profile mismatch for motor | OCA | Medium |
| Ground fault on motor or cable | OCA | Medium |
| Motor too small for load | OCC | Low |

## Step-by-Step Diagnosis {#diagnosis}

**Step 1 — Identify the fault variant**
- OCA (during acceleration): usually a ramp time or motor parameter issue
- OCb (during deceleration): usually ramp too short; try increasing deceleration time
- OCC (constant speed): usually mechanical overload or stall
- OC at startup: may indicate short circuit — immediately check motor and cable

**Step 2 — Extend acceleration ramp (if OCA)**
- V1000 Parameter C1-01 (Acceleration Time 1): increase by 25–50%
- Default is 10 seconds — try 20 seconds and see if OCA clears

**Step 3 — Check for mechanical jam**
- If the motor shaft cannot turn freely: check driven equipment for binding, seized bearings, or jam
- With power off, manually rotate the load — it should turn freely

**Step 4 — Megger test motor and cable**
- With drive output disconnected, megger from each phase to ground
- Below 1 MΩ: insulation failure — replace motor or cable
- This rules out a fault caused by ground leakage being misread as overcurrent

**Step 5 — Check the V/f setting**
- Incorrect V/f settings cause excessive magnetizing current
- V1000 Parameter E1-01 through E1-13: verify input voltage and motor base frequency match motor nameplate
- Running at full voltage before the motor reaches base speed causes OCA

**Step 6 — Check drive output transistors**
- With the motor disconnected and power off (wait 5 minutes for bus discharge):
- Measure from U, V, W output terminals to DC+ and DC- with a multimeter on diode test
- A healthy IGBT shows one-way diode drop; a short in either direction = failed IGBT

## Key V1000 Parameters for OC Faults

| Parameter | Function | OC-Related Setting |
|---|---|---|
| C1-01 | Acceleration Time 1 | Increase if OCA fault |
| C1-02 | Deceleration Time 1 | Increase if OCb fault |
| L3-04 | Stall Prevention — constant speed | Adjust for heavy loads |
| E1-01 | Input voltage setting | Must match actual supply |
| L3-02 | Stall Prevention — acceleration | Enable for variable loads |

## Replacement Parts

| Part | Notes |
|---|---|
| Yaskawa V1000 drive | [Amazon](https://www.amazon.com/s?i=industrial&k=Yaskawa+V1000+drive&tag=errorcodefixes-20) \| If output IGBT is shorted |
| Motor | [Amazon](https://www.amazon.com/s?i=industrial&k=Motor&tag=errorcodefixes-20) \| If winding insulation failed |
| Motor cable | [Amazon](https://www.amazon.com/s?i=industrial&k=Motor+cable&tag=errorcodefixes-20) \| Use shielded cable — 4-conductor VFD-rated |
> **Pro tip:** The Yaskawa V1000 supports online auto-tuning (parameter T1-01 = 2 for rotational auto-tune). Running auto-tune after a motor change or OC fault helps the drive learn the correct motor parameters and reduces OC trips.

## Related Articles

- [Yaskawa A1000 OC Fault — Overcurrent](/posts/yaskawa-a1000-fault-oc/)
- [Yaskawa A1000 Fault UV1, DC Bus Undervoltage Causes & Fix](/posts/yaskawa-a1000-fault-uv1/)
- [Yaskawa A1000 Fault Code OC — Overcurrent Diagnosis & Fix](/posts/yaskawa-a1000-oc-fault-code/)
- [Yaskawa GA700 OC Fault — Overcurrent Fix](/posts/yaskawa-ga700-fault-oc/)
- [Yaskawa GA700 Fault UV1 — Main Circuit Undervoltage Causes & Fix](/posts/yaskawa-ga700-fault-uv1/)
