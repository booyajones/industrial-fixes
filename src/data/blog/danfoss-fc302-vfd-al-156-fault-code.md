---
title: "Danfoss FC302 VFD AL-15 Fault - Causes & Fix"
description: "AL-15 (Hardware Mismatch) means an incompatible or loose option card is installed. Reseat or replace the card to clear the alarm."
pubDatetime: 2026-06-26T09:48:57Z
modDatetime: 2026-06-26T09:48:57Z
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
  - "Power down the drive, discharge capacitors per Danfoss safety procedure, then remove and firmly reseat the option card in its slot"
  - "Inspect the option card connector pins for corrosion, dirt, or bent pins and clean with compressed air"
  - "Remove the option card entirely and power up the drive to see if the alarm clears"
part_price: "$80-250"
no_buy_pct: "60%"
---

## Danfoss FC302 VFD AL-15 Fault — What It Means

AL-15 (Hardware Mismatch) on the Danfoss FC302 VFD indicates the drive has detected an option card or accessory module that is not compatible with the specific model, firmware version, or is not fitted correctly in its slot. The drive cannot communicate with the card or the card's identification does not match the drive's expected hardware list, so it rejects the card and trips the alarm. If you see a display that appears to show '156' it is almost certainly AL-15 with a display glitch or misread. This is a hardware detection fault, not a motor or power supply issue.

The drive will not run until the mismatch is resolved. Common incompatible cards include serial communication modules, brake control cards, or I/O expansion modules from older Danfoss VLT series or other drive families that physically fit the slot but are not electrically compatible with the FC302 logic board.

## Before You Replace Anything

Technicians sometimes replace the main logic board assuming a board fault when the real problem is simply a dirty or loose connector on an option card. Always reseat and clean the card connector pins before ordering any board replacement.

[Jump to Fix](#fix)

## Common Causes

- **Loose or poorly seated option card (~40%)** The accessory module (serial comm card, brake card, or I/O expansion) is not fully inserted into the slot or the connector has vibrated loose during operation.
- **Incompatible option card installed (~30%)** An accessory from a different Danfoss series (FC500, older VLT) or a third-party card that is not on the FC302 compatibility list was installed in the drive.
- **Dirty or corroded connector pins (~15%)** Dust, moisture, or oxidation on the option card edge connector or the drive's mating socket prevents reliable electrical contact and ID detection.
- **Firmware incompatibility (~10%)** The option card is hardware-compatible but the drive's firmware version is too old (or too new) to support the card, causing the drive to flag it as mismatched.
- **Drive logic board fault (~5%)** The main control board has corrupted memory or a failed detection circuit that falsely reports a hardware mismatch even when the card is correct and seated properly.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the alarm clear when you remove the option card and power up the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The card itself is the problem (incompatible, faulty, or needs cleaning). Verify the card part number against the FC302 compatibility list and reseat or replace it.<br><strong>No:</strong> The drive logic board may have a fault or the card detection circuit is corrupted. Update firmware first, then suspect the main board.</div>
</details>

<details class="dtree"><summary>Is the option card part number listed in the FC302 manual compatibility table?</summary>
<div class="dtree-body"><strong>Yes:</strong> The card is compatible. The issue is likely a loose connection, dirty pins, or outdated firmware. Clean and reseat the card, then update firmware if available.<br><strong>No:</strong> The card is not compatible with the FC302. Source the correct Danfoss option card for the FC302 series from your distributor.</div>
</details>

<details class="dtree"><summary>After reseating and cleaning, does the alarm still appear immediately on power-up?</summary>
<div class="dtree-body"><strong>Yes:</strong> The card is likely faulty or the drive logic board cannot recognize it. Replace the option card first (lower cost). If the new card also triggers AL-15, replace the logic board.<br><strong>No:</strong> The connection was the issue. Run the drive under load and monitor for recurring alarms.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** by disconnecting AC mains and any DC bus supply. Wait at least five minutes for internal capacitors to discharge per Danfoss safety guidelines.
2. **Remove the option card** by unscrewing the retaining screws (if present) and carefully pulling the card straight out of its slot. Note the card's orientation and part number.
3. **Inspect and clean the connector** by examining both the card edge connector and the drive's mating socket for dust, corrosion, or bent pins. Use compressed air or a non-conductive brush to clean the contacts.
4. **Verify compatibility** by checking the card's part number against the FC302 compatibility list in the drive manual or on the Danfoss website. Confirm the card is designed for the FC302 series.
5. **Reseat the card firmly** by aligning the card with the slot guides and pushing it fully home until it clicks or seats flush. Secure any retaining screws. Restore power and observe the display.
6. **Test without the card** if the alarm persists. Remove the card entirely, power up the drive, and check if AL-15 clears. If it clears, the card is faulty or incompatible. If it remains, the logic board may be at fault.
7. **Update firmware** if the card is known compatible but the alarm persists. Download the latest FC302 firmware from Danfoss and follow the update procedure in the manual. Re-install the card after the update and test.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 compatible option card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-156-fault-code&k=Danfoss+FC302+compatible+option+card&tag=errorcodefixes-20) \| Verify the exact part number for your application (serial comm, brake, I/O expansion) from the FC302 compatibility list before ordering. |
| Danfoss FC302 main logic board (control card) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-156-fault-code&k=Danfoss+FC302+main+logic+board+%28control+card%29&tag=errorcodefixes-20) \| Only needed if the alarm persists with a known-good option card removed or if multiple cards all trigger AL-15. Confirm the board part number for your drive frame size. |

## When to Call a Pro

Call a qualified industrial electrician or controls technician if you are not comfortable working inside VFD enclosures, if high-voltage DC bus capacitors are involved, or if the drive's firmware update procedure is unfamiliar. A technician can safely discharge the capacitors, verify option card compatibility with test equipment, and access Danfoss service tools to read detailed fault logs. Also call a pro if you have replaced or reseated the card and updated firmware but AL-15 still appears, as the main logic board may need replacement or the drive may require factory-level diagnostics. Any work on three-phase power systems or VFD internal circuits should be performed by someone trained in industrial power electronics and familiar with arc-flash safety and lockout-tagout procedures.

**Rough cost:** A pro service call runs about $150-400.
