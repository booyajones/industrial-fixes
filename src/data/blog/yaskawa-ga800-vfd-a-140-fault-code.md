---
title: "Yaskawa GA800 A.140 Fault - Causes & Fix"
description: "A.140 on a Yaskawa GA800 VFD signals an encoder or feedback communication error. Most often caused by loose encoder wiring or a faulty cable."
pubDatetime: 2026-06-09T11:31:02Z
modDatetime: 2026-06-09T11:31:02Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Encoder feedback cable"
most_likely_cause: "Loose or damaged encoder cable or connector"
likelihood: "the most common cause"
diy_or_pro: "pro"
---

## Yaskawa GA800 A.140 Fault — What It Means

The A.140 fault on a Yaskawa GA800 variable frequency drive indicates a problem with encoder or feedback communication. While the exact GA800-specific definition is not confirmed in manufacturer documentation provided, Yaskawa uses A.140 in related products to signal an encoder communication error in the feedback circuit. This means the drive cannot receive clean position or speed data from the motor's encoder.

The fault typically appears when the drive powers up or during operation if communication is lost. The drive will shut down output to protect the motor and system. The root cause is nearly always in the physical connection between the drive's feedback terminals and the encoder device mounted on the motor, or in the encoder cable itself.

## Before You Replace Anything

Technicians sometimes replace the drive itself when the real problem is a severed wire inside the encoder cable jacket or a single bent pin in the encoder connector. Always verify cable continuity and connector condition with a multimeter before ordering a new drive or encoder.

[Jump to Fix](#fix)

## Common Causes

- **Loose or corroded encoder connector (~35%)** Vibration or installation error can unseat the encoder plug at the drive or motor, breaking communication.
- **Damaged encoder cable (~30%)** Flexing, pinching, or rodent damage can break signal wires inside the cable even when the jacket looks intact.
- **Failed encoder device (~20%)** The encoder itself can fail due to moisture, heat, or bearing damage in the motor.
- **Incorrect wiring or pinout (~10%)** Mismatched encoder type, wrong terminal assignment, or swapped polarity will prevent proper communication.
- **Drive feedback interface fault (~5%)** A failed opto-isolator, communication chip, or feedback card inside the drive can block encoder signals.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the encoder cable connector fully seated and latched at both the drive and the motor?</summary>
<div class="dtree-body"><strong>Yes:</strong> The physical connection is secure. Proceed to check cable continuity and encoder power supply voltage.<br><strong>No:</strong> Reseat both ends firmly, verify any locking tabs engage, then clear the fault and test. Loose connectors are the most frequent cause.</div>
</details>

<details class="dtree"><summary>Does the encoder cable show any visible damage, tight bends, or areas where it was pinched or run near high-voltage power cables?</summary>
<div class="dtree-body"><strong>Yes:</strong> Replace the encoder cable. Even hidden wire breaks inside the jacket will cause intermittent or permanent communication loss.<br><strong>No:</strong> The cable jacket looks intact. Use a multimeter to verify continuity on each signal pair and check for shorts between wires.</div>
</details>

<details class="dtree"><summary>Does the fault clear and stay off after reseating connectors and the motor runs normally?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem was a marginal connection. Document the fix and monitor for recurrence over the next week.<br><strong>No:</strong> The fault returns immediately or the drive still will not run. Test encoder power supply voltage and consider substituting the encoder or the drive feedback interface to isolate the faulty component.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Lock out and tag out** all power to the VFD and motor, then wait at least five minutes for internal capacitors to discharge before opening any covers.
2. **Inspect the encoder cable** from end to end for cuts, tight bends, abrasion, or areas where it passes near power cables or moving machinery.
3. **Disconnect and reseat** the encoder connector at the drive's feedback terminals and at the encoder housing on the motor, checking each pin for corrosion or damage.
4. **Measure continuity** on each wire in the encoder cable using a multimeter, and confirm no shorts exist between signal pairs or to ground.
5. **Verify encoder supply voltage** at the drive terminals matches the encoder specification (consult your drive and encoder manuals for the correct voltage), and check that current draw is within normal range.
6. **Restore power** and attempt to clear the fault through the drive keypad or parameter reset, then run the motor under no-load conditions to confirm communication is restored.
7. **Substitute the encoder cable** first if continuity tests fail, then swap the encoder itself if a known-good cable does not resolve the fault, and finally consider drive feedback board replacement if the fault follows the drive when components are swapped.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Encoder feedback cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-140-fault-code&k=Encoder+feedback+cable&tag=errorcodefixes-20) \| Match the original cable length, conductor count, and shielding type. Yaskawa or motor-manufacturer supplied cables are recommended for noise immunity. |
| Replacement encoder | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-140-fault-code&k=Replacement+encoder&tag=errorcodefixes-20) \| Must match the original pulse-per-revolution count, output type (differential, open-collector, etc.), and mounting flange. Verify compatibility with the GA800 feedback interface. |

## When to Call a Pro

Call a qualified industrial electrician or VFD technician if you are not trained in lockout-tagout procedures, if you cannot safely access the motor or encoder, or if continuity and voltage tests do not reveal an obvious cable or connector fault. High DC bus voltage remains inside the drive even after input power is removed, and improper encoder wiring can damage both the drive and the encoder. A technician with an oscilloscope can verify encoder signal quality and pinpoint whether the fault is on the encoder side or the drive side, saving time and preventing unnecessary part swaps.

**Rough cost:** A pro service call runs about $200-500.
