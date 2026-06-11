---
title: "Siemens Circuit Breaker Fault Codes - Complete Guide"
description: "Siemens 3WL and 3VA circuit breaker fault codes and ETU trip unit alarms: overload, short circuit, ground fault, causes and fixes."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - siemens
  - circuit-breaker
  - electrical
money_part: "ETU trip unit"
---

## Siemens Circuit Breaker Fault Codes - Quick Reference

Siemens 3WL air circuit breakers and 3VA molded case breakers use ETU (Electronic Trip Unit) 20B, 25B, 45B, and 76B trip units. Faults are shown via LED indicators, ETU displays, and PROFIBUS/Modbus communication.

| Fault / LED | Meaning | Quick Fix |
|------------|---------|-----------|
| OVERLOAD | Long-time overcurrent | Check actual current draw |
| SHORT CIRCUIT | Instantaneous or short-time trip | Inspect load circuit |
| GROUND FAULT | Earth fault detected | Find insulation fault |
| NEUTRAL PROTECT | Neutral overcurrent | Check for harmonics |
| TEST | Manual test trip | Reset and close |
| MAINTENANCE | Inspection interval due | Schedule breaker service |
| COM ERROR | Communication module fault | Check wiring and module |
| ZSI ACTIVE | Zone interlock signal present | Check downstream breakers |
| UVT TRIP | Undervoltage trip on power loss | Normal on power outage |
| ALARM | Pre-trip warning condition | Address before trip occurs |

## Most Common Faults

### Overload Trip
Siemens ETU trip units record the cause of every trip. After reset, press the INFO button (on ETU 45B/76B) to read the last trip cause and fault current. An overload trip means RMS current exceeded the Ir setting for the tr time. Check load current with a clamp meter on all three phases.

### Short Circuit Trip
A Siemens 3WL short circuit trip stores fault current in the trip log. Retrieve this data via Siemens SIMARIS Protect or via Modbus before resetting, then inspect load-side cables, switchgear bus connections, and equipment terminals.

### Ground Fault
ETU 45B and 76B include ground fault protection via a summation CT (3-phase). Trips typically indicate insulation failure on motor windings or cables. Use a 500V or 1000V megohmmeter to test each phase to ground on the load circuit.

### COM Error
3WL COM modules (Modbus RTU, PROFIBUS) fault on cable damage or address conflicts. Verify the RS-485 bus termination at both ends and confirm the breaker address matches the SCADA/BMS configuration.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ETU trip unit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-circuit-breaker-fault-codes&k=ETU+trip+unit&tag=errorcodefixes-20) \| Replace on display or trip failure |
| COM module (Modbus/PROFIBUS) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-circuit-breaker-fault-codes&k=COM+module+%28Modbus%2FPROFIBUS%29&tag=errorcodefixes-20) \| Replace on communication fault |
| Auxiliary switch block | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-circuit-breaker-fault-codes&k=Auxiliary+switch+block&tag=errorcodefixes-20) \| Replace on worn contacts |
| Arc chutes (3WL) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-circuit-breaker-fault-codes&k=Arc+chutes+%283WL%29&tag=errorcodefixes-20) \| Inspect after multiple SC trips |
| Motor drive for 3WL | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-circuit-breaker-fault-codes&k=Motor+drive+for+3WL&tag=errorcodefixes-20) \| Replace on spring charge failure |
## When to Call a Pro
Siemens 3WL maintenance (lubrication, contact inspection, arc chute replacement) requires factory-trained personnel. 3VA trip unit verification should be done with Siemens Sentron software.

## Related Articles

- [Siemens Sinumerik 828D Alarm Codes Guide — Complete Diagnostic Reference](/posts/siemens-828d-alarm-codes/)
- [Siemens 840D Alarm 380000 — Causes & Fix](/posts/siemens-840d-alarm-380000/)
- [Siemens Desigo BMS Fault Codes - Complete Guide](/posts/siemens-desigo-fault-codes/)
- [Siemens Cerberus/MXL Fire Alarm Fault Codes — Troubleshooting Guide](/posts/siemens-fire-alarm-fault-codes/)
- [Siemens G120C VFD Fault Code Guide — Complete Diagnostic Reference](/posts/siemens-g120c-fault-codes/)

## See Also

- [Siemens Sinumerik Alarm 300204 — Causes & Fix](/posts/siemens-sinumerik-alarm-300204/)
- [Siemens SINAMICS V20 F1 Fault — Causes & Fix](/posts/siemens-sinamics-v20-f1-fault/)
- [Siemens VFD F1 Fault (SINAMICS V20 Overcurrent): Causes, Codes, Fix](/posts/siemens-sinamics-v20-f1-overcurrent/)
- [Siemens Sinumerik Alarm 25201 — Causes & Fix](/posts/siemens-sinumerik-alarm-25201/)
