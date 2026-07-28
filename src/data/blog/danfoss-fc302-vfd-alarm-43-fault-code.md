---
title: "Danfoss FC302 Alarm 43 - Causes & Fix"
description: "Alarm 43 means an external fault or interlock signal is active. Check E-stop, safety contacts, and control wiring first."
pubDatetime: 2026-06-03T10:50:19Z
modDatetime: 2026-06-03T10:50:19Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "External interlock contact or safety relay"
most_likely_cause: "Open safety or interlock contact"
---

## What this code means
Alarm 43 on the Danfoss FC302 VFD indicates an external fault or external interlock signal is active. This is not an internal drive failure. The drive is reporting that something outside the VFD is opening the run-enable or interlock chain, such as a safety contact, E-stop, or field device contact. The drive stops and displays the alarm because it is being told to trip by an external signal.

In practical terms, the FC302 is responding to a deliberate external shutdown command or an unintended open circuit in your safety or permissive wiring. The fault does not point to a problem inside the drive itself but rather to the control wiring, field devices, or safety chain that feeds the drive's external fault input.

## Common Causes

- **Open safety or interlock contact** An E-stop button, safety relay, or interlock contact in the external fault chain is open or not in the correct state.
- **Loose or broken control wiring** Field wiring to the digital input terminal for external fault is loose, broken, corroded, or miswired.
- **HOA, bypass, or permissive panel not enabled** A hand-off-auto switch, bypass panel, or permissive circuit is not closed, preventing the drive from running.
- **External device contact failure** A field device such as a pressure switch, flow switch, overload relay, firestat, or proof switch has opened the interlock chain.
- **Incorrect drive parameterization** The drive input terminal or function is incorrectly configured so the wrong signal is interpreted as an external fault or interlock.
- **Control card input misreading** With the external circuit verified closed, the drive's control card may be misreading the input due to a card fault or damaged I/O channel.

## Step-by-Step Fix {#fix}

1. **Identify the external fault circuit** on your machine schematic and determine which contact, relay, or terminal is assigned to the interlock or alarm chain for the FC302.
2. **Check the external fault input status** at the drive control terminals and verify whether the interlock signal is open or closed using a multimeter or the drive's digital input status display.
3. **Inspect all field wiring** in the interlock chain for loose terminal screws, broken conductors, corrosion at connections, or mislanded wires at the drive control terminals.
4. **Verify the safety circuit and permissives** by checking that E-stops are reset, HOA switches are in the correct position, and all bypass or run-enable contacts are closed.
5. **Isolate the field circuit section by section** to find which device is opening the chain by temporarily bypassing one contact or switch at a time until the open device is identified.
6. **Reset the alarm** only after the external circuit is restored and all interlock contacts are confirmed closed and functioning.
7. **If the alarm persists with the external circuit proven closed**, check the drive's control input wiring and control card I/O condition, and consider that the control card itself may have a fault if the input circuit is verified correct.

## Parts Often Needed

| Part | Notes |
|------|-------|
| External interlock contact or safety relay | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-43-fault-code&k=External+interlock+contact+or+safety+relay&tag=errorcodefixes-20) \| Replace if the field circuit device (E-stop, pressure switch, flow switch, or safety relay) is found to be defective or stuck open. |
| Field wiring terminal blocks and connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-43-fault-code&k=Field+wiring+terminal+blocks+and+connectors&tag=errorcodefixes-20) \| Replace any damaged terminal blocks, corroded connectors, or broken wire sections in the interlock chain. |
| Danfoss FC302 control card / control PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-43-fault-code&k=Danfoss+FC302+control+card+%2F+control+PCB&tag=errorcodefixes-20) \| Replace only if the external circuit is verified closed and the drive still misreads the input condition, indicating a control card fault. |

## When to Call a Pro

Call a qualified electrician or automation technician if you cannot locate the open contact in the interlock chain, if the machine schematic is unavailable or unclear, or if the alarm persists after verifying all external wiring and contacts are correct. A technician with a schematic and multimeter can systematically trace the interlock circuit and identify which field device or wiring segment is opening the chain. Also call a professional if you suspect a control card fault, as drive control board diagnosis and replacement require familiarity with VFD parameter backup, proper handling of static-sensitive components, and verification of correct I/O configuration after card replacement.
