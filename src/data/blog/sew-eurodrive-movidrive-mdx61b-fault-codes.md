---
title: "SEW-Eurodrive MOVIDRIVE MDX60B/61B Fault Codes: Complete Error List with Sub-Error Codes"
description: "Every MOVIDRIVE MDX60B/61B fault code from SEW's official error list, F01 through F199, with sub-error codes, factory fault responses, real causes, and field fixes."
pubDatetime: 2026-07-28T08:00:00Z
modDatetime: 2026-07-28T08:00:00Z
author: "Error Code Fixes Editorial Team"
slug: sew-eurodrive-movidrive-mdx61b-fault-codes
featured: false
draft: true
tags:
  - vfd
  - electrical
  - sew-eurodrive
money_part: "Braking resistor (SEW-specified)"
free_checks:
  - "Read the fault memory (P080): it stores the last five faults with speed, output current, DC link voltage, heat sink temperature, and utilization at the moment of each trip"
  - "Read the sub-error code in MOVITOOLS MotionStudio (version 4.50 or later) or on the DBG60B keypad before condemning any part"
  - "Power cycle the drive with the supply contactor off for at least 10 seconds, then see if the fault returns under load"
---

## MOVIDRIVE MDX60B/61B Fault Codes — What They Mean

The SEW-Eurodrive MOVIDRIVE MDX60B and MDX61B (the "MOVIDRIVE B" series) report faults as a two-level code: a main fault code (F01, F07, F14, and so on) plus a sub-error code that pinpoints the exact failure inside that fault family. The unit's 7-segment display flashes the main code digit by digit: hundreds (if present), tens, then ones, each shown for about one second with a short blank between them. So a display sequence of 1 - 0 - 0 is fault 100, not three separate faults.

The 7-segment display only shows the main code. To see the sub-error code, which is often the difference between "check a cable" and "send the unit in," you need MOVITOOLS MotionStudio (version 4.50 or later) or the DBG60B keypad.

Before you reset anything, read the fault memory. Parameter P080 stores the last five faults (t-0 through t-4), and for each one it records the state of the binary inputs and outputs, inverter operating status, heat sink temperature, speed, output current, active current, unit utilization, DC link voltage, power-on hours, enable hours, parameter set, and motor utilization at the moment of the trip. That snapshot usually tells you whether the drive tripped while accelerating, decelerating, or sitting at speed, and that alone eliminates half the suspect list.

Note: the related MOVITRAC B frequency inverter uses a similar F-numbered scheme, but its fault table is not identical. Use the table below for MOVIDRIVE B only.

## The three switch-off responses

Every fault triggers one of three factory-set reactions, and the reaction matters on a hoist or a machine with stored energy:

- **Immediate disconnection** — the output stage goes to high resistance instantly and the brake output (DB00 "/Brake") drops to 0, applying the brake immediately. The drive can no longer brake the load electrically.
- **Rapid stop** — the drive brakes down the stop ramp t13/t23, applies the brake at stop speed, then the output stage goes to high resistance after the brake reaction time (P732/P735).
- **Emergency stop** — same sequence, but down the emergency ramp t14/t24.

Where the table below shows "(P)," the response is programmable via the P83x error-response parameters (or with IPOSplus). For fault 108 the response is set in P555, and for fault 109 in P556.

## Complete MDX60B/61B fault code table

Compiled from SEW-Eurodrive's official error list (Compact Operating Instructions, section 6.2.3).

