---
title: "SEW-Eurodrive Fault F07: Fix DC Link Overvoltage + Codes"
description: "SEW-Eurodrive fault F07 is DC link overvoltage from regenerative braking. Learn the real causes, the step-by-step fix, and related MOVITRAC/MOVIDRIVE fault codes."
pubDatetime: 2026-04-22T08:00:00Z
modDatetime: 2026-04-22T08:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - sew-eurodrive
money_part: "Braking resistor (SEW-specified)"
most_likely_cause: "Deceleration ramp too short"
---

## SEW-Eurodrive Fault F07 — What It Means

SEW-Eurodrive fault F07 means overvoltage on the DC link — the DC bus voltage exceeded the maximum allowable threshold. On SEW MOVITRAC B, MOVIDRIVE B, and MOVIMOT series drives, F07 is triggered when the DC bus rises above approximately 800–850 VDC on a 480V-class drive, or 400–420 VDC on a 240V-class drive. DC bus overvoltage is typically caused by regenerative energy — kinetic energy from a decelerating load feeding voltage back into the bus faster than the bus can absorb it or dissipate it through a braking resistor.

[Jump to Fix](#fix)

## Common Causes

- **Deceleration ramp too short** — If the drive is commanded to stop or slow down quickly, the motor acts as a generator and pumps energy back into the DC bus faster than the internal brake chopper can handle it.
- **No braking resistor or undersized braking resistor** — High-inertia loads (large fans, centrifuges, hoists) require an external braking resistor to dissipate regenerative energy. Without one, the bus voltage climbs until F07 trips.
- **Input overvoltage** — If the AC input supply is already at the high end of tolerance (e.g., 500V on a 480V system), the DC bus sits higher than normal and a small regeneration event is enough to trip F07.
- **Failed brake chopper** — The brake chopper transistor (internal to the drive) is supposed to activate the braking resistor when bus voltage rises. If the chopper has failed open, no energy is dissipated and F07 follows.

## Step-by-Step Fix {#fix}

1. **Increase deceleration ramp time** — In SEW MOVITOOLS or via the keypad, find the deceleration ramp parameter (Ramp t11 in MOVITRAC B, Ramp 1 in MOVIDRIVE). Increase it significantly and test. This is the most common fix.
2. **Check braking resistor** — If the application requires fast stops or has high-inertia loads, verify a braking resistor is installed and correctly wired to the brake chopper terminals (BW+ and BW on SEW drives). Measure resistor continuity.
3. **Measure input voltage** — Check the AC input at the drive terminals. If supply voltage is high (>510V on a 480V system), F07 will appear at deceleration rates that would be fine at nominal voltage.
4. **Test the brake chopper** — With the drive in a controlled test, monitor DC bus voltage during deceleration. If bus voltage climbs above the chopper activation threshold without the resistor heating, the chopper may have failed.
5. **Reset the system** — After increasing deceleration time or installing/verifying the braking resistor, reset the fault via the keypad (STOP/RESET key) and test a complete stop cycle.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Braking resistor (SEW-specified) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-sew-eurodrive-fault-f07&k=Braking+resistor+%28SEW-specified%29&tag=errorcodefixes-20) \| Must match SEW's resistance and wattage specification for your drive size |
| Brake chopper module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-sew-eurodrive-fault-f07&k=Brake+chopper+module&tag=errorcodefixes-20) \| Internal to larger drives; separate external module for high-power applications |
| Line reactor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-sew-eurodrive-fault-f07&k=Line+reactor&tag=errorcodefixes-20) \| Reduces input overvoltage from supply transients |
## When to Call a Pro

If the braking resistor is correctly sized, installed, and tested good, but F07 persists, the internal brake chopper transistor may have failed. SEW-certified technicians can test the chopper circuit and replace the relevant IGBT module.

## More Sew Eurodrive Fault F07 fault codes

Compiled from manufacturer service manuals and authorized documentation.

