---
title: "Yaskawa GA800 E56 Fault - Causes & Fix"
description: "E56 on a Yaskawa GA800 means the Safe Torque Off (STO) safety circuit is open. Most common fix: check for a missing jumper or open safety relay."
pubDatetime: 2026-06-06T11:42:30Z
modDatetime: 2026-06-06T11:42:30Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
most_likely_cause: "Missing jumper on STO terminals or open safety relay contact"
likelihood: "the most common causes"
diy_or_pro: "pro"
money_part: "STO jumper or terminal link for GA800"
---

## Yaskawa GA800 E56 Fault — What It Means

The E56 fault code on the Yaskawa GA800 VFD indicates a safety-related input problem tied to the drive's Safe Torque Off (STO) function. The STO feature is a built-in safety mechanism that prevents the drive from producing motor torque when the safety circuit is not satisfied. When you see E56, the drive has detected that the STO input terminals are in an open or not-permissive state.

This is not a motor overload or overcurrent trip. It is a safety circuit problem. The drive will not run until the STO circuit is restored to the correct state. Treat E56 as a wiring, safety device, or configuration issue rather than a motor or load fault.

## Before You Replace Anything

Technicians sometimes replace the drive control board when E56 is actually caused by a missing jumper, loose terminal wire, or external safety device (E-stop or gate switch) that is still open. Always verify the STO wiring and external safety chain continuity with a meter before ordering drive parts.

[Jump to Fix](#fix)

## Common Causes

- **Missing or unseated STO jumper** When the drive is configured to use STO but the required jumper link between STO terminals is missing or loose, the drive sees an open circuit and trips E56.
- **Safety relay not energized or failed contacts** An upstream safety relay that feeds the STO input may not be energized, may have failed contacts, or may not be resetting after an E-stop event.
- **Open external safety device** An E-stop button, door interlock, gate switch, light curtain, or safety PLC output in the machine's safety chain is intentionally holding the STO circuit open.
- **Loose or incorrect STO terminal wiring** Field wiring to the GA800 STO input terminals may be loose, damaged, or miswired according to the machine schematic.
- **Terminal or connector damage** Physical damage to the STO input terminal block or connector can create intermittent or permanent open conditions that trigger E56.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is there an E-stop button or safety gate switch in the machine, and is it currently pressed or open?</summary>
<div class="dtree-body"><strong>Yes:</strong> The external safety device is holding the STO circuit open by design. Reset the E-stop or close the gate, then press RESET on the keypad to clear E56.<br><strong>No:</strong> The fault is either a missing jumper, failed safety relay, or wiring problem at the drive. Proceed to inspect the STO terminals and upstream safety chain.</div>
</details>

<details class="dtree"><summary>Does the GA800 have a jumper or wire link installed between the STO input terminals as shown in the machine's wiring diagram?</summary>
<div class="dtree-body"><strong>Yes:</strong> The jumper is present, so check for loose connections, verify the safety relay is energized, and measure continuity through the entire STO circuit to find the open point.<br><strong>No:</strong> Install the correct jumper or wire link as specified in the drive configuration. This is the most common oversight when commissioning a GA800 that does not use external STO devices.</div>
</details>

<details class="dtree"><summary>With power locked out, does a continuity test across the STO input terminals show a closed circuit when all safety devices are in the run state?</summary>
<div class="dtree-body"><strong>Yes:</strong> The external wiring is good. The fault may be inside the drive's safety input interface. Restore power, attempt a reset, and if E56 persists contact Yaskawa technical support.<br><strong>No:</strong> Trace the open point in the external wiring or safety relay chain. Repair the open connection, replace the failed relay or device, then test again.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Lock out and tag out** all power to the drive and machine, and verify the equipment is in a safe state before working on the STO safety circuit.
2. **Read the fault history** on the GA800 keypad to confirm the active code is E56 and note the conditions when it occurred.
3. **Inspect the STO terminal wiring** at the drive. Compare the actual wiring to the machine's safety schematic and verify that any required jumper or link is present and firmly seated.
4. **Check the upstream safety chain** by tracing from the STO terminals back through any E-stop buttons, door switches, safety relays, safety PLC outputs, or enabling contacts that feed the STO circuit.
5. **Measure continuity** through the STO circuit with a multimeter when all safety devices are in the run position. Restore each device one at a time to isolate the open point.
6. **Repair or replace** the missing jumper, loose terminal wire, failed safety relay, or open safety device. make sure all connections are tight and correctly terminated.
7. **Restore power** and verify the STO inputs are in the permissive state. Press the RESET button on the keypad to clear the E56 fault and confirm the drive is ready to run.
8. **Test the machine** through a normal start cycle to verify the fault does not return. If E56 persists with proven-good wiring, escalate to Yaskawa technical support for drive inspection.

## Parts Often Needed

| Part | Notes |
|------|-------|
| STO jumper or terminal link for GA800 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e56-fault-code&k=STO+jumper+or+terminal+link+for+GA800&tag=errorcodefixes-20) \| Required when the drive is not using external STO devices. Check the drive model and configuration before ordering. |
| Safety relay or contactor feeding STO | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e56-fault-code&k=Safety+relay+or+contactor+feeding+STO&tag=errorcodefixes-20) \| Replace if the relay coil or contacts are failed. Match the voltage and contact rating to the machine design. |
| Field wiring to STO terminals | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e56-fault-code&k=Field+wiring+to+STO+terminals&tag=errorcodefixes-20) \| Repair or replace damaged wire, crimp terminals, or connectors. Use wire gauge and type specified in the machine schematic. |

## When to Call a Pro

Call a qualified industrial electrician or controls technician if you are not trained to work on VFD safety circuits or if you cannot locate the open point in the STO wiring after following the steps above. Safety circuits like STO are designed to prevent injury, and improper jumper installation or bypassing safety devices can create serious hazards. Also call a professional if the fault persists with all wiring verified correct, as the issue may be in the drive's internal safety input interface and require factory support or board-level repair.

**Rough cost:** A pro service call runs about $150-400.
