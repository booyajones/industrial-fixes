---
title: "Weil-McLain A41 Error Code - Causes & Fix"
description: "A41 means ignition failure: the boiler tried to light but saw no flame. Most often a warped ignitor or dirty flame sensor."
pubDatetime: 2026-06-14T11:48:47Z
modDatetime: 2026-06-14T11:48:47Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
money_part: "Hot Surface Ignitor (HSI) for Weil-McLain"
most_likely_cause: "Warped or worn hot surface ignitor"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power-cycle the boiler (turn off, wait 30 seconds, turn on) and press reset once"
  - "Verify the gas valve at the boiler is fully open"
  - "Check that system pressure is below 25 PSI (dangerous if exceeded)"
part_price: "$40-80"
---

## Weil-McLain A41 Error Code — What It Means

The A-41 code indicates an ignition failure. The boiler entered its startup cycle (fan started, ignitor fired, gas valve opened), but the flame sensor did not confirm a flame within the allotted time. The system then shut down and entered lockout to prevent unsafe operation.

Weil-McLain recommends no more than two reset attempts in a row. If the code persists after two resets, a professional diagnosis is required to identify and correct the underlying cause.

## Before You Replace Anything

Many homeowners replace the control board first, but a warped ignitor or dirty flame sensor causes most A41 lockouts. Measure the ignitor-to-burner gap and check the flame sensor signal before replacing the controller.

[Jump to Fix](#fix)

## Common Causes

- **Warped or worn ignitor (~35%)** Heat cycles cause the hot surface ignitor to warp and drift away from the burner, preventing reliable ignition.
- **Dirty or failed flame sensor (~30%)** The sensor is coated with residue or electrically open, failing to detect the flame even when present.
- **No gas flow (~20%)** Gas valve is closed, gas supply is interrupted, or the gas valve solenoid is faulty.
- **Intermittent connection or temperature issue (~10%)** The error appears when the unit is idle for a while, suggesting a low in-cabinet temperature affecting a connection or component.
- **Internal controller fault (~5%)** The main controller board itself has an internal fault (rare).

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the ignitor glow bright orange when the boiler tries to start?</summary>
<div class="dtree-body"><strong>Yes:</strong> The ignitor is heating. Check the flame sensor next (dirty or failing) or verify gas flow reaches the burner.<br><strong>No:</strong> The ignitor is not heating. Check its wiring connections and measure resistance (typically 40-90 ohms). Replace if cracked, warped, or open.</div>
</details>

<details class="dtree"><summary>Do you hear the gas valve click open during the ignition cycle?</summary>
<div class="dtree-body"><strong>Yes:</strong> Gas valve is opening. Inspect the ignitor position (warped or too far from burner) and clean the flame sensor.<br><strong>No:</strong> Gas valve is not opening. Verify 24V AC at the valve during ignition attempt and check that the gas supply valve is open.</div>
</details>

<details class="dtree"><summary>Does the error appear only after the boiler has been idle for several hours?</summary>
<div class="dtree-body"><strong>Yes:</strong> An intermittent connection or cold-temperature component issue is likely. Inspect low-voltage wiring inside the cabinet and tighten connections.<br><strong>No:</strong> The fault is consistent. Focus on the ignitor, flame sensor, and gas valve as the primary suspects.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify gas supply:** Confirm the gas valve at the boiler is fully open and gas pressure is present at the inlet.
2. **Reset the unit:** Power-cycle the boiler (turn off, wait 30 seconds, turn on) and press the reset button once.
3. **Inspect the ignitor:** Look for cracks or warping. Measure the distance between the ignitor and the burner. If it has drifted away, the ignitor is warped and needs replacement.
4. **Inspect the flame sensor:** Remove the sensor and clean it with fine emery cloth to remove residue. Check for a proper flame signal (greater than 0.5 microamps DC) if the boiler ignites momentarily.
5. **Check gas valve operation:** Verify the gas valve opens during the cycle (audible click) and measure 24V AC at the valve during ignition attempt.
6. **Review lockout history:** Access the Contractor Menu (hold UP and DOWN arrows), then Diagnostics, then Errors/Lockout History to confirm if the fault is consistent or intermittent.
7. **Check connections:** If the fault is intermittent (idle-related), inspect low-voltage wiring connections inside the cabinet for heat or cold sensitivity.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hot Surface Ignitor (HSI) for Weil-McLain | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a41-error-code&k=Hot+Surface+Ignitor+%28HSI%29+for+Weil-McLain&tag=errorcodefixes-20) \| Replace if warped, cracked, or drifted away from the burner. Part number varies by model (Ultra, Aqua Balance, CGa). |
| Flame Sensor for Weil-McLain | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a41-error-code&k=Flame+Sensor+for+Weil-McLain&tag=errorcodefixes-20) \| Replace if cleaning fails to restore signal or if sensor is electrically open. |
| Gas Valve for Weil-McLain | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a41-error-code&k=Gas+Valve+for+Weil-McLain&tag=errorcodefixes-20) \| Replace if valve does not open (no click) and 24V AC is present at the terminals. |

## When to Call a Pro

Call a licensed heating technician if the code persists after two reset attempts. Ignition failures involve gas appliances and flame detection, both of which require specific diagnostic tools (multimeters, microamp meters, gas pressure gauges) and training. Technicians can measure ignitor resistance, flame sensor signal, gas valve voltage, and inspect for warping or connection faults. Misdiagnosing an ignition issue can lead to unsafe operation or carbon monoxide risk. Always consult the specific Weil-McLain installation and service manual for your model for exact specifications and part numbers.

**Rough cost:** A pro service call runs about $150-350.

## See Also

- [Weil-McLain A151 Error - Causes & Fix](/posts/weil-mclain-boiler-a151-error-code/)
- [Weil-McLain Boiler A80 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a80-error-code/)
- [Weil-McLain Boiler Error Code E08 — Causes & Fix](/posts/weil-mclain-e08-error-code/)
- [Weil-McLain Boiler A62 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a62-error-code/)
