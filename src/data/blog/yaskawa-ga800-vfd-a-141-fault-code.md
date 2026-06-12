---
title: "Yaskawa GA800 A.141 Fault - Causes & Fix"
description: "A.141 is a Safe Torque Off (STO) safety circuit fault. The drive will not run until the STO input loop is closed or the jumper is restored."
pubDatetime: 2026-06-10T10:51:51Z
modDatetime: 2026-06-10T10:51:51Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "STO terminal jumper wire"
most_likely_cause: "Missing or removed jumper on the STO terminals"
likelihood: "the most common cause"
diy_or_pro: "pro"
---

## Yaskawa GA800 A.141 Fault — What It Means

The A.141 indication on a Yaskawa GA800 is a Safe Torque Off (STO) condition. The drive has detected that the STO safety circuit is not satisfied, so torque production is inhibited and the motor will not run until the safety input condition is restored. The GA800 has a built-in Safe Torque Off function that prevents torque production to the motor even while main input power remains present.

In practice, the drive is being held in a safe-disabled state because the STO input chain is open, missing, miswired, or otherwise not in the required energized or closed condition. This is a safety-circuit issue, not a motor overload or drive power-stage failure.

## Before You Replace Anything

Technicians sometimes replace the drive or power stage when the real issue is simply a missing jumper wire or open safety relay upstream. Always verify STO terminal continuity and safety-device status before ordering drive hardware.

[Jump to Fix](#fix)

## Common Causes

- **Missing or removed jumper on STO terminals (~40%)** When the drive is not wired into a safety relay or controller, a jumper loop must connect the STO terminals, and removing it prevents the drive from running.
- **Safety relay not energized or not reset (~25%)** An upstream safety relay or PLC output that is supposed to close the dual-channel STO inputs has dropped out or failed to reset after an E-stop event.
- **Miswiring of STO terminals (~15%)** After installation or maintenance, the safety conductors were landed on the wrong terminals or swapped, leaving the STO loop incomplete.
- **Broken or loose field wiring in the STO loop (~10%)** An open circuit in the interlock chain from damaged, loose, or disconnected safety wiring prevents the STO inputs from closing.
- **External safety device tripped upstream (~7%)** An E-stop button, guard switch, light curtain, or other safety device in the chain is open and holding the STO circuit inactive.
- **Incorrect terminal-function parameterization (~3%)** The drive was customized for a safety application and the STO terminal assignments or safety parameters were reassigned improperly.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the drive installed without an external safety relay or E-stop chain?</summary>
<div class="dtree-body"><strong>Yes:</strong> Check the STO terminals on the drive for the required jumper wire. If it is missing or loose, install or reseat the jumper per the GA800 installation diagram and clear the fault.<br><strong>No:</strong> Proceed to verify that all upstream safety devices (relays, E-stops, guard switches) are reset and providing closed outputs to the drive STO inputs.</div>
</details>

<details class="dtree"><summary>Are all external safety devices (E-stops, guard switches, safety relays) reset and healthy?</summary>
<div class="dtree-body"><strong>Yes:</strong> Measure continuity through the entire STO field-wiring loop from the safety-device outputs to the drive terminals. An open reading indicates a break or loose connection in the chain.<br><strong>No:</strong> Reset or repair the tripped safety device, then clear the A.141 fault and test-run the drive.</div>
</details>

<details class="dtree"><summary>Does the STO wiring show continuity and match the installation diagram exactly?</summary>
<div class="dtree-body"><strong>Yes:</strong> Recheck the drive terminal-assignment parameters and consult Yaskawa technical support with the model number, serial number, and wiring details if the fault persists.<br><strong>No:</strong> Correct the miswiring or repair the broken conductor, then clear the fault and verify normal operation.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Lock out and tag out** the drive per site safety procedures before touching control wiring or terminals.
2. **Confirm the fault code** on the keypad is A.141 and verify that the drive is otherwise powered normally with no additional alarms.
3. **Inspect the STO wiring and terminals** on the GA800 and compare the actual connections to the installation diagram in the drive manual.
4. **Check for the required jumper** if the drive is not integrated into a safety relay. Install the jumper between the STO-related terminals if it is missing.
5. **Verify the safety relay or safety PLC outputs** are energized and actually closing the STO channels. Reset any E-stop or guard-switch devices in the chain.
6. **Measure continuity** through the safety loop from the safety device through the field wiring to the drive STO inputs, looking for opens, loose terminals, or damaged conductors.
7. **Restore the proper STO state**, clear the A.141 fault at the keypad, and test-run the drive under controlled conditions to confirm normal operation.
8. **Escalate to Yaskawa technical support** with model and spec number, serial number, and detailed failure description if the fault persists after verifying all wiring and safety devices.

## Parts Often Needed

| Part | Notes |
|------|-------|
| STO terminal jumper wire | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-141-fault-code&k=STO+terminal+jumper+wire&tag=errorcodefixes-20) \| Factory jumper or equivalent rated for the STO circuit; consult GA800 installation manual for part number and terminal location. |
| Safety relay (dual-channel) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-141-fault-code&k=Safety+relay+%28dual-channel%29&tag=errorcodefixes-20) \| If the existing safety relay has failed; must provide dual outputs compatible with GA800 STO inputs. |

## When to Call a Pro

Call a qualified industrial electrician or controls technician if you are not trained in lockout/tagout procedures, if you cannot locate the STO terminals or safety wiring on the drive, or if the fault persists after verifying external safety devices and jumpers. Because the STO function is a safety-rated circuit, incorrect wiring or bypassing the safety loop can create a serious hazard. If the drive continues to report A.141 after all field wiring and safety devices have been confirmed correct, contact Yaskawa technical support with the drive model, serial number, and application details before replacing any drive hardware.

**Rough cost:** A pro service call runs about $150-400.