| Code | Fault | Factory response | Cause and first fix |
| --- | --- | --- | --- |
| F00 | No error | – | Normal state. |
| F01 | Overcurrent | Immediate disconnection | Short circuit at the output, motor too large for the inverter, or defective output stage. Rectify the short, fit a correctly sized motor, activate P138 ramp limit and/or lengthen the ramp. |
| F03 | Ground fault | Immediate disconnection | Ground fault in the motor lead, the motor, or the inverter itself. Eliminate the ground fault; consult SEW Service if it is internal. |
| F04 | Brake chopper | Immediate disconnection | Too much regenerative power, braking resistor circuit interrupted or shorted, brake resistance too high, or defective chopper. Extend deceleration ramps, check the resistor cable and its technical data; replace the unit if the chopper is defective. |
| F06 | Mains phase failure | Immediate disconnection | DC link voltage periodically too low from a missing supply phase or poor line quality. Check the line cable, fuses, contactor, and supply configuration. |
| F07 | DC link overvoltage | Immediate disconnection | Regenerative energy pushed the DC bus too high. Extend deceleration ramps, check the braking resistor supply cable and resistor data. |
| F08 | Speed monitoring | Immediate disconnection (P) | Speed or current controller at its set limit from mechanical overload or a missing supply/motor phase; encoder wired wrong; n_max exceeded in torque control. Reduce load, increase the delay (P501/P503), check encoder wiring and supply, current limit, motor cable, and mains phases. |
| F09 | Startup | Immediate disconnection | The drive has not been commissioned for the selected operating mode, or the wrong encoder type is set. Perform startup for the required mode. |
| F10 | IPOS-ILLOP | Emergency stop | Invalid command or invalid conditions during IPOSplus program execution. Correct the program memory and check the sequence against the IPOSplus manual. |
| F11 | Overtemperature | Emergency stop (P) | Heat sink too hot from thermal overload, or a defective temperature sensor. Reduce load, ensure cooling, check the fan. |
| F13 | Control signal source | Immediate disconnection | Control source set to something not installed (e.g. fieldbus with no fieldbus card). Set the correct source in P101. |
| F14 | Encoder | Immediate disconnection | Encoder cable or shield not connected correctly, shorted or broken wire, or defective encoder. Check cable, shield, and connections (sub-codes below identify the interface). |
| F17–F24 | System malfunction | Immediate disconnection | Inverter electronics disrupted, possibly by EMC (stack overflow/underflow, external NMI, undefined opcode, protection fault, illegal access). Improve grounding and shielding; consult SEW Service if it recurs. |
| F25 | EEPROM | Rapid stop | Read/write error on the power-section EEPROM or the memory card. Activate factory settings, reset, re-enter parameters; replace the memory card if it is defective. |
| F26 | External terminal | Emergency stop (P) | An external error signal was read in via a programmable input. Eliminate the external cause; reprogram the terminal if needed. |
| F27 | No limit switches | Emergency stop | Open circuit, both limit switches missing, or switches swapped relative to direction of rotation. Check wiring, swap connections, reprogram terminals. |
| F28 | Fieldbus timeout | Rapid stop (P) | No master-slave communication within the configured monitoring time. Check the master's communication routine; extend P819 or deactivate monitoring. |
| F29 | Limit switch contacted | Emergency stop | A hardware limit switch was reached in IPOSplus mode. Check the travel range and correct the user program. |
| F30 | Emergency stop timeout | Immediate disconnection | Drive overloaded or the emergency stop ramp is too short. Check the configuration; extend the ramp. |
| F31 | TF/TH sensor tripped | No response (P) | Motor too hot (TF/TH triggered), or the TF/TH is not connected correctly. Let the motor cool and reset; check the wiring; if no TF/TH is used, jumper X10:1 to X10:2 and set P835 to "No response". |
| F32 | IPOS index overflow | Emergency stop | Programming violations caused an internal stack overflow. Correct the IPOSplus user program. |
| F33 | Setpoint source | Immediate disconnection | Setpoint source not available (e.g. fieldbus with no card). Set the correct source in P100. |
| F34 | Ramp timeout | Immediate disconnection | The down-ramp time was exceeded, typically from overload. Extend the downward ramps; eliminate the overload. |
| F35 | Operating mode | Immediate disconnection | Operating mode not defined or not matched to the technology function (P916/P888 mismatch). Set the correct mode in P700/P701 and check P916 and P888. |
| F36 | Option missing | Immediate disconnection | Option card type not permitted, or setpoint/control source/operating mode not allowed with this card; wrong encoder type set for DIP11B. Fit the correct card; correct P100, P101, P700, and the encoder type. |
| F37 | System watchdog | Immediate disconnection | Error while executing system software. Consult SEW Service. |
| F38 | System software | Immediate disconnection | System malfunction. Consult SEW Service. |
| F39 | Reference travel | Immediate disconnection (P) | Reference cam missing or not switching, limit switches wired wrong, or the reference travel type was changed mid-travel. Check cam, connections, and travel-type settings. |
| F40 | Boot synchronization | Immediate disconnection | Boot synchronization between inverter and option card failed. Install a new option card if it recurs. |
| F41 | Watchdog option | Immediate disconnection | Communication error between system and option software; IPOSplus watchdog; or an application module loaded without the application version. Check P079/P078; consult SEW Service. |
| F42 | Lag error | Immediate disconnection (P) | Positioning lag: encoder connected incorrectly, ramps too short, P-gain or lag tolerance too small, or blocked mechanics. Check encoder and mechanics, extend ramps, raise the lag tolerance. |
| F43 | RS485 timeout | Rapid stop (P) | Communication via the RS485 interface (PC or DBG60B) dropped out. Check the connection. |
| F44 | Unit utilization | Immediate disconnection | IxT utilization exceeded 125%. Decrease output power, extend ramps, reduce the load; if that is not possible, use a larger inverter. |
| F45 | Initialization | Immediate disconnection | EEPROM parameters missing/incorrect or an option card not seated on the backplane bus. Restore factory settings; seat the card; consult SEW Service if it persists. |
| F46 | System bus 2 timeout | Rapid stop (P) | Communication error on system bus CAN2. Check the bus connection. |
| F47 | System bus 1 timeout | Rapid stop (P) | Communication error on system bus CAN1. Check the bus connection. |
| F48 | Hardware DRS | Immediate disconnection | Only with the DRS11B synchronous-operation card: faulty master/synchronous encoder signal or hardware. Check encoder signals and wiring; replace the card. |
| F77 | IPOS control word | No response (P) | Only in IPOSplus: an invalid automatic mode was set by the external control, or an invalid ramp type is selected. Check the serial link and written values; set a valid ramp type (P916). |
| F78 | IPOS SW limit switch | No response (P) | Programmed target position lies outside the software limit switches. Check the user program and the limit-switch positions. |
| F79 | Hardware configuration | Immediate disconnection | After a memory card swap, the power rating, voltage, variant, series, version, or option cards no longer match. Use identical hardware or restore the delivery condition (P802 factory setting). |
| F80 | RAM test | Immediate disconnection | Internal unit fault, RAM defective. Consult SEW Service. |
| F81 | Start condition | Immediate disconnection | VFC hoist mode only: the motor could not be magnetized correctly in the premagnetizing time (motor power too small versus the inverter, or motor cable cross-section too small). Check startup data, the motor connection, and cable cross-section. |
| F82 | Open output | Immediate disconnection | VFC hoist mode only: two or all output phases interrupted, or rated motor power too small versus the inverter. Check the motor connection and repeat startup if needed. |
| F84 | Motor protection | Emergency stop (P) | Motor utilization too high (thermal motor model). Reduce load, extend ramps, allow longer pauses; check P345/P346; select a larger motor if needed. |
| F86 | Memory module | Immediate disconnection | No memory card or a defective one. Insert and secure the card (tighten the knurled screw) or replace it. |
| F87 | Technology function | Immediate disconnection | A technology function was activated on a standard-version unit. Disable the technology function. |
| F88 | Flying start | Immediate disconnection | VFC n-CTRL mode only: actual speed exceeded 6000 rpm with the inverter enabled. Only enable at 6000 rpm or below. |
| F92 | DIP encoder problem | Error display (P) | Encoder signals an error; with a Stahl WCS3 the usual cause is a dirty encoder. Clean it. |
| F93 | DIP encoder error | Emergency stop (P) | Absolute encoder fault: power failure, cable not twisted-pair/shielded, cycle frequency too high for the cable length, max speed/acceleration exceeded, or defective encoder. Check connection and cables, set the correct cycle frequency, reduce speed or ramp, replace the encoder if needed. |
| F94 | EEPROM checksum | Immediate shut-off | Electronics disrupted, possibly EMC or an internal defect. Send the unit in for repair. |
| F95 | DIP plausibility error | Emergency stop (P) | No plausible position: wrong encoder type set, wrong IPOSplus travel parameters, wrong numerator/denominator factor, zero adjustment performed, or defective encoder. Correct the settings; reset after zero adjustment; replace the encoder if defective. |
| F97 | Copy error | Immediate disconnection | Parameter upload/download to the memory card failed or was cancelled. Repeat the copy; if needed restore the default (P802) first, then copy again. |
| F98 | CRC error | Immediate disconnection | Internal flash memory defective. Send the unit in for repair. |
| F99 | IPOS ramp calculation | Immediate disconnection | With a sinusoidal or square positioning ramp, ramp times or travel speeds were changed while enabled. Rewrite the IPOSplus program so they change only when the inverter is inhibited. |
| F100 | Vibration warning | Display error (P) | Vibration sensor warning (DUV10A). Find the cause; operation may continue until F101 occurs. |
| F101 | Vibration error | Rapid stop (P) | Vibration sensor reports an error. SEW recommends fixing the cause immediately. |
| F102 | Oil aging warning | Display error (P) | Oil aging sensor message. Schedule a gear-unit oil change. |
| F103 | Oil aging error | Display error (P) | Oil aging sensor error. Change the gear unit oil immediately. |
| F104 | Oil aging overtemperature | Display error (P) | Oil aging sensor reports overtemperature. Let the oil cool; check gear-unit cooling and the sensor supply voltage. |
| F105 | Oil aging ready signal | Display error (P) | Oil aging sensor not ready for operation. Check the sensor and its supply; replace if needed. |
| F106 | Brake wear | Display error (P) | Brake lining worn. Replace the brake lining. |
| F107 | Line components | Immediate disconnection | No feedback signal from the main contactor. Check the contactor and its control cables. |
| F108 | DCS error | Immediate stop/malfunction (P via P555) | DCS21B/31B safety-option fault: configuration transfer, wrong programming interface/version, faulty reference/system/test/24 V supply voltage, ambient temperature out of range, or output driver fault. Resend the configuration, check supply voltages, ambient temperature, and output wiring. |
| F109 | DCS alarm | Rapid stop/warning (P via P556) | DCS21B/31B safety alarm: no valid data from the inverter, plausibility errors on digital inputs DI1-DI8 (pulse 1/pulse 2), speed or position sensor disagreement, encoder interface/supply faults, or output driver faults. Check wiring and encoder connections against the configuration; use the SCOPE function to compare sensor signals. |
| F110 | Ex-e protection | Emergency stop | Operation below 5 Hz exceeded the permitted duration on an Ex-e protected drive. Shorten the time spent below 5 Hz. |
| F113 | Analog input open circuit | No response (P) | AI1 analog input open circuit. Check the wiring. |
| F116 | MOVI-PLC timeout | Rapid stop/warning | Communication timeout with the MOVI-PLC controller. Check startup settings and wiring. |
| F123 | Positioning interruption | Emergency stop (P) | An interrupted positioning move was resumed and the target would be overrun. Run the positioning process through to completion without interruption. |
| F124 | Ambient conditions | Emergency stop (P) | Ambient temperature above 60 °C. Improve ventilation and cabinet cooling; check filter mats. |
| F196 | Power section | Immediate disconnection | Internal power-section faults: precharge/discharge control, inverter coupling, mismatched phase modules, control-unit configuration, DC link fan, or implausible DC link voltage measurement per phase. Most sub-codes end at SEW Service or replacement of the coupling/control unit. |
| F197 | Power supply | Immediate disconnection | Line overvoltage or undervoltage from poor line quality. Check fuses, contactor, and supply configuration. |
| F199 | DC link charging | Immediate disconnection | The DC link could not charge: precharge overload, too much connected DC link capacitance, or a short in the DC link. Check the DC link connections, especially with multiple units on a shared bus. |

