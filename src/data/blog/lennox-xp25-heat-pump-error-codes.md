---
title: "Lennox XP25 Heat Pump Error Codes - iComfort Fault Diagnostics"
description: "Full fault code reference for the Lennox XP25 variable-speed heat pump, covering all iComfort S30 reported numeric codes, communicating system diagnostics, and control board faults. Includes diagnosis steps and parts for homeowners and HVAC technicians."
pubDatetime: 2026-04-25T00:00:00Z
author: "Dana Kowalski"
tags:
  - hvac
  - error-codes
---

The Lennox XP25 sits at the top of Lennox's residential heat pump lineup, a fully variable-speed inverter-driven system that pairs with the iComfort S30 smart thermostat. Unlike conventional systems that blink LED codes and call it a day, the XP25 uses a full communicating network (Lennox calls it the iComfort system bus) to report detailed numeric fault codes directly on the thermostat screen. This guide covers every fault code you'll encounter, what each means mechanically, and how to diagnose and fix it.

## What Does a Lennox XP25 Error Code Mean?

The XP25 reports faults in two ways. The **iComfort S30 thermostat** displays numeric alarm codes on its screen under the Alerts menu. The **outdoor unit control board** also has a diagnostic LED that blinks a simplified version of the fault for techs working without thermostat access.

