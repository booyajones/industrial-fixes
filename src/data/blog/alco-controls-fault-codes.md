---
title: "Alco Controls EXV Fault Codes - Complete Guide"
description: "Alco Controls (Emerson) electronic expansion valve fault codes for EX series controllers: causes and troubleshooting steps."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - alco-controls
  - emerson
  - refrigeration
  - expansion-valve
money_part: "EXV stepper motor coil"
---

## Alco Controls EXV Fault Codes - Quick Reference

Alco Controls (Emerson brand) EX4, EX5, EX6, and EX7 electronic expansion valves with EBC (Electronic Board for Control) and ECB (Electronic Control Board) controllers display faults via LED indicators and alarm outputs.

| Fault / LED | Meaning | Quick Fix |
|------------|---------|-----------|
| Alarm LED - Sensor S1 | Suction temperature sensor fault | Check sensor wiring and resistance |
| Alarm LED - Sensor S2 | Suction pressure sensor fault | Check sensor signal |
| Alarm LED - Valve Open | EXV failed in open position | Check stepper motor and coil |
| Alarm LED - Valve Closed | EXV failed in closed position | Check stepper motor and wiring |
| Low Superheat Alarm | Superheat below setpoint | Check superheat setpoint, refrigerant |
| High Superheat Alarm | Superheat above setpoint | Check TXV setting, refrigerant charge |
| Communication Fault | RS-485 | Network communication lost | Check wiring and address |
| Power Fail | Power | Supply voltage lost | Check 24VAC supply |
| Initialization | Startup | Valve initializing | Wait for completion |
| Manual Override | Any | Manual valve position active | Release override |

## Most Common Faults

### S1 Temperature Sensor Fault
The EBC S1 sensor monitors suction line temperature to calculate superheat. Alco uses NTC thermistors - 10K Ohm at 25°C is common. Disconnect the sensor at the board and measure resistance; compare to the Alco temperature-resistance curve. A reading below 200 Ohms indicates a short; above 100K Ohms indicates an open wire.

### High Superheat
High superheat means the refrigerant is leaving the evaporator too dry. The EXV is not opening enough. Causes: incorrect superheat setpoint, sensor placement too far downstream, refrigerant undercharge, or a failed EXV stepper motor. Check superheat setpoint (typically 5–10°F for refrigeration) and verify the valve responds to a manual open command.

### Valve Stuck Open
An EXV stuck open causes flood-back - liquid refrigerant returning to the compressor, which can cause severe compressor damage. Symptoms include icing on the suction line back to the compressor and abnormally low superheat. Shut down the system and replace the EXV assembly.

### RS-485 Communication Fault
Alco EBC boards communicate via RS-485 Modbus. Faults occur from incorrect address DIP switch settings, missing bus termination, or cable damage. Verify the address matches the controller's database and that the baud rate matches (typically 9600 or 19200 bps).

## Parts Often Needed

| Part | Notes |
|------|-------|
| EXV stepper motor coil | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-alco-controls-fault-codes&k=EXV+stepper+motor+coil&tag=errorcodefixes-20) \| Replace on valve mechanical fault |
| S1 NTC thermistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-alco-controls-fault-codes&k=S1+NTC+thermistor&tag=errorcodefixes-20) \| Replace on sensor fault |
| S2 pressure transducer | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-alco-controls-fault-codes&k=S2+pressure+transducer&tag=errorcodefixes-20) \| Replace on sensor fault |
| EBC controller board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-alco-controls-fault-codes&k=EBC+controller+board&tag=errorcodefixes-20) \| Replace on electronics failure |
| EXV body assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-alco-controls-fault-codes&k=EXV+body+assembly&tag=errorcodefixes-20) \| Replace on stuck valve |
## When to Call a Pro
Alco EXV superheat tuning in refrigeration circuits requires refrigerant certification. Incorrect superheat settings can flood the compressor and cause catastrophic failure.

