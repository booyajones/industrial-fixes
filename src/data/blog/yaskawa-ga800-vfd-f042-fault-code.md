---
title: "Yaskawa GA800 F042 - Causes & Fix"
description: "F042 does not exist on Yaskawa GA800 drives. This code belongs to Allen Bradley PowerFlex 525 and indicates a Phase UW short. Check your manual."
pubDatetime: 2026-06-28T10:10:55Z
modDatetime: 2026-06-28T10:10:55Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa GA800 Control Board"
most_likely_cause: "Misidentification of drive brand or fault code"
likelihood: "the most common cause when F042 is reported on a Yaskawa unit"
diy_or_pro: "pro"
free_checks:
  - "Verify the drive nameplate to confirm it is a Yaskawa GA800 and not an Allen Bradley PowerFlex 525"
  - "Check the actual fault code displayed on the GA800 keypad or HMI against the Yaskawa fault code table in the manual"
  - "Power cycle the drive and record the exact alphanumeric code that appears"
---

## What this code means
There is no F042 fault code in the Yaskawa GA800 VFD fault table. The F042 code belongs exclusively to the Allen Bradley PowerFlex 525 drive, where it indicates a Phase UW Short (excessive current detected between output terminals U and W). If you are seeing F042 on what you believe is a Yaskawa GA800, you are either reading a different drive's display or misidentifying the equipment. The Yaskawa GA800 manual does not list F042 in its fault code table and explicitly states that repair information beyond fan and control board replacement is not provided.

If you have a fault on your Yaskawa GA800, you must refer to the Yaskawa-specific fault codes (such as bUS for bus errors, OV for overvoltage, SC for short circuit, or bA for brake anomalies) in the GA800 Maintenance & Troubleshooting Manual. The hardware, firmware, and fault logic are entirely different between Yaskawa and Allen Bradley products. Contact Yaskawa Technical Support at repair@yaskawa.com or 1.800.927.5292 for the correct fault code interpretation and diagnostics for your specific GA800 unit.

## Before You Replace Anything

Technicians sometimes attempt to apply Allen Bradley diagnostics to Yaskawa drives when they see an unfamiliar code. Always verify the drive manufacturer nameplate and consult the correct manual before ordering parts or performing tests.

## Common Causes

- **Wrong drive brand identified (~60%)** The drive displaying F042 is actually an Allen Bradley PowerFlex 525, not a Yaskawa GA800.
- **Misread fault code (~25%)** The technician misread a legitimate Yaskawa fault code (such as F or bF followed by other digits) as F042.
- **Mixed equipment in system (~10%)** Multiple VFDs from different manufacturers are present and the fault code was read from the wrong unit.
- **Documentation error (~5%)** Service records or remote monitoring software display a code from a different drive or a logging error.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drive nameplate say Allen Bradley PowerFlex 525?</summary>
<div class="dtree-body"><strong>Yes:</strong> You have the wrong drive. Use Allen Bradley F042 diagnostics: check motor wiring between U and W terminals for shorts, inspect remote wiring, verify input fuses, and replace the control module or drive if wiring is intact.<br><strong>No:</strong> Confirm the nameplate says Yaskawa GA800 and record the exact fault code displayed on the keypad.</div>
</details>

<details class="dtree"><summary>Does the Yaskawa GA800 display show a different fault code (such as bUS, OV, SC, or another alphanumeric code)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Look up that specific Yaskawa fault code in the GA800 manual and follow the manufacturer diagnostics. Contact Yaskawa support for interpretation.<br><strong>No:</strong> The display may be blank or the drive may not be faulted. Check input power, verify the keypad connection, and consult Yaskawa support.</div>
</details>

<details class="dtree"><summary>Is there more than one VFD in the system?</summary>
<div class="dtree-body"><strong>Yes:</strong> Check each drive's nameplate individually and match the fault code to the correct manufacturer's documentation.<br><strong>No:</strong> Verify you are reading the fault from the correct display and not from remote monitoring software that may be logging a different unit.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify drive identity:** Check the nameplate on the front or side of the VFD to confirm it says Yaskawa GA800 and not Allen Bradley PowerFlex 525 or another brand.
2. **Record the exact fault code:** Write down the full alphanumeric code displayed on the GA800 keypad or HMI, including any prefix letters (such as bUS, OV, SC, or bA).
3. **Consult the Yaskawa GA800 manual:** Open the GA800 Maintenance & Troubleshooting Manual and locate the fault code table to find the exact meaning of the code you recorded.
4. **Inspect all VFDs in the system:** If multiple drives are present, check each nameplate and display to confirm you are diagnosing the correct unit.
5. **Contact Yaskawa Technical Support:** Call 1.800.927.5292 or email repair@yaskawa.com with your drive serial number and the exact fault code for manufacturer-specific diagnostics.
6. **Do not apply Allen Bradley diagnostics:** Allen Bradley F042 procedures (checking U-W terminal shorts, replacing control modules) do not apply to Yaskawa hardware and may cause damage or void warranty.
7. **Follow Yaskawa repair limits:** The GA800 manual states that repair information beyond fan and control board replacement is not provided, so field repair options are limited and factory service may be required.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 Control Board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f042-fault-code&k=Yaskawa+GA800+Control+Board&tag=errorcodefixes-20) \| Only if Yaskawa support confirms a control board fault after correct code diagnosis. |
| Yaskawa GA800 Cooling Fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f042-fault-code&k=Yaskawa+GA800+Cooling+Fan&tag=errorcodefixes-20) \| Only if the actual Yaskawa fault code indicates a fan or thermal fault. |

## When to Call a Pro

Call a qualified VFD technician or contact Yaskawa Technical Support immediately if you cannot positively identify the drive brand or if the fault code does not match any entry in the Yaskawa GA800 manual. VFD diagnostics require understanding of three-phase power systems, motor wiring, and manufacturer-specific fault logic. Applying the wrong manufacturer's procedures can damage the drive, create safety hazards, or void the warranty. If the drive is confirmed to be a Yaskawa GA800 and displays a legitimate Yaskawa fault code, the manual explicitly limits field repair to fan and control board replacement. All other repairs must be performed by Yaskawa or an authorized service center. For Allen Bradley PowerFlex 525 drives displaying F042, contact an Allen Bradley distributor or Rockwell Automation support for the correct Phase UW Short diagnostics.

**Rough cost:** A pro service call runs about $150-400 for Yaskawa-specific diagnostics and repair.
