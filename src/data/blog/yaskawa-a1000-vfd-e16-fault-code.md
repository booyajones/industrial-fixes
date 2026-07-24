---
title: "Yaskawa A1000 VFD E16 Fault - Causes & Fix"
description: "E16 signals a ground fault or insulation breakdown. Check motor winding insulation and cable shielding first."
pubDatetime: 2026-07-22T07:42:47Z
modDatetime: 2026-07-22T07:42:47Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "VFD-rated shielded motor cable"
most_likely_cause: "Degraded motor winding insulation or damaged power cable"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Disconnect the motor cable from the drive output terminals and inspect for moisture, burn marks, or pinched conductors"
  - "Check motor terminal box for moisture, corrosion, or loose connections that could create a ground path"
---

## Yaskawa A1000 VFD E16 Fault — What It Means

The E16 fault code on a Yaskawa A1000 variable frequency drive indicates a ground fault has been detected. The drive's internal monitoring has sensed current leaking to ground, typically through damaged motor windings, degraded cable insulation, or compromised shielding. This protection feature shuts down the drive to prevent equipment damage and electrical hazards.

The fault can appear during startup, under load, or intermittently depending on the severity and location of the ground path. High humidity, moisture ingress, mechanical wear, or thermal cycling can all accelerate insulation breakdown. Addressing the fault requires isolating whether the problem lies in the motor itself, the power cable between drive and motor, or occasionally in the drive's output stage.

## Before You Replace Anything

Technicians sometimes replace the VFD output section or entire drive before testing motor and cable insulation with a megohmmeter. A simple insulation resistance test at 500V or 1000V will identify whether the motor windings or cable are grounded.

[Jump to Fix](#fix)

## Common Causes

- **Motor winding insulation failure (~45%)** Moisture, thermal stress, or mechanical vibration breaks down the insulation between windings and the motor frame, creating a direct path to ground.
- **Damaged or pinched motor cable (~30%)** Cable insulation can be cut, crushed, or abraded by conduit edges, tight bends, or mechanical contact, exposing conductors to ground.
- **Moisture in motor or cable (~15%)** Water ingress through damaged seals, condensation, or flooding creates conductive paths between live conductors and grounded metal enclosures.
- **Faulty cable shielding or grounding (~5%)** Improperly terminated cable shield or poor grounding practice can cause stray currents to be misinterpreted as ground faults.
- **Drive output stage component failure (~5%)** Internal drive components such as IGBTs or capacitors can develop internal short circuits to chassis ground, though this is less common.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault appear immediately when you power up the drive with the motor cable disconnected?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem is internal to the VFD; call a qualified technician or the manufacturer for drive diagnostics and possible board replacement.<br><strong>No:</strong> The fault is external; proceed to test the motor cable and motor windings for insulation resistance.</div>
</details>

<details class="dtree"><summary>Can you see visible damage, moisture, or corrosion at the motor terminal box or along the cable route?</summary>
<div class="dtree-body"><strong>Yes:</strong> Dry out the motor, repair or replace damaged cable sections, and retest insulation resistance before reconnecting the drive.<br><strong>No:</strong> Use a megohmmeter to measure insulation resistance from each motor phase to ground; readings below the motor manufacturer's specification indicate winding failure.</div>
</details>

<details class="dtree"><summary>Does the insulation resistance test show all three motor phases above the manufacturer's minimum specification?</summary>
<div class="dtree-body"><strong>Yes:</strong> Check cable shield grounding and VFD parameter settings for ground fault trip threshold; consult the A1000 manual to verify settings match your installation.<br><strong>No:</strong> The motor windings have failed insulation; the motor requires rewinding or replacement.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down and lock out** the VFD and all upstream disconnects following your facility's electrical safety procedures.
2. **Record the fault code** and any active parameters from the drive display or keypad before clearing the fault.
3. **Disconnect the motor cable** at the drive output terminals (U, V, W) and verify all three phases are isolated from the drive.
4. **Inspect the motor cable** for visible damage, sharp bends, moisture, or pinch points along the entire run from drive to motor.
5. **Measure insulation resistance** using a megohmmeter rated for at least 500V DC; test each motor phase (U, V, W) to the motor frame and to ground, and compare readings to the motor nameplate or manufacturer specifications.
6. **Dry out the motor** if moisture is present by running it in a warm, dry environment or using heat lamps; retest insulation resistance after drying.
7. **Replace or repair** any damaged cable sections, ensuring proper routing, strain relief, and shield grounding per the A1000 installation manual and NEC requirements.
8. **Reconnect the motor cable** to the drive output terminals, verify all ground connections are tight, and restore power to the drive.
9. **Clear the fault code** using the drive keypad and monitor the drive during a no-load test run; if the fault returns, consult the manufacturer or a qualified VFD technician.

## Parts Often Needed

| Part | Notes |
|------|-------|
| VFD-rated shielded motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-e16-fault-code&k=VFD-rated+shielded+motor+cable&tag=errorcodefixes-20) \| Match cable size to motor current and cable length per the A1000 manual; use symmetrical shielding and proper grounding hardware. |
| Motor terminal box gasket and seal kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-e16-fault-code&k=Motor+terminal+box+gasket+and+seal+kit&tag=errorcodefixes-20) \| Replace damaged seals to prevent moisture ingress into the motor enclosure. |

## When to Call a Pro

Call a qualified electrician or motor technician if you are not trained in high-voltage electrical work, if insulation testing reveals motor winding failure requiring rewind or replacement, or if the fault persists after verifying motor and cable integrity. VFD troubleshooting involves live high-voltage DC bus capacitors that remain charged even after input power is removed. Ground fault diagnosis also requires specialized test equipment and knowledge of NEC grounding practices. If the drive itself is suspected, contact Yaskawa technical support or an authorized service center for internal diagnostics and repair.

**Rough cost:** A pro service call runs about $200-800.
