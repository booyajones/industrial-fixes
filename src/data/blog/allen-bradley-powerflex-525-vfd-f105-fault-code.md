---
title: "Allen-Bradley PowerFlex 525 F105 - Causes & Fix"
description: "F105 (C Connect Err) means the control module lost connection while the drive was powered. Reseat the module with power OFF and clear the fault."
pubDatetime: 2026-06-12T10:28:13Z
modDatetime: 2026-06-12T10:28:13Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - allen-bradley
money_part: "PowerFlex 525 control module"
most_likely_cause: "control module removed or reseated while drive was powered"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power down the drive completely and verify the control module is fully seated in its connector with no visible damage or contamination."
  - "Clear the fault after reseating the module and observe whether F105 returns on the next power cycle."
---

## Allen-Bradley PowerFlex 525 F105 — What It Means

F105 on the PowerFlex 525 displays as 'C Connect Err' and tells you the drive detected that the control module was disconnected or lost connection while the unit was energized. This is not a motor overload or line-voltage problem. The fault triggers when the module is removed, reseated, or experiences a connection interruption under power.

Rockwell Automation documentation makes clear that you should never remove or install the control module while the drive has power applied. Once the fault is logged, you must clear it and verify all parameter settings before returning the drive to service.

## Before You Replace Anything

Some technicians replace the entire drive assembly before confirming the control module is properly seated. Always power down, firmly reseat the module, clear the fault, and check for a return before ordering a new drive.

[Jump to Fix](#fix)

## Common Causes

- **Control module disconnected under power (~70%)** The module was removed, reseated, or lost contact while the drive was energized, which Rockwell explicitly identifies as the cause of F105.
- **Loose or improperly seated module (~20%)** The control module was not fully inserted after previous service, or vibration and handling gradually unseated the connector.
- **Damaged module connector or backplane (~8%)** Pins in the module connector or the drive backplane are bent, corroded, or contaminated, preventing a reliable connection.
- **Faulty control module (~2%)** The module itself has failed internally and cannot maintain a stable connection even when properly installed.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Did someone work on the drive or reseat the control module recently?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault likely happened when the module was handled under power. Power down, reseat firmly, clear the fault, and test.<br><strong>No:</strong> Vibration or a loose fit may have unseated the module over time. Power down, inspect the connector, reseat, and clear the fault.</div>
</details>

<details class="dtree"><summary>Does the fault clear and stay gone after a proper reseat and power cycle?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem was a seating issue. Verify all parameter settings and return the drive to service.<br><strong>No:</strong> The module or drive backplane may be damaged. Replace the control module and test again before replacing the entire drive.</div>
</details>

<details class="dtree"><summary>Do you see bent pins, corrosion, or contamination in the module connector or drive socket?</summary>
<div class="dtree-body"><strong>Yes:</strong> Clean the contacts carefully or replace the damaged component. If the backplane is damaged, you may need a new drive assembly.<br><strong>No:</strong> The module is probably faulty. Replace the control module and verify the fault does not return.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off all power** to the drive at the main disconnect and verify it is completely de-energized before touching the control module.
2. **Remove the control module** carefully and inspect both the module connector pins and the drive backplane socket for bent contacts, corrosion, dirt, or physical damage.
3. **Clean any contamination** with contact cleaner and a lint-free cloth, and straighten any bent pins if possible or replace the damaged component.
4. **Reinstall the control module** firmly into the drive socket, making sure it clicks or seats completely with no gaps.
5. **Restore power** and clear the F105 fault using the drive keypad or software interface.
6. **Verify all parameter settings** against your commissioning record or backup, because Rockwell requires this step after clearing F105.
7. **Monitor the drive** through several start-stop cycles to confirm the fault does not return; if F105 reappears, replace the control module or consult the drive assembly for backplane damage.

## Parts Often Needed

| Part | Notes |
|------|-------|
| PowerFlex 525 control module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f105-fault-code&k=PowerFlex+525+control+module&tag=errorcodefixes-20) \| The primary replaceable component for persistent F105 faults after correct reseating and power-down procedures. |
| PowerFlex 525 drive assembly (complete unit) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f105-fault-code&k=PowerFlex+525+drive+assembly+%28complete+unit%29&tag=errorcodefixes-20) \| Required if the control module replacement does not resolve the fault or if the backplane connector is damaged beyond repair. |

## When to Call a Pro

Call a qualified electrician or industrial controls technician if you are not trained to work on variable-frequency drives or if your facility safety rules require a licensed professional for high-voltage equipment. A technician will safely de-energize the drive, verify the control module connection, clear the fault, and replace the module or drive assembly if needed. Professional service also includes verifying all drive parameters and confirming the system returns to normal operation without repeat faults.

**Rough cost:** A pro service call runs about $150-400 depending on module replacement or field service call.
