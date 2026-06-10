---
title: "Yaskawa GA800 A.123 Fault - Causes & Fix"
description: "A.123 signals a soft-charge relay maintenance problem. The most common fix is replacing the control board or the entire drive unit."
pubDatetime: 2026-06-08T11:21:57Z
modDatetime: 2026-06-08T11:21:57Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
most_likely_cause: "Worn or failed soft-charge bypass relay contacts"
likelihood: "the most common cause"
diy_or_pro: "pro"
---

## Yaskawa GA800 A.123 Fault — What It Means

The A.123 code on a Yaskawa GA800 VFD is a soft-charge (precharge) relay maintenance indicator, not a motor-tripping fault in the usual sense. The drive is not receiving the expected relay contact confirmation in the soft-charge bypass circuit during startup. This code is tied to the drive's maintenance monitor U4-06 [PreChargeRelayMainte], which tracks the service life of the relay that manages the precharge sequence.

When this value climbs above about 90 percent, Yaskawa directs technicians to replace the control board or the complete drive assembly. The soft-charge relay energizes during power-up to limit inrush current to the DC bus capacitors, then a bypass contactor takes over for normal operation. If the relay contacts are worn, the relay coil driver circuit has failed, or the feedback signal is lost, the drive flags A.123 and may refuse to run.

## Before You Replace Anything

Technicians sometimes replace the entire drive immediately without checking the U4-06 maintenance counter first. If the counter is below 90 percent and the fault clears on a power cycle, the relay may have years of life left and no parts are needed yet.

[Jump to Fix](#fix)

## Common Causes

- **Worn soft-charge bypass relay contacts (~50%)** Repeated switching cycles pit or weld the relay contacts so they no longer close cleanly or fail to feed back a clean signal to the control board.
- **Failed relay drive circuitry on the control board (~30%)** The transistor or IC that energizes the relay coil has failed, or a feedback opto-isolator is open, so the drive never sees the relay pull in.
- **High relay maintenance counter (U4-06 above 90%) (~15%)** The drive tracks relay operations and flags A.123 when the relay is near end of service life, even if it still operates today.
- **Loose or corroded feedback wiring (~5%)** A broken solder joint or oxidized connector in the relay feedback path prevents the control board from detecting that the relay closed.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear after removing power for two minutes and restarting?</summary>
<div class="dtree-body"><strong>Yes:</strong> The relay may have recovered or the contact was marginal. Check U4-06 on the keypad to see if the maintenance counter is above 90 percent. If it is high, schedule board or drive replacement soon.<br><strong>No:</strong> The relay or control-board circuitry has failed. Proceed to check the maintenance monitor and replace the board or drive.</div>
</details>

<details class="dtree"><summary>Is the U4-06 PreChargeRelayMainte value above 90 percent?</summary>
<div class="dtree-body"><strong>Yes:</strong> Yaskawa guidance is to replace the control board or the entire drive. Do not attempt field repair of the relay itself.<br><strong>No:</strong> The relay may have failed early. Inspect for burnt contacts, verify supply voltage to the relay coil, and check feedback signal continuity before replacing the board.</div>
</details>

<details class="dtree"><summary>Can you hear or measure the relay clicking when the drive attempts to start?</summary>
<div class="dtree-body"><strong>Yes:</strong> The relay coil is energizing but the contacts may be welded, pitted, or the feedback circuit is open. Replace the control board.<br><strong>No:</strong> No coil energization suggests a failed relay driver on the control board or a broken coil. Replace the control board or drive.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Remove power** from the drive at the upstream disconnect and wait at least five minutes for the DC bus capacitors to discharge. Verify zero voltage with a meter rated for the bus voltage.
2. **Re-energize the drive** and observe the keypad. If A.123 does not reappear immediately, the fault may have been transient. Monitor the drive over several start cycles.
3. **Navigate to U4-06 [PreChargeRelayMainte]** on the keypad menu and record the percentage. If the value is above 90 percent, plan to replace the control board or the entire drive assembly.
4. **Inspect the soft-charge relay** (typically on the main power board or control board, depending on frame size). Look for discolored contacts, burnt coil windings, or evidence of arcing. Do not energize individual components with external voltage without factory approval.
5. **Check feedback wiring and connectors** between the relay contacts and the control board. Re-seat ribbon cables and check solder joints under magnification if you have board-level repair skills.
6. **Replace the control board** if the relay maintenance counter is high or if the relay drive circuitry is suspect. Follow the drive manual for board removal, noting all parameter backups and jumper positions.
7. **Clear the fault** using the RESET button on the keypad after the cause is corrected. If the drive still flags A.123 after board replacement, replace the entire drive unit and return the old unit for warranty or core credit analysis.

## Parts Often Needed

| Part | Notes |
|------|-------|
| GA800 control board (model-specific) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-123-fault-code&k=GA800+control+board+%28model-specific%29&tag=errorcodefixes-20) \| Consult the drive nameplate for exact frame size and voltage rating. Board part numbers vary by horsepower and options installed. |
| Complete GA800 drive assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-123-fault-code&k=Complete+GA800+drive+assembly&tag=errorcodefixes-20) \| Required if the control board replacement does not resolve A.123 or if the drive is otherwise at end of service life. |

## When to Call a Pro

Call a qualified drive technician or an authorized Yaskawa service center for any A.123 fault. The drive contains high-voltage DC bus capacitors that remain charged long after AC input is removed, and incorrect troubleshooting can destroy the control board or create an arc-flash hazard. Do not perform withstand-voltage or Megger insulation tests on the drive. If U4-06 is above 90 percent, only a factory-trained technician should replace the control board or drive, because parameter cloning, option-card transfer, and firmware matching are all critical to a successful swap. If your facility does not have in-house VFD repair capability, this is always a professional call.

**Rough cost:** A pro service call runs about $500-2500.
