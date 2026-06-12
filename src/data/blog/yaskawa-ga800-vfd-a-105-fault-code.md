---
title: "Yaskawa GA800 A.105 Alarm - Causes & Fix"
description: "A.105 means the GA800 could not complete its auto-tuning routine. Most often caused by loose motor wiring or incorrect motor data entry."
pubDatetime: 2026-06-08T10:58:02Z
modDatetime: 2026-06-08T10:58:02Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
most_likely_cause: "motor wiring issues such as loose terminals, open phase, or incorrect motor connection"
likelihood: "the most common cause"
diy_or_pro: "pro"
money_part: "Motor output power cable"
---

## Yaskawa GA800 A.105 Alarm — What It Means

A.105 is an alarm code on the Yaskawa GA800 variable frequency drive that appears when the drive cannot successfully finish its auto-tuning or motor adjustment routine. Unlike a fault that trips the drive immediately, this alarm indicates the drive was unable to establish the motor parameters it needs for proper control during the tuning process. The GA800 manual distinguishes alarms from faults, and A.105 falls into the alarm category related to tuning and adjustment functions.

When this alarm appears, the drive is essentially telling you it could not gather or verify the motor data required for vector control or other advanced control modes. This can happen during initial commissioning, after a parameter reset, or anytime the auto-tune procedure is run. The drive needs accurate motor electrical characteristics to operate efficiently and safely, and A.105 means that process was interrupted or unsuccessful.

## Before You Replace Anything

Technicians sometimes replace the drive itself when A.105 appears, assuming internal failure. Instead, always inspect and tighten all motor output terminals (U, V, W) and verify motor nameplate data matches drive parameters before declaring the drive defective.

[Jump to Fix](#fix)

## Common Causes

- **Loose or poor motor wiring (~40%)** Open phase, loose U/V/W terminals, incorrect motor connection, or poor termination prevents the drive from completing tuning.
- **Incorrect motor data entered (~25%)** Mismatched horsepower, voltage, amperage, pole count, or base frequency in drive parameters after motor replacement or reset.
- **Mechanical load unsuitable for tuning (~20%)** Coupled load that is too heavy, locked, or unsafe to rotate during the auto-tune procedure prevents completion.
- **Wrong control mode or parameter state (~10%)** Incorrect parameterization after reinitialization or reset leaves the drive in a state incompatible with tuning.
- **Input power quality issues (~5%)** Unstable input voltage or wiring abnormalities during tuning prevent the drive from maintaining stable conditions.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Are all three motor output terminals (U, V, W) tight and correctly connected?</summary>
<div class="dtree-body"><strong>Yes:</strong> Wiring is good. Move on to verify motor nameplate data matches drive parameters.<br><strong>No:</strong> Tighten all terminals to proper torque and check for swapped or loose conductors, then clear alarm and retry tuning.</div>
</details>

<details class="dtree"><summary>Does the motor nameplate horsepower, voltage, and frequency match what is programmed in the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor data is correct. Check if the motor can be uncoupled from the load for a no-load tuning test.<br><strong>No:</strong> Re-enter correct motor nameplate data into drive parameters, then clear alarm and retry tuning.</div>
</details>

<details class="dtree"><summary>Can the motor shaft rotate freely by hand when uncoupled from the load?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor is free. Retry auto-tune with motor uncoupled. If alarm repeats, escalate to Yaskawa support or suspect drive hardware.<br><strong>No:</strong> Mechanical binding or locked load is preventing tuning. Remove or disconnect the load, then retry tuning.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Record the alarm context**: note whether A.105 appeared during initial commissioning, after a reset, or during a manual auto-tune attempt, and check the keypad status ring to confirm it is an alarm rather than a fault.
2. **Inspect motor output wiring**: verify all U, V, and W terminals are tight to proper torque, check for loose or swapped conductors, and confirm motor cable shielding and grounding are correct.
3. **Verify motor nameplate data**: compare motor horsepower (or kW), voltage, amperage, pole count, and base frequency on the nameplate against drive parameters and correct any mismatches.
4. **Check motor insulation and phase continuity**: use a megohmmeter or multimeter to confirm motor windings are not shorted or open, and verify balanced resistance across all three phases.
5. **Uncouple the motor from the load if necessary**: if the application allows, disconnect the motor mechanically from the driven equipment and retry the auto-tune procedure with no load.
6. **Review drive control mode and initialization state**: confirm the drive is set to the correct control mode (V/f or vector) for your application and that parameter A1-03 initialization has been completed if a reset was performed.
7. **Clear the alarm and retry tuning**: reset the alarm from the keypad, then manually initiate the auto-tune or adjustment function according to the GA800 manual procedure for your control mode.
8. **Escalate to Yaskawa support if alarm repeats**: if A.105 persists after wiring, motor data, and mechanical checks, contact Yaskawa with the drive model, spec number, serial number, and detailed failure information for further diagnosis.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor output power cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-105-fault-code&k=Motor+output+power+cable&tag=errorcodefixes-20) \| If existing cable shows damage, fraying, or poor termination; must be rated for VFD use with proper shielding. |
| Motor terminal lugs and connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-105-fault-code&k=Motor+terminal+lugs+and+connectors&tag=errorcodefixes-20) \| Replacement lugs if existing terminals are corroded, overheated, or mechanically damaged. |

## When to Call a Pro

Call a qualified electrician or automation technician immediately if you are not trained to work on high-voltage three-phase equipment, if the alarm persists after basic wiring and parameter checks, or if you need to verify motor insulation and phase balance with specialized test equipment. Yaskawa VFDs operate at lethal voltages (typically 480V three-phase in industrial settings), and improper wiring or testing can cause electric shock, arc flash, or equipment damage. A professional can safely measure motor characteristics, perform proper auto-tuning procedures, interpret drive diagnostics, and escalate to Yaskawa technical support with the correct model and serial information if hardware replacement is needed.

**Rough cost:** A pro service call runs about $150-400 for diagnosis and wiring correction; more if motor or drive replacement needed.

## See Also

- [Yaskawa GA800 E10 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e10-fault-code/)
- [Yaskawa GA800 E57 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e57-fault-code/)
- [Yaskawa GA800 E07 Fault - Causes & Fix](/posts/yaskawa-ga800-e07-fault-code/)
- [Yaskawa GA800 E84 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e84-fault-code/)
