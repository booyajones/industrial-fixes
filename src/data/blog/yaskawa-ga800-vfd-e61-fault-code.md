---
title: "Yaskawa GA800 E61 Fault - Causes & Fix"
description: "E61 on a Yaskawa GA800 indicates a soft-charge precharge circuit abnormality. The most common fix is replacing the soft-charge bypass relay."
pubDatetime: 2026-06-06T11:46:22Z
modDatetime: 2026-06-06T11:46:22Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
most_likely_cause: "Stuck, worn, or failed soft-charge bypass relay or contactor inside the drive"
likelihood: "the most common cause"
diy_or_pro: "pro"
---

## Yaskawa GA800 E61 Fault — What It Means

The E61 fault on a Yaskawa GA800 drive signals a soft-charge answerback fault. This means the drive detected a problem with the precharge or soft-charge bypass relay circuit during startup. The drive expects to see the relay close and confirm its state during the power-up sequence. If that confirmation does not arrive, the drive throws E61 and will not proceed to normal operation.

The soft-charge circuit protects the drive by limiting inrush current during power-up. When the relay fails to operate correctly or the control board cannot read the relay's status, the drive cannot safely complete its startup and flags this fault.

## Before You Replace Anything

Technicians sometimes replace the entire control board before checking the precharge relay maintenance counter (U4-06). If U4-06 shows above 90%, the relay itself is worn out and either the board or drive must be replaced.

[Jump to Fix](#fix)

## Common Causes

- **Failed soft-charge bypass relay** The internal relay that switches the precharge resistor out of the circuit after startup becomes stuck, burned, or mechanically worn and does not close or report its state.
- **Control board failure** The board that drives the relay coil or reads the answerback contact has failed and cannot confirm the relay state even if the relay itself is working.
- **Precharge relay wear beyond maintenance threshold** The drive's internal maintenance counter U4-06 exceeds 90%, indicating the relay has reached end of life and must be replaced along with the board or drive.
- **Power cycle or transient startup fault** A temporary fault during drive re-energization that clears on restart but returns if underlying relay or board damage exists.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear immediately after you power-cycle the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The relay may have recovered from a transient condition. Monitor the drive and check parameter U4-06 to see if the precharge relay is nearing end of life.<br><strong>No:</strong> The relay or control board has a hardware failure that will not resolve without replacement. Proceed to check the maintenance counter and plan for parts replacement.</div>
</details>

<details class="dtree"><summary>Is parameter U4-06 (PreChargeRelayMainte) showing above 90%?</summary>
<div class="dtree-body"><strong>Yes:</strong> The precharge relay has exceeded its maintenance threshold. Replace the control board or the entire drive per Yaskawa guidance.<br><strong>No:</strong> The fault is likely in the relay hardware itself or the answerback circuit on the control board. Replacement of the board or drive is still required.</div>
</details>

<details class="dtree"><summary>Did the fault appear immediately after a long shutdown or power restoration?</summary>
<div class="dtree-body"><strong>Yes:</strong> Relay contacts may have oxidized or stuck during the idle period. Try one more power cycle, but if the fault returns the relay must be replaced.<br><strong>No:</strong> The fault developed during normal operation and points to component wear or control board failure rather than a transient event.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power off the drive** completely and wait 5 minutes for all DC bus capacitors to discharge before opening any covers.
2. **Re-energize the drive** and observe whether the E61 fault clears on its own after the startup sequence completes.
3. **Navigate to parameter U4-06** (PreChargeRelayMainte) in the drive's monitor menu and record the percentage value displayed.
4. **If U4-06 exceeds 90%**, plan to replace the control board or the entire drive, as the precharge relay has reached end of life and further operation will cause repeated faults.
5. **If the fault persists after restart and U4-06 is below 90%**, the soft-charge bypass relay or its answerback circuit on the control board has failed and requires board or drive replacement.
6. **Consult the drive's wiring diagram** and verify that no external contactor or interlock is preventing the soft-charge relay from receiving its control signal.
7. **Replace the control board or drive** according to Yaskawa service bulletins, as field repair of the internal relay circuit is not supported.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e61-fault-code&k=Yaskawa+GA800+control+board&tag=errorcodefixes-20) \| Match the board part number to your drive frame size and firmware revision. Required if U4-06 exceeds 90% or relay circuit fails. |
| Yaskawa GA800 variable frequency drive (complete unit) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e61-fault-code&k=Yaskawa+GA800+variable+frequency+drive+%28complete+unit%29&tag=errorcodefixes-20) \| Full drive replacement if control board replacement is not supported for your frame size or if repeated faults indicate deeper damage. |

## When to Call a Pro

Call a qualified technician or industrial electrician as soon as the E61 fault appears. This fault involves high-voltage DC bus circuits, internal relay diagnostics, and drive parameter monitoring that require specialized test equipment and training. Field repair of the soft-charge relay is not supported. The technician will read the precharge relay maintenance counter, verify the control board health, and replace the board or drive if the fault does not clear. Attempting to bypass or override the soft-charge circuit can destroy the drive's input rectifier and capacitors, resulting in a much more expensive failure.

**Rough cost:** A pro service call runs about $500-2000 depending on whether a control board or complete drive replacement is needed.
