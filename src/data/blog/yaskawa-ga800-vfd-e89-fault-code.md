---
title: "Yaskawa GA800 E89 Fault - Causes & Fix"
description: "E89 means the soft-charge bypass relay did not send the expected feedback signal. Replace the control board or check relay maintenance life."
pubDatetime: 2026-06-07T10:25:28Z
modDatetime: 2026-06-07T10:25:28Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
most_likely_cause: "Damaged soft-charge bypass relay or contactor"
likelihood: "the most common cause"
diy_or_pro: "pro"
money_part: "Yaskawa GA800 control board (PCB)"
---

## Yaskawa GA800 E89 Fault — What It Means

E89 is a soft-charge answerback fault on the Yaskawa GA800 VFD. The drive's precharge circuit uses a bypass relay or contactor to safely energize the DC bus capacitors. When the relay closes, it is supposed to send a feedback signal back to the control board confirming the circuit completed correctly. This fault appears when the drive does not receive that expected answerback, meaning either the relay failed, the feedback path is broken, or the control board cannot read the signal.

The fault protects the drive from operating with a defective precharge sequence, which could lead to inrush current damage or unsafe conditions. The drive will not run until the bypass relay circuit and its feedback loop are verified and restored.

## Before You Replace Anything

Technicians sometimes replace the entire drive when the control board alone is at fault. Always check parameter U4-06 (PreChargeRelayMainte) first to see if relay life has expired, which points to a board or relay issue rather than the entire drive.

[Jump to Fix](#fix)

## Common Causes

- **Damaged soft-charge bypass relay or contactor** The relay that bridges the precharge resistor may have worn contacts, a burned coil, or mechanical failure that prevents it from closing or sending feedback.
- **Relay life exhausted** Parameter U4-06 tracks the maintenance counter for the precharge relay and flags when the relay has cycled too many times and needs replacement.
- **Control board failure** The board may no longer be able to read the answerback signal from the relay due to a failed input circuit, damaged trace, or component fault.
- **Broken feedback wiring or connector** The wire or terminal that carries the relay feedback signal to the control board may be loose, corroded, or broken, blocking the answerback path.
- **Drive internal circuit fault** If re-energizing and board replacement do not clear the fault, the drive itself may have a deeper internal failure in the precharge or feedback circuit.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear after turning the drive off and back on?</summary>
<div class="dtree-body"><strong>Yes:</strong> The relay may have recovered or the fault was transient. Monitor U4-06 and watch for recurrence.<br><strong>No:</strong> The relay, feedback circuit, or control board is likely damaged. Check U4-06 and proceed to board replacement.</div>
</details>

<details class="dtree"><summary>Is parameter U4-06 (PreChargeRelayMainte) above 90%?</summary>
<div class="dtree-body"><strong>Yes:</strong> Relay life is exhausted. Replace the control board or the drive as recommended by the manufacturer.<br><strong>No:</strong> The relay still has life remaining. Inspect wiring and connections, then replace the control board if fault persists.</div>
</details>

<details class="dtree"><summary>Does the fault remain after replacing the control board?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive itself has a deeper internal failure. Replace the entire VFD.<br><strong>No:</strong> The control board was the cause. The drive should now operate normally.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off the drive** and disconnect input power for at least 30 seconds to allow capacitors to discharge and reset internal logic.
2. **Re-energize the drive** and observe whether the E89 fault reappears immediately or clears on its own.
3. **Navigate to parameter U4-06** [PreChargeRelayMainte] in the drive menu and record the percentage value shown.
4. **If U4-06 is above 90%**, plan to replace the control board or the entire drive, as the relay has reached its maintenance limit and is likely failing.
5. **Inspect the soft-charge bypass relay** and its wiring for visible damage, loose terminals, or burnt contacts if the drive is accessible and you are qualified to work inside it.
6. **Replace the control board** if the fault persists after re-energizing and U4-06 is high or if wiring checks are clean.
7. **Replace the entire drive** if the fault remains after control board replacement, as the internal precharge circuit or feedback path is defective beyond board-level repair.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e89-fault-code&k=Yaskawa+GA800+control+board+%28PCB%29&tag=errorcodefixes-20) \| Order the correct board revision for your drive model and firmware version from Yaskawa or an authorized distributor. |
| Yaskawa GA800 VFD (complete drive replacement) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e89-fault-code&k=Yaskawa+GA800+VFD+%28complete+drive+replacement%29&tag=errorcodefixes-20) \| Required only if control board replacement does not resolve the fault or if U4-06 and board checks both point to a deeper internal failure. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician for all E89 diagnostics and repair. The fault involves high-voltage DC bus circuits, internal relay feedback paths, and control board replacement that require proper lockout/tagout, discharge procedures, and factory training. Accessing the interior of a VFD without proper safety procedures can result in lethal shock even after input power is removed. If your facility does not have trained personnel, contact a Yaskawa-authorized service center to inspect parameter U4-06, test the soft-charge bypass relay, replace the control board, or swap the drive. Never attempt to bypass or jumper the precharge circuit, as this can destroy the drive and create a fire or shock hazard.

**Rough cost:** A pro service call runs about $400–1,200 depending on whether a control board or full drive is needed.

## See Also

- [Yaskawa GA800 E24 Fault - Causes & Fix](/posts/yaskawa-ga800-e24-fault-code/)
- [Yaskawa GA800 E79 - Causes & Fix](/posts/yaskawa-ga800-vfd-e79-fault-code/)
- [Yaskawa A1000 AL16 - Causes & Fix](/posts/yaskawa-a1000-vfd-al-16-fault-code/)
- [Yaskawa A1000 AL-36 Fault - Causes & Fix](/posts/yaskawa-a1000-vfd-al-36-fault-code/)
