---
title: "Yaskawa GA800 E95 Fault - Causes & Fix"
description: "E95 on a Yaskawa GA800 VFD is not documented in available manuals. Check your exact model's fault list and wiring diagram before repair."
pubDatetime: 2026-06-07T10:30:44Z
modDatetime: 2026-06-07T10:30:44Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
diy_or_pro: "pro"
money_part: "Yaskawa GA800 control board"
most_likely_cause: "Misread or transposed code"
---

## Yaskawa GA800 E95 Fault — What It Means

An E95 fault code on the Yaskawa GA800 drive does not appear in the manufacturer troubleshooting documentation provided. Yaskawa assigns specific alphanumeric codes to each fault condition, but E95 is not confirmed for the GA800 series in available technical literature. You may be seeing a different code (such as UV3, which indicates a soft-charge answerback fault), a misread display, or a code specific to a custom parameter set or firmware revision. Before attempting any repair, verify the exact characters on the keypad, confirm your drive model number and firmware version, and consult the GA800 maintenance manual or wiring diagram for your unit.

Yaskawa training materials emphasize reading the elementary diagram first, then identifying what the fault code indicates before troubleshooting. If you cannot locate E95 in your manual, contact Yaskawa technical support with your drive serial number and the alarm history log to confirm the meaning and recommended corrective action.

## Before You Replace Anything

Technicians sometimes replace the control board or entire drive without verifying the fault code in the manual or checking simple wiring issues first. Always confirm the code meaning and inspect all connections and relay circuits before ordering expensive parts.

[Jump to Fix](#fix)

## Common Causes

- **Misread or transposed code** The display may show a different fault (such as UV3 or another alphanumeric code) that was read incorrectly in poor lighting or at an angle.
- **Custom parameter or firmware-specific alarm** Some drives running custom application code or older firmware revisions may display fault codes not listed in standard manuals.
- **Soft-charge bypass relay fault (if the code is actually UV3)** Damage to the relay or contactor on the soft-charge bypass circuit prevents the drive from receiving the expected answerback signal.
- **Control board communication error** A fault in the board's answerback circuit or internal diagnostics can trigger an unlisted or generic fault code.
- **Wiring or terminal connection issue** Loose, corroded, or incorrect wiring at control terminals can generate spurious fault codes that do not match standard lists.
- **Drive assembly internal failure** In rare cases, internal component damage can cause the drive to report a non-standard or corrupted fault code.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does your keypad clearly show E95, or could it be UV3, E.95, or another code?</summary>
<div class="dtree-body"><strong>Yes:</strong> Photograph the display and compare it to the fault list in your GA800 manual or contact Yaskawa support to confirm the code exists for your model.<br><strong>No:</strong> Write down the exact characters displayed, including any dots or dashes, and look up that code in the troubleshooting section of your drive's manual.</div>
</details>

<details class="dtree"><summary>Can you access the alarm history log (usually in the diagnostics menu)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Review the last five alarm entries to see if E95 repeats or if other codes appear before it, then cross-reference all codes in the manual.<br><strong>No:</strong> Power-cycle the drive once and note whether the same code appears immediately or if a different fault shows up.</div>
</details>

<details class="dtree"><summary>Do you have the GA800 maintenance manual and wiring diagram for your specific drive model and revision?</summary>
<div class="dtree-body"><strong>Yes:</strong> Look up the fault code table and the elementary diagram to identify the circuit or sensor involved, then follow the manual's corrective action steps.<br><strong>No:</strong> Download the manual from Yaskawa's website using your drive's model and serial number, or call Yaskawa technical support before attempting any repair.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the fault code** on the drive's keypad or HMI display. Write down every character, including letters, numbers, dots, and spaces, and photograph the screen if possible.
2. **Consult the GA800 fault code table** in the maintenance manual for your exact drive model and firmware revision. If E95 does not appear, check for similar codes such as UV3 or consult the alarm history log.
3. **Check parameter U4-06 [PreChargeRelayMainte]** if the fault is related to the soft-charge circuit. If the value exceeds 90%, the relay or control board may need replacement.
4. **Inspect all control wiring and terminals** for loose connections, corrosion, or damage. Refer to the elementary diagram to trace the circuit associated with the fault.
5. **Power-cycle the drive** by removing input power for at least 30 seconds, then re-energize and observe whether the fault clears or repeats.
6. **Contact Yaskawa technical support** with your drive's model number, serial number, firmware revision, and alarm history if the code remains unlisted or the fault persists after basic checks.
7. **Replace the control board or drive** only after confirming the fault code meaning and following the manufacturer's recommended corrective action for that specific code.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e95-fault-code&k=Yaskawa+GA800+control+board&tag=errorcodefixes-20) \| Order by drive model and revision; required if U4-06 exceeds 90% or answerback circuit is damaged. |
| Soft-charge bypass relay or contactor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e95-fault-code&k=Soft-charge+bypass+relay+or+contactor&tag=errorcodefixes-20) \| Confirm part number from the elementary diagram if the fault is related to precharge or UV3. |

## When to Call a Pro

Call a qualified drive technician or Yaskawa-certified service provider if you cannot locate the fault code in your manual, if the alarm history shows multiple or intermittent faults, or if the drive does not clear the fault after a power cycle. High-voltage work inside a VFD requires specialized training and test equipment. Do not open the drive or attempt board-level repairs unless you are trained in electrical safety and have confirmed the code meaning and corrective action with the manufacturer.

**Rough cost:** A pro service call runs about $200–800 depending on the actual fault and whether a relay, board, or drive replacement is needed.