The iComfort system distinguishes between **alerts** (warnings that haven't shut the system down yet) and **alarms** (faults that have caused a lockout). Both show on the thermostat; alarms display with a red indicator.

### iComfort Numeric Fault Code Reference

| Code | Fault Description |
|------|-----------------|
| 125 | High-pressure switch trip, outdoor high side exceeded cutout |
| 126 | Low-pressure switch trip, suction pressure fell below cutout |
| 128 | Loss of charge / low refrigerant pressure alert |
| 134 | Outdoor unit fan motor fault |
| 140 | Outdoor ambient temperature sensor failure |
| 141 | Outdoor coil temperature sensor failure |
| 144 | Discharge temperature sensor failure |
| 145 | Suction temperature sensor failure |
| 146 | Liquid line temperature sensor failure |
| 160 | Inverter communication fault, iQ Drive module not responding |
| 161 | Inverter fault, iQ Drive internal error (overcurrent, overtemp, undervoltage) |
| 162 | Compressor fault, iQ Drive detected locked rotor or phase loss |
| 170 | Control board internal fault |
| 175 | Communication bus fault, outdoor unit lost communication with iComfort system |
| 178 | Indoor unit communication fault, no signal from air handler |
| 180 | Reversing valve fault |
| 185 | Defrost system fault |
| 191 | EEV (electronic expansion valve) fault |
| 195 | Outdoor unit voltage fault, supply voltage out of range |

### Understanding the iQ Drive System

The XP25's variable-speed operation comes from Lennox's iQ Drive inverter module, a variable frequency drive that controls compressor speed in response to real-time load calculations. Codes 160–162 all relate to this module. The iQ Drive module communicates with the main control board over a dedicated serial interface; if that link breaks (code 160), the system shuts down entirely since the main board has no way to control compressor speed safely.

Code 161 (iQ Drive internal fault) is a catch-all for conditions the drive detects within itself: DC bus overvoltage, DC bus undervoltage, output overcurrent, module overtemperature. The drive stores a sub-fault code internally that a Lennox service tool can read via the USB port on the module, if you have a tech with the Lennox service tool laptop kit, pull the sub-code before ordering parts.

Code 162 (compressor fault) means the iQ Drive tried to start the compressor but couldn't, either the rotor is mechanically locked, one or more compressor windings are open, or there's a phase-to-ground fault. This code almost always means compressor replacement.

**EEV fault (code 191)** is unique to the XP25 and its variable-capacity counterparts. The electronic expansion valve modulates refrigerant flow to match the inverter's output. A failed EEV or its stepper motor driver will cause poor performance, high superheat, and eventually a high-pressure or discharge temperature fault. The EEV is an Alco or Danfoss unit; Lennox part number **13W75** covers the EEV driver board.

## How to Fix It

### For High/Low Pressure Faults (Code 125, 126, 128)

1. At the thermostat, go to Settings → Advanced → Service Diagnostics and check how many times the fault has occurred and how recently.
2. A single trip that cleared itself is often a transient condition (brief power surge, temporary airflow restriction). A fault that trips repeatedly is a real problem.
3. Check outdoor coil airflow: clean the coil with a fin comb and garden hose if fouled, ensure nothing is blocking airflow within 24 inches of the unit.
4. Connect a manifold gauge set and run the unit in the mode that triggers the fault. For code 125 (high pressure): check high-side pressure, should stay below 580 psig on R-410A at normal conditions. For code 126 (low pressure): suction should stay above 100 psig in cooling at 75°F indoor.
5. Abnormal pressures with normal airflow point to a refrigerant issue (overcharge, undercharge, restriction, or non-condensables). These require a licensed tech.
6. Normal pressures with a repeated pressure fault: check continuity of the pressure switch, inspect wiring between switch and control board.

### For Sensor Faults (Codes 140–146)

1. Identify which sensor is reporting. The outdoor ambient sensor mounts on the coil guard or control box bracket; the coil sensor clips directly to the coil; discharge and suction sensors clamp onto the refrigerant lines.
2. Disconnect the suspect sensor and measure resistance with a multimeter. Lennox sensors are 10k NTC thermistors, expect approximately 10,000 ohms at 77°F. An open circuit or zero resistance confirms failure.
3. Inspect sensor wiring for chafing against the unit cabinet or pinching at the control box entry.
4. Replace the faulty sensor. Most XP25 sensors use Lennox part **10W91** (outdoor sensors) or **47W83** (line temperature sensors).

### For iQ Drive/Inverter Faults (Codes 160–162)

1. For code 160 (communication fault): power cycle the entire system, breaker off, outdoor disconnect off, wait 60 seconds, restore in reverse order. Communication faults sometimes result from startup sequencing issues.
2. Check the serial communication cable between the main control board and the iQ Drive module. It's a small multi-conductor harness that plugs into both boards. Reseat both connectors.
3. For code 161 (iQ Drive internal): check incoming L1-L2 voltage at the contactor (208–240VAC). Check for loose connections at the drive input terminals. Inspect the drive heat sink, the drive mounts to the inside of the unit cabinet with fins that must stay clean.
4. For code 162 (compressor fault): measure winding resistance across all three pairs of compressor leads. Equal resistance in the 2–8 ohm range is normal. Any open winding (OL) or phase-to-ground fault confirms compressor failure.
5. iQ Drive replacement requires Lennox factory-matched parts and specific startup procedures, do not substitute a generic VFD.

### For Communication Faults (Codes 175, 178)

1. Check the communication wiring between all components. The iComfort system uses a 4-wire bus. Verify wires are connected to correct terminals (A, B, R, C) at both ends.
2. Turn off power to all components, then restore power to the air handler first, then the outdoor unit, then apply thermostat power last. The bus initializes in sequence.
3. On the iComfort S30, go to Settings → Equipment → Outdoor Unit and check if the unit is recognized. If it shows as "Not Connected," the outdoor board or its bus transceiver has failed.

### For EEV Fault (Code 191)

1. Turn off power and inspect the EEV motor connector on the outdoor control board. Reseat the connector and power cycle.
2. If fault returns immediately, the EEV driver circuit on the control board may have failed. Check for 12VDC at the EEV drive output, absence confirms driver failure.
3. EEV replacement requires recovering refrigerant, replacing the valve, evacuating, and recharging, licensed tech work.

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| [Lennox Outdoor Temperature Sensor 10W91](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-lennox-xp25-heat-pump-error-codes&tag=errorcodefixes-20) | Replace on sensor faults 140, 141; clips to coil or bracket | $20–$45 |
| [Lennox Line Temperature Sensor 47W83](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-lennox-xp25-heat-pump-error-codes&tag=errorcodefixes-20) | Discharge, suction, and liquid line sensors; faults 144, 145, 146 | $20–$45 |
| [Lennox XP25 Control Board](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-lennox-xp25-heat-pump-error-codes&tag=errorcodefixes-20) | Main outdoor board; required for persistent code 170 or EEV driver faults | $200–$450 |
| [High Pressure Switch for Lennox Heat Pump](https://www.amazon.com/dp/B013IHQ8CU?ascsubtag=ecf-lennox-xp25-heat-pump-error-codes&tag=errorcodefixes-20) | Trips on code 125; test continuity before replacing | $25–$60 |
| [iComfort S30 Smart Thermostat](https://www.amazon.com/s?ascsubtag=ecf-lennox-xp25-heat-pump-error-codes&k=Lennox+iComfort+S30+thermostat&tag=errorcodefixes-20) | Required for full fault code visibility on the XP25 | $200–$350 |
| [Fin Comb HVAC Coil Cleaner Tool](https://www.amazon.com/s?ascsubtag=ecf-lennox-xp25-heat-pump-error-codes&k=HVAC+fin+comb+coil+cleaning+tool&tag=errorcodefixes-20) | Straighten bent fins that restrict airflow and cause high-pressure trips | $15–$30 |

## When to Call a Pro

Any fault code involving refrigerant pressures, compressor diagnosis, or the iQ Drive module should be handled by a licensed technician:

- **Code 162 (compressor fault):** Compressor replacement on the XP25 means recovering refrigerant, removing the inverter drive, and installing a matched replacement compressor, not DIY territory.
- **Code 161 with confirmed drive failure:** iQ Drive modules are system-matched and expensive. Lennox requires factory-authorized installation to maintain warranty.
- **Code 191 (EEV fault) with confirmed valve failure:** Requires refrigerant recovery and brazing.
- **Repeated 125/126 faults with abnormal pressures:** The system has a refrigerant problem, leak search, repair, evacuation, and recharge requires EPA 608 certification.
- **Warranty work:** The XP25 carries a 10-year parts warranty when registered. Any repair that could affect warranty coverage should go through a Lennox dealer.

Sensor replacements, pressure switch swaps, and communication wiring troubleshooting are appropriate for a confident DIYer or a general-service tech.

## Frequently Asked Questions

**Q: My iComfort S30 shows multiple fault codes at the same time. Which one do I fix first?**
A: Start with the highest-numbered code, iComfort displays faults in the order they occurred, and cascading failures often trace to one root cause. For example, a code 126 (low pressure) followed by codes 140 and 144 usually means a refrigerant undercharge caused suction temperature anomalies, not three separate failures. Fix the root cause first.

**Q: The XP25 runs but only at low speed and won't ramp up. No fault codes showing. What's happening?**
A: This usually means the iQ Drive is in a "limp mode", it detected a condition that isn't severe enough to fault out but throttled compressor speed to protect itself. Check the iComfort Alert history for any recent cleared faults. Also check incoming line voltage: if L1-L2 is below 200VAC, the drive will limit output.

**Q: How do I access the service diagnostics on the iComfort S30?**
A: On the S30 touchscreen, go to the main menu → Settings (gear icon) → Advanced → Service. You'll need to enter the installer PIN (default 1234 unless your installer changed it). Service diagnostics shows live sensor readings, fault history, and runtime data for each component.

**Q: The XP25 shows code 180 (reversing valve fault) but the unit runs fine in one mode. Is it safe to keep running it?**
A: Yes, temporarily. If the unit is stuck in cooling mode and it's winter, that's a problem. But if it's cooling correctly during summer and the fault appeared during a heating call that you don't need right now, you can run it in cooling mode safely while waiting for service. Don't ignore the fault, a reversing valve that partially sticks can cause refrigerant slugging and compressor damage over time.
