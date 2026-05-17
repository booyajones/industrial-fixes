---
title: "Trane XV20i/XV18 Variable Speed Heat Pump Error Codes"
description: "Trane XV20i and XV18 variable speed heat pump error codes and fault diagnostics. ComfortLink II fault codes, causes, and technician fixes."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-05-01T08:00:00Z
author: "Marcus Webb"
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

| Code | Fault Description | Common Cause | Action |
|------|------------------|--------------|--------|
| 26 | Defrost fault | Defrost sensor issue | Check sensor position and resistance |
| 27 | High discharge temp | Refrigerant issue, high load | Check charge and condenser airflow |
| 40 | Control board fault | Communication or board failure | Check wiring, replace board |
| 41 | Inverter fault | Inverter driver failure | Check DC bus voltage, inverter board |
| 42 | Compressor over-amp | Overload or mechanical issue | Check voltage, check compressor amps |
| 43 | High/Low pressure trip | Refrigerant or airflow issue | Check pressures with manifold gauges |
| 44 | Outdoor coil sensor | Failed ambient or defrost sensor | Check sensor resistance |
| 51 | Reversing valve fault | RV stuck or solenoid failure | Check solenoid coil, RV operation |
| 60 | Loss of communication | Wiring to ComfortLink II | Check all communication wiring |
| 79 | Pressure switch fault | HP/LP switch wiring or failure | Check switch continuity |
| 89 | Defrost lockout | Repeated defrost failures | Check defrost system |

## Most Common XV20i/XV18 Faults

### Code 41 — Inverter Fault
The XV20i uses a variable speed inverter compressor. Inverter faults require DC bus voltage measurement (should be 170+ VDC from 120 VAC supply). Check for capacitor leakage and inverter board connections before condemning.

### Code 43 — High/Low Pressure Trip
Variable speed units can operate at lower pressures than conventional systems. Use Trane's charging charts specific to the XV20i — do not use standard fixed-speed charging charts. EXV (electronic expansion valve) position affects superheat significantly.

### Code 26 — Defrost Fault
XV20i uses an inverter-controlled defrost. The defrost sensor must be clipped firmly to the liquid tube near the bottom of the outdoor coil. Check resistance: 10k╬⌐ at 77°F (25°C).

### Code 60 — Loss of Communication
Check ComfortLink II communication wiring for breaks, shorts, or reversed polarity. The system uses a 2-wire data bus — wire color coding is critical.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Inverter board | [Amazon](https://www.amazon.com/s?i=industrial&k=Inverter+board&tag=errorcodefixes-20) \| High cost — verify with Trane tech support before ordering |
| ComfortLink II thermostat | [Amazon](https://www.amazon.com/s?i=industrial&k=ComfortLink+II+thermostat&tag=errorcodefixes-20) \| Required for fault code display |
| Defrost sensor | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?tag=errorcodefixes-20) \| Clip-on thermistor — verify resistance |
| Reversing valve | [Amazon](https://www.amazon.com/s?i=industrial&k=Reversing+valve&tag=errorcodefixes-20) \| Match refrigerant type |
| Electronic expansion valve (EXV) | [Amazon](https://www.amazon.com/s?i=industrial&k=Electronic+expansion+valve+%28EXV%29&tag=errorcodefixes-20) \| Variable speed units use EXV not TXV |
> **Pro tip:** Trane XV20i diagnostic data can be viewed via the Nexia app or Trane Diagnostics Tool. Always check inverter board LED indicators before ordering parts — they often pinpoint the specific fault.

## Related Articles

- [Trane 1 Flash Error Code — Causes & Fix](/posts/trane-1-flash-error-code/)
- [Trane Error Code 126 — Ignition Lockout Fix](/posts/trane-126-error-code/)
- [Trane 2 Flashes Error Code — Causes & Fix](/posts/trane-2-flashes-error-code/)
- [Trane 3 Flashes Error Code — Pressure Switch Fault Fix](/posts/trane-3-flashes-error-code/)
- [Trane 3 Flash Pressure Switch Fault — Detailed Diagnosis Guide](/posts/trane-3-flashes-pressure-switch/)
