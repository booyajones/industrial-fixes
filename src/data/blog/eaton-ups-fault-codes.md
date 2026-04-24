---
title: "Eaton UPS Fault Codes - Complete Guide"
description: "Eaton UPS fault codes for 9PX, 9SX, 9E, BladeUPS, and 9395 systems: LED indicators, alarms, causes, and troubleshooting steps."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - eaton
  - ups
  - power-systems
---

## Eaton UPS Fault Codes - Quick Reference

Eaton UPS systems (9PX, 9SX, 9E, 5PX, BladeUPS, and 9395 three-phase) communicate faults via LCD panels, LED indicators, alarm buzzers, and via Eaton Intelligent Power Manager (IPM) or network cards.

| Fault | System | Meaning | Quick Fix |
|-------|--------|---------|-----------|
| Battery Fault | 9PX/9SX | Battery test failed or battery open | Replace battery |
| Overload | All | Load exceeds UPS rating | Reduce connected load |
| On Battery | All | Utility power lost | Check power input |
| Replace Battery | 5PX/9PX | End of battery life | Replace battery |
| Bypass Active | 9PX/9SX | UPS in bypass - not protecting | Check for UPS fault |
| Output Fault | 9395 | Output voltage out of range | Check load, call service |
| Fan Fault | 9395/BladeUPS | Cooling fan failed | Replace fan module |
| Communication Fault | All | Network card or serial fault | Check network card |
| Input Fault | All | Input voltage out of range | Check utility supply |
| Battery Low | All | Runtime remaining below threshold | Connect to power or reduce load |

## Most Common Faults

### Battery Fault / Replace Battery
Eaton 9PX and 9SX batteries self-test on startup and periodically during operation. A battery fault means the battery cannot deliver rated voltage under load. Check battery connections first - loose or corroded terminals cause false battery faults. If connections are good, replace the battery module. Eaton EBMs (External Battery Modules) also report faults if disconnected or failed.

### Overload
Eaton 9PX and 9SX display overload as a percentage on the LCD. Reduce load until the overload alarm clears. If the UPS trips to bypass on overload, the load is being supplied unprotected - identify and remove the offending load quickly.

### Bypass Active
When an Eaton UPS transfers to static bypass, load is connected directly to utility with no power conditioning or battery backup. Bypass occurs during UPS faults, overtemperature, or when maintenance bypass is manually selected. Investigate the underlying fault that caused the bypass transfer.

### Fan Fault (9395 / BladeUPS)
Three-phase Eaton systems monitor individual cooling fans. A failed fan causes derating or a fault alarm. Eaton 9395 fan trays are field-replaceable - check the part number on the fan tray label and order directly from Eaton.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Internal battery module | [Amazon](https://www.amazon.com/s?k=Internal+battery+module&tag=errorcodefixes-20) \| Size to UPS model |
| External battery module (EBM) | [Amazon](https://www.amazon.com/s?k=External+battery+module+%28EBM%29&tag=errorcodefixes-20) \| For extended runtime systems |
| Network management card | [Amazon](https://www.amazon.com/s?k=Network+management+card&tag=errorcodefixes-20) \| Replace on communication fault |
| Fan tray / fan module | [Amazon](https://www.amazon.com/s?k=Fan+tray+%2F+fan+module&tag=errorcodefixes-20) \| Replace on fan fault |
| Static bypass assembly | [Amazon](https://www.amazon.com/s?k=Static+bypass+assembly&tag=errorcodefixes-20) \| Replace on switching fault |
## When to Call a Pro
Eaton 9395 and 9XXX three-phase systems require trained service personnel for internal work. Capacitor replacement, transformer inspection, and rectifier/inverter service must be done by Eaton-authorized technicians.

