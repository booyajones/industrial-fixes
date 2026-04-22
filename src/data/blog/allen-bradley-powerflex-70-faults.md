---
title: "Allen-Bradley PowerFlex 70 Fault Codes: Complete Guide"
description: "Allen-Bradley PowerFlex 70 VFD fault codes and diagnostics. F-codes, causes, and technician-level troubleshooting for PF70 drives."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - allen-bradley
  - industrial
  - motor-control
---

# Allen-Bradley PowerFlex 70 Fault Codes

The Allen-Bradley PowerFlex 70 is a mid-range VFD rated 0.37–448 kW. Fault codes display on the HIM (Human Interface Module) as fault numbers. The PowerFlex 70 uses a similar fault structure to the PF700 and PF755 but with its own parameters (accessible via Connected Components Workbench or DriveExplorer).

## PowerFlex 70 Fault Code Table

| Code | Fault Description | Common Cause | Action |
|------|------------------|--------------|--------|
| F2 | Auxiliary input | External fault from TB6 | Check external fault wiring |
| F3 | Power loss | Input power interruption | Check supply voltage |
| F4 | Undervoltage | Low supply voltage | Verify input voltage |
| F5 | Overvoltage | Regenerative energy or voltage spike | Add brake resistor |
| F6 | Motor stall | Motor stalled or overloaded | Check mechanical load |
| F7 | Motor overcurrent | Motor overload or winding fault | Check motor amps and winding |
| F8 | Heatsink overtemperature | High ambient or blocked cooling | Clean fins, check fan |
| F12 | HW overcurrent | Hardware overcurrent (fast) | Check for short circuit |
| F13 | Ground fault | Motor winding or cable ground | Megger test motor |
| F15 | Load loss | Belt broken or load disconnect | Check mechanical connection |
| F23 | Auto tune fault | Motor data entry error | Verify motor nameplate data |
| F25 | Drive overtemperature | Internal temperature high | Check cooling system |
| F33 | Start inhibit | Safety input or logic inhibit | Check digital input wiring |
| F38 | Phase loss | Output phase missing | Check motor connections |
| F63 | Software fault | Parameter or firmware issue | Reset and reload parameters |
| F111 | Internal fault | Hardware fault | Contact Rockwell support |

## Most Common PowerFlex 70 Faults

### F7 — Motor Overcurrent
Check motor nameplate FLA vs. parameter P032 (motor NP amps). Verify correct motor overload setting. Check motor for single-phasing, winding imbalance, or locked rotor condition. Increase accel time (parameter A051).

### F8 — Heatsink Overtemperature
The PowerFlex 70 requires 3-inch clearance on all sides. Clean fins with compressed air — debris accumulates on the cooling fins rapidly in industrial environments. Check internal cooling fan (starts automatically with drive power).

### F13 — Ground Fault
Disconnect motor leads at drive output terminals. Megger test each conductor to ground at 1000 VDC. Reading below 1 MΩ indicates a failed cable or motor winding. Also check cable tray for damaged insulation.

### F5 — Overvoltage
Pumping applications with fast deceleration cause motor regeneration. Increase deceleration ramp time (parameter A052). If regeneration is unavoidable, add a dynamic braking resistor to the brake resistor terminals.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| HIM module | Plug-in display — model 20-HIM-A3 is most common |
| Cooling fan | Match PowerFlex 70 frame size |
| Input fuses | Class J or CC — match ampere rating |
| Brake resistor | Match ohm and watt rating to drive |

> **Pro tip:** PowerFlex 70 stores fault queue (F01–F08 parameters in the fault log group). Access via HIM: DIAGNOSTICS → FAULT LOG. Always review the full fault queue — a single event often produces multiple faults in sequence that tell the root cause story.
