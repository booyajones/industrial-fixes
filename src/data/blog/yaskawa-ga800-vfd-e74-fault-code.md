---
title: "Yaskawa GA800 E74 Fault Code - Causes & Fix"
description: "E74 on the GA800 may indicate a soft-charge bypass relay fault. Most common fix: re-energize the drive and check relay maintenance indicator."
pubDatetime: 2026-06-07T10:14:35Z
modDatetime: 2026-06-07T10:14:35Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
most_likely_cause: "Damaged soft-charge bypass relay or contactor"
likelihood: "the most common cause"
diy_or_pro: "pro"
---

## Yaskawa GA800 E74 Fault Code — What It Means

The E74 fault code is not explicitly documented in the available GA800 troubleshooting materials. However, the GA800 commonly displays faults related to the soft-charge bypass relay and contactor feedback path, labeled as Uv3 in Yaskawa documentation. This type of fault occurs when the drive detects a problem with the soft-charge answerback circuit, which is responsible for verifying that the pre-charge relay has properly energized before switching the main contactor. The fault typically points to damage or failure in the relay or contactor on the soft-charge bypass circuit.

Because E74 is not a standard GA800 code in the provided reference materials, verify the exact fault code displayed on your keypad or in the alarm history screen. If your display shows Uv3 or references soft-charge, the troubleshooting steps below apply. If the code is definitively E74, consult your drive's maintenance manual or contact Yaskawa technical support for model-specific guidance, as fault code definitions can vary between firmware revisions and drive configurations.

## Before You Replace Anything

Technicians sometimes replace the entire control board without first checking the pre-charge relay maintenance indicator at parameter U4-06. If the indicator reads below 90%, simply re-energizing the drive can clear the fault and save the cost of a board replacement.

[Jump to Fix](#fix)

## Common Causes

- **Failed soft-charge bypass relay** The relay on the soft-charge circuit has worn out or sustained contact damage and no longer provides proper answerback feedback to the control board.
- **Damaged soft-charge contactor** The contactor paired with the bypass relay has failed, preventing the drive from verifying successful pre-charge of the DC bus capacitors.
- **Control board fault** The control board itself has sustained damage in the soft-charge monitoring circuit, causing false fault detection even when the relay is functional.
- **High relay maintenance indicator** The pre-charge relay maintenance counter at parameter U4-06 has exceeded 90 percent, indicating the relay has reached end of life and requires replacement.
- **Power supply transient** A momentary power disruption or line transient has caused the drive to lose answerback signal during the pre-charge sequence.
- **Wiring or connection issue** Loose or corroded wiring in the soft-charge feedback path prevents the drive from receiving the relay status signal.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear after you cycle power to the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was likely a transient event. Monitor the drive for recurrence and log the event. If it reappears frequently, proceed to check the relay maintenance indicator.<br><strong>No:</strong> The fault is persistent. Proceed to check parameter U4-06 for the pre-charge relay maintenance indicator value.</div>
</details>

<details class="dtree"><summary>Is the pre-charge relay maintenance indicator (U4-06) above 90 percent?</summary>
<div class="dtree-body"><strong>Yes:</strong> The relay has reached its service life and the board or drive assembly requires replacement per Yaskawa guidance.<br><strong>No:</strong> The relay should still be serviceable. Inspect wiring to the soft-charge relay and contactor for loose connections or damage, then test the relay coil and contacts.</div>
</details>

<details class="dtree"><summary>Do you have access to the drive's alarm history to confirm the exact fault code?</summary>
<div class="dtree-body"><strong>Yes:</strong> Review the alarm history screen to verify whether the code is E74, Uv3, or another designation, then cross-reference it with your drive's manual or contact Yaskawa support.<br><strong>No:</strong> Document the displayed code exactly as it appears on the keypad and consult the GA800 maintenance manual or Yaskawa technical support to confirm the fault definition before ordering parts.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off and lock out power** to the drive at the main disconnect, then wait at least five minutes for the DC bus capacitors to discharge fully before opening any panels.
2. **Re-energize the drive** and observe whether the fault clears on its own. Some soft-charge faults are transient and will reset after a power cycle.
3. **Navigate to parameter U4-06** on the keypad to check the pre-charge relay maintenance indicator. Record the percentage value displayed.
4. **If the indicator is above 90 percent**, the relay has reached end of life. Follow Yaskawa guidance to replace the control board or the entire drive assembly, depending on your drive model and warranty status.
5. **If the indicator is below 90 percent**, inspect the soft-charge bypass relay and contactor for physical damage, burnt contacts, or loose wiring connections. Use a multimeter to verify relay coil resistance and contact continuity.
6. **Replace the soft-charge relay or contactor** if testing reveals failure. If no component-level fault is found, the control board may have sustained damage and should be replaced.
7. **Clear the fault** from the drive's alarm history, restore power, and run the drive under load while monitoring for recurrence. Log the event and schedule follow-up inspection if intermittent faults continue.

## Parts Often Needed

| Part | Notes |
|------|-------|
| GA800 soft-charge bypass relay | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e74-fault-code&k=GA800+soft-charge+bypass+relay&tag=errorcodefixes-20) \| Verify the exact relay part number for your GA800 horsepower and frame size from the maintenance manual or Yaskawa parts department. |
| GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e74-fault-code&k=GA800+control+board&tag=errorcodefixes-20) \| Required if the pre-charge relay maintenance indicator exceeds 90 percent or if relay replacement does not clear the fault. Confirm board revision and model compatibility before ordering. |

## When to Call a Pro

Call a qualified drives technician or Yaskawa authorized service center if you do not have experience working with high-voltage DC bus circuits, if the pre-charge relay maintenance indicator is above 90 percent and you are unsure which board or drive assembly to order, or if the fault persists after relay replacement. VFD troubleshooting requires proper lockout/tagout procedures, capacitor discharge verification, and familiarity with parameter navigation. Because the E74 code is not explicitly documented in standard GA800 materials, professional diagnosis ensures you receive the correct part and avoid unnecessary board replacements. If your facility does not have a qualified electrician or drives specialist on staff, contact Yaskawa technical support with your drive model number, serial number, and alarm history before ordering parts.

**Rough cost:** A pro service call runs about $400-1200 depending on whether relay replacement or full board/drive replacement is required.
