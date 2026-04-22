---
title: "GE Industrial Circuit Breaker Fault Codes - Complete Guide"
description: "GE Industrial (ABB, Grid Solutions) MCCB and power circuit breaker fault codes: DECS trip unit alarms, causes, and reset procedures."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - ge
  - circuit-breaker
  - electrical
---

## GE Circuit Breaker Fault Codes - Quick Reference

GE Industrial circuit breakers (Power/Vac, AKR, SACE PowerBreak II, Spectra RMS) use DECS, DECS-UPM, and M-DECS trip units. GE's power circuit breaker line was acquired by ABB and continues under the ABB/Grid Solutions brand.

| [Fault / LED](https://www.amazon.com/s?k=Fault%20%2F%20LED&tag=errorcodefixe-20) | Meaning | Quick Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------------ |---------|-----------|
| OVERLOAD | [Long-time overcurrent](https://www.amazon.com/s?k=Long-time%20overcurrent&tag=errorcodefixe-20) | Check load current |
| [SHORT CIRCUIT](https://www.amazon.com/s?k=SHORT%20CIRCUIT&tag=errorcodefixe-20) | Fault current above SC threshold | Find and clear fault | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | GROUND FAULT | Earth leakage detected | [Check insulation on load](https://www.amazon.com/s?k=Check%20insulation%20on%20load&tag=errorcodefixe-20) |  | PHASE LOSS | [Missing phase detected](https://www.amazon.com/s?k=Missing%20phase%20detected&tag=errorcodefixe-20) | Check supply connections |
| [UNDERVOLTAGE](https://www.amazon.com/s?k=UNDERVOLTAGE&tag=errorcodefixe-20) | Supply voltage below minimum | Check supply voltage | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | NEUTRAL OVERCURRENT | Neutral overloaded | [Check for 3rd harmonic loads](https://www.amazon.com/s?k=Check%20for%203rd%20harmonic%20loads&tag=errorcodefixe-20) |  | MAINTENANCE | [Wear indicator active](https://www.amazon.com/s?k=Wear%20indicator%20active&tag=errorcodefixe-20) | Inspect contacts |
| [M-DECS Comm Fault](https://www.amazon.com/s?k=M-DECS%20Comm%20Fault&tag=errorcodefixe-20) | Communication module offline | Check wiring and address | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | TEST Trip | Manual test complete | [Reset and re-close](https://www.amazon.com/s?k=Reset%20and%20re-close&tag=errorcodefixe-20) |  | ALARM | [Pre-trip condition](https://www.amazon.com/s?k=Pre-trip%20condition&tag=errorcodefixe-20) | Investigate before trip occurs |

## Most Common Faults

### Overload Trip (DECS)
GE DECS trip units record last trip information on the LED panel. Press the RECALL button on DECS-UPM to display last trip current on the digital readout. An overload trip on a correctly-set breaker means load has grown - check motor FLA, transformer loading, or added loads.

### Short Circuit Trip
GE PowerBreak and AKR breakers have been extensively used in critical infrastructure. After a short circuit trip, check the arc chutes for damage - repeated SC trips degrade the arc chute inserts. Contact inspection should be done by a GE/ABB-trained technician.

### Ground Fault
DECS ground fault detection on GE breakers uses a summation of phase CT currents. False ground fault trips on long cable runs can be caused by cable capacitance. If nuisance trips occur, raise the Ig threshold after confirming the system is actually free of ground faults.

### Phase Loss
GE DECS breakers with phase loss protection trip immediately on loss of any phase to protect three-phase loads. Check the incoming supply bus and all fused disconnects upstream of the breaker.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [DECS trip unit](https://www.amazon.com/s?k=DECS%20trip%20unit&tag=errorcodefixe-20) | Replace on electronics failure |
| [Arc chutes (AKR/PowerBreak)](https://www.amazon.com/s?k=Arc%20chutes%20(AKR%2FPowerBreak)&tag=errorcodefixe-20) | Replace after multiple fault trips |
| [Auxiliary/alarm contacts](https://www.amazon.com/s?k=Auxiliary%2Falarm%20contacts&tag=errorcodefixe-20) | Replace when worn |
| [M-DECS communication module](https://www.amazon.com/s?k=M-DECS%20communication%20module&tag=errorcodefixe-20) | Replace on comm fault |
| [Closing spring/motor mechanism](https://www.amazon.com/s?k=Closing%20spring%2Fmotor%20mechanism&tag=errorcodefixe-20) | Replace on charge failure |

## When to Call a Pro
GE/ABB Power circuit breaker maintenance requires factory training. Contact ABB Grid Solutions for authorized service on AKR and PowerBreak II breakers.

