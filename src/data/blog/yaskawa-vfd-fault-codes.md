---
title: "Yaskawa VFD Fault Codes — Complete Reference (V1000, A1000, GA700)"
description: "Yaskawa VFD fault codes: all major faults for V1000, A1000, J1000, and GA700 drives including OC, OV, UV, GF, and OH faults."
pubDatetime: 2026-04-22T16:00:00Z
modDatetime: 2026-04-22T16:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
---

## Yaskawa VFD Fault Codes — Quick Reference

Yaskawa drives (V1000, J1000, A1000, GA700, P1000, Z1000 series) display fault codes as abbreviated text on the LED keypad or LCD operator panel. Faults (FLT) stop the motor immediately; alarms (ALM) allow continued operation with reduced performance. Access the fault history via the operator panel diagnostic menu.

| Code | Meaning | Common Fix |
|------|---------|-----------|
| oC | Overcurrent | Check motor; extend accel time |
| ov | Overvoltage | Extend decel time; add braking resistor |
| Uv1 | DC bus undervoltage | Check input power supply |
| GF | Ground fault | Megger motor and cable |
| oH | Drive overtemperature | Clean cooling; check ambient temp |
| oL1 | Motor overload | Check motor FLA parameter; reduce load |
| oL2 | Drive overload | Reduce load or use larger drive |
| SC | Short circuit | Check motor winding and cable |
| PF | Power supply fault | Check input voltage quality |
| LF | Output phase loss | Check motor connection; cable |
| CF | Control fault | Check control board; reset |
| bb | Base block (safe torque off) | Check STO/SFS input wiring |
| Er | EEPROM fault | Cycle power; replace control board |
| GA700: CPF | Control power fault | Check 24V control power supply |

## Most Common Codes

### oC: Overcurrent
The output current exceeded the drive's trip level (usually 200% of rated current). Common causes: mechanical jam/stall, acceleration ramp too fast for the load inertia, motor parameters incorrectly set, or a motor/cable insulation fault that's not quite a ground fault.

**Fix:** (1) Verify C1-01 (acceleration time) is not too short. (2) Check motor FLA — set E2-01 (Motor Rated Current) to match the motor nameplate. (3) Check for mechanical binding. (4) If oC trips at startup, suspect undersized cables or motor terminal box wiring issues.

### ov: Overvoltage
DC bus exceeded trip level due to regenerative energy. The GA700 has built-in flux braking; the V1000 and A1000 require either increased decel time (C1-02) or an external braking resistor. Enable stall prevention during deceleration (L3-04) if overvoltage is intermittent.

### Uv1: Undervoltage
Input voltage too low. On 480V Yaskawa drives, DC bus undervoltage trips at approximately 190V DC (about 268V AC input). Check: (1) all three input phases are present and symmetrical, (2) input fuses/breaker is not open, (3) supply voltage is within spec (+10%/-15% of drive rating).

### GF: Ground Fault
A current path to ground was detected in the output circuit. This is a serious fault. Before restarting: (1) disconnect the motor from the drive, (2) megger test the motor phases to ground at 500V DC — should be >1 MΩ, (3) megger test the motor cable. Also check the drive output terminals for physical damage. If motor and cable are clean, the fault may be in the drive's output current sensors.

### oH: Overtemperature
The heatsink temperature exceeded the limit (usually 90–105°C depending on model). On V1000 drives, the cooling fan is automatic (runs when hot) — check that it spins. On A1000 and GA700, the fan is continuous — if it's failed, temperature rises steadily. Clear heatsink fins with compressed air annually.

### LF: Output Phase Loss
One motor phase is missing or has very high impedance. Check: motor cable for a broken conductor, terminal box connections at the motor (loose lug), and the drive's output terminals. LF can also trip if the motor is disconnected while the drive is running.

### bb: Base Block
The Base Block (safe torque off) input has been activated. The drive will not produce output while bb is active. Check: (1) STO/SFS terminals — they should have +24V when run is commanded, (2) safety relay wiring if a safety circuit is installed, (3) jumpers between SFS and SCF if no safety circuit is used (per the drive startup guide).

## Clearing Faults

- **Manual reset:** Press RESET key on the operator panel.
- **Digital input reset:** Configure a digital input for Fault Reset (H1-XX = 14).
- **Auto-reset:** Configure L5-01 (Number of Auto Restarts) and L5-02 (auto restart fault select).

## Parts Often Needed

| Part | Notes |
|------|-------|
| Braking resistor | [Amazon](https://www.amazon.com/s?k=Braking+resistor&tag=errorcodefixes-20) \| Yaskawa ERF or ERV series, sized per drive catalog |
| Cooling fan | [Amazon](https://www.amazon.com/s?k=Cooling+fan&tag=errorcodefixes-20) \| Drive-specific; V1000: YPJP31-B fan assembly |
| Control power fuse | [Amazon](https://www.amazon.com/s?k=Control+power+fuse&tag=errorcodefixes-20) \| 2A time-lag, model-specific |
## When to Call a Pro
GF (ground fault) and SC (short circuit) faults that persist after checking the motor and cable indicate a failed drive output stage. IGBT replacement in Yaskawa drives requires authorized service.

## Related Articles

- [Yaskawa A1000 OC Fault — Overcurrent](/posts/yaskawa-a1000-fault-oc/)
- [Yaskawa A1000 Fault UV1, DC Bus Undervoltage Causes & Fix](/posts/yaskawa-a1000-fault-uv1/)
- [Yaskawa A1000 Fault Code OC — Overcurrent Diagnosis & Fix](/posts/yaskawa-a1000-oc-fault-code/)
- [Yaskawa GA700 OC Fault — Overcurrent Fix](/posts/yaskawa-ga700-fault-oc/)
- [Yaskawa GA700 Fault UV1 — Main Circuit Undervoltage Causes & Fix](/posts/yaskawa-ga700-fault-uv1/)
