---
title: "ABB ACS880 Fault Codes: List, Causes & Fixes"
description: "ABB ACS880 fault codes explained: overcurrent, overvoltage, undervoltage, STO, overtemp, phase loss and fieldbus faults with real causes and fixes."
pubDatetime: 2026-06-11T09:44:17Z
modDatetime: 2026-06-11T09:44:17Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "ABB ACS880 Control Board"
most_likely_cause: "Motor cable damage or mechanical binding"
likelihood: "the most common cause for overcurrent faults"
diy_or_pro: "pro"
---

## What this code means
The ABB ACS880 drive uses alphanumeric fault codes to diagnose problems. The first digit tells you the category: 2xxx codes are overcurrent or short circuit faults, 3xxx are overvoltage faults, 7xxx are temperature warnings, and F0xxx are internal drive failures. Common examples include 2310 (sustained overcurrent during operation), 2340 (short circuit detected in motor cable or windings), 2330 (ground fault or leakage current), 3210 (DC link overvoltage from fast deceleration or high line voltage), 7120 or 7121 (drive or IGBT overtemperature), F0001 (internal control board or firmware fault), and F0120 (encoder feedback failure).

Each code points to a specific hardware or configuration problem. Overcurrent faults usually mean mechanical binding, wrong acceleration settings, or cable damage. Overvoltage faults happen when a high-inertia load decelerates too quickly and pumps energy back into the drive. Temperature faults point to cooling system failure or a hot environment. Internal faults often require factory service or board replacement. Always record the exact code and consult your drive's firmware manual for the precise definition, since code meanings can vary slightly between ACS880 models and firmware versions.

## Before You Replace Anything

Technicians often replace the drive itself when the real problem is a shorted motor cable or jammed load. Before replacing the drive, disconnect the motor cable and measure insulation resistance to ground and between phases with a megohmmeter.

## Common Causes

- **Damaged motor cable** Physical damage to the output cable insulation causes phase-to-phase or phase-to-ground shorts that trigger 2330 or 2340 faults.
- **Mechanical binding or jam** A seized bearing, misaligned coupling, or jammed load forces the motor to draw excessive current and trip 2310 overcurrent faults.
- **Cooling system failure** Clogged air filters, bent fan blades, or a failed drive cooling fan cause the heatsink or IGBT temperature to exceed limits and trigger 7120 or 7121 faults.
- **Deceleration time too short** When a high-inertia load decelerates faster than the drive can dissipate energy, the DC link voltage spikes and triggers 3210 overvoltage faults.
- **Motor startup data mismatch** If parameter 99 motor data does not match the actual motor nameplate, the drive calculates wrong current limits and trips on 2310.

## Step-by-Step Fix {#fix}

1. **Record the exact fault code** from the drive display or keypad and write down the code number (e.g., 2310, 3210, 7120) before resetting the fault.
2. **Consult the drive firmware manual** to confirm the exact meaning of the code for your ACS880 model, since definitions can vary by firmware version.
3. **Power down and lockout** the drive, then disconnect the motor cable from the drive output terminals U, V, and W.
4. **Megohmmeter test the motor cable and motor** by measuring insulation resistance from each phase to ground and between phases (should be greater than 1 megohm for a healthy cable).
5. **Inspect motor and load mechanically** by rotating the motor shaft by hand to check for binding, seized bearings, or misaligned couplings.
6. **Check drive cooling system** by verifying that all cooling fans are spinning freely, air filters are clean, and there is no dust buildup on heatsinks.
7. **Review drive parameters** in group 46 (acceleration and deceleration times) and group 99 (motor startup data) to confirm they match your motor nameplate and load inertia, then consult your model's parameter table for recommended settings.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB ACS880 Control Board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-880-fault-codes&k=ABB+ACS880+Control+Board&tag=errorcodefixes-20) \| For F0001 internal faults; confirm part number from your drive nameplate before ordering. |
| Drive Cooling Fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-880-fault-codes&k=Drive+Cooling+Fan&tag=errorcodefixes-20) \| Match voltage and CFM rating to your ACS880 frame size. |
| Motor Output Cable (Shielded VFD-Rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-880-fault-codes&k=Motor+Output+Cable+%28Shielded+VFD-Rated%29&tag=errorcodefixes-20) \| Use cable rated for variable frequency drive service with proper gauge for motor current. |

