---
title: "Cutler-Hammer (Eaton) Fault Codes — Complete Guide"
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

## Cutler-Hammer Fault Codes — Quick Reference

Cutler-Hammer (branded Eaton since 2004) makes motor starters, combination motor controllers, and circuit breakers. The most common fault diagnostics come from the C441 Motor Insight, C440/E3 Plus electronic overload relays, and Freedom Series contactors.

| Fault | Device | Meaning | Quick Fix |
|-------|--------|---------|-----------|
| OL — Overload | C440/E3 Plus | Motor current exceeded | Check motor amps and load |
| GF — Ground Fault | E3 Plus | Earth fault detected | Check motor insulation |
| PL — Phase Loss | E3 Plus | Missing phase on motor | Check supply and connections |
| PI — Phase Imbalance | E3 Plus | Phase current imbalance | Check supply voltage balance |
| JM — Jam/Stall | E3 Plus | Motor stalled or jammed | Check driven load |
| UL — Underload | E3 Plus | Motor running light | Check driven load coupling |
| Thermistor Trip | E3 Plus | Motor thermistor tripped | Check motor cooling |
| NVR Trip | Starter | No-voltage release — power loss | Normal after power loss |
| Contactor Weld | N/A | Contacts welded closed | Replace contactor |
| Reset Required | C440 | Fault latch — manual reset needed | Identify fault, reset relay |

## Most Common Faults

### Overload (OL) Trip
The C440 and E3 Plus overload relays use true RMS current measurement. An OL trip means motor current exceeded the full load amp (FLA) setting for the trip class time. Verify the relay FLA setting matches the motor nameplate — it's common to find incorrect settings after motor replacements.

### Ground Fault (GF)
E3 Plus ground fault detection uses a core balance CT around all three phases. Any residual current above the GF threshold triggers a trip. Test motor winding insulation with a megohmmeter — values below 1 MΩ to ground indicate insulation failure.

### Phase Loss (PL)
A missing phase on a three-phase motor causes single-phasing, which rapidly overheats the motor windings. C440 relay detects this by monitoring current on all three phases. Check fuses, contactor contacts, and incoming supply for the missing phase.

### Jam/Stall
The E3 Plus Jam function trips when current exceeds a set multiple of FLA for a defined time. This typically indicates a mechanical jam in the driven load — conveyor, pump, fan, or compressor. Investigate the load before restarting.

## Parts Often Needed

| Part | Notes |
|------|-------|
| C440 overload relay | Replace on relay failure |
| Freedom contactor | Replace on welded contacts |
| E3 Plus module | Replace on electronics fault |
| Overload heater elements (older) | Size to motor FLA |
| Contactor coil | Replace on coil open/short |

## When to Call a Pro
Repeated overload trips on a properly-sized motor indicate mechanical or electrical problems with the motor or load. Have a motor shop test winding insulation resistance and bearing condition before assuming the relay is mis-set.
