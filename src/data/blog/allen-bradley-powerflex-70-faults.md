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

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Fault Description | Common Cause | [Action](https://www.amazon.com/s?k=Action&tag=errorcodefixe-20) |  |------|------------------|--------------|--------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | F2 | Auxiliary input | [External fault from TB6](https://www.amazon.com/s?k=External%20fault%20from%20TB6&tag=errorcodefixe-20) | Check external fault wiring |
| [F3](https://www.amazon.com/s?k=F3&tag=errorcodefixe-20) | Power loss | Input power interruption | [Check supply voltage](https://www.amazon.com/s?k=Check%20supply%20voltage&tag=errorcodefixe-20) |  | F4 | [Undervoltage](https://www.amazon.com/s?k=Undervoltage&tag=errorcodefixe-20) | Low supply voltage | Verify input voltage | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | F5 | Overvoltage | [Regenerative energy or voltage spike](https://www.amazon.com/s?k=Regenerative%20energy%20or%20voltage%20spike&tag=errorcodefixe-20) | Add brake resistor |
| [F6](https://www.amazon.com/s?k=F6&tag=errorcodefixe-20) | Motor stall | Motor stalled or overloaded | [Check mechanical load](https://www.amazon.com/s?k=Check%20mechanical%20load&tag=errorcodefixe-20) |  | F7 | [Motor overcurrent](https://www.amazon.com/s?k=Motor%20overcurrent&tag=errorcodefixe-20) | Motor overload or winding fault | Check motor amps and winding | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | F8 | Heatsink overtemperature | [High ambient or blocked cooling](https://www.amazon.com/s?k=High%20ambient%20or%20blocked%20cooling&tag=errorcodefixe-20) | Clean fins, check fan |
| [F12](https://www.amazon.com/s?k=F12&tag=errorcodefixe-20) | HW overcurrent | Hardware overcurrent (fast) | [Check for short circuit](https://www.amazon.com/s?k=Check%20for%20short%20circuit&tag=errorcodefixe-20) |  | F13 | [Ground fault](https://www.amazon.com/s?k=Ground%20fault&tag=errorcodefixe-20) | Motor winding or cable ground | Megger test motor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | F15 | Load loss | [Belt broken or load disconnect](https://www.amazon.com/s?k=Belt%20broken%20or%20load%20disconnect&tag=errorcodefixe-20) | Check mechanical connection |
| [F23](https://www.amazon.com/s?k=F23&tag=errorcodefixe-20) | Auto tune fault | Motor data entry error | [Verify motor nameplate data](https://www.amazon.com/s?k=Verify%20motor%20nameplate%20data&tag=errorcodefixe-20) |  | F25 | [Drive overtemperature](https://www.amazon.com/s?k=Drive%20overtemperature&tag=errorcodefixe-20) | Internal temperature high | Check cooling system | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | F33 | Start inhibit | [Safety input or logic inhibit](https://www.amazon.com/s?k=Safety%20input%20or%20logic%20inhibit&tag=errorcodefixe-20) | Check digital input wiring |
| [F38](https://www.amazon.com/s?k=F38&tag=errorcodefixe-20) | Phase loss | Output phase missing | [Check motor connections](https://www.amazon.com/s?k=Check%20motor%20connections&tag=errorcodefixe-20) |  | F63 | [Software fault](https://www.amazon.com/s?k=Software%20fault&tag=errorcodefixe-20) | Parameter or firmware issue | Reset and reload parameters | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | F111 | Internal fault | [Hardware fault](https://www.amazon.com/s?k=Hardware%20fault&tag=errorcodefixe-20) | Contact Rockwell support |

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
| [HIM module](https://www.amazon.com/s?k=HIM%20module&tag=errorcodefixe-20) | Plug-in display — model 20-HIM-A3 is most common |
| [Cooling fan](https://www.amazon.com/s?k=Cooling%20fan&tag=errorcodefixe-20) | Match PowerFlex 70 frame size |
| [Input fuses](https://www.amazon.com/s?k=Input%20fuses&tag=errorcodefixe-20) | Class J or CC — match ampere rating |
| [Brake resistor](https://www.amazon.com/s?k=Brake%20resistor&tag=errorcodefixe-20) | Match ohm and watt rating to drive |

> **Pro tip:** PowerFlex 70 stores fault queue (F01–F08 parameters in the fault log group). Access via HIM: DIAGNOSTICS → FAULT LOG. Always review the full fault queue — a single event often produces multiple faults in sequence that tell the root cause story.
