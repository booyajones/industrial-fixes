---
title: "Siemens Circuit Breaker Fault Codes - Complete Guide"
description: "Siemens 3WL and 3VA circuit breaker fault codes and ETU trip unit alarms: overload, short circuit, ground fault, causes and fixes."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - siemens
  - circuit-breaker
  - electrical
---

## Siemens Circuit Breaker Fault Codes - Quick Reference

Siemens 3WL air circuit breakers and 3VA molded case breakers use ETU (Electronic Trip Unit) 20B, 25B, 45B, and 76B trip units. Faults are shown via LED indicators, ETU displays, and PROFIBUS/Modbus communication.

| [Fault / LED](https://www.amazon.com/s?k=Fault%20%2F%20LED&tag=errorcodefixe-20) | Meaning | Quick Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------------ |---------|-----------|
| OVERLOAD | [Long-time overcurrent](https://www.amazon.com/s?k=Long-time%20overcurrent&tag=errorcodefixe-20) | Check actual current draw |
| [SHORT CIRCUIT](https://www.amazon.com/s?k=SHORT%20CIRCUIT&tag=errorcodefixe-20) | Instantaneous or short-time trip | Inspect load circuit | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | GROUND FAULT | Earth fault detected | [Find insulation fault](https://www.amazon.com/s?k=Find%20insulation%20fault&tag=errorcodefixe-20) |  | NEUTRAL PROTECT | [Neutral overcurrent](https://www.amazon.com/s?k=Neutral%20overcurrent&tag=errorcodefixe-20) | Check for harmonics |
| [TEST](https://www.amazon.com/s?k=TEST&tag=errorcodefixe-20) | Manual test trip | Reset and close | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | MAINTENANCE | Inspection interval due | [Schedule breaker service](https://www.amazon.com/s?k=Schedule%20breaker%20service&tag=errorcodefixe-20) |  | COM ERROR | [Communication module fault](https://www.amazon.com/s?k=Communication%20module%20fault&tag=errorcodefixe-20) | Check wiring and module |
| [ZSI ACTIVE](https://www.amazon.com/s?k=ZSI%20ACTIVE&tag=errorcodefixe-20) | Zone interlock signal present | Check downstream breakers | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | UVT TRIP | Undervoltage trip on power loss | [Normal on power outage](https://www.amazon.com/s?k=Normal%20on%20power%20outage&tag=errorcodefixe-20) |  | ALARM | [Pre-trip warning condition](https://www.amazon.com/s?k=Pre-trip%20warning%20condition&tag=errorcodefixe-20) | Address before trip occurs |

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
| [ETU trip unit](https://www.amazon.com/s?k=ETU%20trip%20unit&tag=errorcodefixe-20) | Replace on display or trip failure |
| [COM module (Modbus/PROFIBUS)](https://www.amazon.com/s?k=COM%20module%20(Modbus%2FPROFIBUS)&tag=errorcodefixe-20) | Replace on communication fault |
| [Auxiliary switch block](https://www.amazon.com/s?k=Auxiliary%20switch%20block&tag=errorcodefixe-20) | Replace on worn contacts |
| [Arc chutes (3WL)](https://www.amazon.com/s?k=Arc%20chutes%20(3WL)&tag=errorcodefixe-20) | Inspect after multiple SC trips |
| [Motor drive for 3WL](https://www.amazon.com/s?k=Motor%20drive%20for%203WL&tag=errorcodefixe-20) | Replace on spring charge failure |

## When to Call a Pro
Siemens 3WL maintenance (lubrication, contact inspection, arc chute replacement) requires factory-trained personnel. 3VA trip unit verification should be done with Siemens Sentron software.

