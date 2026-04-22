---
title: "Trane VRF System Error Codes Guide"
description: "Complete guide to Trane VRF error codes. Covers all fault codes for Trane VRF multi-split systems with diagnostic steps and technician fixes."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - trane
  - vrf
  - commercial-hvac
---

# Trane VRF System Error Codes: Complete Guide

Trane VRF (Variable Refrigerant Flow) systems display fault codes on the wired remote controller, the outdoor unit LED display, and the Trane Tracer building automation system. This guide covers all major Trane VRF error codes.

## Trane VRF Error Code Table

### Outdoor Unit Faults

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Description | Common Cause | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | --- |---|---|
| E01 | [Outdoor PCB fault](https://www.amazon.com/s?k=Outdoor%20PCB%20fault&tag=errorcodefixe-20) | Replace main control board |
| [E02](https://www.amazon.com/s?k=E02&tag=errorcodefixe-20) | High-pressure protection | Dirty condenser coil, overcharge | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | E03 | Low-pressure protection | [Low refrigerant, airflow issue](https://www.amazon.com/s?k=Low%20refrigerant%2C%20airflow%20issue&tag=errorcodefixe-20) |  | E04 | [Discharge temperature high](https://www.amazon.com/s?k=Discharge%20temperature%20high&tag=errorcodefixe-20) | Low refrigerant, TXV restriction |
| [E05](https://www.amazon.com/s?k=E05&tag=errorcodefixe-20) | Phase detection fault | Check 3-phase power and rotation | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | E06 | Compressor overload protection | [High amp draw — check compressor](https://www.amazon.com/s?k=High%20amp%20draw%20%E2%80%94%20check%20compressor&tag=errorcodefixe-20) |  | E07 | [Fan motor fault](https://www.amazon.com/s?k=Fan%20motor%20fault&tag=errorcodefixe-20) | Fan motor or inverter board fault |
| [E08](https://www.amazon.com/s?k=E08&tag=errorcodefixe-20) | Electronic expansion valve fault | EEV coil or wiring | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | E09 | Outdoor temperature sensor fault | [Replace outdoor air sensor](https://www.amazon.com/s?k=Replace%20outdoor%20air%20sensor&tag=errorcodefixe-20) |  | E10 | [Heat exchanger sensor fault](https://www.amazon.com/s?k=Heat%20exchanger%20sensor%20fault&tag=errorcodefixe-20) | Check condenser coil sensor |
| [E11](https://www.amazon.com/s?k=E11&tag=errorcodefixe-20) | Discharge pipe sensor fault | Sensor at compressor discharge | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | E12 | Communication fault — outdoor PCBs | [Internal board communication](https://www.amazon.com/s?k=Internal%20board%20communication&tag=errorcodefixe-20) | ### Indoor Unit Faults | Code | [Description](https://www.amazon.com/s?k=Description&tag=errorcodefixe-20) | Common Cause |
|---|---|---| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | I01 | Indoor PCB fault | [Replace indoor control board](https://www.amazon.com/s?k=Replace%20indoor%20control%20board&tag=errorcodefixe-20) |  | I02 | [Communication fault — indoor](https://www.amazon.com/s?k=Communication%20fault%20%E2%80%94%20indoor&tag=errorcodefixe-20) | Check F1/F2 wiring |
| [I03](https://www.amazon.com/s?k=I03&tag=errorcodefixe-20) | Indoor fan motor fault | Fan motor or capacitor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | I04 | Freeze protection | [Low refrigerant, dirty filter](https://www.amazon.com/s?k=Low%20refrigerant%2C%20dirty%20filter&tag=errorcodefixe-20) |  | I05 | [Drain sensor / overflow fault](https://www.amazon.com/s?k=Drain%20sensor%20%2F%20overflow%20fault&tag=errorcodefixe-20) | Blocked drain, failed pump |
| [I06](https://www.amazon.com/s?k=I06&tag=errorcodefixe-20) | Room temperature sensor fault | Check 10K sensor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | I07 | Indoor coil sensor fault | [Check pipe temperature sensor](https://www.amazon.com/s?k=Check%20pipe%20temperature%20sensor&tag=errorcodefixe-20) |  | I08 | [Indoor EEV fault](https://www.amazon.com/s?k=Indoor%20EEV%20fault&tag=errorcodefixe-20) | EEV coil or wiring |

### System-Wide Faults

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Description | Common Cause | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | --- |---|---|
| C01 | [Communication fault — all units](https://www.amazon.com/s?k=Communication%20fault%20%E2%80%94%20all%20units&tag=errorcodefixe-20) | F1/F2 network issue |
| [C02](https://www.amazon.com/s?k=C02&tag=errorcodefixe-20) | Address conflict | Duplicate indoor unit addresses | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | C03 | Indoor unit capacity mismatch | [Connected capacity exceeds outdoor](https://www.amazon.com/s?k=Connected%20capacity%20exceeds%20outdoor&tag=errorcodefixe-20) |  | L01 | [Hard lockout — requires manual reset](https://www.amazon.com/s?k=Hard%20lockout%20%E2%80%94%20requires%20manual%20reset&tag=errorcodefixe-20) | 3 consecutive same faults |

## Most Common Trane VRF Faults

### E02 — High Pressure Protection
1. Inspect and clean condenser coil
2. Verify all condenser fans are running (check run capacitors)
3. Check refrigerant subcooling at liquid line — target 8–15°F
4. Check for non-condensables if system was recently serviced

### E03 — Low Pressure Protection
1. Check refrigerant charge with manifold gauges
2. Inspect indoor filters at every air handler
3. Check indoor blower motors
4. Inspect TXV/EEV operation

### C01 — Communication Fault
1. Walk every indoor unit and check F1/F2 terminal connections
2. Verify wire polarity is consistent throughout
3. Check for damaged wire or junction boxes in the communication loop
4. Look for any units with address switches set to 0 or duplicated

### I04 — Freeze Protection
1. Check and replace indoor air filter
2. Verify indoor fan operates at all speeds
3. Check refrigerant superheat at the indoor coil
4. Check for refrigerant undercharge

## Accessing Fault History on Trane VRF

**Wired remote controller:** Press MENU > INFORMATION > ERROR HISTORY to view the last 10 faults with timestamps.

**Tracer BAS:** The Tracer system logs all VRF faults with timestamps. Access via the Tracer dashboard under System Status > VRF Alarms.

## Trane VRF Parts Reference

| Part | Notes |
|---|---|
| [EEV coil](https://www.amazon.com/s?k=EEV%20coil&tag=errorcodefixe-20) | Model-specific — check winding resistance before replacement |
| [Outdoor main board](https://www.amazon.com/s?k=Outdoor%20main%20board&tag=errorcodefixe-20) | Match exact model — firmware may need update |
| [Indoor PCB](https://www.amazon.com/s?k=Indoor%20PCB&tag=errorcodefixe-20) | Indoor unit-specific part number |
| [Temperature sensor](https://www.amazon.com/s?k=Temperature%20sensor&tag=errorcodefixe-20) | 10K NTC — match resistance curve |
| [Communication wire](https://www.amazon.com/s?k=Communication%20wire&tag=errorcodefixe-20) | 18-gauge unshielded 2-conductor |

> **Note:** Trane VRF systems are manufactured in partnership with Daikin. Some service procedures and parts cross-reference to Daikin VRV documentation.
