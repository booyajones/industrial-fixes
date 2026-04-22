---
title: "Alco Controls EXV Fault Codes - Complete Guide"
description: "Alco Controls (Emerson) electronic expansion valve fault codes for EX series controllers: causes and troubleshooting steps."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - alco-controls
  - emerson
  - refrigeration
  - expansion-valve
---

## Alco Controls EXV Fault Codes - Quick Reference

Alco Controls (Emerson brand) EX4, EX5, EX6, and EX7 electronic expansion valves with EBC (Electronic Board for Control) and ECB (Electronic Control Board) controllers display faults via LED indicators and alarm outputs.

| [Fault / LED](https://www.amazon.com/s?k=Fault%20%2F%20LED&tag=errorcodefixe-20) | Meaning | Quick Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------------ |---------|-----------|
| Alarm LED - Sensor S1 | [Suction temperature sensor fault](https://www.amazon.com/s?k=Suction%20temperature%20sensor%20fault&tag=errorcodefixe-20) | Check sensor wiring and resistance |
| [Alarm LED - Sensor S2](https://www.amazon.com/s?k=Alarm%20LED%20-%20Sensor%20S2&tag=errorcodefixe-20) | Suction pressure sensor fault | Check sensor signal | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Alarm LED - Valve Open | EXV failed in open position | [Check stepper motor and coil](https://www.amazon.com/s?k=Check%20stepper%20motor%20and%20coil&tag=errorcodefixe-20) |  | Alarm LED - Valve Closed | [EXV failed in closed position](https://www.amazon.com/s?k=EXV%20failed%20in%20closed%20position&tag=errorcodefixe-20) | Check stepper motor and wiring |
| [Low Superheat Alarm](https://www.amazon.com/s?k=Low%20Superheat%20Alarm&tag=errorcodefixe-20) | Superheat below setpoint | Check superheat setpoint, refrigerant | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | High Superheat Alarm | Superheat above setpoint | [Check TXV setting, refrigerant charge](https://www.amazon.com/s?k=Check%20TXV%20setting%2C%20refrigerant%20charge&tag=errorcodefixe-20) |  | Communication Fault | [RS-485](https://www.amazon.com/s?k=RS-485&tag=errorcodefixe-20) | Network communication lost | Check wiring and address | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Power Fail | Power | [Supply voltage lost](https://www.amazon.com/s?k=Supply%20voltage%20lost&tag=errorcodefixe-20) | Check 24VAC supply |
| [Initialization](https://www.amazon.com/s?k=Initialization&tag=errorcodefixe-20) | Startup | Valve initializing | [Wait for completion](https://www.amazon.com/s?k=Wait%20for%20completion&tag=errorcodefixe-20) |  | Manual Override | [Any](https://www.amazon.com/s?k=Any&tag=errorcodefixe-20) | Manual valve position active | Release override | [## Most Common Faults

### S1 Temperature Sensor Fault
The EBC S1 sensor monitors suction line temperature to calculate superheat. Alco uses NTC thermistors - 10K Ohm at 25°C is common. Disconnect the sensor at the board and measure resistance; compare to the Alco temperature-resistance curve. A reading below 200 Ohms indicates a short; above 100K Ohms indicates an open wire.

### High Superheat
High superheat means the refrigerant is leaving the evaporator too dry. The EXV is not opening enough. Causes: incorrect superheat setpoint, sensor placement too far downstream, refrigerant undercharge, or a failed EXV stepper motor. Check superheat setpoint (typically 5–10°F for refrigeration) and verify the valve responds to a manual open command.

### Valve Stuck Open
An EXV stuck open causes flood-back - liquid refrigerant returning to the compressor, which can cause severe compressor damage. Symptoms include icing on the suction line back to the compressor and abnormally low superheat. Shut down the system and replace the EXV assembly.

### RS-485 Communication Fault
Alco EBC boards communicate via RS-485 Modbus. Faults occur from incorrect address DIP switch settings, missing bus termination, or cable damage. Verify the address matches the controller's database and that the baud rate matches (typically 9600 or 19200 bps).

## Parts Often Needed](https://www.amazon.com/s?k=%23%23%20Most%20Common%20Faults%0A%0A%23%23%23%20S1%20Temperature%20Sensor%20Fault%0AThe%20EBC%20S1%20sensor%20monitors%20suction%20line%20temperature%20to%20calculate%20superheat.%20Alco%20uses%20NTC%20thermistors%20-%2010K%20Ohm%20at%2025%C2%B0C%20is%20common.%20Disconnect%20the%20sensor%20at%20the%20board%20and%20measure%20resistance%3B%20compare%20to%20the%20Alco%20temperature-resistance%20curve.%20A%20reading%20below%20200%20Ohms%20indicates%20a%20short%3B%20above%20100K%20Ohms%20indicates%20an%20open%20wire.%0A%0A%23%23%23%20High%20Superheat%0AHigh%20superheat%20means%20the%20refrigerant%20is%20leaving%20the%20evaporator%20too%20dry.%20The%20EXV%20is%20not%20opening%20enough.%20Causes%3A%20incorrect%20superheat%20setpoint%2C%20sensor%20placement%20too%20far%20downstream%2C%20refrigerant%20undercharge%2C%20or%20a%20failed%20EXV%20stepper%20motor.%20Check%20superheat%20setpoint%20(typically%205%E2%80%9310%C2%B0F%20for%20refrigeration)%20and%20verify%20the%20valve%20responds%20to%20a%20manual%20open%20command.%0A%0A%23%23%23%20Valve%20Stuck%20Open%0AAn%20EXV%20stuck%20open%20causes%20flood-back%20-%20liquid%20refrigerant%20returning%20to%20the%20compressor%2C%20which%20can%20cause%20severe%20compressor%20damage.%20Symptoms%20include%20icing%20on%20the%20suction%20line%20back%20to%20the%20compressor%20and%20abnormally%20low%20superheat.%20Shut%20down%20the%20system%20and%20replace%20the%20EXV%20assembly.%0A%0A%23%23%23%20RS-485%20Communication%20Fault%0AAlco%20EBC%20boards%20communicate%20via%20RS-485%20Modbus.%20Faults%20occur%20from%20incorrect%20address%20DIP%20switch%20settings%2C%20missing%20bus%20termination%2C%20or%20cable%20damage.%20Verify%20the%20address%20matches%20the%20controller's%20database%20and%20that%20the%20baud%20rate%20matches%20(typically%209600%20or%2019200%20bps).%0A%0A%23%23%20Parts%20Often%20Needed&tag=errorcodefixe-20) | Part | Notes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |-------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | EXV stepper motor coil | Replace on valve mechanical fault | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | S1 NTC thermistor | Replace on sensor fault | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | S2 pressure transducer | Replace on sensor fault | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | EBC controller board | Replace on electronics failure | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | EXV body assembly | Replace on stuck valve |

## When to Call a Pro
Alco EXV superheat tuning in refrigeration circuits requires refrigerant certification. Incorrect superheat settings can flood the compressor and cause catastrophic failure.

