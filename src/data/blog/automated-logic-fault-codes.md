---
title: "Automated Logic WebCTRL Fault Codes - Complete Guide"
description: "Automated Logic WebCTRL BAS fault codes and alarms for ALC controllers: communication failures, sensor faults, and troubleshooting steps."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - automated-logic
  - webctrl
  - bms
  - building-automation
---

## Automated Logic WebCTRL Fault Codes - Quick Reference

Automated Logic (Carrier subsidiary) WebCTRL uses BACnet controllers (MCB, LGR, VMA, ZN series) and SiteBuilder software. Alarms display in the WebCTRL Alarm Manager and via e-mail/SMS notification.

| [Alarm](https://www.amazon.com/s?k=Alarm&tag=errorcodefixe-20) | Device | Meaning | [Quick Fix](https://www.amazon.com/s?k=Quick%20Fix&tag=errorcodefixe-20) |  |-------|--------|---------|-----------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Controller Offline | MCB/LGR | [Controller not responding](https://www.amazon.com/s?k=Controller%20not%20responding&tag=errorcodefixe-20) | Check power and network |
| [Sensor Out of Range](https://www.amazon.com/s?k=Sensor%20Out%20of%20Range&tag=errorcodefixe-20) | VMA/ZN | Sensor reading exceeds limits | [Check sensor and wiring](https://www.amazon.com/s?k=Check%20sensor%20and%20wiring&tag=errorcodefixe-20) |  | Communication Fault | [All](https://www.amazon.com/s?k=All&tag=errorcodefixe-20) | BACnet communication lost | Check MS/TP or BACnet IP | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Fan Status Alarm | AHU | [Fan command/status mismatch](https://www.amazon.com/s?k=Fan%20command%2Fstatus%20mismatch&tag=errorcodefixe-20) | Check fan and status input |
| [Discharge Air Fault](https://www.amazon.com/s?k=Discharge%20Air%20Fault&tag=errorcodefixe-20) | AHU | Discharge air out of range | [Check coil valves and economizer](https://www.amazon.com/s?k=Check%20coil%20valves%20and%20economizer&tag=errorcodefixe-20) |  | Freeze Alarm | [AHU](https://www.amazon.com/s?k=AHU&tag=errorcodefixe-20) | Low temperature detected | Check heating coil and OA damper | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Override Active | Any | [Manual override in effect](https://www.amazon.com/s?k=Manual%20override%20in%20effect&tag=errorcodefixe-20) | Clear override via WebCTRL |
| [Valve Fault](https://www.amazon.com/s?k=Valve%20Fault&tag=errorcodefixe-20) | AHU | Actuator position fault | [Check actuator wiring](https://www.amazon.com/s?k=Check%20actuator%20wiring&tag=errorcodefixe-20) |  | Occupancy Fault | [Zone](https://www.amazon.com/s?k=Zone&tag=errorcodefixe-20) | Occupancy schedule error | Check schedule configuration | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | WebCTRL Server Fault | Server | [Server application error](https://www.amazon.com/s?k=Server%20application%20error&tag=errorcodefixe-20) | Restart WebCTRL service |

## Most Common Faults

### Controller Offline
An ALC controller going offline in WebCTRL typically indicates a network issue or a power problem. Check that the controller is powered (status LED on), then ping the controller's IP address from the WebCTRL server. BACnet MS/TP trunk faults cause cascading offline alarms for all devices on that trunk.

### Sensor Out of Range
ALC controllers accept UI (universal input) configured as thermistor, 0–10V, 4–20mA, or dry contact. A sensor out of range alarm means the raw input is outside the calibrated range. In SiteBuilder, check the input type configuration matches the physical sensor. A broken thermistor wire reads the same as a short and will be outside range.

### Freeze Alarm
WebCTRL freeze alarms from AHU applications latch and require acknowledgment plus reset at the controller. The freeze strategy (close OA damper, open HW valve, stop fan or not) is configured per-program. After resolving the freeze condition, reset the alarm in WebCTRL and verify the OA damper returned to controlled position.

### WebCTRL Server Fault
WebCTRL runs as a Windows service. If the service crashes or fails to start after an update, check the WebCTRL log files in the install directory. Common causes: Java heap size too small, SQL database connection failure, or a corrupt WebCTRL database. ALC recommends quarterly database backups.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [MCB/LGR controller](https://www.amazon.com/s?k=MCB%2FLGR%20controller&tag=errorcodefixe-20) | Replace on hardware fault |
| [VMA VAV controller](https://www.amazon.com/s?k=VMA%20VAV%20controller&tag=errorcodefixe-20) | Replace on hardware fault |
| [Zone sensor (ZS)](https://www.amazon.com/s?k=Zone%20sensor%20(ZS)&tag=errorcodefixe-20) | Replace on sensor fault |
| [Damper actuator](https://www.amazon.com/s?k=Damper%20actuator&tag=errorcodefixe-20) | Replace on valve/damper fault |
| [WebCTRL server hardware](https://www.amazon.com/s?k=WebCTRL%20server%20hardware&tag=errorcodefixe-20) | Replace on server fault |

## When to Call a Pro
WebCTRL server administration, database management, and BACnet network configuration require Automated Logic-certified technicians. An incorrect network change can disable multiple buildings simultaneously.

