---
title: "Siemens Micromaster F0090 - Causes & Fix"
description: "F0090 means encoder feedback loss on Siemens Micromaster VFDs. Most often caused by loose encoder wiring or wrong P0400 configuration."
pubDatetime: 2026-06-24T09:59:40Z
modDatetime: 2026-06-24T09:59:40Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Encoder cable (shielded)"
most_likely_cause: "Loose or broken encoder cable connections"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Check r0949 to identify whether the fault is configuration (5), hardware detection (6), or signal loss (0)"
  - "Inspect all encoder cable connections at both the motor and drive terminals for loose or corroded contacts"
  - "Verify P0400 is set to the correct encoder type (e.g., 1 for TTL, 2 for SinCos) and matches the control mode in P1300"
no_buy_pct: "60%"
---

## What this code means
The F0090 fault indicates the drive cannot receive the expected speed or position signal from the encoder connected to the motor. The specific reason is detailed in monitor parameter r0949. When r0949 shows 0, the encoder signal is physically lost. When r0949 shows 5, the encoder is not configured in parameter P0400 even though the drive is set for sensored control (P1300 = 21 or 23). When r0949 shows 6, the encoder module hardware is not found by the drive, even though it is configured in P0400.

This fault only appears on systems using an encoder for closed-loop speed or position control. The drive expects continuous pulse feedback from the encoder and will trip F0090 when that signal drops below the threshold set in parameter P0492 or when the hardware chain is incomplete.

## Before You Replace Anything

Technicians often replace the encoder module or entire drive when the fault is actually a misconfigured P0400 parameter or a loose terminal. Always check r0949 first and verify P0400 matches your encoder type before swapping hardware.

## Common Causes

- **Loose or broken encoder cable (~35%)** Physical disconnection, broken wires, loose terminals, or damaged connectors between the encoder and the inverter interrupt the pulse train.
- **Encoder not configured in P0400 (~25%)** The drive is set for sensored control (P1300 = 21 or 23) but P0400 does not match the installed encoder type, triggering r0949 = 5.
- **Encoder module hardware not detected (~15%)** The encoder input module on the drive has failed or is not seated properly, so the drive cannot find the hardware even though P0400 is configured, triggering r0949 = 6.
- **Electrical noise on encoder cable (~15%)** Poorly shielded cables or lack of grounding allow electrical interference to drown out the encoder pulse signal.
- **Defective encoder (~10%)** The encoder itself has failed internally and no longer generates a valid pulse train.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does r0949 show a value of 5?</summary>
<div class="dtree-body"><strong>Yes:</strong> The encoder is not configured in P0400. Set P0400 to match your encoder type (1 for TTL, 2 for SinCos) and reset the fault.<br><strong>No:</strong> Move to the next check.</div>
</details>

<details class="dtree"><summary>Does r0949 show a value of 6?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive cannot find the encoder module hardware. Reseat the encoder input card or module and check for internal connection faults.<br><strong>No:</strong> Move to the next check.</div>
</details>

<details class="dtree"><summary>Do you see continuity on all encoder cable conductors when the motor and drive are de-energized?</summary>
<div class="dtree-body"><strong>Yes:</strong> The cable is intact. The encoder itself may be defective or the signal is too weak. Test the encoder or increase P0492 threshold.<br><strong>No:</strong> Repair or replace the encoder cable and make sure shielded cable is grounded at one end only.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Check r0949** on the drive display or via the keypad to determine if the fault is configuration (5), hardware detection (6), or signal loss (0).
2. **Verify P0400 and P1300** match your system. If r0949 = 5, set P0400 to the correct encoder type (1 for TTL, 2 for SinCos). make sure P1300 control mode (21 or 23 for sensored vector) is appropriate for your encoder setup.
3. **Inspect encoder cable** from motor to drive. Check for broken wires, loose terminals, damaged connectors, and continuity on all conductors. Replace damaged cable with properly shielded encoder cable and ground the shield at the drive end only.
4. **Test encoder health** by temporarily switching P1300 to 0 (V/f control) or 20/22 (sensorless vector) and running the motor at a fixed speed. Monitor r0061 (speed feedback) to see if the drive detects any signal. If r0061 is zero, the encoder is likely failed.
5. **Reseat encoder module** if r0949 = 6. Power down the drive, remove and reinstall the encoder input card or module, and check internal connectors.
6. **Adjust P0492 threshold** if the encoder signal is weak but present. Increase the encoder loss threshold value to prevent premature faulting from marginal signals.
7. **Clear fault memory** using P0952 and power cycle the drive to confirm the repair.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Encoder cable (shielded) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0090-fault-code&k=Encoder+cable+%28shielded%29&tag=errorcodefixes-20) \| Match the pin count and connector type to your motor and drive model. |
| Replacement encoder | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0090-fault-code&k=Replacement+encoder&tag=errorcodefixes-20) \| Verify encoder type (TTL, SinCos, resolver) and pulse-per-revolution rating matches the original. |
| Encoder input module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0090-fault-code&k=Encoder+input+module&tag=errorcodefixes-20) \| For Micromaster 440 and similar models with plug-in encoder cards. |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not trained in VFD parameter programming or encoder wiring. Incorrect encoder configuration can cause runaway motor conditions or damage to the drive and motor. If you have verified wiring and configuration but the fault persists, a technician with a scope can test encoder pulse quality and diagnose internal drive failures. Work on VFDs involves high DC bus voltage even when AC input is off, so always follow lockout-tagout and wait for the DC bus capacitors to discharge before opening the unit.

**Rough cost:** A pro service call runs about $150-400 depending on whether the fix is wiring repair or encoder replacement.
