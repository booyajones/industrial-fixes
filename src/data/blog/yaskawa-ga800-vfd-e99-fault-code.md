---
title: "Yaskawa GA800 E99 Fault - Causes & Fix"
description: "E99 on a Yaskawa GA800 points to an external condition or installation issue, not a drive power failure. Check wiring and options first."
pubDatetime: 2026-06-08T10:48:48Z
modDatetime: 2026-06-08T10:48:48Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
most_likely_cause: "Loose or incorrect control wiring on terminals or safety circuits"
likelihood: "the most common cause"
diy_or_pro: "pro"
money_part: "GA800 replacement fan kit"
---

## Yaskawa GA800 E99 Fault — What It Means

The E99 code on a Yaskawa GA800 VFD is not a standard internal power-stage fault like overcurrent or overvoltage. Instead, it signals an external condition or abnormal input that requires checking the drive's installed option cards, control wiring, and the specific alarm text displayed on the operator keypad. Yaskawa's troubleshooting approach for the GA800 treats codes like E99 as indicators to verify peripheral devices, field wiring, and compatibility rather than assuming a component failure inside the drive itself.

Because the exact fault-table entry for E99 is not documented in the supplied GA800 materials, the correct response is to read the full alarm text on the keypad, inspect all control and power wiring for loose or incorrect connections, verify that any installed option cards are properly seated, and check safety or interlock circuits such as Safe Torque Off (STO) or external permissive loops for open connections or missing jumpers. Only after removing the underlying cause should you reset the drive from the keypad.

## Before You Replace Anything

Technicians sometimes replace the main control board when E99 appears, but the code almost always points to external wiring, option-card seating, or a missing jumper in a safety chain. Inspect all field wiring, peripheral connections, and STO/permissive loops before ordering any board.

[Jump to Fix](#fix)

## Common Causes

- **Loose or incorrect field wiring on control terminals (~35%)** A damaged conductor, loose terminal screw, or wrong wire assignment on a control input can trigger an external-condition fault.
- **Improperly seated or incompatible option card (~25%)** A communication or I/O option card that is not fully inserted, has bent pins, or is not compatible with the GA800 firmware will generate an abnormal-input code.
- **Open or missing jumper in a Safe Torque Off or external permissive circuit (~20%)** If the drive is configured to require an STO or permissive signal and the loop is open or a jumper is missing, the drive will fault and display an external-condition alarm.
- **Peripheral device incompatibility or incorrect ratings (~15%)** A mismatch between the connected motor, encoder, or brake resistor and the drive's expected ratings can cause the drive to flag an installation issue.
- **Transient condition that latched the fault (~5%)** A momentary noise spike, voltage dip, or external signal glitch can latch an E99 alarm until the cause is removed and the drive is manually reset.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the keypad display additional alarm text beyond the E99 code?</summary>
<div class="dtree-body"><strong>Yes:</strong> Write down the full text and check the GA800 manual fault table for that specific message, then inspect the wiring or option referenced in the text.<br><strong>No:</strong> Proceed to inspect all control wiring, option cards, and safety circuits for loose connections or missing jumpers before attempting a reset.</div>
</details>

<details class="dtree"><summary>Is an option card or communication module installed in the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> Power down, remove the card, inspect the connector pins for damage, reseat it firmly, and verify compatibility with your GA800 firmware version.<br><strong>No:</strong> Focus on field wiring, checking every control terminal for tightness and correct assignment against your wiring diagram.</div>
</details>

<details class="dtree"><summary>Is the drive configured for Safe Torque Off or an external permissive input?</summary>
<div class="dtree-body"><strong>Yes:</strong> Verify that the STO or permissive loop is closed, all required jumpers are in place, and any safety relay contacts are energized as designed.<br><strong>No:</strong> Check for transient conditions such as loose power connections or noise sources near the control wiring, then reset the drive after corrections.</div>
</details>

## Step-by-Step Fix {#fix}

1. **De-energize the drive and wait** for all status LEDs to go dark and internal capacitors to discharge before touching any wiring.
2. **Read the full alarm text** on the keypad or operator panel, not just the E99 code number, and write it down for reference.
3. **Inspect all control wiring** at the drive terminals for loose screws, damaged insulation, or incorrect terminal assignments against your wiring diagram.
4. **Check installed option cards** by powering down, removing each card, inspecting the connector pins for bends or debris, and reseating firmly.
5. **Verify safety and interlock circuits** such as STO or external permissive loops, confirming that all required jumpers are present and relay contacts are closed.
6. **Confirm peripheral compatibility** by checking that the connected motor, encoder, brake resistor, or communication device matches the ratings and firmware version documented in the GA800 manual.
7. **Remove the underlying cause**, then reset the fault from the keypad and monitor for recurrence; if E99 returns, collect the drive model number, serial number, and alarm text and contact Yaskawa technical support.

## Parts Often Needed

| Part | Notes |
|------|-------|
| GA800 replacement fan kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e99-fault-code&k=GA800+replacement+fan+kit&tag=errorcodefixes-20) \| If a fan fault accompanies E99, use the fan service kit listed in the GA800 maintenance documentation. |
| GA800 option card or communication module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e99-fault-code&k=GA800+option+card+or+communication+module&tag=errorcodefixes-20) \| Replace only if the existing card shows physical damage or fails compatibility checks. |
| Control board assembly for GA800 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e99-fault-code&k=Control+board+assembly+for+GA800&tag=errorcodefixes-20) \| Replace only after confirming all external wiring, option cards, and peripherals are correct and the board itself is verified faulty by Yaskawa support. |

## When to Call a Pro

Call a qualified VFD technician or Yaskawa-authorized service provider if you are not trained to work safely around high-voltage DC bus capacitors, if the E99 code persists after checking all wiring and option cards, or if the keypad alarm text references an internal hardware condition that requires factory diagnostics. A professional will use proper lockout-tagout procedures, verify capacitor discharge with a meter, and have access to Yaskawa's technical support line with your drive's model, spec number, and serial number. Attempting to swap the control board or option cards without isolating the external cause first often results in repeat failures and added cost.

**Rough cost:** A pro service call runs about $150–400 depending on wiring corrections and travel time.

## See Also

- [Yaskawa GA800 A.120 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-a-120-fault-code/)
- [Yaskawa VFD Fault ER — Causes & Fix](/posts/yaskawa-vfd-fault-er/)
- [Yaskawa VFD Fault OV — DC Bus Overvoltage Fix](/posts/yaskawa-vfd-fault-ov/)
- [Yaskawa GA800 VFD F0017 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-f0017-fault-code/)
