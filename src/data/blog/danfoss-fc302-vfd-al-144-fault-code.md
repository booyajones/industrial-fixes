---
title: "Danfoss FC302 Alarm 14 - Causes & Fix"
description: "Alarm 14 means the drive detected current leakage to ground. Most common: deteriorated motor winding insulation from moisture or age."
pubDatetime: 2026-06-25T09:30:48Z
modDatetime: 2026-06-25T09:30:48Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "AC motor (replacement)"
most_likely_cause: "Motor winding insulation deterioration"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect and tighten all output terminals at drive U/V/W connections and motor junction box for loose or corroded connections"
  - "Disconnect motor leads from drive outputs, power on, and reset alarm to isolate whether fault is in motor/cable or internal drive"
---

## Danfoss FC302 Alarm 14 — What It Means

Alarm 14 activates when the Danfoss FC302 drive senses current leakage to ground on the output circuit. This indicates insulation breakdown somewhere in the motor circuit, which could be motor windings, cable insulation, or internal drive components. The fault protects personnel from electric shock and prevents further equipment damage by shutting down the drive when it detects a ground path that should not exist.

The drive monitors output current and trips when insulation resistance falls below safe levels, typically below 2 megohms. This is a safety-critical fault that requires immediate diagnosis to locate the failed insulation before returning the system to service.

## Before You Replace Anything

Many technicians replace the entire drive assuming internal failure without first isolating the motor and cable. Disconnect the motor leads and power the drive on; if Alarm 14 clears with the motor disconnected, the drive is healthy and the fault lies in the motor or cable.

[Jump to Fix](#fix)

## Common Causes

- **Motor winding insulation deterioration (~50%)** Moisture infiltration, contamination, or thermal aging reduces insulation resistance below 2 megohms between windings and ground.
- **Damaged motor cable insulation (~25%)** Cables run through conduit with sharp edges, rodent damage, or mechanical stress cause insulation breakdown and ground paths.
- **Loose or corroded output connections (~15%)** Loose terminals at drive output or motor junction box create intermittent ground paths that trigger the alarm.
- **Internal drive component failure (~8%)** Failed output IGBTs, gate driver circuits, or current sensors inside the drive cause false detection even with motor disconnected.
- **Incorrect motor parameter settings (~2%)** Motor nominal current parameter set too high for actual motor rating causes false ground fault detection.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>With motor disconnected and drive powered on, does Alarm 14 clear and current display read near zero?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive is healthy; fault is in motor or cable. Proceed to megger test motor windings and cable insulation.<br><strong>No:</strong> Internal drive failure is likely. Contact Danfoss technical support for service or replacement of output stage components.</div>
</details>

<details class="dtree"><summary>After tightening all output terminals and resetting, does the alarm clear and stay off during operation?</summary>
<div class="dtree-body"><strong>Yes:</strong> Loose connection was the cause; monitor for recurrence and verify all terminations are torqued properly.<br><strong>No:</strong> Insulation failure exists in motor or cable. Perform megger test to locate the breakdown point.</div>
</details>

<details class="dtree"><summary>Does a 1000V megger test on motor windings to ground show readings above 2 megohms?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor insulation is acceptable; test cable insulation separately or check for internal drive fault.<br><strong>No:</strong> Motor winding insulation has failed; motor requires replacement or rewinding.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Remove all power** and lock out the drive supply disconnect. Wait for DC bus capacitors to discharge before proceeding.
2. **Inspect output terminals** at drive U/V/W connections and motor junction box. Look for loose, corroded, or oxidized connections. Tighten any loose terminals to proper torque and clean corrosion.
3. **Disconnect motor leads** from drive output terminals. Label leads for reconnection later.
4. **Power drive back on** and reset Alarm 14. Attempt to run the drive with no motor attached. If current display shows near zero and alarm clears, the motor or cable is faulty. If alarm persists, internal drive failure is present.
5. **Perform megger test** on motor windings using a 1000V megohm tester. Test each winding (U, V, W) to ground. Readings below 2 megohms indicate insulation failure. Test cable insulation separately if motor passes.
6. **Replace failed components** based on test results. If motor fails megger test, replace motor or send for rewinding. If cable fails, replace damaged cable section. If drive has internal fault, contact Danfoss Drives technical support for repair or replacement.
7. **Verify parameter settings** after repairs. Confirm motor nominal current parameter matches actual motor nameplate rating. Incorrect settings can cause false detection.
8. **Reconnect motor** and restore power. Reset alarm and run drive under load. Monitor for alarm recurrence and verify normal operation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| AC motor (replacement) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-144-fault-code&k=AC+motor+%28replacement%29&tag=errorcodefixes-20) \| Required if megger test shows motor winding insulation below 2 megohms; match nameplate HP, voltage, and frame size. |
| Motor power cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-144-fault-code&k=Motor+power+cable&tag=errorcodefixes-20) \| Shielded VFD-rated cable when existing cable fails insulation test or shows physical damage. |
| Danfoss FC302 output stage assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-144-fault-code&k=Danfoss+FC302+output+stage+assembly&tag=errorcodefixes-20) \| Required if Alarm 14 persists with motor disconnected; contact Danfoss for part number and service. |

## When to Call a Pro

Call a qualified electrician or VFD technician if you are not trained to work with high-voltage industrial equipment or do not have a 1000V megger tester. Internal drive repairs require knowledge of power electronics, access to Danfoss parts, and proper safety procedures. If the fault persists with the motor disconnected, the drive needs professional diagnosis and repair. Ground fault conditions present shock hazards, so only personnel trained in industrial electrical safety should troubleshoot this alarm. Professionals have the test equipment to isolate faults quickly and can coordinate motor rewinding or drive warranty service.

**Rough cost:** A pro service call runs about $200-800 depending on whether motor cable, motor replacement, or drive repair is required.

## See Also

- [Danfoss FC302 AL-143 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-143-fault-code/)
- [Danfoss FC302 VFD Alarm 23 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-23-fault-code/)
- [Danfoss FC302 ALARM 35 - Causes & Fix](/posts/danfoss-fc302-alarm-35-fault-code/)
- [Danfoss FC302 Alarm 34 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-34-fault-code/)
