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

| [Fault](https://www.amazon.com/s?k=Fault&tag=errorcodefixe-20) | System | Meaning | [Quick Fix](https://www.amazon.com/s?k=Quick%20Fix&tag=errorcodefixe-20) |  |-------|--------|---------|-----------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Battery Fault | 9PX/9SX | [Battery test failed or battery open](https://www.amazon.com/s?k=Battery%20test%20failed%20or%20battery%20open&tag=errorcodefixe-20) | Replace battery |
| [Overload](https://www.amazon.com/s?k=Overload&tag=errorcodefixe-20) | All | Load exceeds UPS rating | [Reduce connected load](https://www.amazon.com/s?k=Reduce%20connected%20load&tag=errorcodefixe-20) |  | On Battery | [All](https://www.amazon.com/s?k=All&tag=errorcodefixe-20) | Utility power lost | Check power input | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Replace Battery | 5PX/9PX | [End of battery life](https://www.amazon.com/s?k=End%20of%20battery%20life&tag=errorcodefixe-20) | Replace battery |
| [Bypass Active](https://www.amazon.com/s?k=Bypass%20Active&tag=errorcodefixe-20) | 9PX/9SX | UPS in bypass - not protecting | [Check for UPS fault](https://www.amazon.com/s?k=Check%20for%20UPS%20fault&tag=errorcodefixe-20) |  | Output Fault | [9395](https://www.amazon.com/s?k=9395&tag=errorcodefixe-20) | Output voltage out of range | Check load, call service | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Fan Fault | 9395/BladeUPS | [Cooling fan failed](https://www.amazon.com/s?k=Cooling%20fan%20failed&tag=errorcodefixe-20) | Replace fan module |
| [Communication Fault](https://www.amazon.com/s?k=Communication%20Fault&tag=errorcodefixe-20) | All | Network card or serial fault | [Check network card](https://www.amazon.com/s?k=Check%20network%20card&tag=errorcodefixe-20) |  | Input Fault | [All](https://www.amazon.com/s?k=All&tag=errorcodefixe-20) | Input voltage out of range | Check utility supply | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Battery Low | All | [Runtime remaining below threshold](https://www.amazon.com/s?k=Runtime%20remaining%20below%20threshold&tag=errorcodefixe-20) | Connect to power or reduce load |

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
| [Internal battery module](https://www.amazon.com/s?k=Internal%20battery%20module&tag=errorcodefixe-20) | Size to UPS model |
| [External battery module (EBM)](https://www.amazon.com/s?k=External%20battery%20module%20(EBM)&tag=errorcodefixe-20) | For extended runtime systems |
| [Network management card](https://www.amazon.com/s?k=Network%20management%20card&tag=errorcodefixe-20) | Replace on communication fault |
| [Fan tray / fan module](https://www.amazon.com/s?k=Fan%20tray%20%2F%20fan%20module&tag=errorcodefixe-20) | Replace on fan fault |
| [Static bypass assembly](https://www.amazon.com/s?k=Static%20bypass%20assembly&tag=errorcodefixe-20) | Replace on switching fault |

## When to Call a Pro
Eaton 9395 and 9XXX three-phase systems require trained service personnel for internal work. Capacitor replacement, transformer inspection, and rectifier/inverter service must be done by Eaton-authorized technicians.

