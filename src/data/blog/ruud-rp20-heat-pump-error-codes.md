---
title: "Ruud Prestige RP20 Heat Pump Error Codes - Full Fault Code Reference"
description: "Complete guide to Ruud Prestige RP20 heat pump error codes including LED flash codes, communicating thermostat faults, reversing valve issues, and refrigerant faults. Covers diagnosis steps and replacement parts for homeowners and HVAC techs."
pubDatetime: 2026-04-25T00:00:00Z
author: "Marcus Webb"
tags:
  - hvac
  - error-codes
---

The Ruud Prestige RP20 is Ruud's top-of-the-line variable-speed heat pump, featuring a two-stage compressor, ECM fan motor, and full compatibility with Ruud's EcoNet communicating thermostat system. When something goes wrong, the RP20 uses both LED flash codes on the control board and numeric fault codes reported through the EcoNet display. This guide covers every code you're likely to encounter, what each one means, and how to fix it.

## What Does a Ruud RP20 Error Code Mean?

The RP20 communicates faults two ways. First, the **control board LED** on the unit's circuit board blinks a sequence, a number of rapid flashes followed by a pause, that maps to a specific fault. Second, if you have the **Ruud EcoNet Smart Thermostat** (or a compatible communicating stat), fault codes appear as alphanumeric codes on the thermostat display.

### LED Flash Code Reference

| Flash Pattern | Fault Description |
|---------------|------------------|
| 2 flashes | High pressure lockout, system tripped high-side pressure switch |
| 3 flashes | Low pressure lockout, system tripped low-side pressure switch |
| 4 flashes | Open high-pressure switch, wiring or switch failure |
| 5 flashes | Open low-pressure switch, wiring or switch failure |
| 6 flashes | Outdoor ambient temperature sensor fault |
| 7 flashes | Outdoor coil temperature sensor fault |
| 8 flashes | Discharge line temperature sensor fault |
| 9 flashes | Suction line temperature sensor fault |
| 10 flashes | Inverter drive fault, variable-speed compressor drive error |
| 11 flashes | Communication fault, loss of signal between thermostat and outdoor unit |
| 12 flashes | Reversing valve stuck or failed to switch |
| 13 flashes | Defrost board fault |

Count the flashes carefully: the board pauses between complete sequences. A "3-flash" fault is three rapid blinks, a pause of about 3 seconds, then three more blinks. Repeat until you've counted two complete identical sequences before pulling the service panel.

### EcoNet Communicating Fault Codes

When paired with the EcoNet system, the RP20 reports alphanumeric codes:

| Code | Meaning |
|------|---------|
| E1 | High pressure fault, exceeded cutout pressure (typically 610 psig on R-410A) |
| E2 | Low pressure fault, fell below cutout (typically 54 psig) |
| E3 | Discharge temperature exceeded limit (240°F cutout) |
| E4 | Outdoor coil sensor open or shorted |
| E5 | Ambient temperature sensor open or shorted |
| E6 | Suction temperature sensor fault |
| E7 | Inverter/drive communication error |
| E8 | Reversing valve fault, failed to energize or de-energize |
| E9 | Defrost cycle fault |
| F1 | Loss of communication with indoor air handler |
| F2 | Loss of communication with thermostat |
| F3 | Control board internal memory fault |

**Reversing valve faults (E8/12 flashes)** are worth calling out specifically. The RP20 uses a solenoid-operated reversing valve to switch between heating and cooling modes. Faults here usually mean one of three things: the solenoid coil has failed, the 24V signal from the control board isn't reaching the solenoid, or the valve itself is mechanically stuck. A stuck valve will often let the unit start but blow cold air in heat mode (or warm air in cool mode). Check for 24V at the solenoid terminals before condemning the valve body.

**Inverter drive faults (E7/10 flashes)** are the most technically involved. The RP20's variable-speed compressor runs off an inverter module that converts 240V single-phase power to variable-frequency drive output. Drive faults can come from overvoltage, undervoltage, overtemperature on the drive module itself, or a locked rotor condition in the compressor. Check incoming voltage (should be 208–240V ±10%), check the drive heat sink for debris or a failed cooling fan, then check compressor winding resistance before assuming the drive itself is bad.

