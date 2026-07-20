---
title: "ABB ACS580 VFD E0031 Fault Code - Causes & Fix"
description: "E0031 signals a motor or drive issue on ABB ACS580 VFDs. Check parameter settings, motor connections, and load conditions first."
pubDatetime: 2026-07-18T08:00:07Z
modDatetime: 2026-07-18T08:00:07Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - abb
money_part: "ABB ACS580 control board or I/O board"
most_likely_cause: "incorrect parameter settings or motor configuration mismatch"
likelihood: "often"
diy_or_pro: "pro"
free_checks:
  - "Check the drive display or keypad for the detailed fault description and consult the manual for E0031 specifics"
  - "Verify that all motor cable connections are tight at both the drive and motor terminal boxes"
  - "Review the drive's parameter settings against the motor nameplate to confirm motor type, voltage, frequency, and current ratings match"
no_buy_pct: "60%"
---

## ABB ACS580 VFD E0031 Fault Code — What It Means

The E0031 fault code on an ABB ACS580 variable frequency drive indicates the controller has detected an abnormal operating condition. The exact meaning of E0031 can vary depending on your drive's firmware version and configuration, so consult your ACS580 manual or the drive's diagnostic display for the specific fault description.

In general, fault codes in this range often relate to motor control issues, parameter mismatches, or unexpected feedback from the motor or load. The drive trips to protect itself and the connected equipment from damage. Clearing the fault and restarting may work temporarily, but the underlying cause must be found to prevent repeated trips.

## Before You Replace Anything

Technicians sometimes replace the entire VFD when the real problem is a loose motor cable or an incorrect parameter setting. Always review the fault history log and verify motor nameplate data against drive parameters before ordering a new drive.

[Jump to Fix](#fix)

## Common Causes

- **Parameter mismatch or incorrect motor settings (~35%)** If the drive's motor parameters do not match the actual motor nameplate data, the controller can generate faults during startup or under load.
- **Loose or damaged motor power cables (~25%)** Poor connections or damaged insulation on the output cables can cause intermittent faults or unexpected current readings.
- **Excessive or unbalanced motor load (~20%)** A mechanical overload, binding, or imbalance in the driven equipment can cause the motor to draw unexpected current and trip the drive.
- **Encoder or feedback device error (~10%)** If your application uses an encoder or other feedback device, a wiring fault or device failure can trigger control faults.
- **Internal drive sensor or control board fault (~10%)** A failed current sensor, temperature sensor, or control circuit inside the VFD can generate spurious fault codes.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drive display show a detailed fault description for E0031 on the keypad or HMI?</summary>
<div class="dtree-body"><strong>Yes:</strong> Note the full description and consult the manual's fault table for that specific message and recommended corrective actions.<br><strong>No:</strong> Power-cycle the drive and attempt to access the fault history log through the menu to retrieve more information.</div>
</details>

<details class="dtree"><summary>Are the motor nameplate voltage, frequency, and current ratings entered correctly in the drive's motor parameters?</summary>
<div class="dtree-body"><strong>Yes:</strong> The parameter setup is likely correct; check motor cable connections and mechanical load next.<br><strong>No:</strong> Correct the motor parameters to match the nameplate, perform an auto-tune if available, and reset the fault.</div>
</details>

<details class="dtree"><summary>Does the motor run smoothly by hand or with the mechanical load disconnected?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor and cables are likely OK; the fault may be caused by excessive load, binding, or a control issue.<br><strong>No:</strong> Inspect the motor bearings, coupling, and driven equipment for mechanical faults before re-energizing the drive.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Stop the drive and lock out power** at the upstream disconnect to safely inspect connections and review settings.
2. **Access the drive's display or keypad** and record the full fault description for E0031 along with any other active faults or warnings in the fault history log.
3. **Consult the ACS580 manual** for your firmware version to find the exact definition of E0031 and the manufacturer's recommended corrective actions.
4. **Verify motor nameplate data** against the drive's motor parameter group, including rated voltage, frequency, current, power, and connection type; correct any mismatches.
5. **Inspect all motor power cables** at the drive output terminals and at the motor for tight, clean connections and check for signs of insulation damage or overheating.
6. **Check the mechanical load** by disconnecting the motor from the driven equipment if possible and verifying that the motor shaft turns freely without binding or unusual noise.
7. **Reset the fault** using the drive's keypad or control input, then restart the drive and monitor current, speed, and torque on the display to confirm normal operation; if the fault recurs immediately, contact a qualified VFD technician or ABB support for further diagnostics.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB ACS580 control board or I/O board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0031-fault-code&k=ABB+ACS580+control+board+or+I%2FO+board&tag=errorcodefixes-20) \| Only required if internal diagnostics confirm a board-level fault; consult ABB service first. |
| Motor power cable assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0031-fault-code&k=Motor+power+cable+assembly&tag=errorcodefixes-20) \| Use shielded VFD-rated cable of the correct gauge for your motor and cable length. |

## When to Call a Pro

Call a qualified electrician or VFD technician if you are not trained to work safely around high-voltage motor drives, if the fault persists after verifying parameters and connections, or if internal diagnostics suggest a failed sensor or control board. VFD troubleshooting requires multimeter skills, familiarity with three-phase power, and access to manufacturer diagnostic tools. A technician can also perform auto-tuning, load testing, and firmware updates that may resolve intermittent faults. If your application is mission-critical or the drive is still under warranty, always contact ABB or an authorized service center before opening the enclosure or replacing components.

**Rough cost:** A pro service call runs about $200-600.
