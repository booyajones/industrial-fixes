---
title: "Weil-McLain A140 Error Code - Causes & Fix"
description: "A140 meaning varies by Weil-McLain model. Check your manual's fault table, then verify gas, venting, flame sensor, and pressure switch."
pubDatetime: 2026-06-17T11:32:39Z
modDatetime: 2026-06-17T11:32:39Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - boiler
  - weil-mclain
money_part: "Flame sensor / flame rod"
diy_or_pro: "pro"
free_checks:
  - "Verify gas shutoff valve is fully open and gas meter is running"
  - "Check system water pressure is above 12 psi and refill if needed"
  - "Inspect vent pipes and intake for blockages, ice, or disconnected sections"
---

## Weil-McLain A140 Error Code — What It Means

The A140 error code on a Weil-McLain boiler does not have a single universal definition across all models. Different Weil-McLain control boards and models use distinct fault-code tables, so the exact meaning of A140 can vary. The code may relate to flame proving, pressure switch proving, ignition failure, limit trips, or condensate drainage problems, depending on your specific boiler model and control board version.

To determine what A140 means on your unit, locate the model-specific service manual or the fault-code table printed inside the boiler's control-panel door. The manual will list the exact fault description and the component or circuit the control is monitoring. Until you confirm the definition, treat A140 as a lockout that requires you to identify the root cause through the control's diagnostic history and the associated proving or safety circuit before resetting or replacing any part.

## Before You Replace Anything

Homeowners often replace the ignition control board or gas valve first without testing the flame sensor, pressure switch, or proving circuit. Use a multimeter to check flame rectification microamps and switch continuity before ordering expensive controls.

[Jump to Fix](#fix)

## Common Causes

- **Flame sensor contamination or poor rectification (~30%)** Carbon buildup or condensation on the flame rod prevents the control from reading flame current, causing a lockout that may display as A140 on some models.
- **Pressure switch stuck open or tubing disconnected (~25%)** The pressure switch may not close to prove air flow if the tubing is cracked, plugged with condensate, or the diaphragm is torn.
- **Blocked or frozen condensate drain (~20%)** A plugged trap or frozen drain line can back up condensate into the heat exchanger, trip a safety switch, or prevent the pressure switch from proving.
- **Gas valve or gas supply problem (~15%)** Low inlet gas pressure, a closed manual shutoff, or a failed gas valve coil will prevent ignition and trigger a fault code.
- **Low water cutoff or limit safety trip (~10%)** If the boiler runs low on water or a high-limit control trips, the lockout may appear as A140 on certain control boards.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the gas shutoff valve fully open and is the meter wheel spinning when the boiler calls for heat?</summary>
<div class="dtree-body"><strong>Yes:</strong> Gas supply is reaching the boiler. Move to checking the flame sensor and pressure switch.<br><strong>No:</strong> Open the shutoff valve or call your gas utility. No fault-code repair will succeed without gas.</div>
</details>

<details class="dtree"><summary>Does the boiler show system water pressure above 12 psi on the gauge?</summary>
<div class="dtree-body"><strong>Yes:</strong> Water pressure is adequate. Focus on combustion and proving circuits.<br><strong>No:</strong> Refill the system to around 15 psi using the boiler's fill valve and retest. Low water can trigger safety lockouts.</div>
</details>

<details class="dtree"><summary>Do you hear the inducer fan run for at least 30 seconds before the ignition attempt?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fan is running. Check the pressure switch and its tubing for a closure signal to the control.<br><strong>No:</strong> The inducer may have failed, or the control is not calling for it. Verify power and wiring to the fan and check for a blocked vent.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Access the fault history** on the control board by pressing the diagnostic button or following the menu sequence in your model's manual, and write down the exact code and any accompanying lockout text.
2. **Locate the A140 definition** in the service manual or fault table for your specific model and control board version so you know which circuit or component the control is monitoring.
3. **Verify field conditions** by checking that the gas shutoff valve is open, system water pressure is above 12 psi, the vent and intake pipes are clear and properly terminated, and the condensate drain is not blocked or frozen.
4. **Inspect the proving circuit** associated with the fault. If the manual indicates flame proving, remove and clean the flame sensor with fine sandpaper and check the grounding wire. If it indicates a pressure switch, inspect the tubing for cracks, water, or disconnections and confirm the switch closes with a multimeter.
5. **Test the safety devices** by checking continuity on the pressure switch when the inducer is running, measuring flame rectification microamps during ignition (typically 0.5–5.0 µA DC), and verifying that the low-water cutoff and high-limit controls are not open.
6. **Correct the root cause** by replacing the contaminated sensor, clearing the blocked drain, repairing tubing, or replacing the failed switch or valve as identified by your diagnostic tests.
7. **Clear the lockout** by cycling power or pressing the reset button, then observe a complete start-up cycle to confirm stable ignition, flame proving, and no re-lockout before leaving the boiler in service.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame sensor / flame rod | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a140-error-code&k=Flame+sensor+%2F+flame+rod&tag=errorcodefixes-20) \| Order the exact part number from your model's illustrated parts list. |
| Pressure switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a140-error-code&k=Pressure+switch&tag=errorcodefixes-20) \| Match the pressure-range and connection-port configuration to your boiler model. |
| Gas valve | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a140-error-code&k=Gas+valve&tag=errorcodefixes-20) \| Specify your model and control-voltage (24 V or other) when ordering. |
| Ignition control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a140-error-code&k=Ignition+control+board&tag=errorcodefixes-20) \| Use the exact board part number from the service label inside the boiler cabinet. |

## When to Call a Pro

Call a licensed boiler technician for any A140 lockout. Gas-fired boiler diagnostics require measuring flame rectification, testing pressure-switch proving circuits, checking gas pressure at the manifold, and verifying control-board signals with a multimeter. A technician will retrieve the fault history from the control, cross-reference the exact A140 definition in the model-specific manual, and test the associated safety or proving circuit before replacing any part. If the fault involves the gas valve, ignition module, or control board, those repairs must be performed by a professional to maintain warranty coverage and meet local code. Weil-McLain also directs contractors to contact factory support for warranty and service actions rather than relying on generic troubleshooting, so professional help ensures you get the correct part and repair sequence for your specific boiler model.

**Rough cost:** A pro service call runs about $200–500.

## See Also

- [Weil-McLain A146 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a146-error-code/)
- [Weil-McLain A102 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a102-error-code/)
- [Weil-McLain A82 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a82-error-code/)
- [Weil-McLain Boiler Error Code E10 — Causes & Fix](/posts/weil-mclain-e10-error-code/)
