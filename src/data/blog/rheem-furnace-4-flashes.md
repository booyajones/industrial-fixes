---
title: "Rheem Furnace 4 Flashes — Open High Temperature Limit Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-29T08:00:00Z
modDatetime: 2024-03-29T08:00:00Z
slug: rheem-furnace-4-flashes
featured: false
draft: false
tags:
  - hvac
  - rheem
  - furnace
  - limit-switch
description: "Rheem furnace 4 flashes means the high temperature limit switch has opened due to overheating. This guide covers every cause and fix for the Rheem/Ruud 4-flash fault."
---

## Error Code: Rheem/Ruud 4 Flashes

**What it means:** Four flashes on a Rheem or Ruud furnace means the high temperature limit device has opened. The high limit switch is a normally-closed bimetal switch mounted in the supply plenum or heat exchanger casing. It opens when plenum temperature exceeds its rated setpoint — typically 150–200°F depending on the furnace model and limit location. When the limit opens, the gas valve closes and the blower runs in continuous mode to cool the heat exchanger. If the limit resets on its own (most Rheem/Ruud limits are auto-reset) but the underlying cause persists, the fault will repeat.

## Common Causes

- **Clogged air filter** — Restricted return airflow causes heat to accumulate in the heat exchanger. The number one cause — always check the filter first.
- **Closed or obstructed supply registers** — Insufficient return air or restricted supply ducts traps heat.
- **Blower motor failure** — A blower that won't start or runs at reduced speed (bad capacitor, failed winding) leaves the heat exchanger unable to shed heat.
- **Dirty evaporator coil** — A clogged A-coil downstream of the furnace creates significant airflow restriction, raising temperatures upstream.
- **Incorrect blower speed tap** — If the furnace was installed with the blower on low speed, airflow may be insufficient for the BTU output. This is a setup error, not a component failure.
- **Cracked heat exchanger** — In some cases, a crack alters airflow patterns inside the exchanger, causing localized overheating that repeatedly trips the limit even with adequate system airflow.

## Diagnosis Steps

1. Check and replace the filter. If it's clogged, this is likely your only cause.
2. Verify all supply and return registers are open and unobstructed. Measure the temperature rise across the furnace — return air temperature in minus supply air out. Normal is 40–70°F. Above 70°F confirms restricted airflow.
3. Listen to the blower during a heat cycle. It should ramp to full speed within 60 seconds. A noisy, slow, or non-starting blower points to a motor or capacitor problem.
4. With a multimeter, check blower motor capacitor MFD. A capacitor reading more than 10% below its rated MFD is degraded — replace it.
5. If airflow is verified correct and the fault persists, inspect the limit switch itself. With power off and furnace cool, the switch should read continuity. An open reading on a cold limit confirms the switch has failed closed (welded contacts) or failed open.

## Fix

Filter replacement and airflow correction resolve the majority of Rheem 4-flash faults. If the blower capacitor is weak, replace it before the motor — it's a fraction of the cost and cures low-RPM issues in most cases.

If the limit switch has failed (won't reset or reads open when cold), replace it. Rheem/Ruud uses several limit configurations — the replacement must match the original's temperature rating, body style, and mounting configuration. Order by furnace model number.

If the fault recurs after airflow correction and limit replacement, have a licensed tech perform a heat exchanger inspection.

## Parts

| Part | Where to Buy |
|------|-------------|
| High limit switch | RepairClinic, SupplyHouse |
| Blower motor capacitor | Grainger, Amazon |
| PSC or ECM blower motor | RepairClinic, Grainger |

## When to Call a Technician

If the 4-flash fault returns after correcting airflow and replacing the limit switch, have a licensed HVAC tech inspect the heat exchanger. A cracked exchanger is a CO risk and should not be operated.
