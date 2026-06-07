---
title: "Yaskawa GA800 E22 Error Code - Causes & Fix"
description: "E22 on a Yaskawa GA800 means serial communication transmission error. Check communication cable wiring, connections, and shorts first."
pubDatetime: 2026-06-05T09:56:24Z
modDatetime: 2026-06-05T09:56:24Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
---

## Yaskawa GA800 E22 Error Code — What It Means

E22 on the Yaskawa GA800 variable frequency drive indicates a serial communication transmission error. The drive has detected a problem in the communication line between the controller and the VFD. This is not a motor or power problem. It is a control signal or network path fault. The documented corrective action is to locate and repair wiring errors, disconnected cables, or short circuits in the serial communication cable.

[Jump to Fix](#fix)

## Common Causes

- **Incorrect communication cable wiring** Reversed conductors, wrong terminal assignments, or improper cable routing can prevent the drive from receiving clean serial data.
- **Disconnected or open cable** A broken wire, loose terminal, or unplugged connector in the serial communication circuit stops transmission and triggers the fault.
- **Short circuit in the communication cable** Damaged insulation or pinched wires that create a short between conductors or to ground will corrupt the signal.
- **Communication option card or network switch issue** If the drive uses a network option board, a fault in the card, its wiring, or the upstream switch or gateway can appear as E22.
- **Faulty control board communication interface** If wiring and cables are intact, the drive's control board communication circuit may have failed and require replacement.

## Step-by-Step Fix {#fix}

1. **Confirm the fault code** by checking the keypad or operator display to verify it reads E22 and not a different communication alarm.
2. **Inspect the serial communication cable** at both the drive and controller ends for loose terminals, reversed wires, damaged insulation, or broken conductors.
3. **Test the cable for opens and shorts** using a multimeter to check continuity and isolation between conductors and from each conductor to ground.
4. **Check network option wiring and connections** if the drive uses an option card or fieldbus module, and inspect any upstream switches or gateways for link status.
5. **Correct any wiring errors** by re-terminating cables to match the wiring diagram, and repair or replace any damaged cable sections.
6. **Clear the fault** from the drive keypad and cycle power if needed, then monitor the communication link to confirm the alarm does not return.
7. **Escalate to control board diagnosis** if the fault persists after cable and wiring repair, as the issue may be in the drive's communication interface hardware rather than field wiring.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Serial communication cable (shielded twisted-pair) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e22-fault-code&k=Serial+communication+cable+%28shielded+twisted-pair%29&tag=errorcodefixes-20) \| Match the cable type and gauge to your communication protocol and distance per the GA800 installation manual. |
| Communication option board or module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e22-fault-code&k=Communication+option+board+or+module&tag=errorcodefixes-20) \| If the drive uses a network option card (DeviceNet, Profibus, Ethernet/IP), confirm the part number with your drive serial tag. |
| GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e22-fault-code&k=GA800+control+board&tag=errorcodefixes-20) \| Replacement for the drive's internal control circuit if wiring is intact but communication faults persist. |

## When to Call a Pro

Call a qualified industrial technician or Yaskawa-authorized service provider if you cannot locate a wiring fault in the communication cable and the alarm returns after repairs. Communication faults that remain after correct wiring and cable replacement usually indicate a drive control board or option card failure that requires bench-level diagnosis and replacement. Have the drive model number, serial number, and a description of the communication setup (protocol, option cards, controller type) ready when you contact support.
