---
title: "Yaskawa GA800 E79 - Causes & Fix"
description: "E79 means the Safe Torque Off (STO) safety circuit is open or missing. Most common fix: restore the factory STO jumper if no safety relay is used."
pubDatetime: 2026-06-07T10:18:07Z
modDatetime: 2026-06-07T10:18:07Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
most_likely_cause: "Missing or removed factory STO jumper with no external safety circuit wired in its place"
likelihood: "the most common cause"
diy_or_pro: "pro"
---

## Yaskawa GA800 E79 — What It Means

The E79 fault on the Yaskawa GA800 VFD is a Safe Torque Off (STO) safety input related alarm. It means the drive has detected that the STO safety circuit is open, not satisfied, or inconsistent with the expected state. The STO function is a built-in safety feature that prevents torque production to the motor even while main input power remains applied. When the STO inputs or their required jumper or safety relay path are not in the correct state, the drive will not allow operation and will report this safety condition.

This is not a motor overload or overcurrent fault. Instead, the drive is telling you that the safety interlock circuit is incomplete or interrupted, so torque production is inhibited as a protective measure. The fault will persist until the STO circuit is properly closed or restored to the configuration the drive expects.

## Before You Replace Anything

Technicians sometimes suspect the drive control board is faulty and replace the entire VFD. Before doing that, carefully inspect the STO terminal jumper and verify the safety relay outputs are actually closing, which costs nothing and resolves the majority of E79 faults.

[Jump to Fix](#fix)

## Common Causes

- **Factory STO jumper removed** The drive shipped with a jumper across the STO terminals, and it was removed during installation without wiring an external safety circuit.
- **Safety relay output not closing** One or both STO channels are not receiving the correct safety relay output because the relay is not energized or not reset.
- **Loose or miswired STO terminals** Loose, missing, or incorrectly wired terminals in the STO loop, including the safety relay feedback path.
- **Upstream safety chain fault** An E-stop button, gate switch, light curtain, or other upstream safety device in the machine safety system is open or faulted, keeping the STO circuit open.
- **Incorrect STO terminal function assignment** Drive parameters were reinitialized or changed, and the STO-related terminal function assignments no longer match the installed wiring.
- **Failed STO input circuitry** Internal safety input circuit on the drive has failed and cannot detect a closed STO loop even when wiring is correct.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is there a wire jumper or plug installed across the STO input terminals on the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The jumper is present, so the issue is likely a loose connection, incorrect wiring, or a fault upstream in an external safety relay circuit. Proceed to verify safety relay outputs and wiring continuity.<br><strong>No:</strong> The jumper is missing. If this drive is not integrated with an external safety system, reinstall the factory STO jumper and reset the fault. If the drive is part of a safety system, verify the safety relay outputs are wired correctly and the relay is energized.</div>
</details>

<details class="dtree"><summary>Is the drive connected to an external safety relay or safety controller?</summary>
<div class="dtree-body"><strong>Yes:</strong> Check that the safety relay is energized and its output contacts are closed. Verify that no E-stop, gate, or other upstream safety device is open. Measure continuity through the entire safety chain to the STO terminals.<br><strong>No:</strong> The drive should have the factory STO jumper installed. If the jumper is missing, install it. If the jumper is present and the fault persists, inspect for loose terminals or contact the manufacturer for service.</div>
</details>

<details class="dtree"><summary>Does the fault clear after you reset the drive and verify all STO wiring is tight and correct?</summary>
<div class="dtree-body"><strong>Yes:</strong> The issue was a temporary open circuit or loose connection. Monitor the drive during operation to confirm the fault does not return.<br><strong>No:</strong> The STO input circuit on the drive may be damaged, or there is an intermittent fault in the safety relay or upstream safety device. Call a qualified technician or the manufacturer for diagnostics.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the exact fault code** displayed on the GA800 keypad and confirm it is E79 and not a different alarm or fault number.
2. **Inspect the STO terminal block** on the drive and check whether the factory jumper is still installed if the drive is not connected to an external safety system.
3. **If the jumper is missing and no safety circuit is used**, reinstall the factory STO jumper across the designated STO input terminals and proceed to reset the fault.
4. **If an external safety relay is installed**, verify the safety relay is energized and that both STO channel outputs are closed and delivering the correct signal to the drive.
5. **Check all STO wiring** for loose terminals, broken conductors, incorrect terminal assignments, or swapped channels between the safety relay and the drive.
6. **Trace the upstream safety chain** including E-stop buttons, gate switches, light curtains, and any other safety interlocks to confirm none are open or faulted.
7. **Reset the drive fault** using the keypad or parameter reset function, then attempt a test run to verify the STO circuit is satisfied and the drive operates normally.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 STO jumper | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e79-fault-code&k=Yaskawa+GA800+STO+jumper&tag=errorcodefixes-20) \| Factory-supplied jumper for STO terminals when no external safety circuit is used. Often part of the original drive accessory kit. |
| Safety relay compatible with GA800 STO | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e79-fault-code&k=Safety+relay+compatible+with+GA800+STO&tag=errorcodefixes-20) \| Dual-channel safety relay for machine integration. Must match the drive's STO input voltage and contact rating. |

## When to Call a Pro

Call a qualified electrician or automation technician if you are not familiar with VFD wiring, safety circuit design, or machine safety standards. The STO function is a safety-critical circuit, and incorrect wiring can create a hazard or violate safety regulations. If the drive was integrated into a machine safety system and you cannot identify which upstream device is causing the fault, a technician with access to the machine wiring diagrams and safety relay documentation is required. If the STO jumper is correctly installed or the safety relay outputs are verified closed and the fault still persists, the drive's internal STO input circuit may be damaged and will need manufacturer service or replacement.

**Rough cost:** A pro service call runs about $150-400.
