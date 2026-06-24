---
title: "Weil-McLain A130 Error Code - Causes & Fix"
description: "A130 meaning varies by Weil-McLain boiler model. Check your manual for the exact fault. Most likely: low system pressure or flow issue."
pubDatetime: 2026-06-17T11:23:33Z
modDatetime: 2026-06-17T11:23:33Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - boiler
  - weil-mclain
money_part: "Circulator pump (Weil-McLain or Taco)"
diy_or_pro: "pro"
free_checks:
  - "Check system pressure gauge and add water if below minimum (typically 12-15 psi cold)"
  - "Open all zone valves and isolation valves to restore flow"
  - "Bleed air from circulator and high points in the loop"
---

## Weil-McLain A130 Error Code — What It Means

A130 is not a universal code across all Weil-McLain boilers. The exact meaning depends on your specific model and control platform. Weil-McLain directs technicians to the model-specific manual for the error definition and fault-history steps. Without the manufacturer documentation for your exact model, the precise fault cannot be stated with confidence.

Based on Weil-McLain diagnostic workflows and typical boiler fault patterns, codes in this range often point to system conditions like low pressure, poor flow, blocked circulation, air in the hydronic loop, or sensor faults. The first step is to retrieve the stored fault history from the control menu and consult your model manual before attempting any repair or reset.

## Before You Replace Anything

Technicians sometimes replace the circulator pump or control board before verifying system pressure, closed isolation valves, or trapped air. Check pressure gauge reading and open all valves first.

[Jump to Fix](#fix)

## Common Causes

- **Low system pressure or closed valve (~35%)** System pressure dropped below the minimum threshold or an isolation valve was left closed, blocking circulation and triggering a lockout.
- **Air trapped in the hydronic loop (~25%)** Air pockets in the circulator, near the boiler, or at high points prevent proper flow and can mimic a pressure or sensor fault.
- **Failed or dirty temperature sensor (~20%)** A thermistor-type sensor reads incorrectly or is fouled, sending out-of-range signals that the control interprets as a fault.
- **Circulator failure or blockage (~15%)** The circulator pump is not spinning, is airlocked, or the impeller is jammed, preventing flow through the heat exchanger.
- **Control board fault or wiring issue (~5%)** A loose connector, corroded terminal, or failed relay on the control board prevents normal startup or sensor communication.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the system pressure gauge below 12 psi when cold?</summary>
<div class="dtree-body"><strong>Yes:</strong> Add water through the fill valve until pressure reaches 12-15 psi cold, then try a reset.<br><strong>No:</strong> Pressure is adequate. Move on to checking valves and air.</div>
</details>

<details class="dtree"><summary>Are all zone valves and isolation valves fully open?</summary>
<div class="dtree-body"><strong>Yes:</strong> Flow path is clear. Check for air in the circulator and bleed if needed.<br><strong>No:</strong> Open every valve in the system, wait a minute, then reset the boiler.</div>
</details>

<details class="dtree"><summary>Can you hear or feel the circulator pump running when the boiler calls for heat?</summary>
<div class="dtree-body"><strong>Yes:</strong> Circulator is energized. The fault likely lies in a sensor, air, or control communication issue.<br><strong>No:</strong> Circulator is not running. Check power to the pump, wiring, and the pump itself for a seized rotor.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Record the fault history** from the control or contractor menu by following the button sequence in your model manual so you capture the exact error and any repeating pattern.
2. **Check system pressure** on the gauge. If below 12 psi cold, open the fill valve slowly and bring the system to 12-15 psi, then close the valve.
3. **Open all isolation and zone valves** fully. Walk the entire loop and confirm every valve handle is in the open position.
4. **Bleed air** from the circulator vent screw and any manual air vents at high points in the piping until you see solid water with no bubbles.
5. **Verify circulator operation** by listening for the hum and feeling for vibration at the pump body when the boiler calls for heat. If silent, check power and wiring to the pump.
6. **Inspect sensor connections** at the boiler supply and return. Look for loose spade terminals, corrosion, or moisture. Reseat or clean connectors as needed.
7. **Reset the boiler once** using the reset button. Observe the startup sequence. If the fault returns immediately, consult the model manual for sensor resistance or voltage checks and call a technician if the cause is not obvious.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Circulator pump (Weil-McLain or Taco) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a130-error-code&k=Circulator+pump+%28Weil-McLain+or+Taco%29&tag=errorcodefixes-20) \| Match horsepower and flange size to your model. Verify pump is actually failed before ordering. |
| Temperature sensor (thermistor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a130-error-code&k=Temperature+sensor+%28thermistor%29&tag=errorcodefixes-20) \| Model-specific NTC sensor. Consult manual for correct part number and resistance table. |

## When to Call a Pro

Call a licensed boiler technician if you have restored system pressure, bled all air, confirmed all valves are open, and the A130 fault returns after one reset. The technician will retrieve the full fault history from the control, measure sensor resistance and voltage against the model-specific table, verify ignition and flame sensing if applicable, and test the circulator and control board with proper test equipment. Do not attempt repeated resets or any work on gas piping, combustion components, or high-voltage wiring. If you smell gas or see water leaking from the boiler, shut off the gas valve and power switch and call immediately.

**Rough cost:** A pro service call runs about $150-400.

## See Also

- [Weil-McLain A04 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a04-error-code/)
- [Weil-McLain A74 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a74-error-code/)
- [Weil-McLain Boiler A69 Error - Causes & Fix](/posts/weil-mclain-boiler-a69-error-code/)
- [Weil-McLain Boiler A24 Error - Causes & Fix](/posts/weil-mclain-boiler-a24-error-code/)
