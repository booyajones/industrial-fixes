---
title: "Allen-Bradley PowerFlex 4M Fault Codes — F2, F4, F5, F7, F12 Fix Guide"
author: "Industrial Error Code Fixes"
pubDatetime: 2026-04-24T22:20:00Z
modDatetime: 2026-04-24T22:20:00Z
slug: allen-bradley-powerflex-4m-fault-codes
featured: false
draft: false
tags:
  - allen-bradley
  - powerflex
  - vfd
  - industrial
  - fault-codes
description: "Allen-Bradley PowerFlex 4M fault codes explained — F2 aux input, F4 undervoltage, F5 overvoltage, F7 motor overtemp, F12 HW overcurrent. Step-by-step fixes and parts table for the 22A drive."
---

## Allen-Bradley PowerFlex 4M (Catalog 22A) Fault Codes

The Allen-Bradley PowerFlex 4M (catalog prefix **22A**) is a compact, low-cost variable frequency drive produced by Rockwell Automation. It is one of the most widely deployed OEM drives in North America, used in conveyors, pumps, fans, packaging machinery, material handling, and HVAC equipment. Power ranges from 0.2 to 11 kW (0.25 to 15 HP) in 120V, 240V, and 480V configurations. When a fault occurs, the drive's display shows an **F** followed by a number (e.g., **F 5**) and the drive coasts the motor to a stop.

The PowerFlex 4M is closely related to the PowerFlex 4 (catalog 22F) and shares similar fault codes, but the 4M includes additional features such as an integral EMC filter option and a full numeric keypad. Most faults can be cleared by pressing the **Stop/Reset** key or cycling the **Enable** input; however, persistent faults require diagnosing and eliminating the root cause.

