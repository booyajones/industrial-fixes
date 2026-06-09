---
title: "Yaskawa GA800 E73 Fault - Causes & Fix"
description: "E73 is a soft charge answerback fault: the drive's precharge relay or control board failed. Most common fix: replace the control board."
pubDatetime: 2026-06-07T10:13:52Z
modDatetime: 2026-06-07T10:13:52Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
most_likely_cause: "Failed soft-charge bypass relay or control board"
likelihood: "the most common cause"
diy_or_pro: "pro"
---

## Yaskawa GA800 E73 Fault — What It Means

The E73 code on a Yaskawa GA800 is a Soft Charge Answerback Fault. During startup, the drive precharges its internal capacitors through a soft-charge circuit, then expects a feedback signal from the bypass relay or contactor to confirm the circuit switched over. When that answerback signal does not arrive, the drive shuts down with E73. This is an internal drive hardware problem, not a motor or wiring issue.

The fault points to one of three areas inside the drive: the soft-charge bypass relay or contactor has failed, the control board cannot command or read the answerback circuit, or the power section has reached end of life. Yaskawa groups E73 with drive-side hardware faults and notes that repairs beyond fan and control board replacement are not covered in field service guides, which means many E73 cases require either a board swap or a complete drive replacement.

## Before You Replace Anything

Technicians sometimes replace the entire drive immediately without checking the control board first. Always read parameter U4-06 (PreChargeRelayMainte) to see relay life percentage before ordering a new drive.

[Jump to Fix](#fix)

## Common Causes

- **Worn soft-charge bypass relay or contactor** The relay that switches the precharge circuit out of the power path has failed or its contacts no longer close reliably.
- **Failed control board** The board cannot send the command to the bypass relay or cannot read the answerback signal, even though the relay itself is good.
- **High relay maintenance life (U4-06 > 90%)** The drive tracks the cumulative switching cycles of the soft-charge relay, and Yaskawa recommends board or drive replacement when U4-06 exceeds 90 percent.
- **End-of-life power section** Internal components in the drive's power assembly have degraded to the point where the precharge circuit no longer functions correctly.
- **Loose or corroded internal connections** Wiring between the control board and the soft-charge bypass relay has come loose or corroded, breaking the answerback feedback path.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the E73 fault clear when you cycle power to the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault may have been a one-time glitch. Monitor the drive during the next few starts. If E73 reappears, proceed to check relay life.<br><strong>No:</strong> The fault is persistent. Move to the next check to inspect the internal relay-life counter.</div>
</details>

<details class="dtree"><summary>Is parameter U4-06 (PreChargeRelayMainte) greater than 90 percent?</summary>
<div class="dtree-body"><strong>Yes:</strong> The soft-charge relay has reached its service life. Replace the control board or the entire drive per manufacturer guidance.<br><strong>No:</strong> The relay counter is still low, so suspect the control board or internal wiring. A board swap is the next logical step.</div>
</details>

<details class="dtree"><summary>Does the fault return immediately after you replace the control board?</summary>
<div class="dtree-body"><strong>Yes:</strong> The power section or bypass relay itself is faulty. Replace the entire drive.<br><strong>No:</strong> The control board was the root cause. The drive should run normally.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and lock out all upstream disconnects following your facility electrical safety procedures.
2. **Wait at least five minutes** for the DC bus capacitors to discharge before opening any covers.
3. **Power the drive back up** and observe whether the E73 fault clears on its own. If it does, monitor the drive through several start cycles to see if the fault recurs.
4. **Access the monitoring menu** and navigate to parameter U4-06 (PreChargeRelayMainte). Record the percentage value shown.
5. **If U4-06 is above 90 percent**, plan to replace the control board or the entire drive. Yaskawa's guidance is that relay life above 90 percent means the soft-charge bypass relay is near end of service.
6. **If U4-06 is below 90 percent** and the fault persists, replace the control board first. The board is the most common field-replaceable cause when relay life is still healthy.
7. **If the fault returns after board replacement**, the power section or bypass relay hardware has failed and the drive must be replaced as a complete assembly.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 control board (model-specific) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e73-fault-code&k=Yaskawa+GA800+control+board+%28model-specific%29&tag=errorcodefixes-20) \| Verify your exact frame size and firmware revision before ordering. Not all frame sizes use the same control board. |
| Yaskawa GA800 VFD (complete drive replacement) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e73-fault-code&k=Yaskawa+GA800+VFD+%28complete+drive+replacement%29&tag=errorcodefixes-20) \| Required when the power section or bypass relay itself has failed. Match horsepower, voltage, and enclosure rating to your application. |

## When to Call a Pro

E73 is an internal drive fault that requires high-voltage work and familiarity with VFD architecture. A qualified electrician or drive technician should diagnose the fault, read the relay-life parameter, and replace the control board or the entire drive. Do not attempt to open the drive enclosure unless you are trained in high-voltage DC bus safety. Capacitors inside the drive can hold lethal voltage for several minutes after power is removed. If your facility does not have in-house drive techs, contact a Yaskawa authorized service center or an industrial controls integrator to perform the repair.

**Rough cost:** A pro service call runs about $300–1,200 for control board replacement or full drive swap, depending on frame size.
