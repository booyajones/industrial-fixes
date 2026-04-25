---
title: "VFD Fault Codes: Complete Troubleshooting Guide"
description: "VFD fault codes explained across ABB, Allen-Bradley, Danfoss, Siemens, Yaskawa, and Schneider drives with common alarms and practical fix steps."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - troubleshooting
  - industrial
---

## VFD Fault Codes — What They Mean and How to Fix Them

Most VFD faults fall into a few repeat patterns: too much current, too much voltage, too little voltage, too much heat, or a bad signal from the motor or control system. Once you know the category, you can narrow the cause fast.

| [Fault Family](https://www.amazon.com/s?k=Fault+Family&tag=errorcodefixes-20) | Common Abbreviations | Typical Cause |
|-------------|----------------------|---------------|
| [Overcurrent](https://www.amazon.com/s?k=Overcurrent&tag=errorcodefixes-20) | OC, F001, Fault 7 | Mechanical jam, shorted motor, accel too fast |
| [Overvoltage](https://www.amazon.com/s?k=Overvoltage&tag=errorcodefixes-20) | OV, F003, 3210 | Decel too fast, regenerative load |
| [Undervoltage](https://www.amazon.com/s?k=Undervoltage&tag=errorcodefixes-20) | UV, F004, 3300 | Weak supply, blown fuse, phase loss |
| [Overtemperature](https://www.amazon.com/s?k=Overtemperature&tag=errorcodefixes-20) | OH, oH, 4110 | Dirty fan, blocked airflow, high ambient |
| [Ground Fault](https://www.amazon.com/s?k=Ground+Fault&tag=errorcodefixes-20) | GF | Motor winding or cable insulation failure |
| [Communication Fault](https://www.amazon.com/s?k=Communication+Fault&tag=errorcodefixes-20) | COM, 9300, F81 | PLC or network problem |
| [Overload](https://www.amazon.com/s?k=Overload&tag=errorcodefixes-20) | OL, F012, 5010 | Motor load above rating |

## The 5 Checks That Solve Most VFD Faults

1. Verify incoming three-phase voltage at the drive.
2. Check the motor and cable insulation with a megohm meter.
3. Look for mechanical drag or a locked load.
4. Inspect the drive cooling fan and heatsink for dust.
5. Review accel and decel times before replacing parts.

## Most Common Fault Types

### Overcurrent
The drive tried to push more current than its output stage allows. Start with the mechanical load. A stuck conveyor, seized pump, or locked compressor will trip overcurrent even when the drive is healthy.

### Overvoltage
This shows up during deceleration on high-inertia loads. The motor becomes a generator and pushes energy back into the DC bus. Lengthen the decel ramp or add a brake resistor if the application stops hard.

### Undervoltage
Check the input fuses and the line voltage under load. A loose terminal or weak transformer can look fine with no load and collapse when the motor starts.

### Overtemperature
A dirty drive cabinet causes more VFD faults than most people expect. Clean the fan screens, verify the internal fan runs, and make sure the drive has the clearances listed in the manual.

## Common Brands Covered on This Site

| [Brand](https://www.amazon.com/s?k=Brand&tag=errorcodefixes-20) | Example Guide |
|------|---------------|
| ABB | [ABB VFD Fault Codes](/abb-vfd-fault-codes) |
| [Allen-Bradley](https://www.amazon.com/s?k=Allen-Bradley&tag=errorcodefixes-20) | [Allen-Bradley PowerFlex Fault Codes](/allen-bradley-powerflex-fault-codes) |
| [Danfoss](https://www.amazon.com/s?k=Danfoss&tag=errorcodefixes-20) | [Danfoss VFD Fault Codes](/danfoss-vfd-fault-codes) |
| [Siemens](https://www.amazon.com/s?k=Siemens&tag=errorcodefixes-20) | [Siemens VFD Fault Codes](/siemens-vfd-fault-codes) |
| [Yaskawa](https://www.amazon.com/s?k=Yaskawa&tag=errorcodefixes-20) | [Yaskawa VFD Fault Codes](/yaskawa-vfd-fault-codes) |
| [Eaton](https://www.amazon.com/s?k=Eaton&tag=errorcodefixes-20) | [Eaton VFD Fault Codes](/eaton-vfd-fault-codes) |

## Before You Replace the Drive

- Save or photograph all parameters.
- Check the motor nameplate data programmed into the drive.
- Disconnect the motor and test the drive without load if the manual allows it.
- Inspect for signs of a shorted motor cable before you install a new drive.

## When to Call a Pro
If the drive trips on ground fault, blows input fuses, or shows IGBT or power section errors, stop and test the motor and cable before you restart. A drive shop or field service tech can save you from burning up the replacement drive too.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
