---
title: "Danfoss FC302 AL-16 Fault - Causes & Fix"
description: "AL-16 signals an instantaneous short circuit in the drive's output or motor. Most often the drive's IGBT module has failed and needs repair."
pubDatetime: 2026-06-26T09:53:51Z
modDatetime: 2026-06-26T09:53:51Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "IGBT inverter module"
most_likely_cause: "Failed IGBT module in the drive's power stage"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify parameter 1-24 (Nominal Motor Current) matches the motor's nameplate rated current"
  - "Inspect motor cable and terminal box for visible signs of burning, arcing, or loose connections"
---

## Danfoss FC302 AL-16 Fault — What It Means

Alarm 16 on the Danfoss FC302 VFD indicates an instantaneous short circuit condition on the drive's output. The drive detects a catastrophic overcurrent event, typically from a direct short across the DC bus or output phases, and shuts down within microseconds to protect itself. This is the most severe overcurrent fault the drive can throw.

The fault is usually caused by a breakdown inside the drive's IGBT (power semiconductor) modules, creating a hard short between DC+ and DC– rails. Less often it is triggered by a short circuit in the motor windings, motor cable, or incorrect parameter settings that confuse the drive's protection logic.

## Before You Replace Anything

Technicians sometimes replace the entire drive when only the IGBT inverter module or power board has failed. Always disconnect the motor and run the drive unloaded first to isolate whether the fault is in the drive itself or in the motor circuit.

[Jump to Fix](#fix)

## Common Causes

- **IGBT module failure (~60%)** The inverter's semiconductor junctions break down and create a direct short across the DC bus or between output phases.
- **Motor winding short (~20%)** A phase-to-phase or phase-to-ground short inside the motor or at the motor terminal box trips the instantaneous overcurrent protection.
- **Motor cable short (~10%)** Damaged insulation or pinched wiring in the cable between the drive and motor creates a hard fault.
- **Incorrect motor parameter settings (~10%)** Setting the nominal motor current (parameter 1-24) much higher than the actual motor rating causes false overcurrent detection.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the alarm clear when you disconnect the motor from the drive output terminals (U, V, W) and run the drive unloaded?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive itself is healthy and the fault is in the motor or motor cable. Test the motor insulation with a megger and inspect the cable for damage.<br><strong>No:</strong> The drive's power board or IGBT module has failed internally and requires repair or replacement.</div>
</details>

<details class="dtree"><summary>Did you recently change motor parameters or commission a new motor?</summary>
<div class="dtree-body"><strong>Yes:</strong> Double-check parameter 1-24 (Nominal Motor Current) and parameters 120-125 (motor data) against the motor nameplate. Incorrect settings can trigger false alarms.<br><strong>No:</strong> The fault is likely a hardware failure in the drive or motor circuit, not a parameter issue.</div>
</details>

<details class="dtree"><summary>Can you see any visible damage, burn marks, or melted insulation at the motor terminal box or drive output terminals?</summary>
<div class="dtree-body"><strong>Yes:</strong> A catastrophic short has occurred. Replace the damaged cable or motor and inspect the drive's IGBT module for collateral damage.<br><strong>No:</strong> The fault is internal. Proceed with insulation testing and IGBT module diagnostics.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down completely** and lock out the drive. Wait at least 5 minutes for the DC bus capacitors to discharge before touching any terminals.
2. **Disconnect the motor** from the drive output terminals U, V, and W. Leave the input power connected.
3. **Run the drive unloaded** by powering it back on without a motor attached. If Alarm 16 persists, the drive's IGBT module or power board is faulty and must be repaired or replaced.
4. **Test the motor and cable** if the alarm cleared. Use a megger to check insulation resistance between each motor phase and ground. Readings should be above 1 MΩ. Anything lower indicates insulation breakdown.
5. **Verify motor parameters** in the drive. Confirm parameter 1-24 (Nominal Motor Current) matches the motor nameplate rated current exactly. Check parameters 120-125 for correct motor voltage, frequency, and power data.
6. **Replace the faulty component**. If the drive is at fault, replace the IGBT inverter module or the complete power-stage board. If the motor or cable is shorted, repair or replace the damaged component.
7. **Restore connections** and run a test cycle with no load, then gradually bring the motor up to full speed and monitor for alarm recurrence.

## Parts Often Needed

| Part | Notes |
|------|-------|
| IGBT inverter module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-162-fault-code&k=IGBT+inverter+module&tag=errorcodefixes-20) \| The semiconductor power module on the drive's inverter leg. Often sold as a single replaceable assembly. |
| Power-stage board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-162-fault-code&k=Power-stage+board&tag=errorcodefixes-20) \| The complete rectifier and inverter assembly. Replace if multiple IGBTs fail or extensive damage is present. |

## When to Call a Pro

Call a qualified VFD technician or drive repair specialist for Alarm 16. This fault involves high-voltage DC bus components and sensitive IGBT modules that require specialized test equipment and experience to diagnose safely. Incorrect handling can destroy the drive or create a shock hazard. A professional can isolate the fault between the drive and motor, perform insulation resistance testing with a megger, and replace IGBT modules or power boards using factory-approved procedures. If you lack high-voltage training or the tools to safely discharge and test DC bus components, do not attempt this repair yourself.

**Rough cost:** A pro service call runs about $300-900.
