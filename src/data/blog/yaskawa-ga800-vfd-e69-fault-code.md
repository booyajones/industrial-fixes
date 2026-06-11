---
title: "Yaskawa GA800 E69 Fault - Causes & Fix"
description: "E69 on a Yaskawa GA800 VFD means a Safe Torque Off (STO) safety input problem. The most common fix is installing the STO jumper."
pubDatetime: 2026-06-07T10:10:54Z
modDatetime: 2026-06-07T10:10:54Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
most_likely_cause: "Missing or removed STO jumper on terminals M3 and M4"
likelihood: "the most common field cause"
diy_or_pro: "pro"
money_part: "STO jumper wire or terminal block jumper"
---

## Yaskawa GA800 E69 Fault — What It Means

An E69 fault on the Yaskawa GA800 variable frequency drive indicates the Safe Torque Off (STO) safety circuit is not satisfied. The drive will not enable torque output because it sees an open or incorrect safety input. This is a protective feature, not a motor or overload fault.

The GA800 uses dedicated STO input terminals (M3 and M4) that must be bridged by a jumper when no external safety device is used, or wired to a closed safety relay contact when integrated into a safety system. If the drive does not see a complete circuit on those inputs, it will trip E69 and block torque.

## Before You Replace Anything

Technicians sometimes replace the control board or motor when seeing a safety fault, but E69 is almost always a wiring or external-contact issue. Always verify the STO jumper and safety-relay continuity before ordering drive components.

[Jump to Fix](#fix)

## Common Causes

- **Missing STO jumper** If the drive is meant to run without external safety gating, a factory jumper must connect the STO terminals M3 and M4, and removing or losing it will trip E69.
- **Open safety relay or contact** An external safety relay used to gate the STO inputs may have dropped out, failed, or lost power, opening the safety loop.
- **Miswired STO inputs** Incorrect terminal assignment or field wiring after commissioning changes can leave the STO circuit incomplete.
- **Loose or corroded terminal connections** Bad connections at the drive STO terminals, safety relay, or terminal strip will open the safety circuit and trigger the fault.
- **Incorrect parameter configuration** If the drive was reinitialized or parameters restored from backup, the STO configuration may not match the installed wiring.
- **Failed safety-relay output** The output contacts of the external safety relay or controller may have worn out or welded, preventing proper STO-loop closure.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is there a wire jumper installed between terminals M3 and M4 on the drive (when no external safety device is used)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The jumper is present. Move to checking external safety wiring and relay contacts for an open circuit.<br><strong>No:</strong> Install the factory STO jumper between M3 and M4, then try to clear the fault and enable the drive.</div>
</details>

<details class="dtree"><summary>Does the machine use an external safety relay or e-stop circuit wired to the STO inputs?</summary>
<div class="dtree-body"><strong>Yes:</strong> Measure continuity through the entire safety chain from the relay output to the drive STO terminals to find the open point.<br><strong>No:</strong> The drive should have the jumper installed. Verify the jumper is intact and seated, then check the drive terminal block for damage.</div>
</details>

<details class="dtree"><summary>After ensuring the STO circuit is complete, does the fault clear when you reset the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The wiring or jumper repair solved the problem. Return the machine to service and monitor for recurrence.<br><strong>No:</strong> The drive's STO input circuitry or control board may have failed. Consult a Yaskawa service center or qualified VFD technician.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Lock out and tag out** all power sources to the drive and machine, then verify zero voltage before opening any covers or touching terminals.
2. **Retrieve the fault history** from the GA800 keypad or parameter list to confirm the exact alarm code and any associated timestamps or conditions.
3. **Locate the STO terminals** M3 and M4 on the drive control terminal strip and identify whether the application uses a jumper or external safety wiring.
4. **Check for the factory jumper** if the drive is supposed to run without external safety gating, and install or replace it if missing or damaged.
5. **Trace the external safety circuit** from the safety relay output through field wiring to the drive STO inputs, using a multimeter to measure continuity at each connection point.
6. **Inspect all terminal connections** for loose screws, broken wires, or corrosion, and clean or tighten as needed.
7. **Verify safety-relay operation** by manually tripping and resetting the e-stop or safety gate, and confirming the relay contacts close and open as expected.
8. **Review the drive parameters** related to STO and digital-input assignment to make sure the configuration matches the installed wiring and machine documentation.
9. **Re-energize the drive** and attempt to clear the E69 fault, then run the machine through a test cycle to confirm torque output is restored and the fault does not recur.

## Parts Often Needed

| Part | Notes |
|------|-------|
| STO jumper wire or terminal block jumper | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e69-fault-code&k=STO+jumper+wire+or+terminal+block+jumper&tag=errorcodefixes-20) \| Factory part if the original was lost; consult the GA800 installation manual for the correct jumper style. |
| Safety relay (machine-specific model) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e69-fault-code&k=Safety+relay+%28machine-specific+model%29&tag=errorcodefixes-20) \| Replace only if testing confirms the relay output contacts are failed or the coil does not energize. |
| Field wiring harness for STO inputs | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e69-fault-code&k=Field+wiring+harness+for+STO+inputs&tag=errorcodefixes-20) \| Order or fabricate per the machine's electrical schematic if the existing harness is damaged or corroded beyond repair. |

## When to Call a Pro

Call a qualified VFD or controls technician if you are unfamiliar with industrial safety circuits, the machine uses a configurable safety controller that requires programming, or the fault persists after verifying all STO wiring and jumpers are correct. Drives with failed STO input circuitry require factory or authorized service-center repair. Any work on high-voltage drive terminals or integrated safety systems should be performed only by trained personnel with proper lockout/tagout procedures.

**Rough cost:** A pro service call runs about $150–400 depending on whether it is a simple jumper install or safety-relay replacement and wiring repair.
