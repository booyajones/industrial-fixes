---
title: "Yaskawa GA800 E28 Fault - Serial Watchdog Timeout Fix"
description: "E28 on Yaskawa GA800 means serial interface watchdog timeout. Drive lost control data from PLC or controller. Diagnose comms and restore link."
pubDatetime: 2026-05-30T12:36:14Z
modDatetime: 2026-05-30T12:36:14Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Serial communication cable (shielded, twisted-pair)"
most_likely_cause: "Controller or PLC stopped transmitting"
---

## Yaskawa GA800 E28 Fault — What It Means

E28 is a serial interface watchdog timeout fault on the Yaskawa GA800 drive. It means the drive stopped receiving the expected control data over its serial communication link within the allowed time window. This is not a power stage, overcurrent, or motor fault. It is a communications supervision problem tied to the command data path from your PLC or controller to the drive.

When the drive is configured to run from a serial network (Modbus, for example) and the controller stops sending valid control words or heartbeat data, the watchdog timer expires and the drive trips E28. The drive protects itself by halting operation until communication is restored and the fault is cleared.

[Jump to Fix](#fix)

## Common Causes

- **Controller or PLC stopped transmitting** The PLC program halted, the communications task failed, or the network link was disabled in software.
- **Loss of serial control data** The drive is configured for serial command mode but is no longer receiving valid data packets from the connected device.
- **Wiring or connection problems** Loose terminals, damaged cable, reversed polarity, or poor shield termination on the serial network conductors.
- **Mismatched network settings** Protocol, node address, baud rate, parity, or watchdog timeout parameters do not match between the drive and controller.
- **Noise or EMI on the communication link** Electrical interference disrupts serial data packets and prevents the drive from recognizing valid control messages.
- **Failed communication option card or interface** The hardware module handling serial communications on the drive has failed or unseated from its connector.

## Step-by-Step Fix {#fix}

1. Confirm drive control source: verify in drive parameters that the GA800 is actually configured to accept run commands from the serial communications network, not from the keypad or analog inputs.
2. Check controller status: inspect your PLC or controller to confirm it is online, scanning normally, and actively sending control words and heartbeat data to the drive on the correct network address.
3. Inspect serial wiring and connectors: examine the cable, shield termination, terminal tightness, and connector seating on both the drive and controller ends, and repair any loose, damaged, or reversed conductors.
4. Verify network parameter match: compare protocol type, node or slave address, baud rate, parity, and watchdog timeout settings on both the drive and controller, and correct any mismatches.
5. Clear the fault and test: reset the E28 fault at the keypad or through the controller, restore communication, and run the system long enough under load to confirm the watchdog no longer trips.
6. Isolate the faulty component: if the fault persists with known-good wiring and controller data, test the communication option card or interface module, and swap or test the drive control board if necessary.
7. Contact Yaskawa technical support: if communication hardware and parameters are verified correct but E28 continues, provide model number, serial number, and fault details to Yaskawa for further diagnostic support.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Serial communication cable (shielded, twisted-pair) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e28-fault-code&k=Serial+communication+cable+%28shielded%2C+twisted-pair%29&tag=errorcodefixes-20) \| Replace if damaged, cut, or shield continuity is broken. |
| GA800 communication option card or interface module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e28-fault-code&k=GA800+communication+option+card+or+interface+module&tag=errorcodefixes-20) \| Required if the installed option card has failed or shows physical damage. |
| GA800 control board assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e28-fault-code&k=GA800+control+board+assembly&tag=errorcodefixes-20) \| Needed only if onboard communication circuitry is confirmed faulty after all external checks pass. |

## When to Call a Pro

Call a qualified technician or contact Yaskawa technical support if you have verified the PLC is transmitting correct data, all wiring and network settings are confirmed good, and the E28 fault still will not clear. Troubleshooting communication protocol issues or replacing the drive control board requires specialized knowledge of both the drive and your network architecture. If your facility does not have personnel trained in serial communications or VFD service, professional help will save time and prevent damage to the drive or connected equipment.

## See Also

- [Yaskawa GA700 Fault UV1 — Main Circuit Undervoltage Causes & Fix](/posts/yaskawa-ga700-fault-uv1/)
- [Yaskawa VFD Fault OH — Causes & Fix](/posts/yaskawa-vfd-fault-oh/)
- [Yaskawa GA800 E20 Fault Code - Causes & Fix](/posts/yaskawa-ga800-e20-fault-code/)
- [Yaskawa GA800 E10 Fault Code - Causes & Fix](/posts/yaskawa-ga800-e10-fault-code/)
