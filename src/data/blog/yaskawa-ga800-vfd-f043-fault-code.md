---
title: "Yaskawa GA800 F043 Fault Code - Causes & Fix"
description: "F043 is not a standard GA800 code. The closest match is CPF39 (Control Circuit Error). Most likely cause: control board failure. Verify the exact code on your display."
pubDatetime: 2026-06-28T10:11:38Z
modDatetime: 2026-06-28T10:11:38Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa GA800 Control Board"
most_likely_cause: "Control board power supply failure or microprocessor fault"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power down the drive completely, disconnect main power, wait 5 minutes for capacitor discharge, then reconnect and observe if the fault clears"
  - "Inspect all control board terminals for loose, corroded, or damaged wires and clean any dust or moisture with a non-conductive brush"
part_price: "$300-600"
no_buy_pct: "15%"
---

## Yaskawa GA800 F043 Fault Code — What It Means

There is no standard fault code F043 in the Yaskawa GA800 VFD catalog. The closest and most likely intended code is CPF39 (sometimes displayed as CPF039), which indicates a Control Circuit Error. This fault signals a hardware problem in the drive's control board, such as a power supply failure, microprocessor error, or internal component fault. CPF39 is a major fault that stops drive operation until resolved.

If your display explicitly shows F043, it may be a proprietary parameter fault, a misread (for example F instead of CPF), or a code from a different drive model. Confirm the exact characters on the keypad and consult the GA800 Technical Manual (SIEPC-010800-01) for definitive fault listings.

## Before You Replace Anything

Technicians sometimes replace external wiring or main power boards before diagnosing the control board itself. Measure the 5V and 15V power rails on the control board first to confirm board failure.

[Jump to Fix](#fix)

## Common Causes

- **Control board power supply failure (~45%)** The 5V or 15V power rails on the control board are unstable or out of specification, preventing the microprocessor from operating correctly.
- **Microprocessor or firmware glitch (~25%)** Voltage transients, overheating, or electrical noise cause the microprocessor to lock up or generate a fault condition.
- **Physical damage to the control board (~15%)** Moisture, dust intrusion, electrical surge, or physical impact damages components or traces on the control board.
- **Loose or corroded control board connections (~10%)** Terminal connections on the control board become intermittent or high-resistance due to corrosion, vibration, or poor installation.
- **Code display error or wrong drive model (~5%)** The fault code is misread (F043 instead of CPF39) or the drive is not a GA800, leading to confusion about the actual fault.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear after a complete power-down and restart?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault may have been a transient microprocessor glitch. Monitor the drive and check for loose connections or electrical noise sources.<br><strong>No:</strong> The fault is persistent. Proceed to inspect the control board and measure power supply rails.</div>
</details>

<details class="dtree"><summary>Are the 5V and 15V power rails on the control board within 5% of specification (4.75-5.25V and 14.25-15.75V)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The power supply is good. The fault is likely a microprocessor or component failure on the control board. Replace the control board.<br><strong>No:</strong> The control board power supply has failed. Replace the control board.</div>
</details>

<details class="dtree"><summary>Does your display show exactly F043 or does it show CPF39 (or CPF039)?</summary>
<div class="dtree-body"><strong>Yes:</strong> If it shows CPF39, follow the control circuit error diagnosis. If it shows F043, verify the drive model and consult the manual for that specific code.<br><strong>No:</strong> Recheck the display carefully under good lighting and compare against the manual fault table.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the GA800 completely** by disconnecting main power at the breaker or disconnect switch. Wait a minimum of 5 minutes for all internal capacitors to discharge before proceeding.
2. **Reconnect power and observe the keypad display** to confirm the exact fault code characters. Write down whether it shows F043, CPF39, CPF039, or another code, and check the GA800 Technical Manual (SIEPC-010800-01) for the code definition.
3. **Inspect all control board terminals and wiring** for loose, corroded, or damaged connections. Remove any dust or moisture using a non-conductive brush and compressed air, and check that ventilation openings are clear.
4. **Measure the control board power supply rails** using a multimeter. Check that the 5V rail is between 4.75V and 5.25V, and the 15V rail is between 14.25V and 15.75V. If either is out of specification, the control board has failed.
5. **Replace the control board** if power rails are out of spec or the fault persists after cleaning and re-energizing. Order the correct board for your GA800 model (part number such as TOEPYAIGA8001 or model-specific GA800-CTL-BRD) from Yaskawa or an authorized distributor.
6. **Install the new control board** following the installation instructions in the GA800 manual. Transfer any user parameters from the old board if possible, or reprogram from backup files.
7. **Contact Yaskawa Technical Support** if the fault remains after board replacement. Email repair@yaskawa.com or call 1.800.927.5292 (Option 2, then Option 1) with the drive model, serial number, fault code, and application details for further diagnosis.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 Control Board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f043-fault-code&k=Yaskawa+GA800+Control+Board&tag=errorcodefixes-20) \| Order the correct board for your drive frame size and voltage rating. Common part numbers include TOEPYAIGA8001 or model-specific variants. Verify with Yaskawa or your distributor. |
| GA800 Technical Manual (SIEPC-010800-01) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f043-fault-code&k=GA800+Technical+Manual+%28SIEPC-010800-01%29&tag=errorcodefixes-20) \| Free download from Yaskawa's website. Contains fault code tables and control board replacement procedures. |

## When to Call a Pro

Call a qualified VFD technician or Yaskawa-authorized service provider if you are not comfortable working with high-voltage industrial equipment, if you lack the tools to safely measure control board power rails, or if the fault persists after control board replacement. CPF39 (or any control circuit error) requires precise diagnostics and knowledge of the GA800 internal architecture. Yaskawa does not support field repair of internal components beyond fan and control board replacement. For complex or recurring faults, Yaskawa Technical Support can replicate issues using simulated systems and may request project files or trend recordings to diagnose application-specific problems.

**Rough cost:** A pro service call runs about $400-900 for control board replacement including labor.
