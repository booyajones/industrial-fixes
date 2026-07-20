---
title: "ABB ACS580 VFD E0013 Fault - Causes & Fix"
description: "E0013 indicates an overcurrent or ground fault trip. Most often caused by wiring problems or motor insulation breakdown."
pubDatetime: 2026-07-18T07:44:48Z
modDatetime: 2026-07-18T07:44:48Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - abb
money_part: "Motor power cable (shielded VFD-rated)"
most_likely_cause: "Motor cable insulation failure or incorrect wiring"
likelihood: "often the cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect motor cable for visible damage, pinch points, or abraded insulation"
  - "Check all three motor terminals and ground connections for tightness and corrosion"
  - "Review drive parameter settings to confirm motor nameplate data matches configured values"
---

## ABB ACS580 VFD E0013 Fault — What It Means

The E0013 fault code on an ABB ACS580 variable frequency drive typically signals an overcurrent condition or ground fault detected during operation. The drive's internal protection circuitry has tripped because current flow exceeded safe limits or a path to ground was detected in the motor circuit. This fault protects the drive and motor from damage due to short circuits, insulation breakdown, or wiring faults.

The exact threshold and behavior depend on your drive's parameter settings and application profile. Consult your ACS580 manual for the precise definition of E0013 for your firmware version, as fault codes can vary slightly across different models and software releases. The drive will not restart until the fault is cleared and the underlying issue is resolved.

## Before You Replace Anything

Technicians sometimes replace the VFD itself when the actual problem is damaged motor cable insulation or a short in the motor windings. Use a megohm meter to test cable and motor insulation resistance before condemning the drive.

[Jump to Fix](#fix)

## Common Causes

- **Motor cable insulation breakdown (~35%)** Damaged or aged cable insulation allows current to leak to ground or creates a short between phases.
- **Motor winding fault (~25%)** Internal insulation failure in the motor windings creates a short circuit or ground path that trips the drive.
- **Loose or corroded connections (~15%)** Poor connections at the drive output terminals or motor junction box create intermittent faults or arcing that triggers overcurrent protection.
- **Incorrect drive parameters (~10%)** Motor parameters programmed into the drive do not match the actual motor nameplate, causing the drive to misinterpret normal current as a fault condition.
- **Ground fault in conduit or cable tray (~10%)** Motor cable touching grounded metal conduit or tray due to damaged outer jacket allows leakage current to ground.
- **Drive output stage failure (~5%)** Internal damage to the drive's IGBT output transistors or gate drivers can cause erratic current output and fault detection.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault occur immediately on power-up before the motor even starts?</summary>
<div class="dtree-body"><strong>Yes:</strong> Indicates a hard short or ground fault in the wiring or motor. Disconnect the motor and test cable and motor insulation separately with a megohm meter.<br><strong>No:</strong> The fault occurs during operation, which suggests a dynamic issue like loose connections, motor overload, or intermittent insulation breakdown under load.</div>
</details>

<details class="dtree"><summary>When you disconnect the motor cables from the drive outputs, does the fault clear and allow the drive to power up normally?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem is downstream of the drive in the motor cable or motor itself. Test insulation resistance on the cable and motor windings.<br><strong>No:</strong> The fault persists without a motor connected, pointing to an internal drive issue or incorrect parameter configuration.</div>
</details>

<details class="dtree"><summary>Are the drive's programmed motor parameters (voltage, current, frequency) consistent with the motor nameplate?</summary>
<div class="dtree-body"><strong>Yes:</strong> Parameters are correct, so focus on physical wiring, cable condition, and motor insulation testing.<br><strong>No:</strong> Re-enter the correct motor nameplate data into the drive parameters and run an auto-tune if your model supports it.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** to the drive at the supply disconnect and lock out the circuit breaker following your facility's electrical safety procedures.
2. **Verify the fault code** by reviewing the drive display or parameter log to confirm E0013 and note whether it occurred at startup or during run.
3. **Inspect all motor cable connections** at the drive output terminals (U, V, W) and at the motor junction box for tightness, discoloration, or signs of arcing.
4. **Disconnect the motor cables** from the drive output terminals and measure insulation resistance from each motor lead to ground and between phases using a megohm meter set to at least 500 VDC.
5. **Test the motor windings** separately by disconnecting the motor leads at the motor junction box and measuring winding-to-ground and phase-to-phase insulation resistance; readings below 1 megohm indicate insulation failure.
6. **Review drive parameters** in the programming menu to confirm motor voltage, current, frequency, and power factor match the motor nameplate exactly; correct any mismatches and save changes.
7. **Reconnect the motor** if insulation tests pass, restore power, clear the fault using the drive keypad or reset input, and monitor the drive during a test run under no load then gradually increase load while watching current readings.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor power cable (shielded VFD-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0013-fault-code&k=Motor+power+cable+%28shielded+VFD-rated%29&tag=errorcodefixes-20) \| Replace if insulation resistance tests fail or cable jacket is damaged; must be rated for VFD use with proper shielding |
| Three-phase AC motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0013-fault-code&k=Three-phase+AC+motor&tag=errorcodefixes-20) \| Required if motor winding insulation has failed and cannot be rebuilt; verify frame size and nameplate specifications |

## When to Call a Pro

Call a qualified electrician or controls technician if you are not trained in high-voltage work or do not have access to insulation test equipment. The ACS580 operates at voltages that can cause severe injury or death. A professional can safely perform insulation resistance testing, verify drive parameters, and trace ground faults in the motor circuit. If the drive itself has failed internally, replacement or factory repair requires proper configuration and commissioning to match your application. Any work inside the drive enclosure or on live circuits must be performed by personnel with appropriate electrical safety training.

**Rough cost:** A pro service call runs about $200-800.
