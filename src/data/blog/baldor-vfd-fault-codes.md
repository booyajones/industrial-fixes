---
title: "Baldor/ABB VS1 VFD Fault Codes — Complete Guide"
description: "Baldor VS1 and ABB VFD fault codes: all fault codes for Baldor VS1SP, VS1MD, and ABB-based Baldor drives with causes and step-by-step fixes."
pubDatetime: 2026-04-22T19:00:00Z
modDatetime: 2026-04-22T19:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - baldor
  - abb
  - motor-control
---

## Baldor/ABB VS1 VFD Fault Codes — Quick Reference

Baldor Electric (now part of ABB) manufactures the VS1 series of variable frequency drives, which are based on ABB's drive platform. The VS1SP (simple panel) and VS1MD (micro drive) series share fault codes with the ABB ACS300/ACS310/ACS355 family. Faults appear on the drive's display panel.

| Fault Code | Meaning | Common Cause | Quick Fix |
|-----------|---------|-------------|-----------|
| F0001 | Overcurrent | Load too high; short circuit | Check motor wiring; reduce acceleration |
| F0002 | DC Bus Overvoltage | Regen energy; high input voltage | Check input voltage; add braking resistor |
| F0003 | DC Bus Undervoltage | Low input voltage; power dip | Check input voltage; check fuses |
| F0004 | Drive overtemperature | Blocked cooling; ambient too hot | Clean heatsink; improve ventilation |
| F0005 | Motor overtemperature | Motor overloaded; PTC fault | Check motor load; check PTC wiring |
| F0006 | Emergency stop | External E-stop input activated | Check E-stop circuit; reset |
| F0007 | Control board fault | Internal hardware fault | Power cycle; replace if persists |
| F0009 | Underload fault | Load dropped below threshold | Check for broken belt or coupling |
| F0011 | External fault | Digital input configured for external fault | Check external fault input wiring |
| F0013 | Analog input loss | 4–20mA signal lost | Check signal source; check wiring |
| F0014 | Motor stall | Motor not turning at commanded speed | Check motor and mechanical load |
| F0016 | Earth fault (ground fault) | Winding-to-ground insulation fault | Test motor insulation; check wiring |
| F0017 | Motor phase loss | Missing motor output phase | Check U, V, W output wiring |
| F0022 | Parameter CRC fault | Parameter checksum error | Reload parameters from backup |
| F0025 | Input phase loss | Missing input phase | Check L1, L2, L3 input connections |

## Most Common Faults

### F0001 — Overcurrent
The drive's output current exceeded the overcurrent trip threshold. On VS1 drives this is typically 200% of rated current instantaneously. Causes:
- **Acceleration too fast:** Increase the acceleration time parameter (typically P2.1 on VS1SP) — a longer ramp gives the motor more time to accelerate without drawing excessive current
- **Motor winding short:** Disconnect the motor and megger test between each phase and ground — should be >1 MΩ
- **Mechanical jam:** Check if the driven load is seized

### F0004 — Drive Overtemperature
The drive heatsink temperature exceeded the maximum. Baldor VS1 drives require adequate cooling airflow across the heatsink fins. Check:
1. Clear the heatsink fins of dust and debris with compressed air
2. Verify the ambient temperature in the drive enclosure is below 40°C (104°F)
3. Verify there is at least 4 inches of clearance above and below the drive for natural convection, or that forced-air cooling fans are working

### F0016 — Earth / Ground Fault
Current is flowing from a motor phase winding to ground. This is a motor insulation failure. Test the motor: disconnect the motor leads from the drive output terminals (U, V, W). Use a megohmmeter (insulation tester) to test each motor phase to ground — any reading below 1 MΩ at 500VDC indicates failing insulation. If the test fails with the motor disconnected and passes with it connected, the motor cable insulation may be damaged.

### F0002 — DC Bus Overvoltage
When a motor decelerates, it generates energy that flows back into the drive's DC bus. If the deceleration is too fast or the supply voltage is high, the DC bus voltage exceeds the trip point. Fix:
- Increase the deceleration time (parameter for decel time)
- Add an external braking resistor (allows the regenerated energy to be dissipated as heat)
- If supply voltage is high, check the incoming line voltage — should be within ±10% of rated

### F0013 — Analog Input Signal Loss
The 4–20mA or 0–10VDC control signal from a PLC, BAS, or manual setpoint pot has dropped below the minimum expected value. Check:
- The signal source is powered and active
- The wiring between source and drive AI terminal is intact
- The AI signal is at or above 4mA (for 4–20mA systems) or 0V (for 0–10V systems)
- The drive parameter for "analog loss action" (typically configured to fault, warning, or ignore)

## VS1 Drive Fault Reset

Most VS1 faults are reset by pressing the STOP/RESET button on the keypad after the fault condition is corrected. If the fault returns immediately, the root cause has not been resolved. For F0016 (ground fault) and F0025 (input phase loss), do not repeatedly reset — these indicate actual electrical faults that can damage the drive.

## When to Call a Pro
Ground fault (F0016), phase loss (F0025), and control board fault (F0007) require an industrial electrician or drive service technician. Motor megger testing also requires proper insulation test equipment.
