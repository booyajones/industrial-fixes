---
title: "Square D (Schneider) Circuit Breaker Fault Codes - Complete Guide"
description: "Square D (Schneider Electric) Masterpact, Powerpact, and QO circuit breaker fault codes and trip indicators: causes and reset steps."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - square-d
  - schneider
  - circuit-breaker
  - electrical
---

## Square D Circuit Breaker Fault Codes - Quick Reference

Square D (Schneider Electric) Masterpact NT/NW and Powerpact H/J/L frame breakers use Micrologic trip units that display fault codes via LED indicators and the trip cause button. Older QO and QOB residential breakers use a mechanical trip indicator only.

| Fault / LED | Meaning | Quick Fix |
|------------|---------|-----------|
| Trip - Overload (OL) | Long-time overcurrent | Reduce load, reset after cooling |
| Trip - Short Circuit (SC) | Instantaneous fault current | Find and clear fault, inspect breaker |
| Trip - Ground Fault (GF) | Earth fault detected | Locate ground fault, test insulation |
| Trip - Earth Leakage | Micrologic 6/7 - leakage trip | Check for ground faults |
| Trip - Long Time Memory | Accumulated overload | Reduce load |
| ALARM: Overload warning | Load approaching trip threshold | Reduce current draw |
| ALARM: Maintenance | Breaker at contact wear limit | Schedule replacement |
| ALARM: Communication | Micrologic bus fault | Check wiring to building management |
| 50Hz / 60Hz mismatch | Wrong frequency setting | Adjust Micrologic frequency setting |
| Micrologic - No Communication | BSCM module fault | Check module and wiring |

## Most Common Faults

### Overload Trip
An OL trip on a Masterpact means load current exceeded the long-time protection setting (Ir × In) for the required time (tr). Check actual amperage on all three phases with a clamp meter. If all phases are within rated current, check the Ir and tr settings on the Micrologic unit - they may have been set incorrectly.

### Short Circuit Trip
An SC trip is immediate and occurs on fault currents above the magnetic threshold (Im setting). After an SC trip, visually inspect the load-side wiring, the load itself, and the breaker contacts. Do not immediately reset without locating the fault - repeated SC trips damage the breaker arc chutes.

### Ground Fault Trip
Micrologic 5, 6, and 7 trip units include ground fault protection. A GF trip indicates current flowing to ground - typically from insulation failure, a wet connection, or equipment with a shorted winding. Use a megohmmeter to test insulation resistance on connected cables and equipment.

### Maintenance Alarm
Masterpact breakers track contact wear via operating cycles. When the contact wear limit is reached, a maintenance alarm signals that the breaker should be inspected by a qualified electrical technician. Do not continue running without service.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Micrologic trip unit | [Amazon](https://www.amazon.com/s?i=industrial&k=Micrologic+trip+unit&tag=errorcodefixes-20) \| Replacement when electronics fail |
| Arc chutes | [Amazon](https://www.amazon.com/s?i=industrial&k=Arc+chutes&tag=errorcodefixes-20) \| Replace after multiple SC trips |
| BSCM communication module | [Amazon](https://www.amazon.com/s?i=industrial&k=BSCM+communication+module&tag=errorcodefixes-20) \| Replace on communication fault |
| Auxiliary contact blocks | [Amazon](https://www.amazon.com/s?i=industrial&k=Auxiliary+contact+blocks&tag=errorcodefixes-20) \| Replace on worn auxiliary contacts |
| Breaker body (NW/NT) | [Amazon](https://www.amazon.com/s?i=industrial&k=Breaker+body+%28NW%2FNT%29&tag=errorcodefixes-20) \| Replace at end of contact life |
## When to Call a Pro
Circuit breaker maintenance and replacement in 400A–6300A switchgear requires a licensed electrician. Do not reset a breaker after a short circuit trip without inspecting the load circuit thoroughly.

