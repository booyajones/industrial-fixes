---
title: "Weil-McLain Boiler A177 Error - Causes & Fix"
description: "A177 is not a verified Weil-McLain fault code. Check your model's diagnostics menu and service manual for the exact meaning and fix."
pubDatetime: 2026-06-19T10:19:05Z
modDatetime: 2026-06-19T10:19:05Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
money_part: "Flame sensor rod"
diy_or_pro: "pro"
free_checks:
  - "Verify the incoming gas shutoff valve is fully open and gas is supplied to the building."
  - "Check that the boiler has power and the circuit breaker or disconnect switch is on."
  - "Access the fault-history or diagnostics menu on the control display and note the exact code and description shown."
---

## Weil-McLain Boiler A177 Error — What It Means

A177 could not be confirmed as a manufacturer-defined Weil-McLain fault code from available documentation. Weil-McLain control platforms use model-specific codes, and the exact meaning depends on the control family installed in your boiler. The code you see on the display may be an event-history entry, a lockout condition, or a code from a third-party control module. Most Weil-McLain ignition lockouts share common causes such as no gas flow, a dirty flame sensor, or a failed ignitor, but you must check the diagnostics or fault-history menu on your exact model and match it to the service manual before interpreting the code.

If your boiler is locked out and will not fire, the controller attempted an ignition sequence but did not prove flame. Common field issues include a closed gas shutoff valve, no incoming gas supply, a fouled flame sensor that cannot detect the flame, or a burned-out hot-surface ignitor. Do not repeatedly reset the lockout without correcting the underlying cause. Pull the full model number from the rating plate and consult the service manual to confirm the code definition and the correct diagnostic procedure for your control platform.

## Before You Replace Anything

Homeowners often replace the gas valve when the real problem is a dirty flame sensor or failed ignitor. Clean the sensor with fine sandpaper and verify ignitor glow and continuity before ordering a valve.

[Jump to Fix](#fix)

## Common Causes

- **Dirty or failed flame sensor (~35%)** The sensor rod is coated with soot or combustion residue and cannot detect flame even when the burner lights, causing a lockout.
- **Failed hot-surface ignitor (~25%)** The ignitor is cracked or burned out and does not heat enough to ignite the gas, preventing flame proving.
- **No gas supply or closed shutoff (~20%)** The manual gas valve is closed, the meter is shut off, or the supply line is empty, so no gas reaches the burner during the ignition sequence.
- **Faulty gas valve (~15%)** The valve does not open on command from the control, blocking gas flow even when the ignitor is hot and the inducer is running.
- **Control module or ignition board failure (~5%)** The control does not execute the ignition sequence correctly or misreads sensor signals, generating a false lockout code.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the boiler display show a different code or number when you check the diagnostics or fault-history menu?</summary>
<div class="dtree-body"><strong>Yes:</strong> Write down that code and match it to your model's service manual. The code you first saw may be a placeholder or event counter, not the active fault.<br><strong>No:</strong> Proceed to verify gas supply and check the flame sensor and ignitor for visible damage or heavy fouling.</div>
</details>

<details class="dtree"><summary>When the boiler tries to start, does the hot-surface ignitor glow bright orange for several seconds?</summary>
<div class="dtree-body"><strong>Yes:</strong> The ignitor is working. Check that the gas valve opens (listen for a click) and that the flame sensor is clean and properly grounded.<br><strong>No:</strong> The ignitor is likely failed or not receiving voltage. Measure continuity and replace the ignitor if open or cracked.</div>
</details>

<details class="dtree"><summary>Can you smell gas or hear the hiss of gas flow when the valve should open during the ignition attempt?</summary>
<div class="dtree-body"><strong>Yes:</strong> Gas is reaching the burner. If the ignitor glows but flame does not establish, inspect the burner orifices for blockage and verify ignitor position.<br><strong>No:</strong> No gas flow. Confirm the manual shutoff is open, incoming supply pressure is normal, and the gas valve is receiving the proper control signal.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Identify your exact model.** Locate the rating plate on the boiler jacket and write down the full model number and serial number.
2. **Access the diagnostics menu.** Press the button sequence on the control display (consult your manual) to view fault history and active error codes, and note the exact code shown.
3. **Match the code to the service manual.** Download or request the service manual for your model from Weil-McLain and look up the code definition and diagnostic procedure.
4. **Verify gas supply.** Confirm the manual gas shutoff valve upstream of the boiler is fully open, the building gas meter is on, and gas is flowing to other appliances if present.
5. **Inspect and clean the flame sensor.** Remove the sensor rod from the burner assembly, sand it lightly with fine-grit sandpaper or emery cloth to remove soot, and reinstall it with firm electrical contact.
6. **Check the hot-surface ignitor.** Look for cracks, breaks, or heavy carbon buildup. Measure continuity across the ignitor terminals (typically 50 to 150 ohms when cold). Replace if open or visibly damaged.
7. **Test the ignition sequence.** Restore power, initiate a call for heat, and watch for inducer startup, ignitor glow, gas-valve click, flame establishment, and flame-sensor proving. Use a multimeter to verify 24 VAC at the gas valve during the call if the valve does not open.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame sensor rod | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a177-error-code&k=Flame+sensor+rod&tag=errorcodefixes-20) \| Order by model number. Includes mounting hardware and wire connector. |
| Hot-surface ignitor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a177-error-code&k=Hot-surface+ignitor&tag=errorcodefixes-20) \| Match the voltage and mounting bracket to your burner assembly. Handle by the ceramic base only. |
| Gas valve (combination valve) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a177-error-code&k=Gas+valve+%28combination+valve%29&tag=errorcodefixes-20) \| Specify inlet and outlet thread size and voltage. Requires gas shutoff and purge before replacement. |
| Ignition control module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a177-error-code&k=Ignition+control+module&tag=errorcodefixes-20) \| Control-family specific. Verify the exact board part number from the service manual before ordering. |

## When to Call a Pro

Call a licensed heating technician if you cannot find the A177 code in your model's service documentation, if the boiler has no gas supply and you are not trained to work on gas piping or meters, or if you have cleaned the sensor and verified the ignitor but the lockout persists. Gas-fired boiler work involves combustion safety, gas-leak risk, and carbon-monoxide hazards. A qualified tech has calibrated combustion analyzers, manometers for gas-pressure measurement, and the training to diagnose control-module logic and flame-proving circuits safely. If the fault involves the main control board, gas valve, or burner assembly, professional replacement and combustion testing are required to restore safe operation and maintain any remaining warranty coverage.

**Rough cost:** A pro service call runs about $200-450.
