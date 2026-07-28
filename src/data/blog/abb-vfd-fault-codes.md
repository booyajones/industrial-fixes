---
title: "ABB VFD Fault Codes: ACS550, ACS580, ACS880 Error Guide"
description: "ABB VFD fault codes explained: 2310, 2330, 3130, 3210, 3220, 5091 STO and more for ACS550, ACS580 and ACS880 drives, with likely causes and fixes."
pubDatetime: 2026-04-22T16:00:00Z
modDatetime: 2026-04-22T16:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "Input fuses"
---

## ABB VFD Fault Codes — Quick Reference

ABB drives display fault codes on the integral keypad panel as four-digit numbers or abbreviated text. Faults cause the drive to trip and stop the motor; alarms display but don't stop the drive. The fault history is stored in the drive's memory and can be retrieved via the control panel or Drive Composer software.

| Fault Code | Meaning | Common Fix |
|-----------|---------|-----------|
| 0001 | Overcurrent | Check motor/cable; reduce accel ramp |
| 2201 | Overcurrent (short circuit) | Motor winding short or cable fault |
| 2310 | Overcurrent (peak) | Check for mechanical jam |
| 3130 | Input phase loss | Check all 3 input phases |
| 3210 | DC bus overvoltage | Extend decel ramp; add brake resistor |
| 3300 | DC bus undervoltage | Check input power supply |
| 4110 | Drive overtemperature | Clean cooling fan; check ambient temp |
| 5010 | Overload | Reduce continuous load; check motor FLA |
| 7121 | Analog I/O fault | Check signal wiring |
| 9300 | Communication fault | Check fieldbus adapter or wiring |
| AF10 | Heatsink overtemperature | Clean fan; check airflow |

## Most Common Codes

### Fault 3130: Input Phase Loss
One of the three supply phases (L1, L2, or L3) is missing or has significantly reduced voltage. Check the input fuses (one per phase) — a blown fuse on one phase is the most common cause. Also check the main contactor (if installed) for a burned contact. Measure phase-to-phase voltage at the drive's L1/L2/L3 input terminals.

ABB drives will attempt to run on two phases briefly before tripping 3130. If the fault appears intermittently, check for a loose terminal screw or a contact with high resistance under load.

### Fault 2310: Overcurrent (Peak)
An instantaneous overcurrent trip — the drive output current exceeded the trip threshold. Causes: motor winding short, cable insulation failure, locked rotor (mechanical jam), or too-fast acceleration ramp. Start by megger-testing the motor and cable for insulation resistance (should be >1 MΩ at 500V). If insulation is good, check for mechanical issues and extend the acceleration time.

### Fault 3210: DC Bus Overvoltage
Regenerative energy from a decelerating motor raised the DC bus above the trip threshold. Solutions: (1) extend the deceleration ramp in parameter group 23 (ACS550) or 01.13 (ACS880), (2) enable the flux braking feature (available on ACS880 — uses motor resistance to dissipate energy), (3) install a dynamic braking resistor and chopper module for high-inertia loads.

### Fault 3300: DC Bus Undervoltage
Input supply voltage dropped too low. Check incoming voltage at the drive terminals under load. On ACS550 and ACS880 with a 380–480V supply, the minimum is approximately 270V DC bus (~338V AC input). A weak transformer, long cable runs, or undersized input conductors all contribute.

### Fault 4110: Drive Overtemperature
The drive's IGBT heatsink exceeded its temperature limit. Open the drive cabinet and inspect: (1) internal cooling fan — is it spinning? A failed fan is the #1 cause, (2) heatsink fins — clear with compressed air if clogged with dust, (3) ambient temperature — ACS550/ACS880 are rated to 40°C ambient without derating. Above that, the drive must be derated or better ventilation provided.

### Fault 0001 / 2201: Overcurrent
The drive output stage detected overcurrent above trip level. On ACS880, separate cause analysis is needed: fault 2201 (overcurrent on ground fault or winding short) is more serious than fault 0001 (transient overcurrent during starting). For 2201, use a megger before restarting — a shorted motor winding can damage the drive's output IGBTs.

### Fault 9300: Communication Fault
On ACS550/ACS880 drives with fieldbus adapters (Profibus, EtherNet/IP, Modbus), fault 9300 indicates loss of communication with the master. Check: adapter module is seated securely, fieldbus cable is connected, PLC/master is running and communicating. Fault 9300 can also mean the communication response time exceeded the configured watchdog timeout.

## Retrieving Fault History

On ACS550: Navigate to parameter group 14 (FAULT HISTORY). Parameters 14.01–14.03 show the three most recent faults with time stamps.