## Sub-error codes for the most common faults

The sub-error code (read it in MotionStudio 4.50+ or on the DBG60B) narrows a fault family to the exact failing element. Here are the tables you will actually use in the field.

### F01 Overcurrent

| Sub | Meaning |
| --- | --- |
| 0 | Output stage fault (short circuit at output, motor too large, defective output stage) |
| 1 | VCE monitoring or gate-driver undervoltage monitoring |
| 5 | Inverter stuck in hardware current limit (ramp limit deactivated and ramp time too short: activate P138 and/or extend the ramp) |
| 6 / 7 / 8 | Phase module monitoring, phase U / V / W (defective phase module, unstable 24 V supply, or interrupted/shorted signal lines from the phase modules) |
| 9 / 10 / 11 / 12 | The same, phases U+V / U+W / V+W / U+V+W |
| 13 | Voltage supply, current converter in mains-operation status |
| 14 | MFE signal lines |

### F07 DC link overvoltage

| Sub | Meaning |
| --- | --- |
| 0 / 1 | DC link voltage too high in 2Q operation |
| 2–4 | DC link voltage too high in 4Q operation, identified per phase (U/V/W) |

All variants have the same first fixes: extend the deceleration ramps, then check the braking resistor supply cable and the resistor's technical data against spec.

