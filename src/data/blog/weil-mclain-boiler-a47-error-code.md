---
title: "Weil-McLain A47 Error Code - Causes & Fix"
description: "A47 is a model-specific fault or history code on Weil-McLain boilers. Check your control's diagnostics menu for the actual fault name."
pubDatetime: 2026-06-14T11:53:45Z
modDatetime: 2026-06-14T11:53:45Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
money_part: "Flame sensor / flame rod"
diy_or_pro: "pro"
free_checks:
  - "Enter the boiler's diagnostics menu and write down the actual fault name or number stored in history."
  - "Confirm the gas supply valve is fully open and the boiler has power."
  - "Clean the flame sensor rod with fine abrasive cloth or steel wool if accessible without dismantling burner components."
---

## Weil-McLain A47 Error Code — What It Means

A47 is not a universal Weil-McLain error code. It appears as a model-specific alarm or history entry on certain control boards. The exact meaning depends on your boiler series and the control installed. Weil-McLain designs its diagnostics so that technicians enter the contractor menu or fault-history screen to retrieve the actual fault name before starting repairs. Without that detail, A47 alone does not identify a single failed part.

Because Weil-McLain stores multiple fault codes in history, A47 may be a logged event rather than the current active lockout. The practical next step is to power up the boiler, enter the diagnostics area on your control, and read the stored fault description. Only then can you match the fault to the correct component and repair procedure in your model-specific manual.

## Before You Replace Anything

Many technicians replace the ignitor or gas valve after repeated ignition lockouts without first cleaning the flame sensor. A dirty or corroded flame rod is often the real cause and costs nothing to clean.

[Jump to Fix](#fix)

## Common Causes

- **Dirty or corroded flame sensor (~35%)** Carbon buildup or corrosion on the flame rod prevents the control from proving flame, causing repeated ignition lockouts even when the burner lights.
- **No gas flow or closed gas valve (~25%)** If the manual gas valve is off or gas pressure is low, the ignitor will cycle but no flame will appear.
- **Faulty or dirty ignitor (~15%)** A cracked or fouled hot-surface ignitor may glow weakly or not at all, preventing ignition.
- **Gas valve failure (~15%)** The gas valve may receive voltage but fail to open mechanically, blocking fuel to the burner.
- **Low water or high-limit lockout (~10%)** A tripped low-water cutoff or high-limit aquastat will prevent the control from calling for heat, and the code may appear in fault history.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the boiler's diagnostics menu show a current active fault or only A47 in history?</summary>
<div class="dtree-body"><strong>Yes:</strong> Write down the active fault name and consult your model's manual for that specific code.<br><strong>No:</strong> A47 is a logged event. Clear the history, attempt a call for heat, and watch for a new fault to appear.</div>
</details>

<details class="dtree"><summary>Do you hear the gas valve click and see a flame when the ignitor glows?</summary>
<div class="dtree-body"><strong>Yes:</strong> The ignitor and gas valve are working. Check the flame sensor for fouling or loose wiring.<br><strong>No:</strong> Confirm gas supply is on and check gas pressure. If pressure is correct, test the gas valve for voltage and mechanical operation.</div>
</details>

<details class="dtree"><summary>Does the flame sensor rod look dark, corroded, or covered in soot?</summary>
<div class="dtree-body"><strong>Yes:</strong> Clean the rod with fine steel wool or abrasive cloth, reset the boiler, and test again.<br><strong>No:</strong> Measure flame-sense microamps at the control. If reading is zero or very low, replace the flame sensor or check its wiring.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power** to the boiler at the service switch or breaker and close the manual gas valve.
2. **Enter the diagnostics menu** on your control board (consult your model's manual for the button sequence) and record the current fault name and any fault-history entries.
3. **Inspect the flame sensor** by removing the burner door or access panel, locating the flame rod near the burner, and checking for soot, corrosion, or bent position.
4. **Clean the flame sensor** with fine abrasive cloth or steel wool until the metal is shiny, then reinstall it securely with proper grounding to the bracket.
5. **Check the ignitor** for cracks or heavy carbon deposits. If damaged, replace it with the correct part number for your model.
6. **Verify gas supply** by opening the manual valve fully and checking inlet pressure at the gas valve (consult your model's table for correct pressure).
7. **Restore power and gas**, initiate a call for heat, and observe the ignition sequence. If the fault repeats, check gas-valve voltage and wiring, then test the valve itself for mechanical failure.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame sensor / flame rod | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a47-error-code&k=Flame+sensor+%2F+flame+rod&tag=errorcodefixes-20) \| Order by model and serial number. The rod must match the length and thread size of the original. |
| Hot-surface ignitor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a47-error-code&k=Hot-surface+ignitor&tag=errorcodefixes-20) \| Fragile silicon-carbide or silicon-nitride element. Handle by the ceramic base only and verify voltage before replacement. |
| Gas valve | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a47-error-code&k=Gas+valve&tag=errorcodefixes-20) \| Match the Btu rating and voltage stamped on your existing valve. Some valves require control-board programming after installation. |

## When to Call a Pro

Call a licensed HVAC or boiler technician if you cannot access the diagnostics menu, if you are uncomfortable working with gas piping or high-voltage wiring, or if the boiler continues to lock out after cleaning the flame sensor and verifying gas supply. Gas appliances require proper combustion testing and leak checks after any valve or burner work. A technician will also measure gas pressure, flame-sense current, and control-board outputs to pinpoint failures that a visual inspection cannot detect. If your boiler is still under warranty, unauthorized repairs may void coverage, so contact the installer or Weil-McLain's service network first.

**Rough cost:** A pro service call runs about $150-350.

## See Also

- [Weil-McLain A118 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a118-error-code/)
- [Weil-McLain A30 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a30-error-code/)
- [Weil-McLain A121 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a121-error-code/)
- [Weil-McLain Boiler A80 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a80-error-code/)
