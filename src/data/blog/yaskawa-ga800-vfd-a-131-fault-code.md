---
title: "Yaskawa GA800 VFD A.131 Fault - Causes & Fix"
description: "A.131 is not a confirmed GA800 fault code. Likely a parameter number or misread display. Verify exact code on keypad and consult manual."
pubDatetime: 2026-06-09T11:20:20Z
modDatetime: 2026-06-09T11:20:20Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa GA800 option card (model-specific)"
most_likely_cause: "Misread or misidentified code"
diy_or_pro: "pro"
---

## Yaskawa GA800 VFD A.131 Fault — What It Means

A.131 does not appear in verified Yaskawa GA800 documentation as a fault code. Yaskawa drives typically display fault codes in formats like oC, ov, CPF06, or oFA31. The string A.131 may be a parameter number, monitor display item, or a code from a different menu screen rather than an actual alarm. It is also possible the code was misread or belongs to a different drive model or option card.

Before attempting any repair, verify the exact code shown on the operator keypad, including all punctuation and capitalization. Consult the GA800 manual alarm index for the precise code displayed. If the drive has option cards installed, the code may relate to communication or option-board faults, which are often resolved by reseating or replacing the card.

## Before You Replace Anything

Technicians sometimes replace the main control board when the actual fault is a loose or failed option card. Always reseat option cards and verify wiring before replacing the drive or control board.

[Jump to Fix](#fix)

## Common Causes

- **Misread or misidentified code (~40%)** The displayed string may be a parameter number, menu item, or code from a different drive family rather than a GA800 fault.
- **Option card communication fault (~30%)** If an option card is installed, poor seating, loose wiring, or card failure can produce unexpected displays or secondary fault codes.
- **Control board fault (~20%)** Internal control-circuit issues or corrupted firmware can cause non-standard codes or display errors.
- **Keypad or display malfunction (~10%)** A failing operator keypad or display module may show garbled or incorrect codes.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drive display the same code after a power cycle?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is persistent. Record the exact code and consult the GA800 manual alarm section to confirm the code exists.<br><strong>No:</strong> The code may have been transient or a display glitch. Monitor the drive and document the exact code if it reappears.</div>
</details>

<details class="dtree"><summary>Is an option card (communication, encoder, or I/O) installed in the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> Power down, reseat the option card, verify terminal wiring, and power up. If the code persists, replace the option card.<br><strong>No:</strong> The fault is likely internal to the main control board or the code is misidentified. Verify the exact displayed code and consult the manual.</div>
</details>

<details class="dtree"><summary>Can you locate the displayed code in the GA800 manual alarm index?</summary>
<div class="dtree-body"><strong>Yes:</strong> Follow the manual troubleshooting steps for that specific code.<br><strong>No:</strong> The code may not be a fault. Check parameter and monitor menus, or contact Yaskawa technical support with the exact display text.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and lock out the AC supply. Wait at least five minutes for DC bus capacitors to discharge before opening the enclosure.
2. **Photograph the keypad display** showing the exact code, including all letters, numbers, punctuation, and any additional text or symbols.
3. **Consult the GA800 manual** alarm index for the exact code displayed. If the code is not listed, check the parameter and monitor sections of the manual.
4. **Inspect option cards** (if installed). Power down, remove the option card, clean the contacts, reseat firmly, and verify all terminal wiring is secure.
5. **Check control board connections**. Inspect ribbon cables, grounding, and terminal blocks for loose or corroded connections.
6. **Power up the drive** and observe whether the code reappears. Record any additional fault codes or display messages.
7. **Contact Yaskawa technical support** or a qualified drive technician with the exact code, drive model, firmware version, and application details if the code cannot be identified.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 option card (model-specific) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-131-fault-code&k=Yaskawa+GA800+option+card+%28model-specific%29&tag=errorcodefixes-20) \| Match the card to your application (DeviceNet, Modbus, encoder, etc.) |
| Yaskawa GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-131-fault-code&k=Yaskawa+GA800+control+board&tag=errorcodefixes-20) \| Order by drive frame size and voltage rating; requires factory or authorized distributor |

## When to Call a Pro

Call a qualified drive technician or Yaskawa-authorized service center if you cannot locate the exact code in the GA800 manual, if the drive will not power up, or if the fault persists after reseating option cards and verifying wiring. VFD troubleshooting requires multimeter diagnostics, firmware tools, and knowledge of motor control to avoid damage to the drive or connected equipment. Always work with a technician familiar with Yaskawa drives when the fault code is uncertain or when high-voltage circuits are involved.

**Rough cost:** A pro service call runs about $200-500 for service call and diagnostics, plus parts if option card or control board replacement is needed.
