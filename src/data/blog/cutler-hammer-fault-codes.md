---
title: "Cutler-Hammer (Eaton) Fault Codes - Complete Guide"
description: "Cutler-Hammer (Eaton) motor starters, contactors, and circuit breaker fault codes: overload relay trips, fault indicators, and fixes."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - cutler-hammer
  - eaton
  - motor-starter
  - electrical
---

## Cutler-Hammer Fault Codes - Quick Reference

Cutler-Hammer (branded Eaton since 2004) makes motor starters, combination motor controllers, and circuit breakers. The most common fault diagnostics come from the C441 Motor Insight, C440/E3 Plus electronic overload relays, and Freedom Series contactors.

| [Fault](https://www.amazon.com/s?k=Fault&tag=errorcodefixe-20) | Device | Meaning | [Quick Fix](https://www.amazon.com/s?k=Quick%20Fix&tag=errorcodefixe-20) |  |-------|--------|---------|-----------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | OL - Overload | C440/E3 Plus | [Motor current exceeded](https://www.amazon.com/s?k=Motor%20current%20exceeded&tag=errorcodefixe-20) | Check motor amps and load |
| [GF - Ground Fault](https://www.amazon.com/s?k=GF%20-%20Ground%20Fault&tag=errorcodefixe-20) | E3 Plus | Earth fault detected | [Check motor insulation](https://www.amazon.com/s?k=Check%20motor%20insulation&tag=errorcodefixe-20) |  | PL - Phase Loss | [E3 Plus](https://www.amazon.com/s?k=E3%20Plus&tag=errorcodefixe-20) | Missing phase on motor | Check supply and connections | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | PI - Phase Imbalance | E3 Plus | [Phase current imbalance](https://www.amazon.com/s?k=Phase%20current%20imbalance&tag=errorcodefixe-20) | Check supply voltage balance |
| [JM - Jam/Stall](https://www.amazon.com/s?k=JM%20-%20Jam%2FStall&tag=errorcodefixe-20) | E3 Plus | Motor stalled or jammed | [Check driven load](https://www.amazon.com/s?k=Check%20driven%20load&tag=errorcodefixe-20) |  | UL - Underload | [E3 Plus](https://www.amazon.com/s?k=E3%20Plus&tag=errorcodefixe-20) | Motor running light | Check driven load coupling | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Thermistor Trip | E3 Plus | [Motor thermistor tripped](https://www.amazon.com/s?k=Motor%20thermistor%20tripped&tag=errorcodefixe-20) | Check motor cooling |
| [NVR Trip](https://www.amazon.com/s?k=NVR%20Trip&tag=errorcodefixe-20) | Starter | No-voltage release - power loss | [Normal after power loss](https://www.amazon.com/s?k=Normal%20after%20power%20loss&tag=errorcodefixe-20) |  | Contactor Weld | [N/A](https://www.amazon.com/s?k=N%2FA&tag=errorcodefixe-20) | Contacts welded closed | Replace contactor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Reset Required | C440 | [Fault latch - manual reset needed](https://www.amazon.com/s?k=Fault%20latch%20-%20manual%20reset%20needed&tag=errorcodefixe-20) | Identify fault, reset relay |

## Most Common Faults

### Overload (OL) Trip
The C440 and E3 Plus overload relays use true RMS current measurement. An OL trip means motor current exceeded the full load amp (FLA) setting for the trip class time. Verify the relay FLA setting matches the motor nameplate - it's common to find incorrect settings after motor replacements.

### Ground Fault (GF)
E3 Plus ground fault detection uses a core balance CT around all three phases. Any residual current above the GF threshold triggers a trip. Test motor winding insulation with a megohmmeter - values below 1 MΩ to ground indicate insulation failure.

### Phase Loss (PL)
A missing phase on a three-phase motor causes single-phasing, which rapidly overheats the motor windings. C440 relay detects this by monitoring current on all three phases. Check fuses, contactor contacts, and incoming supply for the missing phase.

### Jam/Stall
The E3 Plus Jam function trips when current exceeds a set multiple of FLA for a defined time. This typically indicates a mechanical jam in the driven load - conveyor, pump, fan, or compressor. Investigate the load before restarting.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [C440 overload relay](https://www.amazon.com/s?k=C440%20overload%20relay&tag=errorcodefixe-20) | Replace on relay failure |
| [Freedom contactor](https://www.amazon.com/s?k=Freedom%20contactor&tag=errorcodefixe-20) | Replace on welded contacts |
| [E3 Plus module](https://www.amazon.com/s?k=E3%20Plus%20module&tag=errorcodefixe-20) | Replace on electronics fault |
| [Overload heater elements (older)](https://www.amazon.com/s?k=Overload%20heater%20elements%20(older)&tag=errorcodefixe-20) | Size to motor FLA |
| [Contactor coil](https://www.amazon.com/s?k=Contactor%20coil&tag=errorcodefixe-20) | Replace on coil open/short |

## When to Call a Pro
Repeated overload trips on a properly-sized motor indicate mechanical or electrical problems with the motor or load. Have a motor shop test winding insulation resistance and bearing condition before assuming the relay is mis-set.

