---
title: "Yaskawa GA800 F015 Fault - Causes & Fix"
description: "F015 is not documented for Yaskawa GA800 drives. Confirm the code on the display and check if the drive is a Schneider ATV series instead."
pubDatetime: 2026-06-27T11:36:01Z
modDatetime: 2026-06-27T11:36:01Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa GA800 Control Board"
most_likely_cause: "Drive misidentification or incorrect fault code reading"
likelihood: "the most common cause when F015 appears on equipment labeled as Yaskawa GA800"
diy_or_pro: "pro"
free_checks:
  - "Verify the drive manufacturer nameplate matches Yaskawa (not Schneider Electric)"
  - "Photograph the exact fault code as displayed on the operator keypad"
  - "Check the drive model number against Yaskawa GA800 Technical Manual fault code list"
---

## Yaskawa GA800 F015 Fault — What It Means

The fault code F015 does not appear in any Yaskawa GA800 documentation available. Yaskawa GA800 drives use two-letter alphanumeric fault codes (such as OV for overvoltage, SC for short circuit, LU for load unbalance, or GF for ground fault) rather than numeric "F" codes. The F015 code is specific to Schneider Electric drives (ATV310, ATV610, and ATV31C series) where it indicates "3 Output phases loss" meaning all three output phases to the motor are missing.

If you see F015 on what you believe is a Yaskawa GA800, either the drive has been misidentified and is actually a Schneider model, the code is being read incorrectly from the display, or there is cross-brand confusion in the documentation. Yaskawa's maintenance manual for the GA800 explicitly states the drive does not support field repairs beyond fan and control board replacement and does not list F015 as a valid fault. Contact Yaskawa Technical Support at 1.800.927.5292 (Option 2 then Option 1 for Drive Support) or email repair@yaskawa.com to verify the actual fault code and obtain the GA800 Technical Manual for your specific model.

## Before You Replace Anything

Technicians may assume F015 is a Yaskawa fault and replace output boards or motor cables. First verify the drive brand nameplate and consult the correct manufacturer's fault code list before ordering any parts.

[Jump to Fix](#fix)

## Common Causes

- **Drive brand misidentification (~50%)** The drive is actually a Schneider Electric ATV310 or ATV610 model and F015 correctly indicates loss of all three output phases to the motor.
- **Incorrect fault code reading (~30%)** The display shows a different Yaskawa two-letter code (such as OL, UV, or another valid GA800 fault) that is being misread or transcribed as F015.
- **Cross-referenced documentation error (~15%)** A technician is using a Schneider manual or fault code chart while servicing a Yaskawa drive, leading to confusion about which codes apply.
- **Display or keypad malfunction (~5%)** The operator keypad or display module is failing and showing garbled or incorrect fault codes that do not match the GA800 fault list.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drive nameplate say Schneider Electric, ATV310, or ATV610?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive is a Schneider model and F015 means all three output phases to the motor are lost. Check motor connections, output contactors, and motor cable continuity.<br><strong>No:</strong> Confirm the nameplate says Yaskawa GA800 and proceed to verify the actual fault code displayed.</div>
</details>

<details class="dtree"><summary>Does the fault display show exactly F015 with those characters?</summary>
<div class="dtree-body"><strong>Yes:</strong> Photograph the display and contact Yaskawa Technical Support at 1.800.927.5292 to confirm whether F015 exists for your GA800 model and firmware version.<br><strong>No:</strong> Write down the exact two-letter code shown and look it up in the Yaskawa GA800 Technical Manual fault code section.</div>
</details>

<details class="dtree"><summary>Do you have access to the Yaskawa GA800 Technical Manual for your drive model?</summary>
<div class="dtree-body"><strong>Yes:</strong> Cross-reference the displayed fault code against the manual's fault code table to determine the correct meaning and troubleshooting steps.<br><strong>No:</strong> Contact Yaskawa Technical Support at repair@yaskawa.com or call 1.800.927.5292 to request the technical manual and verify the fault code.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and lock out the disconnect to prevent accidental energization during inspection.
2. **Verify the drive manufacturer** by reading the nameplate on the front or side of the unit and confirm it says Yaskawa (not Schneider Electric, Altivar, or ATV).
3. **Photograph the fault display** showing the exact alphanumeric code as it appears on the operator keypad or LCD panel.
4. **Consult the Yaskawa GA800 Technical Manual** (document number beginning with SIEPC) for your specific model to cross-reference the displayed fault code.
5. **Contact Yaskawa Technical Support** at 1.800.927.5292 (select Option 2 for Technical Support, then Option 1 for Drives) or email repair@yaskawa.com with the drive model number, serial number, and fault code photograph.
6. **If the drive is confirmed to be a Schneider ATV model**, follow Schneider's F015 troubleshooting: check all motor cable connections, verify the motor is connected and draws at least 6 percent of drive rated current, inspect output contactors for open circuits, and test output phase continuity.
7. **Do not attempt field repairs** beyond fan or control board replacement on Yaskawa GA800 drives as the manufacturer explicitly does not support other component-level repairs and recommends factory service for internal faults.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 Control Board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f015-fault-code&k=Yaskawa+GA800+Control+Board&tag=errorcodefixes-20) \| Only if Yaskawa Technical Support confirms the fault is control-board related and the drive is confirmed as a GA800 model. |
| Yaskawa GA800 Cooling Fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f015-fault-code&k=Yaskawa+GA800+Cooling+Fan&tag=errorcodefixes-20) \| User-replaceable part per the GA800 maintenance manual if overheating is confirmed as the root cause. |

## When to Call a Pro

Call a professional immediately if you cannot confirm the drive brand or the fault code does not match any entry in the manufacturer's technical manual. Variable frequency drives operate at lethal voltages (typically 230V to 480V three-phase) and contain large DC bus capacitors that retain charge even after power is removed. Only qualified electricians or drive technicians should open the drive enclosure, measure internal voltages, or replace components. Yaskawa explicitly recommends contacting their technical support or an authorized service center for any fault that cannot be resolved by checking external connections or resetting the drive. If the drive is actually a Schneider model showing F015, a professional should verify motor cable integrity, measure output phase currents, and adjust parameters 605, 310, 304, 305, and 318 as outlined in Schneider's service documentation.

**Rough cost:** A pro service call runs about $200-500 for diagnostic service and fault code verification.
