---
title: "Weil-McLain Boiler A137 Error - Causes & Fix"
description: "A137 is not a universal Weil-McLain code. Check your model's fault history menu for the exact lockout cause-often ignition or sensor failure."
pubDatetime: 2026-06-17T11:29:59Z
modDatetime: 2026-06-17T11:29:59Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - boiler
  - weil-mclain
money_part: "Flame sensor / flame rod"
diy_or_pro: "pro"
free_checks:
  - "Check system water pressure-if below about 12 psi, refill to roughly 15 psi and purge air from the system."
  - "Verify gas supply is on and the manual shutoff valve at the boiler is fully open."
  - "Inspect venting and condensate drain (on condensing models) for ice, debris, or slope issues that block airflow."
---

## Weil-McLain Boiler A137 Error — What It Means

A137 does not appear as a standard fault code in Weil-McLain's published documentation. Weil-McLain boilers use model-specific controls that store detailed fault and lockout histories in a contractor diagnostics menu. The exact meaning of any displayed code depends on your specific boiler series, control board version, and CP number. Before replacing any parts, you must enter the diagnostics menu and retrieve the stored fault history to identify the actual lockout condition. Common lockout events logged by Weil-McLain controls include ignition failure, flame-proving issues, blower or air-proving faults, sensor errors (thermistor or low-water-cutoff), circulator or flow problems, and combustion or venting obstructions on condensing models.

Because the code is not universally defined, proceed by identifying your exact boiler model and control, retrieving the fault history, and then testing the suspected component rather than guessing. Many lockouts involve sensors giving false readings, failed igniters or flame rods, blocked vents or condensate drains, or low system pressure. Do not rely on the displayed code alone. Weil-McLain directs technicians to use the stored diagnostics and verify basic operating conditions before ordering parts.

## Before You Replace Anything

Many technicians replace the igniter or flame sensor first without testing them. Use a multimeter to check the flame rod signal and the thermistor resistance against the manual's table before ordering parts.

[Jump to Fix](#fix)

## Common Causes

- **Ignition or flame-proving failure (~30%)** A dirty or failed flame sensor, worn igniter, or unstable flame prevents the control from proving ignition and triggers a lockout.
- **Thermistor or low-water-cutoff sensor fault (~25%)** A failed temperature probe or low-water sensor sends false readings to the control, causing a false lockout even when water level and temperature are normal.
- **Low system pressure or flow problem (~20%)** Pressure below about 12 psi, air in the hydronic system, or a failed circulator prevents proper flow and trips the pressure or flow safety.
- **Blower or air-proving switch issue (~15%)** On models with induced-draft fans, a failed blower motor, blocked air intake, or stuck proving switch stops the ignition sequence.
- **Vent or condensate obstruction (condensing models) (~10%)** Ice, debris, or improper slope in the PVC vent piping or condensate drain blocks airflow or water drainage and triggers a safety lockout.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the system water pressure gauge reading below 12 psi?</summary>
<div class="dtree-body"><strong>Yes:</strong> Low pressure is likely causing the lockout. Refill the system to roughly 15 psi, purge air from radiators or baseboards, and check for leaks.<br><strong>No:</strong> Pressure is acceptable. Move on to check ignition and sensor components.</div>
</details>

<details class="dtree"><summary>Does the blower or draft fan start when the thermostat calls for heat?</summary>
<div class="dtree-body"><strong>Yes:</strong> Blower is running. Check for flame ignition and sensor signals in the diagnostics menu.<br><strong>No:</strong> No blower means a failed motor, stuck air-proving switch, or control board issue. A technician must test the circuit and motor.</div>
</details>

<details class="dtree"><summary>Do you see ice or water pooling near the vent pipes or condensate drain?</summary>
<div class="dtree-body"><strong>Yes:</strong> Vent or condensate blockage is likely. Clear ice, check drain slope, and make sure trap is filled with water.<br><strong>No:</strong> Venting and drainage are clear. Focus on flame sensor, thermistor, or circulator faults.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Record the exact boiler model number and CP number** from the rating plate so you can look up the correct fault-code table and parts list.
2. **Enter the contractor diagnostics menu** on the control panel (consult your installation manual for the button sequence) and retrieve the stored fault or lockout history to identify the actual error condition.
3. **Check system water pressure** at the gauge—if it is below about 12 psi, close the boiler isolation valves, refill through the fill valve to roughly 15 psi, then purge air from all zones and radiators.
4. **Verify gas supply and electrical power** by confirming the manual gas valve is open, the service switch is on, and the circuit breaker is not tripped.
5. **Inspect the flame sensor or flame rod** for carbon buildup and clean it with fine steel wool or emery cloth, then check the igniter for cracks or wear.
6. **Test thermistors and low-water-cutoff sensors** with a multimeter, comparing measured resistance to the values in your model's service table, and replace any sensor that reads out of range.
7. **Check the condensate drain and vent pipes** (on condensing boilers) for ice, debris, or sagging sections that trap water, and clear or re-slope as needed.
8. **Reset the boiler** after correcting the fault, observe a full ignition cycle, and confirm stable flame and no recurring lockout before leaving the system.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame sensor / flame rod | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a137-error-code&k=Flame+sensor+%2F+flame+rod&tag=errorcodefixes-20) \| Match the part number stamped on your existing rod to make sure the correct probe length and connector. |
| Igniter (hot-surface or spark electrode) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a137-error-code&k=Igniter+%28hot-surface+or+spark+electrode%29&tag=errorcodefixes-20) \| Verify whether your model uses a hot-surface igniter or spark ignition before ordering. |
| Thermistor or temperature sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a137-error-code&k=Thermistor+or+temperature+sensor&tag=errorcodefixes-20) \| Check the wiring diagram in your manual for the correct sensor location (supply, return, or outdoor reset) and resistance curve. |
| Circulator pump | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a137-error-code&k=Circulator+pump&tag=errorcodefixes-20) \| Note the voltage (usually 120 V), flange size, and flow rating stamped on your existing circulator. |

## When to Call a Pro

Call a licensed heating technician immediately if you smell gas, if the boiler repeatedly locks out after you reset it, or if you are unfamiliar with entering the diagnostics menu and interpreting fault codes. Because Weil-McLain fault codes are model-specific and the same display can mean different things on different controls, a technician with the correct service manual and diagnostic tools is essential for accurate troubleshooting. Gas-fired boiler work involves testing ignition circuits, combustion air proving, and venting—all of which require specialized training and a combustion analyzer to verify safe, efficient operation. If you have replaced a sensor or flame rod and the lockout persists, a professional must trace the wiring, test the control board outputs, and confirm that the root cause has been corrected rather than masked.

**Rough cost:** A pro service call runs about $200–500.
