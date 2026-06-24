---
title: "Danfoss FC302 AL-68 Fault - Causes & Fix"
description: "AL-68 means Safe Stop Activated because the drive lost the 24V safety signal at Terminal 37. Check wiring and reset the drive."
pubDatetime: 2026-06-22T10:21:21Z
modDatetime: 2026-06-22T10:21:21Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "High Pressure Control (HPC) switch"
most_likely_cause: "Missing 24V DC at Terminal 37"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Measure DC voltage between Terminal 37 and Terminal 0V to confirm 24V is present"
  - "Inspect all wiring connections to Terminal 37 for loose or corroded contacts"
  - "Check that any relay controlling Terminal 37 is energized and safety switches are closed"
no_buy_pct: "80%"
---

## Danfoss FC302 AL-68 Fault — What It Means

The AL-68 (or A68) fault on a Danfoss FC302 VFD does not indicate a component failure. It means Safe Stop Activated because the drive's Safe Torque Off (STO) circuit has been triggered. The drive intentionally disabled output power to the motor to enforce a safe stop condition. This happens when the drive does not detect the required 24V DC signal at Terminal 37, which is the Safe Stop input. When this signal is missing, the output transistors (IGBTs) turn off and the motor stops immediately.

In most installations, especially HVAC systems like Danfoss TR200 chillers, the 24V safety signal at Terminal 37 is routed through a safety circuit. This circuit often includes a High Pressure Control (HPC) switch or a relay (such as 1K14). If the high pressure exceeds the set limit, the relay de-energizes, or the circuit opens during a power loss, the 24V signal is removed and the drive logs AL-68. The drive can stay powered for about 40 seconds on its internal DC capacitors after losing mains power, so if the 24V signal disappears during that window, the fault will appear.

## Before You Replace Anything

Technicians sometimes replace the VFD control board thinking it has failed, when the actual problem is a faulty relay or safety switch in the 24V loop. Always measure voltage at Terminal 37 with a DC voltmeter before ordering parts.

[Jump to Fix](#fix)

## Common Causes

- **Missing 24V DC at Terminal 37 (~50%)** The drive does not detect the required 24V safety signal at Terminal 37, which is the most common cause and is often due to an open safety circuit or de-energized relay.
- **Safety circuit interruption (HPC switch or relay) (~25%)** In HVAC systems, the 24V signal is routed through a High Pressure Control switch or relay (e.g. 1K14), and when the switch opens due to high pressure or the relay de-energizes, the signal is removed.
- **Power loss scenario (~10%)** If the drive loses mains power, the relay controlling Terminal 37 may open, and the drive logs AL-68 while it stays powered on internal capacitance for up to 40 seconds.
- **Loose wiring or corroded connector (~10%)** A broken wire, corroded terminal, or poor connection in the path between the 24V source (Terminal 12 or 13) and Terminal 37 will interrupt the safety signal.
- **Open safety contact in loop (~5%)** A Normally Closed safety contact (emergency stop, door interlock, or other safety device) is open and preventing 24V from reaching Terminal 37.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Do you measure 24V DC between Terminal 37 and Terminal 0V?</summary>
<div class="dtree-body"><strong>Yes:</strong> The safety circuit is intact. Press the Reset button on the keypad or send a reset command via bus to clear the fault and restore operation.<br><strong>No:</strong> The safety circuit is open. Trace the wiring from the 24V supply (Terminal 12 or 13) to Terminal 37 and check every switch, relay, and connection in that path.</div>
</details>

<details class="dtree"><summary>Does the fault clear after you jumper Terminal 12 directly to Terminal 37 for testing?</summary>
<div class="dtree-body"><strong>Yes:</strong> A switch or relay in the safety loop is faulty or open. Identify and replace the failed component. Do not leave the jumper in place during normal operation.<br><strong>No:</strong> Check for a wiring fault, a blown fuse in the 24V supply circuit, or a problem with the VFD internal safety circuit. Consult a qualified technician.</div>
</details>

<details class="dtree"><summary>Is there a High Pressure Control (HPC) switch in the safety loop?</summary>
<div class="dtree-body"><strong>Yes:</strong> Verify the HPC switch is closed and the system pressure is within normal range. Reset the HPC if it has tripped and address the underlying pressure issue.<br><strong>No:</strong> Look for other safety devices in the loop, such as emergency stops, door interlocks, or control relays that may have opened.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power** to the drive at the main disconnect and verify lockout/tagout procedures are followed.
2. **Restore power** and use a DC voltmeter to measure between Terminal 37 and Terminal 0V. You should read 24V DC if the safety circuit is intact.
3. **Trace the wiring** from the 24V source (typically Terminal 12 or Terminal 13) to Terminal 37. Identify every switch, relay, and contact in this path.
4. **Inspect each safety device** in the loop, such as the High Pressure Control switch, control relays (e.g. 1K14), emergency stops, and door interlocks. Verify all Normally Closed contacts are closed and all relays are energized.
5. **Check all connections** at Terminal 37 and the 24V supply terminals for loose wires, corrosion, or damage. Tighten or clean any suspect connections.
6. **Test with a temporary jumper** (for diagnosis only) by connecting Terminal 12 to Terminal 37 with a short jumper wire. If the fault clears, the problem is in the safety loop. Do not operate the machine with the jumper in place permanently.
7. **Reset the drive** once 24V DC is confirmed at Terminal 37. Press the Reset button on the LCP keypad, send a reset command via the bus, or use a digital input configured for reset. The drive should clear the AL-68 fault and allow normal operation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| High Pressure Control (HPC) switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-68-fault-code&k=High+Pressure+Control+%28HPC%29+switch&tag=errorcodefixes-20) \| If the HPC switch is faulty or stuck open, replace with the correct pressure-rated switch for your system. |
| Control relay (e.g. 1K14) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-68-fault-code&k=Control+relay+%28e.g.+1K14%29&tag=errorcodefixes-20) \| If the relay controlling Terminal 37 has failed, replace with a 24V DC coil relay rated for the control circuit. |

## When to Call a Pro

Call a qualified VFD or HVAC technician if you are not comfortable working with control wiring, 24V DC circuits, or variable frequency drives. This fault involves the drive's safety system, which is designed to prevent injury and equipment damage. A technician should diagnose the issue if you cannot locate the open circuit, if the drive does not clear after verifying 24V at Terminal 37, or if you suspect a fault in the drive's internal Safe Torque Off circuit. Do not permanently bypass the safety loop by leaving a jumper installed, as this defeats critical safety protections.

**Rough cost:** A pro service call runs about $150-400.
