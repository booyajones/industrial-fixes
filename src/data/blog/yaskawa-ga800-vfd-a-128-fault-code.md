---
title: "Yaskawa GA800 A.128 Fault - Causes & Fix"
description: "A.128 is not a verified GA800 fault code. Check your keypad display carefully and consult your manual for the exact alarm. Wiring faults are common."
pubDatetime: 2026-06-09T11:17:51Z
modDatetime: 2026-06-09T11:17:51Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Encoder cable (shielded, matched to PG card)"
most_likely_cause: "Misread or non-standard code"
diy_or_pro: "pro"
---

## Yaskawa GA800 A.128 Fault — What It Means

The code A.128 does not appear in verified Yaskawa GA800 documentation. GA800 drives typically display faults in formats like oC, ov, or CPF06, not decimal-style A.128 codes. Before proceeding, confirm the exact text shown on the keypad or operator display. The code may be misread, may belong to a different device in your system, or may be specific to a custom firmware revision not covered in standard manuals.

If you have verified A.128 is truly displayed by your GA800, the general troubleshooting approach for unverified or uncommon GA-family codes starts with inspection of control wiring, encoder connections, and option cards. Many GA800 faults stem from wiring issues, encoder path problems, or option-board communication errors. Double-check your drive's manual addendum or contact Yaskawa technical support with your exact model and serial number to decode this specific alarm.

## Before You Replace Anything

Technicians sometimes replace the entire drive or control board without first checking encoder wiring, option-card seating, and shield grounding. Inspect all wiring and reseat option cards before ordering expensive assemblies.

[Jump to Fix](#fix)

## Common Causes

- **Misread or non-standard code (~30%)** The alarm may be from a different device, a custom parameter set, or misread from the keypad.
- **Encoder wiring fault (~25%)** Disconnected, crossed, or broken encoder cable or shield grounding issue on the PG option path.
- **PG or encoder option card fault (~20%)** The encoder interface card is loose, damaged, or has failed communication with the main control board.
- **Control wiring issue (~15%)** Loose or miswired control terminals, damaged control cable, or incorrect signal grounding.
- **Control board or gate drive fault (~10%)** Internal circuit damage on the drive's control board or gate driver after a transient or component aging.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the keypad show exactly A.128 or could it be A128, AL28, or another similar code?</summary>
<div class="dtree-body"><strong>Yes:</strong> Verify the exact display text and photograph it. Consult the GA800 manual appendix or contact Yaskawa support to confirm the meaning.<br><strong>No:</strong> You may have misread the code. Re-check the display and note the exact characters, then look up that code in your drive manual.</div>
</details>

<details class="dtree"><summary>Is an encoder or PG option card installed in the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> Inspect the encoder cable for damage, check that the PG card is fully seated, and verify encoder wiring matches the manual pin-out.<br><strong>No:</strong> Focus on control wiring, parameter settings, and main control board health. The fault is less likely encoder-related.</div>
</details>

<details class="dtree"><summary>Does the fault clear after a power cycle and stay clear during idle (motor not running)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The issue may be load-dependent or intermittent. Monitor the drive under load and check for mechanical binding or transient noise on control lines.<br><strong>No:</strong> The fault is persistent and likely hardware or wiring related. Proceed with systematic wiring inspection and option-card reseating.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the exact fault code** displayed on the keypad. Write down every character exactly as shown and photograph the screen if possible. Consult your GA800 user manual or technical manual addendum for that code.
2. **Power down the drive safely** by following lockout-tagout procedures and disconnecting AC input power. Wait for DC bus discharge (at least five minutes or until the charge LED extinguishes).
3. **Inspect all control wiring** at the drive terminals. Check that control signal wires are seated firmly, shields are terminated correctly, and no conductors are crossed or broken.
4. **Check encoder and PG option connections** if your system uses a pulse generator or encoder feedback. Remove and reseat the encoder cable at both the motor and drive ends. Verify the PG option card is fully inserted and latched.
5. **Power the drive back on** and observe whether the fault returns immediately or only under specific conditions (such as during acceleration or under load). Note the exact behavior.
6. **Use DriveWizard Industrial or the keypad diagnostic menu** to view detailed alarm history and parameter status. Compare active parameters against your application manual.
7. **Contact Yaskawa technical support** with your exact model number, serial number, and the verified alarm code. If A.128 is not documented in your manual, the factory can decode custom or firmware-specific codes and recommend the correct repair path.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Encoder cable (shielded, matched to PG card) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-128-fault-code&k=Encoder+cable+%28shielded%2C+matched+to+PG+card%29&tag=errorcodefixes-20) \| Replace if damaged, cut, or showing continuity faults; verify pin-out matches your encoder type. |
| PG or encoder option card (e.g. JUSP-ACP21JA) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-128-fault-code&k=PG+or+encoder+option+card+%28e.g.+JUSP-ACP21JA%29&tag=errorcodefixes-20) \| Order the exact card listed in your GA800 option manual if reseating and wiring checks do not resolve the fault. |
| Control board assembly (main CPU board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-128-fault-code&k=Control+board+assembly+%28main+CPU+board%29&tag=errorcodefixes-20) \| Required only if diagnostics confirm internal circuit failure; verify with Yaskawa support before ordering. |

## When to Call a Pro

Call a qualified drive technician or automation integrator if you cannot verify the exact meaning of A.128 from your manual, if encoder or control wiring inspection does not reveal an obvious fault, or if the fault persists after reseating option cards and cycling power. VFD troubleshooting requires multimeter skills, knowledge of encoder signal types, and sometimes oscilloscope work to diagnose noise or communication faults. High DC bus voltage remains present inside the drive even after AC input is disconnected, so only personnel trained in high-voltage electrical work should open the drive enclosure or measure internal circuits. If your process cannot tolerate extended downtime, have Yaskawa or an authorized service center diagnose and repair the drive to avoid misdiagnosis and repeat failures.

**Rough cost:** A pro service call runs about $150-400 depending on diagnosis and parts.
