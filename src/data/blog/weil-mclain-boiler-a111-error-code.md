---
title: "Weil-McLain A111 Error - Causes & Fix"
description: "A111 on Weil-McLain boilers usually signals ignition or sensor trouble. Most common fix: clean the flame rod and check gas pressure."
pubDatetime: 2026-06-16T11:24:12Z
modDatetime: 2026-06-16T11:24:12Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - boiler
  - weil-mclain
money_part: "Flame sensor or flame rod"
most_likely_cause: "dirty or misaligned flame sensor or flame rod"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify system pressure is at or above 12 psi and top up through the fill valve if low."
  - "Reset the boiler control and listen for the igniter and gas valve during a fresh call for heat."
  - "Check that the circulator pump is running and purge air from the system at bleed valves."
---

## Weil-McLain A111 Error — What It Means

Weil-McLain does not publish a universal A111 fault code across all models, so the exact meaning depends on your boiler's control platform and series. In practice, field technicians encounter this code (or codes that behave similarly) during ignition failures, flame-sensing faults, or temperature-sensor and overheat-related shutdowns. The boiler's control board halts operation when it cannot prove flame during startup, detects an unsafe condition, or receives out-of-range feedback from a thermistor or limit sensor.

Because Weil-McLain model families (Ultra, CGa, and others) use different displays and diagnostic logic, the same-looking code may not mean the same thing across product lines. Always verify your exact model number and consult the wiring diagram or service manual before beginning work. Common real-world causes include a dirty or misaligned flame rod, weak or interrupted gas supply, ignition-system trouble, failed supply or return temperature sensor, circulator or circulation problems, trapped air, low system pressure, or a loose connection on the control board.

## Before You Replace Anything

Homeowners often replace the control board when the real problem is a dirty flame rod or a failed thermistor. Pull and inspect the flame rod first, and measure sensor resistance before ordering electronics.

[Jump to Fix](#fix)

## Common Causes

- **Dirty or misaligned flame sensor (~35%)** Carbon buildup or incorrect rod position prevents the control from proving flame even when the burner lights.
- **Weak or unstable gas supply (~25%)** Low gas pressure, a partially closed valve, or air in the gas line stops the burner from lighting or holding flame.
- **Failed temperature sensor or thermistor (~20%)** An out-of-spec supply or return sensor sends incorrect readings that trigger a safety lockout.
- **Low system pressure or trapped air (~10%)** Below 12 psi or air in the piping causes poor circulation, overheating, and sensor faults.
- **Circulator pump not running (~5%)** A failed or stalled pump prevents water flow and can trigger high-limit or sensor errors.
- **Control board or wiring issue (~5%)** Loose connections, corrosion, or a failed board misread inputs and generate false faults.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the system pressure gauge read 12 psi or higher?</summary>
<div class="dtree-body"><strong>Yes:</strong> Pressure is acceptable. Move on to check the flame rod and ignition sequence.<br><strong>No:</strong> Pressure is too low. Open the fill valve to bring pressure into the 12–25 psi range, purge air, and retry.</div>
</details>

<details class="dtree"><summary>Do you hear the igniter click and see a steady flame through the sight glass?</summary>
<div class="dtree-body"><strong>Yes:</strong> Ignition is working. The fault is likely a dirty flame rod or a sensor problem downstream.<br><strong>No:</strong> No flame or intermittent flame. Check gas valve position, gas supply pressure, and igniter operation before touching sensors.</div>
</details>

<details class="dtree"><summary>Is the circulator pump warm and vibrating during a call for heat?</summary>
<div class="dtree-body"><strong>Yes:</strong> Pump is running. Focus on flame-proving and temperature-sensor diagnostics.<br><strong>No:</strong> Pump may be stuck or failed. Tap the housing gently, check power at the pump terminals, and replace if necessary.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify your exact Weil-McLain model and control board** by checking the rating plate and comparing it to your service manual, because A111 is not a universal fault code across all series.
2. **Check system pressure** at the gauge and top up through the fill valve if pressure is below 12 psi, then purge air from the system at all bleeder valves.
3. **Reset the boiler control** and observe a full ignition sequence, listening for the igniter click and watching through the sight glass for a steady blue flame.
4. **Remove and inspect the flame sensor or flame rod** for carbon buildup, corrosion, or misalignment, clean it with fine sandpaper or steel wool, and reinstall it in the correct position relative to the burner.
5. **Measure gas supply pressure** at the inlet to the gas valve using a manometer or low-pressure gauge, and confirm it matches the pressure specified on the rating plate (consult your model's installation manual for the exact value).
6. **Test the supply and return temperature sensors** by disconnecting each thermistor, measuring resistance with a multimeter, and comparing the reading to the resistance table in your service documentation.
7. **Confirm the circulator pump is running** during a call for heat by feeling for vibration and warmth, and check current draw at the pump terminals if you have an amp clamp (one field report notes a Taco 007 drawing about 0.70 A, but consult your pump's nameplate).
8. **Replace the failed component** (flame rod, thermistor, pump, or control board) only after confirming it tests out of specification, then restart the boiler and monitor through a complete heating cycle to verify stable operation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame sensor or flame rod | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a111-error-code&k=Flame+sensor+or+flame+rod&tag=errorcodefixes-20) \| Match the rod length and mounting bracket to your exact Weil-McLain burner assembly. |
| Supply or return temperature sensor (thermistor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a111-error-code&k=Supply+or+return+temperature+sensor+%28thermistor%29&tag=errorcodefixes-20) \| Verify the resistance curve and connector type against your model's parts diagram. |
| Circulator pump | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a111-error-code&k=Circulator+pump&tag=errorcodefixes-20) \| Common replacements are Taco 007 or Grundfos UPS15-58FC, but confirm flange size and flow rate for your boiler. |
| Boiler control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a111-error-code&k=Boiler+control+board&tag=errorcodefixes-20) \| Order by the exact part number printed on your existing board, as Weil-McLain uses different controls across model families. |

## When to Call a Pro

Call a licensed heating technician whenever you see an A111 or similar fault code on a Weil-McLain boiler. The diagnostic path involves measuring gas pressure, testing flame-proving circuits, and working with 120 V control wiring, all of which require gas-appliance certification and proper combustion-analysis tools. Even if you are comfortable with basic electrical work, the consequences of misadjusting gas pressure, venting, or flame-sensor alignment include carbon-monoxide hazards, equipment damage, and voided warranties. A qualified tech will identify whether the fault stems from ignition, flame-sensing, or temperature-sensor feedback, perform the correct tests in sequence, and replace only the component that has actually failed.

**Rough cost:** A pro service call runs about $150–300.

## See Also

- [Weil-McLain Boiler A55 Error - Causes & Fix](/posts/weil-mclain-boiler-a55-error-code/)
- [Weil-McLain E06 Error Code — Ignition Lockout](/posts/weil-mclain-e06-error-code/)
- [Weil-McLain A162 Error - Causes & Fix](/posts/weil-mclain-boiler-a162-error-code/)
- [Weil-McLain A44 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a44-error-code/)
