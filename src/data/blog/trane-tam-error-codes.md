---
title: "Trane TAM Air Handler Error Codes — Complete Guide"
description: "Trane TAM air handler error codes: fault codes for TAM7, TAM8, and TAM9 series air handlers with causes and step-by-step fixes."
pubDatetime: 2026-04-22T19:00:00Z
modDatetime: 2026-04-22T19:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - trane
  - air-handler
---

## Trane TAM Air Handler Error Codes — Quick Reference

Trane TAM series air handlers (TAM7, TAM8, TAM9) communicate fault codes via LED flash sequences on the control board and, on communicating systems, through the connected Trane ComfortLink II thermostat. The TAM series works with Trane XL and XR heat pumps and central air conditioning systems. Codes are read by counting blinks: slow blinks = tens digit, fast blinks = ones digit.

| [Flash Code](https://www.amazon.com/s?k=Flash+Code&tag=errorcodefixes-20) | Meaning | Quick Fix |
|------------|---------|-----------|
| 1-1 | System standby / normal operation | No action needed |
| 1-2 | Communication fault (ComfortLink) | Check communication wiring |
| 2-1 | Indoor coil temperature sensor fault | Check NTC sensor; replace if failed |
| 2-2 | Discharge air temperature sensor fault | Inspect duct sensor wiring |
| 3-1 | Blower motor fault — ECM | Check ECM motor connections; test motor |
| 3-2 | Blower motor speed fault | Verify airflow; check static pressure |
| 4-1 | Low-pressure fault (cooling) | Check refrigerant charge; check filter |
| 4-2 | High-pressure fault (cooling) | Check condenser airflow; outdoor coil |
| 5-1 | High-temperature limit fault | Check filter and airflow restrictions |
| 5-2 | Drain pan overflow / float switch | Check condensate drain; clear blockage |
| 6-1 | Electric heat fault (if equipped) | Inspect electric heater strips |
| 6-2 | Electric heat over-temperature | Check heat strip fuse links |
| 7-1 | Low-voltage supply fault | Verify 24VAC transformer; check fuse |
| 8-1 | Control board internal fault | Replace control board |

## Most Common Faults

### 3-1 — Blower Motor (ECM) Fault
TAM series air handlers use Electronically Commutated Motors (ECM) for variable-speed airflow. An ECM fault means the motor failed to start, lost communication with the control board, or has a winding fault. First, check that the motor control plug (usually a 5-pin or 16-pin connector) is fully seated. If the motor is warm and won't spin, the ECM module may have failed — on TAM air handlers the ECM module can often be replaced separately from the motor body.

### 5-2 — Drain Pan Overflow / Float Switch
The TAM series has a safety float switch in the secondary drain pan. When the primary condensate drain clogs and the pan fills, the float switch opens and shuts down the air handler to prevent water damage. Clear the primary drain line using a wet/dry vacuum at the clean-out tee. After draining, pour water into the drain pan to test that the float switch resets properly.

### 4-1 — Low-Pressure Fault (Cooling Mode)
The system pressure is below the low-pressure cutout. Common causes: low refrigerant charge, extremely cold outdoor temperatures during cooling (which shouldn't happen, but a failed check valve can cause this), a restricted metering device (TXV or orifice), or a dirty air filter causing low airflow and freezing the indoor coil. Check the filter first, then have a technician check refrigerant charge.

### 2-1 — Indoor Coil Temperature Sensor Fault
The NTC thermistor clipped to the indoor coil has failed or is reading out of range. Locate the sensor — it's usually clipped to a return bend on the evaporator coil — and check the wiring harness to the control board. Thermistors rarely fail from old age alone; check for physical damage to the wire or sensor body first.

### 1-2 — Communication Fault (ComfortLink II)
On communicating system installations, the TAM air handler communicates with the outdoor unit and thermostat over a two-wire data bus. A 1-2 fault means the communication link has been interrupted. Check the data bus wiring at the TAM's communication terminal block (usually labeled COM1 and COM2). Verify the outdoor unit is powered and its own fault codes are not the root cause.

### 6-2 — Electric Heat Over-Temperature
If the TAM is equipped with electric heat strips, over-temperature faults indicate the thermal fuse links (fusible links) protecting the heater elements have opened. These are one-time protection devices — once they open, they must be replaced. Find the cause of the over-temperature (typically restricted airflow) before replacing the fuse links, or they will fail again immediately.

## When to Call a Pro
Refrigerant-related faults (4-1, 4-2) require a certified HVAC technician for refrigerant diagnosis and charging. ECM motor failures also require a technician to correctly size and program a replacement motor module.

## Related Articles

- [Trane 1 Flash Error Code — Causes & Fix](/posts/trane-1-flash-error-code/)
- [Trane Error Code 126 — Ignition Lockout Fix](/posts/trane-126-error-code/)
- [Trane 2 Flashes Error Code — Causes & Fix](/posts/trane-2-flashes-error-code/)
- [Trane 3 Flashes Error Code — Pressure Switch Fault Fix](/posts/trane-3-flashes-error-code/)
- [Trane 3 Flash Pressure Switch Fault — Detailed Diagnosis Guide](/posts/trane-3-flashes-pressure-switch/)
