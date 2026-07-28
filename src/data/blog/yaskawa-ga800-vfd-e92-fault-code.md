---
title: "Yaskawa GA800 E92 Fault - Causes & Fix"
description: "E92 on a Yaskawa GA800 means the Safe Torque Off (STO) safety circuit is open or invalid. Most often a missing jumper or open E-stop."
pubDatetime: 2026-06-08T10:44:47Z
modDatetime: 2026-06-08T10:44:47Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
most_likely_cause: "Missing or removed jumper on the STO terminals"
likelihood: "the most common cause"
diy_or_pro: "pro"
money_part: "STO jumper for Yaskawa GA800"
---

## What this code means
E92 on the Yaskawa GA800 VFD is a Safe Torque Off (STO) safety-input-related fault. It does not indicate a motor fault, overcurrent, or power problem. Instead, the drive has detected that the STO safety circuit is not in the required closed or valid state, so torque production to the motor is inhibited even though control power may still be present. The STO function is a safety feature that prevents the drive from delivering torque when the safety circuit is open, miswired, or not satisfied.

When the drive reports E92, it means the safety terminals are either missing the required factory jumper (if the drive is configured to run without an external safety loop), or the external safety chain (E-stop, guard door, safety relay contacts, interlock wiring) is open or faulted. Yaskawa's troubleshooting guidance emphasizes verifying the safety circuit wiring and the drive's STO terminal configuration rather than treating this as a drive hardware failure.

## Before You Replace Anything

Technicians sometimes replace the VFD control board or main drive unit when E92 appears, but the fault is almost always in the external safety wiring or a missing STO jumper. Always trace the safety circuit end-to-end and confirm the STO terminal state before ordering drive parts.

## Common Causes

- **Missing or removed STO jumper (~40%)** When the drive is meant to run without an external safety loop, the factory or field jumper at the STO terminals must be present and correctly installed.
- **Open E-stop or guard switch (~30%)** An activated E-stop, open guard door, or safety relay contact in the external safety chain will prevent the STO circuit from closing.
- **Loose, broken, or mislanded wiring at STO terminals (~15%)** Wiring faults on the STO inputs, associated common, or feedback terminals will cause the drive to detect an invalid safety state.
- **Incorrect terminal assignment after initialization (~10%)** After a factory reset or reinitialization, the drive's STO terminal configuration may no longer match the field wiring arrangement.
- **Failed safety relay or interposing contact (~5%)** A safety relay or interlock contact in the upstream safety chain may have failed open even though the E-stop appears reset.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is there an external E-stop or guard safety circuit wired to the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> Check that all E-stops are reset, guard doors are closed, and safety relay contacts are made. Use a multimeter to verify continuity through the entire safety chain.<br><strong>No:</strong> The drive should have a factory jumper across the STO terminals. Power down safely, wait for DC bus discharge, then inspect the STO terminal block for the jumper.</div>
</details>

<details class="dtree"><summary>Does the keypad show the same E92 fault after resetting the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The STO circuit is still open or invalid. Trace the safety wiring end-to-end using the machine's elementary diagram and verify all connections at the drive terminals.<br><strong>No:</strong> The fault was transient or the external safety condition has been restored. Monitor the drive during normal operation to confirm the issue is resolved.</div>
</details>

<details class="dtree"><summary>Did the fault appear immediately after a drive reset, reinitialization, or parameter change?</summary>
<div class="dtree-body"><strong>Yes:</strong> The STO terminal configuration may have been altered during initialization. Verify the drive's STO parameter settings match the physical jumper or external safety wiring arrangement.<br><strong>No:</strong> Focus on the external safety chain. Inspect wiring, contacts, and safety relay operation rather than drive parameters.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Confirm the fault code** on the GA800 keypad and note the exact fault text. Verify the drive model and terminal arrangement before proceeding.
2. **Obtain the machine's elementary or safety diagram** so you can trace the STO safety circuit end-to-end from the drive terminals through all external devices.
3. **Power down the drive safely** using the disconnect or main breaker, then wait for the DC bus discharge time specified on the drive label before touching any wiring.
4. **Inspect the STO terminal block** on the GA800. If the drive is configured to run without an external safety loop, confirm the required STO jumper is present and seated correctly.
5. **Trace the external safety chain** if one is installed. Check E-stop buttons, guard switches, safety relay contacts, and all interposing wiring for continuity. Measure across each device in the de-energized state to confirm the circuit is closed when it should be.
6. **Verify STO terminal assignment and parameters** if the drive was recently initialized or reset. Confirm the parameter settings match the physical wiring (factory jumper vs. external safety circuit).
7. **Restore power and reset the fault** from the keypad after the STO circuit cause is corrected. If the fault persists with verified wiring and jumper, substitute known-good safety contact hardware or contact Yaskawa technical support for drive-level troubleshooting.

## Parts Often Needed

| Part | Notes |
|------|-------|
| STO jumper for Yaskawa GA800 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e92-fault-code&k=STO+jumper+for+Yaskawa+GA800&tag=errorcodefixes-20) \| Factory or field jumper for drives configured to run without an external safety loop. Consult the GA800 manual for the correct terminal arrangement. |
| Safety relay or contact block | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e92-fault-code&k=Safety+relay+or+contact+block&tag=errorcodefixes-20) \| Replacement for failed safety relay or interposing contact in the external E-stop or guard circuit. Match the existing relay model and contact rating. |

## When to Call a Pro

Call a qualified electrician or automation technician if you are not trained in industrial control wiring, lockout/tagout procedures, or VFD safety circuits. Safe Torque Off troubleshooting requires working with the machine's safety diagram, understanding the external interlock chain, and verifying DC bus discharge before touching terminals. If the STO circuit appears intact but the fault persists, the drive's control or safety interface may be damaged and requires evaluation by Yaskawa technical support or a certified service center. Never bypass or jumper STO terminals to defeat the safety function.

**Rough cost:** A pro service call runs about $150-400.
