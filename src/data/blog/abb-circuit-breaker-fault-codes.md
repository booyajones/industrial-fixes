---
title: "ABB Tmax/Emax Circuit Breaker Fault Codes - Complete Guide"
description: "ABB Tmax T-series and Emax 2 circuit breaker fault codes, trip indicators, and Ekip trip unit alarms: causes and reset steps."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - abb
  - circuit-breaker
  - electrical
---

## ABB Circuit Breaker Fault Codes - Quick Reference

ABB Tmax (T4, T5, T6, T7) and Emax 2 air circuit breakers use Ekip trip units (G, M, Hi, E series) that display fault history via LED indicators, Ekip Com modules, and the ABB Electrical Systems software.

| [Fault / LED](https://www.amazon.com/s?k=Fault%20%2F%20LED&tag=errorcodefixe-20) | Meaning | Quick Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------------ |---------|-----------|
| LT LED | [Long-time overload trip](https://www.amazon.com/s?k=Long-time%20overload%20trip&tag=errorcodefixe-20) | Check load current, reduce if needed |
| [ST LED](https://www.amazon.com/s?k=ST%20LED&tag=errorcodefixe-20) | Short-time delay trip | Find and clear downstream fault | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | I LED | Instantaneous trip | [Inspect load circuit for fault](https://www.amazon.com/s?k=Inspect%20load%20circuit%20for%20fault&tag=errorcodefixe-20) |  | G LED | [Ground fault trip](https://www.amazon.com/s?k=Ground%20fault%20trip&tag=errorcodefixe-20) | Locate earth fault |
| [OT LED](https://www.amazon.com/s?k=OT%20LED&tag=errorcodefixe-20) | Overtemperature trip | Check breaker cooling and load | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | COM Fault | Ekip Com module communication lost | [Check wiring and module](https://www.amazon.com/s?k=Check%20wiring%20and%20module&tag=errorcodefixe-20) |  | Maintenance Required | [Trip counter at limit](https://www.amazon.com/s?k=Trip%20counter%20at%20limit&tag=errorcodefixe-20) | Inspect breaker contacts |
| [Phase Loss](https://www.amazon.com/s?k=Phase%20Loss&tag=errorcodefixe-20) | Missing phase detected | Check supply and bus connections | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Ekip: Test Trip | Manual test result | [Reset and close normally](https://www.amazon.com/s?k=Reset%20and%20close%20normally&tag=errorcodefixe-20) |  | ZSI Active | [Zone interlock engaged](https://www.amazon.com/s?k=Zone%20interlock%20engaged&tag=errorcodefixe-20) | Check ZSI wiring and downstream breaker |

## Most Common Faults

### Long-Time Overload (LT)
Ekip trip units record fault current and duration. Use the Ekip View software (via USB or Ekip Com) to read the trip log and verify actual fault current. If fault current is below rated load current, check the Ekip LT threshold (Ir) and time settings - factory defaults may not match your installation.

### Instantaneous Trip (I)
ABB Emax 2 instantaneous trips indicate fault current above the Ii threshold, typically a bolted fault or severe cable insulation failure. After the breaker opens, inspect all load-side cables with a megohmmeter before re-energizing.

### Ground Fault (G)
Ekip Hi and E trip units include sensitive ground fault protection. On systems with long cable runs, capacitive leakage current can cause nuisance ground fault trips. Adjust the Ig setting if leakage is confirmed to be capacitive rather than resistive.

### COM Fault
The Ekip Com module provides Modbus, PROFIBUS, or BACnet connectivity. Loss of communication is usually caused by a loose connector, damaged RS-485 cable, or incorrect baud rate/address settings. Check the DIP switches on the Ekip Com module.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Ekip trip unit](https://www.amazon.com/s?k=Ekip%20trip%20unit&tag=errorcodefixe-20) | Replace on electronics failure |
| [Ekip Com module](https://www.amazon.com/s?k=Ekip%20Com%20module&tag=errorcodefixe-20) | Replace on communication fault |
| [Arc chutes](https://www.amazon.com/s?k=Arc%20chutes&tag=errorcodefixe-20) | Replace after multiple fault trips |
| [Auxiliary contact blocks](https://www.amazon.com/s?k=Auxiliary%20contact%20blocks&tag=errorcodefixe-20) | Replace on worn contacts |
| [Undervoltage release (UVR)](https://www.amazon.com/s?k=Undervoltage%20release%20(UVR)&tag=errorcodefixe-20) | Replace on no-trip-open fault |

## When to Call a Pro
ABB circuit breaker contact inspection and Ekip calibration require qualified electrical personnel. Do not reset after an instantaneous trip without verifying the load circuit is fault-free.

