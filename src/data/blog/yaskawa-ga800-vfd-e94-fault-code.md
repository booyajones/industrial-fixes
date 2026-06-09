---
title: "Yaskawa GA800 E94 Fault - Causes & Fix"
description: "E94 is not a verified GA800 code. Check for Uv3 (soft-charge relay fault). Most likely fix: replace the soft-charge bypass relay."
pubDatetime: 2026-06-07T10:29:51Z
modDatetime: 2026-06-07T10:29:51Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
most_likely_cause: "Soft-charge bypass relay or contactor failure"
likelihood: "the most common cause"
diy_or_pro: "pro"
---

## Yaskawa GA800 E94 Fault — What It Means

E94 does not appear in verified Yaskawa GA800 documentation. The GA800 uses a different fault-code nomenclature, and the code you see may be a misread or a display error. The confirmed GA800 fault that involves similar internal circuits is Uv3, which indicates a soft-charge answerback fault. This means the drive did not receive the expected signal from the soft-charge bypass relay or contactor after energizing. The soft-charge circuit limits inrush current to the DC bus capacitors during power-up, and the relay should close to bypass the charging resistor once the bus voltage is stable.

If your display shows E94, verify the exact characters on the keypad and consult your drive's manual or contact Yaskawa support with the model number, spec code, serial number, and a description of when the fault occurs. If the fault is actually Uv3, the drive has detected that the soft-charge relay did not respond correctly, which can happen when the relay contacts are worn, the coil has failed, or the control board is not sending or receiving the answerback signal.

## Before You Replace Anything

Technicians sometimes replace the entire control board when the fault is caused by a failed soft-charge relay. Test or swap the relay first before ordering a new board or drive.

[Jump to Fix](#fix)

## Common Causes

- **Soft-charge bypass relay worn or failed** The relay contacts may be pitted or the coil open, preventing the answerback signal from reaching the control board.
- **Soft-charge contactor damaged** If your drive uses a contactor instead of a relay, mechanical wear or coil failure will produce the same fault.
- **Control board not sending or receiving answerback** A fault in the board's relay driver circuit or input conditioning can prevent proper soft-charge sequencing.
- **Wiring or connector issue in the soft-charge circuit** Loose terminals, broken wires, or corroded connectors between the relay and the control board interrupt the answerback signal.
- **Incorrect drive parameter or configuration** Some drives allow soft-charge timeout or bypass settings that, if misconfigured, can trigger a fault on power-up.
- **Power supply or DC bus capacitor degradation** If the DC bus does not charge quickly enough, the drive may time out waiting for the soft-charge relay to close.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault appear immediately every time you power up the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The soft-charge circuit is likely failing during the power-on sequence. Inspect the soft-charge relay and wiring first.<br><strong>No:</strong> The fault may be intermittent due to a relay nearing end-of-life or a loose connection. Monitor the relay maintenance counter if available and check all terminals.</div>
</details>

<details class="dtree"><summary>Can you hear or see the soft-charge relay click when you apply power?</summary>
<div class="dtree-body"><strong>Yes:</strong> The relay coil is energizing but the contacts may not be closing reliably. Test contact continuity or replace the relay.<br><strong>No:</strong> The relay coil is not being driven or has failed open. Check the control board relay-driver output and coil resistance.</div>
</details>

<details class="dtree"><summary>After clearing the fault and re-energizing, does the drive run normally?</summary>
<div class="dtree-body"><strong>Yes:</strong> The issue may be transient or related to a weak relay that works after warming up. Replace the relay as a preventive measure.<br><strong>No:</strong> The fault persists, pointing to a control board issue or a completely failed relay. Replace the relay first, then the control board if needed.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Lock out and tag out all power** to the drive and verify zero voltage at the input terminals with a multimeter.
2. **Record the exact fault code** displayed on the keypad and verify it matches E94 or Uv3. Take a photo if possible and note the drive model, spec code, and serial number from the nameplate.
3. **Locate the soft-charge bypass relay or contactor** inside the drive enclosure. Consult the drive's service manual or internal wiring diagram to identify the component and its connections.
4. **Inspect the relay for visible damage** such as burnt contacts, melted coil housing, or loose terminals. Check all wiring and connectors leading to the relay for corrosion or breaks.
5. **Measure the relay coil resistance** with a multimeter when the drive is de-energized. Compare the reading to the relay datasheet or a known good relay. An open coil indicates relay failure.
6. **Test the relay contacts** for continuity in both the de-energized and energized states, or substitute a known-good relay of the same specification and rating.
7. **Replace the soft-charge relay** with an identical part number if testing shows a fault. Torque all terminals to the manufacturer's specification and dress wiring away from high-voltage bus bars.
8. **Re-energize the drive** and observe the power-up sequence. If the fault clears and the drive runs normally, the repair is complete. If the fault persists, replace the control board or contact Yaskawa support for further diagnostics.
9. **Document the repair** including the fault code, test results, parts replaced, and any maintenance counter values. Update your preventive maintenance schedule to inspect the relay periodically.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Soft-charge bypass relay | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e94-fault-code&k=Soft-charge+bypass+relay&tag=errorcodefixes-20) \| Match the coil voltage, contact rating, and terminal configuration to the original relay on your drive model. |
| Control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e94-fault-code&k=Control+board&tag=errorcodefixes-20) \| Order by the drive's complete model and spec code. Required only if replacing the relay does not clear the fault. |

## When to Call a Pro

Call a qualified drives technician or an authorized Yaskawa service center if you cannot verify the exact fault code from your manual, if the relay and wiring appear intact but the fault persists, or if you are not trained to work safely inside energized or high-voltage industrial equipment. The repair requires lockout-tagout procedures, multimeter testing of relay circuits, and access to internal components near the DC bus, which can hold lethal voltage even after input power is removed. A technician will also gather detailed failure information, check the drive's maintenance counters, and determine whether the control board or the entire drive needs replacement if the relay is not the root cause.

**Rough cost:** A pro service call runs about $200-600.
