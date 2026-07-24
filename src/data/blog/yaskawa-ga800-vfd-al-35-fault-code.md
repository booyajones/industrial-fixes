---
title: "Yaskawa GA800 VFD AL-35 Fault - Causes & Fix"
description: "AL-35 indicates an overcurrent or ground fault. Most often caused by a shorted motor cable or motor winding. Check cable insulation first."
pubDatetime: 2026-07-22T07:28:19Z
modDatetime: 2026-07-22T07:28:19Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "VFD-rated shielded motor cable"
most_likely_cause: "Shorted or damaged motor cable insulation"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect motor cable for visible damage, pinch points, or abraded insulation"
  - "Check cable routing for contact with sharp edges or rotating parts"
  - "Verify motor cable shield and ground connections are tight and corrosion-free"
part_price: "$80-300"
---

## Yaskawa GA800 VFD AL-35 Fault — What It Means

The AL-35 fault code on a Yaskawa GA800 variable frequency drive typically signals an overcurrent condition or ground fault detected during operation. This alarm trips when the drive senses current flow exceeding safe limits, either through an output phase or to ground. The drive shuts down immediately to protect both itself and the connected motor from damage.

The fault can occur during acceleration, steady-state running, or deceleration. Because the GA800 monitors output current constantly, AL-35 may appear alongside other alarms if multiple conditions exist. Consult your drive's manual for the exact parameter definitions and threshold values, as configuration and sensitivity can vary by model and application.

## Before You Replace Anything

Many technicians replace the VFD itself when AL-35 appears, but most cases stem from damaged output cables or motor windings. Perform a megohm insulation test on the motor cable and motor windings before condemning the drive.

[Jump to Fix](#fix)

## Common Causes

- **Shorted or damaged motor cable (~40%)** Insulation breakdown in the output cable creates a phase-to-phase or phase-to-ground fault that trips the overcurrent protection.
- **Motor winding fault (~25%)** Shorted or grounded motor windings draw excessive current and trigger the alarm during operation.
- **Incorrect drive parameters (~15%)** Overly aggressive acceleration rates, incorrect motor nameplate data, or low current-limit settings cause nuisance trips.
- **Mechanical overload (~10%)** Seized bearings, jammed loads, or coupling misalignment force the motor to draw fault-level current.
- **Drive output module failure (~7%)** Failed IGBTs or gate drivers inside the VFD generate erratic output current and trigger the fault.
- **Loose or corroded cable terminations (~3%)** Poor connections at the drive output terminals or motor junction box create arcing and current spikes.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault occur immediately on startup before the motor accelerates?</summary>
<div class="dtree-body"><strong>Yes:</strong> Likely a shorted motor cable or motor winding. Disconnect the motor and perform a megohm test on the cable and motor separately.<br><strong>No:</strong> The fault may be load-related or parameter-based. Check for mechanical binding and review acceleration and current-limit settings.</div>
</details>

<details class="dtree"><summary>Can you feel heat or smell burning insulation at the motor or cable?</summary>
<div class="dtree-body"><strong>Yes:</strong> Stop operation immediately. A short or ground fault is generating heat. Inspect cable insulation and motor windings before applying power again.<br><strong>No:</strong> The fault may be intermittent or parameter-related. Check cable routing and verify all parameter settings match the motor nameplate.</div>
</details>

<details class="dtree"><summary>Does the drive clear the fault and run normally after a power cycle?</summary>
<div class="dtree-body"><strong>Yes:</strong> An intermittent issue such as a loose connection or marginal cable insulation is likely. Inspect and re-torque all terminations.<br><strong>No:</strong> The fault is persistent. Disconnect the motor and test the drive with no load to isolate whether the drive or motor circuit is at fault.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down and lock out** the VFD and disconnect all upstream power to eliminate shock hazards.
2. **Record the fault history** from the drive's alarm log to see if AL-35 is the only fault or if others accompany it.
3. **Inspect the motor cable** along its entire length for cuts, pinches, cable ties that are too tight, or contact with sharp edges.
4. **Disconnect the motor cable** at the drive output terminals and perform a megohm insulation test on the cable between each phase and ground, and phase-to-phase.
5. **Test motor winding insulation** using a megohm meter at the motor junction box with the cable disconnected to isolate cable faults from motor faults.
6. **Check all output terminations** at both the drive and motor for tightness, corrosion, and proper torque per the installation manual.
7. **Review drive parameters** including motor nameplate data, acceleration and deceleration times, and current-limit settings to confirm they match the application and motor rating.

## Parts Often Needed

| Part | Notes |
|------|-------|
| VFD-rated shielded motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-35-fault-code&k=VFD-rated+shielded+motor+cable&tag=errorcodefixes-20) \| Use cable rated for inverter duty with proper shielding and sized per drive manual recommendations. |
| Replacement three-phase motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-35-fault-code&k=Replacement+three-phase+motor&tag=errorcodefixes-20) \| Match horsepower, voltage, frequency, and frame size to the original motor nameplate. |

## When to Call a Pro

Call a qualified electrician or automation technician if you lack experience with high-voltage equipment, megohm testing, or VFD parameter programming. AL-35 faults involve live circuits and require safe lockout procedures and proper test equipment. A professional can perform insulation resistance tests, verify grounding integrity, check drive output modules with an oscilloscope, and reprogram parameters to match your motor and load. If the fault persists after cable and motor checks, the drive's internal components may need repair or replacement, which requires factory-trained service.

**Rough cost:** A pro service call runs about $200-800.
