---
title: "Weil-McLain A81 Error Code - Causes & Fix"
description: "A81 means ignition failure: the boiler tried to light but didn't prove flame. Most common fix: check gas supply & replace the ignitor."
pubDatetime: 2026-06-15T11:38:25Z
modDatetime: 2026-06-15T11:38:25Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
money_part: "Hot surface ignitor (HSI)"
most_likely_cause: "No gas flow or insufficient gas supply"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Confirm the gas service valve (upstream of the boiler) is fully open and that other gas appliances in the home are working normally."
  - "Reset the lockout once by cycling power or pressing the reset button and observe whether the ignitor glows during the next start attempt."
  - "Check that the ignitor is properly seated in its bracket and not visibly cracked or deformed."
part_price: "$40-80"
---

## What this code means
The A81 code on a Weil-McLain boiler signals an ignition failure or failed light-off fault. The boiler attempted to start and go through its ignition sequence, but the control board did not detect a stable flame. When this happens, the system locks out to prevent unburned gas from accumulating. In practical terms, the burner did not establish combustion when commanded to fire.

The exact ignition sequence and lockout behavior vary by model family, and Weil-McLain service manuals state that diagnosis is intended for qualified service technicians. The fault can occur at different stages: prepurge, spark/ignition, gas valve actuation, or flame proving. Each model may use a slightly different combination of ignitor type, flame sensor design, and control logic, so always consult the nameplate and pull the model-specific service manual before testing components.

## Before You Replace Anything

Homeowners often replace the control board first, assuming the electronics failed. Before ordering any board, verify gas supply at the valve inlet and inspect the ignitor for cracks or misalignment. A worn ignitor or closed gas shutoff accounts for most A81 faults.

## Common Causes

- **No gas flow or insufficient gas supply (~35%)** The service valve is closed, the meter regulator is locked out, or the gas line has been capped or interrupted upstream of the boiler.
- **Failed or weak hot surface ignitor (~30%)** The ignitor is cracked, misaligned, warped, or drawing insufficient current to reach ignition temperature.
- **Gas valve not opening (~15%)** The gas valve coil is defective, the wiring is loose, or the valve itself is stuck closed and does not admit gas when commanded.
- **Dirty or failed flame-sensing components (~12%)** The flame sensor or flame-proving electrode is fouled with soot or carbon, preventing the control from confirming that combustion has started.
- **Internal control or board issue (~8%)** The ignition module or main control board is not executing the ignition sequence correctly or is failing to interpret the flame signal.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the ignitor glow orange-white for a few seconds at the start of each call for heat?</summary>
<div class="dtree-body"><strong>Yes:</strong> The ignitor is receiving power and heating. The problem is likely no gas flow (closed valve, empty tank, or failed gas valve) or a flame-sensing issue.<br><strong>No:</strong> The ignitor circuit is interrupted. Check for loose wiring at the ignitor connector, a cracked ignitor element, or a faulty control board output.</div>
</details>

<details class="dtree"><summary>Do you hear the gas valve click open a few seconds after the ignitor glows?</summary>
<div class="dtree-body"><strong>Yes:</strong> Gas is being admitted. If flame still does not light, suspect a weak ignitor that cannot ignite the gas, misaligned ignitor position, or obstructed burner ports.<br><strong>No:</strong> The gas valve is not opening. Verify gas supply pressure, check the valve coil wiring and resistance (consult your model's manual for spec), and test for voltage at the valve terminals during a call.</div>
</details>

<details class="dtree"><summary>After resetting the fault once, does the same A81 code reappear on the next start?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is repeatable. Do not keep resetting. Proceed with systematic component checks: gas supply, ignitor condition, gas valve operation, and flame sensor cleanliness.<br><strong>No:</strong> If the boiler runs normally after one reset, the fault may have been a transient event (draft disturbance, momentary low gas pressure). Monitor for recurrence before replacing parts.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power** to the boiler at the service switch and turn the gas shutoff valve to the OFF position before beginning any inspection.
2. **Confirm gas supply** by checking that the upstream service valve is fully open and that the meter or tank is delivering gas to other appliances in the building.
3. **Inspect the ignitor** by removing the burner access panel and visually checking the hot surface igniter for cracks, carbon buildup, or misalignment in its bracket.
4. **Observe the ignition sequence** by restoring power and initiating a call for heat, watching for ignitor glow, listening for the gas valve click, and looking for flame establishment.
5. **Test the gas valve** by measuring supply pressure at the inlet (consult your model manual for the correct value) and checking for 24 VAC or 120 VAC (model-dependent) at the valve coil terminals during a call.
6. **Clean or replace the flame sensor** if your model uses a separate flame-proving rod, removing any soot or oxidation with fine-grit sandpaper or a soft wire brush.
7. **Replace the ignitor** if it is cracked, drawing low current, or fails to glow bright orange-white, using the OEM part number from your boiler's service manual or nameplate.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hot surface ignitor (HSI) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a81-error-code&k=Hot+surface+ignitor+%28HSI%29&tag=errorcodefixes-20) \| Model-specific ceramic or silicon-carbide element. Verify the exact OEM part number from your nameplate or service manual before ordering. |
| Flame sensor / flame-proving electrode | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a81-error-code&k=Flame+sensor+%2F+flame-proving+electrode&tag=errorcodefixes-20) \| Used on models with separate sensing rods. Clean first before replacing. |
| Gas valve | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a81-error-code&k=Gas+valve&tag=errorcodefixes-20) \| Solenoid-operated valve, 24 VAC or millivolt depending on model. Replacement requires gas piping work and leak testing. |
| Ignition control board / module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a81-error-code&k=Ignition+control+board+%2F+module&tag=errorcodefixes-20) \| Controls the ignition sequence and flame proving. Replace only after ruling out ignitor, gas valve, and sensor faults. |

## When to Call a Pro

Call a licensed HVAC or boiler technician immediately if you are not trained to work with gas appliances. Gas ignition faults require systematic diagnosis of gas pressure, electrical circuits, and flame-proving logic. A technician will use a combustion analyzer, multimeter, and manometer to pinpoint whether the fault is in the gas supply, ignitor, valve, sensor, or control board. Repeated resets without proper diagnosis can lead to dangerous conditions, including gas accumulation or carbon monoxide production. If you have replaced the ignitor and confirmed gas flow but the A81 code persists, the problem is likely in the gas valve actuation circuit or the control board, both of which require professional testing and calibration. Weil-McLain service manuals are written for qualified technicians and contain model-specific wiring diagrams, voltage tables, and timing sequences that are necessary for accurate repair.

**Rough cost:** A pro service call runs about $150-350.
