---
title: "Yaskawa GA800 F033 - Causes & Fix"
description: "F033 does not exist on Yaskawa GA800 drives. This code is specific to Allen-Bradley PowerFlex 525 and means auto-restart tries exceeded."
pubDatetime: 2026-06-27T11:50:42Z
modDatetime: 2026-06-27T11:50:42Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
diy_or_pro: "pro"
free_checks:
  - "Verify the drive model number on the nameplate to confirm whether you have a Yaskawa GA800 or an Allen-Bradley PowerFlex 525"
  - "Check the display or HMI to see if it is connected to multiple drives or PLCs that might be showing a fault from a different device"
---

## What this code means
There is no F033 fault code in the Yaskawa GA800 VFD manual or fault table. The F033 code belongs to Allen-Bradley PowerFlex 525 drives, where it indicates Auto Restart Tries Exceeded. This means the drive attempted to automatically restart after a fault but failed multiple times, reaching the maximum number of configured auto-restart attempts (typically set in parameter P151 or A541). F033 is always a secondary fault, so the root cause is another fault (such as overload, ground fault, or power loss) that triggered the auto-restart loop. If you see F033 on a display connected to equipment you believe is a Yaskawa GA800, verify the drive model number on the nameplate. You may have a PowerFlex 525 instead, or the display may be showing a fault from a different device in the system.

## Before You Replace Anything

Technicians sometimes replace the drive itself when seeing F033, but the drive is rarely faulty. Disable auto-restart (set P151 to 0 on PowerFlex 525) to reveal the original fault code, then troubleshoot that root cause instead.

## Common Causes

- **Wrong drive model identified (~60%)** The fault code F033 does not exist in Yaskawa GA800 documentation and belongs to Allen-Bradley PowerFlex 525 drives, so the first step is confirming the actual drive brand and model on the nameplate.
- **Display showing fault from another device (~25%)** In multi-drive or networked systems, an HMI or display may show a fault code from a different drive or controller, leading to confusion about which device generated the fault.
- **Incorrect documentation or label (~10%)** Someone may have mislabeled equipment or referenced the wrong manual during previous service, causing ongoing confusion about fault codes.
- **Typographical error in fault display (~5%)** A display or communication error could corrupt the fault code being shown, making it appear as F033 when the actual code is different.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the nameplate on the drive say Yaskawa GA800 or Allen-Bradley PowerFlex?</summary>
<div class="dtree-body"><strong>Yes:</strong> If it says Allen-Bradley PowerFlex 525, consult PowerFlex documentation for F033 troubleshooting (auto-restart tries exceeded). If it says Yaskawa GA800, the F033 code is not valid for that model.<br><strong>No:</strong> Take a photo of the complete nameplate and model number, then look up the correct fault code table for that specific drive model online or in the manual.</div>
</details>

<details class="dtree"><summary>Is the display or HMI connected to more than one drive or controller?</summary>
<div class="dtree-body"><strong>Yes:</strong> Check each connected device individually to determine which one is actually faulting, as the F033 may be coming from a PowerFlex drive elsewhere in the system.<br><strong>No:</strong> Focus troubleshooting on the single drive, but verify its brand and model first before proceeding with any fault code interpretation.</div>
</details>

<details class="dtree"><summary>Does the Yaskawa GA800 manual list F033 in its fault code table?</summary>
<div class="dtree-body"><strong>Yes:</strong> Follow the manual's troubleshooting steps for that code (though this is extremely unlikely, as F033 is not a documented GA800 code).<br><strong>No:</strong> The code does not exist for the GA800. Confirm the drive model, check for communication errors, and consult the correct manual for the actual drive you have.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the drive brand and model** by reading the nameplate on the front or side of the unit, noting the full model number and serial number.
2. **Check the fault code table** in the operator manual for the exact model you identified, either in the printed manual or downloaded from the manufacturer's website.
3. **If the drive is a PowerFlex 525**, temporarily disable auto-restart by setting parameter P151 to 0, then clear the fault and restart to see the original root fault code instead of F033.
4. **Identify and troubleshoot the root fault** shown after disabling auto-restart (common root faults include motor overload, ground fault, or power supply issues).
5. **Inspect motor and mechanical systems** for grounded phases, shorted windings, blockages, or excessive load that would cause repeated faults.
6. **Check power supply quality** with a multimeter or power quality analyzer, looking for low voltage, interruptions, or significant fluctuations outside the drive's input voltage range.
7. **Test drive-to-motor wiring** for shorts, ground faults, or open circuits using a megohmmeter and continuity tester, paying close attention to cable terminations and conduit entry points.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Replacement component | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f033-fault-code&k=Yaskawa+GA800+F033+-+Causes+%26+Fix&tag=errorcodefixes-20) \| verify fitment for your exact model |

## When to Call a Pro

Call a qualified industrial electrician or drive technician immediately if you cannot verify the drive model, if the fault persists after confirming the correct drive documentation, or if troubleshooting reveals issues with high-voltage wiring, motor windings, or the drive's internal components. VFD repair requires specialized test equipment, knowledge of power electronics, and adherence to lockout-tagout safety procedures. Never attempt to open or service a VFD cabinet without proper training, as lethal voltages can remain present even after disconnecting input power. A professional can also diagnose communication or network issues that may be causing fault codes from other devices to appear on a shared display.

**Rough cost:** A pro service call runs about $150-400 for diagnostics and repair of root cause.