## When to Call a Pro

Call a qualified drive technician or ABB-certified service provider for any fault that persists after you have verified cable integrity, mechanical freedom, and cooling airflow. Internal faults (F0xxx codes) almost always require board-level diagnostics or factory repair. Overvoltage faults that recur after adjusting deceleration time may need a braking resistor installation, which must be sized and wired by a professional. If you are not trained to work with high-voltage DC link circuits (up to 800 VDC on larger models) or lack a megohmmeter and insulation testing experience, do not attempt repairs beyond inspecting filters and fans. Drive repairs involve lethal voltages and require specific safety procedures and test equipment.

## More Abb 880 fault codes

Compiled from manufacturer service manuals and authorized documentation.

| Code | What it means | Likely cause | How to fix |
| --- | --- | --- | --- |
| 3220 | DC link undervoltage | Intermediate (DC bus) voltage too low, usually from a missing supply phase, blown input fuse, low line voltage, or a fault in the rectifier bridge. | Check the incoming supply voltage on all three phases, inspect input fuses and the main contactor, and verify supply cabling. Correct any missing phase or low-voltage condition before restarting. |
| 3130 | Input phase loss | One of the incoming supply phases is missing, or the DC bus voltage is rippling because of an open phase, blown fuse, or loose supply connection. | Measure all three input phases at the drive terminals, check input fuses and disconnect contacts, and tighten supply-side terminations. Restore the missing phase before resetting. |
| 3381 | Output phase loss | The drive detects that a motor output phase (U, V or W) is missing, typically an open motor cable conductor, loose output terminal, or an open motor winding. | Power down and lock out, then check continuity of each output phase from the drive to the motor and inspect the motor windings. Repair the open conductor or connection. |
| 2381 | IGBT overload | Excessive IGBT junction-to-case temperature. Protects the output IGBTs and can be triggered by a short circuit in the motor cable, excessive load, or too high a switching frequency for the load. | Check the motor cable and motor for shorts with a megohmmeter, reduce load or acceleration demand, and verify cooling. Confirm switching frequency and drive sizing match the application. |
| 4210 | IGBT overtemperature | Estimated IGBT temperature is excessive, usually from blocked cooling airflow, a failed cooling fan, high ambient temperature, or sustained overload. | Clean or replace air filters, verify all cooling fans spin freely, clear dust from the heatsink, and confirm the ambient temperature is within the drive rating. Reduce load if the drive is undersized. |
| 5091 | Safe torque off | The Safe Torque Off function is active because a safety-circuit signal on connector XSTO is broken during start or run, or the drive is stopped with STO diagnostics set to Fault. | Check the STO wiring and both XSTO channels, verify the safety relay/E-stop chain is closed, and confirm parameter 31.22 STO diagnostics configuration. Restore the safety circuit before resetting. |
| 5090 | STO hardware failure | The Safe Torque Off hardware self-diagnostic has detected an internal fault in the STO circuitry. | Cycle power to clear a transient. If it persists, the STO hardware or control unit needs service. Contact ABB or a certified drive technician; do not bypass STO. |
| 7081 | Panel port communication (control panel / keypad communication lost) | The control panel (keypad) or PC tool selected as the active control location has stopped communicating with the drive over the panel port. | Reseat the control panel and its cable, check the panel connector, and confirm the panel/PC tool communication settings. Replace a damaged panel cable if needed. |
| 7310 | Overspeed | Motor speed has exceeded the allowed limit, often because of an overhauling/high-inertia load, wrong speed-limit parameters, or an encoder/feedback problem. | Check the speed limit parameters, verify encoder feedback and scaling, and confirm the load is not driving the motor faster than commanded. Add a braking resistor for overhauling loads if required. |
| 7510 | FBA A communication | Cyclic communication is lost between the drive and a fieldbus adapter module (FBA A), from adapter cabling, configuration, or master faults. | Check the fieldbus adapter connection and network cabling, verify the adapter configuration and the comm-loss action parameters, and confirm the PLC/master is communicating. |
| FA81 | Safe torque off 1 | Loss of the Safe Torque Off channel 1 signal at the STO input. | Inspect the STO channel 1 wiring and the safety device driving it (E-stop, safety relay, gate), and restore the signal. Both STO channels must be healthy to run. |

