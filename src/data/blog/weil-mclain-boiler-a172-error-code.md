---
title: "Weil-McLain A172 Error - Causes & Fix"
description: "A172 is not a standard Weil-McLain code. Check your model's manual for the real fault name. Most ignition faults trace to gas supply or dirty flame sensor."
pubDatetime: 2026-06-19T10:14:30Z
modDatetime: 2026-06-19T10:14:30Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
money_part: "Flame sensor rod"
diy_or_pro: "pro"
free_checks:
  - "Verify the gas valve is fully open and the main gas supply is on"
  - "Check for a thermostat or zone controller call and confirm power to the boiler"
  - "Reseat all connectors on the control module and inspect wiring for corrosion"
---

## Weil-McLain A172 Error — What It Means

A172 does not appear as a standard error code in Weil-McLain manufacturer documentation. Weil-McLain boilers use control-specific fault names and lockout codes that vary by model and control type. The code you see may be a display artifact, a shorthand notation, or a code specific to an aftermarket control. To find the actual fault, locate your boiler model number and consult the service manual or diagnostics menu on the control itself. Most Weil-McLain ignition-related lockouts involve gas flow problems, a dirty or failed flame sensor, a bad ignitor, or wiring issues at the control module.

## Before You Replace Anything

Technicians sometimes replace the control board when the real problem is a dirty flame sensor or loose connector. Clean the flame sensor and reseat all control module connectors before ordering a new board.

[Jump to Fix](#fix)

## Common Causes

- **Dirty or failed flame sensor (~30%)** Carbon buildup or corrosion on the flame sensor prevents it from detecting the flame, causing repeated lockouts even when the burner lights.
- **Gas valve closed or no gas flow (~25%)** If the manual shutoff valve is closed or the meter is off, the ignitor will spark but no flame will establish and the control will lock out.
- **Failed ignitor (~20%)** A cracked or worn-out ignitor will not produce a spark or will spark weakly, preventing ignition and triggering a fault.
- **Loose or corroded wiring and connectors (~15%)** Intermittent connections at the control module, limit circuit, or thermostat terminals cause the boiler to drop the call mid-sequence and lock out.
- **Low system pressure or circulation problem (~10%)** Air in the hydronic loop, a failing circulator pump, or pressure below operating range can trigger safety lockouts on some models.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the ignitor spark when the boiler tries to start?</summary>
<div class="dtree-body"><strong>Yes:</strong> Gas flow and the flame sensor are the next suspects. Verify the gas valve is open and clean the flame sensor rod.<br><strong>No:</strong> The ignitor, wiring to the ignitor, or the control module has failed. Check for power at the ignitor and inspect the wiring for breaks.</div>
</details>

<details class="dtree"><summary>Does the system pressure gauge read in the normal range (typically 12–25 psi for residential systems)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Pressure is acceptable. Focus on ignition components and gas supply.<br><strong>No:</strong> Add water to bring pressure into range, then bleed air from the system and restart.</div>
</details>

<details class="dtree"><summary>Does the fault clear after one reset and the boiler runs normally?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem may be intermittent wiring, a thermostat glitch, or temporary air in the gas line. Monitor for repeat faults.<br><strong>No:</strong> A component has failed. Do not keep resetting. Inspect the flame sensor, ignitor, and gas supply before calling for service.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Identify your boiler model and control type.** Locate the model tag on the jacket and find the service manual or wiring diagram for your exact unit.
2. **Check the diagnostics menu or fault history** on the control display to read the actual lockout name or fault description instead of relying on the A172 display.
3. **Verify gas supply and power.** Confirm the manual gas valve is fully open, the meter is on, and the boiler has 120 V power and a valid thermostat call.
4. **Inspect the ignitor and flame sensor.** Remove the burner access panel, check the ignitor for cracks, and clean the flame sensor rod with fine abrasive cloth or steel wool.
5. **Reseat all connectors** on the control module and inspect the wiring harness for loose pins, corrosion, or damage at the ignitor, flame sensor, and limit circuit terminals.
6. **Check hydronic system pressure and circulation.** Verify the pressure gauge reads in the normal operating range and bleed air from radiators or baseboard loops if needed.
7. **Reset once and observe the startup sequence.** Power-cycle the boiler or use the reset button, then watch for ignitor spark, flame establishment, and normal burner operation. If the same fault returns immediately, stop and repair the underlying cause before resetting again.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame sensor rod | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a172-error-code&k=Flame+sensor+rod&tag=errorcodefixes-20) \| Match the length and thread to your burner assembly. Clean first before replacing. |
| Hot-surface ignitor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a172-error-code&k=Hot-surface+ignitor&tag=errorcodefixes-20) \| Verify the ignitor type (silicon carbide or silicon nitride) and voltage rating for your model. |

## When to Call a Pro

Call a licensed heating technician if you cannot locate your boiler model manual, if the diagnostics menu shows a fault you do not understand, or if the problem involves the gas valve, control board, or any component inside the sealed combustion chamber. Gas work and control module replacement require proper combustion testing and code compliance. A pro will use a combustion analyzer to verify air-fuel ratio, check for carbon monoxide spillage, and test flame signal strength with a microamp meter. If you have already cleaned the flame sensor and confirmed gas supply but the fault persists, a technician can isolate whether the issue is the ignitor, the control, or a wiring fault without guessing.

**Rough cost:** A pro service call runs about $150–350.
