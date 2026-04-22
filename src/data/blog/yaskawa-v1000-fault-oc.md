---
title: "Yaskawa V1000 OC Fault — Overcurrent"
description: "Yaskawa V1000 VFD OC fault means overcurrent has been detected. Learn the causes, how to diagnose OCA, OCb, and OC fault types, and how to fix the Yaskawa V1000 OC fault."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "ErrorCodeFixes"
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

| [Fault Code](https://www.amazon.com/s?k=Fault%20Code&tag=errorcodefixe-20) | Description |
|---|---|
| [OC](https://www.amazon.com/s?k=OC&tag=errorcodefixe-20) | Overcurrent — general |
| [OCA](https://www.amazon.com/s?k=OCA&tag=errorcodefixe-20) | Overcurrent during acceleration |
| [OCb](https://www.amazon.com/s?k=OCb&tag=errorcodefixe-20) | Overcurrent during deceleration |
| [OCC](https://www.amazon.com/s?k=OCC&tag=errorcodefixe-20) | Overcurrent during constant speed |
| [OC](https://www.amazon.com/s?k=OC&tag=errorcodefixe-20) | Overcurrent at stop or startup |

The specific variant tells you when in the cycle the overcurrent occurred, which helps identify the cause.

## Jump to Fix

- [Most Likely Cause](#most-likely-cause)
- [Diagnosis Steps](#diagnosis)
- [Parameters](#parameters)

## Common Causes {#most-likely-cause}

| [Cause](https://www.amazon.com/s?k=Cause&tag=errorcodefixe-20) | Fault Type | Likelihood | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | --- |---|---|
| Acceleration ramp too short | [OCA](https://www.amazon.com/s?k=OCA&tag=errorcodefixe-20) | Very High |
| [Motor stall (mechanical load jam)](https://www.amazon.com/s?k=Motor%20stall%20(mechanical%20load%20jam)&tag=errorcodefixe-20) | OCC | High | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Deceleration ramp too short | OCb | [High](https://www.amazon.com/s?k=High&tag=errorcodefixe-20) |  | Short circuit in motor cable | [OCA/OCC](https://www.amazon.com/s?k=OCA%2FOCC&tag=errorcodefixe-20) | Medium |
| [Failed output IGBT](https://www.amazon.com/s?k=Failed%20output%20IGBT&tag=errorcodefixe-20) | OCA | Medium | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | V/f profile mismatch for motor | OCA | [Medium](https://www.amazon.com/s?k=Medium&tag=errorcodefixe-20) |  | Ground fault on motor or cable | [OCA](https://www.amazon.com/s?k=OCA&tag=errorcodefixe-20) | Medium |
| [Motor too small for load](https://www.amazon.com/s?k=Motor%20too%20small%20for%20load&tag=errorcodefixe-20) | OCC | Low | [## Step-by-Step Diagnosis {#diagnosis}

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

## Key V1000 Parameters for OC Faults](https://www.amazon.com/s?k=%23%23%20Step-by-Step%20Diagnosis%20%7B%23diagnosis%7D%0A%0A**Step%201%20%E2%80%94%20Identify%20the%20fault%20variant**%0A-%20OCA%20(during%20acceleration)%3A%20usually%20a%20ramp%20time%20or%20motor%20parameter%20issue%0A-%20OCb%20(during%20deceleration)%3A%20usually%20ramp%20too%20short%3B%20try%20increasing%20deceleration%20time%0A-%20OCC%20(constant%20speed)%3A%20usually%20mechanical%20overload%20or%20stall%0A-%20OC%20at%20startup%3A%20may%20indicate%20short%20circuit%20%E2%80%94%20immediately%20check%20motor%20and%20cable%0A%0A**Step%202%20%E2%80%94%20Extend%20acceleration%20ramp%20(if%20OCA)**%0A-%20V1000%20Parameter%20C1-01%20(Acceleration%20Time%201)%3A%20increase%20by%2025%E2%80%9350%25%0A-%20Default%20is%2010%20seconds%20%E2%80%94%20try%2020%20seconds%20and%20see%20if%20OCA%20clears%0A%0A**Step%203%20%E2%80%94%20Check%20for%20mechanical%20jam**%0A-%20If%20the%20motor%20shaft%20cannot%20turn%20freely%3A%20check%20driven%20equipment%20for%20binding%2C%20seized%20bearings%2C%20or%20jam%0A-%20With%20power%20off%2C%20manually%20rotate%20the%20load%20%E2%80%94%20it%20should%20turn%20freely%0A%0A**Step%204%20%E2%80%94%20Megger%20test%20motor%20and%20cable**%0A-%20With%20drive%20output%20disconnected%2C%20megger%20from%20each%20phase%20to%20ground%0A-%20Below%201%20M%CE%A9%3A%20insulation%20failure%20%E2%80%94%20replace%20motor%20or%20cable%0A-%20This%20rules%20out%20a%20fault%20caused%20by%20ground%20leakage%20being%20misread%20as%20overcurrent%0A%0A**Step%205%20%E2%80%94%20Check%20the%20V%2Ff%20setting**%0A-%20Incorrect%20V%2Ff%20settings%20cause%20excessive%20magnetizing%20current%0A-%20V1000%20Parameter%20E1-01%20through%20E1-13%3A%20verify%20input%20voltage%20and%20motor%20base%20frequency%20match%20motor%20nameplate%0A-%20Running%20at%20full%20voltage%20before%20the%20motor%20reaches%20base%20speed%20causes%20OCA%0A%0A**Step%206%20%E2%80%94%20Check%20drive%20output%20transistors**%0A-%20With%20the%20motor%20disconnected%20and%20power%20off%20(wait%205%20minutes%20for%20bus%20discharge)%3A%0A-%20Measure%20from%20U%2C%20V%2C%20W%20output%20terminals%20to%20DC%2B%20and%20DC-%20with%20a%20multimeter%20on%20diode%20test%0A-%20A%20healthy%20IGBT%20shows%20one-way%20diode%20drop%3B%20a%20short%20in%20either%20direction%20%3D%20failed%20IGBT%0A%0A%23%23%20Key%20V1000%20Parameters%20for%20OC%20Faults&tag=errorcodefixe-20) | Parameter | Function | [OC-Related Setting](https://www.amazon.com/s?k=OC-Related%20Setting&tag=errorcodefixe-20) |  |---|---|---|
| [C1-01](https://www.amazon.com/s?k=C1-01&tag=errorcodefixe-20) | Acceleration Time 1 | Increase if OCA fault | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | C1-02 | Deceleration Time 1 | [Increase if OCb fault](https://www.amazon.com/s?k=Increase%20if%20OCb%20fault&tag=errorcodefixe-20) |  | L3-04 | [Stall Prevention — constant speed](https://www.amazon.com/s?k=Stall%20Prevention%20%E2%80%94%20constant%20speed&tag=errorcodefixe-20) | Adjust for heavy loads |
| [E1-01](https://www.amazon.com/s?k=E1-01&tag=errorcodefixe-20) | Input voltage setting | Must match actual supply | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | L3-02 | Stall Prevention — acceleration | [Enable for variable loads](https://www.amazon.com/s?k=Enable%20for%20variable%20loads&tag=errorcodefixe-20) | ## Replacement Parts | Part | [Notes](https://www.amazon.com/s?k=Notes&tag=errorcodefixe-20) |  |---|---|
| Yaskawa V1000 drive | [If output IGBT is shorted](https://www.amazon.com/s?k=If%20output%20IGBT%20is%20shorted&tag=errorcodefixe-20) |  | Motor | [If winding insulation failed](https://www.amazon.com/s?k=If%20winding%20insulation%20failed&tag=errorcodefixe-20) |  | Motor cable | Use shielded cable — 4-conductor VFD-rated |

> **Pro tip:** The Yaskawa V1000 supports online auto-tuning (parameter T1-01 = 2 for rotational auto-tune). Running auto-tune after a motor change or OC fault helps the drive learn the correct motor parameters and reduces OC trips.
