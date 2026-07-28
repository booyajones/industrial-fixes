---
title: "Yaskawa GA800 E70 Fault - Causes & Fix"
description: "E70 means soft-charge answerback fault: the precharge bypass relay did not confirm it switched. Re-energize the drive first."
pubDatetime: 2026-06-07T10:11:37Z
modDatetime: 2026-06-07T10:11:37Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
most_likely_cause: "Damaged or worn soft-charge bypass relay or contactor"
likelihood: "the most common cause"
diy_or_pro: "pro"
money_part: "Yaskawa GA800 control board"
---

## What this code means
E70 on a Yaskawa GA800 is a soft-charge answerback fault. The drive did not receive the expected feedback that the precharge (soft-charge) bypass relay changed state correctly during startup. This points to a problem in the relay circuit, the control board, or the drive itself. The precharge relay is used to limit inrush current when the drive powers up, and the drive monitors a feedback signal to confirm the relay has closed or opened as commanded. When that signal does not match what the drive expects, it throws E70 and shuts down to protect itself.

The fault usually means the relay has failed, the control board has lost the ability to drive or read the relay feedback, or internal drive circuitry has failed. Yaskawa GA800 maintenance documentation tracks the relay's operational life in parameter U4-06 (PreChargeRelayMainte), and if that counter exceeds 90%, the board or drive should be replaced. Because the precharge circuit is internal to the drive and tied to high-voltage DC bus components, field repair beyond board replacement is not recommended.

## Before You Replace Anything

Technicians sometimes replace the entire drive when only the control board has failed. Check parameter U4-06 first to see if the relay maintenance counter is over 90%, which confirms relay wear and points to board or drive replacement rather than guessing at other causes.

## Common Causes

- **Failed soft-charge bypass relay or contactor** The relay that switches the precharge resistor in and out of the circuit has worn out or is stuck, so the drive cannot confirm the relay changed state.
- **Control board failure** The control board has lost the ability to drive the relay coil or read the feedback signal, even though the relay itself may still be good.
- **Drive internal failure** Internal circuitry or the DC bus precharge circuit has failed, and the fault persists even after power cycling and board checks.
- **High relay maintenance counter (U4-06 > 90%)** The drive tracks relay operations in parameter U4-06, and when the counter exceeds 90% the relay or board has reached end of service life.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the E70 fault clear after you power down the drive completely for 30 seconds and re-energize it?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was transient, possibly from electrical noise or a momentary relay glitch. Monitor the drive and check parameter U4-06 to see if the relay is nearing maintenance life.<br><strong>No:</strong> The fault is persistent. Move on to check the relay maintenance counter and inspect the control board or relay circuit.</div>
</details>

<details class="dtree"><summary>Is parameter U4-06 (PreChargeRelayMainte) over 90%?</summary>
<div class="dtree-body"><strong>Yes:</strong> The soft-charge bypass relay has reached its service life. Replace the control board or the entire drive per Yaskawa guidance.<br><strong>No:</strong> The relay counter is still good, so the fault is likely a failed relay, bad feedback wiring, or control board issue rather than normal wear. Proceed to board and relay inspection.</div>
</details>

<details class="dtree"><summary>Do you have access to the drive's elementary diagram and can you measure continuity and voltage on the relay feedback circuit?</summary>
<div class="dtree-body"><strong>Yes:</strong> Use the diagram to trace the relay feedback signal and check for open circuits, failed relay coil, or missing feedback voltage. Replace the relay or control board as needed.<br><strong>No:</strong> Without the diagram and metering equipment, you cannot safely diagnose the internal relay circuit. Call a qualified VFD technician or contact Yaskawa support.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive completely** and wait at least 30 seconds for the DC bus capacitors to discharge and the drive to reset.
2. **Re-energize the drive** and observe whether the E70 fault clears on its own. If the fault does not reappear, the issue may have been transient.
3. **Check parameter U4-06 [PreChargeRelayMainte]** in the drive's maintenance menu to see the soft-charge bypass relay life percentage. If U4-06 is over 90%, the relay has reached its service life.
4. **Replace the control board or the entire drive** if U4-06 is over 90%, per Yaskawa maintenance guidance. Consult your model's service manual for the correct control board part number.
5. **Inspect the soft-charge bypass relay and contactor** if U4-06 is below 90%. Use the drive's elementary diagram to locate the relay, check for visible damage, burned contacts, or loose connections, and measure coil resistance and feedback signal continuity.
6. **Replace the control board** if the relay tests good but the fault persists, since the board drives the relay and reads the feedback signal.
7. **Contact Yaskawa technical support or a qualified VFD service center** if the fault remains after board replacement or if you do not have access to the elementary diagram and test equipment, as internal drive circuitry may have failed.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e70-fault-code&k=Yaskawa+GA800+control+board&tag=errorcodefixes-20) \| Match the board part number to your specific GA800 model and frame size. Board replacement often resolves E70 when U4-06 is over 90% or feedback circuitry has failed. |
| Soft-charge bypass relay or contactor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e70-fault-code&k=Soft-charge+bypass+relay+or+contactor&tag=errorcodefixes-20) \| Internal component, part of the precharge circuit. Replacement typically requires control board removal or full drive service. Consult the drive's elementary diagram for location and part number. |

## When to Call a Pro

Call a qualified VFD technician or Yaskawa service center if the fault persists after power cycling, if parameter U4-06 is over 90% and you are not trained to replace the control board or drive, or if you do not have the drive's elementary diagram and metering tools to safely diagnose the relay feedback circuit. The precharge circuit operates at high DC bus voltage and incorrect handling can damage the drive or cause electrical shock. If the fault does not clear after board replacement, internal drive circuitry has likely failed and the drive must be replaced or sent for factory repair.

**Rough cost:** A pro service call runs about $300–900 for control board replacement or drive replacement, depending on model and labor.
