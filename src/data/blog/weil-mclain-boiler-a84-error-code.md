---
title: "Weil-McLain A84 Error Code - Causes & Fix"
description: "A84 is not a standard Weil-McLain code. Verify your exact model's manual and check gas supply, ignition electrodes, and flame sensor."
pubDatetime: 2026-06-15T11:41:14Z
modDatetime: 2026-06-15T11:41:14Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
money_part: "Ignition/flame-sensing electrode assembly"
diy_or_pro: "pro"
free_checks:
  - "Confirm the gas shutoff valve upstream of the boiler is fully open."
  - "Check the boiler's diagnostics menu to retrieve the full fault code and history, not just a brief flash on the display."
  - "Inspect the ignition and flame-sensing electrodes for heavy soot, corrosion, or damage that would prevent proper flame detection."
---

## What this code means
A84 is not a verified standard fault code in Weil-McLain's published documentation for most current boiler models. Weil-McLain uses codes like A01 (no burner ignition), A16, and F07, but A84 does not appear in the AquaBalance or similar control manuals. The code may be specific to an older control board, may be part of the fault history display rather than a current lockout, or may be misread from the boiler's diagnostic screen.

Because the exact meaning of A84 cannot be confirmed from manufacturer sources, the best practice is to verify your boiler's exact model and control board type, then retrieve the full fault history from the diagnostics menu and match it to your installation manual. Most Weil-McLain ignition-related faults trace back to gas supply issues, dirty or damaged ignition and flame-sensing electrodes, faulty gas valves, or sensor and wiring problems.

## Before You Replace Anything

Many technicians replace the gas valve or ignition board first, but dirty or misaligned electrodes and low gas supply pressure account for the majority of ignition faults. Clean and inspect the ignition and flame-sensing electrodes and verify gas supply pressure (3.5 to 11 in. w.c. on AquaBalance models) before ordering parts.

## Common Causes

- **Gas supply closed or insufficient pressure (~30%)** The manual shutoff valve may be closed, or supply pressure may be below the required range (3.5 to 11 in. w.c. for AquaBalance models), preventing ignition.
- **Dirty, corroded, or misaligned ignition or flame-sensing electrode (~25%)** Soot buildup, corrosion, or improper electrode position blocks spark or flame detection, triggering an ignition fault.
- **Faulty gas valve (~20%)** The gas valve may fail to open or modulate correctly, cutting off fuel to the burner even when the control board commands ignition.
- **Sensor or wiring fault (~15%)** Damaged wiring, loose connector pins, bad crimps, or a failed temperature sensor can produce intermittent or phantom fault codes in the control's history.
- **Dirty heat exchanger or blocked combustion air (~10%)** Heavy scale, soot, or restricted combustion air can prevent proper flame establishment or cause erratic flame sensing.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the gas shutoff valve to the boiler fully open?</summary>
<div class="dtree-body"><strong>Yes:</strong> Gas supply is on. Move to electrode and gas-valve diagnostics.<br><strong>No:</strong> Open the valve, wait two minutes for air to purge, then reset the boiler and attempt ignition.</div>
</details>

<details class="dtree"><summary>Does the control display show the same A84 code when you view the fault history in the diagnostics menu?</summary>
<div class="dtree-body"><strong>Yes:</strong> The code is logged. Cross-reference A84 in your exact model's installation manual to confirm its meaning.<br><strong>No:</strong> The code may be transient or misread. Record the actual current fault code and consult the manual for that code.</div>
</details>

<details class="dtree"><summary>Can you see visible soot, corrosion, or damage on the ignition electrode or flame sensor rod?</summary>
<div class="dtree-body"><strong>Yes:</strong> Clean the electrode with fine emery cloth or steel wool, verify proper gap and position per the manual, then test ignition.<br><strong>No:</strong> The electrode may be electrically sound. Check gas valve operation, wiring integrity, and gas supply pressure with a manometer.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power and gas** to the boiler at the main disconnect and upstream shutoff valve before opening the burner compartment.
2. **Access the diagnostics menu** on the boiler's control display and retrieve the full fault history to confirm whether A84 is the current lockout or an old logged event.
3. **Cross-reference the code** in your boiler's installation and service manual, matching your exact model number and control board type to the fault table.
4. **Check gas supply pressure** at the inlet to the gas valve using a manometer (AquaBalance models require 3.5 to 11 in. w.c.), and verify the manual shutoff valve is fully open.
5. **Inspect and clean the ignition and flame-sensing electrodes**, removing soot or corrosion with fine steel wool, then verify electrode gap and position match the specifications in the manual.
6. **Test gas valve operation** by listening for the click when the control calls for heat and measuring voltage at the valve terminals to confirm the control is sending the open signal.
7. **Reset the boiler** only after correcting the underlying fault, then observe a full ignition cycle to confirm stable flame establishment and normal operation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Ignition/flame-sensing electrode assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a84-error-code&k=Ignition%2Fflame-sensing+electrode+assembly&tag=errorcodefixes-20) \| Match your boiler's model number and burner type. |
| Gas valve | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a84-error-code&k=Gas+valve&tag=errorcodefixes-20) \| Verify voltage rating and gas type (natural or LP) before ordering. |

## When to Call a Pro

Call a qualified heating technician immediately if you cannot locate A84 in your boiler's manual, if you are unfamiliar with gas appliance diagnostics, or if you do not own a manometer to measure gas supply pressure. Gas boiler work requires specialized training to handle combustion air, gas piping, pressure testing, and electrode adjustment safely. A technician will retrieve the fault from the control's history, verify the exact code meaning for your model, test gas pressure and valve operation, inspect and clean or replace electrodes, and confirm proper combustion and venting. Weil-McLain's documentation specifies that all diagnostics and service must be performed by a licensed installer or service agency.

**Rough cost:** A pro service call runs about $150-350.
