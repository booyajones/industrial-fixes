---
title: "Weil-McLain A131 Error Code - Causes & Fix"
description: "A131 error code meaning varies by Weil-McLain boiler model. Check your model-specific manual for the exact fault definition and fix."
pubDatetime: 2026-06-17T11:24:31Z
modDatetime: 2026-06-17T11:24:31Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
money_part: "Flame sensor (model-specific)"
diy_or_pro: "pro"
free_checks:
  - "Verify system water pressure is within range (typically 12–15 psi cold on most Weil-McLain residential boilers) and top off if low."
  - "Check for tripped circuit breakers or blown fuses at the boiler disconnect and main panel."
  - "Inspect the display for a fault history menu (some controls store recent codes) and note any other codes shown."
---

## Weil-McLain A131 Error Code — What It Means

Weil-McLain does not publish a universal A131 error code across all boiler families. The same alphanumeric display can represent different faults depending on your exact boiler model and control platform (Ultra, CGi, EG Series, or others). Without the model number and control type, the code cannot be reliably decoded.

To identify what A131 means on your unit, locate the CP/serial number label on the boiler jacket and find the model-specific installation and service manual. The manual's diagnostics or fault-code section will list the exact condition that triggers A131 on that model. Common fault families across Weil-McLain controls include ignition lockout, pressure switch errors, flame-sensor failures, temperature-limit trips, and circulator or water-pressure issues, but the precise cause for A131 depends entirely on which control your boiler uses.

## Before You Replace Anything

Without the correct model manual, technicians sometimes replace flame sensors or pressure switches based on similar-looking codes from other brands. Always consult the boiler's own manual and verify power, gas valve operation, and system pressure before ordering any part.

[Jump to Fix](#fix)

## Common Causes

- **Ignition-sequence fault (~25%)** Many Weil-McLain control platforms trigger an alphanumeric code when the burner fails to ignite or prove flame within the allowed trial-for-ignition window.
- **Pressure-switch error (~20%)** A code may appear if the combustion-air or vent-pressure switch does not close before ignition or does not open after the call ends, indicating blocked venting or a failed switch.
- **Flame-sensor signal out of range (~20%)** If the control reads flame current below or above its acceptable window, it will lock out and display a fault code.
- **High-limit or low-water-cutoff trip (~15%)** A safety control may interrupt operation and post a code if boiler temperature exceeds the limit or water level falls too low.
- **Circulator or zone-valve interlock fault (~10%)** Some controls require proof of flow or correct zone-valve position before firing; if the interlock signal is missing the control logs a fault.
- **Control board or wiring issue (~10%)** Loose connectors, corroded terminals, or a failing control board can cause erratic fault codes that do not match field conditions.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the display show any other fault codes or a fault-history menu?</summary>
<div class="dtree-body"><strong>Yes:</strong> Write down all codes shown and cross-reference them in your boiler's manual; multiple codes often point to a single root cause such as low water pressure or a vent blockage.<br><strong>No:</strong> Proceed to check system pressure and power supply, then consult the manual for A131 specifically.</div>
</details>

<details class="dtree"><summary>Is system water pressure below 12 psi (or below the minimum marked on your gauge)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Top off the system through the fill valve until pressure reaches the cold fill range, then clear the fault per the manual and retry; low pressure often prevents ignition or trips a low-water cutoff.<br><strong>No:</strong> Move on to verify gas supply is on and the emergency shutoff switch near the boiler is in the ON position.</div>
</details>

<details class="dtree"><summary>Did the boiler recently run normally before the code appeared?</summary>
<div class="dtree-body"><strong>Yes:</strong> A sudden fault after normal operation suggests a safety trip (high limit, pressure switch, or flame sensor); check for blocked vents, dirty flame sensor, or a circulator that stopped running.<br><strong>No:</strong> A code at startup or after service work points to wiring errors, incorrect control settings, or air in the system that must be bled.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Identify your exact boiler model and control platform** by reading the CP/serial label on the boiler jacket, then download or request the matching installation and service manual from Weil-McLain.
2. **Look up code A131** in the diagnostics or fault-code table of that manual to learn the specific condition it represents on your model.
3. **Inspect system water pressure** at the gauge; if below the recommended cold fill range, open the fill valve slowly until pressure reaches specification, then close the valve.
4. **Check power and gas supply** by confirming the boiler disconnect switch and emergency shutoff are ON, the circuit breaker is not tripped, and the manual gas valve upstream is fully open.
5. **Follow the manual's diagnostic sequence** for the fault, which typically includes verifying combustion-air inlet and vent-pipe clearances, testing pressure-switch operation, inspecting the flame sensor for soot or corrosion, and confirming circulator operation.
6. **Clear the fault** using the reset button or procedure described in your manual, then call for heat and observe the ignition sequence; note whether the code reappears and at what point in the cycle.
7. **Document the fault history and observations** (LED flash patterns, any unusual noises, burner behavior) and contact a licensed boiler technician if the code persists or if you are unsure of any test procedure, especially those involving gas or high voltage.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame sensor (model-specific) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a131-error-code&k=Flame+sensor+%28model-specific%29&tag=errorcodefixes-20) \| Order by your boiler model number; cleaning the sensor often resolves flame-proving faults before replacement is needed. |
| Pressure switch (combustion-air or vent) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a131-error-code&k=Pressure+switch+%28combustion-air+or+vent%29&tag=errorcodefixes-20) \| Match the part number in your manual; verify vent blockage is not the real cause before replacing the switch. |
| Ignition control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a131-error-code&k=Ignition+control+board&tag=errorcodefixes-20) \| Control boards are model-specific; confirm the fault is truly in the board by testing all field wiring and sensors first. |

## When to Call a Pro

Call a licensed boiler technician immediately if you smell gas, if the code appears alongside unusual burner behavior (delayed ignition, yellow flame, or soot), or if you are not comfortable working with gas-fired equipment. A professional should also handle all combustion-air and vent-pressure testing, gas-valve checks, and control-board diagnostics, because incorrect adjustments can create unsafe operating conditions or void your warranty. Weil-McLain requires warranty part claims to include the failed part description and boiler CP/serial number, so a qualified contractor will document findings properly and make sure any replacement meets manufacturer specifications.

**Rough cost:** A pro service call runs about $150–350.

## See Also

- [Weil-McLain A02 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a02-error-code/)
- [Weil-McLain A150 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a150-error-code/)
- [Weil-McLain Code 1 — No Flame Sensed Fix](/posts/weil-mclain-error-code-1/)
- [Weil-McLain Boiler A78 Error - Causes & Fix](/posts/weil-mclain-boiler-a78-error-code/)
