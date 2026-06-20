---
title: "Allen-Bradley PowerFlex 525 F122 - Causes & Fix"
description: "F122 means I/O board failure inside the drive control section. Power-cycle once; if it returns, replace the control module or drive."
pubDatetime: 2026-06-12T10:34:33Z
modDatetime: 2026-06-12T10:34:33Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - allen-bradley
money_part: "PowerFlex 525 control module or complete drive"
most_likely_cause: "Internal control or I/O board hardware failure"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Record the fault history from the drive's fault queue (usually in parameter P073 or similar) to confirm F122 is the active fault."
  - "Power-cycle the drive completely (disconnect input power, wait 30 seconds, reconnect) and check if F122 clears on restart."
---

## Allen-Bradley PowerFlex 525 F122 — What It Means

F122 is an I/O Board Fail code on the PowerFlex 525 drive. A failure has been detected in the drive control and I/O section, which is the internal hardware that manages inputs, outputs, and control signals. This is not a motor overload or line-voltage issue. It points to a hardware problem inside the drive itself.

Rockwell's prescribed remedy is to cycle power and check if the fault clears. If F122 returns after restart, the manufacturer directs you to replace the drive or control module. The fault does not indicate a specific sensor or wiring problem outside the drive cabinet.

## Before You Replace Anything

Technicians sometimes replace external wiring or parameter settings first, but F122 is a hardware fault inside the drive. Record the fault history and power-cycle before ordering parts.

[Jump to Fix](#fix)

## Common Causes

- **Internal control or I/O board failure (~70%)** The drive's control and I/O section has failed and cannot manage inputs, outputs, or control signals.
- **Control module hardware defect (~20%)** A component on the control module has degraded or failed and does not clear after a power cycle.
- **Transient fault from power disturbance (~5%)** A brief line surge or brownout corrupted the control logic, but the fault may clear with a full power cycle.
- **Poor connection on control module connector (~5%)** The control module plug or I/O terminal connector has oxidation or a loose pin interrupting communication.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does F122 clear after a full power cycle and stay clear when you restart the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was transient. Monitor the drive and check for line-voltage disturbances or loose wiring that might have caused a brief control upset.<br><strong>No:</strong> The control or I/O board has a persistent hardware failure. Proceed to inspect the control module connector and prepare to replace the control module or drive.</div>
</details>

<details class="dtree"><summary>Is the control module a separate plug-in assembly on your frame size?</summary>
<div class="dtree-body"><strong>Yes:</strong> Order the replacement control module for your drive catalog number and swap it. Many frame sizes use a removable control board.<br><strong>No:</strong> The control board is integrated into the drive housing. You will need to replace the entire drive unit.</div>
</details>

<details class="dtree"><summary>Did you recently update parameters, install an add-on I/O card, or change control wiring?</summary>
<div class="dtree-body"><strong>Yes:</strong> Reseat the control module connector and any option-card connections. Power-cycle again. If F122 returns, the module itself has failed.<br><strong>No:</strong> The fault is most likely a spontaneous hardware failure. Follow the power-cycle and replacement steps below.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Record the fault queue.** Navigate to parameter P073 (or consult your manual for the fault-log parameter) and note the last fault code and any associated fault data before clearing the fault.
2. **Disconnect input power** to the drive and wait at least 30 seconds for the DC bus capacitors to discharge fully.
3. **Reconnect power and attempt a restart.** If F122 does not reappear and the drive runs normally, the fault was transient. Monitor the drive and check for line disturbances or loose control wiring.
4. **If F122 returns immediately,** open the drive enclosure (with power off and locked out) and inspect the control module connector and any I/O terminal blocks for corrosion, loose pins, or bent contacts.
5. **Reseat the control module** (if it is a plug-in assembly) or reseat any option-card connectors. Power-cycle again. If the fault persists, the control or I/O board hardware has failed.
6. **Replace the control module** if your frame size uses a separate field-replaceable module. Consult your drive's catalog number and frame size to order the correct Rockwell control-board assembly.
7. **Replace the entire drive** if the control board is integrated into the housing or if a control-module swap does not clear F122. Rockwell's service guidance directs replacement of the drive when the I/O board cannot be serviced separately.

## Parts Often Needed

| Part | Notes |
|------|-------|
| PowerFlex 525 control module or complete drive | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f122-fault-code&k=PowerFlex+525+control+module+or+complete+drive&tag=errorcodefixes-20) \| Catalog number depends on frame size and voltage class; check the drive nameplate and consult Rockwell for the correct replacement part number. |

## When to Call a Pro

Call a qualified electrician or drives technician if you are not familiar with VFD wiring, if the drive is part of a larger automation system where parameter backups and network configuration matter, or if you need to verify that line-voltage disturbances are not causing repeated control faults. A technician will record the fault history, safely power-cycle the drive under lockout procedures, and determine whether your specific frame and catalog number use a replaceable control module or require a full drive swap. High-voltage work and parameter restoration should be handled by someone trained on Allen-Bradley drives.

**Rough cost:** A pro service call runs about $400-1200 depending on frame size and whether you swap the control module or replace the entire drive.

## See Also

- [Allen-Bradley PowerFlex 525 F100 - Causes & Fix](/posts/allen-bradley-powerflex-525-vfd-f100-fault-code/)
- [Allen-Bradley PowerFlex 525 F125 - Causes & Fix](/posts/allen-bradley-powerflex-525-vfd-f125-fault-code/)
- [Allen-Bradley PowerFlex 525 F073 - Causes & Fix](/posts/allen-bradley-powerflex-525-vfd-f073-fault-code/)
- [Allen-Bradley PowerFlex F122 Fault — I/O Board Failure Fix](/posts/allen-bradley-powerflex-f122-fault/)
