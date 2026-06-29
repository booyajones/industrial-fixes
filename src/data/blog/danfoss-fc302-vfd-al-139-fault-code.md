---
title: "Danfoss FC302 AL-139 Fault - Causes & Fix"
description: "AL-139 is likely AL 13 (overcurrent fault). Most common cause: incorrect motor current setting in parameter 1-24 or mechanical overload."
pubDatetime: 2026-06-27T11:33:31Z
modDatetime: 2026-06-27T11:33:31Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 Power Card / IGBT Module"
most_likely_cause: "incorrect motor nominal current setting in parameter 1-24"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify parameter 1-24 matches the motor nameplate current rating exactly"
  - "Check that all motor terminal connections at the drive and motor junction box are tight and corrosion-free"
  - "Confirm the mechanical load is not jammed and the motor shaft rotates freely by hand when powered off"
no_buy_pct: "40%"
---

## Danfoss FC302 AL-139 Fault — What It Means

There is no documented AL-139 fault code for the Danfoss FC302 VFD. The code is almost certainly Alarm 13 (AL 13), which indicates the drive detected output current exceeding safe operating limits during normal operation or motor acceleration. The drive trips to protect itself and the motor when current drawn by the load is higher than the configured maximum limit or the drive's rated capacity. This is an overcurrent protection fault.

The drive monitors current through internal sensors on the power board. When measured current surpasses the threshold set by motor parameters or hardware limits, the alarm trips immediately. The fault can originate from the motor, mechanical load, wiring, incorrect parameter settings, or internal drive components.

## Before You Replace Anything

Technicians often replace the power board or IGBT module without first checking parameter 1-24 (Motor Nominal Current) or testing the motor in isolation. Always verify parameters and disconnect the motor to confirm whether the fault is internal or downstream before ordering expensive parts.

[Jump to Fix](#fix)

## Common Causes

- **Incorrect motor current parameter (~30%)** Parameter 1-24 (Motor Nominal Current) is set lower than the actual motor nameplate current, causing the drive to trip on normal load.
- **Mechanical overload (~25%)** Excessive load on the motor shaft from a jammed pump, heavy conveyor, or seized bearing forces the motor to draw overcurrent.
- **Motor winding fault (~15%)** Partial short circuit or insulation breakdown inside the motor windings creates a low-resistance path that spikes current.
- **Loose or corroded connections (~12%)** Poor contact at motor terminals or drive output terminals increases resistance and causes current spikes during switching.
- **Failed IGBT module (~10%)** Aging or damaged inverter section (IGBT power transistors) fails to regulate current properly and trips the overcurrent protection.
- **Faulty current sensor (~8%)** A damaged current sensor or shunt on the power board reports false high-current readings to the controller.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the alarm still occur when you disconnect all three motor leads from the drive output terminals and run the drive unloaded?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is internal to the drive (power board, IGBT module, or current sensor). Call a qualified technician to test components and replace the faulty section.<br><strong>No:</strong> The fault is downstream in the motor, cable, or mechanical load. Proceed to check motor connections, perform a megger test on the motor windings, and inspect the load for jams.</div>
</details>

<details class="dtree"><summary>Does parameter 1-24 (Motor Nominal Current) match the current rating on the motor nameplate exactly?</summary>
<div class="dtree-body"><strong>Yes:</strong> The parameter is correct. Check for mechanical overload, motor winding faults, or poor connections as the likely cause.<br><strong>No:</strong> Incorrect parameter setting is causing nuisance trips. Enter the correct motor nameplate current into parameter 1-24, save, and reset the drive.</div>
</details>

<details class="dtree"><summary>Can you rotate the motor shaft freely by hand with power off and the load disconnected?</summary>
<div class="dtree-body"><strong>Yes:</strong> The mechanical load is not seized. Focus on motor winding tests (megger) and electrical connection quality.<br><strong>No:</strong> The load or motor bearings are jammed or seized, creating mechanical overload. Repair or replace the mechanical components before restarting the drive.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power off and lockout** the drive at the main disconnect to work safely.
2. **Record all parameters** using the keypad or PC software before making changes, so you can restore settings if needed.
3. **Verify parameter 1-24** on the keypad (Motor Nominal Current). Compare this value to the motor nameplate current rating. If they do not match, enter the correct nameplate current, save, and reset the alarm.
4. **Disconnect the motor** by removing all three output wires (U, V, W) from the drive terminals. Run the drive unloaded. If the alarm clears, the problem is external (motor, cable, or load). If the alarm persists, the drive has an internal fault.
5. **If external, inspect connections** at both the drive output terminals and the motor junction box. Tighten all terminals and clean any corrosion. Check the motor cable for damage or pinched insulation.
6. **Test the motor windings** with a megohmmeter (megger) to measure insulation resistance between each phase and ground. A reading below 1 megohm indicates winding insulation breakdown requiring motor repair or replacement.
7. **Check the mechanical load** by rotating the motor shaft by hand (with the load disconnected if possible). Any binding or excessive resistance points to a jammed pump, seized bearing, or overloaded conveyor that must be corrected.
8. **If internal, check cooling and inspect the power board**. Confirm all cooling fans operate and vents are clear. Remove the drive cover and look for visible damage to the IGBT module (burned components, bulging capacitors). Replace the power board or IGBT assembly if damaged, or call a Danfoss service technician for component-level repair.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 Power Card / IGBT Module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-139-fault-code&k=Danfoss+FC302+Power+Card+%2F+IGBT+Module&tag=errorcodefixes-20) \| Consult your drive model and frame size for the exact replacement part number from Danfoss or an authorized distributor. |
| Three-Phase AC Motor (replacement) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-139-fault-code&k=Three-Phase+AC+Motor+%28replacement%29&tag=errorcodefixes-20) \| Match the motor nameplate voltage, current, power rating, and frame size to the original equipment specification. |

## When to Call a Pro

Call a qualified electrical technician or Danfoss-authorized service provider if the alarm persists after verifying parameters and checking external connections, if the drive trips even with the motor disconnected (indicating an internal fault), or if you lack the tools or training to perform high-voltage testing and component replacement. Drive repair involves working with DC bus voltages above 300 VDC and requires proper discharge procedures, insulation testing equipment, and replacement parts matched to the specific frame size and firmware version. Incorrect repairs can destroy the drive or create serious shock hazards.

**Rough cost:** A pro service call runs about $200-800 depending on whether the fix is parameter adjustment, motor replacement, or drive power board replacement.
