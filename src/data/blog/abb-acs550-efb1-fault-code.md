---
title: "ABB ACS550 EFB1 Fault Code - Causes & Fix"
description: "ABB ACS550 EFB1 fault is a reserved fieldbus communication error. Learn protocol-specific causes and how to adjust timeout settings."
pubDatetime: 2026-05-28T09:07:52Z
modDatetime: 2026-05-28T09:07:52Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "Fieldbus communication cable"
most_likely_cause: "Master device not polling the drive"
---

## What this code means
The ACS550 EFB1 fault (fault code 31) is a reserved fault code for the Embedded Fieldbus (EFB) protocol application. ABB documents this as a communication-related fault, not a power stage hardware problem. The exact meaning depends on which fieldbus protocol your drive is using and how the control system is configured.

In most installations, this fault appears when the master controller (PLC, HMI, or network head) stops polling the drive within the configured timeout window, or when there is a mismatch between the drive's fieldbus settings and the actual network configuration. You must identify the active protocol and treat this as a network or communication fault until proven otherwise.

## Common Causes

- **Master device not polling the drive** The PLC, HMI, or network master has stopped communicating with the drive within the timeout period set in parameter 3019.
- **Communication timeout configured too short** Parameter 3019 COMM FAULT TIME is set lower than the actual polling cycle time of your network.
- **Bad communication wiring or connectors** Loose, open, shorted, or improperly terminated fieldbus cable connections at the drive or along the network.
- **Protocol or application mismatch** The drive's embedded fieldbus protocol settings do not match the master's configuration or the installed communication option module.
- **Network master offline or faulted** The controlling PLC or network head has stopped running or has its own communication fault.

## Step-by-Step Fix {#fix}

1. Identify the active fieldbus protocol on your drive by checking the control panel or parameter settings, because ABB states the meaning of EFB1 is protocol dependent.
2. Check whether the master device (PLC, HMI, or network controller) is online and actively polling the drive on the network.
3. Inspect all communication wiring and connectors at the drive terminal block and throughout the fieldbus network for loose connections, opens, shorts, or missing termination resistors.
4. Review parameter 3019 COMM FAULT TIME and increase the timeout value if your network polling cycle is longer than the current setting.
5. Verify the drive's embedded fieldbus protocol configuration matches the master's settings and the installed communication hardware.
6. Clear the fault after correcting the communication issue using the control panel, a configured digital input, or serial command (depending on parameter 1604 FAULT RESET SEL).
7. If the fault persists after all network and wiring checks, contact ABB or your local representative, as the ACS550 is not field repairable for internal drive faults.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Fieldbus communication cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs550-efb1-fault-code&k=Fieldbus+communication+cable&tag=errorcodefixes-20) \| Replace damaged or undersized cable between drive and network master per protocol specifications. |
| Fieldbus connectors and terminators | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs550-efb1-fault-code&k=Fieldbus+connectors+and+terminators&tag=errorcodefixes-20) \| Use correct termination resistors and rated connectors for the installed protocol (DeviceNet, Profibus, Modbus, etc.). |
| Embedded fieldbus option module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs550-efb1-fault-code&k=Embedded+fieldbus+option+module&tag=errorcodefixes-20) \| Consult your drive's type code and installed protocol. ABB may supply a replacement module for your specific variant. |

## When to Call a Pro

Call a qualified technician or ABB service if the fault persists after you have confirmed the master is polling correctly, the wiring is intact, and the timeout is appropriate. ABB documents the ACS550 as non-field-repairable for internal faults, so unresolved EFB1 codes that are not caused by network issues will require factory support or drive replacement through your ABB representative. Also call for help if you are unfamiliar with fieldbus networks, protocol configuration, or drive parameter adjustment.
