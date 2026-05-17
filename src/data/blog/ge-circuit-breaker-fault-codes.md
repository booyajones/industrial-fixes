---
title: "GE Industrial Circuit Breaker Fault Codes - Complete Guide"
description: "GE Industrial (ABB, Grid Solutions) MCCB and power circuit breaker fault codes: DECS trip unit alarms, causes, and reset procedures."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - ge
  - circuit-breaker
  - electrical
---

## GE Circuit Breaker Fault Codes - Quick Reference

GE Industrial circuit breakers (Power/Vac, AKR, SACE PowerBreak II, Spectra RMS) use DECS, DECS-UPM, and M-DECS trip units. GE's power circuit breaker line was acquired by ABB and continues under the ABB/Grid Solutions brand.

| Fault / LED | Meaning | Quick Fix |
|------------|---------|-----------|
| OVERLOAD | Long-time overcurrent | Check load current |
| SHORT CIRCUIT | Fault current above SC threshold | Find and clear fault |
| GROUND FAULT | Earth leakage detected | Check insulation on load |
| PHASE LOSS | Missing phase detected | Check supply connections |
| UNDERVOLTAGE | Supply voltage below minimum | Check supply voltage |
| NEUTRAL OVERCURRENT | Neutral overloaded | Check for 3rd harmonic loads |
| MAINTENANCE | Wear indicator active | Inspect contacts |
| M-DECS Comm Fault | Communication module offline | Check wiring and address |
| TEST Trip | Manual test complete | Reset and re-close |
| ALARM | Pre-trip condition | Investigate before trip occurs |

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
| DECS trip unit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ge-circuit-breaker-fault-codes&k=DECS+trip+unit&tag=errorcodefixes-20) \| Replace on electronics failure |
| Arc chutes (AKR/PowerBreak) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ge-circuit-breaker-fault-codes&k=Arc+chutes+%28AKR%2FPowerBreak%29&tag=errorcodefixes-20) \| Replace after multiple fault trips |
| Auxiliary/alarm contacts | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ge-circuit-breaker-fault-codes&k=Auxiliary%2Falarm+contacts&tag=errorcodefixes-20) \| Replace when worn |
| M-DECS communication module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ge-circuit-breaker-fault-codes&k=M-DECS+communication+module&tag=errorcodefixes-20) \| Replace on comm fault |
| Closing spring/motor mechanism | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ge-circuit-breaker-fault-codes&k=Closing+spring%2Fmotor+mechanism&tag=errorcodefixes-20) \| Replace on charge failure |
## When to Call a Pro
GE/ABB Power circuit breaker maintenance requires factory training. Contact ABB Grid Solutions for authorized service on AKR and PowerBreak II breakers.

