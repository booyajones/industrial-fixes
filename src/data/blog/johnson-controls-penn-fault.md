---
title: "Johnson Controls Penn Commercial Controls Fault — Troubleshooting Guide"
description: "Johnson Controls Penn commercial controls faults for A421, A350, P70, and pressure/temperature controls: common alarms, causes, and repair steps."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - johnson-controls
  - penn
  - commercial-refrigeration
  - hvac
---

## Johnson Controls Penn Commercial Controls Faults — Quick Reference

Johnson Controls Penn controls show up in rooftop units, walk-ins, chillers, and process cooling equipment. Most Penn controls do not use long digital fault logs. They trip on pressure, temperature, or sensor input and the connected equipment locks out.

| Fault / Condition | Meaning | Quick Fix |
|------------------|---------|-----------|
| Sensor Error | Temperature sensor open or shorted | Check sensor resistance and wiring |
| High Pressure Trip | Pressure exceeded cutout | Check condenser airflow and charge |
| Low Pressure Trip | Suction pressure too low | Check charge and evaporator flow |
| Control Output Not Energizing | Relay failed or no control power | Check 24VAC / line voltage and relay |
| Manual Reset Open | Safety control tripped and latched | Find root cause before reset |
| Display Blank | No power to control | Check transformer, fuse, and wiring |

## Most Common Faults

### Sensor Error
Penn A421 and A350 digital controls use a thermistor sensor. If the sensor opens or shorts, the display shows an error and the relay output drops out. Check the sensor plug, then measure resistance. A typical 10K sensor reads about 10,000 ohms at 77°F.

### High Pressure Trip
Penn pressure controls are often wired in series with the compressor contactor coil. A high pressure trip means the control opened the circuit to protect the compressor. Check condenser fan operation, condenser coil cleanliness, and refrigerant overcharge.

### Low Pressure Trip
A low pressure safety opens when suction pressure falls too low. Common causes are low refrigerant charge, iced evaporator coil, plugged TXV screen, or low airflow across the evaporator.

## Penn Control Types

| Series | Type | Common Use |
|-------|------|------------|
| A421 | Digital temperature control | Walk-ins, condensers, pump control |
| A350 | Electronic temperature control | HVAC and refrigeration |
| P70 | Mechanical pressure control | Refrigeration safety |
| P78 | High/low pressure control | Compressor protection |

## Jump to Fix

- **Sensor error** → Check sensor plug → Measure resistance → Replace sensor
- **High pressure trip** → Check fans → Clean condenser → Check charge
- **Low pressure trip** → Check evaporator airflow → Check charge → Inspect TXV

## When to Call a Pro
If a Penn safety control keeps opening, do not jumper it out and walk away. Find the system problem first. Refrigerant work needs an EPA-certified technician.
