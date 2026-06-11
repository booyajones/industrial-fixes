---
title: "ABB ACS580 A0 Fault Code - Causes & Fix"
description: "A0 by itself is not a standard ACS580 fault code. Read the full code and auxiliary text on the keypad to identify the real problem."
pubDatetime: 2026-05-31T11:09:32Z
modDatetime: 2026-05-31T11:09:32Z
author: "James Rutherford"
featured: false
draft: true
tags:
  - vfd
  - abb
money_part: "ABB ACS580 input line fuse kit"
---

## ABB ACS580 A0 Fault Code — What It Means

The ACS580 drive does not use 'A0' as a standalone fault code in ABB's published fault tables. What appears as 'A0' on your display is likely a misread code, a truncated display, or an auxiliary code attached to another fault. ABB identifies faults by the complete code string and the text shown on the keypad or in the fault history. Without the full code, the exact problem cannot be determined.

Common actual faults on the ACS580 include overcurrent (A2B1), DC link undervoltage or DC not charged (A2B4), wiring or earth fault (3181), output phase loss (3381), and STO-related events (5090 or B5A0). Each has specific causes and the drive's event log will show the real code. Check your keypad or use ABB DriveWindow software to read the complete fault code and associated message before attempting any repair.

[Jump to Fix](#fix)

## Common Causes

- **Incomplete fault code reading** The display shows only part of the full fault identifier, so you cannot determine the actual problem without scrolling or checking the fault history.
- **Missing or loose input power** Blown fuse, disconnected phase, or poor terminal connection triggers undervoltage or phase-loss faults that may display truncated codes.
- **Motor cable or motor earth fault** Damaged insulation, incorrect motor wiring, or grounded motor winding causes earth-fault or overcurrent trips.
- **Mechanical overload or binding** Jammed pump, seized bearing, or excessive load current during start trips the drive with an overcurrent fault.
- **STO circuit open or misconfigured** Missing safety jumper, broken safety-chain contact, or STO hardware failure prevents the drive from running and logs an STO fault.
- **Output phase disconnected** One or more motor leads not connected or broken contactor in the motor circuit causes output phase-loss fault.

## Step-by-Step Fix {#fix}

1. **Navigate to the fault log** on the keypad (or connect ABB DriveWindow) and write down the complete fault code, auxiliary code, and fault text exactly as displayed.
2. **Look up the full code** in the ACS580 user manual fault table to confirm the actual fault name and ABB's recommended actions.
3. **Check all three input phases** at the drive terminals with a multimeter and verify all line fuses are intact and all terminal screws are tight.
4. **Inspect the motor cable and motor terminals** for damage, loose connections, correct phasing (U-V-W), and proper star or delta configuration on the motor.
5. **Measure insulation resistance** from each motor phase to ground using a megohmmeter if an earth fault is suspected (motor and cable should read above 1 MΩ to ground).
6. **Check for mechanical load problems** by rotating the shaft by hand (with power off and motor disconnected) to confirm the load moves freely without binding.
7. **If the fault involves STO**, verify the safety jumper or safety-contact loop is closed, all STO terminals are wired per the manual, and parameter group 26 matches your safety configuration.
8. **Clear the fault** using the reset button or cycle drive power after correcting the root cause, then monitor for recurrence during a test run.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB ACS580 input line fuse kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a0-fault-code&k=ABB+ACS580+input+line+fuse+kit&tag=errorcodefixes-20) \| Consult drive nameplate for correct fuse type and amperage if input fuse has blown. |
| Shielded motor cable (VFD-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a0-fault-code&k=Shielded+motor+cable+%28VFD-rated%29&tag=errorcodefixes-20) \| Replace if insulation is damaged or cable fails megohm test to ground. |
| ABB ACS580 control board (OINT) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a0-fault-code&k=ABB+ACS580+control+board+%28OINT%29&tag=errorcodefixes-20) \| Required if STO hardware failure persists after wiring and configuration checks. |

## When to Call a Pro

Call an ABB-authorized service technician if the full fault code cannot be read from the keypad or event log, if the fault returns immediately after correcting wiring and mechanical issues, if insulation tests show a motor winding fault that requires motor teardown, or if the fault involves internal DC-link or gate-driver hardware that is not accessible without opening the drive. ABB recommends contacting your local ABB representative for recurring or unclear faults, and any repair that requires opening the drive enclosure or replacing internal boards should be done by qualified personnel familiar with high-voltage DC bus safety.

## See Also

- [ABB ACS550 EFB1 Fault Code - Causes & Fix](/posts/abb-acs550-efb1-fault-code/)
- [ABB ACS880 Fault 3210 — DC Bus Undervoltage Causes & Fix](/posts/abb-acs880-fault-3210/)
- [ABB VFD Fault 9300 — Causes & Fix](/posts/abb-vfd-fault-9300/)
- [ABB ACS580 A3D0 Fault Code - Causes & Fix](/posts/abb-acs580-a3d0-fault-code/)
