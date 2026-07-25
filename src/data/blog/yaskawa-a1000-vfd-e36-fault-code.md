---
title: "Yaskawa A1000 VFD E36 Fault - Causes & Fix"
description: "E36 indicates an encoder or PG (pulse generator) feedback error. Check encoder cable connections and wiring before replacing parts."
pubDatetime: 2026-07-23T07:32:23Z
modDatetime: 2026-07-23T07:32:23Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Encoder feedback cable"
most_likely_cause: "Loose or damaged encoder cable connections"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect encoder cable connections at both the motor and drive terminals for looseness or corrosion"
  - "Check parameter settings to confirm encoder type and resolution match the installed hardware"
  - "Power-cycle the drive after reseating all encoder connections"
---

## Yaskawa A1000 VFD E36 Fault — What It Means

The E36 fault on a Yaskawa A1000 variable frequency drive indicates a problem with the encoder or pulse generator (PG) feedback circuit. The drive expects a certain type of feedback signal from the motor's encoder to maintain accurate speed and position control, and this code appears when the signal is missing, corrupted, or does not match the configured parameters. The fault protects the motor and driven equipment from operating without proper feedback.

This error commonly appears on startup or during operation when the drive cannot read the encoder properly. It can be triggered by wiring issues, incorrect parameter settings for the encoder type, a damaged encoder, or a failed encoder interface card inside the drive. Because encoder feedback is optional on many VFD installations, verify that your application actually uses an encoder before troubleshooting encoder-specific hardware.

## Before You Replace Anything

Technicians often replace the encoder or the drive's encoder interface card without first checking cable continuity and shielding. A simple cable continuity test and visual inspection of terminations will catch most wiring faults and save hundreds of dollars.

[Jump to Fix](#fix)

## Common Causes

- **Loose or damaged encoder cable (~40%)** Vibration, installation errors, or cable flexing can break encoder wires or loosen terminations, interrupting the feedback signal.
- **Incorrect encoder parameter settings (~25%)** Mismatched settings for encoder type, pulse count, or voltage level prevent the drive from interpreting the signal correctly.
- **Failed encoder (~20%)** The encoder itself can fail due to bearing wear, contamination, or electrical damage from voltage spikes.
- **Faulty encoder interface card (~10%)** The optional encoder feedback card inside the drive can develop component failures or poor board connections.
- **Electrical noise or grounding issues (~5%)** Improper cable shielding or ground loops inject noise into the low-voltage encoder signal, corrupting the data.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the encoder cable shielded and grounded at only one end?</summary>
<div class="dtree-body"><strong>Yes:</strong> Grounding is correct; proceed to check cable continuity and terminations.<br><strong>No:</strong> Multiple ground points or unshielded cable can cause noise; correct the grounding per drive manual and retest.</div>
</details>

<details class="dtree"><summary>Do the encoder type and resolution parameters in the drive match the nameplate on the motor encoder?</summary>
<div class="dtree-body"><strong>Yes:</strong> Parameters are set correctly; focus on cable and encoder hardware.<br><strong>No:</strong> Reprogram the encoder parameters to match the actual encoder and clear the fault.</div>
</details>

<details class="dtree"><summary>Does the encoder spin freely and show no physical damage or contamination?</summary>
<div class="dtree-body"><strong>Yes:</strong> Encoder mechanically intact; test cable continuity and check for signal at drive terminals.<br><strong>No:</strong> Replace the encoder and verify cable integrity before restarting.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down and lock out** the drive at the main disconnect before working on any wiring or internal components.
2. **Inspect the encoder cable** from motor to drive, looking for pinched insulation, broken conductors, or loose connectors at both ends.
3. **Check encoder cable continuity** with a multimeter, testing each wire and verifying shield integrity; replace cable if any circuit is open.
4. **Verify encoder parameter settings** in the drive menu (consult your model's parameter manual for encoder type, pulses per revolution, and voltage level) and correct any mismatches.
5. **Reseat or replace the encoder interface card** inside the drive if cable and parameters are confirmed correct; power down first and follow ESD precautions.
6. **Test encoder output** by slowly rotating the motor shaft by hand (with power off) and measuring signal continuity, or use a scope to view pulses with power on and drive disabled.
7. **Clear the fault** and run a no-load test, monitoring for stable encoder feedback and smooth motor acceleration before returning to production.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Encoder feedback cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-e36-fault-code&k=Encoder+feedback+cable&tag=errorcodefixes-20) \| Match the connector type and length to your installation; use shielded twisted-pair cable rated for encoder service. |
| Rotary encoder | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-e36-fault-code&k=Rotary+encoder&tag=errorcodefixes-20) \| Verify pulse count, output type (differential or single-ended), and mounting dimensions match your motor. |
| Encoder interface card (PG card) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-e36-fault-code&k=Encoder+interface+card+%28PG+card%29&tag=errorcodefixes-20) \| Order the correct option card model for your A1000 drive from Yaskawa or an authorized distributor. |

## When to Call a Pro

Call a qualified VFD technician or electrician if you are not trained in variable frequency drive programming and high-voltage wiring. Encoder troubleshooting requires familiarity with drive parameters, signal measurement with an oscilloscope, and safe handling of industrial control circuits. A technician can quickly verify cable integrity, check encoder output waveforms, and reprogram parameters without risking additional faults or motor damage. Professional service is also necessary if you need to replace the encoder interface card inside the drive, as this involves working near live DC bus components even after input power is removed.

**Rough cost:** A pro service call runs about $200-600.
