---
title: "Yaskawa GA800 EF3 Fault - Causes & Fix"
description: "EF3 means external fault input S3 is active. Most often caused by incorrect wiring to terminal S3 or a tripped external safety device."
pubDatetime: 2026-06-26T09:59:41Z
modDatetime: 2026-06-26T09:59:41Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa GA800 MFDI terminal block"
most_likely_cause: "Incorrect wiring to terminal S3"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Check if an external safety device (E-stop, overload relay) connected to terminal S3 is in a tripped or fault state and reset it"
  - "Verify parameter H1-01 is set to the correct External Fault value (2C through 2F) and matches the wiring scheme"
  - "Inspect the wiring to terminal S3 for loose connections, broken conductors, or shorts to ground"
no_buy_pct: "60%"
---

## Yaskawa GA800 EF3 Fault — What It Means

The GA800 displays EF3 (not F003) when the external fault input assigned to terminal S3 has been triggered. This fault appears when parameter H1-01 is configured to values 2C through 2F (External Fault) and the terminal detects a fault condition from a connected external device or wiring issue. Terminal S3 is a multi-function digital input (MFDI) that can be wired to safety relays, emergency stop circuits, or overload switches.

The fault tells you that either the external device connected to S3 is in a fault state, or the wiring to S3 does not match the parameter configuration (for example, a short-circuit fault when the drive expects an open-circuit fault). If terminal S3 is not being used for any external device, the fault usually indicates a wiring mistake or a false activation from electrical noise.

## Before You Replace Anything

Technicians sometimes replace the VFD main board when the real problem is a tripped safety relay or a loose wire at terminal S3. Always trace the external device wired to S3 and check its status before swapping control boards.

[Jump to Fix](#fix)

## Common Causes

- **Incorrect wiring to terminal S3 (~40%)** The wiring does not match the parameter configuration (open vs. short fault type), or a conductor is broken or miswired.
- **External safety device in fault state (~30%)** A safety relay, emergency stop circuit, or overload switch connected to S3 has tripped and is sending the fault signal to the drive.
- **Electrical noise or grounding issues (~15%)** Poor grounding or electrical noise causes the S3 input to fluctuate and falsely trigger the external fault.
- **S3 terminal not in use but configured as External Fault (~10%)** Parameter H1-01 is set to External Fault (2C through 2F) but no device is wired to S3, leaving the terminal floating and vulnerable to noise.
- **Mechanical coupling or encoder issue causing safety circuit trip (~5%)** A slipping encoder coupling or gearbox problem creates erratic feedback that causes an external safety circuit tied to S3 to trip.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is there an external safety device (E-stop, relay, overload switch) wired to terminal S3?</summary>
<div class="dtree-body"><strong>Yes:</strong> Check if that device is in a fault or tripped state and reset it. If it resets and the fault clears, the external device was the cause.<br><strong>No:</strong> The terminal S3 may be floating or miswired. Check parameter H1-01 and verify S3 is not configured for External Fault if no device is connected.</div>
</details>

<details class="dtree"><summary>Does the fault clear after you reset the external device and cycle the VFD reset?</summary>
<div class="dtree-body"><strong>Yes:</strong> The external device was the root cause. Investigate why it tripped (overload, mechanical fault, safety condition).<br><strong>No:</strong> Check wiring continuity and inspect for shorts, broken wires, or noise. Verify grounding is correct.</div>
</details>

<details class="dtree"><summary>Is the wiring to terminal S3 intact and do the continuity and fault type (open or short) match parameter H1-01?</summary>
<div class="dtree-body"><strong>Yes:</strong> Look for grounding issues, electrical noise, or a mechanical problem (slipping coupling, gearbox) that may be causing erratic behavior in the external circuit.<br><strong>No:</strong> Repair the wiring to match the configured fault type in H1-01, or reconfigure H1-01 to match the actual wiring scheme.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the VFD and lock out the main disconnect** to work safely on the drive and external wiring.
2. **Locate the external device connected to terminal S3** (safety relay, E-stop, overload switch) and check if it is in a fault or tripped state. Reset the device if needed.
3. **Verify the wiring schematic** for terminal S3 matches the drive manual and check for continuity, broken wires, or shorts to ground using a multimeter.
4. **Confirm parameter H1-01** is set to the correct External Fault value (2C through 2F) and that the fault type (open or short) matches the wiring. Consult your GA800 manual for the parameter table.
5. **Clear the fault** by cycling the VFD reset (keypad or reset input) once the external device is fixed and wiring is verified.
6. **Inspect grounding and shielding** of control wiring to rule out electrical noise. Perform a megger test on motor leads and the motor if the fault persists.
7. **Check mechanical components** (encoder coupling, gearbox, shaft alignment) if the fault reappears during operation, as a slipping coupling can cause erratic torque and trigger safety circuits tied to S3.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 MFDI terminal block | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f003-fault-code&k=Yaskawa+GA800+MFDI+terminal+block&tag=errorcodefixes-20) \| Only if the terminal block itself is damaged or corroded; consult your model's parts list for the exact replacement. |
| External safety relay or overload switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f003-fault-code&k=External+safety+relay+or+overload+switch&tag=errorcodefixes-20) \| If the device connected to S3 is failed and cannot be reset, replace it per the original equipment specification. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician if you cannot identify the external device connected to terminal S3, if wiring schematics are unclear, or if the fault persists after wiring and parameter checks. A pro should handle any high-voltage diagnostic work, grounding system upgrades, or megger testing of the motor and drive. If the fault appears during PID control or complex motion applications, the technician will need to inspect encoder feedback, mechanical couplings, and the entire control loop to rule out system-level issues that may be falsely triggering the external fault input.

**Rough cost:** A pro service call runs about $150-400 depending on wiring complexity and whether the external device needs repair.
