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

| [Alarm](https://www.amazon.com/s?k=Alarm&tag=errorcodefixe-20) | Device | Meaning | [Quick Fix](https://www.amazon.com/s?k=Quick%20Fix&tag=errorcodefixe-20) |  |-------|--------|---------|-----------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Communication Failure | UCM/ICS | [BACnet communication lost](https://www.amazon.com/s?k=BACnet%20communication%20lost&tag=errorcodefixe-20) | Check BACnet IP/MS/TP wiring |
| [Outdoor Air Temp Sensor Fault](https://www.amazon.com/s?k=Outdoor%20Air%20Temp%20Sensor%20Fault&tag=errorcodefixe-20) | Tracer SC+ | OAT sensor read error | [Check sensor wiring](https://www.amazon.com/s?k=Check%20sensor%20wiring&tag=errorcodefixe-20) |  | Unit Not Reporting | [All](https://www.amazon.com/s?k=All&tag=errorcodefixe-20) | Equipment offline | Check controller power and network | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Fan Fault | RTU/AHU | [Fan status feedback fault](https://www.amazon.com/s?k=Fan%20status%20feedback%20fault&tag=errorcodefixe-20) | Check VFD and status wiring |
| [High Discharge Temp](https://www.amazon.com/s?k=High%20Discharge%20Temp&tag=errorcodefixe-20) | RTU | Discharge air temperature alarm | [Check cooling and economizer](https://www.amazon.com/s?k=Check%20cooling%20and%20economizer&tag=errorcodefixe-20) |  | Low Leaving Water Temp | [Chiller](https://www.amazon.com/s?k=Chiller&tag=errorcodefixe-20) | Chilled water temp too low | Check chiller setpoints | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Compressor Fault | RTU/Chiller | [Compressor alarm active](https://www.amazon.com/s?k=Compressor%20alarm%20active&tag=errorcodefixe-20) | Check unit controller fault codes |
| [Damper Fault](https://www.amazon.com/s?k=Damper%20Fault&tag=errorcodefixe-20) | AHU | Economizer damper fault | [Check actuator and damper](https://www.amazon.com/s?k=Check%20actuator%20and%20damper&tag=errorcodefixe-20) |  | Override Active | [Any](https://www.amazon.com/s?k=Any&tag=errorcodefixe-20) | Manual override running | Release override via UI | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Database Alarm | Tracer SC+ | [System database error](https://www.amazon.com/s?k=System%20database%20error&tag=errorcodefixe-20) | Check SC+ logs, contact Trane |

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
| [UCM controller](https://www.amazon.com/s?k=UCM%20controller&tag=errorcodefixe-20) | Replace on controller failure |
| [BACnet MS/TP cable](https://www.amazon.com/s?k=BACnet%20MS%2FTP%20cable&tag=errorcodefixe-20) | Replace on communication fault |
| [Tracer SC+ controller](https://www.amazon.com/s?k=Tracer%20SC%2B%20controller&tag=errorcodefixe-20) | Replace on hardware failure |
| [Differential pressure switch (fan)](https://www.amazon.com/s?k=Differential%20pressure%20switch%20(fan)&tag=errorcodefixe-20) | Replace on fan status fault |
| [OAT temperature sensor](https://www.amazon.com/s?k=OAT%20temperature%20sensor&tag=errorcodefixe-20) | Replace on OAT fault |

## When to Call a Pro
Trane Tracer SC+ database configuration, BACnet programming, and UCM commissioning require Trane-trained controls technicians. Contact Trane Service for any Tracer SC+ database corruption or hardware replacement.

