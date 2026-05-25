---
title: "ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide"
description: "ABB ACS880 VFD fault codes in PLC-integrated applications: communication faults, fieldbus errors, and drive-PLC handshake troubleshooting."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - abb
  - acs880
  - plc
  - industrial
---

## ABB ACS880 PLC Integration Fault Codes — Quick Reference

When the ABB ACS880 is integrated with a PLC via PROFIBUS, PROFINET, EtherNet/IP, or Modbus TCP, additional fault categories appear related to communication, fieldbus, and process data mapping.

| [Fault Code](https://www.amazon.com/s?ascsubtag=ecf-abb-acs-drives-plc-fault&k=Fault+Code&tag=errorcodefixes-20) | Meaning | Quick Fix |
|-----------|---------|-----------|
| [7081 — Fieldbus Communication Loss](https://www.amazon.com/s?ascsubtag=ecf-abb-acs-drives-plc-fault&k=7081+%E2%80%94+Fieldbus+Communication+Loss&tag=errorcodefixes-20) | No communication from PLC master | Check network cable, IP, and master config |
| [7082 — Fieldbus Timeout](https://www.amazon.com/s?ascsubtag=ecf-abb-acs-drives-plc-fault&k=7082+%E2%80%94+Fieldbus+Timeout&tag=errorcodefixes-20) | Communication timeout exceeded | Check PLC cycle time and network load |
| [3210 — DC Bus Overvoltage](https://www.amazon.com/s?ascsubtag=ecf-abb-acs-drives-plc-fault&k=3210+%E2%80%94+DC+Bus+Overvoltage&tag=errorcodefixes-20) | Bus voltage too high | Check brake chopper and regen conditions |
| [3130 — Input Phase Loss](https://www.amazon.com/s?ascsubtag=ecf-abb-acs-drives-plc-fault&k=3130+%E2%80%94+Input+Phase+Loss&tag=errorcodefixes-20) | Input phase missing | Check fuses and supply connections |
| [2310 — Overcurrent](https://www.amazon.com/s?ascsubtag=ecf-abb-acs-drives-plc-fault&k=2310+%E2%80%94+Overcurrent&tag=errorcodefixes-20) | Output current limit exceeded | Check motor, cable, and load |
| [5091 — Encoder Communication](https://www.amazon.com/s?ascsubtag=ecf-abb-acs-drives-plc-fault&k=5091+%E2%80%94+Encoder+Communication&tag=errorcodefixes-20) | Encoder interface fault | Check encoder cable and module |
| [64A0 — Control Word Timeout](https://www.amazon.com/s?ascsubtag=ecf-abb-acs-drives-plc-fault&k=64A0+%E2%80%94+Control+Word+Timeout&tag=errorcodefixes-20) | Control word not updated by PLC | Check PLC program cycle |
| [7011 — Ethernet Adapter Fault](https://www.amazon.com/s?ascsubtag=ecf-abb-acs-drives-plc-fault&k=7011+%E2%80%94+Ethernet+Adapter+Fault&tag=errorcodefixes-20) | Ethernet adapter communication error | Cycle power on adapter, check settings |

## PLC Integration Fault Troubleshooting

### Fieldbus Communication Loss (7081)
This fault occurs when the ACS880 loses communication with the controlling PLC or SCADA system. Steps:
1. Verify network cable continuity on the fieldbus adapter (FPBA-01 for PROFIBUS, FENA-21 for PROFINET/EIP).
2. Confirm the PLC scanner cycle is within the fieldbus timeout window (Parameter 51.04 in ACS880).
3. Check that the PLC is in RUN mode and the drive is in its scan list.
4. Inspect connector pins on the fieldbus module — corrosion is common in wet environments.

### Control Word Timeout (64A0)
The PLC program is not updating the drive control word within the configured timeout period. Check the PLC communication task cycle time and the EDS/GSD file configuration.

### Process Data Mapping Issues
If the motor runs but speed or torque commands behave unexpectedly, verify the drive parameter group 51 (Fieldbus Adapter) and group 58 (Embedded Fieldbus) are configured to match the PLC's process data mapping.

## Common Integration Parameters

| [Parameter](https://www.amazon.com/s?ascsubtag=ecf-abb-acs-drives-plc-fault&k=Parameter&tag=errorcodefixes-20) | Function | Notes |
|-----------|---------|-------|
| [51.01](https://www.amazon.com/s?ascsubtag=ecf-abb-acs-drives-plc-fault&k=51.01&tag=errorcodefixes-20) | Fieldbus adapter type | Set to installed adapter |
| [51.04](https://www.amazon.com/s?ascsubtag=ecf-abb-acs-drives-plc-fault&k=51.04&tag=errorcodefixes-20) | Communication timeout | Set to 3× PLC cycle time |
| [58.01](https://www.amazon.com/s?ascsubtag=ecf-abb-acs-drives-plc-fault&k=58.01&tag=errorcodefixes-20) | Embedded fieldbus protocol | Modbus or EIP |
| [20.01](https://www.amazon.com/s?ascsubtag=ecf-abb-acs-drives-plc-fault&k=20.01&tag=errorcodefixes-20) | Speed reference source | Set to fieldbus |

## Jump to Fix

- **7081 loss of communication** → Check cable → Check PLC scan list → Check timeout settings
- **7082 timeout** → Increase timeout parameter → Check PLC cycle load
- **64A0 control word** → Trace PLC program → Verify output tag mapping

## When to Call a Pro
ABB drives specialists and system integrators can verify fieldbus configuration using ABB DriveStudio or Drive Composer software.

## Related Articles

- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
- [ABB ACS550 AF10 Fault — Causes & Fix](/posts/abb-acs550-af10-heatsink/)

## See Also

- [ABB VFD Fault 4110 — Causes & Fix](/posts/abb-vfd-fault-4110/)
- [ABB VFD Fault 3210 — Causes & Fix](/posts/abb-vfd-fault-3210/)
- [ABB ACS880 Fault 2310 - Overcurrent Diagnosis and Fix](/posts/abb-acs880-fault-2310/)
- [ABB ACS880 Fault 3130 — Input Phase Loss Causes & Fix](/posts/abb-acs880-fault-3130/)
