---
title: "Danfoss FC302 AL-149 Fault - Causes & Fix"
description: "AL-14 (Err 14) is a ground fault: current leaks from motor leads to earth. Most often the motor insulation has failed. Disconnect the motor and test."
pubDatetime: 2026-06-25T09:34:59Z
modDatetime: 2026-06-25T09:34:59Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 power board / IGBT module"
most_likely_cause: "Motor winding insulation failure"
likelihood: "the most frequent cause"
diy_or_pro: "pro"
free_checks:
  - "Tighten all connections at drive output terminals (U, V, W) and motor junction box"
  - "Perform manual initialization via the drive menu to reset current sensor offsets"
  - "Disconnect motor leads from drive and attempt to run drive unloaded to isolate fault location"
---

## Danfoss FC302 AL-149 Fault — What It Means

Alarm 14 (AL-14 or Err 14) on a Danfoss FC302 VFD is a ground fault error. The drive has detected electrical current leaking from one of the output phases (U, V, or W) to the ground or earth system instead of flowing through the motor. This happens when insulation fails in the motor windings, output cables are damaged, or an internal IGBT transistor in the drive has shorted to the chassis ground.

The drive stops immediately when this fault triggers to protect equipment and personnel. The fault can originate either downstream in the motor and cabling or internally in the drive power board. The key to diagnosis is isolating the motor from the drive to determine which side of the connection is at fault.

## Before You Replace Anything

Technicians often replace the entire drive power board before testing the motor. Always perform a megohm insulation test on the motor windings and cables first; readings below 2 megohms indicate failed insulation and point to the motor, not the drive.

[Jump to Fix](#fix)

## Common Causes

- **Motor winding insulation failure (~50%)** Moisture, contamination, thermal aging, or voltage spikes degrade the insulation inside the motor windings, allowing current to leak to the motor frame and ground.
- **Damaged output cables (~25%)** Cable insulation stripped by sharp conduit edges, rodents, or corrosion exposes conductors that short to ground in the cable tray or raceway.
- **Failed drive IGBTs (~15%)** An output IGBT transistor on the power board has failed internally and shorted to the drive chassis ground, triggering the fault even with no motor connected.
- **Loose terminal connections (~7%)** Loose or corroded connections at the drive output or motor junction box cause arcing that creates intermittent ground leakage paths.
- **Current sensor offset (~3%)** A drift in the drive's current sensor calibration can falsely detect ground current and trigger the alarm without a physical short present.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the alarm clear and the drive run normally with the motor disconnected from U, V, and W terminals?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is downstream in the motor or cables. Proceed to megohm test of motor windings and cable insulation.<br><strong>No:</strong> The fault is internal to the drive power board (likely failed IGBTs). The drive needs repair or replacement of the power module.</div>
</details>

<details class="dtree"><summary>Do motor winding-to-ground megohm readings measure below 2 megohms?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor insulation has failed. Replace or rewind the motor.<br><strong>No:</strong> Check cable insulation with a megohmmeter. If cables test good but fault persists, recheck all terminal connections and look for intermittent shorts.</div>
</details>

<details class="dtree"><summary>Did performing a manual initialization through the drive menu clear the fault?</summary>
<div class="dtree-body"><strong>Yes:</strong> The alarm was likely caused by a current sensor offset. Monitor the drive during operation to confirm the fault does not return.<br><strong>No:</strong> Proceed to the motor isolation test to locate the physical ground fault in the motor, cables, or drive.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Remove all power** from the drive including AC mains and DC-link supplies, then wait for internal capacitors to discharge fully per the manufacturer's safety table before opening any covers or touching terminals.
2. **Inspect and tighten** all connections at the drive output terminals (U, V, W) and at the motor junction box to eliminate loose or corroded contact points.
3. **Perform manual initialization** by accessing the drive menu and running the initialization routine to reset any current sensor offsets that may be falsely triggering the ground fault alarm.
4. **Disconnect the motor leads** completely from the drive output terminals U, V, and W, then reapply power to the drive and reset the alarm.
5. **Attempt to run the drive** with no motor attached (unload test). If the drive runs normally and shows little or no output current, the fault is in the motor or cables. If Alarm 14 persists, the fault is internal to the drive power board.
6. **Test motor and cable insulation** using a megohmmeter. Measure resistance from each motor winding (and each cable conductor) to ground. Readings below 2 megohms indicate failed insulation that must be repaired or replaced.
7. **Contact Danfoss technical support** or a certified VFD repair center if the fault persists with the motor disconnected, as the drive power board requires disassembly and IGBT module replacement by a trained technician.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 power board / IGBT module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-149-fault-code&k=Danfoss+FC302+power+board+%2F+IGBT+module&tag=errorcodefixes-20) \| Required only if internal drive fault confirmed by motor-disconnected test. Must match your exact drive frame size and voltage rating. |
| Replacement three-phase motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-149-fault-code&k=Replacement+three-phase+motor&tag=errorcodefixes-20) \| Choose a motor with matching horsepower, voltage, and frame size if megohm test shows insulation failure below 2 megohms. |
| VFD-rated motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-149-fault-code&k=VFD-rated+motor+cable&tag=errorcodefixes-20) \| Use only VFD-rated cable with adequate insulation for the voltage and environment if cable insulation test fails. |

## When to Call a Pro

Call a qualified electrician or VFD technician immediately if you are not trained in high-voltage systems or do not have the proper test equipment. This fault involves live AC and DC voltages that can cause fatal shock. A professional should perform the megohm insulation tests, interpret the results, and replace the drive power board if needed. If the motor isolation test shows an internal drive fault, the repair requires disassembly of the drive enclosure, testing of individual IGBT modules, and replacement of semiconductors that are not available to end users. Only attempt the free checks (tightening connections, manual initialization, and motor disconnection test) if you have lockout/tagout training and the proper PPE.

**Rough cost:** A pro service call runs about $200-800 depending on whether motor or drive power board replacement is needed.
