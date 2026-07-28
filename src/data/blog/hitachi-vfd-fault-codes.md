---
title: "Hitachi WJ200 / WL200 VFD Fault Codes Guide"
description: "Hitachi WJ200 and WL200 VFD fault codes explained. Diagnose overcurrent, ground fault, undervoltage, EEPROM, and overheating trips quickly."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - hitachi
  - vfd
  - industrial
  - error-code
---

## Hitachi WJ200 / WL200 Fault Codes

Hitachi WJ200 and WL200 drives are common on pumps, fans, and light machinery. Their fault list centers on current, voltage, thermal, and memory protection.

## Common Hitachi Faults

| Fault | Meaning | Quick Fix |
|---|---|---|
| E01 | Overcurrent at constant speed | Check load and motor wiring |
| E02 | Overcurrent during decel | Lengthen decel time |
| E03 | Overcurrent during accel | Lengthen accel time |
| E05 | Overload protection | Check motor FLA and load |
| E07 | Overvoltage | Increase decel time |
| E08 | EEPROM/CPU fault | Power cycle, replace drive if persistent |
| E09 | Undervoltage | Check line voltage |
| E12 | External trip | Check fault input terminal |
| E13 | Ground fault | Test motor and leads |
| E14 | Overtemperature | Clean cooling path, check fan |

## Best First Checks

1. Inspect motor leads for insulation damage
2. Verify nameplate motor data entered correctly
3. Check if fault occurs on accel, decel, or run — that narrows the cause fast
4. Clean the heatsink and fan path

## Bottom Line

Hitachi faults usually tell you when in the motion profile the problem occurred. Use that clue — accel faults, decel faults, and run faults point to different fixes.