| Code | What it means | Likely cause | How to fix |
| --- | --- | --- | --- |
| F01 | Overcurrent. Immediate switch-off with inhibit. | Short circuit at the output, motor too large for the inverter, or a defective output stage. | Disconnect the motor and cable and check for a short or ground. Verify the motor is correctly sized for the drive. If the fault persists with the motor disconnected, the output stage is likely damaged and the unit needs service. |
| F03 | Ground fault. Immediate switch-off with inhibit. | Ground fault in the motor, in the inverter, or in the motor/supply lead. | Disconnect the motor and megger/insulation-test the motor and cable to earth. Replace or repair the faulted cable or motor. If the fault clears with the motor disconnected, the wiring or motor is the culprit; if not, the inverter needs service. |
| F04 | Brake chopper. Immediate switch-off with inhibit. | Too much regenerative power, the braking resistor circuit interrupted, or the brake chopper defective. | Extend the deceleration ramp and confirm the braking resistor is correctly sized and its supply cable is intact and wired. If the resistor and wiring are good but F04 persists, the internal brake chopper may have failed and requires service. |
| F06 | Mains phase failure. Immediate switch-off with inhibit. | A phase of the AC supply has failed or is missing (or supply voltage too low). | Measure all three input phases at the drive terminals and confirm they are present and balanced. Check upstream fuses, contactors, and terminal connections. Correct any loose or blown connection before restarting. |
| F08 | Speed monitoring. Immediate switch-off with inhibit. | Mechanical overload, output phase failure, or maximum speed exceeded. | Check for a mechanical overload or jam on the driven load, confirm the motor connection and output phases, and verify the maximum speed setting and ramp parameters match the application. |
| F11 | Overtemperature. Stop with inhibit. | Thermal overload of the inverter. | Reduce the load or improve cooling. Clean the heatsink and confirm the cooling fan runs, verify ambient temperature is within spec, and confirm the drive is not undersized for the duty cycle. |
| F34 | Ramp timeout. Immediate switch-off with inhibit. | The set ramp time was exceeded, or the stop ramp time is exceeded by a certain duration. | Review the ramp parameters and the load. A load that cannot follow the commanded ramp (too much inertia or friction) triggers this; extend ramp times or resolve the mechanical restriction. |
| F44 | Unit utilization. Immediate switch-off with inhibit. | The Ixt value was exceeded (the drive was run above its allowable current over time). | Reduce the load, lengthen ramps, and allow longer pauses between cycles. Confirm the drive is correctly sized for the continuous and peak duty of the application. |
| F82 | Open output. Immediate switch-off with inhibit. | In VFC hoist mode, output phases interrupted, or the rated motor power is too small. | Check all three output leads and connections between the drive and motor for a break or loose terminal. Confirm the motor rating is compatible with the drive. |
| F84 | Motor protection. Stop with inhibit. | Motor utilization too high (thermal model overload). | Reduce load, extend ramps, and allow longer pause times between starts. Verify the motor-protection parameters match the actual motor nameplate. |
| F94 | EEPROM checksum. Immediate switch-off with inhibit. | Defective EEPROM, or the parameter module was removed during a copy operation. | Load factory settings or restore a complete data set from a parameter module. If the fault returns, the unit needs service. |
| F113 | Analog input open circuit. Rapid stop/warning. | AI1 analog input open circuit. | Check the analog reference wiring to AI1 for a break or loose terminal and confirm the source signal is present. Review the analog input startup/scaling settings. |


## How to troubleshoot Sew Eurodrive Fault F07

On any SEW-Eurodrive drive (MOVITRAC B, MOVIDRIVE B, MOVIMOT), start by reading the exact fault code and the fault history from the keypad or MOVITOOLS/MotionStudio before touching anything. The code plus the stored fault memory tells you whether the trip happened during acceleration, at constant speed, during deceleration, or at power-up, which narrows the cause faster than any single measurement.

Work from the most common failure modes outward. Deceleration-time faults (F07 DC link overvoltage, F04 brake chopper) point to regenerative energy and braking-resistor sizing. Current and ground faults (F01, F03, F82) point to the motor and motor cable, so isolate the motor and insulation-test the windings and leads to earth. Thermal faults (F11 inverter overtemperature, F44 unit utilization, F84 motor protection) point to overload or cooling, so check duty cycle, heatsink cleanliness, fan operation, and ambient temperature. Supply faults (F06) point upstream to fuses, contactors, and phase balance.

Safety first: a VFD DC bus holds a lethal charge for several minutes after power-off. Always lock out and tag out, wait the full discharge time stated in the manual, and verify zero volts across the DC link terminals with a meter before opening the drive or disconnecting motor leads. Never reset a drive repeatedly into a hard fault; a persistent overcurrent or ground fault can escalate damage.

Call a certified technician when the fault persists after the motor and cabling are proven good, when a code points to internal hardware (a system-software or watchdog fault, F94/F97/F98 memory faults, or a failed output stage), or when the drive shows physical damage or a burnt smell. Those are unit-level repairs, not field parameter changes.


## Frequently asked questions

### What does SEW-Eurodrive fault F07 actually mean?

F07 is DC link overvoltage: the DC bus voltage rose above the drive's allowable maximum. On MOVITRAC B and MOVIDRIVE B this is almost always regenerative energy from a decelerating or overhauling load feeding the bus faster than it can be dissipated. The manual lists the response as immediate switch-off with inhibit.

### Why does F07 keep coming back even after I reset it?

A reset alone does not remove the cause. If the deceleration ramp is still too short, or the braking resistor is missing, undersized, or disconnected, the bus will overvoltage again on the next stop. Extend the ramp, verify the resistor and its wiring at the drive's braking-resistor terminals, and check that input supply voltage is not sitting at the high end of tolerance.

### Is F07 the same as the F04 brake chopper fault?

No. F07 is DC link overvoltage; F04 is a brake chopper fault. They are related because both involve braking energy. If the chopper or resistor cannot dump the regenerated energy, the bus climbs and you can see F07, F04, or both depending on where the failure is. Diagnose the resistor and chopper circuit together.

### Can I fix F07 myself or do I need an SEW technician?

The common fixes are field-serviceable: lengthening the deceleration ramp in the parameters and verifying or resizing the braking resistor. If the resistor and wiring are confirmed good but F07 persists, the internal brake chopper may have failed, and that is a unit-level repair for an SEW-certified technician.

### How do I read the fault history on a SEW drive?

Use the keypad menu or connect with MOVITOOLS MotionStudio to view the stored fault memory. The history shows the sequence of recent faults and the operating state at the time of each trip, which helps confirm whether F07 occurred during deceleration versus at another point in the cycle.


## Related guides

- [Sew Eurodrive Vfd Fault Codes](/posts/sew-eurodrive-vfd-fault-codes/)
- [Delta Vfd Fault Codes](/posts/delta-vfd-fault-codes/)
- [Siemens Sinumerik Alarm 25000 Drive Fault](/posts/siemens-sinumerik-alarm-25000-drive-fault/)
- [Abb Acs880 Complete Guide](/posts/abb-acs880-complete-guide/)

