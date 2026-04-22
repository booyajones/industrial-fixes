---
title: "Daikin Applied Chiller Fault Codes Guide — WMC / AGZ / ALZ Series"
description: "Daikin Applied chiller fault codes for WMC, AGZ, ALZ, and centrifugal chillers: alarm descriptions, causes, and troubleshooting steps."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - chiller
  - daikin-applied
  - hvac
  - industrial
---

## Daikin Applied Chiller Fault Codes — Quick Reference

Daikin Applied chillers (WMC water-cooled scroll, AGZ air-cooled, ALZ air-cooled scroll, and centrifugal units) use the MicroTech III or MicroTech 4 controller to display alarms and shutdowns.

| Fault Code | Meaning | Quick Fix |
|-----------|---------|-----------|
| Low Pressure Cutout | Suction pressure too low | Check refrigerant charge and evaporator flow |
| High Pressure Cutout | Discharge pressure too high | Check condenser flow/fan and refrigerant |
| Low Evaporator LWT | Leaving water temp too low | Check flow rate and load |
| High Motor Temp | Compressor motor temperature high | Check voltage, load, and cooling |
| Freeze Protection | Evaporator temperature near freeze | Check flow, setpoints, and antifreeze |
| Comm Fault | Controller communication loss | Check BACnet/Modbus wiring |
| Compressor Fault | Compressor protection tripped | Check motor protection and contactor |
| Low Refrigerant | Refrigerant pressure low on both sides | Inspect for leaks, check charge |

## Most Common Faults

### Low Pressure Cutout
Low suction pressure is the most frequent chiller alarm. On water-cooled units, check the chilled water flow rate through the evaporator — low flow causes the refrigerant to get too cold. Also check refrigerant charge. On air-cooled units, verify ambient temperature is within the unit's operating range.

### High Pressure Cutout
Discharge pressure is too high. On air-cooled chillers, check: condenser coil cleanliness, fan operation (all fans running), and ambient temperature. On water-cooled units, check condenser water flow rate and entering condenser water temperature.

### Freeze Protection
The evaporator approach temperature has reached the freeze protection threshold. Check for: low chilled water flow (pump failure, valve closed), low load causing low flow, or incorrect setpoints. Do not defeat freeze protection — a frozen evaporator is a major repair.

## MicroTech III Navigation

1. HOME → ALARMS to view active alarms
2. ALARM HISTORY to view past events with timestamp and conditions
3. SETPOINTS to verify operating limits
4. UNIT STATUS to view live sensor readings

## Parts Often Needed

| Part | Notes |
|------|-------|
| Refrigerant charge | Common after leaks |
| Condenser fan motor | Replace on high pressure faults |
| Flow switch | Inspect on low pressure and freeze faults |
| Pressure transducer | Check on unexplained pressure readings |

## Jump to Fix

- **Low pressure** → Check chilled water flow → Check refrigerant charge → Inspect evaporator
- **High pressure** → Check condenser coil → Verify all fans running → Check condenser water
- **Freeze protection** → Confirm flow rate → Check pump and valves → Verify setpoints

## When to Call a Pro
Daikin Applied service providers handle refrigerant work, compressor replacement, and control system configuration. Contact Daikin Applied service at 1-877-554-4834.
