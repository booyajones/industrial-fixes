---
title: "ECM Blower Motor Error Codes Guide — Genteq / Regal Beloit"
description: "ECM blower motor error codes and fault diagnostics for Genteq, Regal Beloit, and OEM ECM motors: flash codes, LED blink sequences, and troubleshooting steps."
pubDatetime: 2026-04-22T19:00:00Z
modDatetime: 2026-04-22T19:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - ecm-motor
  - blower
---

## ECM Blower Motor Error Codes — Quick Reference

ECM (Electronically Commutated Motor) blower motors are used in most modern variable-speed furnaces and air handlers. Manufacturers include Genteq (formerly GE Motors), Regal Beloit, and Nidec. ECM motors communicate fault information via LED flash codes on the motor's control module. To read the codes: locate the motor module (mounted on the motor body), count the LED blinks in a repeating pattern.

| [Flash Code](https://www.amazon.com/s?i=industrial&k=Flash+Code&tag=errorcodefixes-20) | Meaning | Quick Fix |
|------------|---------|-----------|
| [1 flash](https://www.amazon.com/s?i=industrial&k=1+flash&tag=errorcodefixes-20) | Normal operation / standby | No fault — motor waiting for call |
| [2 flashes](https://www.amazon.com/s?i=industrial&k=2+flashes&tag=errorcodefixes-20) | Low airflow / high static pressure | Check filter; open registers; clean coils |
| [3 flashes](https://www.amazon.com/s?i=industrial&k=3+flashes&tag=errorcodefixes-20) | Control input out of range | Verify control board output signal (0–10V or PWM) |
| [4 flashes](https://www.amazon.com/s?i=industrial&k=4+flashes&tag=errorcodefixes-20) | Internal module fault | Replace ECM module |
| [5 flashes](https://www.amazon.com/s?i=industrial&k=5+flashes&tag=errorcodefixes-20) | Over-temperature — motor or module | Check for blocked airflow; allow cool-down |
| [6 flashes](https://www.amazon.com/s?i=industrial&k=6+flashes&tag=errorcodefixes-20) | DC bus voltage fault | Check input voltage; verify 120/240VAC supply |
| [7 flashes](https://www.amazon.com/s?i=industrial&k=7+flashes&tag=errorcodefixes-20) | Internal module memory fault | Replace ECM module |
| [Rapid flash](https://www.amazon.com/s?i=industrial&k=Rapid+flash&tag=errorcodefixes-20) | Active fault — see blink count | Count individual blinks carefully |
| [No flash](https://www.amazon.com/s?i=industrial&k=No+flash&tag=errorcodefixes-20) | No power to module | Check power supply; check fuse/breaker |
| [Continuous on](https://www.amazon.com/s?i=industrial&k=Continuous+on&tag=errorcodefixes-20) | Module locked in fault | Cycle power to reset |

## Most Common Faults

### 2 Flashes — Low Airflow / High Static Pressure
This is the single most common ECM fault code. The motor senses it is working harder than expected to move air through the system — a condition caused by a clogged filter, dirty evaporator coil, closed zone dampers, or partially closed registers. ECM motors are designed to maintain a target airflow regardless of static pressure, but they have limits. Replace or clean the air filter first. If the code persists, check that all supply and return registers are fully open.

### 3 Flashes — Control Input Out of Range
The ECM motor receives its speed command either as a 0–10VDC analog signal or as a PWM (pulse-width modulation) signal from the furnace control board. A 3-flash fault means the signal is outside the expected range. Check the control board output voltage — on 0–10V systems, the signal should scale from approximately 2V (low speed) to 10V (high speed). A failed control board, loose connector, or damaged control wire will cause this fault.

### 4 Flashes — Internal Module Fault
The ECM module (the electronics mounted on the motor body) has detected an internal fault. This can sometimes be caused by a power surge or lightning strike. Try power-cycling the system by turning off the furnace disconnect for 5 minutes. If the 4-flash code returns on power-up, the module requires replacement. On most ECM motors, the module (sometimes called the ECM controller or ECM driver board) can be replaced separately from the motor body, which significantly reduces repair cost.

### 5 Flashes — Over-Temperature
The motor or module overheated. This can occur during extreme high-static conditions (when the motor is fighting very restricted airflow), in very high ambient temperatures, or when the motor is in a location with poor ventilation. Check airflow restrictions first. If the motor is physically very hot and the airflow path appears clear, the motor's internal thermal protection may be weakening — schedule replacement before complete failure.

### 6 Flashes — DC Bus Voltage Fault
The motor's internal power supply is operating outside its DC voltage range. Check the incoming line voltage with a multimeter — it should be within ±10% of the motor's rated voltage (typically 115VAC or 230VAC). Voltage fluctuations, a failing blower capacitor on a PSC-type motor replacement, or a failing transformer can cause this fault. On 230VAC systems, verify both legs of the supply are present.

## ECM Module Replacement Notes

- The ECM module (control board) is separate from the motor body on most Genteq/Regal Beloit motors
- Module part numbers are printed on the module label — always replace with the exact same part number
- When replacing a module, ensure the new module is programmed for the correct motor HP and speed table
- Some modules are pre-programmed; others require programming with a Regal Beloit ECM programming tool

## Genteq ECM Module vs. Motor Identification

| [Motor Family](https://www.amazon.com/s?i=industrial&k=Motor+Family&tag=errorcodefixes-20) | Module Style | Common HP |
|-------------|-------------|-----------|
| [ECM 2.3](https://www.amazon.com/s?i=industrial&k=ECM+2.3&tag=errorcodefixes-20) | Separate slide-on module | 1/2–1 HP |
| [ECM X13](https://www.amazon.com/s?i=industrial&k=ECM+X13&tag=errorcodefixes-20) | Integrated module | 1/3–3/4 HP |
| [ECM 3.0](https://www.amazon.com/s?i=industrial&k=ECM+3.0&tag=errorcodefixes-20) | Separate bolt-on module | 1/2–1-1/2 HP |

## When to Call a Pro
A 4-flash or 7-flash internal module fault requires motor module replacement — a task most experienced HVAC technicians can handle. If the motor body itself has failed (burned windings, failed bearings), a full motor replacement is needed.
