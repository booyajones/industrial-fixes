---
title: "Eaton Circuit Breaker Fault Codes - Complete Guide"
description: "Eaton Magnum DS, PowerDefense, and Cutler-Hammer circuit breaker fault codes and trip indicators: causes and reset procedures."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - eaton
  - circuit-breaker
  - electrical
---

## Eaton Circuit Breaker Fault Codes - Quick Reference

Eaton Magnum DS and PowerDefense (formerly Cutler-Hammer) air circuit breakers use the EATON/Digitrip RMS 810/910 and PowerNet trip units. Faults are shown on LED panels, trip cause indicators, and via PowerNet communication.

| [Fault / Indicator](https://www.amazon.com/s?k=Fault%20%2F%20Indicator&tag=errorcodefixe-20) | Meaning | Quick Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------------------ |---------|-----------|
| Trip - Long Time (LT) | [Sustained overload](https://www.amazon.com/s?k=Sustained%20overload&tag=errorcodefixe-20) | Reduce load, check current |
| [Trip - Short Time (ST)](https://www.amazon.com/s?k=Trip%20-%20Short%20Time%20(ST)&tag=errorcodefixe-20) | Short-circuit delay zone | Locate and clear fault | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Trip - Instantaneous (INST) | High-level fault current | [Inspect load and wiring immediately](https://www.amazon.com/s?k=Inspect%20load%20and%20wiring%20immediately&tag=errorcodefixe-20) |  | Trip - Ground Fault (GF) | [Earth fault (Digitrip 5/8/9)](https://www.amazon.com/s?k=Earth%20fault%20(Digitrip%205%2F8%2F9)&tag=errorcodefixe-20) | Find ground fault source |
| [Trip - Neutral Overcurrent](https://www.amazon.com/s?k=Trip%20-%20Neutral%20Overcurrent&tag=errorcodefixe-20) | Neutral conductor overloaded | Check for harmonics | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | TEST - Trip | Manual trip test result | [Normal - reset and close](https://www.amazon.com/s?k=Normal%20-%20reset%20and%20close&tag=errorcodefixe-20) |  | Zone Selective Interlock | [Downstream breaker tripped](https://www.amazon.com/s?k=Downstream%20breaker%20tripped&tag=errorcodefixe-20) | Find tripped downstream breaker |
| [PowerNet: Comm Fault](https://www.amazon.com/s?k=PowerNet%3A%20Comm%20Fault&tag=errorcodefixe-20) | Network communication lost | Check wiring to PowerNet | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Maintenance Indicator | Inspection interval reached | [Schedule maintenance](https://www.amazon.com/s?k=Schedule%20maintenance&tag=errorcodefixe-20) |  | ALARM - Overload | [Pre-trip warning](https://www.amazon.com/s?k=Pre-trip%20warning&tag=errorcodefixe-20) | Reduce load before trip |

## Most Common Faults

### Long Time Overload Trip
Check actual load current on all three phases. On three-phase systems with high harmonic content (VFD loads, UPS systems), neutral currents can be very high - this can cause long-time trips even when phase currents look normal. Verify Digitrip settings match the conductor and equipment ratings.

### Zone Selective Interlock (ZSI)
Eaton Magnum breakers support ZSI - when a downstream breaker detects a fault, it signals upstream breakers to add a short-time delay, allowing the closest breaker to clear the fault selectively. If ZSI faults are appearing, check the ZSI wiring between breakers and verify ZSI is enabled in all breaker settings.

### Ground Fault Trip
Eaton Digitrip 810/910 ground fault protection trips when ground fault current (measured via a core balance CT or summation of phase currents) exceeds the Ig setting. Check for leakage current paths in the load - especially motors with degraded winding insulation and cables exposed to moisture.

### Instantaneous Trip
An instantaneous (INST) trip on Eaton breakers occurs at 2–10× rated current. This is nearly always a fault in the load circuit. Inspect the load terminals, cables, and equipment before attempting a reset.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Digitrip RMS module](https://www.amazon.com/s?k=Digitrip%20RMS%20module&tag=errorcodefixe-20) | Replace on electronics failure |
| [Arc chutes](https://www.amazon.com/s?k=Arc%20chutes&tag=errorcodefixe-20) | Inspect after fault trips |
| [Auxiliary/alarm contacts](https://www.amazon.com/s?k=Auxiliary%2Falarm%20contacts&tag=errorcodefixe-20) | Replace when worn |
| [PowerNet communication module](https://www.amazon.com/s?k=PowerNet%20communication%20module&tag=errorcodefixe-20) | Replace on comm fault |
| [Spring charging motor](https://www.amazon.com/s?k=Spring%20charging%20motor&tag=errorcodefixe-20) | Replace on slow charge or no-charge |

## When to Call a Pro
Magnum DS maintenance, contact inspection, and trip unit calibration require training. Never reset after an instantaneous trip without an electrician inspecting the load circuit.

