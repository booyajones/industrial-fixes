---
title: "Danfoss FC302 VFD AL-114 - Causes & Fix"
description: "AL-114 means earth fault: the drive detects current leaking to ground. Most often caused by motor winding insulation breakdown."
pubDatetime: 2026-06-24T10:11:07Z
modDatetime: 2026-06-24T10:11:07Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Motor cable (appropriately rated for VFD output)"
most_likely_cause: "Motor winding insulation deterioration"
likelihood: "the most frequent culprit"
diy_or_pro: "pro"
free_checks:
  - "Power down and check for loose connections at the drive output terminals (U, V, W) and the motor junction box, then tighten and reset the alarm"
  - "Perform a manual initialization on the drive to clear any current sensor offsets that may have developed"
---

## What this code means
AL-114 (Alarm 14) on a Danfoss FC302 VFD indicates an earth fault. The drive's ground-fault detection circuit has sensed that the sum of the output currents (U, V, W) is not zero, meaning current is leaking from the motor circuit to ground instead of returning through the motor windings. This signals insulation breakdown somewhere in the motor or cable circuit.

When this fault activates, the drive immediately trips and stops to prevent damage and make sure safety. The fault can originate in the motor windings, the cable running to the motor, or inside the drive itself. Moisture, aging insulation, physical cable damage, or failed internal components are the typical culprits.

## Before You Replace Anything

Many technicians replace the entire drive when the fault is actually in the motor or cable. Always disconnect the motor and test the drive with no load first, then megohm-test the motor and cable to ground before condemning the VFD.

## Common Causes

- **Motor winding insulation deterioration (~50%)** Aging, moisture, contamination, or thermal stress breaks down the insulation on motor windings, creating a path to ground (megohm readings below 2 megohms confirm this).
- **Damaged motor cable (~25%)** Physical damage from sharp conduit edges, rodents, or abrasion creates a ground path in the cable between the drive and motor.
- **Loose or corroded connections (~10%)** Loose terminals at the drive output or motor junction box cause arcing or create intermittent ground paths.
- **Failed internal drive components (~10%)** Output IGBTs, gate driver circuits, or current sensors inside the drive have failed, causing the fault to persist even with the motor disconnected.
- **Incorrect parameter settings (~5%)** Motor nominal current parameter set much higher than the actual motor rating can trigger false earth fault detection.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>After tightening all connections and performing a manual initialization, does the fault clear and stay cleared during a test run?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem was a loose connection or sensor offset. Monitor the drive for a few cycles to confirm the fix holds.<br><strong>No:</strong> Proceed to isolate the motor and cable by disconnecting them from the drive output terminals.</div>
</details>

<details class="dtree"><summary>With the motor leads disconnected and the drive powered on, does the AL-114 fault still trip when you attempt to run the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is inside the drive itself (failed IGBTs, gate drivers, or current sensors). Contact Danfoss technical support or a drive repair specialist.<br><strong>No:</strong> The fault is in the motor or cable. Proceed to megohm-test the motor windings and inspect the cable for damage.</div>
</details>

<details class="dtree"><summary>Does a megohm test of the motor windings to ground read 2 megohms or higher?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor insulation is acceptable. Inspect and test the cable for physical damage or insulation breakdown, then replace the cable if needed.<br><strong>No:</strong> The motor winding insulation has failed. Replace the motor or have the windings rewound.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and remove all electrical power before beginning any work.
2. **Inspect and tighten connections** at the drive output terminals (U, V, W) and at the motor junction box, looking for loose, corroded, or burned terminals.
3. **Restore power and perform a manual initialization** on the drive to clear any current sensor offsets, then reset the alarm and attempt a test run.
4. **Disconnect the motor leads** from the drive output terminals, power the drive back on, and attempt to run it with no motor attached to isolate whether the fault is in the drive or the external circuit.
5. **If the fault clears with the motor disconnected**, perform a megohm (insulation resistance) test on the motor windings and cable to ground, looking for readings below 2 megohms that indicate insulation breakdown.
6. **Inspect the motor cable** for physical damage such as cuts, abrasion, sharp conduit edges, or rodent damage, and replace the cable if any damage is found.
7. **If the fault persists with the motor disconnected**, the problem is internal to the drive (failed IGBTs, gate drivers, or current sensors), and you should contact Danfoss technical support or a qualified drive repair center for diagnosis and parts.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable (appropriately rated for VFD output) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-114-fault-code&k=Motor+cable+%28appropriately+rated+for+VFD+output%29&tag=errorcodefixes-20) \| Replace if physical damage or insulation breakdown is found during inspection or megohm testing. |
| Replacement motor (matching HP and voltage) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-114-fault-code&k=Replacement+motor+%28matching+HP+and+voltage%29&tag=errorcodefixes-20) \| Needed if motor winding insulation tests below 2 megohms and cannot be economically rewound. |

## When to Call a Pro

Call a qualified VFD technician or motor specialist if the fault persists after you have tightened connections and performed a manual initialization. If the drive still trips with the motor disconnected, internal drive components (output IGBTs, gate driver circuits, or current sensors) have likely failed and require factory parts and specialized knowledge to replace. Similarly, if megohm testing shows motor winding insulation below 2 megohms, a motor repair shop can assess whether rewinding is cost-effective or if replacement is needed. Working inside a VFD power section involves high-voltage DC bus capacitors that can remain charged even after power is removed, so leave internal drive repairs to trained professionals with the proper safety equipment.

**Rough cost:** A pro service call runs about $150-500 depending on whether the issue is cable repair, motor replacement, or drive internal repair.
