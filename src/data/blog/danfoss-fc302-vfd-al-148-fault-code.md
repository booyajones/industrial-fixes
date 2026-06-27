---
title: "Danfoss FC302 AL-148 Fault - Causes & Fix"
description: "AL-148 is not a documented Danfoss FC302 code. You likely mean Alarm 14 (earth fault). Check motor winding insulation and cable first."
pubDatetime: 2026-06-25T09:34:06Z
modDatetime: 2026-06-25T09:34:06Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Motor cable (VFD-rated shielded cable)"
most_likely_cause: "Motor winding insulation failure"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power down the drive, wait for capacitor discharge, then check and tighten all U/V/W output terminal connections and motor junction box connections"
  - "Disconnect motor leads from the drive, power back on, and attempt to reset the alarm; if it clears, the fault is external to the drive"
---

## Danfoss FC302 AL-148 Fault — What It Means

No official Danfoss FC302 documentation lists an 'AL-148' fault code. The closest valid alarm matching this pattern is Alarm 14, which indicates an earth fault (ground fault) on the drive output. Alarm 14 means the FC302 has detected current leaking from one or more output phases (U, V, or W) to ground instead of returning through the motor windings, exceeding the internal trip threshold. This is a protective fault that shuts down the drive to prevent motor damage or electrical shock risk.

If you are reading 'AL-148' from a display, verify the actual number carefully. Alarm 14 is the most common earth-fault code on the FC302 and typically points to motor insulation breakdown, damaged motor cable, or loose output connections. If your display truly shows a different number, consult your drive's manual or contact Danfoss technical support to confirm the exact fault definition for your firmware version.

## Before You Replace Anything

Many technicians replace the drive power board first, assuming an internal sensor fault. Always disconnect the motor leads and test for alarm persistence with no load attached. If the alarm clears, the fault is in the motor or cable, not the drive.

[Jump to Fix](#fix)

## Common Causes

- **Motor winding insulation failure (~40%)** Moisture, contamination, or thermal aging degrades motor winding insulation; megohm test readings below 2 MΩ to ground confirm breakdown and require motor repair or replacement.
- **Damaged motor cable (~30%)** Cracked insulation, water ingress, or physical damage in the cable between drive and motor creates a path to ground and triggers the earth-fault alarm.
- **Loose drive output terminals (~15%)** Poor connections at U, V, or W terminals create resistance and current spikes that the drive interprets as a ground fault.
- **Drive internal current sensor fault (~10%)** Degraded or failed current sensors on the power board misreport ground current and trigger a false earth-fault alarm.
- **Incorrect motor nominal current parameter (~5%)** Setting motor nominal current too high in the drive parameters causes the earth-fault detection threshold to trip prematurely under normal load.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the alarm clear when you disconnect the motor leads from the drive and power back on?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is in the motor or motor cable. Perform a megohm test from motor windings to ground and inspect the cable for damage.<br><strong>No:</strong> The fault is inside the drive. Attempt a manual initialization (hold keys for 5 seconds) to clear sensor offset errors, or contact service for power-board diagnosis.</div>
</details>

<details class="dtree"><summary>Does the motor megohm test show insulation resistance below 2 MΩ to ground?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor winding insulation has failed. The motor needs rewinding or replacement.<br><strong>No:</strong> Inspect the motor cable for cracks, water, or loose connections; replace the cable if damaged.</div>
</details>

<details class="dtree"><summary>Are the U/V/W terminal connections tight and free of corrosion?</summary>
<div class="dtree-body"><strong>Yes:</strong> Check the drive parameter for motor nominal current; verify it matches the motor nameplate rating.<br><strong>No:</strong> Clean and tighten all output connections, then reset the alarm and test.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Remove all power** from the drive at the main disconnect and wait for the DC bus capacitors to discharge fully (consult your model's table for the safe wait time).
2. **Inspect and tighten** all U, V, and W output terminal connections at the drive and the motor junction box; look for corrosion or arcing marks.
3. **Disconnect the motor leads** from the drive output terminals and secure them away from ground.
4. **Power the drive back on** with no motor attached and attempt to reset the alarm from the control panel.
5. **If the alarm clears**, the fault is external; perform a megohm (insulation resistance) test from each motor winding to ground and check the motor cable for cracks or moisture.
6. **If the alarm persists** with no motor connected, the drive has an internal fault; perform a manual initialization by holding the reset keys for 5 seconds to clear sensor offsets.
7. **If initialization does not clear the alarm**, the current sensor on the power board has failed and requires drive disassembly or factory service for repair.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable (VFD-rated shielded cable) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-148-fault-code&k=Motor+cable+%28VFD-rated+shielded+cable%29&tag=errorcodefixes-20) \| Use VFD-rated cable with proper shielding; length and gauge must match the drive output current rating |
| Drive power board (current sensor assembly) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-148-fault-code&k=Drive+power+board+%28current+sensor+assembly%29&tag=errorcodefixes-20) \| Only replace if the alarm persists with no motor connected and manual initialization fails; contact Danfoss service for part number and assembly |

## When to Call a Pro

Call a qualified technician or Danfoss-certified service provider if you are not trained in high-voltage VFD work, if the drive continues to alarm with no motor connected, or if the megohm test confirms motor insulation failure requiring rewinding. Professional diagnosis is required to safely open the drive enclosure, test internal current sensors, or replace the power board. Working inside a VFD without proper discharge procedures and PPE can result in lethal shock even after power is removed. If the motor needs rewinding or replacement, an industrial motor shop should perform the work to match the original specifications and maintain UL or CE compliance.

**Rough cost:** A pro service call runs about $200-500 for motor megohm testing, cable replacement, or drive repair.
