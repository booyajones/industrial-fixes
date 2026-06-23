---
title: "Yaskawa GA800 A.119 Fault - Causes & Fix"
description: "A.119 on a Yaskawa GA800 means the safety input circuit is not satisfied. Most often a missing STO jumper or open safety relay contact."
pubDatetime: 2026-06-08T11:15:11Z
modDatetime: 2026-06-08T11:15:11Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
most_likely_cause: "Missing or disconnected STO jumper when no external safety circuit is used"
likelihood: "the most common cause"
diy_or_pro: "pro"
money_part: "STO jumper wire or terminal block jumper"
---

## Yaskawa GA800 A.119 Fault — What It Means

The A.119 alarm on a Yaskawa GA800 drive indicates the Safe Torque Off (STO) circuit is not in the expected closed state. The GA800 has a built-in STO safety function that uses dedicated terminals, and the drive will refuse to run if that circuit is open or miswired. If you are not using an external safety relay or E-stop system, the STO terminals must be jumpered together at the factory or during installation. If the jumper is missing or the safety contacts are not closing, the drive will throw this alarm and stay locked out.

Yaskawa's GA800 troubleshooting procedure says to locate the cause of the fault using the wiring diagram, correct the circuit condition, then reset the alarm from the keypad. The STO function is a two-terminal input arrangement, and both terminals must see continuity for the drive to consider the safety chain satisfied. Check your elementary diagram to see whether the drive was intended to run with a jumper or with external safety relay contacts feeding the STO inputs.

## Before You Replace Anything

Technicians sometimes replace the control board or main contactor when the real problem is simply a missing factory jumper on the STO terminals or a failed safety relay contact upstream. Always verify continuity through the entire safety chain and check the elementary diagram before ordering circuit boards.

[Jump to Fix](#fix)

## Common Causes

- **Missing STO terminal jumper (~45%)** When the GA800 is not integrated into a machine safety system, a jumper wire must connect the two STO terminals so the drive sees a closed loop.
- **Open safety relay contact (~30%)** An external safety relay or E-stop module is installed but its output contacts are not closing into the STO inputs, either because the relay is de-energized or the contact has failed.
- **Miswired STO terminals (~15%)** The wiring to the STO inputs was landed on the wrong terminals or reversed during installation or after service work.
- **Loose or corroded terminal connection (~10%)** A wire at the STO terminal block is not fully seated, or oxidation at the terminal prevents good continuity through the safety chain.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is a jumper wire present between the two STO terminals on the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The jumper is in place so an external safety relay or wiring problem is the next suspect. Move to checking upstream contacts.<br><strong>No:</strong> Install the required STO jumper across the two STO terminals, then reset the alarm from the keypad and test the drive.</div>
</details>

<details class="dtree"><summary>Is there an external E-stop button, safety relay, or light curtain wired into the STO circuit?</summary>
<div class="dtree-body"><strong>Yes:</strong> Verify that all external safety devices are energized and their contacts are closed. Check continuity from the relay output all the way to the drive STO input.<br><strong>No:</strong> The drive should be jumpered directly at the STO terminals. Confirm the jumper is tight and not damaged, then reset the alarm.</div>
</details>

<details class="dtree"><summary>Does the alarm clear after you reset it from the keypad?</summary>
<div class="dtree-body"><strong>Yes:</strong> The safety circuit is now satisfied. Document what was corrected and run a full function test of the drive and any safety interlocks.<br><strong>No:</strong> The safety chain still has an open or the drive may have a parameter mismatch. Consult the GA800 manual for STO parameter settings and verify the wiring against the elementary diagram.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Confirm the alarm code** on the keypad display and write down the exact fault number and any accompanying text to match it against the GA800 manual.
2. **Locate the STO terminals** on the GA800 using the terminal layout diagram in the drive manual or on the terminal cover label.
3. **Check for a jumper wire** across the two STO terminals if no external safety relay is used, and verify the jumper is tight and undamaged.
4. **If an external safety relay or E-stop is wired**, use a multimeter to verify continuity from the relay output contacts through the conductors to the drive STO input terminals.
5. **Inspect all STO terminal screws** for tightness and check that wire ferrules or ring terminals are not loose, broken, or corroded.
6. **Correct any open circuit** by installing the missing jumper, replacing the failed safety relay contact, or re-landing loose wires on the correct STO terminals.
7. **Reset the alarm** from the keypad per the GA800 operating manual, then attempt to start the drive and verify that the STO circuit remains satisfied during normal operation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| STO jumper wire or terminal block jumper | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-119-fault-code&k=STO+jumper+wire+or+terminal+block+jumper&tag=errorcodefixes-20) \| Consult the GA800 terminal diagram for the correct wire gauge and length if the factory jumper is lost. |
| Safety relay or E-stop module contacts | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-119-fault-code&k=Safety+relay+or+E-stop+module+contacts&tag=errorcodefixes-20) \| If your installation uses an external safety device, replace the relay or contact block that feeds the STO inputs. |

## When to Call a Pro

Call a qualified industrial electrician or drive technician if you are not trained to work inside motor control panels or if the safety circuit includes a programmable safety controller or light curtain system. High-voltage AC drive terminals carry lethal voltage even when the drive is faulted, and incorrectly wiring the STO circuit can defeat the machine's entire safety architecture. A pro will have the elementary diagrams, know the local electrical and machine safety codes, and can verify that the STO function meets the required safety integrity level for your application. If the alarm persists after you have verified the STO wiring and jumper, the drive may need parameter changes or a control board inspection that requires Yaskawa factory training.

**Rough cost:** A pro service call runs about $150-400.

## See Also

- [Yaskawa GA800 A.130 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-a-130-fault-code/)
- [Yaskawa GA800 E53 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e53-fault-code/)
- [Yaskawa GA800 E18 Fault Code - Causes & Fix](/posts/yaskawa-ga800-vfd-e18-fault-code/)
- [Yaskawa VFD Fault GF — Causes & Fix](/posts/yaskawa-vfd-fault-gf/)
