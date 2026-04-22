---
title: "ClimateMaster Trilogy Geothermal Error Codes: Complete Guide"
description: "ClimateMaster Trilogy geothermal heat pump error codes. Trilogy Q fault codes, causes, and technician-level troubleshooting procedures."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - climatemaster
  - geothermal
  - heat-pump
---

# ClimateMaster Trilogy Geothermal Error Codes

ClimateMaster Trilogy Q units use the ClimateTalk communicating system with a color touchscreen thermostat for diagnostics. Fault codes display directly on the Trilogy thermostat. Non-communicating installations use LED flash codes on the control board.

## Trilogy Fault Code Table

| Code | Fault Description | Common Cause | Severity |
|------|------------------|--------------|---------|
| LO | Low-pressure fault | Low charge, low loop flow | Lockout |
| HI | High-pressure fault | Dirty coil, high EWT, overcharge | Lockout |
| FP | Freeze protection | Low EWT or low refrigerant | Lockout |
| CO | High discharge temp | Refrigerant problem | Lockout |
| OA | Over-amperage | Compressor overloading | Lockout |
| CC | Contactor check | Contactor failure | Lockout |
| EE | EEPROM error | Control board corruption | Lockout |
| FL | Flow fault | Low loop GPM | Warning |
| ST | Sensor fault | Temperature sensor failure | Warning |
| RS | Reversing valve stuck | RV or solenoid failure | Lockout |
| CM | Communication fault | ClimateTalk wiring | Warning |

## Most Common Trilogy Faults

### FP — Freeze Protection
Trilogy units monitor entering water temperature (EWT). FP activates when EWT approaches 32°F. Check loop pump, pressure, and antifreeze mix. Propylene glycol mix should be tested annually with a refractometer.

### LO — Low-Pressure Fault
Check loop flow first: Trilogy requires 1.5–3.0 GPM/ton depending on model. Low refrigerant charge also triggers LO — check subcooling and superheat before adding refrigerant.

### HI — High-Pressure Fault
On closed-loop systems: EWT above 90°F in cooling causes elevated discharge pressures. Check loop sizing and ground loop heat rejection. On water-to-water units: check heat exchanger for scaling.

### FL — Flow Fault
ClimateMaster uses a flow switch that opens on low GPM. Verify loop pump operation, check for closed isolation valves, and purge air from system. Measure differential pressure across flow center.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| ClimateTalk thermostat | Required for fault code display |
| Control board | Match unit model and revision |
| Flow center pump | Match GPM requirement |
| TXV | Match refrigerant and model |
| Reversing valve | Match model spec |
| EWT sensor | Check resistance vs. temperature |

> **Pro tip:** ClimateMaster Trilogy logs operational data continuously. Use the ClimateTalk thermostat trend screen to review EWT, LWT, refrigerant pressures, and compressor amps over the past 24 hours before diagnosing.
