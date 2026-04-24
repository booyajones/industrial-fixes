---
title: "WaterFurnace Geothermal Fault Code 1 — Low Pressure Lockout"
description: "WaterFurnace geothermal heat pump Fault Code 1 means low refrigerant pressure lockout. Learn the causes, diagnostic steps, and how to fix this geothermal fault."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - waterfurnace
  - geothermal
  - heat-pump
---

# WaterFurnace Geothermal Fault Code 1 — Low Pressure Lockout

**Fault Code 1** on WaterFurnace geothermal heat pumps (Series 7, Envision, 5 Series, and similar) indicates a low-pressure lockout on the refrigerant circuit. The unit has tripped the low-pressure switch and shut down to protect the compressor.

## Jump to Fix

- [Most Likely Cause](#most-likely-cause)
- [Diagnosis Steps](#diagnosis)
- [Parts](#parts)

## What Triggers Fault Code 1

The low-pressure switch monitors suction-side refrigerant pressure. When pressure drops below the trip setpoint (typically 40–60 psig for R-410A), the switch opens, the compressor shuts off, and Fault 1 is logged by the IntelliZone or Symphony II controller.

## Common Causes {#most-likely-cause}

| Cause | Likelihood | Season |
|---|---|---|
| Low refrigerant charge (leak) | High | Any |
| Dirty air coil / blower filter | High | Any |
| Low airflow across air coil | High | Any |
| Failing TXV (thermal expansion valve) | Medium | Any |
| Low loop fluid temperature | Medium | Winter |
| Air in the ground loop | Medium | Any |
| Failed or stuck low-pressure switch | Low | Any |

## Step-by-Step Diagnosis {#diagnosis}

**Step 1 — Check airflow**
- Inspect the air filter — replace if dirty
- Check blower motor operation and run capacitor
- Confirm all supply and return registers are open

**Step 2 — Check loop water temperature and flow**
- WaterFurnace geothermals require adequate loop flow: minimum 1.5 GPM per ton
- Measure entering water temperature (EWT) and leaving water temperature (LWT)
- In heating mode: if EWT is below 25°F, the unit may legitimately trip on low pressure
- Check loop pump operation — a failed loop pump causes rapid low-pressure trips

**Step 3 — Check refrigerant pressures**
- Connect gauges to the service ports on the refrigerant circuit
- Low-side pressure (R-410A): should be 90–120 psig in cooling, 80–100 psig in heating
- Significantly low suction pressure with normal loop temps = refrigerant leak

**Step 4 — Inspect the TXV**
- The TXV regulates refrigerant flow into the evaporator
- Symptoms of a failing TXV: suction pressure too low with normal EWT, frost on suction line near TXV
- Bulb may be loose or improperly clamped to suction line

**Step 5 — Test the low-pressure switch**
- With gauges connected, check pressure at switch trip
- The switch should remain closed above 40 psig (R-410A) in most models
- Inconsistent tripping at normal pressure = faulty switch

## Fault 1 Reset Procedure

WaterFurnace units allow up to 3 fault trips before hard lockout:
1. The Symphony II or IntelliZone controller displays the fault code
2. After correcting the cause, press the Reset button on the controller
3. If in hard lockout (fault repeated 3 times), power-cycle the unit at the circuit breaker

## Replacement Parts {#parts}

| Part | Notes |
|---|---|
| Low-pressure switch | [Amazon](https://www.amazon.com/s?k=Low-pressure+switch&tag=errorcodefixes-20) \| WaterFurnace part 8733800700 or equivalent |
| TXV assembly | [Amazon](https://www.amazon.com/s?k=TXV+assembly&tag=errorcodefixes-20) \| Must match refrigerant type and capacity |
| Loop pump | [Amazon](https://www.amazon.com/s?k=Loop+pump&tag=errorcodefixes-20) \| Grundfos or Bell & Gossett — match GPM and head |
| Blower run capacitor | [Amazon](https://www.amazon.com/s?k=Blower+run+capacitor&tag=errorcodefixes-20) \| Match µF and voltage |
> **Important:** WaterFurnace geothermal units require EPA 608-certified technicians for refrigerant work. Low refrigerant always means a leak — find and repair before recharging.