## How to Fix It

### For High/Low Pressure Faults (E1, E2, 2 or 3 flashes)

1. Turn the thermostat to OFF and let the unit sit for 10 minutes to allow pressures to equalize and the lockout timer to reset.
2. Check outdoor unit airflow: inspect for blocked coils (debris, vegetation, snow), bent fins, or a failed outdoor fan motor.
3. With a manifold gauge set, check static refrigerant pressures. For R-410A at 70°F ambient, expect roughly 120 psig on the suction side and 280–320 psig on the high side at idle.
4. If pressures are abnormal, do not add refrigerant without finding the leak. A system that repeatedly trips low pressure is leaking.
5. If pressures are normal and the fault is intermittent, suspect a faulty pressure switch, check ohms across the switch terminals (should be closed/continuity at normal pressures).
6. Replace a faulty pressure switch. The RP20 uses Ruud part **42-25101-83** for the high-pressure switch and **42-25101-84** for the low-pressure switch.

### For Sensor Faults (E4, E5, E6, 6, 7, or 9 flashes)

1. Disconnect the sensor connector from the control board and measure resistance with a multimeter. A good 10k NTC thermistor reads approximately 10,000 ohms at 77°F. An open circuit (OL) or short (0 ohms) confirms the sensor is bad.
2. Inspect the sensor harness for pinched or chewed wiring near the base pan or conduit entry.
3. Replace the faulty sensor. Ruud uses a common 10k NTC thermistor across multiple sensor positions; OEM replacement is **42-25101-10P**.

### For Communication Faults (F1, F2, 11 flashes)

1. Check the thermostat wiring at both ends (thermostat sub-base and outdoor unit terminal block). The EcoNet system uses a 4-wire communicating connection: R, C, and two data wires (typically labeled A and B or D1 and D2).
2. Measure 24VAC between R and C at the outdoor unit terminal block. If absent, check the transformer in the air handler.
3. Swap the A/B data wire polarity at one end, communicating systems are sometimes polarity-sensitive.
4. If wiring checks out, cycle power to both indoor and outdoor units simultaneously. Communication faults sometimes result from firmware timing mismatches that clear on a hard reset.
5. If fault persists after reset, connect a laptop with Ruud's service tool software to the EcoNet port to check firmware versions on both boards.

### For Reversing Valve Faults (E8, 12 flashes)

1. Verify the unit is calling for the correct mode (heat vs. cool) at the thermostat.
2. Check for 24VAC across the O/B reversing valve terminals at the outdoor unit. Presence of voltage confirms the control board is sending the signal.
3. If voltage is present, measure resistance across the reversing valve solenoid coil. A good coil reads 15–40 ohms. An open coil means the solenoid needs replacement.
4. If coil resistance is good but the valve is stuck, the valve body itself has failed mechanically. This requires refrigerant recovery, valve replacement, and system recharge, a licensed tech job.

### For Inverter Drive Faults (E7, 10 flashes)

