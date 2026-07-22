---
title: "Yaskawa GA800 VFD F0014 Fault - Causes & Fix"
description: "F0014 on a Yaskawa GA800 VFD signals a ground fault or excessive leakage current. Check motor cable insulation and grounding first."
pubDatetime: 2026-07-20T07:37:11Z
modDatetime: 2026-07-20T07:37:11Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "VFD-rated motor cable"
most_likely_cause: "damaged motor cable insulation"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect motor cable for visible damage, pinching, or contact with sharp edges"
  - "Check that motor and drive chassis are properly bonded to earth ground"
  - "Verify all cable glands and conduit fittings are tight and moisture-free"
part_price: "$80-300"
---

## Yaskawa GA800 VFD F0014 Fault — What It Means

The F0014 fault code on a Yaskawa GA800 variable frequency drive indicates a ground fault or excessive leakage current detected between the motor and ground. The drive has shut down to protect itself and the motor from damage caused by current flowing through an unintended path to ground.

This fault typically appears when the drive detects an imbalance in the current flowing to the motor compared to the current returning, suggesting some current is leaking to ground through damaged insulation, moisture intrusion, or a wiring fault. The drive's internal ground fault protection circuit monitors for this condition and trips when the leakage exceeds the threshold programmed in the drive parameters.

## Before You Replace Anything

Technicians sometimes replace the VFD itself when the fault is actually in the motor cable or motor windings. Always perform insulation resistance testing on the motor and cables with a megohmmeter before replacing the drive.

[Jump to Fix](#fix)

## Common Causes

- **Damaged motor cable insulation (~40%)** Worn, pinched, or moisture-contaminated motor cable allows current to leak to ground through the outer sheath or conduit.
- **Motor winding insulation failure (~30%)** Insulation breakdown inside the motor windings creates a path for current to flow directly to the motor frame and ground.
- **Moisture or contamination in motor junction box (~15%)** Water, condensation, or conductive dust in the motor terminal box provides a leakage path between phases and ground.
- **Loose or corroded ground connections (~10%)** Poor grounding creates resistance that can cause nuisance ground fault detection or allow actual faults to develop.
- **VFD ground fault detection circuit fault (~5%)** The drive's internal current sensing or ground fault protection circuitry may fail and trigger false alarms.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault appear immediately when you power up the drive, before issuing a run command?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem is likely in the drive itself or the incoming power wiring. Check input power grounding and verify drive parameters are set correctly for your installation.<br><strong>No:</strong> The fault occurs during operation, pointing to the motor, motor cable, or load. Proceed with cable and motor insulation testing.</div>
</details>

<details class="dtree"><summary>Can you disconnect the motor cable at the drive and run the drive into a known-good test motor without faulting?</summary>
<div class="dtree-body"><strong>Yes:</strong> The original motor or its cable is at fault. Perform insulation resistance testing on both to isolate which component has failed.<br><strong>No:</strong> The drive itself may have a failed ground fault detection circuit or internal component. Consult factory support or plan for drive replacement.</div>
</details>

<details class="dtree"><summary>Does a megohmmeter test show motor winding insulation resistance above 2 megohms to ground?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor windings are likely acceptable. Focus on the motor cable, connections, and any external contamination or moisture paths.<br><strong>No:</strong> Motor winding insulation has failed and the motor requires rewinding or replacement.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** to the VFD at the main disconnect and lock out the circuit per your facility lockout-tagout procedure.
2. **Record the fault** history by viewing the drive's fault log to see if F0014 has occurred before and under what conditions.
3. **Inspect the motor cable** from the drive output terminals to the motor junction box for physical damage, tight bends, pinch points, or areas where insulation may be compromised.
4. **Check all grounding connections** at the drive chassis, motor frame, conduit fittings, and earth ground to verify they are tight, clean, and continuous.
5. **Perform insulation resistance testing** using a megohmmeter set to 500V DC or 1000V DC (consult your motor nameplate voltage). Test each motor phase to ground and phase-to-phase with the motor disconnected from the drive. Values below 2 megohms indicate insulation failure.
6. **Inspect the motor junction box** for moisture, dust, carbon tracking, or loose terminal connections that could create a leakage path.
7. **Reset the drive** and attempt to run it. If the fault recurs immediately, disconnect the motor cable at the drive and test into a known-good motor or resistive load bank to isolate whether the problem is in the drive or the field wiring and motor.

## Parts Often Needed

| Part | Notes |
|------|-------|
| VFD-rated motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f0014-fault-code&k=VFD-rated+motor+cable&tag=errorcodefixes-20) \| Shielded, stranded cable rated for variable frequency drive use; size according to your motor nameplate current and cable run length |
| Motor terminal block or junction box | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f0014-fault-code&k=Motor+terminal+block+or+junction+box&tag=errorcodefixes-20) \| Replacement terminal assembly if contamination or tracking damage cannot be cleaned |

## When to Call a Pro

Ground fault diagnosis and repair on a VFD system requires high-voltage test equipment, including a megohmmeter capable of testing at motor voltage levels, and familiarity with industrial electrical safety practices. If you do not have lockout-tagout training, insulation testing tools, or experience working with three-phase motor drives, call a qualified industrial electrician or motor service technician. Any work inside the VFD enclosure or motor requires de-energizing and verifying zero voltage with a rated tester. If insulation testing reveals a motor winding fault, motor shops can perform rewind services or help size a replacement motor. VFD parameter adjustments and ground fault sensitivity settings should only be changed by someone trained on the specific Yaskawa GA800 programming software and familiar with the application requirements.

**Rough cost:** A pro service call runs about $200-800.
