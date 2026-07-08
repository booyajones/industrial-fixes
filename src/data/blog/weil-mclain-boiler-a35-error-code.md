---
title: "Weil-McLain A35 Error Code - Causes & Fix"
description: "A35 means the boiler failed to light or prove flame during ignition. Clean the flame rod and check gas supply before replacing parts."
pubDatetime: 2026-06-13T13:12:33Z
modDatetime: 2026-06-13T13:12:33Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
money_part: "Flame sensor / flame rod"
most_likely_cause: "dirty or damaged flame sensor rod"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify the manual gas shutoff valve upstream of the boiler is fully open."
  - "Check that the combustion-air inlet and vent pipe are unobstructed."
  - "Inspect the flame rod for soot, corrosion, or loose ground connections and clean it with fine emery cloth."
part_price: "$30-60 for a flame rod"
no_buy_pct: "60%"
---

## Weil-McLain A35 Error Code — What It Means

A35 is an ignition lockout on Weil-McLain boilers. The burner sequence started, but the control did not detect a valid flame signal, so the boiler locked out for safety. In the field, this is a "failed to light" or "flame not proven" condition rather than a generic sensor fault.

The code appears when the control looks for flame rectification current from the flame sensor during the trial-for-ignition window and either sees no flame or an unstable signal. The boiler will stay locked out until you press the reset button or cycle power, but repeated resets without correcting the underlying problem are not a repair.

## Before You Replace Anything

Many people replace the control board first when the real culprit is a fouled flame rod or closed gas valve. Clean and inspect the flame sensor and verify gas flow before ordering any electronics.

[Jump to Fix](#fix)

## Common Causes

- **Dirty or damaged flame sensor rod (~40%)** Soot, corrosion, or mineral deposits on the flame rod prevent proper rectification current, so the control never confirms ignition.
- **Gas supply problem (~30%)** A closed manual valve, low inlet pressure, or a gas valve that does not open during the call stops fuel from reaching the burner.
- **Faulty ignitor or hot-surface igniter (~15%)** A cracked, weak, or failed igniter does not reach temperature or creates an arc path that prevents reliable ignition.
- **Poor combustion airflow or venting (~10%)** Blocked air intake, restricted exhaust, or condensate backup can choke combustion and prevent stable flame proving.
- **Control board or wiring fault (~5%)** Loose flame-sense wiring, poor grounding, or a failed ignition module will lock out even when the sensor and gas supply are good.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the manual gas shutoff valve upstream of the boiler fully open?</summary>
<div class="dtree-body"><strong>Yes:</strong> Gas is available; move on to inspect the flame sensor and ignitor.<br><strong>No:</strong> Open the valve and press reset; if the boiler lights and runs, you found the problem.</div>
</details>

<details class="dtree"><summary>Does the ignitor glow bright orange during the startup sequence?</summary>
<div class="dtree-body"><strong>Yes:</strong> Ignitor is working; focus on the flame sensor, gas valve, and flame-sense wiring.<br><strong>No:</strong> Ignitor may be failed or not receiving power; check connections and measure voltage at the ignitor terminals, then replace the ignitor if voltage is present but it does not glow.</div>
</details>

<details class="dtree"><summary>After cleaning the flame rod, does the boiler light and stay running?</summary>
<div class="dtree-body"><strong>Yes:</strong> The rod was fouled; monitor for repeat lockouts and improve combustion air if soot builds up quickly.<br><strong>No:</strong> Check inlet gas pressure with a manometer, inspect the gas valve for proper opening, and test flame-sense continuity and grounding before replacing the control board.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power and gas** at the boiler's service switch and manual shutoff valve, then let the unit cool.
2. **Record the lockout code** and any diagnostic history in the contractor menu if your control supports it, so you know whether the fault is current or old.
3. **Inspect the flame sensor rod** for soot, corrosion, or cracks; remove it and polish the sensing tip with fine emery cloth or steel wool, then check that the mounting bracket provides a solid ground path.
4. **Check the ignitor** for visible cracks, carbon tracking, or loose connections; measure resistance across the ignitor terminals if your manual gives a spec, or simply observe whether it glows bright orange during startup.
5. **Verify gas supply** by confirming the manual valve is open, measuring inlet pressure with a manometer (consult your model's table for the correct range), and listening or watching for the gas valve to click open during the trial-for-ignition sequence.
6. **Reinstall all components**, restore power and gas, then press reset and observe the full ignition cycle; if flame appears but the boiler still locks out, check flame-sense wiring and ground continuity.
7. **Replace only the failed part** identified by your tests (flame rod, ignitor, gas valve, or control board) and clear the lockout; repeated resets without a repair will not solve the problem and may damage the control.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame sensor / flame rod | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a35-error-code&k=Flame+sensor+%2F+flame+rod&tag=errorcodefixes-20) \| Match the part number in your boiler's service manual or measure the original's length and mounting hardware. |
| Hot-surface ignitor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a35-error-code&k=Hot-surface+ignitor&tag=errorcodefixes-20) \| Verify voltage rating and ceramic shape; fragile during handling, so support the base when disconnecting wires. |
| Gas valve | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a35-error-code&k=Gas+valve&tag=errorcodefixes-20) \| Order by boiler model and serial number; gas valves are not interchangeable across series. |
| Ignition control board / module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a35-error-code&k=Ignition+control+board+%2F+module&tag=errorcodefixes-20) \| Replace only after confirming all sensors, wiring, and gas delivery are correct; many boards are misdiagnosed. |

## When to Call a Pro

Call a licensed HVAC or boiler technician if you are not comfortable working with gas appliances, if you cannot safely access the flame sensor or ignitor, or if cleaning and basic gas checks do not clear the A35 lockout. Gas work and combustion diagnostics require calibrated manometers, multimeters, and knowledge of your boiler's specific control logic. A qualified tech will measure inlet and manifold gas pressure, test flame rectification current, inspect venting and combustion air paths, and isolate whether the fault is in the sensor, valve, wiring, or control board. Skipping proper diagnostics and throwing parts at the problem wastes money and can create unsafe operating conditions.

**Rough cost:** A pro service call runs about $150-350 depending on parts and labor.

## See Also

- [Weil-McLain Boiler A98 Error - Causes & Fix](/posts/weil-mclain-boiler-a98-error-code/)
- [Weil-McLain Boiler A72 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a72-error-code/)
- [Weil-McLain Boiler A163 Error - Causes & Fix](/posts/weil-mclain-boiler-a163-error-code/)
- [Weil-McLain Boiler A73 Error - Causes & Fix](/posts/weil-mclain-boiler-a73-error-code/)
