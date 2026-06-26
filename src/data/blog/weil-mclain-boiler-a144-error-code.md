---
title: "Weil-McLain A144 Error Code - Causes & Fix"
description: "A144 on Weil-McLain boilers usually signals ignition failure. Most common fix: check gas supply, clean flame sensor, or replace ignitor."
pubDatetime: 2026-06-18T09:53:33Z
modDatetime: 2026-06-18T09:53:33Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - boiler
  - weil-mclain
money_part: "Flame sensor / flame rod"
most_likely_cause: "dirty or failed flame sensor"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Confirm gas shutoff valve is fully open and thermostat is calling for heat"
  - "Check breaker and service switch are on, system water pressure is in normal range"
  - "Read fault history from the control diagnostics menu to verify A144 definition for your model"
part_price: "$15-40"
---

## Weil-McLain A144 Error Code — What It Means

A144 is not a universal code across all Weil-McLain boilers. The meaning depends on your exact model and control platform. From available field reports, A144 typically indicates the boiler attempted to light but failed. Common triggers include no gas flow, a dirty or failed flame sensor, or a weak ignitor. Because Weil-McLain uses different control families (Ultra, EverGreen, etc.), always confirm the fault against your specific boiler manual and check the control's fault history menu before ordering parts.

On some models, ignition-family faults appear under different code formats, so what shows as A144 on one control might be labeled differently on another. If your boiler repeatedly tries to light and locks out, the root cause is usually in the ignition train, gas supply, or flame-proving circuit. Do not reset the boiler repeatedly without fixing the underlying problem.

## Before You Replace Anything

Many people replace the control board first when the real issue is a dirty flame sensor or weak ignitor. Always clean the flame rod and test the ignitor's resistance and current draw before condemning the board.

[Jump to Fix](#fix)

## Common Causes

- **Dirty or failed flame sensor (~35%)** Soot, oxide buildup, or a weak sensor prevents the control from proving flame even when the burner lights, causing immediate lockout.
- **No gas supply or low gas pressure (~30%)** Closed shutoff valve, empty tank, regulator fault, or utility interruption means the ignitor glows but no flame appears.
- **Weak or failed ignitor (~20%)** A cracked, aged, or electrically weak hot-surface ignitor does not get hot enough to light the gas reliably.
- **Blocked intake or exhaust vent (~10%)** Obstructed combustion air or flue passages prevent proper draft, and the pressure switch or draft-proving device halts ignition on models so equipped.
- **Control board fault (~5%)** Internal relay failure or corrupted fault logic can produce false ignition-lockout codes, though this is less common than field-side issues.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the gas shutoff valve fully open and do you smell gas near the boiler during a call for heat?</summary>
<div class="dtree-body"><strong>Yes:</strong> Gas is reaching the appliance. Focus on the ignitor and flame sensor.<br><strong>No:</strong> Check for a closed valve, empty propane tank, or utility interruption. Restore gas supply before proceeding.</div>
</details>

<details class="dtree"><summary>Does the ignitor glow bright orange during startup?</summary>
<div class="dtree-body"><strong>Yes:</strong> Ignitor is receiving power. Inspect and clean the flame sensor and verify burner flame appearance.<br><strong>No:</strong> Ignitor may be cracked, weak, or the control is not sending voltage. Test ignitor resistance and replace if out of spec.</div>
</details>

<details class="dtree"><summary>Does the burner light briefly then shut off within a few seconds?</summary>
<div class="dtree-body"><strong>Yes:</strong> The flame sensor is likely dirty or failing. Clean the rod with fine abrasive or replace if cleaning does not help.<br><strong>No:</strong> No flame at all suggests gas-valve fault, wiring issue, or very low gas pressure. Measure inlet and manifold pressures.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Identify your exact model and control** from the nameplate and locate the service manual. Cross-reference A144 in the fault table to confirm whether it truly means ignition failure on your unit.
2. **Read the fault history** from the control diagnostics menu. Many Weil-McLain controls log multiple faults, and the front-panel display may not show the earliest or root cause.
3. **Verify basics** before disassembly. Confirm the service switch and breaker are on, thermostat is calling for heat, gas shutoff is open, and system water pressure is in the normal range per your manual.
4. **Inspect the ignitor** visually for cracks or breaks. Measure its resistance (typically 40-90 ohms for a silicon-carbide type, but consult your model's table). Replace if cracked or out of specification.
5. **Clean the flame sensor** with fine emery cloth or a dollar bill to remove oxide and soot. Check the sensor harness and grounding. A poor ground path breaks flame rectification even when the rod is clean.
6. **Check combustion air and venting**. Clear any blockage in the intake and exhaust. On condensing models, verify the condensate trap is filled and draining freely. Test any pressure switch for proper operation.
7. **Measure gas supply pressure** at the inlet and manifold during a call for heat. Compare readings to the boiler's specification plate. Low or unstable pressure causes repeated ignition failure even when all other parts test good.
8. **Reset the boiler once** after correcting the fault and observe a full ignition cycle. If A144 returns, replace only the component identified by test results, not the board by default.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame sensor / flame rod | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a144-error-code&k=Flame+sensor+%2F+flame+rod&tag=errorcodefixes-20) \| Model-specific. Verify length, thread, and harness connector before ordering. |
| Hot-surface ignitor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a144-error-code&k=Hot-surface+ignitor&tag=errorcodefixes-20) \| Silicon-carbide or silicon-nitride type. Match the wattage and mounting bracket to your burner assembly. |
| Gas valve | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a144-error-code&k=Gas+valve&tag=errorcodefixes-20) \| Required only if testing confirms the valve does not open or hold pressure. Order by boiler model and gas type (natural or LP). |

## When to Call a Pro

Call a licensed heating technician if you are not comfortable working with gas appliances, if you cannot locate or interpret your boiler's manual and fault history, or if the fault returns after cleaning the flame sensor and verifying gas supply. A pro will measure ignitor current draw, gas pressures at the valve, and flame-sensor microamp signal to pinpoint the failed component. Repeated resetting without diagnosis risks nuisance lockouts, incomplete combustion, or damage to the control board. If combustion air or venting is suspect, a technician will perform a combustion-analysis test to confirm safe operation before returning the boiler to service.

**Rough cost:** A pro service call runs about $150-300.

## See Also

- [Weil-McLain ECG Boiler Error Codes — Complete Fault Guide](/posts/weil-mclain-ecg-error-codes/)
- [Weil-McLain Boiler Error Code E02 — Ignition Failure Fix](/posts/weil-mclain-e02-ignition-failure/)
- [Weil-McLain A174 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a174-error-code/)
- [Weil-McLain A97 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a97-error-code/)
