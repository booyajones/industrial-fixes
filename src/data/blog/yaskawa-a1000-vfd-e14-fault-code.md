---
title: "Yaskawa A1000 VFD E14 Fault - Causes & Fix"
description: "E14 on a Yaskawa A1000 signals a ground fault or output short. Check motor and cable insulation, then motor terminal connections."
pubDatetime: 2026-07-22T07:41:24Z
modDatetime: 2026-07-22T07:41:24Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "VFD-rated shielded motor cable"
most_likely_cause: "Degraded motor winding insulation or cable insulation"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Visually inspect the motor and output cables for physical damage, moisture, or burn marks"
  - "Check that all motor terminal connections are tight and properly torqued"
  - "Verify that the motor is not jammed or mechanically seized"
---

## Yaskawa A1000 VFD E14 Fault — What It Means

The E14 fault code on a Yaskawa A1000 variable frequency drive typically indicates a ground fault or output short circuit condition. The drive has detected that current is leaking to ground or that one or more output phases are shorted together or to ground. This is a protective shutdown that prevents damage to the drive, motor, and connected equipment.

The fault can be triggered by deteriorated motor insulation, damaged output cables, moisture intrusion in the motor or junction boxes, or improper wiring at the motor terminals. Because VFDs use high-frequency switching, even marginal insulation problems that would not trip a line-voltage motor can trigger this fault. The drive will not restart until the fault is cleared and the condition corrected.

## Before You Replace Anything

Technicians sometimes replace the VFD itself when the real problem is a motor or cable fault. Always perform an insulation resistance test (megger test) on the motor and output cables before condemning the drive.

[Jump to Fix](#fix)

## Common Causes

- **Degraded motor winding insulation (~40%)** Over time, heat, moisture, and mechanical stress break down the varnish and insulation on motor windings, allowing current to leak to the motor frame.
- **Damaged output cable insulation (~25%)** VFD-rated cables can be damaged by sharp edges, excessive bending, pinch points, or wear through cable tray, especially in conduit runs or at terminations.
- **Moisture in motor or junction box (~15%)** Water infiltration from leaks, condensation, or wash-down environments creates a conductive path from live conductors to ground.
- **Loose or improperly terminated motor connections (~10%)** A loose wire at the motor terminal block can arc and create a ground fault path or intermittent short circuit.
- **Internal VFD output stage failure (~7%)** A failed IGBT or output module inside the drive can trigger a ground fault detection, though this is less common than external problems.
- **Incorrect grounding or ground loop (~3%)** Improper grounding practices, multiple ground points, or a ground loop can cause nuisance ground fault trips.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault occur immediately when you enable the drive, before the motor starts turning?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is likely in the output wiring or motor terminals rather than a running condition. Inspect all connections and perform an insulation test on the motor.<br><strong>No:</strong> The fault may be load-related or thermal. Check for mechanical binding, moisture ingress during operation, or intermittent cable damage that only shows under vibration.</div>
</details>

<details class="dtree"><summary>Can you measure continuity between any motor lead and the motor frame with power off?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor has a direct short to ground. Disconnect the motor from the VFD and verify the short is in the motor or cable, not the drive output.<br><strong>No:</strong> The fault is likely high-resistance or intermittent. Perform a megohm insulation test on the motor and cables at rated voltage.</div>
</details>

<details class="dtree"><summary>Is there visible moisture, corrosion, or contamination in the motor terminal box or cable run?</summary>
<div class="dtree-body"><strong>Yes:</strong> Clean and dry all connections, seal any entry points, and apply dielectric grease to terminals. Retest insulation before reconnecting to the drive.<br><strong>No:</strong> The problem is likely internal to the motor windings or a hidden cable fault. A professional insulation test and motor inspection are needed.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Lock out and tag out** all power to the VFD and motor circuit, following your facility electrical safety procedures.
2. **Disconnect the motor leads** from the VFD output terminals (U, V, W or T1, T2, T3) to isolate the motor and cable from the drive.
3. **Perform a megohm insulation test** on the motor with a 500V or 1000V megger from each motor lead to the motor frame and between phases; readings should typically be above 1 megohm (consult your motor nameplate and VFD manual for acceptance thresholds).
4. **Inspect all output cable** runs for physical damage, sharp bends, pinch points, moisture intrusion, and proper support; look for signs of arcing or overheating at terminations.
5. **Check motor terminal connections** for tightness, corrosion, and proper torque; remove any moisture or contamination and apply dielectric grease if appropriate for the environment.
6. **Test the VFD output stage** by measuring resistance from each output terminal (U, V, W) to ground with the motor disconnected; you should see high resistance (megohms); if you see low resistance, the drive itself may have a fault.
7. **Reconnect the motor** only after all insulation tests pass and all faults are corrected, then clear the fault from the VFD display and attempt a test run under no-load or light-load conditions.

## Parts Often Needed

| Part | Notes |
|------|-------|
| VFD-rated shielded motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-e14-fault-code&k=VFD-rated+shielded+motor+cable&tag=errorcodefixes-20) \| Use cable rated for variable frequency drive service with appropriate voltage and bend radius for your installation |
| Motor terminal kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-e14-fault-code&k=Motor+terminal+kit&tag=errorcodefixes-20) \| Includes lugs, heat-shrink, and dielectric grease for proper motor terminations |

## When to Call a Pro

Call a qualified electrician or motor technician if you are not trained in high-voltage electrical work or do not have access to a megohm insulation tester. Ground fault diagnosis requires specialized test equipment and an understanding of VFD output characteristics. If insulation tests show marginal readings, a professional can assess whether the motor can be dried out and restored or needs rewinding or replacement. Any work inside the VFD cabinet or on the output power section requires knowledge of DC bus capacitor hazards and proper discharge procedures. If the motor or VFD is part of a critical process or safety system, always use a certified technician to diagnose and repair the fault.

**Rough cost:** A pro service call runs about $200-800 depending on whether the issue is a cable repair, motor rewinding, or motor replacement.