1. Check incoming voltage at the contactor: should be 208–240VAC L1 to L2.
2. Inspect the drive module (mounted on the inside of the unit cabinet) for signs of overheating, burnt smell, discoloration, swollen capacitors.
3. Check compressor winding resistance: disconnect all three compressor leads and measure T1-T2, T2-T3, T1-T3. Values should be equal and low (under 10 ohms). Any open winding means compressor replacement.
4. If compressor checks out and drive is overheating, clean the drive heat sink fins and verify the drive cooling fan is spinning.
5. A confirmed failed drive module requires replacement, part number varies by tonnage; confirm with the unit's data plate.

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| [Ruud High Pressure Switch 42-25101-83](https://www.amazon.com/dp/B013IHQ8CU?tag=errorcodefixes-20) | Trips on E1 fault; replace if switch fails to close at normal pressures | $25–$55 |
| [Ruud Low Pressure Switch 42-25101-84](https://www.amazon.com/dp/B013J2J97A?tag=errorcodefixes-20) | Trips on E2 fault; replace if suction pressure is normal but fault persists | $25–$55 |
| [Ruud NTC Thermistor Sensor 42-25101-10P](https://www.amazon.com/s?i=industrial&k=Ruud+NTC+thermistor+sensor+10k+heat+pump&tag=errorcodefixes-20) | Coil, ambient, and suction sensors, replace on any E4, E5, E6 fault | $15–$35 |
| [Reversing Valve Solenoid Coil](https://www.amazon.com/s?i=industrial&k=heat+pump+reversing+valve+solenoid+coil+24V&tag=errorcodefixes-20) | Powers the 4-way valve; fails on E8/12-flash faults | $20–$45 |
| [EcoNet Control Board for RP20](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) | Main outdoor control board; required for F3 or persistent F1/F2 faults | $150–$350 |
| [R-410A Refrigerant (25 lb cylinder)](https://www.amazon.com/s?i=industrial&k=R-410A+refrigerant+25+lb&tag=errorcodefixes-20) | Required if system is low from a leak (E2 fault with confirmed low charge) | $75–$120 |

## When to Call a Pro

Call a licensed HVAC technician when:

- **Refrigerant is involved.** Adding or recovering R-410A requires EPA 608 certification. A technician must find and repair any leak before recharging.
- **The compressor is suspect.** Compressor winding checks and replacement require refrigerant recovery and specialized tools.
- **The inverter drive needs replacement.** Drive modules on variable-speed systems are expensive and require proper startup procedures to avoid re-damaging a new unit.
- **You're seeing a reversing valve fault and the valve body is stuck.** The four-way valve requires brazing and a system evacuation, not a DIY repair.
- **Fault codes return after power cycling.** A fault that immediately resets without clearing points to a real component failure, not a transient glitch.

For the sensor and pressure switch replacements described above, a confident DIYer with basic electrical skills can handle the job. Everything involving refrigerant or compressor diagnosis stays with a licensed tech.

## Frequently Asked Questions

**Q: My Ruud RP20 shows 3 flashes but my refrigerant pressures look normal. What's wrong?**
A: A low-pressure fault with normal static pressures points to a faulty low-pressure switch, a wiring issue between the switch and the control board, or a leak that only appears under running conditions. Connect manifold gauges and run the system to check operating pressures. If they stay in range and the fault still trips, test switch continuity and replace if needed.

**Q: The RP20 keeps going into defrost every 30 minutes. Is that normal?**
A: No. Normal defrost cycles run every 30–90 minutes and last under 10 minutes. Frequent short defrost cycles usually mean a refrigerant undercharge, a failed defrost sensor, or a defrost board fault (code E9/13 flashes). Check that the outdoor coil sensor is seated correctly against the coil, a sensor that has fallen out of its clip will give incorrect coil temperatures and trigger defrost too often.

**Q: How do I clear fault codes on the Ruud RP20?**
A: Most faults clear automatically once the underlying condition is resolved. For a manual reset, turn the thermostat to OFF, then turn off the disconnect at the outdoor unit and the breaker at the panel. Wait 30 seconds, restore power at the breaker, then reconnect the outdoor disconnect. If fault codes reappear immediately, the root cause has not been fixed.

**Q: My RP20 runs fine in cooling but blows cold air in heating mode. What is that?**
A: This is a classic stuck or failed reversing valve. The valve should shift to heating position when the O/B terminal is energized or de-energized (depending on thermostat configuration). Check whether the reversing valve solenoid coil is receiving 24V in heat mode. If voltage is present and the coil resistance is good but the unit still won't switch, the valve body is mechanically stuck and needs to be replaced by a technician.

**Q: What refrigerant does the Ruud RP20 use?**
A: The RP20 uses R-410A refrigerant. Units manufactured from 2023 onward may be equipped for R-454B as part of the EPA refrigerant transition, check the unit's data plate to confirm which refrigerant your specific unit requires before ordering or adding any refrigerant.
