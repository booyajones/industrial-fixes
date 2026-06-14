---
title: "Siemens Micromaster F0060 - Causes & Fix"
description: "Siemens Micromaster F0060 (ASIC Timeout) indicates an internal communications failure in the drive. Learn diagnosis and replacement steps."
pubDatetime: 2026-05-29T09:35:13Z
modDatetime: 2026-05-29T09:35:13Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Siemens Micromaster 420 or 440 inverter (complete drive)"
---

## Siemens Micromaster F0060 — What It Means

F0060 is labeled ASIC Timeout by Siemens and signals an internal communications failure inside the Micromaster 420 or 440 inverter. The drive's application-specific integrated circuit (ASIC) did not finish its required processing or internal handshake in the expected time window. This is not a motor, cable, or load problem. It is a failure inside the drive's own control electronics. Siemens classifies F0060 as an internal fault and directs technicians to replace the inverter if the code persists.

[Jump to Fix](#fix)

## Common Causes

- **Internal control electronics fault** A component or circuit inside the drive's processor board has failed or degraded, preventing normal ASIC operation.
- **ASIC or processor board timeout** The application-specific integrated circuit did not complete its internal communication cycle in the allowed time window.
- **Intermittent board-level issue** Solder joints, traces, or connections on the control PCB may be failing intermittently under thermal or vibration stress.
- **Drive firmware or software anomaly** Although not explicitly listed by Siemens, a corrupted firmware state can prevent the ASIC from completing handshake cycles.

## Step-by-Step Fix {#fix}

1. **Verify the fault code** on the drive display to confirm it reads exactly F0060 and not a different internal fault number.
2. **Acknowledge and reset the fault** using the drive's keypad or control panel and observe whether the fault clears and stays cleared.
3. **Power-cycle the inverter** completely by disconnecting mains power for at least 30 seconds, then re-energize and check for fault return.
4. **Monitor the drive during startup and run** to see if F0060 reappears immediately, intermittently, or stays cleared after the reset.
5. **If the fault persists or returns**, prepare to replace the complete inverter unit, as Siemens documentation specifies drive replacement for recurring F0060.
6. **Contact Siemens Customer Support or Service Department** to confirm warranty status, obtain a replacement drive, and arrange return or disposal of the faulty unit.
7. **Install the replacement Micromaster inverter** and verify parameter settings match the application before returning the system to service.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens Micromaster 420 or 440 inverter (complete drive) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-f0060-fault-code&k=Siemens+Micromaster+420+or+440+inverter+%28complete+drive%29&tag=errorcodefixes-20) \| Match the exact model number and power rating of your existing drive. F0060 requires full drive replacement, not a sub-board. |

## When to Call a Pro

Call a qualified technician or Siemens service partner if you are not trained to isolate mains power, handle VFD wiring, or configure drive parameters. F0060 is an internal electronics fault that cannot be repaired in the field by replacing fuses, resetting parameters, or adjusting motor settings. Because Siemens directs replacement of the entire inverter for persistent F0060 faults, professional support ensures correct drive selection, safe electrical work, and proper commissioning of the new unit. If your system is under warranty or service contract, contact Siemens or your distributor before attempting any replacement.

## See Also

- [Siemens G120 F01600 - Causes & Fix](/posts/siemens-g120-vfd-f01600-fault-code/)
- [Siemens Micromaster F0011 - Causes & Fix](/posts/siemens-micromaster-f0011-fault-code/)
- [Siemens Micromaster F0070 - Causes & Fix](/posts/siemens-micromaster-f0070-fault-code/)
- [Siemens VFD F1 Fault - Causes & Fix](/posts/siemens-vfd-f1-fault/)