### F08 Speed monitoring

| Sub | Meaning |
| --- | --- |
| 0 | Inverter in current limit or slip limit |
| 3 | "Actual speed" system limit exceeded: speed difference between ramp setpoint and actual value stayed above expected slip for twice the ramp time |
| 4 | Maximum rotating field speed exceeded (output frequency reached 150 Hz in VFC mode, or 600 Hz in V/f mode) |

On hoists, do not paper over F08 by deactivating speed monitoring (P500/P502) or stretching the delay time (P501/P503): per SEW's own footnote, that cannot safely prevent the hoist from sagging. Find the mechanical or electrical cause.

### F09 Startup

| Sub | Meaning |
| --- | --- |
| 0 | Startup (commissioning) missing |
| 1 | Wrong operating mode selected |
| 2 | Wrong encoder type set or defective encoder card |

### F11 Overtemperature

| Sub | Meaning |
| --- | --- |
| 0 | Heat sink temperature too high or temperature sensor defective |
| 3 | Overtemperature of the switched-mode power supply |
| 6 / 7 / 8 | Heat sink temperature/sensor, phase U / V / W (size 7 units) |

If F11 appears when the drive is clearly not hot, SEW's manual says that points to a faulty phase-module temperature sensor; on size 7 units the fix is replacing the phase module.

