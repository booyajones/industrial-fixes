---
title: "HVAC-E002 – Low Suction Pressure Alarm (<50 PSI on R-410A)"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-02-08T08:00:00Z
modDatetime: 2024-02-08T08:00:00Z
slug: hvac-e002-low-suction-pressure
featured: false
draft: false
tags:
  - hvac
  - suction-pressure
  - r-410a
  - refrigeration
description: "HVAC-E002 fires when suction pressure drops below 50 PSI on R-410A systems. Here's the systematic diagnostic process to find the root cause."
---

## Error Code: HVAC-E002

*Technical Meaning:* Low suction pressure alarm — suction pressure dropped below 50 PSI on an R-410A system. The system has locked out to prevent the compressor from running in a vacuum, which destroys bearing oil and causes slugging.

## Step-by-Step Fix

1. **Check evaporator coil for ice buildup** — inspect the indoor coil for frost or ice blocking airflow. A frozen coil is the fastest path to low suction pressure and will not clear until defrost completes.
2. **Verify airflow across the evaporator** — measure static pressure drop or use a velometer at supply registers. Low airflow starves the evaporator and pulls suction pressure down.
3. **Inspect blower belt tension** — a loose or broken belt reduces airflow immediately. Belt-driven air handlers are a common culprit in commercial systems.
4. **Check air filter restriction** — a severely clogged filter can drop suction pressure 20–40 PSI below normal. Replace if dirty.
5. **Measure superheat at the suction line** — high superheat (>20°F on a TXV system) indicates a starved evaporator from low charge, restricted TXV, or blocked liquid line.
6. **Inspect TXV for stuck-closed condition** — warm the TXV sensing bulb with your hand. Suction pressure should rise. No change = TXV likely stuck or lost its charge.
7. **Add refrigerant if subcooling confirms undercharge** — check subcooling at the liquid line service port. Less than 5°F subcooling on R-410A confirms low charge. Add refrigerant per manufacturer spec.

## Saturation Reference (R-410A)

| Suction Pressure | Saturation Temp | Typical Condition |
|---|---|---|
| 70 PSI | 34°F | Low — investigate |
| 50 PSI | 20°F | Alarm threshold |
| 30 PSI | 3°F | Critical — compressor lockout |

> *Important:* Always resolve the root cause before adding refrigerant. If the system has a refrigerant leak, recharging without repair is a temporary fix and an EPA 608 violation for systems >5 lbs.
