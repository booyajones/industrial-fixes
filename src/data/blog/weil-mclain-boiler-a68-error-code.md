---
title: "Weil-McLain A68 Error Code - Causes & Fix"
description: "A68 means ignition failure: burner won't light. Most often a dirty flame sensor or no gas flow. Clean sensor or check gas supply first."
pubDatetime: 2026-06-15T11:26:56Z
modDatetime: 2026-06-15T11:26:56Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
money_part: "Flame Sensor (Weil-McLain)"
most_likely_cause: "dirty or failed flame sensor"
likelihood: "one of the most common causes"
diy_or_pro: "pro"
free_checks:
  - "Verify the gas valve is fully open and gas is flowing to the boiler"
  - "Power cycle the boiler by turning off power for 30 seconds then restore"
  - "Press the reset button once (no more than two resets in a row)"
part_price: "$25-60 for a flame sensor"
no_buy_pct: "40%"
---

## Weil-McLain A68 Error Code — What It Means

The A68 error code on a Weil-McLain boiler signals an ignition failure lockout. The control board started the ignition sequence (fan spin, ignitor activation, gas valve opening) but the flame sensor did not confirm a flame within the allowed time window. The system then enters a safety lockout to prevent unburned gas from accumulating.

This is a standard ignition lockout fault documented in Weil-McLain service manuals for gas boilers including CGa, CGI, and AquaBalance series. The lockout protects your home by shutting down the boiler until the fault is corrected and the system is manually reset.

## Before You Replace Anything

Many people replace the gas valve or control board before checking the flame sensor. Clean the sensor with fine emery cloth and verify gas supply before replacing any expensive components.

[Jump to Fix](#fix)

## Common Causes

- **Dirty or failed flame sensor (~30%)** Carbon buildup or sensor failure prevents the control board from detecting the flame even when the burner lights.
- **No gas flow (~25%)** Gas valve closed, faulty gas valve, or upstream supply issue stops fuel from reaching the burner during ignition.
- **Faulty ignitor (~20%)** Cracked, warped, or electrically open ignitor will not spark to light the gas.
- **Bad gas valve (~15%)** Valve stuck open, closed, or pilot valve defect prevents proper gas delivery during the ignition cycle.
- **Poor circulation or high limit trip (~7%)** Overheating due to failed circulator triggers high-limit safety lockout that mimics ignition failure.
- **Low water cutoff fault (~3%)** System shuts down if water level is too low, preventing ignition from starting.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the gas valve handle turned to the open position and do you smell gas near the boiler?</summary>
<div class="dtree-body"><strong>Yes:</strong> If you smell gas, evacuate immediately and call emergency gas services. Do not attempt any repair.<br><strong>No:</strong> Turn the gas valve fully open (handle parallel to pipe) and power cycle the boiler. If still no ignition, check the flame sensor and ignitor.</div>
</details>

<details class="dtree"><summary>After reset, does the ignitor glow bright orange during the startup sequence?</summary>
<div class="dtree-body"><strong>Yes:</strong> Ignitor is working. The problem is likely a dirty flame sensor or bad gas valve. Clean the sensor with fine emery cloth and test again.<br><strong>No:</strong> Ignitor is failed or has no power. Call a technician to test ignitor resistance (typically 40-100 Ω) and replace if faulty.</div>
</details>

<details class="dtree"><summary>Does the circulator pump make noise or feel hot to the touch during a call for heat?</summary>
<div class="dtree-body"><strong>Yes:</strong> Failed circulator may cause overheating and high-limit lockout. A technician should test circulation and verify high-limit settings.<br><strong>No:</strong> Circulation is likely fine. Focus diagnostic on ignition components: flame sensor, ignitor, and gas valve.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power and gas** to the boiler at the electrical disconnect and gas shutoff valve. Confirm no gas smell. If gas odor is present, evacuate and call emergency services.
2. **Verify gas supply** by checking that the gas valve is fully open (handle parallel to pipe). A technician can use a manometer to confirm inlet pressure is within spec for your fuel type.
3. **Inspect the flame sensor** by removing it from the burner assembly. Clean the sensor rod with fine emery cloth to remove carbon buildup. Check for continuity (should be less than 1 Ω). Replace if damaged.
4. **Check the ignitor** for cracks, warping, or discoloration. A technician should measure resistance (consult your model's manual for exact spec, often 40-100 Ω). Replace if open circuit or cracked.
5. **Test the gas valve** by listening for a click during the ignition cycle. A technician can measure coil resistance (spec varies by valve model) and verify the valve opens when powered.
6. **Review fault history** by accessing the Contractor Menu (hold UP and DOWN arrows for 10 seconds). Navigate to Diagnostics, Fault History, then Lockout History to confirm A68 and check for secondary codes.
7. **Reset and observe** by restoring power, waiting 30 seconds, then pressing the reset button once. Watch the startup sequence: fan, ignitor spark, gas valve, flame. Do not reset more than twice in a row. If ignition still fails, replace the identified faulty component.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame Sensor (Weil-McLain) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a68-error-code&k=Flame+Sensor+%28Weil-McLain%29&tag=errorcodefixes-20) \| Verify the part number for your specific boiler model (CGa, CGI, AquaBalance, etc.) before ordering. |
| Hot Surface Ignitor (Weil-McLain) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a68-error-code&k=Hot+Surface+Ignitor+%28Weil-McLain%29&tag=errorcodefixes-20) \| Match the resistance spec and mounting style to your burner assembly. Handle carefully during installation. |
| Gas Valve (Weil-McLain) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a68-error-code&k=Gas+Valve+%28Weil-McLain%29&tag=errorcodefixes-20) \| Model-specific part. Note the number of pins (e.g. 6-pin for CGI series) and voltage rating before ordering. |

## When to Call a Pro

Call a licensed HVAC technician immediately if you smell gas, if the boiler continues to lock out after two resets, or if you are uncomfortable working around gas appliances. Gas boiler repair requires specialized tools (manometers, multimeters, combustion analyzers) and knowledge of ignition timing, gas pressure specs, and combustion safety. A technician will measure ignitor resistance, test gas valve operation, verify flame sensor microamp readings, check circulation and high-limit settings, and access diagnostic menus to confirm the fault. Attempting DIY repair on gas systems can create carbon monoxide hazards or explosion risk if not done correctly. Most A68 faults are resolved in a single service call with sensor cleaning, ignitor replacement, or gas valve repair.

**Rough cost:** A pro service call runs about $150-350 depending on part and labor.
