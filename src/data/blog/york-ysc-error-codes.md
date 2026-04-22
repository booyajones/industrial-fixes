---
title: "York YSC Rooftop Unit Error Codes Guide"
description: "Complete York YSC series rooftop unit error codes. Covers all E-codes, P-codes, and flash codes with technician-level diagnostic steps."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - york
  - rooftop-unit
  - commercial-hvac
---

# York YSC Rooftop Unit Error Codes: Complete Guide

The York YSC series is a light commercial packaged rooftop unit covering 2–12.5 tons. Fault codes are displayed via the LED on the IFC board (flash codes) and alphanumeric codes on the optional diagnostic panel or communicating thermostat.

## York YSC Flash Code Table

| [Flash Count](https://www.amazon.com/s?k=Flash%20Count&tag=errorcodefixe-20) | Fault | Common Cause | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | --- |---|---|
| 1 flash | [System lockout](https://www.amazon.com/s?k=System%20lockout&tag=errorcodefixe-20) | Manual reset required |
| [2 flashes](https://www.amazon.com/s?k=2%20flashes&tag=errorcodefixe-20) | Low-pressure switch open | Low refrigerant, dirty filter | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 3 flashes | High-pressure switch open | [Dirty condenser, fan failure](https://www.amazon.com/s?k=Dirty%20condenser%2C%20fan%20failure&tag=errorcodefixe-20) |  | 4 flashes | [Limit switch open](https://www.amazon.com/s?k=Limit%20switch%20open&tag=errorcodefixe-20) | Airflow restriction |
| [5 flashes](https://www.amazon.com/s?k=5%20flashes&tag=errorcodefixe-20) | Rollout switch open | Heat exchanger issue | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 6 flashes | Ignition lockout | [Gas, igniter, or sensor fault](https://www.amazon.com/s?k=Gas%2C%20igniter%2C%20or%20sensor%20fault&tag=errorcodefixe-20) |  | 7 flashes | [Flame sense fault](https://www.amazon.com/s?k=Flame%20sense%20fault&tag=errorcodefixe-20) | Dirty or failed flame sensor |
| [8 flashes](https://www.amazon.com/s?k=8%20flashes&tag=errorcodefixe-20) | Pressure switch stuck closed | Faulty pressure switch | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 9 flashes | Reverse rotation — blower | [Blower wired incorrectly or failed](https://www.amazon.com/s?k=Blower%20wired%20incorrectly%20or%20failed&tag=errorcodefixe-20) | ## York YSC Alphanumeric Fault Codes | Code | [Description](https://www.amazon.com/s?k=Description&tag=errorcodefixe-20) | Likely Cause / Action |
|---|---|---| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | E1 | Control board communication fault | [Check wiring harness, replace board](https://www.amazon.com/s?k=Check%20wiring%20harness%2C%20replace%20board&tag=errorcodefixe-20) |  | E2 | [Supply air temperature sensor fault](https://www.amazon.com/s?k=Supply%20air%20temperature%20sensor%20fault&tag=errorcodefixe-20) | Check sensor resistance, replace |
| [E3](https://www.amazon.com/s?k=E3&tag=errorcodefixe-20) | Return air temperature sensor fault | Check or replace return sensor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | E4 | Outdoor air temperature sensor fault | [Check or replace outdoor sensor](https://www.amazon.com/s?k=Check%20or%20replace%20outdoor%20sensor&tag=errorcodefixe-20) |  | E5 | [Discharge temperature sensor fault](https://www.amazon.com/s?k=Discharge%20temperature%20sensor%20fault&tag=errorcodefixe-20) | Check sensor at compressor discharge |
| [E6](https://www.amazon.com/s?k=E6&tag=errorcodefixe-20) | High-pressure switch lockout — circuit 1 | Check condenser coil, fan, refrigerant | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | E7 | High-pressure switch lockout — circuit 2 | [Check condenser coil, fan, refrigerant](https://www.amazon.com/s?k=Check%20condenser%20coil%2C%20fan%2C%20refrigerant&tag=errorcodefixe-20) |  | E8 | [Low-pressure switch lockout](https://www.amazon.com/s?k=Low-pressure%20switch%20lockout&tag=errorcodefixe-20) | Check refrigerant charge and airflow |
| [E9](https://www.amazon.com/s?k=E9&tag=errorcodefixe-20) | Compressor time delay active | Wait — normal startup protection | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | P1 | Low-ambient compressor lockout | [Ambient below minimum — check settings](https://www.amazon.com/s?k=Ambient%20below%20minimum%20%E2%80%94%20check%20settings&tag=errorcodefixe-20) |  | P2 | [Low-ambient heating lockout](https://www.amazon.com/s?k=Low-ambient%20heating%20lockout&tag=errorcodefixe-20) | Ambient too low for heating operation |
| [P3](https://www.amazon.com/s?k=P3&tag=errorcodefixe-20) | Brownout / low voltage lockout | Check supply voltage | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | H1 | High humidity lockout | [Dehumidification mode — check controls](https://www.amazon.com/s?k=Dehumidification%20mode%20%E2%80%94%20check%20controls&tag=errorcodefixe-20) | ## Most Common YSC Faults and Fixes

### E6 / E7 — High-Pressure Lockout
The most frequent YSC summer fault:
1. Check condenser coil — clean if dirty
2. Verify all condenser fan motors are running (check run capacitors)
3. Check refrigerant charge — superheat and subcooling
4. Confirm the high-pressure switch trips correctly (replace if stuck open or failing intermittently)

### Flash 4 — Open Limit Switch
The most frequent YSC heating fault:
1. Replace dirty air filter
2. Confirm all supply grilles are open and unobstructed
3. Check blower motor and run capacitor
4. Test limit switch continuity at room temperature

### E2 / E3 / E4 — Sensor Faults
Temperature sensors on York YSC units have a nominal resistance of 10K ohms at 77°F (25°C). Check resistance with a multimeter and compare to the resistance chart in the service manual.

### Flash 6 — Ignition Lockout
1. Measure gas pressure at manifold: 3.5 in. w.c. natural gas
2. Inspect hot surface igniter for cracks
3. Clean or replace flame sensor
4. Check for combustion air obstructions

## YSC Parts Reference | Part | [Notes](https://www.amazon.com/s?k=Notes&tag=errorcodefixe-20) |  |---|---|
| Temperature sensor | [10K thermistor — York part S1-02525919700](https://www.amazon.com/s?k=10K%20thermistor%20%E2%80%94%20York%20part%20S1-02525919700&tag=errorcodefixe-20) |  | Hot surface igniter | [Model-specific — check tonnage and model suffix](https://www.amazon.com/s?k=Model-specific%20%E2%80%94%20check%20tonnage%20and%20model%20suffix&tag=errorcodefixe-20) |  | Flame sensor rod | [Measure µA before replacing](https://www.amazon.com/s?k=Measure%20%C2%B5A%20before%20replacing&tag=errorcodefixe-20) |  | High-pressure switch | [Check trip pressure setting](https://www.amazon.com/s?k=Check%20trip%20pressure%20setting&tag=errorcodefixe-20) |  | Run capacitor | [Check µF on both compressor and fan caps](https://www.amazon.com/s?k=Check%20%C2%B5F%20on%20both%20compressor%20and%20fan%20caps&tag=errorcodefixe-20) |  | IFC control board | York part number varies by tonnage |

> **Note:** The York YSC shares many components with the Coleman and Luxaire commercial RTU lines. Parts are interchangeable.
