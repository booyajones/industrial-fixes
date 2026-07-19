---
title: "ABB ACS580 VFD E0001 Fault Code - Causes & Fix"
description: "E0001 signals an overcurrent trip on the ABB ACS580 drive. Check motor and wiring for shorts, then verify parameter settings."
pubDatetime: 2026-07-17T07:40:02Z
modDatetime: 2026-07-17T07:40:02Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - abb
money_part: "Motor cable (shielded VFD-rated)"
most_likely_cause: "motor or cable fault causing excessive current draw"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect motor cable for visible damage, pinched insulation, or water ingress"
  - "Check drive parameter settings against motor nameplate to confirm ramp times and current limits are appropriate"
  - "Review the drive's fault history log to see if the fault occurs at a specific point in the cycle"
---

## ABB ACS580 VFD E0001 Fault Code — What It Means

The E0001 fault on an ABB ACS580 variable frequency drive indicates an overcurrent condition has been detected and the drive has tripped to protect itself and the connected motor. This fault occurs when the current drawn by the motor exceeds the drive's safe operating limits, either instantaneously or over a brief period.

The drive monitors current continuously and will shut down if it detects a sudden surge or sustained overload that could damage internal components or the motor. The fault can be triggered during acceleration, deceleration, or steady-state operation depending on the underlying cause. Consult your model's manual for the specific current thresholds that trigger this fault, as these vary by drive frame size and rating.

## Before You Replace Anything

Replacing the VFD itself is often unnecessary. Measure motor winding resistance and insulation resistance first to confirm the motor is not shorted or grounded, which account for many E0001 faults.

[Jump to Fix](#fix)

## Common Causes

- **Motor winding or cable short (~35%)** A short circuit in the motor windings or in the cable between the drive and motor creates a low-resistance path that draws excessive current and trips the drive immediately.
- **Mechanical overload on motor (~25%)** A jammed bearing, seized pump, or other mechanical bind forces the motor to draw higher current as it struggles against the load, eventually exceeding the drive's limits.
- **Incorrect drive parameters (~20%)** Acceleration or deceleration times set too short, current limits set too low, or motor parameters not matching the actual motor nameplate can cause the drive to trip even under normal load.
- **Drive output stage failure (~10%)** A failed IGBT or other component in the drive's inverter section can create an internal fault that manifests as an overcurrent condition.
- **Ground fault in motor or cable (~7%)** Insulation breakdown allowing current to flow to ground through the motor frame or cable shield triggers overcurrent protection.
- **Incorrect motor connection (~3%)** Motor wired for the wrong voltage (for example delta when it should be wye) will draw current outside the drive's rating.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault occur immediately upon start, or only after the motor runs for a time?</summary>
<div class="dtree-body"><strong>Yes:</strong> Immediate faults point to a wiring short, ground fault, or severe parameter mismatch. Inspect cables and connections first.<br><strong>No:</strong> Faults after running suggest mechanical overload or thermal issues. Check for binding in the driven equipment and verify load is within motor rating.</div>
</details>

<details class="dtree"><summary>Can you disconnect the motor and run the drive into a known-good test motor without faulting?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem is in the original motor, its cable, or the driven load. Focus troubleshooting there.<br><strong>No:</strong> The drive itself may have an internal fault or the parameter settings are incorrect. Review programming and consider drive replacement if settings are correct.</div>
</details>

<details class="dtree"><summary>Do the motor cable and terminations show any signs of physical damage, moisture, or overheating?</summary>
<div class="dtree-body"><strong>Yes:</strong> Replace or repair the damaged cable and terminations, then test. Damaged insulation is a frequent cause of overcurrent trips.<br><strong>No:</strong> Proceed to electrical testing of motor windings and insulation resistance, and verify parameter settings against the motor nameplate.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** from the drive and follow lockout/tagout procedures. Wait for the DC bus capacitors to discharge completely before opening any covers or touching terminals.
2. **Record all drive parameters** by uploading the configuration to a laptop or writing down acceleration time, deceleration time, motor nameplate settings, and current limits so you can restore them if needed.
3. **Inspect the motor cable** from the drive output terminals to the motor junction box. Look for pinched insulation, cuts, cable ties that are too tight, or any signs of arcing or moisture.
4. **Measure motor winding resistance** phase-to-phase with a multimeter. The three readings should be balanced within a few percent. A very low reading indicates a shorted winding.
5. **Perform an insulation resistance test** (megger test) between each motor phase and ground with at least 500 VDC. Readings below one megohm suggest insulation breakdown.
6. **Verify drive parameter settings** against the motor nameplate. Confirm that the rated motor voltage, current, frequency, and power match the values entered in the drive, and that acceleration and deceleration ramps are not set to unrealistically short times.
7. **Check for mechanical binding** by rotating the motor shaft by hand (with power off and the load disconnected if possible). The shaft should turn smoothly without excessive resistance.
8. **Clear the fault** and restart the drive under no-load or light-load conditions. If the fault does not recur, gradually increase load while monitoring current on the drive display to identify the point at which the fault trips.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable (shielded VFD-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0001-fault-code&k=Motor+cable+%28shielded+VFD-rated%29&tag=errorcodefixes-20) \| Use cable rated for variable frequency drive service with continuous flex rating if the application involves motion. |
| Three-phase AC motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0001-fault-code&k=Three-phase+AC+motor&tag=errorcodefixes-20) \| Match voltage, horsepower, frame, and mounting to the original motor nameplate and application requirements. |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not trained in high-voltage AC work, do not have the proper test equipment (multimeter, megohmmeter, and clamp ammeter), or if the fault persists after checking cables and parameters. VFD troubleshooting requires interpreting current waveforms, verifying three-phase balance, and sometimes accessing internal diagnostics that are beyond typical DIY scope. A technician can also perform dynamic testing under load and use a motor circuit analyzer to pinpoint intermittent faults that do not show up during static resistance checks.

**Rough cost:** A pro service call runs about $200-800.

## See Also

- [ABB ACS580 A2A3 Fault Code - Causes & Fix](/posts/abb-acs580-vfd-a2a3-fault-code/)
- [ABB ACS580 VFD E0002 Fault Code - Causes & Fix](/posts/abb-acs580-vfd-e0002-fault-code/)
- [ABB ACS580 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs580-fault-3130/)
- [ABB ACS880 Fault 2310 Overcurrent — Causes & Fix](/posts/abb-acs880-fault-2310-overcurrent/)
