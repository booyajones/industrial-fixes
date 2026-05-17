---
title: "ABB Tmax/Emax Circuit Breaker Fault Codes - Complete Guide"
description: "ABB Tmax T-series and Emax 2 circuit breaker fault codes, trip indicators, and Ekip trip unit alarms: causes and reset steps."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - abb
  - circuit-breaker
  - electrical
---

## ABB Circuit Breaker Fault Codes - Quick Reference

ABB Tmax (T4, T5, T6, T7) and Emax 2 air circuit breakers use Ekip trip units (G, M, Hi, E series) that display fault history via LED indicators, Ekip Com modules, and the ABB Electrical Systems software.

| Fault / LED | Meaning | Quick Fix |
|------------|---------|-----------|
| LT LED | Long-time overload trip | Check load current, reduce if needed |
| ST LED | Short-time delay trip | Find and clear downstream fault |
| I LED | Instantaneous trip | Inspect load circuit for fault |
| G LED | Ground fault trip | Locate earth fault |
| OT LED | Overtemperature trip | Check breaker cooling and load |
| COM Fault | Ekip Com module communication lost | Check wiring and module |
| Maintenance Required | Trip counter at limit | Inspect breaker contacts |
| Phase Loss | Missing phase detected | Check supply and bus connections |
| Ekip: Test Trip | Manual test result | Reset and close normally |
| ZSI Active | Zone interlock engaged | Check ZSI wiring and downstream breaker |

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
| Ekip trip unit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-circuit-breaker-fault-codes&k=Ekip+trip+unit&tag=errorcodefixes-20) \| Replace on electronics failure |
| Ekip Com module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-circuit-breaker-fault-codes&k=Ekip+Com+module&tag=errorcodefixes-20) \| Replace on communication fault |
| Arc chutes | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-circuit-breaker-fault-codes&k=Arc+chutes&tag=errorcodefixes-20) \| Replace after multiple fault trips |
| Auxiliary contact blocks | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-circuit-breaker-fault-codes&k=Auxiliary+contact+blocks&tag=errorcodefixes-20) \| Replace on worn contacts |
| Undervoltage release (UVR) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-circuit-breaker-fault-codes&k=Undervoltage+release+%28UVR%29&tag=errorcodefixes-20) \| Replace on no-trip-open fault |
## When to Call a Pro
ABB circuit breaker contact inspection and Ekip calibration require qualified electrical personnel. Do not reset after an instantaneous trip without verifying the load circuit is fault-free.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
