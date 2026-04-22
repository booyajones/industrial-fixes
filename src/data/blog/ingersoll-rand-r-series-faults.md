---
title: "Ingersoll-Rand R-Series Compressor Fault Codes: Complete Guide"
description: "Ingersoll-Rand R-Series rotary screw compressor fault codes and diagnostics. Fault codes, causes, and technician-level troubleshooting."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - compressor
  - ingersoll-rand
  - industrial
---

# Ingersoll-Rand R-Series Compressor Fault Codes

Ingersoll-Rand R-Series rotary screw compressors (R7.5–R90) use the Intellisys® controller for monitoring and fault management. Faults display on the Intellisys panel as text messages. The controller logs fault history with timestamps and run hours.

## R-Series Fault Code Table

| [Fault](https://www.amazon.com/s?k=Fault&tag=errorcodefixe-20) | Fault Description | Common Cause | [Action](https://www.amazon.com/s?k=Action&tag=errorcodefixe-20) |  |-------|------------------|--------------|--------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | HIGH TEMP | High discharge temperature | [Cooler dirty, low oil, high ambient](https://www.amazon.com/s?k=Cooler%20dirty%2C%20low%20oil%2C%20high%20ambient&tag=errorcodefixe-20) | Clean cooler, check oil level |
| [HIGH TEMP WARN](https://www.amazon.com/s?k=HIGH%20TEMP%20WARN&tag=errorcodefixe-20) | Temperature warning | Approaching shutdown threshold | [Pre-clean cooler before shutdown](https://www.amazon.com/s?k=Pre-clean%20cooler%20before%20shutdown&tag=errorcodefixe-20) |  | STAR DELTA FAULT | [Starter transition fault](https://www.amazon.com/s?k=Starter%20transition%20fault&tag=errorcodefixe-20) | Contactor or timing issue | Check starter sequence | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | OVERLOAD | Motor overload trip | [Motor overload or high current](https://www.amazon.com/s?k=Motor%20overload%20or%20high%20current&tag=errorcodefixe-20) | Check motor amps and load |
| [HIGH PRESSURE](https://www.amazon.com/s?k=HIGH%20PRESSURE&tag=errorcodefixe-20) | Discharge pressure too high | Excessive demand or closed valve | [Check discharge valve](https://www.amazon.com/s?k=Check%20discharge%20valve&tag=errorcodefixe-20) |  | LOW INLET PRESSURE | [Inlet filter restricted](https://www.amazon.com/s?k=Inlet%20filter%20restricted&tag=errorcodefixe-20) | Dirty inlet filter | Replace inlet air filter | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | OIL FAULT | Low oil pressure | [Low oil, failed oil pump](https://www.amazon.com/s?k=Low%20oil%2C%20failed%20oil%20pump&tag=errorcodefixe-20) | Check oil level and pump |
| [PHASE FAULT](https://www.amazon.com/s?k=PHASE%20FAULT&tag=errorcodefixe-20) | Phase loss or imbalance | Supply fault | [Check input voltage](https://www.amazon.com/s?k=Check%20input%20voltage&tag=errorcodefixe-20) |  | EMERGENCY STOP | [E-stop activated](https://www.amazon.com/s?k=E-stop%20activated&tag=errorcodefixe-20) | E-stop button pressed | Check E-stop circuit | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | SERVICE LEVEL 1 | Preventive maintenance due | [Hours elapsed](https://www.amazon.com/s?k=Hours%20elapsed&tag=errorcodefixe-20) | Perform scheduled PM |
| [SERVICE LEVEL 2](https://www.amazon.com/s?k=SERVICE%20LEVEL%202&tag=errorcodefixe-20) | Major PM due | Major service interval | [Perform major PM](https://www.amazon.com/s?k=Perform%20major%20PM&tag=errorcodefixe-20) |  | SENSOR FAULT | [Temperature sensor failure](https://www.amazon.com/s?k=Temperature%20sensor%20failure&tag=errorcodefixe-20) | Failed thermistor | Replace temperature sensor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | DRAIN FAULT | Auto-drain failure | [Solenoid drain valve stuck](https://www.amazon.com/s?k=Solenoid%20drain%20valve%20stuck&tag=errorcodefixe-20) | Check drain valve operation |

## Most Common R-Series Faults

### HIGH TEMP — High Discharge Temperature
Ingersoll-Rand R-Series maximum discharge temperature is typically 235°F (113°C) for standard models. High temp shutdowns are almost always caused by dirty oil coolers or dirty air coolers. Blow cooler fins with low-pressure air or wash with coil cleaner. Check oil level with the unit loaded and running.

### OVERLOAD — Motor Overload
Check three-phase supply voltage and balance. A 5% voltage imbalance can cause 25%+ current imbalance. Reset the overload relay after determining the cause. Check unloader operation — if the unit is starting under load, motor current is excessive on startup.

### LOW INLET PRESSURE — Inlet Filter
Ingersoll-Rand R-Series inlet filters have a differential pressure switch that triggers this alarm when restriction is excessive. Check filter element — replace at the service interval or when restriction is detected. Do not operate the compressor with a dirty filter; accelerated airend wear results.

### SERVICE LEVEL 1/2
The Intellisys controller tracks service intervals by run hours. Level 1 is typically the oil filter and separator element interval (every 2,000 hours). Level 2 is the major service interval (airend inspection, oil change, full filter replacement). Perform maintenance and reset the service timer in the Intellisys menu.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| [Inlet air filter](https://www.amazon.com/s?k=Inlet%20air%20filter&tag=errorcodefixe-20) | Replace at scheduled interval |
| [Oil filter element](https://www.amazon.com/s?k=Oil%20filter%20element&tag=errorcodefixe-20) | IR-specific — match model |
| [Oil separator element](https://www.amazon.com/s?k=Oil%20separator%20element&tag=errorcodefixe-20) | Replace at Level 2 interval |
| [Compressor oil](https://www.amazon.com/s?k=Compressor%20oil&tag=errorcodefixe-20) | IR synthetic — model-specific |
| [Auto-drain solenoid valve](https://www.amazon.com/s?k=Auto-drain%20solenoid%20valve&tag=errorcodefixe-20) | Check for stuck-open or stuck-closed |
| [Temperature sensor](https://www.amazon.com/s?k=Temperature%20sensor&tag=errorcodefixe-20) | Match Intellisys controller input type |

> **Pro tip:** Ingersoll-Rand Intellisys controllers on networked compressor rooms can be monitored remotely via the IR Connect app. Fault alerts can be sent to maintenance personnel by email or text, enabling faster response to high-temperature events before the compressor shuts down.
