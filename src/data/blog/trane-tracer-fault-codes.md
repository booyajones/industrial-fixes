---
title: "Trane Tracer BAS Fault Codes - Complete Guide"
description: "Trane Tracer SC+, Tracer ES, and Tracer Summit BAS fault codes and alarms: controller faults, communication errors, and diagnostic steps."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - trane
  - tracer
  - bms
  - building-automation
---

## Trane Tracer BAS Fault Codes - Quick Reference

Trane Tracer SC+ and Tracer ES systems use BACnet/IP for supervisory control of UCM (Unitary Control Module), ICS, Precedent, and Ascend HVAC equipment. Alarms appear in the Tracer graphical interface and via e-mail notifications.

| Alarm | Device | Meaning | Quick Fix |
|-------|--------|---------|-----------|
| Communication Failure | UCM/ICS | BACnet communication lost | Check BACnet IP/MS/TP wiring |
| Outdoor Air Temp Sensor Fault | Tracer SC+ | OAT sensor read error | Check sensor wiring |
| Unit Not Reporting | All | Equipment offline | Check controller power and network |
| Fan Fault | RTU/AHU | Fan status feedback fault | Check VFD and status wiring |
| High Discharge Temp | RTU | Discharge air temperature alarm | Check cooling and economizer |
| Low Leaving Water Temp | Chiller | Chilled water temp too low | Check chiller setpoints |
| Compressor Fault | RTU/Chiller | Compressor alarm active | Check unit controller fault codes |
| Damper Fault | AHU | Economizer damper fault | Check actuator and damper |
| Override Active | Any | Manual override running | Release override via UI |
| Database Alarm | Tracer SC+ | System database error | Check SC+ logs, contact Trane |

## Most Common Faults

### Communication Failure
Tracer SC+ communicates with Trane UCM controllers via BACnet MS/TP on RS-485. A comm failure means the SC+ cannot poll the unit controller. Check the BACnet address on the UCM (set via DIP switches or service tool), verify the baud rate matches (typically 76,800 bps for Trane UCM), and check the RS-485 cable for damage.

### Unit Not Reporting
When a Trane rooftop unit or AHU stops reporting to Tracer, start with physical layer verification - is the unit controller powered? Is the network cable connected? Use the Tracer TU portable service tool to connect directly to the unit and verify it has a valid BACnet network address.

### Fan Fault
Tracer monitors fan feedback via a differential pressure switch or current sensor on the VFD. A fan fault means the controller commanded the fan on but the feedback didn't confirm. Check the fan VFD fault code directly at the drive - VFD faults (overcurrent, overtemperature) prevent the fan from running.

### Compressor Fault
A compressor alarm in Tracer reflects a fault reported by the individual RTU or chiller controller. Navigate to the specific unit in Tracer and read the active diagnostics - Trane RTUs report their own fault codes (flash codes or UCM diagnostics) that will identify the root cause.

## Parts Often Needed

| Part | Notes |
|------|-------|
| UCM controller | [Amazon](https://www.amazon.com/s?k=UCM+controller&tag=errorcodefixes-20) \| Replace on controller failure |
| BACnet MS/TP cable | [Amazon](https://www.amazon.com/s?k=BACnet+MS%2FTP+cable&tag=errorcodefixes-20) \| Replace on communication fault |
| Tracer SC+ controller | [Amazon](https://www.amazon.com/s?k=Tracer+SC%2B+controller&tag=errorcodefixes-20) \| Replace on hardware failure |
| Differential pressure switch (fan) | [Amazon](https://www.amazon.com/s?k=Differential+pressure+switch+%28fan%29&tag=errorcodefixes-20) \| Replace on fan status fault |
| OAT temperature sensor | [Amazon](https://www.amazon.com/s?k=OAT+temperature+sensor&tag=errorcodefixes-20) \| Replace on OAT fault |
## When to Call a Pro
Trane Tracer SC+ database configuration, BACnet programming, and UCM commissioning require Trane-trained controls technicians. Contact Trane Service for any Tracer SC+ database corruption or hardware replacement.

## Related Articles

- [Trane 1 Flash Error Code — Causes & Fix](/posts/trane-1-flash-error-code/)
- [Trane Error Code 126 — Ignition Lockout Fix](/posts/trane-126-error-code/)
- [Trane 2 Flashes Error Code — Causes & Fix](/posts/trane-2-flashes-error-code/)
- [Trane 3 Flashes Error Code — Pressure Switch Fault Fix](/posts/trane-3-flashes-error-code/)
- [Trane 3 Flash Pressure Switch Fault — Detailed Diagnosis Guide](/posts/trane-3-flashes-pressure-switch/)
