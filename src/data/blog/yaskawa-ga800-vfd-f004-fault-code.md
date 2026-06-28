---
title: "Yaskawa GA800 F004 Fault - Causes & Fix"
description: "F004 means DC bus undervoltage on the Yaskawa GA800 VFD. Most often caused by low incoming line voltage or loose input connections."
pubDatetime: 2026-06-26T10:00:32Z
modDatetime: 2026-06-26T10:00:32Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "AC line reactor (input choke)"
most_likely_cause: "low incoming line voltage or loose input terminal connections"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Measure incoming line voltage at the drive input terminals with a multimeter to verify it matches the drive nameplate rating"
  - "Inspect and tighten all input power terminal connections and motor lead lugs"
  - "Check that the acceleration time parameter (P041) is not set too short for the load"
no_buy_pct: "60%"
---

## Yaskawa GA800 F004 Fault — What It Means

The F004 fault on a Yaskawa GA800 VFD signals that the internal DC bus voltage has dropped below the minimum safe operating threshold. This is a protective shutdown designed to prevent damage to the drive's IGBTs and control circuitry when insufficient voltage is present. The drive will not run until the underlying voltage problem is corrected and the fault is cleared.

This fault typically appears when the incoming AC line voltage is too low, when connections are loose, or when the drive's acceleration settings demand more current than the power supply can deliver without voltage sag. It protects the drive from operating in an unstable state that could destroy internal components.

## Before You Replace Anything

Technicians sometimes replace the drive's main control board or input rectifier before checking the simple things. Always measure the actual incoming line voltage with a true-RMS meter and inspect all terminal connections for tightness before ordering any internal drive components.

[Jump to Fix](#fix)

## Common Causes

- **Low incoming line voltage (~35%)** The utility supply voltage is below the drive's rated minimum (for example, a 480V drive receiving only 400V), causing the DC bus to sag below the protective threshold.
- **Loose or corroded input connections (~25%)** Loose terminal screws or partially clamped wire lugs create resistance that drops voltage under load, triggering the undervoltage fault.
- **Acceleration time set too short (~20%)** A very fast acceleration ramp (short P041 parameter) demands high inrush current that momentarily pulls the DC bus voltage below the threshold, especially on soft power supplies.
- **Long cable runs with undersized wire (~10%)** Resistive voltage drop over long AC cable runs between the supply and the drive input reduces the voltage available to the drive.
- **Phase voltage unbalance (~5%)** Unbalanced input phases (more than 1% variation phase-to-phase) can cause one leg of the rectifier to underperform and drop the DC bus.
- **Mechanical motor rotor issues (~5%)** A motor rotor that momentarily locks and then slips free causes sudden load spikes that can transiently drop the DC bus voltage.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the measured incoming line voltage at the drive input terminals match the drive nameplate rating (within 10%)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Input voltage is acceptable. Move on to check terminal connections and acceleration settings.<br><strong>No:</strong> Supply voltage is too low. Contact your utility or install a line reactor or buck-boost transformer to correct the voltage before it reaches the drive.</div>
</details>

<details class="dtree"><summary>Are all input power terminal screws and motor lead lugs tight (use a torque screwdriver to verify)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Connections are good. Check the acceleration time parameter and cable length next.<br><strong>No:</strong> Loose connections are causing voltage drop. Tighten all terminals to the torque spec in the manual and retest.</div>
</details>

<details class="dtree"><summary>Does the fault occur only during motor start or acceleration?</summary>
<div class="dtree-body"><strong>Yes:</strong> The acceleration ramp is likely too aggressive. Increase the P041 (Accel Time) parameter to reduce inrush current demand.<br><strong>No:</strong> The fault is present even at idle or constant speed. The problem is likely continuous low voltage or a failing input stage in the drive itself.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and lock out the input breaker following your facility's electrical safety procedures.
2. **Measure incoming line voltage** at the drive input terminals (L1, L2, L3) using a true-RMS multimeter and compare to the drive nameplate rating.
3. **Inspect and tighten all input terminal connections** and motor lead lugs to the torque specification in the GA800 manual.
4. **Measure phase-to-phase voltage** on all three legs and verify they are within 1% of each other to rule out phase unbalance.
5. **Review the acceleration time parameter** (P041) in the drive programming and increase it if it is set shorter than the motor and load can handle without excessive current draw.
6. **Check cable run length and wire gauge** from the supply to the drive input and verify the wire is sized correctly for the distance and load to prevent resistive voltage drop.
7. **Clear the fault** using the drive keypad or reset input and restart the drive under normal operating conditions to confirm the fix.

## Parts Often Needed

| Part | Notes |
|------|-------|
| AC line reactor (input choke) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f004-fault-code&k=AC+line+reactor+%28input+choke%29&tag=errorcodefixes-20) \| Installed ahead of the drive to stiffen the DC bus and reduce voltage sag on soft power supplies or long cable runs. |
| Yaskawa GA800 main control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f004-fault-code&k=Yaskawa+GA800+main+control+board&tag=errorcodefixes-20) \| Only if diagnostics confirm the internal voltage sensing or rectifier stage has failed, not a first-line part. |

## When to Call a Pro

Call a qualified electrician or VFD technician if you are not trained and authorized to work inside energized industrial control panels. Diagnosing F004 requires measuring live AC line voltage and working with high-voltage DC bus circuits that can exceed 600 volts. A technician will verify the incoming power quality, check for loose connections, adjust drive parameters, and determine whether the drive itself has internal damage. If the fault persists after correcting supply voltage and connections, the drive may need factory repair or replacement, which requires proper calibration and commissioning.

**Rough cost:** A pro service call runs about $150-400 for diagnostics and wiring corrections, more if drive replacement is needed.
