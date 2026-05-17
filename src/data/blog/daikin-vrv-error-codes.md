---
title: "Daikin VRV System Error Codes: Complete Guide"
description: "Complete guide to Daikin VRV (Variable Refrigerant Volume) system error codes. Covers U, E, A, C, F, and H-series codes with causes and technician fixes."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - daikin
  - vrv
  - vrf
  - commercial-hvac
---

# Daikin VRV System Error Codes: Complete Guide

Daikin VRV (Variable Refrigerant Volume) systems are commercial multi-split systems that use alphanumeric fault codes displayed on the outdoor unit LED panel, indoor unit wired remotes, and the Daikin Intelligent Touch Controller (ITC). This guide covers all major Daikin VRV error codes.

## How to Read Daikin VRV Codes

Daikin VRV fault codes are displayed as two characters:
- **Letter prefix** identifies the fault category
- **Number suffix** identifies the specific fault

Codes appear on:
- The outdoor unit 7-segment LED display
- Wired remote controller (BRC1 series)
- Intelligent Touch Controller (ITC)
- DIII-NET building automation connection

## Daikin VRV Error Code Table

### U-Codes — System/Communication Faults

| [Code](https://www.amazon.com/s?i=industrial&k=Code&tag=errorcodefixes-20) | Description | Common Cause |
|---|---|---|
| U0 | Refrigerant shortage | Low refrigerant — leak in system |
| U1 | Reverse phase / phase loss | Check 3-phase power supply |
| U2 | Low voltage or power failure | Check supply voltage and circuit |
| U3 | Transmission fault — indoor/outdoor | Check DIII-NET wiring |
| U4 | Transmission fault — outdoor/indoor | Communication wiring issue |
| U5 | Abnormal signal — indoor unit | Wiring or indoor board fault |
| U7 | Transmission fault — BS unit | BS branch selector wiring |
| U9 | Abnormal power supply phase | Phase imbalance or loss |
| UA | Indoor unit combination error | Unit count or type mismatch |
| UE | Communication error — outdoor to controller | Check DIII-NET wiring |
| UH | Communication error — indoor units | Check F1/F2 wiring at each indoor unit |

### E-Codes — Heat Exchanger / Sensor Faults

| [Code](https://www.amazon.com/s?i=industrial&k=Code&tag=errorcodefixes-20) | Description | Common Cause |
|---|---|---|
| E1 | Outdoor unit PCB fault | Replace outdoor unit control board |
| E3 | High-pressure lockout | Dirty coil, low airflow, overcharge |
| E4 | Low-pressure lockout | Low refrigerant, low airflow |
| E5 | Inverter compressor overheat | Airflow to inverter section blocked |
| E6 | Compressor motor overload | Check compressor amps |
| E7 | Fan motor fault | Fan motor or inverter board |
| E9 | Electronic expansion valve fault | EEV or wiring |

### A-Codes — Indoor Unit Faults

| [Code](https://www.amazon.com/s?i=industrial&k=Code&tag=errorcodefixes-20) | Description | Common Cause |
|---|---|---|
| A0 | Protection device fault | Indoor unit safety device tripped |
| A1 | Indoor unit PCB fault | Replace indoor control board |
| A3 | Drain level fault | Blocked drain, failed condensate pump |
| A5 | Freeze protection | Low refrigerant, dirty filter |
| A6 | Fan motor fault — indoor | Indoor fan motor or capacitor |
| A9 | Electronic expansion valve fault | EEV coil or position fault |

### C-Codes — Sensor Faults

| [Code](https://www.amazon.com/s?i=industrial&k=Code&tag=errorcodefixes-20) | Description | Common Cause |
|---|---|---|
| C4 | Heat exchanger sensor fault | Outdoor liquid coil sensor |
| C5 | Subcooling coil sensor fault | Check sensor resistance |
| C9 | Discharge temperature sensor fault | Compressor discharge sensor |

### F-Codes — System Protection

| [Code](https://www.amazon.com/s?i=industrial&k=Code&tag=errorcodefixes-20) | Description | Common Cause |
|---|---|---|
| F3 | Discharge temperature too high | Low refrigerant, TXV issue |
| F6 | High-pressure control fault | Pressure protection activated |

## Most Common Daikin VRV Faults

### U4 — Transmission Fault (Most Common)
The #1 VRV service call:
1. Check F1/F2 wiring at every indoor unit — loose connection is common
2. Verify polarity is consistent throughout the system
3. Check DIII-NET address settings — duplicate addresses cause U4
4. Check for damaged wiring in long runs

### E3 — High Pressure Lockout
1. Check condenser coil condition (clean if dirty)
2. Verify all condenser fans are operating
3. Check refrigerant charge — calculate subcooling
4. Check for non-condensables if system was open

### A3 — Drain Level Fault
Check float switch in the condensate pan, condensate line for blockage, and condensate pump operation.

### U0 — Refrigerant Shortage
Daikin VRV systems contain large refrigerant charges. U0 means the system has lost enough refrigerant to affect operation. Perform a full leak check before recharging.

## Daikin VRV Parts Reference

| Part | Notes |
|---|---|
| [EEV (electronic expansion valve)](https://www.amazon.com/s?i=industrial&k=EEV+%28electronic+expansion+valve%29&tag=errorcodefixes-20) | Model-specific — match kv value |
| [Outdoor unit PCB](https://www.amazon.com/s?i=industrial&k=Outdoor+unit+PCB&tag=errorcodefixes-20) | Match model and firmware version |
| [Indoor unit PCB](https://www.amazon.com/s?i=industrial&k=Indoor+unit+PCB&tag=errorcodefixes-20) | Specific to indoor unit model |
| [F1/F2 communication wire](https://www.amazon.com/s?i=industrial&k=F1%2FF2+communication+wire&tag=errorcodefixes-20) | 2-conductor unshielded, max 1000m |
| [DIII-NET adapter](https://www.amazon.com/s?i=industrial&k=DIII-NET+adapter&tag=errorcodefixes-20) | For BAS integration |

> **Pro tip:** Daikin VRV systems support fault history via the ITC. Navigate to Function > Error History to view the last 20 fault records with timestamps — essential for intermittent faults.

## Related Articles

- [Daikin A3 Error Code — Causes & Fix](/posts/daikin-a3-error-code/)
- [Daikin Applied Chiller Fault Codes Guide — WMC / AGZ / ALZ Series](/posts/daikin-applied-fault-codes/)
- [Daikin C4 Error Code — Heat Exchanger Coil Sensor: Causes & Fix](/posts/daikin-c4-error-code/)
- [Daikin C9 Error Code — Compressor Discharge Temperature Sensor Fault](/posts/daikin-c9-error-code/)
- [Daikin E1 Error Code Fix — Indoor Sensor Fault](/posts/daikin-e1-error-code/)
