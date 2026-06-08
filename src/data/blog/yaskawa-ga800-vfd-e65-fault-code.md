---
title: "Yaskawa GA800 E65 Fault - Causes & Fix"
description: "E65 on a Yaskawa GA800 means the Safe Torque Off (STO) safety circuit is open or interrupted. Most often an E-stop, safety relay, or STO wiring issue."
pubDatetime: 2026-06-06T11:49:37Z
modDatetime: 2026-06-06T11:49:37Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
most_likely_cause: "Open STO circuit from an E-stop, safety relay, door switch, guard switch, or interlock"
likelihood: "the most common cause"
diy_or_pro: "pro"
---

## Yaskawa GA800 E65 Fault — What It Means

E65 on the Yaskawa GA800 is a Safe Torque Off (STO) safety input-related fault. It means the drive's internal safe-torque-off safety circuit is open, inconsistent, or the STO-related input state does not meet the drive's run-permit requirement. The drive will inhibit torque production when the STO safety path is not satisfied, preventing motor operation until the safety chain is restored. The STO function is a built-in safety feature that responds to external safety devices like E-stops, guard switches, door interlocks, and safety relays.

This fault is almost always caused by the external safety chain rather than the drive itself. The GA800 is reporting that it does not see the required safety-relay output or jumper connection at its STO input terminals. Yaskawa's troubleshooting process starts by checking the safety circuit and wiring before replacing any drive components.

## Before You Replace Anything

Technicians sometimes replace the GA800 control board before verifying the external safety chain. Always check E-stop status, safety relay outputs, STO terminal wiring, and terminal tightening first. Most E65 faults clear once the external safety circuit is restored.

[Jump to Fix](#fix)

## Common Causes

- **Open STO circuit** An E-stop, safety relay, door switch, guard switch, or interlock is open or not energized, breaking the STO safety path to the drive.
- **Missing jumper or incorrect wiring** The STO terminals lack the required jumper or bridge when the drive is configured for simple run-permit use instead of a full safety relay.
- **Safety relay not energized** The upstream safety relay is not resetting correctly or is stuck in the tripped state, so the STO inputs never close.
- **Loose terminal connections** Loose or corroded terminal screws or damaged control wiring in the safety loop interrupt the STO circuit.
- **Incorrect parameter assignment** The drive's terminal function setup does not match the installed safety method or the STO-related digital input/output mapping is wrong.
- **Internal STO interface or control board issue** After the external safety chain has been verified good, the fault may point to the drive's control board or STO interface circuitry.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is an E-stop button pushed in, a safety relay tripped, or a guard door open?</summary>
<div class="dtree-body"><strong>Yes:</strong> Reset the E-stop, close the door, or clear the safety relay fault, then reset the drive fault. If E65 clears, the external safety chain was the cause.<br><strong>No:</strong> Move to the next check.</div>
</details>

<details class="dtree"><summary>Are the STO input terminals on the GA800 properly wired with a jumper or connected to a safety relay output?</summary>
<div class="dtree-body"><strong>Yes:</strong> The wiring is present. Check terminal tightness, continuity, and correct channel assignment.<br><strong>No:</strong> Install the correct STO jumper or connect the safety relay output to the STO terminals per the GA800 wiring diagram, then reset the fault.</div>
</details>

<details class="dtree"><summary>Does the fault clear after cycling the safety circuit and pressing RESET on the keypad?</summary>
<div class="dtree-body"><strong>Yes:</strong> The external safety chain was the cause. Monitor for intermittent opens.<br><strong>No:</strong> The fault persists with verified-good external wiring. The control board or STO interface circuitry may be faulty. Call Yaskawa service or a qualified technician.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Remove the drive from run command and lock out the machine.** make sure no one can restart the system while you are troubleshooting the safety circuit.
2. **Read the active fault on the keypad and confirm it is E65.** Note whether the fault is persistent or intermittent.
3. **Inspect the external safety chain first.** Check all E-stop devices, safety relay status indicators, guard switches, door interlocks, and any upstream safety PLC outputs that feed the GA800 STO inputs.
4. **Verify STO terminal wiring and jumpers.** Confirm that the correct jumper or bridge is installed if the application does not use an external safety relay. Check terminal tightness, look for broken conductors, swapped channels, or a missing common/return connection.
5. **Confirm the GA800 terminal function setup.** Review the drive parameters to verify the control terminal assignment matches the installed safety method and that STO-related functions are assigned correctly.
6. **Cycle the safety circuit and reset the fault.** After removing the cause, press the RESET button on the keypad to clear the E65 code.
7. **If E65 returns with verified-good external wiring, evaluate internal hardware.** At that point the likely candidates are the control board or STO interface circuitry. Contact Yaskawa service or a qualified drive technician for board-level diagnostics and replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| STO input wiring / safety loop wiring | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e65-fault-code&k=STO+input+wiring+%2F+safety+loop+wiring&tag=errorcodefixes-20) \| Check and repair before replacing drive components. |
| Safety relay / safety controller outputs | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e65-fault-code&k=Safety+relay+%2F+safety+controller+outputs&tag=errorcodefixes-20) \| The external relay feeding the STO circuit. |
| GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e65-fault-code&k=GA800+control+board&tag=errorcodefixes-20) \| Only if the fault persists after external circuit verification. Yaskawa service part. |

## When to Call a Pro

Call a qualified electrician or Yaskawa-trained technician if you are not familiar with industrial control wiring, safety relay logic, or VFD terminal assignments. E65 troubleshooting requires working with live control circuits and understanding the safety chain architecture. If the external safety circuit checks out but the fault persists, the control board or STO interface hardware is likely at fault and should be diagnosed and replaced by a professional. Do not bypass or jumper the STO circuit to force the drive to run, as this defeats the machine's safety system and violates safety standards.

**Rough cost:** A pro service call runs about $150–400 depending on whether the fix is wiring repair, safety relay replacement, or control board.
