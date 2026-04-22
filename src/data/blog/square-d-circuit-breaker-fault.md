---
title: "Square D (Schneider) Circuit Breaker Fault Codes - Complete Guide"
description: "Square D (Schneider Electric) Masterpact, Powerpact, and QO circuit breaker fault codes and trip indicators: causes and reset steps."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
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

| [Fault / LED](https://www.amazon.com/s?k=Fault%20%2F%20LED&tag=errorcodefixe-20) | Meaning | Quick Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------------ |---------|-----------|
| Trip - Overload (OL) | [Long-time overcurrent](https://www.amazon.com/s?k=Long-time%20overcurrent&tag=errorcodefixe-20) | Reduce load, reset after cooling |
| [Trip - Short Circuit (SC)](https://www.amazon.com/s?k=Trip%20-%20Short%20Circuit%20(SC)&tag=errorcodefixe-20) | Instantaneous fault current | Find and clear fault, inspect breaker | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Trip - Ground Fault (GF) | Earth fault detected | [Locate ground fault, test insulation](https://www.amazon.com/s?k=Locate%20ground%20fault%2C%20test%20insulation&tag=errorcodefixe-20) |  | Trip - Earth Leakage | [Micrologic 6/7 - leakage trip](https://www.amazon.com/s?k=Micrologic%206%2F7%20-%20leakage%20trip&tag=errorcodefixe-20) | Check for ground faults |
| [Trip - Long Time Memory](https://www.amazon.com/s?k=Trip%20-%20Long%20Time%20Memory&tag=errorcodefixe-20) | Accumulated overload | Reduce load | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ALARM: Overload warning | Load approaching trip threshold | [Reduce current draw](https://www.amazon.com/s?k=Reduce%20current%20draw&tag=errorcodefixe-20) |  | ALARM: Maintenance | [Breaker at contact wear limit](https://www.amazon.com/s?k=Breaker%20at%20contact%20wear%20limit&tag=errorcodefixe-20) | Schedule replacement |
| [ALARM: Communication](https://www.amazon.com/s?k=ALARM%3A%20Communication&tag=errorcodefixe-20) | Micrologic bus fault | Check wiring to building management | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 50Hz / 60Hz mismatch | Wrong frequency setting | [Adjust Micrologic frequency setting](https://www.amazon.com/s?k=Adjust%20Micrologic%20frequency%20setting&tag=errorcodefixe-20) |  | Micrologic - No Communication | [BSCM module fault](https://www.amazon.com/s?k=BSCM%20module%20fault&tag=errorcodefixe-20) | Check module and wiring |

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
| [Micrologic trip unit](https://www.amazon.com/s?k=Micrologic%20trip%20unit&tag=errorcodefixe-20) | Replacement when electronics fail |
| [Arc chutes](https://www.amazon.com/s?k=Arc%20chutes&tag=errorcodefixe-20) | Replace after multiple SC trips |
| [BSCM communication module](https://www.amazon.com/s?k=BSCM%20communication%20module&tag=errorcodefixe-20) | Replace on communication fault |
| [Auxiliary contact blocks](https://www.amazon.com/s?k=Auxiliary%20contact%20blocks&tag=errorcodefixe-20) | Replace on worn auxiliary contacts |
| [Breaker body (NW/NT)](https://www.amazon.com/s?k=Breaker%20body%20(NW%2FNT)&tag=errorcodefixe-20) | Replace at end of contact life |

## When to Call a Pro
Circuit breaker maintenance and replacement in 400A–6300A switchgear requires a licensed electrician. Do not reset a breaker after a short circuit trip without inspecting the load circuit thoroughly.

