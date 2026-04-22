---
title: "Trane XV20i/XV18 Variable Speed Heat Pump Error Codes"
description: "Trane XV20i and XV18 variable speed heat pump error codes and fault diagnostics. ComfortLink II fault codes, causes, and technician fixes."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - trane
  - heat-pump
  - variable-speed
---

# Trane XV20i/XV18 Variable Speed Heat Pump Error Codes

Trane XV20i (up to 20 SEER) and XV18 variable speed heat pumps use the ComfortLink II communicating system. Fault codes display on the Nexia thermostat or ComfortLink II controller. These units use inverter-driven compressors — some fault codes are inverter-specific.

## XV20i/XV18 Fault Code Table

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Fault Description | Common Cause | [Action](https://www.amazon.com/s?k=Action&tag=errorcodefixe-20) |  |------|------------------|--------------|--------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 26 | Defrost fault | [Defrost sensor issue](https://www.amazon.com/s?k=Defrost%20sensor%20issue&tag=errorcodefixe-20) | Check sensor position and resistance |
| [27](https://www.amazon.com/s?k=27&tag=errorcodefixe-20) | High discharge temp | Refrigerant issue, high load | [Check charge and condenser airflow](https://www.amazon.com/s?k=Check%20charge%20and%20condenser%20airflow&tag=errorcodefixe-20) |  | 40 | [Control board fault](https://www.amazon.com/s?k=Control%20board%20fault&tag=errorcodefixe-20) | Communication or board failure | Check wiring, replace board | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 41 | Inverter fault | [Inverter driver failure](https://www.amazon.com/s?k=Inverter%20driver%20failure&tag=errorcodefixe-20) | Check DC bus voltage, inverter board |
| [42](https://www.amazon.com/s?k=42&tag=errorcodefixe-20) | Compressor over-amp | Overload or mechanical issue | [Check voltage, check compressor amps](https://www.amazon.com/s?k=Check%20voltage%2C%20check%20compressor%20amps&tag=errorcodefixe-20) |  | 43 | [High/Low pressure trip](https://www.amazon.com/s?k=High%2FLow%20pressure%20trip&tag=errorcodefixe-20) | Refrigerant or airflow issue | Check pressures with manifold gauges | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 44 | Outdoor coil sensor | [Failed ambient or defrost sensor](https://www.amazon.com/s?k=Failed%20ambient%20or%20defrost%20sensor&tag=errorcodefixe-20) | Check sensor resistance |
| [51](https://www.amazon.com/s?k=51&tag=errorcodefixe-20) | Reversing valve fault | RV stuck or solenoid failure | [Check solenoid coil, RV operation](https://www.amazon.com/s?k=Check%20solenoid%20coil%2C%20RV%20operation&tag=errorcodefixe-20) |  | 60 | [Loss of communication](https://www.amazon.com/s?k=Loss%20of%20communication&tag=errorcodefixe-20) | Wiring to ComfortLink II | Check all communication wiring | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 79 | Pressure switch fault | [HP/LP switch wiring or failure](https://www.amazon.com/s?k=HP%2FLP%20switch%20wiring%20or%20failure&tag=errorcodefixe-20) | Check switch continuity |
| [89](https://www.amazon.com/s?k=89&tag=errorcodefixe-20) | Defrost lockout | Repeated defrost failures | [Check defrost system](https://www.amazon.com/s?k=Check%20defrost%20system&tag=errorcodefixe-20) | ## Most Common XV20i/XV18 Faults

### Code 41 — Inverter Fault
The XV20i uses a variable speed inverter compressor. Inverter faults require DC bus voltage measurement (should be 170+ VDC from 120 VAC supply). Check for capacitor leakage and inverter board connections before condemning.

### Code 43 — High/Low Pressure Trip
Variable speed units can operate at lower pressures than conventional systems. Use Trane's charging charts specific to the XV20i — do not use standard fixed-speed charging charts. EXV (electronic expansion valve) position affects superheat significantly.

### Code 26 — Defrost Fault
XV20i uses an inverter-controlled defrost. The defrost sensor must be clipped firmly to the liquid tube near the bottom of the outdoor coil. Check resistance: 10kΩ at 77°F (25°C).

### Code 60 — Loss of Communication
Check ComfortLink II communication wiring for breaks, shorts, or reversed polarity. The system uses a 2-wire data bus — wire color coding is critical.

## Parts Commonly Needed | Part | [Notes](https://www.amazon.com/s?k=Notes&tag=errorcodefixe-20) |  |------|-------|
| Inverter board | [High cost — verify with Trane tech support before ordering](https://www.amazon.com/s?k=High%20cost%20%E2%80%94%20verify%20with%20Trane%20tech%20support%20before%20ordering&tag=errorcodefixe-20) |  | ComfortLink II thermostat | [Required for fault code display](https://www.amazon.com/s?k=Required%20for%20fault%20code%20display&tag=errorcodefixe-20) |  | Defrost sensor | [Clip-on thermistor — verify resistance](https://www.amazon.com/s?k=Clip-on%20thermistor%20%E2%80%94%20verify%20resistance&tag=errorcodefixe-20) |  | Reversing valve | [Match refrigerant type](https://www.amazon.com/s?k=Match%20refrigerant%20type&tag=errorcodefixe-20) |  | Electronic expansion valve (EXV) | Variable speed units use EXV not TXV |

> **Pro tip:** Trane XV20i diagnostic data can be viewed via the Nexia app or Trane Diagnostics Tool. Always check inverter board LED indicators before ordering parts — they often pinpoint the specific fault.
