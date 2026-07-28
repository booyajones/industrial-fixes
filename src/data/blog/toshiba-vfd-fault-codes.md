---
title: "Toshiba VFD Fault Codes Guide (VF-S15, VF-S9)"
description: "Toshiba VF-S15 and VF-S9 VFD fault codes explained, including overcurrent, overvoltage, overheating, and EEPROM faults."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - toshiba
  - vfd
  - industrial
  - error-code
---

## Toshiba VFD Fault Codes

Toshiba VF-S15 and VF-S9 drives use compact fault labels that cover motor overload, DC bus faults, overheating, and memory errors.

## Common Toshiba Faults

| Fault | Meaning | Quick Fix |
|---|---|---|
| OC | Overcurrent | Check motor/cable short, jammed load |
| OV | Overvoltage | Increase decel, check braking setup |
| OH | Heatsink overtemperature | Clean drive, verify cooling fan |
| OL1 | Motor overload | Check motor FLA setting |
| OL2 | Drive overload | Reduce load, check sizing |
| LU | Undervoltage | Check input supply and loose terminals |
| EF | External fault input | Check interlock wired to fault terminal |
| CPF | CPU/EEPROM fault | Power cycle, replace drive if persistent |

## Key Troubleshooting Notes

- **LU** faults often come from weak plant power or loose line terminals.
- **CPF** faults can happen after surges or aging electronics.
- **OL1** and **OL2** often point to bad parameter setup, not just a heavy load.

## Bottom Line

Toshiba faults are usually straightforward. Check supply voltage, motor current settings, decel time, and cooling before condemning the drive.