## How to troubleshoot Abb 880

On any ABB ACS880, work the fault by category, which the first digit tells you: 2xxx are current/short-circuit faults, 3xxx are supply and DC-bus voltage or phase-loss faults, 4xxx/5xxx are temperature and hardware/STO faults, 6xxx/7xxx are internal, communication, motor-protection and feedback faults, and 8xxx/9xxx are supervision and external events. Record the exact code and any auxiliary code from the keypad before you reset, because a reset erases the context and some codes only differ by the last hex digit.

Start with the safe, non-invasive checks in this order. First confirm the incoming supply: measure all three input phases, check the input fuses and main contactor, and rule out undervoltage or a lost phase (3130, 3220) before touching the motor side. Next check cooling for any temperature fault (4210, 4310): a clogged filter, dust-caked heatsink, or a dead cooling fan is the single most common recurring cause and is cheap to fix. Only then move to the motor circuit. For overcurrent, short-circuit, earth-fault, or output-phase-loss codes (2310, 2330, 2340, 3381, 2381), power down, lock out, disconnect the motor cable at U/V/W, and megohmmeter-test each phase to ground and phase-to-phase (a healthy cable and motor read well above 1 megohm), then rotate the shaft by hand to rule out a seized bearing or jammed load.

Two categories deserve special care. STO and safety faults (5090, 5091, FA81, FA82) mean the Safe Torque Off circuit opened or failed a self-test; check the XSTO wiring and the E-stop/safety-relay chain, but never jumper or bypass STO to clear a fault. Communication faults (7081, 7510) are usually wiring, termination, node-address, or configuration problems, not a failed drive, so verify the cable and bus parameters before replacing hardware.

Call a qualified drive technician or ABB-certified service for any internal fault that persists after cable, mechanical, and cooling checks, for recurring overvoltage that may need a braking resistor, and for anything requiring work inside the DC-bus circuit, which can hold lethal voltage (up to about 800 VDC on larger frames) for minutes after power-off. If you do not have a megohmmeter, insulation-testing experience, and lockout/tagout training, limit yourself to filters, fans, and reading codes.

## Frequently asked questions

### Is ACS880 fault 7121 an overtemperature fault?

No. In the ACS880 firmware fault list, 7121 is Motor stall, not an overtemperature fault. The genuine temperature faults are 4210 (IGBT overtemperature), 4310 (excess temperature) and 42F1 (IGBT temperature). Always confirm the exact code and its name against your drive's firmware manual, since the code text is the authoritative meaning.

### How do I clear a 5091 Safe Torque Off fault on an ACS880?

5091 means the STO safety signal on connector XSTO opened during start or run, or the drive is stopped with STO diagnostics set to fault. Check both XSTO channels, the E-stop and safety-relay chain, and parameter 31.22. Restore the safety circuit and only then reset. Never jumper the STO inputs to force a reset.

### The drive trips on overcurrent (2310) immediately when I start. What should I check first?

An instant trip before the motor turns usually points to a shorted motor cable, a shorted or grounded motor winding, or IGBT damage. Power down, lock out, disconnect the motor cable at U/V/W, and megohmmeter-test the cable and motor to ground and phase-to-phase. If the cable and motor test good, suspect the drive output stage.

### What causes a 3210 overvoltage fault and how do I stop it recurring?

3210 (DC link overvoltage) happens when a high-inertia load decelerates faster than the drive can absorb the returned energy, or when the line voltage is too high. Lengthen the deceleration time, or if the application needs fast stops, add a properly sized braking resistor and brake chopper wired by a professional.

## Related guides

- [Abb Vfd Fault Codes](/posts/abb-vfd-fault-codes/)
- [Abb Acs580 Fault Codes](/posts/abb-acs580-fault-codes/)
- [Abb Acs880 Complete Guide](/posts/abb-acs880-complete-guide/)
- [Abb Ach580 Fault Codes](/posts/abb-ach580-fault-codes/)
