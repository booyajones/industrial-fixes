---
title: "Eaton Circuit Breaker Fault Codes — Complete Guide"
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

## Eaton Circuit Breaker Fault Codes — Quick Reference

Eaton Magnum DS and PowerDefense (formerly Cutler-Hammer) air circuit breakers use the EATON/Digitrip RMS 810/910 and PowerNet trip units. Faults are shown on LED panels, trip cause indicators, and via PowerNet communication.

| Fault / Indicator | Meaning | Quick Fix |
|------------------|---------|-----------|
| Trip — Long Time (LT) | Sustained overload | Reduce load, check current |
| Trip — Short Time (ST) | Short-circuit delay zone | Locate and clear fault |
| Trip — Instantaneous (INST) | High-level fault current | Inspect load and wiring immediately |
| Trip — Ground Fault (GF) | Earth fault (Digitrip 5/8/9) | Find ground fault source |
| Trip — Neutral Overcurrent | Neutral conductor overloaded | Check for harmonics |
| TEST — Trip | Manual trip test result | Normal — reset and close |
| Zone Selective Interlock | Downstream breaker tripped | Find tripped downstream breaker |
| PowerNet: Comm Fault | Network communication lost | Check wiring to PowerNet |
| Maintenance Indicator | Inspection interval reached | Schedule maintenance |
| ALARM — Overload | Pre-trip warning | Reduce load before trip |

## Most Common Faults

### Long Time Overload Trip
Check actual load current on all three phases. On three-phase systems with high harmonic content (VFD loads, UPS systems), neutral currents can be very high — this can cause long-time trips even when phase currents look normal. Verify Digitrip settings match the conductor and equipment ratings.

### Zone Selective Interlock (ZSI)
Eaton Magnum breakers support ZSI — when a downstream breaker detects a fault, it signals upstream breakers to add a short-time delay, allowing the closest breaker to clear the fault selectively. If ZSI faults are appearing, check the ZSI wiring between breakers and verify ZSI is enabled in all breaker settings.

### Ground Fault Trip
Eaton Digitrip 810/910 ground fault protection trips when ground fault current (measured via a core balance CT or summation of phase currents) exceeds the Ig setting. Check for leakage current paths in the load — especially motors with degraded winding insulation and cables exposed to moisture.

### Instantaneous Trip
An instantaneous (INST) trip on Eaton breakers occurs at 2–10× rated current. This is nearly always a fault in the load circuit. Inspect the load terminals, cables, and equipment before attempting a reset.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Digitrip RMS module | Replace on electronics failure |
| Arc chutes | Inspect after fault trips |
| Auxiliary/alarm contacts | Replace when worn |
| PowerNet communication module | Replace on comm fault |
| Spring charging motor | Replace on slow charge or no-charge |

## When to Call a Pro
Magnum DS maintenance, contact inspection, and trip unit calibration require training. Never reset after an instantaneous trip without an electrician inspecting the load circuit.
