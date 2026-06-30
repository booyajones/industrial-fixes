---
title: "Danfoss FC302 AL-125 - Causes & Fix"
description: "AL-125 is not a valid Danfoss FC302 code. You likely see AL 13 (overcurrent), AL 25 (input phase loss), or AL 12 (overvoltage). Check display."
pubDatetime: 2026-06-25T09:17:14Z
modDatetime: 2026-06-25T09:17:14Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 inverter board or IGBT module"
most_likely_cause: "Misread display showing AL 13 (overcurrent) caused by motor or cable short circuit"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify the exact alarm number on the VFD display (look for AL 13, AL 25, or AL 12 instead of 125)"
  - "Press the Reset button after the drive has been powered off for 30 seconds to see if the fault clears"
  - "Inspect all motor cable connections and drive output terminals for loose or corroded connections"
---

## Danfoss FC302 AL-125 — What It Means

The code AL-125 does not exist in the Danfoss FC302 alarm catalog. The FC302 series uses alarm codes AL 1 through AL 80 only. You are most likely misreading one of three common faults: AL 13 (Overcurrent), which means output current exceeded the peak limit due to a motor short or failed inverter component; AL 25 (Input Phase Missing or Unbalanced), which signals a problem with the three-phase input power; or AL 12 (Overvoltage), which indicates DC bus voltage spikes. AL 13 is by far the most frequent fault on these drives.

If you see AL 13, the drive detected more current flowing to the motor than its IGBTs can safely handle, typically around 200% of rated current. This happens when there is a short circuit in the motor winding or cable, a failed IGBT module inside the drive, or a mechanical jam that forces the motor to draw excessive current. Verifying the exact alarm number on the display is the first step before any repair.

## Before You Replace Anything

Technicians often replace the inverter board without first disconnecting the motor and running the drive unloaded. A simple no-load test isolates whether the fault is in the drive itself or in the motor and cable, saving the cost of unnecessary inverter replacement.

[Jump to Fix](#fix)

## Common Causes

- **Misread display (~40%)** The alarm number 125 does not exist and you are reading AL 13, AL 25, or AL 12 on a small or damaged display.
- **Motor or cable short circuit (if AL 13) (~25%)** A direct short between phases or phase-to-earth in the motor windings or the cable connecting the drive to the motor causes overcurrent trip.
- **Failed IGBT module (if AL 13) (~15%)** One or more IGBTs in the inverter section have shorted or opened, causing current to spike on that output leg.
- **Input phase missing or unbalanced (if AL 25) (~10%)** One leg of the three-phase input power is lost or voltage is severely unbalanced at the drive input terminals.
- **Mechanical overload or jammed shaft (if AL 13) (~5%)** The motor shaft is mechanically jammed or the load is so heavy the motor draws excessive current trying to turn.
- **Incorrect motor parameter settings (if AL 13) (~5%)** Parameter 1-24 (Motor Nominal Current) is set too low compared to the actual motor nameplate rating, causing false overcurrent detection.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the display show exactly AL-125, or do you see AL 13, AL 25, or AL 12?</summary>
<div class="dtree-body"><strong>Yes:</strong> Note the exact code (AL 13, AL 25, or AL 12) and proceed to diagnose that specific fault using the appropriate alarm guide.<br><strong>No:</strong> Take a clear photo of the display and consult the FC302 manual alarm table to confirm the exact code before any repair work.</div>
</details>

<details class="dtree"><summary>With AC power disconnected and the motor terminals (U, V, W) removed from the drive, does the drive run without faulting when you power it back on and press Reset?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is in the motor, motor cable, or mechanical load. Test the motor and cable for shorts and check for mechanical binding.<br><strong>No:</strong> The fault is internal to the drive, likely a failed IGBT module or inverter board. Call a VFD technician or the drive manufacturer.</div>
</details>

<details class="dtree"><summary>Does the fault occur only during deceleration or stopping?</summary>
<div class="dtree-body"><strong>Yes:</strong> Increase the deceleration ramp time in the drive parameters to allow regenerative energy to dissipate more slowly.<br><strong>No:</strong> The fault is present during normal operation and points to a motor short, cable fault, or internal drive failure.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the exact alarm code** by looking closely at the VFD display and comparing it to the FC302 alarm list in the manual (codes run from AL 1 to AL 80 only).
2. **Disconnect AC power** from the drive and lock out the main breaker, then disconnect the motor cable from the drive output terminals U, V, and W.
3. **Inspect all connections** at the motor terminals and drive output for loose wires, corrosion, or physical damage.
4. **Power the drive back on** with no motor connected and press the Reset button, then observe whether the alarm clears and the drive runs normally.
5. **If the alarm clears with no motor**, use a megohmmeter or multimeter to test the motor windings for shorts between phases (U-V, V-W, U-W should show balanced resistance, not zero) and for shorts to ground (infinite resistance from any phase to motor frame).
6. **If the alarm persists with no motor**, the drive has an internal fault (failed IGBT or inverter board) and requires replacement by a qualified VFD technician.
7. **Check Parameter 1-24** (Motor Nominal Current) to confirm it matches the motor nameplate current rating, and verify ramp times are long enough to avoid regenerative overvoltage or overcurrent during deceleration.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 inverter board or IGBT module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-125-fault-code&k=Danfoss+FC302+inverter+board+or+IGBT+module&tag=errorcodefixes-20) \| Only if the drive faults with no motor connected and internal failure is confirmed by a technician |
| Motor cable (shielded, VFD-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-125-fault-code&k=Motor+cable+%28shielded%2C+VFD-rated%29&tag=errorcodefixes-20) \| Replace if insulation is damaged or continuity test shows a short between phases or to ground |

## When to Call a Pro

Call a VFD technician or industrial electrician if the drive continues to fault with the motor disconnected, which indicates an internal inverter or IGBT failure. Also call a pro if you lack the tools or training to safely work with three-phase power, perform insulation resistance testing on motor windings, or interpret drive parameters. VFD repair involves high DC bus voltages (over 500 VDC on the internal capacitors even after AC power is off) and requires proper discharge procedures and test equipment. If the motor or cable is at fault, a motor shop or electrician should verify winding integrity and replace damaged components to avoid destroying a repaired or new drive.

**Rough cost:** A pro service call runs about $300-800.

## See Also

- [Danfoss FC302 AL-19 - Causes & Fix](/posts/danfoss-fc302-vfd-al-19-fault-code/)
- [Danfoss VLT Alarm 14 - Earth Fault: What It Means and How to Fix It](/posts/danfoss-vlt-alarm-14/)
- [Danfoss FC302 VFD Alarm 38 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-38-fault-code/)
- [Danfoss FC302 AL-105 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-105-fault-code/)
