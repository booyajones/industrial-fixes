---
title: "ClimateMaster Geothermal Error Code E1 — High Pressure Fault"
description: "ClimateMaster geothermal heat pump Error Code E1 means a high-pressure lockout. Learn the exact causes, diagnostics, and fixes for this geothermal fault."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - climatemaster
  - geothermal
  - heat-pump
---

# ClimateMaster Geothermal Error Code E1 — High Pressure Fault

**Error Code E1** on ClimateMaster geothermal heat pumps (Tranquility, Genesis, and similar series) indicates a high-pressure lockout on the refrigerant circuit. The high-pressure safety switch has tripped, and the compressor has shut down.

## Jump to Fix

- [Most Likely Cause](#most-likely-cause)
- [Diagnosis Steps](#diagnosis)
- [Parts](#parts)

## What Triggers E1

The high-pressure switch monitors refrigerant discharge pressure. For R-410A ClimateMaster units, the switch typically trips at 590–610 psig. When this pressure is exceeded, E1 is displayed on the Aurora or AXB control board.

## Common Causes {#most-likely-cause}

| [Cause](https://www.amazon.com/s?k=Cause&tag=errorcodefixe-20) | Likelihood | Mode | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | --- |---|---|
| High entering water temperature (loop too warm) | [Very High](https://www.amazon.com/s?k=Very%20High&tag=errorcodefixe-20) | Cooling |
| [Dirty or restricted air coil](https://www.amazon.com/s?k=Dirty%20or%20restricted%20air%20coil&tag=errorcodefixe-20) | High | Cooling | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Low airflow (dirty filter, failed blower) | High | [Cooling](https://www.amazon.com/s?k=Cooling&tag=errorcodefixe-20) |  | Refrigerant overcharge | [Medium](https://www.amazon.com/s?k=Medium&tag=errorcodefixe-20) | Any |
| [Failing TXV](https://www.amazon.com/s?k=Failing%20TXV&tag=errorcodefixe-20) | Medium | Any | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | High entering water temp in heating reversal | Low | [Heating](https://www.amazon.com/s?k=Heating&tag=errorcodefixe-20) |  | Defective high-pressure switch | [Low](https://www.amazon.com/s?k=Low&tag=errorcodefixe-20) | Any |

## Understanding Geothermal High Pressure

Unlike air-source heat pumps where high pressure occurs due to hot ambient air, geothermal high pressure in cooling mode is caused by **high loop water temperature**. If the loop is undersized or the ground has absorbed too much heat from a summer without recovery, EWT can rise to 90°F+, causing head pressure to spike.

## Step-by-Step Diagnosis {#diagnosis}

**Step 1 — Check entering water temperature (EWT)**
- In cooling mode, high EWT is the #1 cause of E1
- ClimateMaster Tranquility units: max rated EWT in cooling is typically 80–90°F depending on model
- Measure EWT at the inlet water connection
- EWT above 85°F on a hot day is a loop sizing/design issue, not an equipment failure

**Step 2 — Check airflow**
- Dirty filter causes E1 even with normal loop temps
- Check filter, blower motor, and run capacitor
- Confirm all supply registers are open

**Step 3 — Check refrigerant pressures**
- High-side pressure (R-410A, cooling): normal is 250–320 psig with EWT 70°F
- Above 400 psig at normal EWT = refrigerant overcharge or non-condensables
- Calculate subcooling at liquid line — above 20°F suggests overcharge

**Step 4 — Inspect TXV operation**
- Superheat should be 8–12°F at steady state
- Very low superheat with high head pressure = TXV stuck open or overcharged
- Very high superheat with high head pressure = TXV restricted

**Step 5 — Test high-pressure switch**
- Switch should be closed at ambient pressure (below 590 psig)
- If switch is open at normal pressure, replace it

## E1 Reset Procedure

ClimateMaster Aurora control boards:
1. Access the Aurora/AXB controller display
2. Navigate to Status > Fault Codes
3. Correct the root cause
4. Press Reset or power-cycle the unit

## Replacement Parts {#parts}

| Part | Notes |
|---|---|
| [High-pressure switch](https://www.amazon.com/s?k=High-pressure%20switch&tag=errorcodefixe-20) | ClimateMaster part 65D83 or equivalent |
| [TXV valve](https://www.amazon.com/s?k=TXV%20valve&tag=errorcodefixe-20) | Must match capacity and refrigerant type |
| [Blower run capacitor](https://www.amazon.com/s?k=Blower%20run%20capacitor&tag=errorcodefixe-20) | Match µF and voltage rating |
| [Loop pump](https://www.amazon.com/s?k=Loop%20pump&tag=errorcodefixe-20) | Check flow rate — minimum 1.5 GPM/ton |

> **Pro tip:** Persistent E1 faults during summer despite correct equipment operation usually indicate an undersized or overloaded ground loop. A ground loop flush and purge to remove air can sometimes improve loop performance.
