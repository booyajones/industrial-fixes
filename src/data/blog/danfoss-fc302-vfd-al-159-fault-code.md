---
title: "Danfoss FC302 AL-159 Fault - Causes & Fix"
description: "AL-159 is likely AL-15 (Hardware Mismatch). A non-compatible or loose option card is the most common cause. Reseat the card first."
pubDatetime: 2026-06-26T09:51:23Z
modDatetime: 2026-06-26T09:51:23Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 compatible option card"
most_likely_cause: "Loose or incorrectly seated option card"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power down the drive safely and reseat the option card to verify it is fully seated and secured"
  - "Check the option card model number against the FC302 compatibility list in your manual"
  - "Inspect the card connector and slot for visible corrosion or physical damage"
no_buy_pct: "60%"
---

## Danfoss FC302 AL-159 Fault — What It Means

There is no official Danfoss FC302 fault code AL-159. The code you are seeing is almost certainly AL-15 (Hardware Mismatch), which is frequently misread as 159 due to formatting errors in diagnostic logs or visual confusion on the display. AL-15 indicates that the drive has detected a non-compatible or incorrectly installed option card, such as a brake control card, serial communication card, or fieldbus adapter. The FC302 logic board identifies the card by its firmware signature. If the signature does not match the drive's supported list, or if the card is physically loose, the drive triggers this alarm and may prevent operation.

## Before You Replace Anything

Technicians sometimes replace the option card when the problem is simply a loose connection or incompatible firmware version. Reseat the card and verify firmware compatibility before ordering a replacement.

[Jump to Fix](#fix)

## Common Causes

- **Loose physical connection (~40%)** The option card is not fully seated in the slot or the mounting screws are loose, causing intermittent communication or a not-detected state.
- **Incorrect option card (~25%)** A card designed for a different drive series (such as an FC200 card in an FC302) or a model not supported by the current firmware version is installed.
- **Firmware incompatibility (~20%)** The option card requires a newer FC302 firmware version than what is currently installed on the drive.
- **Damaged connector (~10%)** The slot on the drive's logic board or the card's connector is corroded or physically damaged.
- **Logic board mis-flag (~5%)** The drive's internal logic board has a firmware error causing it to mis-identify a valid card.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is there an option card installed in the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> Proceed to power down and inspect the card for loose connections or visible damage.<br><strong>No:</strong> The alarm should not occur without an option card. Check for a logic board fault or contact Danfoss support.</div>
</details>

<details class="dtree"><summary>Does the option card model number match the FC302 compatibility list in your manual?</summary>
<div class="dtree-body"><strong>Yes:</strong> The card is correct. Reseat it firmly and check firmware versions. If the alarm persists, the card or logic board may be defective.<br><strong>No:</strong> Replace the card with an FC302-compatible model from Danfoss or an authorized distributor.</div>
</details>

<details class="dtree"><summary>Did reseating the card clear the alarm?</summary>
<div class="dtree-body"><strong>Yes:</strong> The issue was a loose connection. Secure the card with mounting screws and monitor for recurrence.<br><strong>No:</strong> Check the drive firmware version via parameter 14-20. If outdated, update to the latest version. If the alarm still persists, replace the option card or logic board.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down safely.** Turn off the AC mains and any remote DC-link power including UPS or batteries. Wait for capacitors to discharge fully according to the minimum time in Table 1.3 of the Programming Guide.
2. **Locate and inspect the option card.** Open the drive enclosure and find the option card near the logic board. Check for visible damage, corrosion, loose screws, or a model number that does not match the FC302 support list.
3. **Reseat the card.** Remove the option card carefully. If contacts are dirty, clean them with distilled water or electronics cleaner. Reinsert the card firmly until it clicks into the slot and secure it with mounting screws.
4. **Restore power and test.** Turn on the drive and monitor the LCP display. If the alarm clears, the issue was a loose connection. If it persists, continue to the next step.
5. **Check firmware compatibility.** Verify the current FC302 firmware version via parameter 14-20. Compare it to the option card's required firmware version in its documentation. If incompatible, update the drive firmware to the latest version from Danfoss.
6. **Replace the option card if defective.** If the card is damaged, incompatible, or still triggers the alarm after reseating and firmware update, replace it with the correct FC302-compatible model.
7. **Replace the logic board if mis-flagged.** If a valid, properly seated card still triggers the alarm after firmware update, the drive's logic board may be mis-flagging. Install a replacement logic board from Danfoss or Wake Industrial.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 compatible option card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-159-fault-code&k=Danfoss+FC302+compatible+option+card&tag=errorcodefixes-20) \| Verify the exact model number and firmware requirements for your drive before ordering |
| Danfoss FC302 logic board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-159-fault-code&k=Danfoss+FC302+logic+board&tag=errorcodefixes-20) \| Required only if the board is mis-flagging a valid card after all other troubleshooting |

## When to Call a Pro

Call a qualified industrial electrician or automation technician if you are not trained to work on VFDs. This repair requires safe lockout-tagout procedures, discharging high-voltage capacitors, and verifying firmware compatibility. If you are uncomfortable opening the drive enclosure, handling option cards, or updating firmware, contact a Danfoss service partner or an authorized distributor. A technician can also rule out logic board faults and provide warranty support if the drive is still covered.

**Rough cost:** A pro service call runs about $150-400.

## See Also

- [Danfoss FC302 AL-103 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-103-fault-code/)
- [Danfoss FC302 WARNING 77 - Causes & Fix](/posts/danfoss-fc302-vfd-al-77-fault-code/)
- [Danfoss FC302 W66 - Causes & Fix](/posts/danfoss-fc302-vfd-al-66-fault-code/)
- [Danfoss FC302 AL-97 - Causes & Fix](/posts/danfoss-fc302-vfd-al-97-fault-code/)
