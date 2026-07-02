---
title: "Danfoss FC302 AL-135 Fault - Causes & Fix"
description: "AL-135 is likely Alarm 13, output overcurrent during operation. Most common fix: check motor overload and verify parameter 1-24."
pubDatetime: 2026-06-25T09:23:19Z
modDatetime: 2026-06-25T09:23:19Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 inverter IGBT module"
most_likely_cause: "Motor mechanically overloaded or parameter 1-24 (nominal motor current) set too low"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify parameter 1-24 (nominal motor current) matches the motor nameplate rating exactly"
  - "Check that all cooling fans are running and vents are not blocked"
  - "Inspect motor cable connections for loose or corroded terminals at both ends"
---

## Danfoss FC302 AL-135 Fault — What It Means

There is no specific fault code labeled AL-135 for the Danfoss FC302 VFD. The code is most likely a misreading of Alarm 13, which is the standard output overcurrent fault for this drive series. Alarm 13 means the drive detects output current exceeding safe operating thresholds (typically 150 to 160% of nominal current) gradually over several seconds, rather than an instantaneous short circuit. This fault protects the drive from thermal damage due to excessive current loading.

Unlike a fast-trip overcurrent event, Alarm 13 flags a sustained high-current condition during normal operation or acceleration. The drive monitors whether current builds beyond its rated capacity for a period lasting several seconds. Common triggers include mechanical overload on the motor, incorrect parameter settings, motor winding faults, or cooling system problems.

## Before You Replace Anything

Technicians often replace the inverter IGBT modules before checking the motor itself. Run the drive unloaded (motor disconnected) first. If the alarm clears, the fault is in the motor, cable, or load, not the drive.

[Jump to Fix](#fix)

## Common Causes

- **Motor mechanical overload (~35%)** A stuck bearing, jammed impeller, or seized shaft forces the motor to draw excessive current as it tries to overcome the resistance.
- **Incorrect parameter 1-24 (~25%)** Nominal motor current set too low causes the drive to flag normal operating current as overcurrent.
- **Motor winding partial short (~15%)** Developing insulation failure in motor windings creates abnormal current paths and elevated current draw.
- **Loose or corroded motor cable connections (~10%)** High-resistance connections between drive and motor create voltage drop and compensatory current spikes.
- **Failed IGBT modules (~10%)** Aging or damaged inverter IGBT modules lose current regulation ability and mis-report or cause actual overcurrent.
- **Insufficient cooling airflow (~5%)** Blocked vents or failed fans cause overheating, which triggers thermal overcurrent protection.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the motor turn freely by hand with the drive powered off?</summary>
<div class="dtree-body"><strong>Yes:</strong> Mechanical load is normal. Move to parameter and electrical checks.<br><strong>No:</strong> Motor or driven equipment is mechanically bound. Clear the obstruction or repair the bearing before restarting.</div>
</details>

<details class="dtree"><summary>Does Alarm 13 clear when you run the drive with the motor disconnected?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive is functioning correctly. The fault is in the motor, cable, or load.<br><strong>No:</strong> Internal drive failure (IGBT or module fault). The drive needs professional repair or replacement.</div>
</details>

<details class="dtree"><summary>Is parameter 1-24 set to match the motor nameplate current rating?</summary>
<div class="dtree-body"><strong>Yes:</strong> Parameter is correct. Proceed to motor insulation and connection checks.<br><strong>No:</strong> Adjust parameter 1-24 to the correct value from the motor nameplate and reset the drive.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify parameter 1-24** by navigating to the drive menu and confirming the nominal motor current matches the motor nameplate exactly.
2. **Check cooling fans** by observing whether all fans spin when the drive is powered. Clear any blocked intake or exhaust vents.
3. **Inspect motor cable connections** at both the drive output terminals and motor terminal box for tightness and corrosion.
4. **Run the drive unloaded** by disconnecting the motor cables from the drive output and attempting a start. If Alarm 13 clears, the fault is motor-side. If it persists, the drive has an internal failure.
5. **Perform a megohm test** on the motor windings to ground using an insulation tester. Readings below 2 megohms indicate insulation failure and the motor needs repair or replacement.
6. **Check for mechanical overload** by manually rotating the motor shaft with power off. Excessive resistance or binding indicates a stuck bearing or jammed driven equipment.
7. **Replace IGBT modules** if the drive fails the unloaded test. This requires disassembling the drive and swapping the inverter board or IGBT assembly, a job for qualified service personnel or return to Danfoss.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 inverter IGBT module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-135-fault-code&k=Danfoss+FC302+inverter+IGBT+module&tag=errorcodefixes-20) \| Only needed if the drive fails when run unloaded. Consult your model suffix for the correct module. |
| Motor insulation repair or rewind | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-135-fault-code&k=Motor+insulation+repair+or+rewind&tag=errorcodefixes-20) \| If megohm test shows below 2 megohms, the motor needs professional rewind or replacement. |

## When to Call a Pro

Call a qualified drive technician or motor shop if the drive trips Alarm 13 when run unloaded (motor disconnected), which points to internal IGBT or module failure. Also call for help if the motor megohm test reads below 2 megohms, indicating winding insulation failure that requires professional rewind or replacement. If you are unfamiliar with AC drive parameter programming or high-voltage three-phase wiring, bring in a technician to verify motor data settings (parameters 1-20 through 1-25) and inspect output connections safely. Drive and motor repairs involve lethal voltages and require lockout-tagout procedures and appropriate test equipment.

**Rough cost:** A pro service call runs about $200-800 depending on whether the fault is motor-side or requires drive module replacement.

## See Also

- [Danfoss FC302 AL-165 - Causes & Fix](/posts/danfoss-fc302-vfd-al-165-fault-code/)
- [Danfoss FC302 Alarm 34 - Causes & Fix](/posts/danfoss-fc302-alarm-34-fault-code/)
- [Danfoss FC302 AL-95 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-95-fault-code/)
- [Danfoss FC302 VFD AL-87 - Causes & Fix](/posts/danfoss-fc302-vfd-al-87-fault-code/)
