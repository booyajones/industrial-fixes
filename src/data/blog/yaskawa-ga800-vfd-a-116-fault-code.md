---
title: "Yaskawa GA800 A.116 Fault - Causes & Fix"
description: "A.116 means multi-function input open alarm on GA800 VFDs. Most often an open interlock, E-stop, or loose wiring. Check control circuit."
pubDatetime: 2026-06-08T11:10:30Z
modDatetime: 2026-06-08T11:10:30Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
most_likely_cause: "Open or disconnected interlock or safety device in the external control circuit"
likelihood: "the most common real-world cause"
diy_or_pro: "pro"
money_part: "Field control wire"
---

## Yaskawa GA800 A.116 Fault — What It Means

A.116 on a Yaskawa GA800 is a warning alarm, not a major trip fault. It indicates a multi-function input open condition, meaning one of the drive's programmed digital inputs is reading as open when the drive expects it to be closed. This alarm is almost always tied to external control wiring rather than an internal drive failure. The drive is monitoring a permissive chain or interlock circuit and reporting that the circuit is not in the expected state.

The alarm is commonly triggered by safety-chain devices such as E-stop loops, door switches, proving contacts, pressure switches, or other external permissive contacts that feed the monitored input. The drive itself is functioning correctly but is simply reporting that the external control circuit feeding the input is open. Always check your GA800 manual and wiring diagram to confirm which specific multi-function input is assigned to this alarm on your installation.

## Before You Replace Anything

Technicians sometimes replace the drive control board or option card when the real issue is a failed relay contact, loose terminal screw, or broken wire in the external control circuit. Always trace the actual input circuit on the elementary diagram and meter the contact state at the drive terminals before replacing any drive components.

[Jump to Fix](#fix)

## Common Causes

- **Open interlock or safety device (~45%)** An E-stop loop, door switch, pressure switch, or other external permissive contact feeding the monitored input is open or has failed.
- **Loose or broken field wiring (~30%)** A loose terminal screw, broken conductor, or poor connection in the control circuit feeding the multi-function input.
- **Failed auxiliary relay or PLC output contact (~15%)** A control relay, safety relay, or PLC output contact in the permissive chain has failed open and is not closing when commanded.
- **Incorrect input programming (~8%)** The drive parameter assignment or contact logic does not match the actual field wiring, making a healthy circuit appear open to the drive.
- **Option card or connector issue (~2%)** If the monitored input is on an option board, a loose or unseated card or connector can cause the drive to see an open circuit.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is there an E-stop button, door switch, or safety interlock device in your system that is currently open or tripped?</summary>
<div class="dtree-body"><strong>Yes:</strong> Reset or close the safety device and verify the alarm clears. If it does, the device or its contacts may be faulty or sticking open.<br><strong>No:</strong> Proceed to check the wiring and terminal connections at the drive for the monitored input circuit.</div>
</details>

<details class="dtree"><summary>Do you have an elementary diagram or wiring schematic showing which multi-function input is assigned to A.116?</summary>
<div class="dtree-body"><strong>Yes:</strong> Use the diagram to trace the circuit from the field device to the drive terminals and meter for continuity at each point.<br><strong>No:</strong> Check the drive's parameter settings to identify which input is programmed for the alarm, then trace that input's wiring.</div>
</details>

<details class="dtree"><summary>When you meter the circuit at the drive terminals, do you see continuity or the expected contact state?</summary>
<div class="dtree-body"><strong>Yes:</strong> The wiring is intact but the drive may be programmed incorrectly, or the input logic setting does not match the field wiring type.<br><strong>No:</strong> The circuit is open upstream. Trace back through the wiring, devices, and relay contacts to find the break or failed component.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Confirm the alarm code and identify the input.** Read the alarm on the drive keypad and note which multi-function input is assigned to A.116 in your drive parameters or elementary diagram.
2. **Locate the elementary diagram or control wiring schematic.** Find the drawing that shows the permissive chain, interlock devices, and field wiring connected to the monitored input.
3. **Inspect the external control circuit.** Check all terminal screws, wire connections, and inline devices (E-stops, switches, relays, PLC outputs) in the circuit for loose connections, broken wires, or open contacts.
4. **Meter the circuit for continuity.** Use a multimeter to verify continuity from the field device through the wiring to the drive terminals. Test at the drive terminals first, then work back to the field device to isolate where the circuit opens.
5. **Check the state of all safety and interlock devices.** Verify that E-stop buttons are reset, door switches are closed, pressure switches are satisfied, and any relay or PLC output contacts in the chain are closing when commanded.
6. **Verify drive input programming.** If the wiring tests good, review the drive parameters to confirm the input type, logic (normally open vs. normally closed), and assignment match the actual field wiring.
7. **Repair or replace the faulty component.** Tighten loose terminals, replace damaged wire, repair or replace a failed switch or relay, or correct the PLC output that is not closing. Clear the alarm and retest the system to confirm the input reads closed and the alarm does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Field control wire | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-116-fault-code&k=Field+control+wire&tag=errorcodefixes-20) \| Stranded copper, sized per the drive manual for control circuits, to replace damaged conductors in the permissive chain. |
| Interlock relay or auxiliary contact | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-116-fault-code&k=Interlock+relay+or+auxiliary+contact&tag=errorcodefixes-20) \| Replacement relay or contact block for the external safety or permissive device feeding the monitored input. |
| Terminal block or connector | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-116-fault-code&k=Terminal+block+or+connector&tag=errorcodefixes-20) \| If the drive's input terminal block is damaged or loose, a replacement may be needed; verify the part number from Yaskawa for your GA800 model. |

## When to Call a Pro

Call a qualified electrician or industrial controls technician if you are not trained to work with VFD control circuits, if the elementary diagram is unavailable, or if you cannot safely identify and trace the monitored input circuit. A technician will use the drive parameters, wiring diagram, and a meter to systematically isolate whether the issue is in the field wiring, an external device, or the drive itself. Also call a pro if the alarm involves a safety-rated interlock or E-stop circuit that must meet code requirements, or if the repair requires reprogramming the drive or replacing an option card.

**Rough cost:** A pro service call runs about $150-400 depending on whether the fix is a tightened terminal or a replacement relay/switch.
