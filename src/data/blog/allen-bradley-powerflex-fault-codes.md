---
title: "Allen Bradley PowerFlex Fault Codes — Complete Reference"
description: "Allen Bradley PowerFlex fault codes: all F and fault number codes for PowerFlex 4, 40, 523, 525, 700, 753, and 755 drives."
pubDatetime: 2026-04-22T16:00:00Z
modDatetime: 2026-04-22T16:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - allen-bradley
---

## Allen Bradley PowerFlex Fault Codes — Quick Reference

Allen Bradley PowerFlex drives display fault codes on the integral keypad or HIM (Human Interface Module). The fault code format varies by drive family: PowerFlex 4/40 use F-prefix codes; PowerFlex 523/525 use F or numeric codes; PowerFlex 700/753/755 use numeric fault codes accessible via the keypad or DriveExplorer/Studio 5000 software.

| Code | Drive | Meaning | Common Fix |
|------|-------|---------|-----------|
| F002 | 4/40/523 | Auxiliary input fault | Check enable input wiring |
| F004 | 4/40/523 | Undervoltage | Check input power; transformer |
| F005 | 4/40/523 | Overvoltage | Decel ramp too fast; add braking resistor |
| F007 | 4/40/523 | Motor overload (OL) | Reduce load; check motor current |
| F012 | 40/523 | HW overcurrent | Check motor wiring; mechanical jam |
| F025 | 40/523 | DPI comm fault | Check HIM or comm module connection |
| F063 | 40/523 | SW overcurrent | Check drive-to-motor wiring |
| F069 | 40/525 | PI feedback loss | Check feedback device wiring |
| F111 | 40/525 | External fault | Check fault input wiring and source |
| Fault 3 | 700/753/755 | Power loss | Check supply voltage |
| Fault 7 | 700/753/755 | Motor stalled | Check load; increase stall timeout |
| Fault 12 | 700/753/755 | HW overcurrent | Check wiring; mechanical jam |
| Fault 35 | 753/755 | Comms loss | Check EtherNet/IP or DeviceNet |

## Most Common Codes

### F007 / Fault 7: Motor Overload / Motor Stalled
The drive's electronic overload (E-OL) tripped because the motor drew more current than its programmed limit for too long. First check: Is the motor actually stalled by a mechanical jam? Second: Is the motor FLA (Full Load Amps) programmed correctly in the drive? An incorrectly programmed FLA setting (too low) causes nuisance overload trips.

**To check FLA programming on PowerFlex 40:** Navigate to P031 (Motor NP FLA) and verify it matches the motor nameplate FLA. Adjust if needed.

**To check FLA programming on PowerFlex 755:** In Studio 5000, find parameter 28 (Motor NP FLA) in the Motor Control group.

### F004 / Fault 3: Undervoltage / Power Loss
Input voltage dropped below the minimum threshold during operation. Common causes: a weak utility feed, a transformer undersized for the load, or a long run of undersized input wiring with voltage drop. Measure incoming voltage at the drive's L1/L2/L3 terminals under load. On 480V drives, minimum is typically 342V (480 × 0.9 − 10%).

### F005: Overvoltage
The DC bus voltage exceeded its limit. Usually caused by regenerative energy during fast deceleration. Solutions: (1) extend the deceleration time (parameter A441 on PF40, parameter 535 on PF700), (2) enable the built-in DC bus regulation if available, (3) add a dynamic braking resistor for high-inertia loads.

### F012: Hardware Overcurrent
An instantaneous overcurrent condition tripped the drive. This is different from F007 (slow overload) — F012 is a fast peak-current trip. Causes: a motor winding shorted to ground, a phase-to-phase short in the motor cable, a seized bearing causing locked-rotor current, or a failed IGBT in the drive output. Use a megger (insulation resistance tester) to check the motor and cable before re-energizing.

### F025: DPI Communication Fault
The DPI port (which connects the keypad or HIM module) has lost communication. On PowerFlex 4/40 drives, this often occurs when the HIM cover is vibrating loose from the drive door. Re-seat the HIM firmly onto the DPI port. If the fault persists without a HIM installed, check parameter 190 (DPI Fault Select) — if set to "Fault," the drive faults when no HIM is present.

### Fault 35: Communication Loss (PowerFlex 753/755)
The drive lost communication with the EtherNet/IP network or I/O scanner. Check: (1) Ethernet cable connection at the drive's embedded EtherNet/IP port, (2) IP address configuration (verify in Studio 5000), (3) whether the PLC is running and the CIP connection is established. Fault 35 commonly occurs after a PLC reboot if the drive's connection wasn't set as "Configurable."

## Clearing Faults

- **Manual clear:** Press STOP key three times on PowerFlex 4/40; press the fault clear button on PF700/753/755 HIM.
- **Auto-reset:** Configure parameter 194 (Auto Rstrt Tries) to attempt automatic restarts after transient faults.
- **Parameter:** On PF40, set A094 (Fault Clear) to 1 to clear via parameter write.

## Parts Often Needed

| Part | Notes |
|------|-------|
| HIM module | PowerFlex 4/40: 22-HIM-A3; PF700: 20-HIM-A3 |
| Dynamic braking resistor | Size per drive HP; Rockwell catalog or third-party |
| Contactor / line reactor | Add if experiencing nuisance undervoltage trips |

## When to Call a Pro
F012 (hardware overcurrent) and any fault accompanied by a burning smell or visible damage to the drive's output stage require qualified drive service technicians. Replacing IGBTs and gate drivers inside a PowerFlex 700 or 755 requires specialized training and tools.
