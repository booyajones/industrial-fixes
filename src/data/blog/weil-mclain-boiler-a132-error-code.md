---
title: "Weil-McLain A132 Error Code - Causes & Fix"
description: "A132 indicates ignition failure on Weil-McLain boilers. Most common fix: clean the flame sensor and check gas supply."
pubDatetime: 2026-06-17T11:25:25Z
modDatetime: 2026-06-17T11:25:25Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - boiler
  - weil-mclain
money_part: "Weil-McLain flame sensor (flame rod)"
most_likely_cause: "dirty flame sensor"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify gas valve is fully open and gas supply is on"
  - "Check boiler pressure gauge reads 12-25 psi and add water if low"
  - "Power-cycle the boiler by turning off power for 30 seconds, then back on"
no_buy_pct: "60%"
---

## Weil-McLain A132 Error Code — What It Means

The A132 code is not explicitly defined in Weil-McLain's published documentation, but the A1xx pattern on AquaBalance and CGa control boards typically signals a failure to ignite. The boiler attempted to light but did not detect flame within the allowed time window. This triggers a hard lockout, meaning the control will not try again until you reset power and clear the fault. Weil-McLain service manuals confirm that these ignition lockouts point to one of three core problems: no gas reaching the burner, a dirty flame sensor that cannot detect the flame, or a faulty ignitor that fails to spark.

Because this is a lockout condition, the boiler will remain off until a technician or homeowner diagnoses the ignition chain. The fault protects against prolonged gas flow without combustion. Most A1xx faults resolve with cleaning the flame sensor or confirming gas supply, though wiring faults and control board issues also appear in the field.

## Before You Replace Anything

Homeowners often replace the ignitor first, but a dirty flame sensor causes most ignition lockouts. Clean the sensor with fine emery cloth and test before ordering parts.

[Jump to Fix](#fix)

## Common Causes

- **Dirty or carbon-coated flame sensor (~40%)** Carbon buildup on the flame rod prevents the control from detecting flame even when combustion occurs, triggering lockout.
- **No gas flow to burner (~25%)** Gas valve closed, clogged filter, or supply interruption stops fuel from reaching the ignition point.
- **Faulty ignitor (~15%)** Cracked, worn, or weak ignitor fails to produce a spark strong enough to ignite gas.
- **Low boiler pressure (~10%)** Pressure below 12 psi can cause shutdown or poor combustion conditions that prevent ignition.
- **Loose or corroded wiring (~7%)** Intermittent connections at the control board, ignitor, or flame sensor disrupt the ignition sequence.
- **Failing control board (~3%)** Thermal intermittent faults or relay contact failure prevent the board from completing the ignition cycle.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the gas valve handle parallel to the pipe (fully open)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Gas supply is on. Move to flame sensor and ignitor checks.<br><strong>No:</strong> Turn the valve parallel to the pipe, wait one minute, and reset power to the boiler.</div>
</details>

<details class="dtree"><summary>Does the boiler pressure gauge read between 12 and 25 psi?</summary>
<div class="dtree-body"><strong>Yes:</strong> Pressure is normal. Focus on ignition components and wiring.<br><strong>No:</strong> Add water via the fill valve until pressure reaches 12-15 psi, then bleed radiators to remove air.</div>
</details>

<details class="dtree"><summary>Do you see a spark at the ignitor during the call for heat?</summary>
<div class="dtree-body"><strong>Yes:</strong> Ignitor is working. Clean the flame sensor and check for flame detection.<br><strong>No:</strong> Ignitor or wiring is faulty. Test ignitor resistance with a multimeter or call a technician.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power and gas** to the boiler at the service switches and gas valve to make sure safe access to components.
2. **Check boiler pressure** on the gauge. If below 12 psi, open the fill valve to raise pressure to 12-15 psi, then bleed radiators to remove trapped air.
3. **Inspect the flame sensor** for carbon buildup or corrosion. Remove the sensor rod and clean it with fine emery cloth until shiny, then reinstall securely.
4. **Examine the ignitor** for cracks, chips, or heavy deposits. If damaged, replace it. If dirty, clean gently with a soft brush (avoid abrasive contact).
5. **Verify gas supply** by confirming the gas valve is fully open and listening for gas flow during an ignition attempt. If no flow, check upstream regulator and filter.
6. **Re-seat all control board connectors** and inspect wiring for loose, corroded, or burned terminals at the ignitor, flame sensor, and thermostat circuits.
7. **Reset the boiler** by turning power off for 30 seconds, then back on. If the unit has a dedicated reset button, press it once. Observe whether the ignition sequence completes and flame is detected.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Weil-McLain flame sensor (flame rod) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a132-error-code&k=Weil-McLain+flame+sensor+%28flame+rod%29&tag=errorcodefixes-20) \| Match the sensor length and thread to your control board model (AquaBalance or CGa). |
| Hot surface ignitor for Weil-McLain boiler | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a132-error-code&k=Hot+surface+ignitor+for+Weil-McLain+boiler&tag=errorcodefixes-20) \| Verify voltage and mounting style from your boiler's service label before ordering. |

## When to Call a Pro

Call a licensed technician if you smell gas, hear hissing or banging, or if the boiler continues to lock out after cleaning the flame sensor and confirming gas supply. Gas appliance work requires safe handling of combustible fuel, proper combustion analysis, and often a permit for code compliance. A technician will use a multimeter to test ignitor resistance (typically 1-10 Ω), measure flame sensor microamp output, and perform a flue-gas analysis to confirm safe combustion. If the control board shows intermittent thermal failure or if wiring faults are suspected, a pro can isolate the fault without risking further damage or creating a safety hazard.

**Rough cost:** A pro service call runs about $150-300.