### F14 Encoder

| Sub | Meaning |
| --- | --- |
| 0 | Encoder not connected, defective encoder, or defective encoder cable |
| 25 | X15 speed range exceeded (encoder at X15 turning faster than 6542 rpm) |
| 26 | X15 card defective (error in quadrant evaluation) |
| 27 | Encoder connection or encoder defective |
| 28 | X15 RS485 communication error |
| 29 | X14 RS485 communication error |
| 30 | Unknown encoder type at X14/X15 |
| 31 | Hiperface plausibility error X14/X15 (increments lost) |
| 32 | Hiperface encoder at X15 signals an error |
| 33 | Hiperface encoder at X14 signals an error |
| 34 | X15 resolver error (encoder connection or encoder defective) |

For every F14 variant, start the same way: check the encoder cable and shield for correct connection, short circuit, and broken wires before replacing the encoder or the option card.

### F25 EEPROM

| Sub | Meaning |
| --- | --- |
| 0 | Read or write error on the power-section EEPROM |
| 11 | NV memory read error (NV-RAM inside the unit) |
| 13 | Memory card: system module defective |
| 14 | Memory card defective |
| 16 | NV memory initialization error |

Sub-codes 13 and 14 mean replace the memory card; the others start with factory settings, reset, and re-entering parameters.

## How to reset a fault

SEW gives five ways to acknowledge a fault on MOVIDRIVE B:

1. Switch the supply off and back on. Keep the supply contactor (K11) off for at least 10 seconds.
2. Reset via a binary input assigned to reset (DI01-DI07 on the basic unit, DI10-DI17 with the DIO11B option).
3. Manual reset in the SHELL software (P840 = "YES" or Parameter/Manual reset).
4. Manual reset on the DBG60B keypad.
5. Auto reset, which performs up to five resets with an adjustable restart time.

One hard warning from the manual: do not use auto reset on any drive where an automatic restart endangers people or equipment. The motor can start on its own after an auto reset. On hoists, conveyors feeding people-adjacent stations, or anything with a pinch point, use manual reset only.

