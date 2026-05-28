---
title: "Trane XR15 Heat Pump Error Codes — Complete Guide"
description: "Trane XR15 heat pump error codes: all fault codes, flash sequences, causes, and fixes for the Trane XR15 two-stage heat pump."
pubDatetime: 2026-04-22T19:00:00Z
modDatetime: 2026-04-22T19:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - trane
  - heat-pump
---

## Trane XR15 Heat Pump Error Codes — Quick Reference

The Trane XR15 is a two-stage heat pump using the Climatuff compressor. Fault codes are displayed via LED flash sequences on the integrated control board inside the outdoor unit. Open the electrical panel access cover to view the LED. Codes are read as: slow blinks = tens digit, pause, fast blinks = ones digit.

| [Flash Code](https://www.amazon.com/s?ascsubtag=ecf-trane-xr15-error-codes&k=Flash+Code&tag=errorcodefixes-20) | Meaning | Quick Fix |
|------------|---------|-----------|
| [1 flash](https://www.amazon.com/s?ascsubtag=ecf-trane-xr15-error-codes&k=1+flash&tag=errorcodefixes-20) | System normal | No fault |
| 2-1 | Discharge line temperature sensor fault | Check discharge sensor wiring |
| 2-2 | Outdoor ambient temperature sensor fault | Inspect outdoor sensor and connections |
| 3-1 | Low-pressure fault | Check refrigerant; verify airflow |
| 3-2 | High-pressure fault | Check outdoor fan; clean coil |
| 4-1 | Compressor start fault | Check capacitor; verify voltage |
| 4-2 | Compressor thermal overload | Compressor overheated — allow cooldown |
| 5-1 | Outdoor fan motor fault | Check fan motor; check capacitor |
| 5-2 | Defrost fault | Check defrost board and sensor |
| 6-1 | Low ambient lockout | Normal below 0°F — add low-ambient kit |
| 6-2 | High-discharge temperature protection | Refrigerant charge or airflow issue |
| 7-1 | Communication fault (if connected to communicating system) | Check data bus wiring |
| 8-1 | Control board fault | Replace control board |

## Most Common Faults

### 3-1 — Low-Pressure Fault
The system refrigerant pressure dropped below the low-pressure cutout setting. In heating mode, this typically points to a refrigerant leak or, in very cold weather, a malfunctioning defrost cycle causing ice buildup on the outdoor coil. In cooling mode, low pressure usually indicates low refrigerant charge or restricted airflow across the indoor coil (dirty filter). Have a technician check refrigerant charge — do not add refrigerant without finding and fixing any leak first.

### 3-2 — High-Pressure Fault
System pressure exceeded the high-pressure cutout. In cooling mode, this is almost always caused by a blocked outdoor coil, failed outdoor fan motor, or a refrigerant overcharge. Clean the outdoor coil fins with a coil cleaner and garden hose. Verify the outdoor fan is spinning when the compressor is running. In heating mode, high-pressure faults can indicate a failed reversing valve.

### 4-1 — Compressor Start Fault
The compressor failed to start within the timeout period. Check the run and start capacitors first — the XR15 uses a dual-round capacitor (compressor + fan). A failed capacitor is the most common cause. Test with a capacitor meter; replace the entire dual capacitor if either section is out of range. Also verify incoming voltage — the XR15 requires 208–240VAC and will fault if voltage is below 197VAC.

### 5-2 — Defrost Fault
The XR15 uses a demand defrost control that monitors defrost termination time and outdoor coil temperature. A defrost fault means the defrost cycle didn't complete properly or the defrost sensor is faulty. Check the defrost sensor (clipped to the outdoor coil — similar to an NTC thermistor) for physical damage or disconnection. Test sensor resistance at known temperature to verify it is within spec.

### 5-1 — Outdoor Fan Motor Fault
The outdoor fan motor is not running or is running backward. Check the dual capacitor (fan section). If the capacitor is good, check the motor windings with an ohmmeter — open windings indicate a failed motor. The XR15 fan motor is typically a PSC type (not ECM) and is available as a direct replacement from Trane or HVAC supply houses.

## XR15 Refrigerant and Charge Notes

- The XR15 uses R-410A refrigerant
- Proper charge is critical — the XR15 is factory-charged for 15 feet of refrigerant line
- Add or remove charge for longer or shorter line sets per the Trane charging chart
- Low charge symptoms: low-pressure faults, reduced capacity, ice on indoor coil

## When to Call a Pro
All refrigerant-related faults (3-1, 3-2, 6-2) require a certified HVAC technician with EPA Section 608 certification for refrigerant handling.

## Related Articles

- [Trane 1 Flash Error Code — Causes & Fix](/posts/trane-1-flash-error-code/)
- [Trane Error Code 126 — Ignition Lockout Fix](/posts/trane-126-error-code/)
- [Trane 2 Flashes Error Code — Causes & Fix](/posts/trane-2-flashes-error-code/)
- [Trane 3 Flashes Error Code — Pressure Switch Fault Fix](/posts/trane-3-flashes-error-code/)
- [Trane 3 Flash Pressure Switch Fault — Detailed Diagnosis Guide](/posts/trane-3-flashes-pressure-switch/)

## See Also

- [Trane CenTraVac Chiller Fault Codes — Common Faults Guide](/posts/trane-centravac-fault-codes/)
- [Trane XV80 Furnace Error Codes — Flash Code Diagnostic Guide](/posts/trane-xv80-error-codes/)
- [Trane 3 Flashes Error Code — Pressure Switch Fault Fix](/posts/trane-3-flashes-error-code/)
- [Trane XV20i Error Code 79: Communicating Thermostat Fault Fix](/posts/trane-error-79-xv20i/)
