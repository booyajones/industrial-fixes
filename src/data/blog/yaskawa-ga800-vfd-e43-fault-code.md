---
title: "Yaskawa GA800 E43 Fault - Causes & Fix"
description: "E43 on a Yaskawa GA800 is a soft-charge relay answerback fault. The most common fix is replacing the soft-charge bypass relay or control board."
pubDatetime: 2026-06-06T11:31:53Z
modDatetime: 2026-06-06T11:31:53Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
most_likely_cause: "Worn or stuck soft-charge bypass relay"
likelihood: "the most common real cause"
diy_or_pro: "pro"
money_part: "Yaskawa GA800 control board (PCB)"
---

## Yaskawa GA800 E43 Fault — What It Means

The E43 fault on a Yaskawa GA800 VFD indicates a soft-charge or bypass relay answerback failure. During power-up, the drive expects the soft-charge bypass relay to change state and send back a feedback signal confirming the relay has switched correctly. When the drive does not see the expected relay response, it shuts down and reports E43. This points to a problem in the relay itself, the feedback wiring path, or the control board circuitry that commands and monitors the relay.

The soft-charge circuit is part of the drive's DC bus pre-charge sequence, which limits inrush current when the drive first energizes. A failed relay, stuck contacts, burned connections, or a control board that can no longer drive or read the relay will all trigger this fault. The GA800 also tracks relay life in parameter U4-06 (PreChargeRelayMainte), and Yaskawa guidance states that when U4-06 exceeds 90%, the relay, board, or drive should be replaced.

## Before You Replace Anything

Technicians sometimes replace the entire drive before checking relay life parameter U4-06 or inspecting the relay contacts and wiring for heat damage or loose connections.

[Jump to Fix](#fix)

## Common Causes

- **Worn or stuck soft-charge bypass relay** Repeated power cycles wear relay contacts until they no longer close or open cleanly, blocking the answerback signal the drive expects.
- **Failed control board relay-drive circuit** The control board circuitry that energizes the relay or reads its feedback can fail, even when the relay itself is intact.
- **Loose or burned relay wiring connections** Heat, vibration, or poor torque on terminals in the relay feedback path creates intermittent or open circuits that prevent the drive from seeing the relay state.
- **Relay life counter above 90%** Parameter U4-06 tracks relay cycles, and Yaskawa troubleshooting guidance recommends replacement when this counter exceeds 90%.
- **Damaged board-to-board connectors** Internal connectors linking the control board to the relay circuit can crack, corrode, or unseat, breaking the feedback loop.
- **Power surge or transient event** Lightning, line voltage spikes, or switching transients can damage the relay coil, contacts, or board traces in the soft-charge circuit.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault appear every time you power the drive, or only once?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is repeatable and points to a permanent relay, wiring, or board failure. Proceed with inspection and testing.<br><strong>No:</strong> A one-time E43 can be a transient event. Monitor the drive, but if it does not recur, no repair may be needed.</div>
</details>

<details class="dtree"><summary>Is parameter U4-06 (PreChargeRelayMainte) above 90%?</summary>
<div class="dtree-body"><strong>Yes:</strong> The relay has reached end-of-life according to Yaskawa. Replace the relay assembly or control board per the manufacturer's service guidelines.<br><strong>No:</strong> The relay life counter is still acceptable. Focus on inspecting physical relay condition, wiring, and connections.</div>
</details>

<details class="dtree"><summary>Do you see heat discoloration, arcing marks, or loose terminals on the relay or wiring?</summary>
<div class="dtree-body"><strong>Yes:</strong> Physical damage is present. Replace the damaged relay, connectors, or wiring as needed, then re-test the drive.<br><strong>No:</strong> No visible damage suggests an internal control-board fault. Replace the control board or consult Yaskawa service for drive replacement.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect all power** and lock out the drive at the upstream disconnect or breaker before opening any covers.
2. **Wait for DC bus capacitors to discharge** per the GA800 manual (typically five minutes minimum), then verify zero voltage with a meter.
3. **Power the drive back on** and observe whether E43 appears immediately or if the drive starts normally. Record whether the fault is repeatable.
4. **Check parameter U4-06 (PreChargeRelayMainte)** on the keypad or software. If the value is above 90%, plan to replace the relay assembly or control board.
5. **Inspect the soft-charge bypass relay** and all associated wiring for loose terminals, heat discoloration, burned contacts, or mechanical damage.
6. **Test all terminal connections** in the relay feedback path with a torque screwdriver to confirm they meet the torque specification in the GA800 manual.
7. **Replace the control board or relay assembly** if physical inspection finds no damage and the fault persists. Yaskawa documentation limits field repair to board and relay-contactor replacement, not component-level fixes.
8. **Re-energize the drive** after any repair, monitor for fault recurrence, and log the repair in your maintenance records.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e43-fault-code&k=Yaskawa+GA800+control+board+%28PCB%29&tag=errorcodefixes-20) \| Order by exact drive model and frame size. Board handles relay drive and answerback feedback. |
| Soft-charge bypass relay or contactor assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e43-fault-code&k=Soft-charge+bypass+relay+or+contactor+assembly&tag=errorcodefixes-20) \| Verify part number from drive nameplate or contact Yaskawa. Not all GA800 frames use the same relay. |
| Replacement terminal lugs or crimp connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e43-fault-code&k=Replacement+terminal+lugs+or+crimp+connectors&tag=errorcodefixes-20) \| Use if existing relay or board terminals show heat damage or poor contact. |

## When to Call a Pro

Call a qualified electrician or VFD service technician for any E43 fault. The soft-charge circuit operates at high DC bus voltage (typically 300-800 VDC depending on input line), and incorrect handling can cause arc flash, electric shock, or permanent drive damage. Technicians need a working knowledge of VFD startup sequences, access to Yaskawa service documentation, and calibrated test equipment to safely diagnose relay feedback paths and control board circuitry. If parameter U4-06 exceeds 90% or physical inspection reveals burned components, the repair requires board or relay assembly replacement that is beyond typical homeowner capability. Yaskawa GA800 service documentation explicitly limits user-serviceable components to fans and control boards, so any deeper troubleshooting should be handled by factory-trained service personnel or an authorized Yaskawa distributor.

**Rough cost:** A pro service call runs about $300-800 for board or relay assembly replacement, depending on drive size and labor.