[Jump to Fix](#step-by-step-fix)

## PowerFlex 4M Fault Code Quick Reference

| Fault | Name | Description |
|-------|------|-------------|
| F 2 | Auxiliary Input | The digital input configured as "External Fault" or "Auxiliary" was activated |
| F 3 | Power Loss | Control board lost power during run — input voltage drop or control power failure |
| F 4 | Under Voltage | DC bus below the minimum threshold (usually 299 VDC on a 480V drive) |
| F 5 | Over Voltage | DC bus exceeded maximum (usually 810 VDC on a 480V drive) — regenerative load |
| F 6 | Motor Stall | Motor stall detection: current exceeded stall current limit for longer than stall time |
| F 7 | Motor Overtemp | Motor thermistor (PTC) input exceeded threshold; or modeled motor overtemp without thermistor |
| F 8 | Heatsink OT | Drive heatsink temperature exceeded the maximum limit (typically 100°C) |
| F 12 | HW Overcurrent | Hardware overcurrent — output current exceeded instantaneous trip threshold |
| F 13 | Ground Fault | Ground current detected on output (asymmetric current in phases) |
| F 33 | Auto Restart | Maximum auto restart attempts (P046) exceeded without successful recovery |
| F 38 | Phase-to-Phase Short | Two output phases shorted — motor cable or motor fault |
| F 63 | SW Overcurrent (I/O) | Digital output transistor overcurrent |

## Common Causes

- **F 5 (overvoltage)** — The most common fault on PowerFlex 4M drives connected to pump or fan loads. When the drive decelerates a high-inertia load, the motor becomes a generator and pushes energy back into the DC bus. The drive trips F5 before the bus capacitors are damaged. Solution is almost always to **increase the deceleration time** (parameter P034).
- **F 12 (HW overcurrent)** — Triggered by an instantaneous current spike above 300% of drive rated current. Common causes: motor winding short, phase-to-phase short in the cable, locked rotor (mechanical jam), or a failed output IGBT. If F12 trips at the instant of start, suspect motor or cable fault. If it trips during acceleration, increase accel time (P033) or check for mechanical binding.
- **F 7 (motor overtemp)** — If a thermistor (PTC or NTC) is wired to the motor temp input (Terminals 25-26), the drive monitors it and trips F7 when the motor gets too hot. If no thermistor is connected, the drive uses a thermal model based on current and speed. Common causes: motor running continuously above service factor, inadequate motor ventilation (especially in constant-torque variable-speed applications), or incorrect motor data in parameters.
- **F 4 (undervoltage)** — Input supply voltage is too low, there is a momentary power sag from upstream equipment starting, or the main circuit fuse has blown. Particularly common in 120V input models during heavy load starts.
- **F 8 (heatsink overtemp)** — Drive is installed in an enclosure without adequate ventilation, the ambient temperature exceeds 50°C, or the mounting orientation is incorrect (the 4M must be mounted vertically). Also caused by a failed internal cooling fan on larger frame sizes.
- **F 2 (auxiliary input)** — A digital input configured as an external fault has been activated. This is a design-intentional fault used to signal upstream process alarms (high temperature, overflow, E-stop, etc.) to the drive. Check whatever equipment monitors the input wired to that terminal.

## Step-by-Step Fix {#step-by-step-fix}

1. **Clear the fault.** Press **Stop/Reset** on the keypad. If the fault does not clear, power cycle the drive (remove and restore input power). If the fault re-appears immediately, there is an active fault condition that must be resolved before the drive will run.

2. **Check parameter P049 (fault queue).** Navigate to P049 — this stores the last 8 faults. Review the fault history to determine if this is a new fault or a recurring pattern. Recurring F12 with no obvious cause often points to an intermittent motor cable problem.

3. **For F5 (overvoltage):**
   - Increase deceleration time: navigate to **P034** (Decel Time 1) and increase the value (e.g., from 5 seconds to 20 seconds).
   - If the load demands very fast deceleration, add a **dynamic braking resistor** to the drive's BR+/BR– terminals (only available on drives with the braking option — check catalog number suffix for "B").
   - Check parameter **A090** (DC Bus Voltage Limit) — reducing this value makes the drive begin ramp extension sooner during decel.

4. **For F12 (HW overcurrent):**
   - **Disconnect the motor cable** from the drive output terminals (T1/U, T2/V, T3/W). If F12 clears and the drive runs at the set frequency without a connected motor, the fault is in the motor or motor cable.
   - With the motor disconnected, use a 500V megohm tester to check each motor phase to ground and phase-to-phase. Readings below 1 MΩ indicate insulation breakdown.
   - If the motor tests clean, the fault may be in the drive output stage (IGBT). Do not attempt to repair the output stage — drive replacement is required.
   - Also verify the load is not mechanically jammed. Manually rotate the motor or load shaft to confirm it turns freely.

5. **For F7 (motor overtemp):**
   - If a thermistor is connected (parameters **A071** and **A072** configure the thermistor response), verify the thermistor wiring at terminals 25 and 26. An open thermistor reads maximum resistance — the drive may interpret this as overtemp.
   - Verify the motor is operating within its service factor. Use parameter **d003** (output current) to monitor the drive's actual output current during the application cycle.
   - Check motor ventilation — totally enclosed fan-cooled (TEFC) motors running at low speed may not have adequate cooling. A separately powered cooling blower may be needed for constant-torque variable-speed applications below 30 Hz.

6. **For F4 (undervoltage):**
   - Measure the input line voltage at the drive input terminals **R, S, T** (or **L1, L2** for single-phase) while the load is running. Compare to the drive's rated input voltage range.
   - Check the input line fuses — replace any that are blown.
   - If line voltage is correct and fuses are good, verify that parameter **b004** (motor NP volts) is set correctly — the drive uses this for internal calculations.

7. **For F8 (heatsink overtemp):**
   - Power down, allow the drive to cool for 30 minutes, and check the internal fan (on frame C drives and above). The fan should spin freely and start immediately when power is applied.
   - Verify the drive is mounted vertically with at least 50 mm clearance above and below.
   - Check the enclosure temperature. If the ambient inside the panel exceeds 50°C, the drive must be derated or the panel must be cooled.

8. **For F2 (auxiliary input):**
   - Navigate to **P036** (digital input functions) to identify which input terminal is configured as the "External Fault" input.
   - Trace the wiring from that input terminal to the field device that drives it.
   - Check whether the fault is a real process alarm (overfill, high temp, etc.) or a nuisance trip from a wiring issue (floating input picking up noise). If no device is connected to the input, either wire a jumper to the input or reconfigure it to an unused function.

## Parts Often Needed {#parts-often-needed}

| Part | Description | Typical Cost | Where to Buy |
|------|-------------|--------------|--------------|
| PowerFlex 4M replacement drive (22A-D2P3N104) | 1 HP 480V 3-phase (example) — select by catalog number | $300–$800 | [Amazon](https://www.amazon.com/s?i=industrial&k=Allen-Bradley+PowerFlex+4M+22A+drive+replacement&tag=errorcodefixes-20) \| Authorized distributor |
| Dynamic braking resistor | External resistor for F5 prevention on decel loads | $60–$200 | [Amazon](https://www.amazon.com/s?i=industrial&k=Allen-Bradley+PowerFlex+braking+resistor+AK-R2&tag=errorcodefixes-20) \| Rockwell distributor |
| Remote operator panel (HIM) | 22-HIM-C2S — allows parameter viewing without laptop | $150–$250 | [Amazon](https://www.amazon.com/s?i=industrial&k=Allen-Bradley+22-HIM-C2S+remote+HIM&tag=errorcodefixes-20) \| Automation distributor |
| Motor PTC thermistor kit | For F7 active thermistor protection on motor | $20–$60 | [Amazon](https://www.amazon.com/s?i=industrial&k=motor+PTC+thermistor+protection+VFD&tag=errorcodefixes-20) |
| 1203-USB DeviceNet/DSI cable | Required to connect laptop for full parameter programming | $120–$200 | [Amazon](https://www.amazon.com/s?i=industrial&k=Allen-Bradley+1203-USB+DSI+cable+PowerFlex&tag=errorcodefixes-20) \| Automation distributor |

## When to Call a Professional

F12 (HW overcurrent) or F38 (phase-to-phase short) that persists after confirming the motor and cable are fault-free indicates a failed output IGBT module inside the PowerFlex 4M. Replacement of the output transistor module requires disassembling the drive and has risk of high-voltage exposure — the drive must be fully de-energized and the DC bus discharged (typically 5 minutes) before opening the enclosure. For drives under warranty, contact Rockwell Automation technical support at 1-440-646-3434; for out-of-warranty drives, contact a Rockwell Automation Authorized Service Center or evaluate replacing the drive entirely (replacement cost is often lower than repair cost for lower HP 4M drives).

> **Pro tip:** The PowerFlex 4M has a built-in **process PI loop controller** (parameters A256–A275) that is rarely used but very powerful for simple closed-loop pump and fan pressure/flow control without an external PLC. If your application has been running open-loop and hunting for setpoint, enabling the PI controller and wiring in a 4–20 mA process feedback sensor can eliminate speed hunting and reduce wear on the driven equipment.

## See Also

- [Allen-Bradley PowerFlex 40 Complete Guide](/posts/allen-bradley-powerflex-40-complete-guide/)
- [Allen-Bradley PowerFlex 523 Fault F7](/posts/allen-bradley-powerflex-523-fault-f7/)
- [Allen-Bradley PowerFlex 525 Fault F7](/posts/allen-bradley-powerflex-525-f7-fault/)
- [Allen-Bradley PowerFlex 753 Fault F12](/posts/allen-bradley-powerflex-753-f12-fault/)
- [VFD Fault Codes Guide — OC, OV, UV, OL](/posts/vfd-fault-codes-oc-ov-uv-ol/)

## Related Articles

- [Allen-Bradley MicroLogix 1400 Common Fault Codes](/posts/allen-bradley-micrologix-fault/)
- [Allen-Bradley PowerFlex 40 Complete Fault Code Guide](/posts/allen-bradley-powerflex-40-complete-guide/)
- [Allen Bradley PowerFlex 40 F2 Fault — Causes & Fix](/posts/allen-bradley-powerflex-40-f2-fault/)
- [Allen-Bradley PowerFlex 40 F3 Fault — Power Loss](/posts/allen-bradley-powerflex-40-f3/)
- [Allen Bradley PowerFlex 40 F7 Fault — Causes & Fix](/posts/allen-bradley-powerflex-40-f7-fault/)
