---
title: "Fuji Frenic-Mini VFD Fault Codes Guide"
description: "Fuji Frenic-Mini VFD fault codes explained. Learn the common overcurrent, overvoltage, undervoltage, ground fault, and memory errors on Fuji drives."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - fuji
  - vfd
  - industrial
  - error-code
---

## Fuji Frenic-Mini Fault Codes

Fuji Frenic-Mini drives are compact and reliable, but their faults still fall into the usual VFD categories: current, voltage, thermal, and memory issues.

## Common Fuji Faults

| [Fault](https://www.amazon.com/s?k=Fault&tag=errorcodefixes-20) | Meaning | Quick Fix |
|---|---|---|
| OC1 | Overcurrent during accel | Increase accel time, check load |
| OC2 | Overcurrent during decel | Increase decel time |
| OC3 | Overcurrent during run | Check motor short or sudden load |
| OU1 | Overvoltage during accel | Check supply and regen |
| OU2 | Overvoltage during decel | Lengthen decel, add braking |
| LU | Undervoltage | Check line sag or loose terminals |
| OH1 | Drive overtemperature | Clean heatsink and fan |
| EF | External trip | Check external fault input |
| Er1 | Memory / keypad fault | Power cycle, inspect control section |

## Practical Troubleshooting

- If faults happen only on stop, focus on decel and regenerated energy.
- If faults happen only on startup, focus on accel time and load binding.
- If LU happens randomly, inspect the incoming power first.

## Bottom Line

Fuji Frenic faults are usually tied to how aggressively the drive is tuned versus the actual machine load. Start with motor data, accel/decel times, and cooling.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
