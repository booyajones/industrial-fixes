---
title: "Yaskawa GA800 E84 Fault - Causes & Fix"
description: "E84 means the Safe Torque Off (STO) circuit is open or not satisfied. Most often a missing jumper or open safety relay contact."
pubDatetime: 2026-06-07T10:22:00Z
modDatetime: 2026-06-07T10:22:00Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
most_likely_cause: "Missing or removed factory jumper on STO terminals when no external safety relay is used"
likelihood: "the most common cause"
diy_or_pro: "pro"
money_part: "Factory STO jumper wire or plug"
---

## What this code means
The E84 fault on a Yaskawa GA800 variable frequency drive indicates that the Safe Torque Off (STO) safety function is preventing the drive from producing torque to the motor. The STO circuit is a safety feature that blocks the inverter output even when main input power is present. When the drive detects that the STO terminals are not in the expected state (open circuit, missing jumper, or incomplete safety relay connection), it will not run and will display E84.

This fault is strictly a safety interlock issue, not a motor or power problem. The drive requires either a factory-installed jumper on the STO terminals (if no external safety relay is used) or properly wired dual-channel safety relay outputs to close the STO loop. If the safety chain is broken anywhere (open E-stop, guard switch, relay failure, or loose wire), the drive will fault and inhibit torque production until the circuit is restored and the fault is cleared.

## Before You Replace Anything

Technicians sometimes replace the entire drive or control board when E84 appears, but the fault is nearly always in the external safety wiring, missing jumper, or safety relay. Check the STO terminal wiring and jumper presence first before ordering any drive components.

## Common Causes

- **Missing factory jumper** The STO terminals require a factory-installed jumper when no external safety relay is connected, and if it is removed or lost the drive will fault.
- **Open safety relay** An external safety relay feeding the STO inputs may not be energized, one channel may be open, or the relay itself has failed.
- **E-stop or guard switch open** Any E-stop button, guard switch, or safety contact in series with the safety relay will leave the STO loop open if activated or stuck.
- **Loose or damaged wiring** Broken conductors, loose terminal screws, or damaged connectors between the safety relay and the GA800 STO terminals will interrupt the circuit.
- **Misconfigured terminal functions** The drive's terminal function parameters may not be correctly assigned for Safe Torque Off operation, leaving the safety inputs inactive.
- **Incorrect safety relay wiring** The dual-channel outputs of the safety relay must land on the correct GA800 STO input terminals, and reversed or single-channel wiring will cause the fault.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is there an external safety relay or E-stop circuit connected to the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is likely in the safety relay chain. Check that the relay is energized, all E-stops are reset, and both safety relay output channels are wired to the STO terminals.<br><strong>No:</strong> The drive requires a factory jumper on the STO terminals. Inspect the terminal block and confirm the jumper is present and secure, then clear the fault.</div>
</details>

<details class="dtree"><summary>With power off, do you see a jumper wire or plug installed across the STO terminal pair?</summary>
<div class="dtree-body"><strong>Yes:</strong> The jumper is present but the fault persists, so check for loose terminals, damaged jumper wire, or incorrect terminal function programming in the drive parameters.<br><strong>No:</strong> Install the factory jumper exactly as shown in the GA800 manual for your model. Without it, the drive will always fault E84.</div>
</details>

<details class="dtree"><summary>Are all E-stop buttons released and all guard switches closed?</summary>
<div class="dtree-body"><strong>Yes:</strong> The mechanical safety devices are closed, so measure continuity through the safety relay outputs to the STO terminals to find the open point in the wiring.<br><strong>No:</strong> Reset all E-stops, close all guards, and cycle power to the safety relay. If the relay does not pick up, troubleshoot the relay control circuit or replace the relay.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the fault code** on the GA800 keypad and confirm the drive is displaying E84 and not running, indicating the STO circuit is open.
2. **Identify the safety architecture** by inspecting the STO terminals on the drive and determining whether an external safety relay is used or the factory jumper should be present.
3. **Check the factory jumper** if no external safety relay is connected. Power off the drive, inspect the STO terminal block, and confirm the jumper is installed and tight. If missing, install it per the manual.
4. **Inspect the safety relay and wiring** if an external safety system is present. Verify the relay is energized, both output channels are wired to the correct STO terminals, and all connections are secure.
5. **Test E-stop and guard switches** by manually operating each device and confirming the safety relay drops out and picks up as expected. Replace any stuck or failed switch.
6. **Measure continuity** from the safety relay outputs to the GA800 STO terminals with power off. Look for open circuits, broken wires, or loose terminal screws and repair as needed.
7. **Review terminal function parameters** in the drive programming to confirm the STO inputs are correctly assigned. Consult the GA800 manual for your firmware version and correct any misconfiguration.
8. **Clear the fault** from the keypad after correcting the safety circuit, then run the drive and confirm normal operation with the STO loop satisfied.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Factory STO jumper wire or plug | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e84-fault-code&k=Factory+STO+jumper+wire+or+plug&tag=errorcodefixes-20) \| Consult your GA800 model documentation for the correct jumper part number and terminal positions. |
| Dual-channel safety relay | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e84-fault-code&k=Dual-channel+safety+relay&tag=errorcodefixes-20) \| Replace if the existing relay will not energize or one output channel has failed. Must meet machine safety category requirements. |
| Field wiring and terminals | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e84-fault-code&k=Field+wiring+and+terminals&tag=errorcodefixes-20) \| Repair or replace damaged conductors, connectors, or terminal blocks between the safety relay and the drive STO inputs. |

## When to Call a Pro

Call a qualified industrial electrician or controls technician if you are not trained in machine safety systems or do not have the GA800 manual and wiring diagrams. Safe Torque Off circuits are part of the machine's safety architecture and must comply with safety standards. If you are unsure which terminals are the STO inputs, cannot locate the factory jumper, or do not understand dual-channel safety relay wiring, professional service is required. Also call a pro if the drive continues to fault E84 after verifying the STO circuit is closed, as this may indicate a drive internal fault or parameter corruption that requires factory support or drive replacement.

**Rough cost:** A pro service call runs about $150-400.
