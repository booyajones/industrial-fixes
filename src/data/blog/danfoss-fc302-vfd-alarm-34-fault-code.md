---
title: "Danfoss FC302 Alarm 34 - Causes & Fix"
description: "Alarm 34 on a Danfoss FC302 VFD means fieldbus communication fault. Check the option card installation, wiring, and network settings."
pubDatetime: 2026-06-03T10:44:36Z
modDatetime: 2026-06-03T10:44:36Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss fieldbus communication option card"
most_likely_cause: "No valid fieldbus communication"
---

## Danfoss FC302 Alarm 34 — What It Means

Alarm 34 on the Danfoss FC302 is a fieldbus communication fault. The drive has detected that communication on the installed option card is not working correctly. This is officially documented by Danfoss as "WARNING/ALARM 34, Fieldbus communication fault" and appears when the fieldbus on the communication option card is not functioning.

This fault is tied specifically to the communication interface, not a motor problem or power issue. Depending on how your drive is configured, it may appear as a warning first or immediately trip the drive. The fault typically means the drive is expecting network communication but is not receiving valid data from the fieldbus option card.

[Jump to Fix](#fix)

## Common Causes

- **No valid fieldbus communication** The network is not connected, not active, or the drive is not being addressed correctly by the master controller.
- **Option card not properly seated** The communication option card is loose, not fully inserted, or has been disturbed during service or transport.
- **Loose or missing communication wiring** Fieldbus cables are disconnected, have broken conductors, or terminals are not securely fastened to the option card.
- **Incorrect node address or control parameters** After a drive replacement or parameter copy, the communication settings such as node address or control-word source do not match the network configuration.
- **Faulty communication option card** The fieldbus interface card itself has failed or been damaged and is no longer able to communicate with the network.
- **Drive configured for fieldbus but running standalone** The control source is set to expect network commands but the drive is intentionally being operated without an active fieldbus connection.

## Step-by-Step Fix {#fix}

1. **Verify the communication option card is installed.** Open the VFD enclosure and confirm the fieldbus card is fully seated in its slot, with any locking tabs or screws secure.
2. **Inspect all fieldbus wiring and connections.** Check that the network cable is firmly attached to the option card terminals, that there are no broken wires, and that shield connections are intact.
3. **Confirm the fieldbus network is active.** Use network diagnostic tools or check the master controller to verify the network is running and that the FC302's node address is being scanned.
4. **Review communication parameters in the drive.** Check the node address setting and verify the control-word source parameter matches your intended operation (fieldbus or local control).
5. **Power-cycle the drive.** Turn off power completely, wait 30 seconds, then restore power and observe whether Alarm 34 clears or returns immediately.
6. **Swap the communication option card if available.** If you have a spare or known-good fieldbus card, replace the existing card and test whether the fault disappears.
7. **Reconfigure control source if running standalone.** If the drive is not intended to use fieldbus control, change the control-word source parameter away from the communication option to clear the alarm.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss fieldbus communication option card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-34-fault-code&k=Danfoss+fieldbus+communication+option+card&tag=errorcodefixes-20) \| Match the card type (PROFIBUS, BACnet, or other) to your existing installation and network protocol. |
| Fieldbus network cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-34-fault-code&k=Fieldbus+network+cable&tag=errorcodefixes-20) \| Replace if cable shows physical damage, broken conductors, or intermittent continuity at the option card terminals. |

## When to Call a Pro

Call a qualified controls technician or VFD specialist if you are not familiar with fieldbus network configuration, if the alarm persists after reseating the card and verifying wiring, or if you do not have access to the network master controller to verify addressing. A professional can use network scanners and drive programming tools to diagnose whether the issue is in the option card hardware, the drive parameters, or the upstream network. If your process depends on the VFD running reliably, get help before swapping cards or changing control parameters that could affect production.

## See Also

- [Danfoss FC302 VFD ALARM 15 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-15-fault-code/)
- [Danfoss FC302 VFD Alarm 29 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-29-fault-code/)
- [Danfoss FC302 VFD Alarm 23 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-23-fault-code/)
- [Danfoss RX Controller Fault Codes — Troubleshooting Guide](/posts/danfoss-rx-controller-fault/)