On ACS880: Use the Drive Composer PC tool for the full fault log, or navigate to Menu > Diagnostics > Fault Log on the control panel.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input fuses | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-vfd-fault-codes&k=Input+fuses&tag=errorcodefixes-20) \| ABB class J or gR fuses; size per drive catalog |
| Braking resistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-vfd-fault-codes&k=Braking+resistor&tag=errorcodefixes-20) \| ABB catalog OHBR or third-party sized per drive kW |
| Cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-vfd-fault-codes&k=Cooling+fan&tag=errorcodefixes-20) \| Drive-specific; ABB part for ACS550 fan: 68518560 |
| Fieldbus adapter | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-vfd-fault-codes&k=Fieldbus+adapter&tag=errorcodefixes-20) \| FCAN-01 (CAN), FPBA-01 (Profibus), FENA-21 (EIP) |
## When to Call a Pro
Faults 2201 (short circuit overcurrent) and any fault accompanied by a burning smell or blown fuses require qualified drive service. ABB's regional service centers offer warranty and post-warranty repair.

## More Abb Vfd fault codes

Compiled from manufacturer service manuals and authorized documentation.

| Code | What it means | Likely cause | How to fix |
| --- | --- | --- | --- |
| 2340 | Short circuit in the motor cable(s) or motor. | Cabling error or a shorted winding/cable between output phases. | Check motor and motor cable for wiring errors. Confirm no PFC capacitors or surge absorbers are in the motor cable, then cycle power to the drive. |
| 2381 | IGBT overload. Excessive IGBT junction-to-case temperature. | Protects the IGBTs; can be triggered by a short circuit in the motor cable or by an undersized drive for the motor. | Check the motor cable, ambient conditions, airflow and fan operation, heatsink fins for dust, and drive power rating against motor power. |
| 3181 | Wiring or earth fault. Incorrect input-power and motor-cable connection. | Input power cable is connected to the drive's motor (output) terminals, or a similar wiring error. | Check input power connections and confirm supply is landed on the input terminals and the motor on the output terminals. This fault is programmable via par 31.23. |
| 3220 | DC link undervoltage. Intermediate-circuit DC voltage is insufficient. | Missing supply phase, blown fuse, or a fault in the rectifier bridge. | Check supply cabling, fuses and switchgear. Measure incoming voltage under load. |
| 3381 | Output phase loss. Motor-circuit fault from a missing motor connection. | All three motor phases are not connected (open output phase, loose lug, or open contactor on the motor side). | Connect/verify the motor cable on all three output phases. Programmable via par 31.19 Motor phase loss. |
| 4210 | IGBT overtemperature. Estimated drive IGBT temperature is excessive. | Poor cooling, high ambient, clogged heatsink, failed fan, or drive undersized for the motor. | Check ambient conditions, airflow and fan operation, clear dust from heatsink fins, and verify drive power rating versus motor power. |
| 4290 | Cooling. Drive module temperature is excessive. | Ambient above the derating threshold, blocked cooling airflow, dust in the heatsink, or a failing fan. | Verify ambient temperature and derating, check module cooling airflow and fan operation, and clean the cabinet interior and heatsink. |
| 5090 | STO hardware failure. STO hardware diagnostics detected a hardware failure. | Internal Safe Torque Off hardware fault. | Contact ABB for hardware replacement. Do not attempt to defeat or bypass the STO circuit. |
| 5091 | Safe torque off. The STO function is active because a safety-circuit signal to the STO connector opened during start or run. | STO circuit input(s) broken/opened (e-stop, safety relay, gate, or wiring), or control-board supply issue. | Check safety-circuit connections to the STO terminals and verify par 95.04 Control board supply. Programmable via par 31.22 STO indication run/stop. |
| 6681 | EFB comm loss. Communication break on the embedded fieldbus (EFB). | Fieldbus master offline or in error, or a broken RS-485 connection. | Check the fieldbus master status and the cable connections to the EIA-485/X5 terminals 29, 30 and 31 on the control unit. Programmable via par 58.14. |
| 7081 | Control panel loss. The control panel or PC tool set as active control location stopped communicating. | Disconnected or faulty control panel, loose panel connector, or lost PC-tool link. | Check the PC-tool/control-panel connection and connector; disconnect and reconnect the panel. Action is programmable via par 49.05. |
| 7181 | Brake resistor broken or not connected. | Missing, damaged, or incorrectly dimensioned dynamic braking resistor. | Confirm a brake resistor is connected, check its condition, and verify it is correctly sized for the drive. |
| 7310 | Overspeed. Motor is turning faster than the highest allowed speed. | Incorrectly set min/max speed, insufficient braking torque, or load changes when using torque reference. | Check min/max speed settings (par 30.11/30.12), motor braking torque, and whether a brake chopper/resistor is needed. |
| 7510 | FBA A communication. Cyclic communication between the drive and fieldbus adapter module A (or PLC to adapter) is lost. | Fieldbus adapter or cabling fault, master offline, or mis-set fieldbus parameters. | Check fieldbus status and cabling, verify the master is communicating, and review parameter groups 50-53. Programmable via par 50.02. |
| 80A0 | AI supervision. An analog input signal is outside its configured limits. | Broken or shorted analog signal wiring, or a transmitter out of range (aux codes identify AI1/AI2 under-min or over-max). | Check the analog input signal level and wiring, and review the min/max limits in parameter group 12. Programmable via par 12.03. |
| FA81 | Safe torque off 1. STO circuit 1 is broken. | One STO channel input is open (e-stop, safety relay, or wiring on channel 1). | Check STO safety-circuit connections and verify par 95.04 Control board supply. |
| FA82 | Safe torque off 2. STO circuit 2 is broken. | The second STO channel input is open (e-stop, safety relay, or wiring on channel 2). | Check STO safety-circuit connections and verify par 95.04 Control board supply. |
| FF61 | ID run. The motor identification run did not complete successfully. | Incorrect motor nameplate data, an external control system connected during ID run, a locked motor shaft, or limits blocking completion. | Verify motor data in group 99, disconnect any external control, ensure the shaft is free, restore defaults, and rerun the ID run. |

