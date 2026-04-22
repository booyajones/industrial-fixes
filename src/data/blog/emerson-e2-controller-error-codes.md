---
title: "Emerson E2 Refrigeration Controller Error Codes - Complete Guide"
description: "Emerson (Copeland) E2 refrigeration controller error codes and alarms for supermarket and cold storage: causes and fix steps."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - emerson
  - copeland
  - refrigeration
  - e2-controller
---

## Emerson E2 Controller Error Codes - Quick Reference

The Emerson E2 (formerly Alerton, now Emerson Climate Technologies) is a refrigeration and HVAC supervisory controller used in supermarkets, convenience stores, and cold storage. Alarms display on the E2 touchscreen and via the Emerson Store Connect cloud platform.

| [Alarm](https://www.amazon.com/s?k=Alarm&tag=errorcodefixe-20) | Device | Meaning | [Quick Fix](https://www.amazon.com/s?k=Quick%20Fix&tag=errorcodefixe-20) |  |-------|--------|---------|-----------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Sensor Failure | Case/Rack | [Sensor open, short, or out of range](https://www.amazon.com/s?k=Sensor%20open%2C%20short%2C%20or%20out%20of%20range&tag=errorcodefixe-20) | Check sensor wiring |
| [Temperature High](https://www.amazon.com/s?k=Temperature%20High&tag=errorcodefixe-20) | Refrigerated case | Case temp above setpoint | [Check defrost, door seals, evap fan](https://www.amazon.com/s?k=Check%20defrost%2C%20door%20seals%2C%20evap%20fan&tag=errorcodefixe-20) |  | Discharge Pressure High | [Compressor rack](https://www.amazon.com/s?k=Compressor%20rack&tag=errorcodefixe-20) | High head pressure | Check condenser, refrigerant | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Suction Pressure Low | Rack | [Low suction pressure](https://www.amazon.com/s?k=Low%20suction%20pressure&tag=errorcodefixe-20) | Check expansion valve, refrigerant |
| [Low Superheat](https://www.amazon.com/s?k=Low%20Superheat&tag=errorcodefixe-20) | Circuit | Flood-back condition | [Check TXV or EEV](https://www.amazon.com/s?k=Check%20TXV%20or%20EEV&tag=errorcodefixe-20) |  | High Superheat | [Circuit](https://www.amazon.com/s?k=Circuit&tag=errorcodefixe-20) | TXV/EEV starving | Check TXV setting or EEV stepper | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Compressor Fault | Rack | [Compressor failure or alarm](https://www.amazon.com/s?k=Compressor%20failure%20or%20alarm&tag=errorcodefixe-20) | Check compressor controller |
| [Defrost Fail](https://www.amazon.com/s?k=Defrost%20Fail&tag=errorcodefixe-20) | Case | Defrost didn't complete | [Check defrost heater and termination](https://www.amazon.com/s?k=Check%20defrost%20heater%20and%20termination&tag=errorcodefixe-20) |  | Communication Fault | [I/O board](https://www.amazon.com/s?k=I%2FO%20board&tag=errorcodefixe-20) | E2 cannot reach I/O node | Check RS-485 wiring | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Oil Failure | Compressor | [Low oil pressure](https://www.amazon.com/s?k=Low%20oil%20pressure&tag=errorcodefixe-20) | Check oil level and crankcase |

## Most Common Faults

### Temperature High Alarm (Case)
Check defrost schedule first - a missed defrost causes ice buildup on the evaporator coil, which blocks airflow and raises case temperature. Also check: door gaskets, evaporator fan motors, and the case curtains overnight. If all defrost cycles are running normally, suspect refrigerant charge or a failed expansion valve.

### Discharge Pressure High
High discharge pressure (head pressure) indicates: dirty or failed condenser coil, failed condenser fan motors, high ambient temperature, or refrigerant overcharge. Check condenser coil cleanliness and fan operation. On air-cooled systems, condenser pressure should be 15–25°F above ambient.

### Sensor Failure
E2 sensors are typically NTC thermistors (10K Ohm at 77°F/25°C). A failed sensor reads as an open circuit (very high resistance) or short circuit (zero resistance). Test the sensor resistance at the E2 I/O board terminal with the sensor wires disconnected. Replace the sensor if resistance is outside the expected curve.

### Defrost Fail
E2 defrost fail alarms occur when a defrost cycle doesn't terminate within the maximum time limit. Causes include: failed defrost termination sensor, failed defrost heater element, or tripped defrost heater safety fuse. Check the termination sensor location and reading in the E2 defrost parameters.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [E2 temperature sensor (NTC)](https://www.amazon.com/s?k=E2%20temperature%20sensor%20(NTC)&tag=errorcodefixe-20) | Replace on sensor failure |
| [Defrost heater element](https://www.amazon.com/s?k=Defrost%20heater%20element&tag=errorcodefixe-20) | Replace on defrost fail |
| [Defrost termination thermostat](https://www.amazon.com/s?k=Defrost%20termination%20thermostat&tag=errorcodefixe-20) | Replace on defrost timeout |
| [Evaporator fan motor](https://www.amazon.com/s?k=Evaporator%20fan%20motor&tag=errorcodefixe-20) | Replace on case temp alarm |
| [E2 I/O board](https://www.amazon.com/s?k=E2%20I%2FO%20board&tag=errorcodefixe-20) | Replace on communication fault |

## When to Call a Pro
Emerson E2 refrigerant circuit diagnostics, EEV calibration, and compressor rack management require EPA Section 608 certification and E2 training. Incorrect setpoint changes can cause food safety violations.

