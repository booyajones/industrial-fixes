---
title: "Weil-McLain A121 Error Code - Causes & Fix"
description: "A121 is a lockout or fault history code on Weil-McLain boilers. Meaning varies by model. Check diagnostics menu and manual for exact cause."
pubDatetime: 2026-06-17T11:14:19Z
modDatetime: 2026-06-17T11:14:19Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - boiler
  - weil-mclain
money_part: "Thermistor or temperature sensor"
diy_or_pro: "pro"
free_checks:
  - "Check system pressure on the boiler gauge; if below 12 psi, add water to bring it to about 15 psi and see if the fault clears."
  - "Inspect the condensate drain and vent/intake pipes for blockage, ice, or debris and clear any obstruction."
  - "Enter the contractor diagnostics menu on your control (consult your manual) and read the exact fault code or lockout history."
---

## Weil-McLain A121 Error Code — What It Means

A121 appears as a lockout or fault history code on certain Weil-McLain boiler control systems. The exact meaning is not universal across all Weil-McLain models. The code is stored in the boiler control's contractor diagnostics or fault history menu, and the specific definition depends on your boiler's model number and control family. Weil-McLain documentation instructs technicians to enter the diagnostics menu, retrieve the active or past fault code, then match that code to the correct model manual for the exact meaning and corrective steps.

Because code meanings vary by control and boiler series, treating A121 as a single universal fault is not accurate. The verified workflow is to identify your exact boiler model and CP number, pull the fault history from the control, and consult the model-specific manual. Common lockout causes across Weil-McLain boilers include flame-sensing problems, gas supply issues, vent or intake blockage, condensate drain problems, low system pressure, circulation faults, sensor failures, high-limit trips, low-water cutoff faults, and gas valve issues.

## Before You Replace Anything

Do not replace the control board without first testing the thermistor, low-water cutoff sensor, and flame sensor. A documented service case involved a failed thermistor causing a false temperature lockout, not a bad board.

[Jump to Fix](#fix)

## Common Causes

- **Failed thermistor or low-water cutoff sensor (~25%)** A bad temperature sensor or low-water cutoff can send a false signal that triggers a safety lockout, preventing the boiler from firing.
- **Condensate drain blockage or vent obstruction (~20%)** A clogged condensate trap or blocked flue or intake pipe prevents safe combustion and triggers a lockout to protect the boiler.
- **Low system pressure (~15%)** If boiler pressure drops below about 12 psi, the control may lock out to prevent damage or unsafe operation.
- **Flame-sensing or ignition fault (~15%)** A dirty or failed flame sensor, or a gas supply interruption, can prevent reliable ignition and cause the control to lock out after repeated trials.
- **Circulation pump failure or airlocked system (~15%)** If the circulator does not run or the system is airbound, flow and temperature sensing can trip a safety lockout.
- **Faulty gas valve (~10%)** A gas valve that sticks closed or does not modulate correctly can prevent firing and trigger a lockout code.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the system pressure gauge reading below 12 psi?</summary>
<div class="dtree-body"><strong>Yes:</strong> Low pressure may be causing the lockout. Add water to bring pressure to about 15 psi, then reset the boiler and observe whether the fault clears.<br><strong>No:</strong> Pressure is adequate. Move on to check for blockages and fault history in the diagnostics menu.</div>
</details>

<details class="dtree"><summary>Is there a call for heat from the thermostat and does the circulator pump start?</summary>
<div class="dtree-body"><strong>Yes:</strong> The call and pump are working. Focus on gas supply, flame sensing, venting, and sensor diagnostics.<br><strong>No:</strong> No call or no pump means a wiring, thermostat, or circulator problem is blocking the boiler from starting. Check those circuits first.</div>
</details>

<details class="dtree"><summary>Can you see or hear the burner igniting when the boiler attempts to fire?</summary>
<div class="dtree-body"><strong>Yes:</strong> Ignition is occurring. The lockout is likely from a flame-sensing, vent, or sensor issue after ignition.<br><strong>No:</strong> No ignition suggests a gas supply fault, blocked vent/intake, or failed gas valve. Check gas pressure and venting before replacing parts.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Record the boiler model and CP number** from the rating plate so you can identify the correct manual and control family.
2. **Enter the contractor diagnostics menu** on the boiler control (follow the instructions in your model's manual) and read the active fault or lockout history to confirm the exact code and its stored definition.
3. **Check system pressure** on the boiler gauge. If it is below 12 psi, add water through the fill valve until the gauge reads about 15 psi, then reset the boiler.
4. **Inspect the condensate trap and drain** for clogs or standing water. Clear any blockage and verify the drain flows freely.
5. **Check the flue and intake pipes** for obstruction, ice, debris, or disconnected joints. Clear any blockage and verify proper termination.
6. **Test for a call for heat** at the thermostat and confirm the circulator pump starts when the boiler is commanded to fire.
7. **If the fault points to a sensor or safety input**, use a multimeter to test the thermistor, low-water cutoff, and any other temperature or pressure sensors according to the model's service manual specifications before replacing the control board or gas valve.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Thermistor or temperature sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a121-error-code&k=Thermistor+or+temperature+sensor&tag=errorcodefixes-20) \| Match the exact part number for your boiler model and control; generic sensors may not work. |
| Low-water cutoff sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a121-error-code&k=Low-water+cutoff+sensor&tag=errorcodefixes-20) \| Verify compatibility with your boiler series before ordering. |
| Flame sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a121-error-code&k=Flame+sensor&tag=errorcodefixes-20) \| Clean first; replace only if testing shows it is out of range or physically damaged. |
| Gas valve | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a121-error-code&k=Gas+valve&tag=errorcodefixes-20) \| Requires gas-certified technician to diagnose and replace safely. |

## When to Call a Pro

Call a licensed heating professional immediately if you are not comfortable working with gas, if the boiler continues to lock out after you have cleared blockages and checked pressure, or if diagnostic testing points to a failed sensor, gas valve, or control board. Gas-fired boiler work requires specialized tools, combustion analysis equipment, and knowledge of local codes. A technician will retrieve the exact fault history from the control, match the code to the correct manual, test all safety inputs and sensors, verify gas pressure and venting, and replace only the failed component. Weil-McLain strongly recommends that all service be performed by a qualified heating contractor, and warranty coverage often depends on proper professional service and part identification by model and CP number.

**Rough cost:** A pro service call runs about $150-400.
