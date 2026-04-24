---
title: "Wilo Circulator Pump Fault Codes: Complete Guide"
description: "Wilo circulator pump fault codes and error diagnostics. LED indicator codes, fault causes, and technician-level troubleshooting for Wilo pumps."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - pumps
  - wilo
  - hvac
  - industrial
---

# Wilo Circulator Pump Fault Codes

Wilo circulator pumps (Stratos, TOP-S, Yonos, and commercial series) communicate faults via LED indicators and, on advanced models, a display panel. Wilo pumps are widely used in HVAC hydronic systems, district heating, and industrial circulation.

## Wilo Stratos/TOP Series Fault Code Table

| LED/Code | Fault Description | Common Cause | Action |
|----------|------------------|--------------|--------|
| Red LED steady | Fault/lockout | Overtemperature, blocked impeller | Check fluid temp, clear blockage |
| Red LED flashing | Warning | Fault present but pump running | Read fault via Wilo-Net or display |
| E01 | Blocked pump | Impeller locked or air-locked | Vent system, check for debris |
| E02 | Overtemperature | Fluid temp too high | Check system temp, verify bypass |
| E03 | Dry run | No fluid detected | Fill and vent system |
| E04 | Undervoltage | Supply below minimum | Check power supply |
| E05 | Overvoltage | Supply above maximum | Check power supply |
| E06 | Motor overload | Excessive load or stall | Check mechanical load |
| E07 | Electronic fault | Internal board fault | Contact Wilo service |
| E10 | Communication fault | Wilo-Net or BACnet/Modbus error | Check network wiring |
| E11 | Sensor fault | Differential pressure sensor failure | Check sensor connections |
| E12 | Under-flow | Flow below minimum setpoint | Check system for closed valves |

## Most Common Wilo Pump Faults

### E01 ΓÇö Blocked Pump
Wilo circulators are maintenance-free, but system contamination can jam the impeller. Shut off the pump, isolate with service valves, and remove the motor head from the pump body. Check for debris in the impeller chamber. Also check for air lock ΓÇö purge the pump air vent screw (typically on top of pump body) while system is running.

### E02 ΓÇö Overtemperature
Wilo Stratos pumps are rated to 95┬░C fluid temperature. If system temperature exceeds rating, the pump locks out. Check the system boiler or heat source temperature controller. Also verify the pump is not installed in an orientation where it traps heat.

### E03 ΓÇö Dry Run
Dry run protection prevents pump damage when the system runs low on water. Check system fill pressure (minimum 12 PSI for most closed-loop hydronic systems). Check backflow preventer fill valve. If system recently drained, re-fill and bleed air from highest points.

### E10 ΓÇö Communication Fault
Wilo pumps with Wilo-Net, BACnet, or Modbus connectivity will fault if the building automation system (BAS) loses communication. Check network wiring at the pump terminal block and verify BAS controller is online.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Impeller assembly | [Amazon](https://www.amazon.com/s?k=Impeller+assembly&tag=errorcodefixes-20) \| Match pump model and impeller diameter |
| Electronic insert (motor head) | [Amazon](https://www.amazon.com/s?k=Electronic+insert+%28motor+head%29&tag=errorcodefixes-20) \| Full replacement motor assembly |
| Wilo-Net gateway | [Amazon](https://www.amazon.com/s?k=Wilo-Net+gateway&tag=errorcodefixes-20) \| For BAS integration |
| Pressure sensor | [Amazon](https://www.amazon.com/s?k=Pressure+sensor&tag=errorcodefixes-20) \| Differential pressure transducer for variable speed control |
| Service kit | [Amazon](https://www.amazon.com/s?k=Service+kit&tag=errorcodefixes-20) \| Seal and O-ring set |
> **Pro tip:** Wilo Stratos and high-efficiency models have a built-in energy monitoring function. Track pump power consumption via the display or Wilo-Net ΓÇö a sudden increase in power often indicates a developing fault (worn bearing, increased system resistance) before an alarm occurs.
