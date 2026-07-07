---
title: "Danfoss FC302 AL-160 Fault - Causes & Fix"
description: "AL-16 indicates a phase-to-phase short circuit on the drive output. Most often caused by failed IGBT modules inside the power board."
pubDatetime: 2026-06-26T09:52:07Z
modDatetime: 2026-06-26T09:52:07Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 power board (rectifier and inverter assembly)"
most_likely_cause: "Failed IGBT module in the power board"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Disconnect motor from U/V/W terminals and measure resistance between output phases with an ohmmeter"
  - "Inspect motor cable and terminal box for visible damage, moisture, or pinched conductors"
part_price: "$600-1800"
---

## Danfoss FC302 AL-160 Fault — What It Means

The AL-16 fault (also called Err-16) means the drive detected an instantaneous short circuit between output phases (U, V, or W). The drive trips within microseconds to protect itself from catastrophic overcurrent. This is the most severe fault condition on the FC302, distinct from overload or earth faults. The short circuit creates a direct path across the DC bus, usually through broken-down semiconductor junctions inside the drive. The fault can also be triggered by a shorted motor, damaged cable, or wet terminal box, but in the vast majority of cases the drive's internal power electronics have failed.

## Before You Replace Anything

Technicians sometimes replace the motor or cable first. Always disconnect the motor and test for a short with the drive isolated. If the short persists with the motor disconnected, the fault is inside the drive power board.

[Jump to Fix](#fix)

## Common Causes

- **Failed IGBT module (~70%)** Semiconductor junctions in the inverter section break down and create a direct short across the DC bus, triggering instant shutdown.
- **Shorted motor windings (~15%)** Phase-to-phase insulation failure inside the motor creates a hard short that the drive detects immediately.
- **Damaged motor cable (~10%)** Crushed, cut, or moisture-damaged cable causes conductors to touch and short between phases.
- **Wet or contaminated terminal box (~3%)** Water, metal debris, or conductive dust inside the motor terminal box bridges output phases.
- **Shorted DC link capacitor (~2%)** A failed capacitor in the DC bus section can create a short path, though this usually triggers other faults first.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>With the motor disconnected, does an ohmmeter show a short (low resistance) between any two output terminals U, V, or W?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is inside the drive. The power board (IGBT module or capacitors) has failed and must be replaced by a qualified technician.<br><strong>No:</strong> The fault is external. Test the motor and cable for shorts or insulation breakdown before reconnecting.</div>
</details>

<details class="dtree"><summary>Does the motor show low insulation resistance (below 1 megohm to ground) when tested with a megohmmeter?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor windings are breaking down or shorted. The motor needs professional repair or replacement.<br><strong>No:</strong> Inspect the motor cable for damage and verify all connections are clean and dry before attempting another run.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Remove all input power** from the drive and wait at least five minutes for DC bus capacitors to discharge completely.
2. **Disconnect the motor** from the drive output terminals U, V, and W to isolate external faults from internal drive faults.
3. **Measure resistance** between U-to-V, V-to-W, and W-to-U on the drive output terminals using an ohmmeter. High resistance (above 100 kilohms) is normal. Low resistance indicates an internal short.
4. **Test the motor** if the drive showed no short. Use a megohmmeter to measure insulation resistance from each winding to ground (should be at least 1 megohm). Inspect the cable for cuts, pinches, or wet insulation.
5. **Inspect the power board** if the drive showed a short. Open the enclosure and look for burned IGBTs, cracked capacitors, or blown input fuses. Do not attempt to repair individual components.
6. **Replace the power board** with a new or refurbished unit from Danfoss or an authorized supplier. Install following manufacturer torque specs and thermal paste procedures.
7. **Reconnect the motor** and apply power. Test run at low speed and verify normal operation before returning to full load.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 power board (rectifier and inverter assembly) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-160-fault-code&k=Danfoss+FC302+power+board+%28rectifier+and+inverter+assembly%29&tag=errorcodefixes-20) \| Match the exact frame size and voltage rating to your drive model. Available from Danfoss dealers or industrial electronics suppliers. |
| Motor cable (shielded VFD-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-160-fault-code&k=Motor+cable+%28shielded+VFD-rated%29&tag=errorcodefixes-20) \| If external testing shows cable damage. Use continuous-flex VFD cable, not standard building wire. |

## When to Call a Pro

Call a qualified industrial electrician or VFD technician for AL-16 faults. This code indicates a catastrophic short circuit that has likely destroyed sensitive power electronics inside the drive. Troubleshooting requires high-voltage DC measurements and the ability to safely handle charged capacitors. Power board replacement demands precise torque specs, thermal management, and firmware configuration. Do not attempt repeated resets, as each power-up with a shorted IGBT can cascade damage to other components. A technician will isolate whether the fault is internal or external, replace the power board if needed, and verify all protective functions before returning the drive to service.

**Rough cost:** A pro service call runs about $800-2500.

## See Also

- [Danfoss VFD Fault OCL — Causes & Fix](/posts/danfoss-vfd-fault-ocl/)
- [Danfoss VFD Fault W30 — Brake Resistor Overtemperature Fix](/posts/danfoss-vfd-fault-w30/)
- [Danfoss FC302 Alarm 26 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-26-fault-code/)
- [Danfoss FC302 ALARM 35 - Causes & Fix](/posts/danfoss-fc302-alarm-35-fault-code/)
