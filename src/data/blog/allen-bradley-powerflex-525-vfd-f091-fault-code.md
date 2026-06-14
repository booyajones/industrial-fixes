---
title: "Allen-Bradley F091 Encoder Loss - Causes & Fix"
description: "F091 means Encoder Loss on the PowerFlex 525 VFD. One of the two differential encoder channels is missing. Check wiring first."
pubDatetime: 2026-06-12T10:25:50Z
modDatetime: 2026-06-12T10:25:50Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - allen-bradley
money_part: "Differential encoder (model-specific to your motor and application)"
most_likely_cause: "Open, loose, or damaged encoder wiring"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect encoder cable and connectors at the encoder, drive, and any junction points for loose, damaged, or corroded pins."
  - "Cycle power on the drive to clear the fault after re-seating connections and verify if the fault returns immediately."
---

## Allen-Bradley F091 Encoder Loss — What It Means

The F091 fault on an Allen-Bradley PowerFlex 525 VFD indicates Encoder Loss. This fault occurs when the drive is configured to use a differential encoder and one of the two required encoder channel signals (A+ and A-, or B+ and B-) is not being received. The drive depends on both quadrature channels to calculate speed and position feedback. When one channel disappears, the drive cannot trust the feedback loop and trips the fault to protect the system.

In practical terms, the encoder feedback circuit is incomplete. The drive may be missing a signal because of a broken wire, a loose connector, incorrect configuration, or a failed encoder. Rockwell also notes a specific case in positioning applications with Quad Check mode enabled, where channel inputs or motor leads may need to be swapped to correct the phase relationship.

## Before You Replace Anything

Technicians sometimes replace the encoder before checking the wiring and terminations. Inspect all encoder cable connections, shield continuity, and connector pins before swapping the encoder.

[Jump to Fix](#fix)

## Common Causes

- **Open, loose, or damaged encoder wiring (~50%)** A broken wire, loose connector pin, or damaged shield on the encoder cable will cause one channel signal to drop out and trigger F091.
- **Failed encoder hardware (~30%)** The encoder itself can fail internally, losing the ability to generate one or both quadrature channels even when wiring is intact.
- **Incorrect encoder feedback configuration (~10%)** If the drive is set for a differential encoder but the connected encoder is single-ended, or if Quad Check positioning mode requires swapped inputs, the drive will see a missing channel.
- **Swapped or miswired encoder channels (~5%)** In positioning applications with Quad Check enabled (A535 set to 5), Rockwell notes that encoder channel inputs or two motor leads may need to be swapped to correct phase relationship.
- **Drive control module feedback circuitry failure (~5%)** When wiring, configuration, and encoder are verified good but the fault persists, the feedback input circuitry on the control module may be damaged.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the encoder cable have any visible damage, loose connectors, or corroded pins?</summary>
<div class="dtree-body"><strong>Yes:</strong> Repair or replace the encoder cable and connectors, then cycle power and retest.<br><strong>No:</strong> Move on to verifying drive configuration and encoder type match.</div>
</details>

<details class="dtree"><summary>Is the drive configured for Positioning with Quad Check (A535 set to 5)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Swap the encoder A/B channel inputs or swap any two motor leads per Rockwell's note, then cycle power and retest.<br><strong>No:</strong> Verify the encoder type matches the drive's feedback configuration (differential vs. single-ended).</div>
</details>

<details class="dtree"><summary>After correcting wiring and configuration, does the fault clear and stay away?</summary>
<div class="dtree-body"><strong>Yes:</strong> The issue was wiring or setup related, and the drive should now operate normally.<br><strong>No:</strong> Replace the encoder. If the fault still persists after encoder replacement, suspect the drive's control module feedback circuitry.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the fault code** on the PowerFlex 525 display and confirm it reads F091 Encoder Loss.
2. **Inspect all encoder wiring** at the encoder body, drive terminals, and any inline connectors for loose pins, opens, breaks, or damaged shielding.
3. **Check the encoder type and drive configuration** to confirm the application uses a differential encoder as required for F091, and verify parameter A535 (Motor Fdbk Type) matches the installed encoder.
4. **If configured for Positioning with Quad Check** (A535 = 5), swap the encoder A and B channel inputs at the drive terminals, or swap any two motor leads, per Rockwell's troubleshooting note.
5. **Cycle power on the drive** to clear the fault after correcting wiring or configuration, then run the motor and observe whether F091 returns.
6. **Replace the encoder** if wiring and configuration are correct but the fault persists or returns immediately.
7. **Replace the drive control module** if a known-good encoder and verified wiring still produce F091, indicating a feedback-circuit fault in the drive itself.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Differential encoder (model-specific to your motor and application) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f091-fault-code&k=Differential+encoder+%28model-specific+to+your+motor+and+application%29&tag=errorcodefixes-20) \| Verify encoder type, resolution, and connector pinout match the original before ordering. |
| Encoder cable assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f091-fault-code&k=Encoder+cable+assembly&tag=errorcodefixes-20) \| Use shielded cable rated for the encoder signal type and drive input requirements. |
| PowerFlex 525 control module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f091-fault-code&k=PowerFlex+525+control+module&tag=errorcodefixes-20) \| Required only if encoder and wiring are verified and the fault persists, indicating internal feedback-circuit damage. |

## When to Call a Pro

Call a qualified industrial electrician or controls technician for F091 faults. Encoder troubleshooting requires measuring differential signals, verifying quadrature phase relationships, and working safely around live VFD terminals and motor circuits. If the encoder and wiring check out, diagnosing internal drive feedback circuitry or replacing the control module demands factory training and proper test equipment. Incorrect wiring or configuration in positioning applications can cause runaway motor behavior or damage to machinery, so professional diagnosis is the safer route.

**Rough cost:** A pro service call runs about $200-500 depending on encoder model and labor.
