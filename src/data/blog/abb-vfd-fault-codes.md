---
title: "ABB VFD Fault Codes — ACS550, ACS880, ACS310 Reference"
description: "ABB VFD fault codes: complete reference for ACS310, ACS355, ACS550, ACS580, and ACS880 drives including 3130, 3210, and overcurrent faults."
pubDatetime: 2026-04-22T16:00:00Z
modDatetime: 2026-04-22T16:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - abb
---

## ABB VFD Fault Codes — Quick Reference

ABB drives display fault codes on the integral keypad panel as four-digit numbers or abbreviated text. Faults cause the drive to trip and stop the motor; alarms display but don't stop the drive. The fault history is stored in the drive's memory and can be retrieved via the control panel or Drive Composer software.

| [Fault Code](https://www.amazon.com/s?k=Fault%20Code&tag=errorcodefixe-20) | Meaning | Common Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ----------- |---------|-----------|
| 0001 | [Overcurrent](https://www.amazon.com/s?k=Overcurrent&tag=errorcodefixe-20) | Check motor/cable; reduce accel ramp |
| [2201](https://www.amazon.com/s?k=2201&tag=errorcodefixe-20) | Overcurrent (short circuit) | Motor winding short or cable fault | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 2310 | Overcurrent (peak) | [Check for mechanical jam](https://www.amazon.com/s?k=Check%20for%20mechanical%20jam&tag=errorcodefixe-20) |  | 3130 | [Input phase loss](https://www.amazon.com/s?k=Input%20phase%20loss&tag=errorcodefixe-20) | Check all 3 input phases |
| [3210](https://www.amazon.com/s?k=3210&tag=errorcodefixe-20) | DC bus overvoltage | Extend decel ramp; add brake resistor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 3300 | DC bus undervoltage | [Check input power supply](https://www.amazon.com/s?k=Check%20input%20power%20supply&tag=errorcodefixe-20) |  | 4110 | [Drive overtemperature](https://www.amazon.com/s?k=Drive%20overtemperature&tag=errorcodefixe-20) | Clean cooling fan; check ambient temp |
| [5010](https://www.amazon.com/s?k=5010&tag=errorcodefixe-20) | Overload | Reduce continuous load; check motor FLA | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 7121 | Analog I/O fault | [Check signal wiring](https://www.amazon.com/s?k=Check%20signal%20wiring&tag=errorcodefixe-20) |  | 9300 | [Communication fault](https://www.amazon.com/s?k=Communication%20fault&tag=errorcodefixe-20) | Check fieldbus adapter or wiring |
| [AF10](https://www.amazon.com/s?k=AF10&tag=errorcodefixe-20) | Heatsink overtemperature | Clean fan; check airflow | [## Most Common Codes

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

## Parts Often Needed](https://www.amazon.com/s?k=%23%23%20Most%20Common%20Codes%0A%0A%23%23%23%20Fault%203130%3A%20Input%20Phase%20Loss%0AOne%20of%20the%20three%20supply%20phases%20(L1%2C%20L2%2C%20or%20L3)%20is%20missing%20or%20has%20significantly%20reduced%20voltage.%20Check%20the%20input%20fuses%20(one%20per%20phase)%20%E2%80%94%20a%20blown%20fuse%20on%20one%20phase%20is%20the%20most%20common%20cause.%20Also%20check%20the%20main%20contactor%20(if%20installed)%20for%20a%20burned%20contact.%20Measure%20phase-to-phase%20voltage%20at%20the%20drive's%20L1%2FL2%2FL3%20input%20terminals.%0A%0AABB%20drives%20will%20attempt%20to%20run%20on%20two%20phases%20briefly%20before%20tripping%203130.%20If%20the%20fault%20appears%20intermittently%2C%20check%20for%20a%20loose%20terminal%20screw%20or%20a%20contact%20with%20high%20resistance%20under%20load.%0A%0A%23%23%23%20Fault%202310%3A%20Overcurrent%20(Peak)%0AAn%20instantaneous%20overcurrent%20trip%20%E2%80%94%20the%20drive%20output%20current%20exceeded%20the%20trip%20threshold.%20Causes%3A%20motor%20winding%20short%2C%20cable%20insulation%20failure%2C%20locked%20rotor%20(mechanical%20jam)%2C%20or%20too-fast%20acceleration%20ramp.%20Start%20by%20megger-testing%20the%20motor%20and%20cable%20for%20insulation%20resistance%20(should%20be%20%3E1%20M%CE%A9%20at%20500V).%20If%20insulation%20is%20good%2C%20check%20for%20mechanical%20issues%20and%20extend%20the%20acceleration%20time.%0A%0A%23%23%23%20Fault%203210%3A%20DC%20Bus%20Overvoltage%0ARegenerative%20energy%20from%20a%20decelerating%20motor%20raised%20the%20DC%20bus%20above%20the%20trip%20threshold.%20Solutions%3A%20(1)%20extend%20the%20deceleration%20ramp%20in%20parameter%20group%2023%20(ACS550)%20or%2001.13%20(ACS880)%2C%20(2)%20enable%20the%20flux%20braking%20feature%20(available%20on%20ACS880%20%E2%80%94%20uses%20motor%20resistance%20to%20dissipate%20energy)%2C%20(3)%20install%20a%20dynamic%20braking%20resistor%20and%20chopper%20module%20for%20high-inertia%20loads.%0A%0A%23%23%23%20Fault%203300%3A%20DC%20Bus%20Undervoltage%0AInput%20supply%20voltage%20dropped%20too%20low.%20Check%20incoming%20voltage%20at%20the%20drive%20terminals%20under%20load.%20On%20ACS550%20and%20ACS880%20with%20a%20380%E2%80%93480V%20supply%2C%20the%20minimum%20is%20approximately%20270V%20DC%20bus%20(~338V%20AC%20input).%20A%20weak%20transformer%2C%20long%20cable%20runs%2C%20or%20undersized%20input%20conductors%20all%20contribute.%0A%0A%23%23%23%20Fault%204110%3A%20Drive%20Overtemperature%0AThe%20drive's%20IGBT%20heatsink%20exceeded%20its%20temperature%20limit.%20Open%20the%20drive%20cabinet%20and%20inspect%3A%20(1)%20internal%20cooling%20fan%20%E2%80%94%20is%20it%20spinning%3F%20A%20failed%20fan%20is%20the%20%231%20cause%2C%20(2)%20heatsink%20fins%20%E2%80%94%20clear%20with%20compressed%20air%20if%20clogged%20with%20dust%2C%20(3)%20ambient%20temperature%20%E2%80%94%20ACS550%2FACS880%20are%20rated%20to%2040%C2%B0C%20ambient%20without%20derating.%20Above%20that%2C%20the%20drive%20must%20be%20derated%20or%20better%20ventilation%20provided.%0A%0A%23%23%23%20Fault%200001%20%2F%202201%3A%20Overcurrent%0AThe%20drive%20output%20stage%20detected%20overcurrent%20above%20trip%20level.%20On%20ACS880%2C%20separate%20cause%20analysis%20is%20needed%3A%20fault%202201%20(overcurrent%20on%20ground%20fault%20or%20winding%20short)%20is%20more%20serious%20than%20fault%200001%20(transient%20overcurrent%20during%20starting).%20For%202201%2C%20use%20a%20megger%20before%20restarting%20%E2%80%94%20a%20shorted%20motor%20winding%20can%20damage%20the%20drive's%20output%20IGBTs.%0A%0A%23%23%23%20Fault%209300%3A%20Communication%20Fault%0AOn%20ACS550%2FACS880%20drives%20with%20fieldbus%20adapters%20(Profibus%2C%20EtherNet%2FIP%2C%20Modbus)%2C%20fault%209300%20indicates%20loss%20of%20communication%20with%20the%20master.%20Check%3A%20adapter%20module%20is%20seated%20securely%2C%20fieldbus%20cable%20is%20connected%2C%20PLC%2Fmaster%20is%20running%20and%20communicating.%20Fault%209300%20can%20also%20mean%20the%20communication%20response%20time%20exceeded%20the%20configured%20watchdog%20timeout.%0A%0A%23%23%20Retrieving%20Fault%20History%0A%0AOn%20ACS550%3A%20Navigate%20to%20parameter%20group%2014%20(FAULT%20HISTORY).%20Parameters%2014.01%E2%80%9314.03%20show%20the%20three%20most%20recent%20faults%20with%20time%20stamps.%0A%0AOn%20ACS880%3A%20Use%20the%20Drive%20Composer%20PC%20tool%20for%20the%20full%20fault%20log%2C%20or%20navigate%20to%20Menu%20%3E%20Diagnostics%20%3E%20Fault%20Log%20on%20the%20control%20panel.%0A%0A%23%23%20Parts%20Often%20Needed&tag=errorcodefixe-20) | Part | Notes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |-------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Input fuses | ABB class J or gR fuses; size per drive catalog | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Braking resistor | ABB catalog OHBR or third-party sized per drive kW | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Cooling fan | Drive-specific; ABB part for ACS550 fan: 68518560 | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Fieldbus adapter | FCAN-01 (CAN), FPBA-01 (Profibus), FENA-21 (EIP) |

## When to Call a Pro
Faults 2201 (short circuit overcurrent) and any fault accompanied by a burning smell or blown fuses require qualified drive service. ABB's regional service centers offer warranty and post-warranty repair.
