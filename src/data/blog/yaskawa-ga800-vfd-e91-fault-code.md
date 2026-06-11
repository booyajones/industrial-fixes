---
title: "Yaskawa GA800 E91 Fault - Causes & Fix"
description: "E91 means Safe Torque Off circuit open. Most often a missing STO jumper or disconnected safety relay. Check terminals first."
pubDatetime: 2026-06-07T10:27:07Z
modDatetime: 2026-06-07T10:27:07Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
most_likely_cause: "Missing or loose STO jumper at the drive terminals"
likelihood: "the most common cause"
diy_or_pro: "pro"
money_part: "Yaskawa GA800 STO jumper kit"
---

## Yaskawa GA800 E91 Fault — What It Means

E91 on the Yaskawa GA800 indicates a Safe Torque Off (STO) fault. The drive has detected that its STO safety inputs are not in the enabled state, so it refuses to produce torque. STO is a hardware safety function that cuts output when external safety devices (emergency stops, guards, or safety relays) demand it or when required jumpers are missing.

The drive will not run until the STO circuit is satisfied. This is not a motor or output-stage problem. It is a safety-chain issue at the STO input terminals. The fault appears immediately on power-up or when a safety device upstream opens the STO loop.

## Before You Replace Anything

Technicians sometimes replace the control board or output transistors when E91 appears, assuming an internal drive fault. Always verify STO terminal wiring and jumper presence first, a zero-cost visual check that solves most E91 faults.

[Jump to Fix](#fix)

## Common Causes

- **Missing STO jumper** If the drive is configured for local STO operation and the jumper between STO terminals is removed or never installed, the drive immediately faults E91.
- **Safety relay not reset** An external safety relay driving the STO inputs may be latched off or faulted, preventing the dual-channel enable signal the drive expects.
- **Broken or loose STO wiring** Corroded, loose, or broken wires at the STO terminal block create an open circuit that the drive interprets as a safety demand.
- **External safety device active** An upstream emergency stop, guard interlock, or light curtain holds the STO circuit open, and the drive correctly refuses to run.
- **Incorrect terminal assignment parameters** If the drive was reprogrammed and STO-related terminal functions were changed without matching the physical wiring, the drive sees a mismatch and faults.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does your GA800 use a local STO jumper (a small wire link across two STO terminals) instead of a safety relay?</summary>
<div class="dtree-body"><strong>Yes:</strong> Inspect the jumper. If it is missing or loose, reseat or install the jumper per the GA800 manual and reset the fault.<br><strong>No:</strong> Your machine uses an external safety relay or safety controller. Check that all emergency stops and guards are reset and that the safety relay outputs are wired to the correct STO input terminals.</div>
</details>

<details class="dtree"><summary>After resetting all E-stops and guards, does the E91 fault clear?</summary>
<div class="dtree-body"><strong>Yes:</strong> The safety chain is working. One of the upstream devices was open. No further repair needed.<br><strong>No:</strong> The STO circuit itself has a wiring fault, terminal damage, or the safety relay is not providing the correct output. Trace STO wiring and measure continuity at the drive terminals.</div>
</details>

<details class="dtree"><summary>With power locked out, do you measure continuity across the STO input terminals when the safety relay is commanded to enable?</summary>
<div class="dtree-body"><strong>Yes:</strong> The wiring is intact. The drive may have a terminal-block or control-board fault. Escalate to Yaskawa support with the unit serial number and fault log.<br><strong>No:</strong> Open circuit in the safety wiring or relay outputs. Repair the broken wire or replace the faulty safety relay.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Lock out and tag out** all power to the drive and verify zero voltage at the input and control terminals before touching any wiring.
2. **Record the fault code** and drive status LEDs. Confirm the display shows E91 and not a different fault that might also inhibit operation.
3. **Identify your STO configuration.** Check the GA800 wiring diagram on the drive cover or in your documentation. Determine whether the drive uses a local STO jumper or an external safety relay.
4. **Inspect the STO terminals.** If a jumper is required, verify it is present, correctly seated, and not corroded. If a safety relay is used, confirm both relay output wires land on the correct STO input terminals and that terminal screws are tight.
5. **Verify all upstream safety devices.** Walk the machine and confirm every emergency stop button is pulled out (reset), every guard door is closed, and every safety relay reset button (if present) is pressed. Many machines require a deliberate reset after an E-stop.
6. **Measure continuity** in the STO circuit with a multimeter (power locked out). If using a safety relay, jumper the relay inputs to simulate a safe condition and check for continuity at the drive STO terminals. No continuity means broken wiring or a failed relay.
7. **Restore power and reset the drive.** If the STO circuit is now valid, the E91 fault should clear immediately. If it persists, check terminal function parameters in the drive menu to make sure STO assignments match your physical wiring, or contact Yaskawa technical support with the drive serial number and fault history.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 STO jumper kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e91-fault-code&k=Yaskawa+GA800+STO+jumper+kit&tag=errorcodefixes-20) \| Factory or field-supplied jumper wire for local STO bridging when no external safety relay is used. Consult your drive manual for the correct part number for your frame size. |
| Safety relay (dual-channel) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e91-fault-code&k=Safety+relay+%28dual-channel%29&tag=errorcodefixes-20) \| If your machine uses an external safety relay and the relay coil or output contacts are damaged, replace with a relay that matches the original model and meets the required safety category. |
| Terminal block wire and ferrules | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e91-fault-code&k=Terminal+block+wire+and+ferrules&tag=errorcodefixes-20) \| For repairing broken or corroded STO input wiring. Use wire gauge and ferrule size specified in the GA800 installation manual for control terminals. |

## When to Call a Pro

Call a qualified industrial electrician or controls technician if you are not trained in lockout/tagout procedures, if you are unfamiliar with safety relay circuits, or if the STO wiring and jumper check good but the fault remains. STO circuits are safety-critical and must comply with machinery safety standards. Incorrect wiring or bypassing the STO function can create serious hazards. If the fault persists after verifying all external wiring and the drive documentation does not resolve the issue, escalate to Yaskawa technical support with your drive serial number and a description of the tests you performed.

**Rough cost:** A pro service call runs about $150–400 depending on whether the fix is a simple jumper replacement or rewiring a safety relay circuit.
