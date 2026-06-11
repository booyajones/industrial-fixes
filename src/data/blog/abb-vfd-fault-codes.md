---
title: "ABB VFD Fault Codes — ACS550, ACS880, ACS310 Reference"
description: "ABB VFD fault codes: complete reference for ACS310, ACS355, ACS550, ACS580, and ACS880 drives including 3130, 3210, and overcurrent faults."
pubDatetime: 2026-04-22T16:00:00Z
modDatetime: 2026-04-22T16:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "Input fuses"
---

## ABB VFD Fault Codes — Quick Reference

ABB drives display fault codes on the integral keypad panel as four-digit numbers or abbreviated text. Faults cause the drive to trip and stop the motor; alarms display but don't stop the drive. The fault history is stored in the drive's memory and can be retrieved via the control panel or Drive Composer software.

| Fault Code | Meaning | Common Fix |
|-----------|---------|-----------|
| 0001 | Overcurrent | Check motor/cable; reduce accel ramp |
| 2201 | Overcurrent (short circuit) | Motor winding short or cable fault |
| 2310 | Overcurrent (peak) | Check for mechanical jam |
| 3130 | Input phase loss | Check all 3 input phases |
| 3210 | DC bus overvoltage | Extend decel ramp; add brake resistor |
| 3300 | DC bus undervoltage | Check input power supply |
| 4110 | Drive overtemperature | Clean cooling fan; check ambient temp |
| 5010 | Overload | Reduce continuous load; check motor FLA |
| 7121 | Analog I/O fault | Check signal wiring |
| 9300 | Communication fault | Check fieldbus adapter or wiring |
| AF10 | Heatsink overtemperature | Clean fan; check airflow |

## Most Common Codes

### Fault 3130: Input Phase Loss
One of the three supply phases (L1, L2, or L3) is missing or has significantly reduced voltage. Check the input fuses (one per phase) — a blown fuse on one phase is the most common cause. Also check the main contactor (if installed) for a burned contact. Measure phase-to-phase voltage at the drive's L1/L2/L3 input terminals.

ABB drives will attempt to run on two phases briefly before tripping 3130. If the fault appears intermittently, check for a loose terminal screw or a contact with high resistance under load.

### Fault 2310: Overcurrent (Peak)
An instantaneous overcurrent trip — the drive output current exceeded the trip threshold. Causes: motor winding short, cable insulation failure, locked rotor (mechanical jam), or too-fast acceleration ramp. Start by megger-testing the motor and cable for insulation resistance (should be >1 MΩ at 500V). If insulation is good, check for mechanical issues and extend the acceleration time.

### Fault 3210: DC Bus Overvoltage
Regenerative energy from a decelerating motor raised the DC bus above the trip threshold. Solutions: (1) extend the deceleration ramp in parameter group 23 (ACS550) or 01.13 (ACS880), (2) enable the flux braking feature (available on ACS880 — uses motor resistance to dissipate energy), (3) install a dynamic braking resistor and chopper module for high-inertia loads.

### Fault 3300: DC Bus Undervoltage
Input supply voltage dropped too low. Check incoming voltage at the drive terminals under load. On ACS550 and ACS880 with a 380–480V supply, the minimum is approximately 270V DC bus (~338V AC input). A weak transformer, long cable runs, or undersized input conductors all contribute.

### Fault 4110: Drive Overtemperature
The drive's IGBT heatsink exceeded its temperature limit. Open the drive cabinet and inspect: (1) internal cooling fan — is it spinning? A failed fan is the #1 cause, (2) heatsink fins — clear with compressed air if clogged with dust, (3) ambient temperature — ACS550/ACS880 are rated to 40°C ambient without derating. Above that, the drive must be derated or better ventilation provided.

### Fault 0001 / 2201: Overcurrent
The drive output stage detected overcurrent above trip level. On ACS880, separate cause analysis is needed: fault 2201 (overcurrent on ground fault or winding short) is more serious than fault 0001 (transient overcurrent during starting). For 2201, use a megger before restarting — a shorted motor winding can damage the drive's output IGBTs.

### Fault 9300: Communication Fault
On ACS550/ACS880 drives with fieldbus adapters (Profibus, EtherNet/IP, Modbus), fault 9300 indicates loss of communication with the master. Check: adapter module is seated securely, fieldbus cable is connected, PLC/master is running and communicating. Fault 9300 can also mean the communication response time exceeded the configured watchdog timeout.

## Retrieving Fault History

On ACS550: Navigate to parameter group 14 (FAULT HISTORY). Parameters 14.01–14.03 show the three most recent faults with time stamps.

On ACS880: Use the Drive Composer PC tool for the full fault log, or navigate to Menu > Diagnostics > Fault Log on the control panel.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input fuses | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-vfd-fault-codes&k=Input+fuses&tag=errorcodefixes-20) \| ABB class J or gR fuses; size per drive catalog |
| Braking resistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-vfd-fault-codes&k=Braking+resistor&tag=errorcodefixes-20) \| ABB catalog OHBR or third-party sized per drive kW |
| Cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-vfd-fault-codes&k=Cooling+fan&tag=errorcodefixes-20) \| Drive-specific; ABB part for ACS550 fan: 68518560 |
| Fieldbus adapter | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-vfd-fault-codes&k=Fieldbus+adapter&tag=errorcodefixes-20) \| FCAN-01 (CAN), FPBA-01 (Profibus), FENA-21 (EIP) |
## When to Call a Pro
Faults 2201 (short circuit overcurrent) and any fault accompanied by a burning smell or blown fuses require qualified drive service. ABB's regional service centers offer warranty and post-warranty repair.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)

## See Also

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS550 EFB3 Fault - Causes & Fix](/posts/abb-acs550-vfd-efb3-fault-code/)
- [ABB ACS580 A7AB Fault - Causes & Fix](/posts/abb-acs580-a7ab-fault-code/)
- [ABB ACS580 FF63 Fault - STO Diagnostics Failure Fix](/posts/abb-acs580-vfd-ff63-fault-code/)
