---
title: "York YVAA/YVVA Chiller Fault Codes — Complete Troubleshooting Guide"
description: "York YVAA and YVVA air-cooled chiller fault codes: OptiView control panel alarms, causes, and step-by-step troubleshooting for common shutdowns."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - chiller
  - york
  - hvac
  - industrial
---

## York YVAA/YVVA Chiller Fault Codes — Quick Reference

York YVAA (air-cooled screw) and YVVA (air-cooled variable speed screw) chillers use the OptiView Control Center to display safety shutdowns and cycling shutdowns.

| [Fault](https://www.amazon.com/s?k=Fault&tag=errorcodefixe-20) | Type | Meaning | [Quick Fix](https://www.amazon.com/s?k=Quick%20Fix&tag=errorcodefixe-20) |  |-------|------|---------|-----------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Low Refrigerant Pressure | Safety | [Suction pressure below cutout](https://www.amazon.com/s?k=Suction%20pressure%20below%20cutout&tag=errorcodefixe-20) | Check charge and evaporator flow |
| [High Refrigerant Pressure](https://www.amazon.com/s?k=High%20Refrigerant%20Pressure&tag=errorcodefixe-20) | Safety | Discharge pressure too high | [Check fans and condenser](https://www.amazon.com/s?k=Check%20fans%20and%20condenser&tag=errorcodefixe-20) |  | Low Leaving Water Temp | [Safety](https://www.amazon.com/s?k=Safety&tag=errorcodefixe-20) | LWT below freeze protection limit | Check flow and load | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Compressor Discharge Temp High | Safety | [Compressor outlet too hot](https://www.amazon.com/s?k=Compressor%20outlet%20too%20hot&tag=errorcodefixe-20) | Check refrigerant charge |
| [Motor Current High](https://www.amazon.com/s?k=Motor%20Current%20High&tag=errorcodefixe-20) | Safety | Motor overcurrent | [Check voltage and load](https://www.amazon.com/s?k=Check%20voltage%20and%20load&tag=errorcodefixe-20) |  | Loss of Charge | [Safety](https://www.amazon.com/s?k=Safety&tag=errorcodefixe-20) | Refrigerant pressure lost | Inspect for leak, check charge | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Low Ambient | Cycling | [Ambient too cold for operation](https://www.amazon.com/s?k=Ambient%20too%20cold%20for%20operation&tag=errorcodefixe-20) | Check low ambient kit |
| [No Cooling Load](https://www.amazon.com/s?k=No%20Cooling%20Load&tag=errorcodefixe-20) | Cycling | System does not require cooling | [Normal — not a fault](https://www.amazon.com/s?k=Normal%20%E2%80%94%20not%20a%20fault&tag=errorcodefixe-20) | ## Most Common Faults

### Low Refrigerant Pressure (Safety Shutdown)
On the YVAA, low suction pressure (Low Refrigerant Pressure safety) is the most common shutdown. Causes include low refrigerant charge, low chilled water flow, and low entering load. Check chilled water pump operation. If flow is confirmed, a refrigerant leak is likely.

### High Refrigerant Pressure (Safety Shutdown)
High discharge pressure shuts the unit down to protect the compressor. Check condenser fans — all fans must be running at the correct speed and direction. Check condenser coil cleanliness. On YVVA variable-speed units, verify the fan inverter is not faulted.

### Low Leaving Water Temperature (Safety Shutdown)
LWT is dropping below the low setpoint. Check chilled water flow rate with a flow meter or pump performance curve. If flow is adequate, check the setpoints — the LWT setpoint may be too close to the freeze protection limit.

## OptiView Control Center Navigation

- HOME → SYSTEM screen shows compressor status and pressures
- ALARM → HISTORY shows past shutdowns with timestamp and conditions
- SETUP → SETPOINTS for limit configuration

## YVVA Variable Speed Notes

The YVVA uses variable-speed compressors and fans. Additional faults include:
- **Inverter Fault** — drive fault on compressor or fan inverter
- **Speed Reference Fault** — control signal to inverter lost
- **Inverter Overtemp** — check inverter cooling

## Parts Often Needed | Part | [Notes](https://www.amazon.com/s?k=Notes&tag=errorcodefixe-20) |  |------|-------|
| Refrigerant charge (R-134a or R-513A) | [After confirmed leak and repair](https://www.amazon.com/s?k=After%20confirmed%20leak%20and%20repair&tag=errorcodefixe-20) |  | Condenser fan motor | [Replace on high pressure faults](https://www.amazon.com/s?k=Replace%20on%20high%20pressure%20faults&tag=errorcodefixe-20) |  | Fan blade | [Inspect if fan running but pressure high](https://www.amazon.com/s?k=Inspect%20if%20fan%20running%20but%20pressure%20high&tag=errorcodefixe-20) |  | Flow switch / flow sensor | Inspect on LWT faults |

## Jump to Fix

- **Low refrigerant pressure** → Check chilled water flow → Confirm charge → Inspect for leaks
- **High refrigerant pressure** → Verify all fans running → Clean condenser coil
- **Low LWT** → Confirm flow rate → Check LWT setpoint

## When to Call a Pro
York (Johnson Controls) has service centers nationwide. Contact 1-877-874-7378. Refrigerant work requires EPA Section 608 certification.
