---
title: "Weil-McLain Boiler A169 Error Code - Causes & Fix"
description: "A169 on a Weil-McLain boiler is not consistently documented. Check your model manual. Most common causes are flame sensor, gas valve, or air switch."
pubDatetime: 2026-06-18T10:19:38Z
modDatetime: 2026-06-18T10:19:38Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - boiler
  - weil-mclain
money_part: "Flame sensor rod (flame probe)"
diy_or_pro: "pro"
free_checks:
  - "Check that system water pressure is at least 12-15 psi and bleed air from radiators or baseboards"
  - "Inspect intake and exhaust vent pipes for blockage, ice, condensate buildup, or debris"
  - "Verify thermostat is calling for heat and circuit breaker or fuse has not tripped"
---

## Weil-McLain Boiler A169 Error Code — What It Means

The exact meaning of code A169 is not consistently documented in public Weil-McLain materials and varies by boiler model and control generation. Your specific model manual or the fault table on the control board itself will give the authoritative definition. Most Weil-McLain lockout or no-heat faults that present as alphanumeric codes trace to one of a small set of problems: ignition or flame-proving failure, air-proving switch or venting issues, gas supply or gas valve faults, flame sensor contamination, thermistor or low-water cutoff problems, or circulation and pressure faults. Without the exact model documentation, treat A169 as a general lockout condition and work through the standard diagnostic sequence below.

## Before You Replace Anything

Technicians often replace the control board first when the real fault is a dirty flame sensor or poor ground connection. Clean the flame sensor rod with fine emery cloth and verify all ground wires are tight before condemning the board.

[Jump to Fix](#fix)

## Common Causes

- **Flame sensor contamination or poor grounding (~30%)** Carbon deposits or condensation on the flame rod prevent the control from proving flame, and loose or corroded ground wires cause intermittent rectification failures that trigger lockout.
- **Air-proving switch or venting fault (~25%)** Blocked intake or exhaust pipes, a stuck or failed air-proving switch, or condensate buildup stop the ignition sequence or cause shutdown after startup.
- **Gas supply or gas valve issue (~20%)** Closed manual gas valve, low gas pressure, or a failed gas valve coil prevent gas flow or stable flame carryover.
- **Low water pressure or circulation problem (~15%)** System pressure below 12 psi, trapped air, a failed circulator, or a stuck low-water cutoff trip safety limits and prevent firing.
- **Thermistor or temperature sensor fault (~10%)** A failed or out-of-spec thermistor sends false high-temperature or low-water readings that put the boiler into lockout.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the boiler attempt to fire (you hear the blower run or see igniter glow)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Ignition is starting. The fault is likely flame-proving (dirty sensor or poor ground), gas supply, or venting. Proceed with flame sensor cleaning and vent inspection.<br><strong>No:</strong> The boiler is not attempting ignition. Check power, thermostat demand, system pressure, and the air-proving switch. Low water or a stuck pressure switch will block startup.</div>
</details>

<details class="dtree"><summary>Is system water pressure at or above 12 psi when cold?</summary>
<div class="dtree-body"><strong>Yes:</strong> Pressure is adequate. Move to flame, gas, and venting checks.<br><strong>No:</strong> Repressurize the system through the fill valve and bleed air from high points. Low pressure trips the low-water cutoff and prevents firing.</div>
</details>

<details class="dtree"><summary>Are both intake and exhaust vent pipes clear of blockage, ice, or condensate?</summary>
<div class="dtree-body"><strong>Yes:</strong> Venting is open. Focus on flame sensor, gas valve, and ignition components.<br><strong>No:</strong> Clear the obstruction, remove any ice, and make sure condensate can drain freely. Blocked vents prevent the air switch from closing and stop ignition.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Locate your model number and control board** on the boiler jacket label and find the exact fault-code table in the model-specific manual or on the control itself, because A169 definitions vary by platform.
2. **Check system water pressure** at the gauge when the boiler is cold. If below 12 psi, open the fill valve to bring pressure to 12-15 psi and bleed air from all radiators or baseboard zones.
3. **Inspect intake and exhaust vent pipes** for blockage, ice, bird nests, or standing condensate. Clear any obstruction and verify the vent termination meets code clearances.
4. **Turn off power and gas** at the boiler switches and manual valve. Remove the burner or access cover to reach the flame sensor rod.
5. **Clean the flame sensor** with fine emery cloth or steel wool until the metal is bright and shiny. Check that all ground wires on the control and burner assembly are tight and free of corrosion.
6. **Restore power and gas** and call for heat. Watch the ignition sequence. If the burner lights and then drops out after a few seconds, the flame sensor or ground is still the problem. If no ignition occurs, verify gas pressure at the valve inlet and test the air-proving switch for continuity when the blower runs.
7. **Test the thermistor or temperature probe** with a multimeter if sensor fault is suspected. Compare resistance at room temperature against the model's published curve in the manual. Replace only if out of spec.
8. **If all field checks pass** and the fault persists, test for voltage at the gas valve during the call for heat. If voltage is present but the valve does not open, replace the gas valve. If no voltage, the control board or wiring is at fault.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame sensor rod (flame probe) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a169-error-code&k=Flame+sensor+rod+%28flame+probe%29&tag=errorcodefixes-20) \| Model-specific; verify part number from your boiler manual or original sensor before ordering. |
| Gas valve | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a169-error-code&k=Gas+valve&tag=errorcodefixes-20) \| Must match boiler model and gas type (natural or LP); confirm voltage and pilot/standing-pilot vs. electronic ignition. |
| Air-proving switch (pressure switch) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a169-error-code&k=Air-proving+switch+%28pressure+switch%29&tag=errorcodefixes-20) \| Verify switch set-point and hose connection type for your exact boiler series. |

## When to Call a Pro

Call a licensed boiler technician for any work involving gas piping, gas valve replacement, or pressure testing. If you are not comfortable working with 120V wiring, combustion air components, or interpreting control-board diagnostics, a professional will identify the fault safely and confirm proper combustion and venting after repair. A technician should also perform an annual combustion analysis and inspect the heat exchanger, because misdiagnosed or deferred repairs on a boiler can lead to carbon monoxide hazards or expensive secondary damage.

**Rough cost:** A pro service call runs about $150-400.
