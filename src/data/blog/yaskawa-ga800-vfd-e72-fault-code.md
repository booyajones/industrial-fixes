---
title: "Yaskawa GA800 E72 Fault - Causes & Fix"
description: "E72 on a Yaskawa GA800 means the soft-charge bypass relay did not answer back as expected. Inspect relay contacts and control board."
pubDatetime: 2026-06-07T10:13:10Z
modDatetime: 2026-06-07T10:13:10Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
most_likely_cause: "Worn or damaged soft-charge bypass relay contacts or coil"
likelihood: "the most common cause"
diy_or_pro: "pro"
money_part: "Yaskawa GA800 control board"
---

## Yaskawa GA800 E72 Fault — What It Means

E72 is a soft-charge bypass relay answerback fault. When the GA800 drive starts up, it energizes a relay or contactor that bypasses the soft-charge circuit after the DC bus reaches operating voltage. The drive expects feedback (an answerback signal) confirming the relay has closed. If that signal does not arrive or does not match what the drive expects, the E72 fault trips.

The fault points to a mismatch between commanded and actual relay state. It can be caused by worn relay contacts, a failed relay coil, a control board problem affecting either the relay drive circuit or the answerback sensing circuit, or a wiring issue in the feedback path. The GA800 maintenance manual limits field repair to fan and control board replacement, so deeper component-level board diagnostics typically require factory service or a drive replacement.

## Before You Replace Anything

Technicians sometimes replace the entire drive before checking the soft-charge bypass relay maintenance status in parameter U4-06. If U4-06 reads above 90%, replace the control board or the relay circuit first before swapping the entire drive.

[Jump to Fix](#fix)

## Common Causes

- **Worn bypass relay contacts** Contacts in the soft-charge bypass relay or contactor degrade over time and no longer close reliably, preventing the answerback signal.
- **Failed relay coil** The coil that energizes the bypass relay has opened or become too resistive to pull in the contacts.
- **Control board relay driver failure** The circuit on the control board that energizes the bypass relay has failed, so the relay never closes.
- **Answerback sensing circuit fault** The control board circuit that reads the relay feedback signal has failed, even though the relay is operating correctly.
- **Broken or loose answerback wiring** The wire carrying the relay feedback signal to the control board is broken, loose, or corroded.
- **High relay maintenance counter** Parameter U4-06 (PreChargeRelayMainte) has exceeded 90%, indicating the relay has cycled beyond its expected service life.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the E72 fault clear after you cycle power to the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The relay may have closed intermittently. Monitor parameter U4-06 and watch for the fault to return. If U4-06 is above 90%, schedule relay or board replacement soon.<br><strong>No:</strong> The relay or control board circuit has likely failed. Proceed to check parameter U4-06 and inspect the bypass relay circuit.</div>
</details>

<details class="dtree"><summary>Is parameter U4-06 (PreChargeRelayMainte) above 90%?</summary>
<div class="dtree-body"><strong>Yes:</strong> The relay is at end of life. Replace the control board, the relay assembly, or the entire drive per the manufacturer troubleshooting chart.<br><strong>No:</strong> The relay itself is not worn out. Inspect wiring to the relay coil and answerback terminals, then check the control board relay driver and feedback circuits.</div>
</details>

<details class="dtree"><summary>Do you measure coil voltage at the bypass relay when the drive attempts to start?</summary>
<div class="dtree-body"><strong>Yes:</strong> The control board relay driver is working. The problem is in the relay itself (coil or contacts) or in the answerback wiring or sensing circuit.<br><strong>No:</strong> The control board is not energizing the relay. Replace the control board or check for an open in the wiring between the board and the relay coil.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and lock out the incoming supply per NFPA 70E and your site electrical safety procedures.
2. **Cycle power to the drive** and attempt a restart to see if the E72 fault clears on its own, indicating an intermittent relay issue.
3. **Navigate to parameter U4-06** (PreChargeRelayMainte) in the drive display and record the value. If it is above 90%, the relay has exceeded its design cycle life.
4. **Locate the soft-charge bypass relay or contactor** inside the drive enclosure. Consult the GA800 wiring diagram for your frame size to identify the relay terminals.
5. **Inspect the relay coil terminals** for tight connections and measure coil resistance. Compare to any values on the relay nameplate or GA800 service notes. If the coil is open or far out of range, replace the relay.
6. **Check the answerback feedback wiring** from the relay auxiliary contact back to the control board. Look for broken, loose, or corroded connections.
7. **If wiring and relay check good but the fault persists**, replace the control board. The GA800 maintenance manual limits field repair to fan and control board replacement components. If a new control board does not resolve E72, replace the entire drive.
8. **Clear the fault**, restart the drive, and verify normal operation under load. Monitor U4-06 over the next few weeks to confirm the repair has resolved the answerback issue.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e72-fault-code&k=Yaskawa+GA800+control+board&tag=errorcodefixes-20) \| Order by exact drive model and frame size. The control board houses the relay driver and answerback sensing circuits. |
| Soft-charge bypass relay or contactor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e72-fault-code&k=Soft-charge+bypass+relay+or+contactor&tag=errorcodefixes-20) \| Consult the GA800 parts list for your frame to get the correct relay voltage and contact rating. |

## When to Call a Pro

Call a qualified variable-frequency drive technician or an authorized Yaskawa service center for an E72 fault. The repair requires working inside the drive enclosure with high DC bus voltage present even after AC power is removed. Diagnosing the soft-charge bypass relay circuit involves interpreting the drive's internal wiring, measuring coil and feedback signals, and replacing control boards or relays that are not stocked at most electrical distributors. The GA800 maintenance manual explicitly states that repairs beyond fan and control board replacement are outside the scope of field service, so persistent E72 faults after basic troubleshooting usually require factory-level diagnostics or a complete drive replacement. Do not attempt this repair unless you are trained in VFD service and have appropriate PPE and lockout/tagout procedures in place.

**Rough cost:** A pro service call runs about $400–1,200 depending on whether a control board, relay assembly, or complete drive replacement is required.
