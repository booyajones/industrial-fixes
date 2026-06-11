---
title: "Yaskawa GA800 E05 Fault - Causes & Fix"
description: "E05 on a Yaskawa GA800 VFD signals a communication or watchdog error on the industrial network interface. Most often fixed by reseating network cables or correcting node addressing."
pubDatetime: 2026-06-04T09:24:09Z
modDatetime: 2026-06-04T09:24:09Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa GA800 option communication card"
---

## Yaskawa GA800 E05 Fault — What It Means

The E05 fault (sometimes labeled bUS or similar depending on option card and firmware) indicates the GA800 drive has lost valid cyclic communication with the controller over its installed industrial network interface. This is not a motor overcurrent or overvoltage problem. The drive is either not receiving network data within the configured watchdog time or the fieldbus option card has detected a communication exception. The error applies to drives equipped with optional network cards for protocols like EtherNet/IP, PROFINET, or MECHATROLINK.

Unlike basic I/O or hardwired control faults, E05 means the drive and PLC or master controller are not exchanging data properly over the digital network. The drive will stop or refuse to run because it depends on continuous command and status traffic from the upstream controller.

[Jump to Fix](#fix)

## Common Causes

- **Broken or loose network cable** Physical damage, poor crimps, or unseated RJ45 or D-sub connectors between the PLC and drive or between the drive and network switch interrupt data flow.
- **Incorrect node address or network parameters** Mismatched IP address, station number, baud rate, or protocol selection in either the drive or the controller prevents valid handshake and cyclic communication.
- **PLC program not scanning or producing output** The master controller's communication task has faulted, the output assembly is not being sent, or a gateway timeout has stopped cyclic data to the drive.
- **Bad network switch, coupler, or media converter** A failed or misconfigured intermediate network device in the path drops packets or blocks traffic to the drive.
- **Poorly seated or defective option card** The installed fieldbus communication card is not fully inserted into the drive backplane or has an internal failure.
- **Improper termination or shielding** Missing terminators, incorrect topology, or poor shield grounding on the chosen network protocol causes signal reflection or noise-induced errors.

## Step-by-Step Fix {#fix}

1. **Identify the installed option card** by opening the drive enclosure and reading the label on the network interface module to confirm which protocol (EtherNet/IP, PROFINET, MECHATROLINK, or other) is in use.
2. **Inspect all network cables and connectors** for visible damage, verify each connector clicks or seats fully, and check that link and activity LEDs on the drive and upstream switch or coupler are lit and blinking.
3. **Verify drive network settings** using the keypad or DriveWizard software by comparing node address, IP settings, baud rate, and protocol selection against the controller's configuration and network documentation.
4. **Confirm the PLC or master controller** is running, the communication task shows no faults, and the output assembly to this drive node is being produced and scanned continuously.
5. **Reseat the option card** by powering down the drive, removing and then firmly reinserting the communication module into its slot, and securing all mounting screws.
6. **Power-cycle the drive** after correcting wiring or configuration changes, then clear the E05 fault from the keypad and command a start to verify communication is restored.
7. **Swap in a known-good cable or option card** if the fault persists to isolate whether the failure is in the wiring, the network infrastructure, or the card itself.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 option communication card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e05-fault-code&k=Yaskawa+GA800+option+communication+card&tag=errorcodefixes-20) \| Protocol-specific module (EtherNet/IP, PROFINET, etc.) matching your installed network. Consult Yaskawa for exact part number. |
| Industrial Ethernet cable (shielded) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e05-fault-code&k=Industrial+Ethernet+cable+%28shielded%29&tag=errorcodefixes-20) \| Cat5e or Cat6 with metal RJ45 connectors for EtherNet/IP or PROFINET installations. |
| Network switch or managed Ethernet switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e05-fault-code&k=Network+switch+or+managed+Ethernet+switch&tag=errorcodefixes-20) \| Industrial-grade switch if the existing unit is suspected of port failure or packet loss. |

## When to Call a Pro

Call a controls technician or system integrator if you are not familiar with industrial network protocols, PLC programming, or drive parameter configuration. Communication faults require coordinated troubleshooting of both the drive and the upstream controller. A professional can use network diagnostic tools to capture traffic, verify cyclic data integrity, and update PLC logic or drive firmware if needed. Also call for help if swapping cables and reseating the card do not clear the fault, since the issue may lie in the PLC program, network topology, or a deeper drive electronics fault that requires factory support.

## See Also

- [Yaskawa GA800 E16 Fault Code - Causes & Fix](/posts/yaskawa-ga800-e16-fault-code/)
- [Yaskawa GA800 E30 Fault Code - Causes & Fix](/posts/yaskawa-ga800-vfd-e30-fault-code/)
- [Yaskawa GA800 E38 Fault Code - Causes & Fix](/posts/yaskawa-ga800-vfd-e38-fault-code/)
- [Yaskawa GA800 E24 Fault Code - Causes & Fix](/posts/yaskawa-ga800-vfd-e24-fault-code/)
