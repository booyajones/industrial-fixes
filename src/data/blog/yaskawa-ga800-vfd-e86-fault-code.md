---
title: "Yaskawa GA800 E86 Fault - Causes & Fix"
description: "E86 on a Yaskawa GA800 VFD is not documented in available manuals. Check your drive's keypad for the full alarm text and consult Yaskawa support."
pubDatetime: 2026-06-07T10:23:19Z
modDatetime: 2026-06-07T10:23:19Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
diy_or_pro: "pro"
---

## Yaskawa GA800 E86 Fault — What It Means

The E86 fault code is not explicitly defined in the available Yaskawa GA800 documentation. Yaskawa's troubleshooting approach for the GA800 requires reading both the numeric code and the full alarm text displayed on the keypad or monitoring screen, then cross-referencing the elementary diagram for the affected circuit. Without an official fault table entry for E86, the exact meaning can vary by drive firmware revision or configuration. The GA800 does include a Safe Torque Off (STO) safety function, and if the STO circuit is not satisfied the drive will not produce torque to the motor, which can cause drive faults. General troubleshooting begins with verifying safety wiring, checking for correct STO jumper or input connections, and reviewing the drive's alarm history. If the fault persists after basic checks, gather the model number, spec code, serial number, and failure details and contact Yaskawa technical support for the correct code interpretation and service path.

## Before You Replace Anything

Technicians sometimes replace the control board without first verifying the elementary diagram and checking the STO safety circuit wiring, which can be the actual source of the fault and costs nothing to inspect.

[Jump to Fix](#fix)

## Common Causes

- **Undocumented fault code** E86 does not appear in the manufacturer fault tables provided, so the exact trigger is unknown without contacting Yaskawa.
- **Safe Torque Off circuit not satisfied** The GA800 requires the STO input terminals to be correctly wired or jumpered, and an open or miswired STO circuit will prevent torque output and may generate faults.
- **Incorrect or missing elementary diagram reference** Yaskawa troubleshooting training emphasizes checking the elementary diagram before replacing parts, and skipping this step can lead to misdiagnosis.
- **Control board or internal component failure** The maintenance documentation lists the drive control board and fan as repairable components, and internal failures can produce obscure fault codes.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the keypad display a full alarm description in addition to E86?</summary>
<div class="dtree-body"><strong>Yes:</strong> Write down the complete text and cross-reference it with your drive's user manual or contact Yaskawa with that information.<br><strong>No:</strong> The code alone is insufficient. Check the alarm history menu on the keypad to see if additional context or prior faults are logged.</div>
</details>

<details class="dtree"><summary>Is the Safe Torque Off (STO) circuit wired and landed correctly per the elementary diagram?</summary>
<div class="dtree-body"><strong>Yes:</strong> STO is not the issue. Move to checking other wiring, reviewing parameter settings, and contacting Yaskawa support.<br><strong>No:</strong> Land the STO jumper or input wiring correctly. The drive will not run without a satisfied STO circuit.</div>
</details>

<details class="dtree"><summary>Have you reviewed the elementary diagram for the affected circuit before replacing any parts?</summary>
<div class="dtree-body"><strong>Yes:</strong> Good. If the diagram shows no wiring faults, gather the model/spec/serial information and call Yaskawa technical support.<br><strong>No:</strong> Stop. Consult the elementary diagram first to avoid replacing the wrong component.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Record the full alarm text** displayed on the GA800 keypad or monitoring screen, not just the E86 code number.
2. **Verify Safe Torque Off wiring** by checking that the STO input terminals on the drive are correctly landed or jumpered per the elementary diagram.
3. **Check the alarm history** in the keypad menu to see if prior faults or repeated E86 occurrences provide additional context.
4. **Consult the elementary diagram** for your specific GA800 model to identify the circuit associated with the fault before replacing any components.
5. **Gather drive information** including the full model number, spec code, serial number, and a description of when the fault occurs.
6. **Contact Yaskawa technical support** with the alarm text and drive details to obtain the official fault definition and recommended corrective action.
7. **Replace the control board or fan** only if Yaskawa support or the elementary diagram confirms a failed internal component and provides a part number.

## Parts Often Needed

| Part | Notes |
|------|-------|
| GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e86-fault-code&k=GA800+control+board&tag=errorcodefixes-20) \| Only replace if confirmed failed by Yaskawa support and the elementary diagram. Order using your drive's spec code. |
| GA800 cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e86-fault-code&k=GA800+cooling+fan&tag=errorcodefixes-20) \| Replacement fan is listed as a serviceable item in maintenance documentation. Verify part number with Yaskawa. |

## When to Call a Pro

Call a qualified VFD technician or Yaskawa support immediately if the E86 fault reappears after basic safety-circuit checks, if you do not have access to the drive's elementary diagram, or if the alarm text suggests an internal component failure. High-voltage AC drive troubleshooting requires lock-out/tag-out procedures, multimeter diagnostics on live circuits, and familiarity with Yaskawa parameter programming. Replacing the wrong board or ignoring the elementary diagram can cost hundreds of dollars and extend downtime. Yaskawa technical support can provide the official fault definition, remote diagnostics, and the correct part numbers for your specific drive revision.

**Rough cost:** A pro service call runs about $200–500.
