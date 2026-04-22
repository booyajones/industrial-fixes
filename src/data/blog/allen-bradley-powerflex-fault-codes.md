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

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Drive | Meaning | [Common Fix](https://www.amazon.com/s?k=Common%20Fix&tag=errorcodefixe-20) |  |------|-------|---------|-----------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | F002 | 4/40/523 | [Auxiliary input fault](https://www.amazon.com/s?k=Auxiliary%20input%20fault&tag=errorcodefixe-20) | Check enable input wiring |
| [F004](https://www.amazon.com/s?k=F004&tag=errorcodefixe-20) | 4/40/523 | Undervoltage | [Check input power; transformer](https://www.amazon.com/s?k=Check%20input%20power%3B%20transformer&tag=errorcodefixe-20) |  | F005 | [4/40/523](https://www.amazon.com/s?k=4%2F40%2F523&tag=errorcodefixe-20) | Overvoltage | Decel ramp too fast; add braking resistor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | F007 | 4/40/523 | [Motor overload (OL)](https://www.amazon.com/s?k=Motor%20overload%20(OL)&tag=errorcodefixe-20) | Reduce load; check motor current |
| [F012](https://www.amazon.com/s?k=F012&tag=errorcodefixe-20) | 40/523 | HW overcurrent | [Check motor wiring; mechanical jam](https://www.amazon.com/s?k=Check%20motor%20wiring%3B%20mechanical%20jam&tag=errorcodefixe-20) |  | F025 | [40/523](https://www.amazon.com/s?k=40%2F523&tag=errorcodefixe-20) | DPI comm fault | Check HIM or comm module connection | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | F063 | 40/523 | [SW overcurrent](https://www.amazon.com/s?k=SW%20overcurrent&tag=errorcodefixe-20) | Check drive-to-motor wiring |
| [F069](https://www.amazon.com/s?k=F069&tag=errorcodefixe-20) | 40/525 | PI feedback loss | [Check feedback device wiring](https://www.amazon.com/s?k=Check%20feedback%20device%20wiring&tag=errorcodefixe-20) |  | F111 | [40/525](https://www.amazon.com/s?k=40%2F525&tag=errorcodefixe-20) | External fault | Check fault input wiring and source | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Fault 3 | 700/753/755 | [Power loss](https://www.amazon.com/s?k=Power%20loss&tag=errorcodefixe-20) | Check supply voltage |
| [Fault 7](https://www.amazon.com/s?k=Fault%207&tag=errorcodefixe-20) | 700/753/755 | Motor stalled | [Check load; increase stall timeout](https://www.amazon.com/s?k=Check%20load%3B%20increase%20stall%20timeout&tag=errorcodefixe-20) |  | Fault 12 | [700/753/755](https://www.amazon.com/s?k=700%2F753%2F755&tag=errorcodefixe-20) | HW overcurrent | Check wiring; mechanical jam | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Fault 35 | 753/755 | [Comms loss](https://www.amazon.com/s?k=Comms%20loss&tag=errorcodefixe-20) | Check EtherNet/IP or DeviceNet |

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
| [HIM module](https://www.amazon.com/s?k=HIM%20module&tag=errorcodefixe-20) | PowerFlex 4/40: 22-HIM-A3; PF700: 20-HIM-A3 |
| [Dynamic braking resistor](https://www.amazon.com/s?k=Dynamic%20braking%20resistor&tag=errorcodefixe-20) | Size per drive HP; Rockwell catalog or third-party |
| [Contactor / line reactor](https://www.amazon.com/s?k=Contactor%20%2F%20line%20reactor&tag=errorcodefixe-20) | Add if experiencing nuisance undervoltage trips |

## When to Call a Pro
F012 (hardware overcurrent) and any fault accompanied by a burning smell or visible damage to the drive's output stage require qualified drive service technicians. Replacing IGBTs and gate drivers inside a PowerFlex 700 or 755 requires specialized training and tools.
