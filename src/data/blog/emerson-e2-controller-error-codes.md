---
title: "Emerson E2 Refrigeration Controller Error Codes - Complete Guide"
description: "Emerson (Copeland) E2 refrigeration controller error codes and alarms for supermarket and cold storage: causes and fix steps."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - emerson
  - copeland
  - refrigeration
  - e2-controller
money_part: "E2 temperature sensor (NTC)"
---

## Emerson E2 Controller Error Codes - Quick Reference

The Emerson E2 (formerly Alerton, now Emerson Climate Technologies) is a refrigeration and HVAC supervisory controller used in supermarkets, convenience stores, and cold storage. Alarms display on the E2 touchscreen and via the Emerson Store Connect cloud platform.

| Alarm | Device | Meaning | Quick Fix |
|-------|--------|---------|-----------|
| Sensor Failure | Case/Rack | Sensor open, short, or out of range | Check sensor wiring |
| Temperature High | Refrigerated case | Case temp above setpoint | Check defrost, door seals, evap fan |
| Discharge Pressure High | Compressor rack | High head pressure | Check condenser, refrigerant |
| Suction Pressure Low | Rack | Low suction pressure | Check expansion valve, refrigerant |
| Low Superheat | Circuit | Flood-back condition | Check TXV or EEV |
| High Superheat | Circuit | TXV/EEV starving | Check TXV setting or EEV stepper |
| Compressor Fault | Rack | Compressor failure or alarm | Check compressor controller |
| Defrost Fail | Case | Defrost didn't complete | Check defrost heater and termination |
| Communication Fault | I/O board | E2 cannot reach I/O node | Check RS-485 wiring |
| Oil Failure | Compressor | Low oil pressure | Check oil level and crankcase |

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
| E2 temperature sensor (NTC) | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-emerson-e2-controller-error-codes&tag=errorcodefixes-20) \| Replace on sensor failure |
| Defrost heater element | [Amazon](https://www.amazon.com/dp/B07FVP4CY6?ascsubtag=ecf-emerson-e2-controller-error-codes&tag=errorcodefixes-20) \| Replace on defrost fail |
| Defrost termination thermostat | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-emerson-e2-controller-error-codes&tag=errorcodefixes-20) \| Replace on defrost timeout |
| Evaporator fan motor | [Amazon](https://www.amazon.com/dp/B01N0J3ZEH?ascsubtag=ecf-emerson-e2-controller-error-codes&tag=errorcodefixes-20) \| Replace on case temp alarm |
| E2 I/O board | Amazon \| Replace on communication fault |
## When to Call a Pro
Emerson E2 refrigerant circuit diagnostics, EEV calibration, and compressor rack management require EPA Section 608 certification and E2 training. Incorrect setpoint changes can cause food safety violations.

