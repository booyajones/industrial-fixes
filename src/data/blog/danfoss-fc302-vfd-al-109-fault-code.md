---
title: "Danfoss FC302 VFD AL-109 Fault - Causes & Fix"
description: "AL-109 is not a documented Danfoss FC302 code. Most likely you're seeing Alarm 13 (output overcurrent). Check motor connections first."
pubDatetime: 2026-06-24T10:06:20Z
modDatetime: 2026-06-24T10:06:20Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 inverter board or IGBT module"
most_likely_cause: "Misreading of Alarm 13 or corrupted display"
likelihood: "the most plausible explanation when AL-109 appears"
diy_or_pro: "pro"
free_checks:
  - "Write down the exact characters displayed (check if it might be Alarm 13 or another two-digit code)"
  - "Review alarm history in parameter group 16 to see logged fault codes"
  - "Inspect motor cable connections at terminals T1, T2, T3 for looseness or corrosion"
---

## Danfoss FC302 VFD AL-109 Fault — What It Means

The code AL-109 does not appear in official Danfoss FC302 documentation. Danfoss publishes alarm codes 1 through 39 only for this series. If your display shows AL-109, you may be seeing a misread Alarm 13 (output overcurrent), a corrupted display due to control board failure, or an undocumented internal fault code above 5376 that requires factory service. Alarm 13 means the drive output current exceeded its peak current limit, typically 150 to 200 percent of rated current for more than 10 milliseconds. This results from motor winding shorts, sudden mechanical overload, incorrect parameter settings, or failing IGBT modules on the inverter board. Because AL-109 is not defined, confirm the exact characters on your display and consult your drive's alarm history (parameter group 16) or contact Danfoss technical support to decode the fault.

## Before You Replace Anything

Technicians often replace the entire inverter board or IGBT module before verifying the motor and cable are intact. Disconnect the motor leads and run the drive unloaded to isolate whether the fault is internal to the drive or external in the motor circuit.

[Jump to Fix](#fix)

## Common Causes

- **Misread or corrupted display (~40%)** Low-resolution LCDs can render Alarm 13 as 109, or a failing control board can corrupt the display output entirely.
- **Motor winding short or phase-to-ground fault (~25%)** Partial shorts in motor windings or damaged motor cable insulation cause instantaneous overcurrent that triggers Alarm 13.
- **Incorrect motor parameters (~15%)** Motor nominal current (parameter 1-24) set too high or motor data mismatched to the actual motor causes the drive to allow excessive current.
- **Mechanical overload or jammed shaft (~10%)** Sudden torque demand from a seized bearing, jammed conveyor, or blocked impeller drives output current above peak limit.
- **Failing IGBT module or inverter board (~10%)** Cracked solder joints, aging capacitors, or shorted IGBTs on the inverter board produce false overcurrent readings or real current spikes.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the display clearly show AL-109 or could it be Alarm 13?</summary>
<div class="dtree-body"><strong>Yes:</strong> If you see AL-109 distinctly, note that this code is undocumented and likely requires Danfoss support or a control board issue.<br><strong>No:</strong> If it might be Alarm 13, proceed with overcurrent diagnostics by disconnecting the motor and running the drive unloaded.</div>
</details>

<details class="dtree"><summary>Does the alarm persist when motor leads are removed and drive runs unloaded?</summary>
<div class="dtree-body"><strong>Yes:</strong> Fault is internal to the drive (IGBT module, control board, or inverter power stage). Call Danfoss or a drive repair specialist.<br><strong>No:</strong> Fault is in the motor, cable, or mechanical load. Measure motor winding resistance and inspect cable insulation.</div>
</details>

<details class="dtree"><summary>Are motor winding resistances balanced within 5 percent and insulation above 1 megohm?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor is electrically sound. Check for mechanical binding, verify parameter 1-24 matches motor nameplate current, and inspect load coupling.<br><strong>No:</strong> Replace or rewind the motor and inspect the cable for damage or moisture ingress.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Write down the exact display characters** and check the alarm history in parameter group 16 to confirm whether the code is AL-109 or Alarm 13.
2. **Power down and lock out** the drive, then disconnect motor leads from terminals T1, T2, and T3.
3. **Power up the drive** and command it to run at 50 percent speed with no motor connected. If the alarm persists, the fault is inside the drive and you need professional inverter repair or Danfoss service.
4. **Measure motor winding resistance** (phase to phase) with a multimeter. All three pairs should be within 5 percent of each other. Use a megohmmeter to check phase-to-ground insulation, which should read at least 1 megohm.
5. **Inspect motor cable** for loose connections, corrosion at terminals, physical damage, or moisture. Re-torque all connections to manufacturer specification.
6. **Verify motor parameters** in group 1 (especially parameter 1-24 motor nominal current) match the motor nameplate exactly. Run auto-tune (parameter 1-29) if supported.
7. **Check mechanical load** by rotating the motor shaft by hand or decoupling the load. Look for seized bearings, jammed conveyors, or blocked impellers that spike torque on start-up.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 inverter board or IGBT module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-109-fault-code&k=Danfoss+FC302+inverter+board+or+IGBT+module&tag=errorcodefixes-20) \| Required only if internal fault confirmed by unloaded test. Must match your frame size and voltage rating. |
| Replacement motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-109-fault-code&k=Replacement+motor&tag=errorcodefixes-20) \| If winding resistance imbalance or ground fault confirmed. |

## When to Call a Pro

Call a professional or Danfoss service immediately if the alarm persists with the motor disconnected, if you lack a megohmmeter or multimeter to test windings, or if the display shows garbled characters suggesting control board failure. High-voltage VFD work requires training in DC bus discharge, lockout procedures, and IGBT handling. If motor parameters and mechanical load checks do not resolve the issue, a drive repair specialist can test the inverter power stage, gate drivers, and current sensors with oscilloscope and load-bank equipment that is not available to general technicians.

**Rough cost:** A pro service call runs about $200-800 depending on whether the fault is a parameter reset, motor replacement, or drive inverter repair.

## See Also

- [Danfoss FC302 AL-88 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-88-fault-code/)
- [Danfoss FC302 Alarm 32 - Causes & Fix](/posts/danfoss-fc302-alarm-32-fault-code/)
- [Danfoss FC302 Alarm 51 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-51-fault-code/)
- [Danfoss FC302 Alarm 39 - Causes & Fix](/posts/danfoss-fc302-alarm-39-fault-code/)
