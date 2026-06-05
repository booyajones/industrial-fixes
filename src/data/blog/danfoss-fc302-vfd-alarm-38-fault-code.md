---
title: "Danfoss FC302 VFD Alarm 38 - Causes & Fix"
description: "Alarm 38 on a Danfoss FC302 is an internal fault caused by a control-to-power card communication error. Reseat boards first."
pubDatetime: 2026-06-03T10:47:29Z
modDatetime: 2026-06-03T10:47:29Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss FC302 VFD Alarm 38 — What It Means

Alarm 38 on the Danfoss VLT FC 302 indicates an internal fault within the drive itself, not a motor-side problem like overload or phase loss. Danfoss classifies this as a communication error between the control card and the power card. The alarm typically appears with a subcode number that identifies the fault category more precisely, so you should record that number from the display before troubleshooting.

This fault means something has failed or become disconnected inside the drive enclosure. It is not a wiring or configuration issue on the motor or line side. The drive's internal boards talk to each other through ribbon cables and connectors, and Alarm 38 flags a breakdown in that communication path.

[Jump to Fix](#fix)

## Common Causes

- **Loose or poorly seated internal connections** The most commonly cited cause is a loose, missing, or partially seated connection between the control board, power board, and any installed option cards.
- **Control card to power card communication failure** The manufacturer describes Alarm 38 as a communication error between these two main boards, which can occur even when connections appear intact.
- **Failed control card** If reseating does not clear the fault, the control card itself may have failed and lost the ability to communicate with the power board.
- **Failed power card** The power board can also fail internally and stop responding to control signals, triggering the same alarm.
- **Incompatible or failed option card** An installed option card that has failed or is not fully compatible with the firmware can interrupt the internal communication bus.
- **Board-to-board connector damage** Ribbon cables or board-edge connectors that have become damaged, corroded, or bent will prevent reliable communication between cards.

## Step-by-Step Fix {#fix}

1. **Lock out power and verify safe shutdown** by following your site's electrical safety procedures, then confirm the DC bus inside the drive has fully discharged before opening the enclosure.
2. **Record the full alarm code and subcode** shown on the FC 302 display, because Danfoss states that Alarm 38 includes a code number that identifies the fault more specifically.
3. **Power-cycle the drive** by removing power, waiting at least one minute, then restoring power to see if the alarm clears on its own.
4. **Inspect all internal connections** between the control card, power card, and any option boards, looking for loose ribbon cables, partially seated cards, or damaged connectors.
5. **Reseat all boards and connectors** by carefully removing each card, inspecting the connectors and edge contacts for damage or corrosion, and firmly pressing each board back into its socket.
6. **Replace the control card first** if the alarm returns after reseating, because field experience and manufacturer guidance point to the control board as the most common failed component for this alarm.
7. **Replace the power card or option card** if a new control card does not resolve the fault, and contact Danfoss technical support with your model, serial number, and subcode if board replacement does not clear Alarm 38.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC 302 control card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-38-fault-code&k=Danfoss+FC+302+control+card&tag=errorcodefixes-20) \| Verify your exact FC 302 frame size and firmware version before ordering to make sure board compatibility. |
| Danfoss FC 302 power card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-38-fault-code&k=Danfoss+FC+302+power+card&tag=errorcodefixes-20) \| Match the power card to your drive's voltage and current rating, available from the nameplate or original documentation. |
| Danfoss FC 302 option card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-38-fault-code&k=Danfoss+FC+302+option+card&tag=errorcodefixes-20) \| Only required if you have an installed option module that handles fieldbus, I/O expansion, or encoder feedback. |

## When to Call a Pro

Call a qualified VFD technician or industrial controls specialist if you are not trained in working inside energized or recently de-energized industrial drives, because the DC bus can hold lethal voltage even after AC power is removed. Also call for help if reseating boards and replacing the control card does not clear Alarm 38, if you do not have the tools to safely discharge the DC bus, or if your facility requires that only certified personnel open drive enclosures. Danfoss technical support should be contacted with your drive's model number, serial number, and the full alarm subcode if board-level troubleshooting does not resolve the fault, because some internal faults require factory-level diagnostics or firmware updates.
