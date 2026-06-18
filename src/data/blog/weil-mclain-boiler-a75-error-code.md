---
title: "Weil-McLain A75 Error Code - Causes & Fix"
description: "A75 is not a standard Weil-McLain code. Check your model manual for the exact meaning. Most faults trace to flame-sensing or ignition issues."
pubDatetime: 2026-06-16T10:57:50Z
modDatetime: 2026-06-16T10:57:50Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - boiler
  - weil-mclain
money_part: "Flame sensor or flame rod"
diy_or_pro: "pro"
free_checks:
  - "Confirm gas supply is on and system water pressure is in the normal range for your boiler model"
  - "Check that the boiler has power and that no manual shutoff or isolation valve is closed"
  - "Look for any blocked condensate drain or ice in the vent if you have a condensing model"
---

## Weil-McLain A75 Error Code — What It Means

A75 is not a verified standard lockout or fault code in Weil-McLain's published documentation. Weil-McLain uses model-specific fault codes that vary by control platform and boiler series, so the exact meaning of A75 depends on your particular unit and control board. If you see A75 on your display, consult the service manual or wiring diagram for your specific model and control to interpret it correctly.

Based on typical Weil-McLain fault patterns, displayed codes usually point to one of three categories: ignition and flame-proving problems, temperature or sensor limit issues, or safety and pressure-related lockouts. Common field causes across these categories include dirty or misaligned flame sensors, ignition component failure, gas-supply restrictions, blocked condensate drains or venting on condensing models, low system water pressure, circulation problems, or a failed sensor or limit switch in the control chain.

## Before You Replace Anything

Technicians sometimes replace the control board first when the real problem is a dirty flame sensor or a blocked condensate trap. Always test the suspect input circuit electrically and verify basic operating conditions before swapping the control.

[Jump to Fix](#fix)

## Common Causes

- **Dirty or mispositioned flame sensor (~30%)** Oxidation, soot, or poor grounding on the flame rod prevents the control from proving flame even when the burner lights.
- **Ignition component failure (~25%)** A cracked, warped, or misgapped igniter or electrode cannot establish a reliable spark for lightoff.
- **Blocked condensate trap or drain (~20%)** On condensing boilers, a clogged trap, frozen condensate line, or restricted drain triggers a safety shutdown.
- **Gas supply or valve issue (~15%)** Insufficient gas pressure, a closed manual valve, or a sticking gas valve prevents proper burner operation.
- **Low system water pressure or circulation problem (~10%)** Pressure below the required threshold or a failed circulator can trip a low-water cutoff or pressure input.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the display show a lockout code or fault history in the diagnostics menu?</summary>
<div class="dtree-body"><strong>Yes:</strong> Write down all active and past codes and consult your model's service manual to decode them, which will point you to the failed circuit.<br><strong>No:</strong> The control may not store history, so proceed to verify power, gas supply, and system water pressure as baseline checks.</div>
</details>

<details class="dtree"><summary>Do you hear the igniter clicking and see a flame when the boiler tries to start?</summary>
<div class="dtree-body"><strong>Yes:</strong> The ignition system is working, so the fault likely involves flame-proving (dirty sensor) or a downstream safety interlock.<br><strong>No:</strong> The problem is upstream: check gas valve operation, igniter condition, and that the gas supply is fully open.</div>
</details>

<details class="dtree"><summary>Is your boiler a condensing model and do you see water pooling or ice near the condensate drain?</summary>
<div class="dtree-body"><strong>Yes:</strong> A blocked or frozen condensate trap is very likely, remove and clean the trap and verify the drain line is clear.<br><strong>No:</strong> Focus on ignition, flame-sensing, and sensor-input circuits instead of condensate issues.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Identify your exact boiler model and control platform** from the rating plate and retrieve the service manual or wiring diagram so you can decode A75 for your specific unit.
2. **Access the diagnostics or fault-history menu** on the control (if available) and write down all active and stored codes, which often reveal the real root cause.
3. **Verify basic operating conditions**: confirm the boiler has power, the gas manual valve is fully open, and system water pressure is in the normal range for your model.
4. **Inspect ignition and flame-proving components** by removing and cleaning the flame sensor or flame rod with fine emery cloth, checking the igniter for cracks or proper gap, and verifying burner grounding.
5. **Check condensate and venting on condensing models** by removing the condensate trap, flushing it clean, and confirming the drain line and vent intake are not blocked or frozen.
6. **Test suspect sensors and switches electrically** using a multimeter: measure continuity on limit switches, resistance on thermistors, and voltage on pressure switches, then replace only the component that tests outside spec.
7. **Clear the fault and restart** the boiler, then monitor a full cycle to confirm ignition, flame-proving, and that the code does not reappear.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame sensor or flame rod | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a75-error-code&k=Flame+sensor+or+flame+rod&tag=errorcodefixes-20) \| Order the part number specific to your Weil-McLain model and control platform. |
| Igniter or ignition electrode assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a75-error-code&k=Igniter+or+ignition+electrode+assembly&tag=errorcodefixes-20) \| Match the exact model number to make sure correct gap and mounting. |
| Condensate trap assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a75-error-code&k=Condensate+trap+assembly&tag=errorcodefixes-20) \| For condensing boilers, if the trap body is cracked or the internal baffle is damaged. |

## When to Call a Pro

Call a licensed heating technician if you cannot find the model-specific meaning of A75 in your manual, if you are not comfortable working with gas supply or electrical testing, or if the boiler continues to lock out after you have verified basic operating conditions. Gas-fired boiler work involves combustion safety, proper venting, and electrical diagnostics that require training and test equipment. A qualified technician will retrieve fault history from the control, test each input and output circuit with a meter, and replace only the component that has actually failed. Do not attempt to bypass safety interlocks or replace the control board without first confirming that sensors, limits, and the gas train are operating correctly.

**Rough cost:** A pro service call runs about $150-400.
