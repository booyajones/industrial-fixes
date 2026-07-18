---
title: "Yaskawa GA800 E80 Fault - Causes & Fix"
description: "E80 on a Yaskawa GA800 means the soft-charge bypass relay did not confirm closure after precharge. Re-energize the drive once first."
pubDatetime: 2026-06-07T10:18:49Z
modDatetime: 2026-06-07T10:18:49Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
most_likely_cause: "Failed soft-charge bypass relay or contactor"
likelihood: "the most common cause"
diy_or_pro: "pro"
money_part: "GA800 soft-charge bypass relay or contactor"
---

## Yaskawa GA800 E80 Fault — What It Means

E80 is a soft-charge answerback fault. The drive expected the soft-charge bypass relay to close and report back after the precharge cycle, but the confirmation signal never arrived. This means the drive believes the precharge and bypass sequence did not complete correctly.

The fault points to a problem in the precharge/bypass circuit or the control sensing path that monitors the relay. The drive's internal logic is waiting for electrical confirmation that the relay has closed, and when it does not see that signal within the expected time window, it throws E80 and shuts down to protect the power stage.

## Before You Replace Anything

Technicians sometimes replace the entire drive when the control board or bypass relay alone is at fault. Check parameter U4-06 (PreChargeRelayMainte) first to see the relay's performance life before ordering a complete drive.

[Jump to Fix](#fix)

## Common Causes

- **Soft-charge bypass relay or contactor damage** The relay contacts may be welded, burned, or mechanically stuck so the drive does not see the expected closed-circuit confirmation.
- **Failed control board** The board may not be driving the relay coil correctly or the answerback sensing circuit on the board has failed.
- **Relay at end of maintenance life** If parameter U4-06 reads above 90%, the relay has cycled near its design limit and may no longer close reliably.
- **Wiring damage in the bypass circuit** Loose connections, broken wires, or corroded terminals between the relay and the drive control can block the answerback signal.
- **Failed drive power stage** Internal circuitry related to the precharge sequence may be damaged, especially after a surge or overvoltage event.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear after you power-cycle the drive once?</summary>
<div class="dtree-body"><strong>Yes:</strong> The relay may have been stuck temporarily. Monitor for recurrence and check U4-06 to see if the relay is nearing end of life.<br><strong>No:</strong> The relay, control board, or drive power stage has a persistent fault. Proceed to inspect U4-06 and the bypass relay.</div>
</details>

<details class="dtree"><summary>Is parameter U4-06 (PreChargeRelayMainte) above 90%?</summary>
<div class="dtree-body"><strong>Yes:</strong> Replace the control board or the complete drive per Yaskawa's maintenance guidance, as the relay has reached its cycle limit.<br><strong>No:</strong> The relay itself may have failed early or the control board sensing circuit is bad. Inspect the relay and wiring next.</div>
</details>

<details class="dtree"><summary>Do you hear or see the bypass relay energize during power-up?</summary>
<div class="dtree-body"><strong>Yes:</strong> The relay coil is being driven but the answerback circuit is not working. Check wiring to the control board and consider board replacement.<br><strong>No:</strong> The relay coil is not being driven. Check control board outputs and replace the board if no output is present.</div>
</details>

## Step-by-Step Fix {#fix}

1. **De-energize the drive** and follow lockout/tagout. Wait for the DC bus capacitors to discharge fully before opening any covers.
2. **Re-energize the drive** and attempt to run it. Yaskawa troubleshooting specifically recommends power-cycling once as the first action for E80.
3. **Check parameter U4-06** on the keypad or software interface. This parameter shows the precharge relay maintenance life as a percentage.
4. **Inspect the soft-charge bypass relay** visually if U4-06 is below 90% but the fault persists. Look for burned contacts, discolored housing, or a burned coil smell.
5. **Check all wiring** between the bypass relay and the control board. Tighten any loose ring terminals and verify continuity on answerback signal wires.
6. **Replace the control board** if U4-06 is above 90% or if the relay shows no visible damage but the fault remains. Yaskawa's maintenance guidance points to board or drive replacement at high cycle counts.
7. **Replace the complete drive** if a new control board does not clear the fault. Internal power-stage circuitry may be damaged and is not field-repairable on the GA800.

## Parts Often Needed

| Part | Notes |
|------|-------|
| GA800 soft-charge bypass relay or contactor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e80-fault-code&k=GA800+soft-charge+bypass+relay+or+contactor&tag=errorcodefixes-20) \| Part number varies by drive frame size. Consult your GA800 model's parts list or contact Yaskawa for the correct relay assembly. |
| GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e80-fault-code&k=GA800+control+board&tag=errorcodefixes-20) \| Order by drive model and serial number. Some GA800 frames use a plug-in control card that can be swapped in the field. |
| Complete GA800 drive assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e80-fault-code&k=Complete+GA800+drive+assembly&tag=errorcodefixes-20) \| Required if the fault persists after board replacement or if U4-06 is above 90% and Yaskawa recommends drive replacement. |

## When to Call a Pro

Call a qualified industrial electrician or automation technician for E80 faults. The diagnostic steps require safe access to the drive's DC bus, control terminals, and internal relay circuits under live conditions. Mishandling the precharge circuit or the DC bus capacitors can cause severe electric shock or damage to the drive. A technician will also have the correct metering equipment to verify answerback signals, check relay coil resistance, and safely measure DC bus voltage during the precharge sequence. If U4-06 is above 90%, Yaskawa's guidance points to board or drive replacement, and a pro can order the correct part by serial number and install it with the proper firmware checks.

**Rough cost:** A pro service call runs about $300-1200 depending on whether the relay, control board, or complete drive needs replacement.

## See Also

- [Yaskawa GA800 Er-04 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-f049-fault-code/)
- [Yaskawa GA800 E85 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e85-fault-code/)
- [Yaskawa GA800 CPF24 - Causes & Fix](/posts/yaskawa-ga800-vfd-f024-fault-code/)
- [Yaskawa GA800 E62 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e62-fault-code/)
