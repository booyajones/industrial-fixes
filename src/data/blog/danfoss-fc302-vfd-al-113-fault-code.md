---
title: "Danfoss AL 13 Fault - Causes & Fix"
description: "AL 13 means overcurrent (150-160% of rated current for several seconds). Most common cause: motor overload or wrong motor current setting."
pubDatetime: 2026-06-24T10:10:12Z
modDatetime: 2026-06-24T10:10:12Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 IGBT inverter module"
most_likely_cause: "Incorrect motor current setting in parameter 1-24 or mechanical overload on the motor shaft"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify parameter 1-24 (nominal motor current) matches the motor nameplate data exactly"
  - "Check all three motor cable connections at drive output terminals (U, V, W) for tightness"
  - "Measure incoming line voltage at all three phases to confirm balance within 3 percent"
no_buy_pct: "40%"
---

## What this code means
Alarm 13 on a Danfoss FC302 VFD signals overcurrent where the drive's output current has gradually built beyond its rated capacity (typically 150 to 160 percent of nominal current) for several seconds. This is distinct from an instantaneous short circuit fault. The drive detects the motor drawing too much current during normal operation or acceleration, usually because the motor shaft is mechanically overloaded, motor parameters (especially nominal motor current in parameter 1-24) are set incorrectly, or a motor winding has developed a partial short.

Cable issues between the drive and motor can also trigger AL 13. Loose connections create resistance that causes current spikes. Inside the drive, aging IGBT modules or failing DC bus capacitors can lose current regulation ability. Short deceleration times on high-inertia loads or incoming line voltage running more than 10 percent above nominal can push the system into fault territory.

## Before You Replace Anything

Technicians often replace the IGBT inverter module before checking motor settings and connections. Always disconnect the motor and run the drive unloaded first; if AL 13 clears, the fault is motor-side and the drive electronics are fine.

## Common Causes

- **Wrong motor current setting (~30%)** Parameter 1-24 (nominal motor current) does not match the motor nameplate, causing the drive to fault on normal load current.
- **Mechanical overload on motor shaft (~25%)** The motor is driving a seized bearing, jammed conveyor, or other stuck load that forces current draw beyond rated capacity.
- **Loose or corroded motor cable connections (~20%)** High resistance at terminals between the drive and motor causes voltage drop and current spikes that trip the overcurrent alarm.
- **Failing IGBT modules in the inverter (~15%)** Aging or damaged IGBT transistors lose current regulation ability and allow uncontrolled current flow to the motor.
- **Motor winding partial short (~10%)** Insulation breakdown inside the motor creates a turn-to-turn short that draws excess current without mechanically stalling the shaft.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does AL 13 clear when you disconnect the motor and run the drive unloaded?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is motor-side (overload, winding short, or wrong parameter setting). Check parameter 1-24 and inspect the motor for mechanical binding or winding faults.<br><strong>No:</strong> The drive has an internal component failure (IGBT modules or DC bus capacitors). Proceed to voltage and IGBT diagnostics.</div>
</details>

<details class="dtree"><summary>Are all three input phases within 3 percent of one another when measured with a voltmeter?</summary>
<div class="dtree-body"><strong>Yes:</strong> Input power is balanced. Focus on motor parameters, cable connections, and deceleration ramp settings.<br><strong>No:</strong> If the low-phase position moves when you swap wires, the supply is unbalanced. If it stays in the same position after swapping, the VFD rectifier section is faulty.</div>
</details>

<details class="dtree"><summary>Does the motor shaft spin freely by hand with power off and motor disconnected?</summary>
<div class="dtree-body"><strong>Yes:</strong> No mechanical jam. Check motor winding resistance between phases for balance (should be within 5 percent of one another) and verify parameter 1-24 matches nameplate current.<br><strong>No:</strong> Mechanical overload is present. Free the load, repair bearings, or remove obstructions before restarting the drive.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect the motor** from the drive output terminals (U, V, W) and run the drive unloaded to isolate whether the fault is internal to the drive or on the motor side.
2. **Verify motor data** in parameters 1-20 through 1-25, especially parameter 1-24 (nominal motor current), matches the motor nameplate exactly.
3. **Check all cable connections** from drive output terminals to motor windings for tightness and corrosion, then measure continuity through each phase.
4. **Measure incoming line voltage** at all three input phases with a voltmeter and confirm they are within 3 percent of one another; swap the low-phase wire and retest to determine if the supply or rectifier is at fault.
5. **Extend deceleration time** in parameter 2-10 if the load has high inertia and the fault occurs during ramp-down, which can cause regenerative current spikes.
6. **Test IGBT modules** on the inverter board with a multimeter in diode-check mode if internal fault is suspected after unloaded test; replace the inverter IGBT assembly if shorted.
7. **Inspect DC link capacitors** on the DC bus board for bulging, leaking, or exploded cases; replace the capacitor bank if damaged, as spikes cause overcurrent trips.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 IGBT inverter module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-113-fault-code&k=Danfoss+FC302+IGBT+inverter+module&tag=errorcodefixes-20) \| Match the part number to your drive's power rating and voltage class (consult the FC302 parts manual) |
| DC bus capacitor bank for Danfoss FC302 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-113-fault-code&k=DC+bus+capacitor+bank+for+Danfoss+FC302&tag=errorcodefixes-20) \| Specify drive frame size and DC voltage rating when ordering |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician if the drive continues to fault after you correct motor parameters and verify cable connections. High-voltage DC bus work, IGBT module replacement, and inverter board diagnostics require specialized meters, safety training, and knowledge of power electronics. If the motor itself has a winding short, a motor shop will need to rewind or replace the stator. Attempting IGBT or capacitor replacement without proper lockout/tagout and DC bus discharge procedures can result in lethal electric shock or arc flash injury.

**Rough cost:** A pro service call runs about $200-800 depending on whether it is a parameter correction, cable repair, or IGBT module replacement.
