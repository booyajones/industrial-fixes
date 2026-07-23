---
title: "Yaskawa GA800 VFD AL-04 Fault - Causes & Fix"
description: "AL-04 indicates an overcurrent trip during acceleration. Most often caused by rapid acceleration settings or excessive load on the motor."
pubDatetime: 2026-07-21T07:28:54Z
modDatetime: 2026-07-21T07:28:54Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa GA800 series VFD replacement unit"
most_likely_cause: "Acceleration time set too short for the load"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Disconnect motor and check that it rotates freely by hand with no binding or mechanical resistance"
  - "Review acceleration time parameter settings and compare to application requirements"
  - "Inspect output wiring and motor terminations for loose connections or signs of shorting"
no_buy_pct: "65%"
---

## Yaskawa GA800 VFD AL-04 Fault — What It Means

The AL-04 fault on a Yaskawa GA800 variable frequency drive signals an overcurrent condition detected during the motor acceleration phase. The drive has measured current draw exceeding its programmed limits while ramping up to the target speed and has shut down to protect itself and the motor. This fault typically occurs when the motor is being asked to accelerate too quickly, when the connected load is too heavy for the motor rating, or when there is a problem in the motor or output wiring that increases current demand beyond normal operating levels.

## Before You Replace Anything

Technicians sometimes replace the drive itself when the real problem is improper parameter programming or a mechanical binding issue on the driven load. Always check acceleration time settings and verify the motor and load turn freely before condemning the VFD.

[Jump to Fix](#fix)

## Common Causes

- **Acceleration time too short (~40%)** When the drive tries to bring the motor up to speed faster than the load can physically handle, current spikes and trips the overcurrent protection.
- **Excessive or binding load (~25%)** A mechanical problem such as a seized bearing, jammed conveyor, or overloaded pump forces the motor to draw abnormally high current during startup.
- **Motor or cable short circuit (~15%)** Damaged insulation in the motor windings or output cable creates a low-resistance path that causes overcurrent during acceleration.
- **Incorrect motor parameters (~10%)** When the drive is programmed with motor nameplate data that does not match the actual connected motor, the drive may not correctly limit current.
- **Loose or corroded output connections (~7%)** Poor contact at the drive output terminals or motor junction box can create arcing and erratic current readings during ramp-up.
- **Drive internal current sensor fault (~3%)** A failed or miscalibrated current transducer inside the VFD can report false overcurrent even when actual motor current is normal.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the motor turn freely by hand with the drive disconnected and no unusual noise or drag?</summary>
<div class="dtree-body"><strong>Yes:</strong> The mechanical load is likely not the issue. Focus on drive parameter settings and electrical checks.<br><strong>No:</strong> Investigate the mechanical system for seized bearings, jammed material, or misalignment before re-energizing the drive.</div>
</details>

<details class="dtree"><summary>Is the programmed acceleration time less than a few seconds for a large or high-inertia load?</summary>
<div class="dtree-body"><strong>Yes:</strong> Increase the acceleration time parameter incrementally and test. Many applications need five to fifteen seconds for heavy loads.<br><strong>No:</strong> The ramp time is probably adequate. Check motor wiring and nameplate parameter entries next.</div>
</details>

<details class="dtree"><summary>Do the motor nameplate voltage, current, and frequency values match the parameters programmed into the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> Parameters are correct. Verify output wiring integrity and check for shorts in the motor or cable.<br><strong>No:</strong> Re-enter the correct motor nameplate data into the drive and perform an autotune if the drive offers that function.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down and lock out** the drive following all applicable safety procedures, then verify zero voltage at the input and output terminals with a meter.
2. **Disconnect the motor cables** at the drive output terminals and inspect each terminal for tightness, corrosion, and signs of arcing or overheating.
3. **Megger the motor windings** (or use an insulation resistance tester) to check for winding-to-ground or phase-to-phase faults that would cause overcurrent.
4. **Check the mechanical load** by rotating the motor shaft by hand or running the driven equipment with the coupling disengaged to confirm no binding or excessive friction.
5. **Review and adjust acceleration time** by accessing the drive parameter menu, locating the acceleration time register (consult your model's manual for the specific parameter number), and increasing the value to allow a gentler ramp.
6. **Verify motor nameplate parameters** are correctly entered in the drive, including rated voltage, current, frequency, and power factor, and run an autotune sequence if available.
7. **Restore power and test** by starting the drive at no load or light load first, then gradually increasing to full load while monitoring the display for current and fault indications.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 series VFD replacement unit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-04-fault-code&k=Yaskawa+GA800+series+VFD+replacement+unit&tag=errorcodefixes-20) \| Only required if internal hardware fault is confirmed after all parameter and wiring checks. |
| Three-phase shielded VFD output cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-04-fault-code&k=Three-phase+shielded+VFD+output+cable&tag=errorcodefixes-20) \| Replace if insulation damage or short circuit is found in the existing motor cable. |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not trained in high-voltage AC power systems, if you cannot safely perform insulation resistance testing on motor windings, or if the fault persists after correcting acceleration parameters and verifying all wiring. VFD troubleshooting requires familiarity with parameter programming, three-phase power measurement, and safe isolation procedures. A professional can also perform advanced diagnostics such as current waveform analysis and drive component testing that are beyond typical operator capabilities.

**Rough cost:** A pro service call runs about $150-400.

## See Also

- [Yaskawa A1000 rH Fault Code - Causes & Fix](/posts/yaskawa-a1000-vfd-rh-fault-code/)
- [Yaskawa GA800 E52 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e52-fault-code/)
- [Yaskawa GA800 E41 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e41-fault-code/)
- [Yaskawa A1000 oH Fault Code - Causes & Fix](/posts/yaskawa-a1000-vfd-oh-fault-code/)