## How to troubleshoot Abb Vfd

Work an ABB drive fault from the outside in, and always start with safety. These are qualified-electrician tasks: isolate and lock out the supply, then wait for the DC bus to discharge (ABB specifies about 5 minutes) before touching terminals, because the DC link holds a lethal charge after power is removed. If a fault is accompanied by a burning smell, blown input fuses, or visible damage, stop and get the drive serviced rather than resetting and re-energizing.

Read the code, not just the trip. ABB drives log the last several faults with time stamps and an auxiliary code. Pull the fault log first (on ACS580/ACS880 via Menu - Diagnostics - Fault & event log, or the full log in Drive Composer PC tool; on ACS550 via parameter group 04 Fault History). The auxiliary code often pinpoints the phase or channel involved and saves guessing. Note whether the indication is a fault (drive trips, latches, needs a reset) or a warning (self-clears when the cause goes away).

Diagnose by category. Overcurrent, earth-fault, and short-circuit codes (2310, 2330, 2340, 3181) point at the motor and cable first: de-energize and megger-test insulation resistance of the motor and motor cable, and look for PFC capacitors or surge absorbers wrongly wired on the motor side. Bus voltage codes split cleanly: overvoltage (3210) is regenerative energy on deceleration, so extend the decel ramp or add a brake chopper and resistor, while undervoltage (3220/3300) and input phase loss (3130) point upstream to fuses, supply phases, contactors, and terminal tightness. Thermal codes (4110, 4210, 4290) almost always trace to cooling: a failed or clogged cooling fan is the single most common cause, followed by high ambient temperature and dust-packed heatsink fins. STO codes (5091, FA81, FA82) mean the safety circuit opened; check the e-stop, safety relay, and STO wiring, and never defeat or jumper the STO input to clear a trip. Communication codes (6681, 7510, 7081) are fieldbus/panel connectivity, not a power problem.

Know when to call a pro. Internal-hardware codes (5090 STO hardware failure, power-unit and measurement-circuit faults) and any repeat overcurrent after a confirmed-good motor and cable indicate damaged output IGBTs or control hardware and warrant ABB service or a specialist drive-repair shop. Resetting a hard short (2340) without megger-testing first risks destroying the output stage.

## Frequently asked questions

### What is the most common ABB drive fault?

Overvoltage (3210) on deceleration and heatsink overtemperature (4210/4290) are the two most frequent trips in the field. Overvoltage comes from a decel ramp that is too fast for the load's inertia, and is fixed by extending the ramp or adding a brake resistor. Overtemperature is almost always a failed or dust-clogged cooling fan, or ambient temperature above the drive's rating.

### What does fault 2330 (earth leakage) mean on an ABB drive?

The drive sensed current unbalance across the output phases, which usually means an earth (ground) fault in the motor or motor cable. De-energize, wait for the DC bus to discharge, then megger-test the insulation resistance of the motor and cable. Also remove any power-factor-correction capacitors or surge absorbers wired on the motor side, since those can trigger it. If no earth fault is found, ABB says to contact service.

### How do I reset an ABB drive fault?

After removing the cause, reset from the control panel, Drive Composer, a digital input, or fieldbus (source is set by parameter 31.11 on ACS580/ACS880). Some faults, including certain internal and rating-ID faults, require a full control-unit reboot via power cycle or parameter 96.08. If the fault returns immediately on reset, the underlying cause is still present, do not keep resetting into it.

### Why does my ABB drive keep tripping on STO / fault 5091?

Fault 5091 (Safe torque off) means a signal on the STO safety circuit opened during start or run, most often an e-stop, a safety relay, a gate/guard switch, or broken STO wiring. Check the STO terminal connections and the control-board supply (parameter 95.04). Fault 5090 is different, it is an internal STO hardware failure that needs ABB hardware replacement. Never jumper or defeat the STO input to clear the trip.

### Is an ABB drive fault safe to fix myself?

Setup and cooling issues (extending a decel ramp, replacing a cooling fan, cleaning heatsink fins, checking fieldbus cabling) are within reach of a qualified maintenance electrician. But the DC bus stays lethal for about 5 minutes after power-off, and internal power-stage, IGBT, or measurement-circuit faults require a specialist. Any fault with blown fuses, a burning smell, or a repeated short-circuit trip should go to ABB service or a drive-repair shop.
