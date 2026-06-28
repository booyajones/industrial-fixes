---
title: "Danfoss FC302 AL-155 Fault - Causes & Fix"
description: "AL-155 is not a standard Danfoss code. Most likely a misread of AL 15 (Hardware Mismatch). Reseat or replace the option card first."
pubDatetime: 2026-06-26T09:48:07Z
modDatetime: 2026-06-26T09:48:07Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss Option Card (MCB 109, MCB 110, or model-specific card)"
most_likely_cause: "Option card not seated or incompatible with drive firmware"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power down, remove the option card, inspect the slot for dust or corrosion, and firmly reseat the card"
  - "Check the drive display again to confirm the exact alarm number (AL 15 vs AL 13 vs another code)"
  - "Review the drive firmware version in the parameter menu and compare to the option card's compatibility table"
part_price: "$150-400"
---

## Danfoss FC302 AL-155 Fault — What It Means

AL-155 does not appear in standard Danfoss FC302 documentation as a user-facing fault code. The most probable explanation is that you have misread AL 15, which signals a Hardware Mismatch. This alarm means the drive has detected an option card (such as a brake control module, serial communication card, or brake resistor interface) that is either incompatible with your FC302 model, not seated correctly in its slot, or running firmware that does not match the drive's current version. Another possibility is that you are seeing Alarm 13 (DC Undervoltage) and confusing a model number or part label with the alarm code.

If the display clearly shows AL 15, the drive is refusing to operate because it cannot recognize or validate the installed option card. If it shows AL 13, the DC bus voltage has dropped below the minimum threshold, typically due to low input voltage, a failing rectifier, or excess load on the motor. Check your actual display carefully and compare it to the alarm list in your FC302 manual to confirm which code you have before proceeding.

## Before You Replace Anything

Technicians often replace the option card when the real issue is outdated drive firmware or a dirty slot contact. Reseat the card and update firmware before buying a new card.

[Jump to Fix](#fix)

## Common Causes

- **Option card not fully seated (~35%)** The card has worked loose due to vibration or was never pushed firmly into the slot, breaking the digital connection between the card and the drive logic.
- **Incompatible or outdated option card firmware (~30%)** A genuine Danfoss card requires a firmware update to work with the current drive firmware version, or the card was designed for a different voltage or current class.
- **Third-party or counterfeit option card (~15%)** A non-Danfoss card or a clone lacks the correct handshake logic and the drive rejects it as unrecognized hardware.
- **Low input voltage (if the code is actually AL 13) (~10%)** Supply voltage is below the drive's rated minimum, causing the DC bus to sag and triggering an undervoltage alarm instead of a hardware mismatch.
- **Failed main control board (~7%)** The drive's logic board has corrupted memory or a faulty slot controller and incorrectly flags a valid card as incompatible.
- **Corroded or damaged slot contacts (~3%)** Moisture, dust, or physical damage to the option-card slot prevents proper electrical contact and data transfer.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drive display show exactly AL 15 or Alarm 15?</summary>
<div class="dtree-body"><strong>Yes:</strong> You have a Hardware Mismatch alarm. Proceed to reseat the option card and check firmware compatibility.<br><strong>No:</strong> Write down the exact alarm number and consult your FC302 manual. If it reads AL 13, the problem is DC Undervoltage, not a card issue.</div>
</details>

<details class="dtree"><summary>Can you see an option card (a small PCB plugged into a slot on the side or front of the drive)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Remove the card, clean the contacts with contact cleaner, and reseat it firmly. If the alarm persists, the card or drive firmware needs attention.<br><strong>No:</strong> The drive may be detecting phantom hardware or have a corrupted parameter. Reset to factory defaults and check for internal board damage.</div>
</details>

<details class="dtree"><summary>Does the alarm clear after reseating the card and power-cycling the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The card was loose. Monitor for recurrence and secure the card with any available retaining clip or screw.<br><strong>No:</strong> Update the drive firmware, verify card compatibility with your FC302 model number, or replace the card with a known-good unit.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Confirm the alarm code** by recording the exact characters on the drive display and comparing them to the alarm table in your FC302 manual or the parameter 16-92 alarm log.
2. **Power down the drive** at the main disconnect and wait at least five minutes for DC bus capacitors to discharge before opening any covers.
3. **Remove the option card** by unscrewing any retaining hardware, grasping the card edges, and pulling straight out from the slot without twisting.
4. **Inspect the card and slot** for dust, corrosion, bent pins, or physical damage. Use compressed air to clean the slot and a pencil eraser or contact cleaner on the card edge connector.
5. **Reseat the card firmly** by aligning the connector and pushing until you feel or hear a click. Secure with any screws or clips.
6. **Power up and check** whether the alarm clears. If it does, the card was loose. If it persists, note the drive firmware version in parameter 15-43.
7. **Update the drive firmware** to the latest release available from Danfoss for your FC302 model, following the update procedure in the manual or using the MCT 10 software tool.
8. **Verify card compatibility** by cross-referencing the card part number (printed on the card) with the FC302 datasheet to make sure it is listed for your drive voltage and current rating.
9. **Replace the option card** if the alarm remains after firmware update and reseating. Use only a Danfoss-supplied card with a part number verified for your drive.
10. **Replace the main control board** if a known-good, compatible card still triggers AL 15, indicating a fault in the drive's slot controller or memory.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss Option Card (MCB 109, MCB 110, or model-specific card) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-155-fault-code&k=Danfoss+Option+Card+%28MCB+109%2C+MCB+110%2C+or+model-specific+card%29&tag=errorcodefixes-20) \| Match the part number exactly to your FC302 voltage and current class. Verify compatibility with current firmware. |
| FC302 Main Control Board (Logic Board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-155-fault-code&k=FC302+Main+Control+Board+%28Logic+Board%29&tag=errorcodefixes-20) \| Required only if the drive itself mis-flags valid cards. Order by full FC302 model number and serial range. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician if you are not familiar with safely working inside motor drives. High-voltage DC bus capacitors can hold a lethal charge even after power is removed. A professional will use a discharge tool and multimeter to verify safe conditions before touching internal components. If you have reseated the card, updated firmware, and verified compatibility but the alarm persists, the technician will need to test the main control board and may require factory-level diagnostics or a replacement board programmed with your drive parameters. Also call a pro if you suspect the alarm is actually AL 13 and you need to measure three-phase input voltage, inspect rectifier diodes, or test DC bus capacitors, all of which involve high-voltage measurements and potential replacement of the power board.

**Rough cost:** A pro service call runs about $200-500.
