---
title: "Danfoss FC302 AL-13 Fault - Causes & Fix"
description: "AL-13 means overcurrent: drive output exceeded safe peak current (150–160% of nominal). Most often a mechanical overload or motor issue."
pubDatetime: 2026-06-25T09:21:37Z
modDatetime: 2026-06-25T09:21:37Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 IGBT Inverter Module"
most_likely_cause: "Mechanical overload on the motor shaft"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Check input power: measure all three input phases with a voltmeter and confirm they are within 3% of one another"
  - "Inspect all input and output terminal connections for tightness and corrosion"
  - "Verify motor parameter 1-24 (nominal motor current) matches the motor nameplate"
---

## Danfoss FC302 AL-13 Fault — What It Means

AL-13 (sometimes shown as Err 13) indicates an overcurrent fault. The drive detected that output current exceeded its rated capacity during normal operation or acceleration. The trip occurs when current remains above 100% overload for too long, or spikes to 150–160% of nominal current. This is not an instantaneous short circuit but rather a sustained current buildup beyond what the drive can safely handle. The peak current limit circuit activates to protect the drive's output stage from damage.

The fault can come from two broad areas: external problems (motor, load, cables, or parameter settings) or internal drive component failures (IGBTs, rectifier, capacitors, or power board). Pinpointing which side is responsible requires isolating the motor from the drive and running unloaded.

## Before You Replace Anything

Technicians often replace the entire power board or IGBT module before checking the motor and load. Always disconnect the motor and run the drive unloaded first. If the fault clears, the drive is fine and the problem is external.

[Jump to Fix](#fix)

## Common Causes

- **Mechanical overload (~35%)** The motor shaft is mechanically overloaded by a jammed pump, stuck fan, or other blocked load preventing rotation.
- **Incorrect motor parameters (~20%)** Parameter 1-24 (nominal motor current) or other motor data (parameters 1-20 to 1-25) are set incorrectly for the actual motor.
- **Failed IGBT modules (~18%)** Aging or shorted IGBT modules in the inverter section lose regulation ability and allow current surges.
- **Motor winding or cable issues (~15%)** Partial short in motor windings, deteriorating insulation, or loose connections between drive and motor create resistance and current spikes.
- **Rectifier or DC link failure (~10%)** Failed diode in the input rectifier assembly or exploding DC link capacitor causes voltage instability and current surges.
- **Missing external fan selection (~2%)** Motor external fan not selected in parameter 1-91 causes thermal loading and higher operating current.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Are all three input phases within 3% of one another when measured with a voltmeter?</summary>
<div class="dtree-body"><strong>Yes:</strong> Input power is balanced. Proceed to isolate the motor and check for external vs. internal faults.<br><strong>No:</strong> Unbalanced input power can cause overcurrent. Check for loose input wires, blown facility fuses, or supply voltage problems before diagnosing the drive.</div>
</details>

<details class="dtree"><summary>Does the AL-13 fault clear when you disconnect the motor and run the drive unloaded?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive itself is working. The fault is external: inspect the motor for mechanical binding, check motor windings and cables, and verify motor parameter settings.<br><strong>No:</strong> The drive has an internal component failure (IGBT, rectifier, power board, or DC link capacitor). Call a VFD technician or electrician.</div>
</details>

<details class="dtree"><summary>Does the motor shaft turn freely by hand with power off?</summary>
<div class="dtree-body"><strong>Yes:</strong> Mechanical load is not jammed. Check motor insulation, cable continuity, and parameter 1-24 settings.<br><strong>No:</strong> Mechanical overload is present. Inspect the driven equipment (pump, fan, conveyor) for blockages or seized bearings.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify input power balance.** Measure all three input phases with a voltmeter and confirm they are within 3% of one another. Check for blown input fuses and tighten all input terminal connections.
2. **Isolate the motor from the drive.** Disconnect all three motor leads from the drive output terminals U, V, and W. Run the drive unloaded and observe whether AL-13 recurs.
3. **If the fault clears unloaded**, the problem is external. Inspect the motor and load for mechanical binding or overload. Check motor cable continuity and insulation resistance. Verify parameter 1-24 matches the motor nameplate current.
4. **If the fault persists unloaded**, the drive has an internal failure. Inspect the IGBT modules on the inverter board for shorts. Test the rectifier diodes and inspect the DC link capacitors for bulging or leakage.
5. **Replace failed internal components.** If IGBTs or the rectifier are faulty, replace the inverter IGBT modules or the entire power board assembly as needed. Consult the drive service manual for part numbers and replacement procedures.
6. **Re-verify all parameters.** After any repair, confirm parameters 1-20 through 1-25 match the motor nameplate and that parameter 1-91 is set correctly if an external fan is used.
7. **Test under load.** Reconnect the motor and run the drive through a full acceleration and load cycle to confirm the overcurrent fault is resolved.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 IGBT Inverter Module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-133-fault-code&k=Danfoss+FC302+IGBT+Inverter+Module&tag=errorcodefixes-20) \| Match the module part number to your drive's power rating and voltage class. Consult the service manual for the correct module. |
| Danfoss FC302 Power Board Assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-133-fault-code&k=Danfoss+FC302+Power+Board+Assembly&tag=errorcodefixes-20) \| Complete rectifier and inverter assembly. Used when multiple components have failed or when individual module replacement is not practical. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician if the fault persists with the motor disconnected, indicating internal drive failure. High-voltage DC link capacitors (often 400–600 VDC or more) and IGBT modules pose serious shock and arc-flash hazards. Also call a pro if you are not trained to isolate and test motor windings, measure three-phase power, or interpret VFD parameters. Any work inside the drive enclosure requires lockout-tagout and knowledge of capacitor discharge procedures. If the motor is part of a critical process (pump, HVAC, conveyor), a technician can minimize downtime and verify the load is not damaging the new components.

**Rough cost:** A pro service call runs about $300-1200.
