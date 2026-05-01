---
title: "Eaton PowerXL VFD Fault Codes Guide"
description: "Eaton PowerXL and DG1/DC1 VFD fault codes explained. Learn the most common overcurrent, undervoltage, overtemperature, and motor protection faults."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - eaton
  - vfd
  - industrial
  - error-code
---

## Eaton PowerXL VFD Fault Codes

Eaton PowerXL drives, including the **DG1**, **DC1**, and related series, use fault codes for incoming power problems, motor overload, overheating, and communication issues.

## Common Eaton Faults

| [Fault](https://www.amazon.com/s?k=Fault&tag=errorcodefixes-20) | Meaning | Quick Fix |
|---|---|---|
| OC | Overcurrent | Check motor short, accel too fast, jammed load |
| OV | DC bus overvoltage | Increase decel time, add brake resistor |
| UV | Undervoltage | Check supply sag, loose input wiring |
| OH | Drive overtemperature | Clean heatsink, verify fan airflow |
| OL | Motor overload | Check load and motor current settings |
| GF | Ground fault | Megger motor and cable, check leakage |
| PH | Input phase fault | Check 3-phase input and fuses |
| [COMM](https://www.amazon.com/s?k=COMM&tag=errorcodefixes-20) | Communication loss | Check fieldbus and control wiring |

## Most Common Real-World Causes

### OC — Overcurrent

Usually caused by:
- Motor cable short
- Mechanical jam
- Acceleration time set too short
- Incorrect motor data in parameters

### OV — Overvoltage

Common on high-inertia loads that stop too quickly. The regenerated energy raises DC bus voltage.

Fixes:
- Increase decel time
- Add dynamic braking resistor if supported
- Use coast-to-stop where acceptable

### OH — Overtemperature

PowerXL drives depend on clean airflow. Clogged panel filters and failed cooling fans are common causes.

## Bottom Line

Start with the basics: incoming power, motor condition, load condition, and airflow. Most Eaton faults are protection trips caused by real electrical or mechanical problems, not bad drives.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
