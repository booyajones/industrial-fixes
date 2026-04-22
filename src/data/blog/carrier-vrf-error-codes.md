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

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Description | Common Cause | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | --- |---|---|
| E01 | [Indoor/outdoor communication fault](https://www.amazon.com/s?k=Indoor%2Foutdoor%20communication%20fault&tag=errorcodefixe-20) | Check F1/F2 wiring |
| [E02](https://www.amazon.com/s?k=E02&tag=errorcodefixe-20) | Outdoor unit PCB fault | Replace outdoor main board | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | E03 | Phase detection fault | [Check 3-phase power supply](https://www.amazon.com/s?k=Check%203-phase%20power%20supply&tag=errorcodefixe-20) |  | E04 | [High-pressure protection](https://www.amazon.com/s?k=High-pressure%20protection&tag=errorcodefixe-20) | Dirty condenser, overcharge |
| [E05](https://www.amazon.com/s?k=E05&tag=errorcodefixe-20) | Low-pressure protection | Low refrigerant, airflow issue | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | E06 | Discharge temperature high | [Low refrigerant, TXV fault](https://www.amazon.com/s?k=Low%20refrigerant%2C%20TXV%20fault&tag=errorcodefixe-20) |  | E07 | [Compressor overload](https://www.amazon.com/s?k=Compressor%20overload&tag=errorcodefixe-20) | Check compressor amps |
| [E08](https://www.amazon.com/s?k=E08&tag=errorcodefixe-20) | Fan motor fault — outdoor | Fan motor or inverter board | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | E09 | Electronic expansion valve fault | [EEV coil or wiring](https://www.amazon.com/s?k=EEV%20coil%20or%20wiring&tag=errorcodefixe-20) |  | E10 | [Heat exchanger sensor fault](https://www.amazon.com/s?k=Heat%20exchanger%20sensor%20fault&tag=errorcodefixe-20) | Check condenser/evap sensor |

### Indoor Unit Faults

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Description | Common Cause | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | --- |---|---|
| I01 | [Indoor PCB fault](https://www.amazon.com/s?k=Indoor%20PCB%20fault&tag=errorcodefixe-20) | Replace indoor control board |
| [I02](https://www.amazon.com/s?k=I02&tag=errorcodefixe-20) | Indoor communication fault | Check F1/F2 wiring to indoor unit | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | I03 | Indoor fan motor fault | [Motor or capacitor](https://www.amazon.com/s?k=Motor%20or%20capacitor&tag=errorcodefixe-20) |  | I04 | [Freeze protection trip](https://www.amazon.com/s?k=Freeze%20protection%20trip&tag=errorcodefixe-20) | Low refrigerant, dirty filter |
| [I05](https://www.amazon.com/s?k=I05&tag=errorcodefixe-20) | Drain level fault | Blocked drain, condensate pump | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | I06 | Indoor temperature sensor fault | [Check sensor resistance](https://www.amazon.com/s?k=Check%20sensor%20resistance&tag=errorcodefixe-20) |  | I07 | [Pipe temperature sensor fault](https://www.amazon.com/s?k=Pipe%20temperature%20sensor%20fault&tag=errorcodefixe-20) | Check liquid/suction pipe sensors |

### Protection / Lockout Faults

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Description | Common Cause | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | --- |---|---|
| F01 | [Hard lockout — high pressure](https://www.amazon.com/s?k=Hard%20lockout%20%E2%80%94%20high%20pressure&tag=errorcodefixe-20) | 3 HP trips — manual reset |
| [F02](https://www.amazon.com/s?k=F02&tag=errorcodefixe-20) | Hard lockout — low pressure | 3 LP trips — manual reset | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | F03 | Hard lockout — discharge temp | [3 high-temp trips — manual reset](https://www.amazon.com/s?k=3%20high-temp%20trips%20%E2%80%94%20manual%20reset&tag=errorcodefixe-20) |  | F04 | [Compressor lockout](https://www.amazon.com/s?k=Compressor%20lockout&tag=errorcodefixe-20) | Compressor protection activated |

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
| [Electronic expansion valve](https://www.amazon.com/s?k=Electronic%20expansion%20valve&tag=errorcodefixe-20) | Model-specific — match kv and connection |
| [Outdoor main PCB](https://www.amazon.com/s?k=Outdoor%20main%20PCB&tag=errorcodefixe-20) | Match model and firmware version |
| [Indoor PCB](https://www.amazon.com/s?k=Indoor%20PCB&tag=errorcodefixe-20) | Indoor unit-specific |
| [Communication wire](https://www.amazon.com/s?k=Communication%20wire&tag=errorcodefixe-20) | Unshielded 2-conductor — match gauge for run length |
| [Temperature sensor](https://www.amazon.com/s?k=Temperature%20sensor&tag=errorcodefixe-20) | 10K NTC thermistor |
| [Inverter module (IPM)](https://www.amazon.com/s?k=Inverter%20module%20(IPM)&tag=errorcodefixe-20) | High-value outdoor part |

> **Note:** Some Carrier VRF product lines are manufactured by Midea. Technical service manuals are available via Carrier's commercial partner portal. Always verify with the model number before ordering parts.
