---
title: "Danfoss FC302 Alarm 34 - Causes & Fix"
description: "Danfoss FC302 Alarm 34 means fieldbus communication fault. Learn causes, diagnostic steps, and how to fix this VLT drive error."
pubDatetime: 2026-05-29T09:49:39Z
modDatetime: 2026-05-29T09:49:39Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss FC302 Alarm 34 — What It Means

Alarm 34 on a Danfoss VLT FC302 indicates a fieldbus communication fault. The drive has detected that the installed fieldbus or communication option card is not communicating properly with the network. This is not a motor overload, mains voltage problem, or internal power stage failure. It is a communication error between the drive's fieldbus interface and the controller or network it is supposed to connect to.

The fault typically appears when the drive has a communication option card installed (Profibus, BACnet, or similar) but the network master is offline, wiring is incorrect, or parameters do not match the network configuration. The drive can continue to run if control is switched away from the fieldbus source, confirming that the issue is isolated to the communication path and not the motor control hardware.

[Jump to Fix](#fix)

## Common Causes

- **No active network connection** The drive has a fieldbus option card installed but the bus master or controller is not running, not connected, or not polling the drive.
- **Incorrect fieldbus parameters** Node address, control-word source, or other communication settings do not match the network configuration or were not updated after a drive or card swap.
- **Wiring or termination problems** Fieldbus cable is loose, broken, reversed polarity, missing shield ground, or lacks proper termination resistors at the network ends.
- **Stale copied parameters after replacement** Parameters were copied from another drive but the new drive's node address or communication settings were not corrected for the actual network.
- **Failed or mismatched option card** The communication option card is damaged, unseated, or incompatible with the current drive firmware or network type.

## Step-by-Step Fix {#fix}

1. Identify the installed communication option by inspecting the option card slot on the drive (Profibus, BACnet, etc.) to understand which fieldbus network should be active.
2. Verify the network master or controller is online and actively polling devices, and confirm the drive is expected to be on that bus segment.
3. Inspect all fieldbus wiring at the drive terminals for loose connections, broken conductors, correct polarity, shield continuity, and proper termination resistors at both ends of the bus.
4. Check drive parameters for node address, communication timeout, and control-word source settings, comparing them to the network configuration and correcting any mismatches or stale values from copied parameter sets.
5. Temporarily change the control-word source away from fieldbus (to local keypad or analog input) to confirm the drive runs without the alarm, isolating the fault to the communication path.
6. Power-cycle the drive and the network master after verifying all wiring and parameters, then monitor for return of the alarm.
7. Replace the communication option card if the alarm persists with confirmed good wiring, correct parameters, and a healthy network, as the card itself is likely faulty.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Fieldbus communication option card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-34-fault-code&k=Fieldbus+communication+option+card&tag=errorcodefixes-20) \| Profibus, BACnet, or other protocol module specific to your FC302 installation and network type. |
| Fieldbus cable and connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-34-fault-code&k=Fieldbus+cable+and+connectors&tag=errorcodefixes-20) \| Shielded twisted-pair cable rated for your bus type, with correct connectors and termination resistors. |

## When to Call a Pro

Call a qualified technician if you are unfamiliar with fieldbus networks, do not have access to the network master or configuration software, or cannot identify the installed communication option card. Also call for help if the alarm returns after verifying all wiring and parameters, or if your process cannot tolerate downtime for trial-and-error diagnostics. Industrial communication networks often require specialized tools and training to troubleshoot correctly.
