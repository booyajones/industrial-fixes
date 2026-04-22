---
title: "Carrier VRF System Error Codes Guide"
description: "Complete guide to Carrier VRF (Variable Refrigerant Flow) system error codes. Covers all fault codes for Carrier i-Vu and CCN-based VRF systems."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - carrier
  - vrf
  - commercial-hvac
---

# Carrier VRF System Error Codes: Complete Guide

Carrier VRF systems (sold under the Carrier and Midea-sourced product lines) display fault codes on the indoor unit wired remotes, the outdoor unit LED panel, and the i-Vu building automation interface. This guide covers all common Carrier VRF fault codes.

## How Carrier VRF Codes Are Displayed

- **Wired remote (UTY-RNNUM or Carrier branded):** Error code displayed on screen
- **Outdoor unit LED:** Seven-segment display on the main board shows fault code
- **i-Vu / CCN:** Alphanumeric codes in the fault log

## Carrier VRF Error Code Table

### Communication / System Faults

| Code | Description | Common Cause |
|---|---|---|
| E01 | Indoor/outdoor communication fault | Check F1/F2 wiring |
| E02 | Outdoor unit PCB fault | Replace outdoor main board |
| E03 | Phase detection fault | Check 3-phase power supply |
| E04 | High-pressure protection | Dirty condenser, overcharge |
| E05 | Low-pressure protection | Low refrigerant, airflow issue |
| E06 | Discharge temperature high | Low refrigerant, TXV fault |
| E07 | Compressor overload | Check compressor amps |
| E08 | Fan motor fault — outdoor | Fan motor or inverter board |
| E09 | Electronic expansion valve fault | EEV coil or wiring |
| E10 | Heat exchanger sensor fault | Check condenser/evap sensor |

### Indoor Unit Faults

| Code | Description | Common Cause |
|---|---|---|
| I01 | Indoor PCB fault | Replace indoor control board |
| I02 | Indoor communication fault | Check F1/F2 wiring to indoor unit |
| I03 | Indoor fan motor fault | Motor or capacitor |
| I04 | Freeze protection trip | Low refrigerant, dirty filter |
| I05 | Drain level fault | Blocked drain, condensate pump |
| I06 | Indoor temperature sensor fault | Check sensor resistance |
| I07 | Pipe temperature sensor fault | Check liquid/suction pipe sensors |

### Protection / Lockout Faults

| Code | Description | Common Cause |
|---|---|---|
| F01 | Hard lockout — high pressure | 3 HP trips — manual reset |
| F02 | Hard lockout — low pressure | 3 LP trips — manual reset |
| F03 | Hard lockout — discharge temp | 3 high-temp trips — manual reset |
| F04 | Compressor lockout | Compressor protection activated |

## Most Common Carrier VRF Faults

### E01 — Communication Fault
The most common VRF fault. Check:
1. F1/F2 wiring at every indoor unit — ensure tight connections
2. Total wire length does not exceed system maximum (typically 1000m)
3. No reverse polarity in the communication circuit
4. Address switches on all indoor units are unique

### E04 — High Pressure
1. Check condenser coil and clean if dirty
2. Verify all condenser fans are operating
3. Check refrigerant charge (subcooling)
4. Check for non-condensables if system was opened

### I04 — Freeze Protection Trip
1. Replace dirty indoor filter
2. Check indoor fan operation
3. Check refrigerant superheat — should be 8–15°F
4. Inspect indoor coil for ice

### E09 — EEV Fault
Electronic expansion valve faults are common after refrigerant work:
1. Check EEV coil resistance (typically 40–60 ohms per winding)
2. Check wiring harness connections
3. Check for mechanical blockage (debris in EEV)

## Carrier VRF Parts Reference

| Part | Notes |
|---|---|
| Electronic expansion valve | Model-specific — match kv and connection |
| Outdoor main PCB | Match model and firmware version |
| Indoor PCB | Indoor unit-specific |
| Communication wire | Unshielded 2-conductor — match gauge for run length |
| Temperature sensor | 10K NTC thermistor |
| Inverter module (IPM) | High-value outdoor part |

> **Note:** Some Carrier VRF product lines are manufactured by Midea. Technical service manuals are available via Carrier's commercial partner portal. Always verify with the model number before ordering parts.
