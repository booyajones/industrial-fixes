---
title: "Weil-McLain A142 Error Code - Causes & Fix"
description: "A142 is a model-specific diagnostic code on Weil-McLain boilers. Check your manual for exact meaning; often ignition, sensor, or pressure fault."
pubDatetime: 2026-06-17T11:34:26Z
modDatetime: 2026-06-17T11:34:26Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - boiler
  - weil-mclain
money_part: "Flame sensor or ignition electrode assembly"
diy_or_pro: "pro"
free_checks:
  - "Enter the diagnostics menu on your control and write down the active and stored fault codes, then look them up in your model's service manual."
  - "Confirm gas valve is open, system pressure is above 12 psi (if hydronic), and intake and exhaust vents are clear of snow, debris, or blockage."
  - "Power-cycle the boiler by turning off the switch or breaker for 30 seconds, then turn it back on and observe whether the fault recurs immediately or after an ignition attempt."
---

## Weil-McLain A142 Error Code — What It Means

The A142 error code is not a universal Weil-McLain fault code found in standard manufacturer documentation. It is a model-specific diagnostic code whose exact meaning depends on your boiler series and control platform. Weil-McLain fault histories are accessed through the control's diagnostics menu, and the proper next step is to consult your exact model's service manual to determine what A142 indicates on your unit.

Based on typical Weil-McLain troubleshooting patterns, codes in this range usually point to ignition or flame-proving problems, venting or air-proving faults, gas supply issues, failed sensor or thermistor readings, low water or pressure conditions, or control-board and wiring problems. The control board stores active and past faults that help pinpoint the failed safety circuit or input. Without the model-specific manual, a technician must retrieve the fault description from the diagnostics screen and then test the suspect component electrically to confirm the root cause.

## Before You Replace Anything

Homeowners often replace the control board when the real problem is a dirty flame sensor, failed thermistor, or blocked air-proving switch tube. Always test the suspect sensor or switch electrically and check tubing and wiring before ordering a board.

[Jump to Fix](#fix)

## Common Causes

- **Ignition or flame-sensor fault (~30%)** Dirty or misaligned flame sensor, corroded ignition electrode, or grounding issue prevents the control from proving flame and triggers a lockout.
- **Venting or air-proving switch failure (~25%)** Blocked intake or exhaust vent, disconnected pressure-switch tubing, or failed air-proving switch stops the ignition sequence before gas is released.
- **Gas supply or valve issue (~20%)** Closed manual gas valve, low inlet pressure, or stuck gas valve prevents fuel from reaching the burner and causes an ignition fault.
- **Temperature sensor or thermistor out of range (~15%)** Failed thermistor or temperature probe reads outside expected resistance or voltage limits and tells the control to lock out.
- **Low water pressure or cutoff fault (~10%)** System pressure below minimum threshold or failed low-water cutoff opens the safety circuit and prevents ignition.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the burner ignite at all, even briefly, before the code appears?</summary>
<div class="dtree-body"><strong>Yes:</strong> The flame sensor or grounding is likely at fault. Clean the sensor rod with fine sandpaper and check the electrode gap and ground wire.<br><strong>No:</strong> The fault occurs before ignition, so check gas supply, air-proving switch, and system pressure before testing ignition components.</div>
</details>

<details class="dtree"><summary>Is system water pressure above 12 psi and the fill valve open?</summary>
<div class="dtree-body"><strong>Yes:</strong> Pressure is adequate. Focus on ignition, venting, and sensor circuits using the diagnostics menu and service manual.<br><strong>No:</strong> Top up system pressure slowly to about 15 psi, bleed air from radiators or baseboards, then clear the fault and retry.</div>
</details>

<details class="dtree"><summary>Do you hear the inducer or blower motor run during a call for heat?</summary>
<div class="dtree-body"><strong>Yes:</strong> Venting and air-proving are likely working. Move to flame-sensor, gas-valve, and ignition checks.<br><strong>No:</strong> The air-proving switch or inducer may have failed, or tubing is blocked or disconnected. Inspect the pressure switch and tubing first.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the boiler** at the service switch or breaker and wait 30 seconds.
2. **Locate the exact model and control platform** from the boiler rating plate or CP number on the unit.
3. **Enter the diagnostics menu** on the control and read the active and stored fault codes, then cross-reference A142 in your model's service manual to determine the exact fault description.
4. **Check the basics first:** confirm the manual gas valve is open, system water pressure is in range (typically 12–20 psi for hydronic systems), and intake and exhaust vents are clear of obstructions or condensate buildup.
5. **Test the suspect component electrically** using the service manual's specifications. For a flame sensor, measure microamp signal during ignition. For a thermistor, measure resistance at room temperature and compare to the published curve. For an air-proving switch, check continuity and tubing for blockage.
6. **Replace only the confirmed failed part** (flame sensor, ignition electrode, pressure switch, thermistor, gas valve, or control board), then restore power and clear the fault code through the diagnostics menu.
7. **Run a full heat cycle** and verify normal ignition, stable flame, proper circulation, and no recurring lockout or fault code before closing the service call.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame sensor or ignition electrode assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a142-error-code&k=Flame+sensor+or+ignition+electrode+assembly&tag=errorcodefixes-20) \| Order the exact part number for your boiler model and control platform. |
| Air-proving or pressure switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a142-error-code&k=Air-proving+or+pressure+switch&tag=errorcodefixes-20) \| Match the switch to your venting configuration (direct-vent, sealed-combustion, etc.). |
| Thermistor or temperature sensor probe | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a142-error-code&k=Thermistor+or+temperature+sensor+probe&tag=errorcodefixes-20) \| Use the manufacturer part number to make sure correct resistance curve and connector type. |
| Control board or ignition module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a142-error-code&k=Control+board+or+ignition+module&tag=errorcodefixes-20) \| Last resort after confirming all sensors, switches, and wiring are intact and tested good. |

## When to Call a Pro

Call a licensed boiler technician immediately if you are not comfortable working with gas appliances, do not have your model's service manual and diagnostic procedures, or cannot safely access the control board and sensor wiring. Gas boilers require precise ignition and venting adjustments that are unsafe to guess at. A technician will retrieve the exact fault definition from the diagnostics menu, test the failed circuit with calibrated meters, and replace only the confirmed component. If the fault recurs after you replace a part, or if you see multiple codes or unusual noises during ignition, professional diagnosis is the only safe path forward.

**Rough cost:** A pro service call runs about $150-400.

## See Also

- [Weil-McLain Boiler Error Code E10 — Low Water Pressure Fix](/posts/weil-mclain-e10-low-pressure/)
- [Weil-McLain A90 Error - Causes & Fix](/posts/weil-mclain-boiler-a90-error-code/)
- [Weil-McLain A162 Error - Causes & Fix](/posts/weil-mclain-boiler-a162-error-code/)
- [Weil-McLain Boiler A163 Error - Causes & Fix](/posts/weil-mclain-boiler-a163-error-code/)
