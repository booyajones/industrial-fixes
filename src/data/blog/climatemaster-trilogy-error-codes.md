---
title: "ClimateMaster Trilogy Geothermal Error Codes: Complete Guide"
description: "ClimateMaster Trilogy geothermal heat pump error codes. Trilogy Q fault codes, causes, and technician-level troubleshooting procedures."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "Marcus Webb"
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

### FP ΓÇö Freeze Protection
Trilogy units monitor entering water temperature (EWT). FP activates when EWT approaches 32┬░F. Check loop pump, pressure, and antifreeze mix. Propylene glycol mix should be tested annually with a refractometer.

### LO ΓÇö Low-Pressure Fault
Check loop flow first: Trilogy requires 1.5ΓÇô3.0 GPM/ton depending on model. Low refrigerant charge also triggers LO ΓÇö check subcooling and superheat before adding refrigerant.

### HI ΓÇö High-Pressure Fault
On closed-loop systems: EWT above 90┬░F in cooling causes elevated discharge pressures. Check loop sizing and ground loop heat rejection. On water-to-water units: check heat exchanger for scaling.

### FL ΓÇö Flow Fault
ClimateMaster uses a flow switch that opens on low GPM. Verify loop pump operation, check for closed isolation valves, and purge air from system. Measure differential pressure across flow center.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| ClimateTalk thermostat | [Amazon](https://www.amazon.com/s?k=ClimateTalk+thermostat&tag=errorcodefixes-20) \| Required for fault code display |
| Control board | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) \| Match unit model and revision |
| Flow center pump | [Amazon](https://www.amazon.com/s?k=Flow+center+pump&tag=errorcodefixes-20) \| Match GPM requirement |
| TXV | [Amazon](https://www.amazon.com/s?k=TXV&tag=errorcodefixes-20) \| Match refrigerant and model |
| Reversing valve | [Amazon](https://www.amazon.com/s?k=Reversing+valve&tag=errorcodefixes-20) \| Match model spec |
| EWT sensor | [Amazon](https://www.amazon.com/s?k=EWT+sensor&tag=errorcodefixes-20) \| Check resistance vs. temperature |
> **Pro tip:** ClimateMaster Trilogy logs operational data continuously. Use the ClimateTalk thermostat trend screen to review EWT, LWT, refrigerant pressures, and compressor amps over the past 24 hours before diagnosing.
