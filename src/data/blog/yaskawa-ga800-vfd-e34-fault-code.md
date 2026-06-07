---
title: "Yaskawa GA800 E34 Fault Code - Causes & Fix"
description: "E34 is a soft-charge answerback fault on the GA800 VFD. The drive expected the precharge relay to signal completion but got no feedback."
pubDatetime: 2026-06-05T10:03:35Z
modDatetime: 2026-06-05T10:03:35Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
---

## Yaskawa GA800 E34 Fault Code — What It Means

The E34 fault on the Yaskawa GA800 VFD is a soft-charge answerback fault. This means the drive does not receive the expected feedback signal that the soft-charge (precharge) bypass relay has completed its transfer sequence. The drive energizes the relay to charge the DC bus capacitors safely, then expects a contact state change to confirm the relay has switched. When that answerback signal never arrives or arrives incorrectly, the drive throws E34 and stops.

This fault is tied to the soft-charge bypass relay hardware and its control circuit, not to motor overload or output phase problems. The relay itself may have worn or stuck contacts, or the control board that reads the answerback signal may have failed. In some cases the entire drive needs replacement if the fault persists after basic troubleshooting.

[Jump to Fix](#fix)

## Common Causes

- **Worn or damaged soft-charge bypass relay** Stuck contacts, pitted contacts, or a failed coil prevent the relay from completing the transfer and sending the answerback signal to the drive.
- **High relay maintenance life (U4-06 above 90%)** The drive tracks relay cycles in parameter U4-06, and values above 90% indicate the soft-charge bypass relay is near end of life and should be replaced.
- **Control board failure** If the relay hardware is intact, the control board that drives and reads the answerback circuit may have failed.
- **Answerback circuit wiring or connection fault** Loose, corroded, or broken connections in the answerback path prevent the drive from seeing the relay state change.
- **Drive-level failure requiring full replacement** When the fault persists after relay and board checks, the drive itself may have an internal fault that cannot be repaired at component level.

## Step-by-Step Fix {#fix}

1. **Power cycle the drive** and restart to see if the E34 fault clears on its own after a fresh energization.
2. **Check parameter U4-06 (PreChargeRelayMainte)** in the drive's maintenance menu. If the value is above 90%, the soft-charge bypass relay is near end of life and should be replaced.
3. **Inspect the soft-charge bypass relay and contactor** for signs of physical damage, pitting, or stuck contacts. Listen for the relay click during startup and verify the contacts move.
4. **Examine all wiring and connections** in the answerback circuit between the relay and the control board. Tighten, clean, or repair any loose or corroded terminals.
5. **Replace the control board** if the relay hardware is intact and the fault returns after power cycling, especially if U4-06 is high or the relay does not send a valid answerback signal.
6. **Consult the drive's elementary diagram** to identify the exact soft-charge bypass relay and answerback circuit path for your model before any board or relay replacement.
7. **Replace the entire drive** if the fault persists after control board replacement or if the unit is not repairable at component level.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Soft-charge bypass relay (contactor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e34-fault-code&k=Soft-charge+bypass+relay+%28contactor%29&tag=errorcodefixes-20) \| OEM part specific to your GA800 model. Check part number on the existing relay or consult factory service parts list. |
| Control board (GA800 VFD) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e34-fault-code&k=Control+board+%28GA800+VFD%29&tag=errorcodefixes-20) \| Replacement control board for your drive model. Verify exact model and serial number before ordering. |
| Complete GA800 drive replacement | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e34-fault-code&k=Complete+GA800+drive+replacement&tag=errorcodefixes-20) \| If the fault persists after relay and board replacement, the entire drive may need replacement rather than further field repair. |

## When to Call a Pro

Call a qualified industrial electrician or VFD technician if you are not trained to work inside energized or recently de-energized VFD cabinets. The DC bus capacitors can hold lethal voltage even after AC power is removed. If you have checked U4-06 and power cycled the drive but the fault returns, or if you do not have access to the elementary diagram and service documentation for your exact GA800 model, professional diagnosis is the safest path. Also call a pro if the fault persists after control board replacement, since drive-level failures often require factory support or warranty claim handling.