Also note: if the drive is controlled over a fieldbus, RS485, or SBus and you power cycle or reset it, the enable stays ineffective until the drive receives valid data over that interface again.

## Safety: when to stop and call a pro

Several of these faults put you in front of lethal voltage. The DC link capacitors hold a dangerous charge after the supply is removed. Lock out and tag out, wait the discharge time stated on the unit and in the manual, and verify zero volts at the DC link with a meter before touching power terminals, the braking resistor circuit, or motor leads.

Treat these as electrician-or-SEW territory, not operator fixes: F03 ground faults (insulation testing motor and cable at line potential), F04/F07 braking-resistor circuit work, F06/F197 supply-side investigation, and anything the table marks "send in for repair" (F94, F98) or "consult SEW Service" (F37, F38, F80, most F196 sub-codes). Repeatedly resetting a drive into a hard fault like F01 or F03 risks turning a wiring fault into a destroyed output stage.

## When to contact SEW-Eurodrive service

If a fault will not clear, SEW's electronics service will want the digits from the status label plus, if you send the unit in: the serial number from the nameplate, unit designation, standard or application version, a short description of the application and control method (terminals or serial), the connected motor type/voltage/connection, the nature of the fault, accompanying circumstances, and any unusual events that preceded it. Pulling the P080 fault memory contents before you call makes that conversation much shorter.

## Frequently asked questions

### My display only flashes numbers. How do I get the sub-error code?

The 7-segment display shows only the main fault code, one digit at a time. The sub-error code is displayed in MOVITOOLS MotionStudio from version 4.50, or on the DBG60B keypad. If you troubleshoot MOVIDRIVE B units regularly, a DBG60B or a laptop with MotionStudio is worth keeping on the cart, because for faults like F14 (11 sub-codes) or F109 (dozens) the main code alone barely narrows the search.

### What does "(P)" next to the fault response mean?

The factory-set reaction (immediate disconnection, rapid stop, emergency stop, or no response) is programmable for that fault via the P83x error-response parameters or IPOSplus. Faults 108 and 109 are the exception: their responses are set in P555 (DCS error response) and P556 (DCS alarm response).

### The drive shows F79 after I swapped the memory card. Is the card bad?

Usually not. F79 (hardware configuration) means the new inverter does not match what the card expects: power rating, rated voltage, variant, unit series, application/standard version, or installed option cards. Either fit identical hardware or restore the delivery condition with P802 (factory setting), then restart and recommission.

### Can I just extend the delay time to stop nuisance F08 trips on my hoist?

No. P501/P503 delay time and P500/P502 monitoring exist to catch a drive that cannot follow its setpoint, and SEW's manual warns that deactivating the monitoring or setting the delay too long cannot safely prevent a hoist from sagging. Nuisance F08 on a hoist means something real: mechanical overload, a lost mains or motor phase, an encoder wired backwards (swap the A/A and B/B pairs), or a current limit set too low. Fix that instead.

### Are MOVITRAC B fault codes the same as MOVIDRIVE B?

They overlap heavily (F01, F03, F04, F06, F07, F08, F11, and others carry the same names) but the tables are not identical, and some causes differ; for example, MOVITRAC B units with a heat-sink-integrated braking resistor have an extra F11 cause that MOVIDRIVE B does not. Always use the fault table for the product family in front of you.

## Sources

- Compact Operating Instructions – MOVIDRIVE MDX60B/61B (SEW-Eurodrive document 16920813), Section 6.2.3 "Error list": [archived official PDF](https://web.archive.org/web/20130124101658/http://download.sew-eurodrive.com/download/pdf/16920813.pdf)
- Operating Instructions – MOVIDRIVE MDX60B/61B Inverter (SEW-Eurodrive document 11696613), manufacturer's canonical source: [download.sew-eurodrive.com](https://download.sew-eurodrive.com/download/pdf/11696613.pdf)
- MOVITRAC B Operating Instructions 2009-05 (SEW-Eurodrive document 16810813), Section 7.2 "List of faults," used for the MOVITRAC B cross-checks: [archived official PDF](https://web.archive.org/web/20210805131920/https://download.sew-eurodrive.com/download/pdf/16810813.pdf)
