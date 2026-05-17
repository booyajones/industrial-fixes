---
title: "Automated Logic WebCTRL Fault Codes - Complete Guide"
description: "Automated Logic WebCTRL BAS fault codes and alarms for ALC controllers: communication failures, sensor faults, and troubleshooting steps."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "Marcus Webb"
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

| Alarm | Device | Meaning | Quick Fix |
|-------|--------|---------|-----------|
| Controller Offline | MCB/LGR | Controller not responding | Check power and network |
| Sensor Out of Range | VMA/ZN | Sensor reading exceeds limits | Check sensor and wiring |
| Communication Fault | All | BACnet communication lost | Check MS/TP or BACnet IP |
| Fan Status Alarm | AHU | Fan command/status mismatch | Check fan and status input |
| Discharge Air Fault | AHU | Discharge air out of range | Check coil valves and economizer |
| Freeze Alarm | AHU | Low temperature detected | Check heating coil and OA damper |
| Override Active | Any | Manual override in effect | Clear override via WebCTRL |
| Valve Fault | AHU | Actuator position fault | Check actuator wiring |
| Occupancy Fault | Zone | Occupancy schedule error | Check schedule configuration |
| WebCTRL Server Fault | Server | Server application error | Restart WebCTRL service |

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
| MCB/LGR controller | [Amazon](https://www.amazon.com/s?i=industrial&k=MCB%2FLGR+controller&tag=errorcodefixes-20) \| Replace on hardware fault |
| VMA VAV controller | [Amazon](https://www.amazon.com/s?i=industrial&k=VMA+VAV+controller&tag=errorcodefixes-20) \| Replace on hardware fault |
| Zone sensor (ZS) | [Amazon](https://www.amazon.com/s?i=industrial&k=Zone+sensor+%28ZS%29&tag=errorcodefixes-20) \| Replace on sensor fault |
| Damper actuator | [Amazon](https://www.amazon.com/s?i=industrial&k=Damper+actuator&tag=errorcodefixes-20) \| Replace on valve/damper fault |
| WebCTRL server hardware | [Amazon](https://www.amazon.com/s?i=industrial&k=WebCTRL+server+hardware&tag=errorcodefixes-20) \| Replace on server fault |
## When to Call a Pro
WebCTRL server administration, database management, and BACnet network configuration require Automated Logic-certified technicians. An incorrect network change can disable multiple buildings simultaneously.

