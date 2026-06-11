---
title: "Yaskawa GA800 E59 Fault - Causes & Fix"
description: "E59 means Safe Torque Off circuit open. Most often a missing STO jumper or open safety relay. Restore jumper or check E-stop chain."
pubDatetime: 2026-06-06T11:44:55Z
modDatetime: 2026-06-06T11:44:55Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
most_likely_cause: "Missing or removed STO jumper on the safety terminals"
likelihood: "the most common cause"
diy_or_pro: "pro"
money_part: "STO terminal jumper or plug"
---

## Yaskawa GA800 E59 Fault — What It Means

E59 on a Yaskawa GA800 variable frequency drive indicates a Safe Torque Off (STO) fault. The drive sees the STO safety input chain as open or invalid, so it will not produce torque to the motor even though input power is still present. This is a safety-circuit condition, not a motor overload or process alarm.

In practice, the drive is being held out of run by the STO safety inputs or their related wiring and configuration. The GA800 will not run unless the STO terminals are correctly jumpered (for local use without an external safety system) or driven by a valid closed safety relay circuit (when integrated into a machine safety chain).

## Before You Replace Anything

Technicians sometimes replace the drive control board or suspect a motor winding fault. Check the STO terminal jumper or safety relay state with a meter first. A simple open connection in the safety chain is the usual culprit, not a failed drive.

[Jump to Fix](#fix)

## Common Causes

- **Missing STO jumper** When the GA800 is configured for local operation without an external safety system, a jumper must be installed between the STO terminals or the drive will not enable.
- **Open safety relay contacts** If the drive is integrated into a machine safety circuit, an E-stop button, guard door interlock, or safety relay may be open or latched in the tripped state.
- **Miswiring of STO inputs** Incorrect terminal connections or feedback wiring in the safety chain will prevent the drive from seeing a valid closed loop.
- **Incorrect parameter setup** After commissioning, a factory reset, or parameter changes, the terminal functions assigned to the STO circuit may not match the installed wiring scheme.
- **Loose or failed terminal connections** Corroded, loose, or broken wiring at the drive STO terminals, safety relay outputs, or interposing junction points will open the safety loop.
- **Failed safety device** An E-stop switch, guard interlock contact, or safety relay output contact that has failed open will hold the drive out of run.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is there a physical jumper wire or plug installed across the STO terminals on the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The jumper is present. Move on to check external safety devices and wiring.<br><strong>No:</strong> Install the required STO jumper per the GA800 manual if the drive is intended for local operation without an external safety system, then clear the fault and test.</div>
</details>

<details class="dtree"><summary>Are all E-stop buttons, guard doors, and safety relays in the reset (run-enabled) position?</summary>
<div class="dtree-body"><strong>Yes:</strong> The external devices are reset. Check wiring continuity and terminal assignments.<br><strong>No:</strong> Reset all E-stops and close all guard doors. If a safety relay is latched, cycle power to it or press its reset button, then clear the fault and test.</div>
</details>

<details class="dtree"><summary>With a multimeter, do you measure continuity (closed circuit) across the STO input terminals when the safety chain should be active?</summary>
<div class="dtree-body"><strong>Yes:</strong> The safety loop is electrically closed. Verify the drive parameters assign the correct terminals to the STO function and that no other parameter is blocking enable.<br><strong>No:</strong> An open circuit exists. Trace the wiring from the drive STO terminals through each safety device and relay contact to find the break, then repair or replace the failed component.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the fault display** on the keypad shows E59 and confirm the drive otherwise powers up normally without other alarms.
2. **Inspect the STO terminals** on the GA800 control terminal strip. If the drive is configured for local operation, confirm the required jumper wire or plug is installed and seated. If missing, install it per the wiring diagram in the drive manual.
3. **Check the external safety circuit** if the drive is wired to E-stops, guard interlocks, or a safety relay. Verify all devices are in the run-enabled state (E-stops pulled out, doors closed, relay outputs energized).
4. **Measure continuity** across the STO input loop with a multimeter. You should see a closed circuit (near zero ohms) when the safety chain is satisfied. An open reading indicates a broken wire, open contact, or failed relay.
5. **Verify terminal function parameters** in the drive setup menu. Confirm the terminals assigned to the STO safety inputs match your wiring and that no parameter changes have disabled the safety circuit.
6. **Repair or replace the failed component**. Restore the jumper, repair broken wiring, replace a failed E-stop or guard switch, or swap out a faulty safety relay. make sure all connections are tight and clean.
7. **Clear the E59 fault** from the keypad, then command the drive to run. The drive should enable and produce torque normally. If the fault returns immediately, recheck the safety loop for intermittent connections or a device that is not fully closing.

## Parts Often Needed

| Part | Notes |
|------|-------|
| STO terminal jumper or plug | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e59-fault-code&k=STO+terminal+jumper+or+plug&tag=errorcodefixes-20) \| Factory-supplied or field-fabricated short jumper wire to close the STO loop when no external safety system is used. |
| Safety relay module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e59-fault-code&k=Safety+relay+module&tag=errorcodefixes-20) \| Pilz, Schmersal, or equivalent dual-channel safety relay if the existing relay is confirmed failed. Match voltage and contact rating. |
| E-stop pushbutton or guard interlock switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e59-fault-code&k=E-stop+pushbutton+or+guard+interlock+switch&tag=errorcodefixes-20) \| Direct replacement for the failed safety device in the chain. Verify contact configuration (normally open or normally closed). |
| Control terminal block or interface board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e59-fault-code&k=Control+terminal+block+or+interface+board&tag=errorcodefixes-20) \| If the STO input circuit on the drive itself is damaged. Consult Yaskawa support for the correct part number for your GA800 frame size. |

## When to Call a Pro

Call a qualified electrician or controls technician if you are not trained to work on industrial VFDs or safety circuits. The STO function is part of a machine safety system, and incorrect wiring or bypassing safety devices can create serious hazards. A professional will verify the safety relay configuration, trace the entire STO wiring chain, measure loop continuity, and make sure all parameters are set correctly. If the drive control board or terminal interface is damaged, a tech can order the correct Yaskawa service part and perform board-level replacement. Do not attempt to jumper out safety devices or modify the STO circuit without understanding the machine's safety design and local code requirements.

**Rough cost:** A pro service call runs about $150–400 depending on whether the fix is a jumper restore, wiring repair, or safety relay replacement.
