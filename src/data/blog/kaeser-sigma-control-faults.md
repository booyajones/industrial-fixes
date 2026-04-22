---
title: "Kaeser SIGMA CONTROL 2 Fault Codes: Complete Guide"
description: "Kaeser SIGMA CONTROL 2 fault codes and diagnostics. Compressor warnings, shutdowns, causes, and technician-level troubleshooting."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - compressor
  - kaeser
  - industrial
---

# Kaeser SIGMA CONTROL 2 Fault Codes

Kaeser compressors with SIGMA CONTROL 2 (second generation) use text-based alarm messages displayed on the controller panel. The SIGMA CONTROL 2 provides more detail and connectivity than the original Sigma Control, including Ethernet integration and remote monitoring via SIGMA NETWORK.

## SIGMA CONTROL 2 Fault Reference

| [Alarm Message](https://www.amazon.com/s?k=Alarm%20Message&tag=errorcodefixe-20) | Category | Common Cause | [Action](https://www.amazon.com/s?k=Action&tag=errorcodefixe-20) |  |--------------|----------|--------------|--------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Final compression temp — Warning | Warning | [Approaching high temp limit](https://www.amazon.com/s?k=Approaching%20high%20temp%20limit&tag=errorcodefixe-20) | Clean coolers, check oil |
| [Final compression temp — Shutdown](https://www.amazon.com/s?k=Final%20compression%20temp%20%E2%80%94%20Shutdown&tag=errorcodefixe-20) | Shutdown | Excessive temperature | [Clean coolers, check oil, check ambient](https://www.amazon.com/s?k=Clean%20coolers%2C%20check%20oil%2C%20check%20ambient&tag=errorcodefixe-20) |  | Motor protection — Shutdown | [Shutdown](https://www.amazon.com/s?k=Shutdown&tag=errorcodefixe-20) | Motor overload | Check motor amps and load | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Emergency stop — Active | Shutdown | [E-stop circuit open](https://www.amazon.com/s?k=E-stop%20circuit%20open&tag=errorcodefixe-20) | Check all E-stop switches |
| [Pressure sensor — Fault](https://www.amazon.com/s?k=Pressure%20sensor%20%E2%80%94%20Fault&tag=errorcodefixe-20) | Warning | Failed pressure transducer | [Check sensor wiring and signal](https://www.amazon.com/s?k=Check%20sensor%20wiring%20and%20signal&tag=errorcodefixe-20) |  | Temperature sensor — Fault | [Warning](https://www.amazon.com/s?k=Warning&tag=errorcodefixe-20) | Failed temperature sensor | Check sensor resistance | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Dryer — Fault | Warning | [Integrated dryer alarm](https://www.amazon.com/s?k=Integrated%20dryer%20alarm&tag=errorcodefixe-20) | Check refrigerant dryer operation |
| [Service — Required](https://www.amazon.com/s?k=Service%20%E2%80%94%20Required&tag=errorcodefixe-20) | Maintenance | Service interval reached | [Perform scheduled service](https://www.amazon.com/s?k=Perform%20scheduled%20service&tag=errorcodefixe-20) |  | Fan motor — Fault | [Shutdown](https://www.amazon.com/s?k=Shutdown&tag=errorcodefixe-20) | Cooling fan motor fault | Check fan motor amps and contactor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Condensate drain — Fault | Warning | [Drain solenoid not operating](https://www.amazon.com/s?k=Drain%20solenoid%20not%20operating&tag=errorcodefixe-20) | Check drain solenoid and timer |
| [Oil filter — Service](https://www.amazon.com/s?k=Oil%20filter%20%E2%80%94%20Service&tag=errorcodefixe-20) | Maintenance | Oil filter replacement due | [Replace oil filter element](https://www.amazon.com/s?k=Replace%20oil%20filter%20element&tag=errorcodefixe-20) |  | Differential pressure — High | [Warning](https://www.amazon.com/s?k=Warning&tag=errorcodefixe-20) | Separator element clogged | Replace separator element | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Communication — Fault | Warning | [Network communication loss](https://www.amazon.com/s?k=Network%20communication%20loss&tag=errorcodefixe-20) | Check Ethernet and network config |
| [Phase — Fault](https://www.amazon.com/s?k=Phase%20%E2%80%94%20Fault&tag=errorcodefixe-20) | Shutdown | Phase loss or reversal | [Check input power quality](https://www.amazon.com/s?k=Check%20input%20power%20quality&tag=errorcodefixe-20) | ## Most Common SIGMA CONTROL 2 Faults

### Final Compression Temp — Shutdown
Kaeser's shutdown threshold is typically 110°C (230°F). Warning precedes shutdown by approximately 5°C. Root cause is almost always a dirty cooler. Kaeser SIGMA CONTROL 2 logs the temperature trend — review to see if temp is climbing progressively or suddenly.

### Dryer Fault
On packages with integrated refrigerated dryer, the SIGMA CONTROL 2 monitors dryer operation. Dryer fault triggers if the dryer controller generates an alarm. Check the dryer controller (separate display inside the package) for a specific fault. Common: dryer refrigerant pressure alarm, condenser fan fault, or high pressure dewpoint.

### Service Required
SIGMA CONTROL 2 tracks service intervals by operating hours. Service due alerts appear in advance of the actual service interval (configurable, typically 100 hours before). Perform Kaeser-specified maintenance and reset the service counter in the SIGMA CONTROL 2 menu (requires service password).

### Communication Fault
SIGMA CONTROL 2 supports Modbus, PROFIBUS, PROFINET, and Ethernet. A communication fault means the controller cannot communicate with the BMS, master controller, or SIGMA NETWORK. Check network cable connections and verify IP address configuration.

## Parts Commonly Needed | Part | [Notes](https://www.amazon.com/s?k=Notes&tag=errorcodefixe-20) |  |------|-------|
| Oil separator element | [Kaeser-specific — match model](https://www.amazon.com/s?k=Kaeser-specific%20%E2%80%94%20match%20model&tag=errorcodefixe-20) |  | Oil filter element | [Match package model](https://www.amazon.com/s?k=Match%20package%20model&tag=errorcodefixe-20) |  | Pressure transducer | [Check signal output (typically 4–20 mA)](https://www.amazon.com/s?k=Check%20signal%20output%20(typically%204%E2%80%9320%20mA)&tag=errorcodefixe-20) |  | Temperature sensor | [NTC thermistor — check resistance](https://www.amazon.com/s?k=NTC%20thermistor%20%E2%80%94%20check%20resistance&tag=errorcodefixe-20) |  | Condensate drain solenoid | [Match voltage and orifice size](https://www.amazon.com/s?k=Match%20voltage%20and%20orifice%20size&tag=errorcodefixe-20) |  | Fan motor contactor | Check contact condition |

> **Pro tip:** Kaeser SIGMA CONTROL 2 can be connected to SIGMA NETWORK for remote monitoring. Kaeser service centers can remotely access fault logs and performance data. Register the compressor on SIGMA NETWORK to enable predictive maintenance alerts.
