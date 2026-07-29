---
title: "BOGE Compressor Fault Codes: FOCUS Controller List & Fixes"
description: "Numeric BOGE FOCUS controller fault codes 1-38 explained: final compression temp, oil separator DP, transmitter faults, plus likely causes and repair steps."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - compressor
  - boge
  - industrial
money_part: "Oil separator element"
---

## BOGE Compressor Error Codes - Quick Reference

BOGE rotary screw compressors (S, C, and BLUEKAT series) use the BOGE Control and BOGE Select electronic controllers. Alarms display as text or numeric codes depending on controller generation.

| Code / Alarm | Meaning | Quick Fix |
|-------------|---------|-----------|
| High Final Pressure Temp | Discharge temp too high | Clean cooler, check oil |
| Low Oil Pressure | Lube circuit fault | Check oil level and filter |
| Motor Overload (OL) | Motor overcurrent | Check amps and phase balance |
| E-Stop | Emergency stop active | Reset and inspect |
| Service Interval | PM due | Perform service, reset counter |
| Air Filter Diff. High | Air filter blocked | Replace air filter element |
| Oil Separator DP | Oil separator restricted | Replace separator element |
| Pressure Regulator Fault | Regulator not maintaining set point | Check regulator and solenoid |
| Phase Monitoring | Phase loss or reversal | Check supply wiring |
| Temperature Sensor | Sensor out of range | Check sensor wiring |

## Most Common Faults

### High Final Pressure Temperature
BOGE screw compressors are sensitive to oil cooler cleanliness. The cooler fins on BOGE units pack densely and require cleaning from the inside out with compressed air or a fin brush. Verify the cooling fan capacitor - a slow fan is a common cause that's easy to overlook.

### Air Filter Differential High
Some BOGE models have a differential pressure switch across the air filter. A clogged filter reduces airflow, increases velocity through the airend, and causes temperature rise. Replace the filter element before it triggers this shutdown.

### Oil Separator DP
The separator element is a scheduled service part - typically 3,000–4,000 hours. In dusty environments or with degraded oil, it can plug much sooner. A high differential pressure across the separator increases power consumption noticeably before triggering the alarm.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Oil separator element | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-boge-compressor-error-codes&k=Oil+separator+element&tag=errorcodefixes-20) \| Primary PM item |
| Air filter element | [Search on Amazon](https://www.amazon.com/s?ascsubtag=ecf-boge-compressor-error-codes&k=BOGE+Air+filter+element&tag=errorcodefixes-20) \| Replace per service schedule |
| Oil filter | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-boge-compressor-error-codes&k=Oil+filter&tag=errorcodefixes-20) \| Replace with separator |
| Cooling fan capacitor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-boge-compressor-error-codes&k=Cooling+fan+capacitor&tag=errorcodefixes-20) \| Common on single-phase fan motors |
| Discharge temperature sensor | [Search on Amazon](https://www.amazon.com/s?ascsubtag=ecf-boge-compressor-error-codes&k=BOGE+Discharge+temperature+sensor&tag=errorcodefixes-20) \| Thermocouple or NTC type |
## When to Call a Pro
BOGE compressors require factory-specific oil types and torque specs on separator housing reassembly. If repeated temperature shutdowns occur after service, contact a BOGE authorized service provider.

## More Boge Compressor fault codes

Compiled from manufacturer service manuals and authorized documentation.

| Code | What it means | Likely cause | How to fix |
| --- | --- | --- | --- |
| 2 | Motor temperature too high | Motor overload, poor cooling airflow around the motor, high ambient temperature, or a failing PTC/thermistor circuit in the motor windings. | Let the motor cool, check running amps against nameplate, clean motor cooling passages, and verify the PTC sensor and wiring. Investigate load and phase balance before restarting. |
| 5 | Compressor system pressure too high | Internal (sump/separator) pressure exceeded the limit, often from a stuck minimum-pressure/check valve, a plugged separator, or an inlet-valve control fault. | Check the minimum pressure valve, separator differential, and inlet valve operation. Verify the internal pressure transmitter reads correctly. |
| 6 | Suction filter differential pressure too high | Clogged intake/suction air filter element reducing airflow into the airend. | Replace the suction air filter element and reset. In dusty environments shorten the replacement interval. |
| 7 | Oil filter differential pressure too high | Restricted oil filter, cold thick oil at startup, or degraded oil loading the filter. | Replace the oil filter element and change oil if past its interval. If it recurs only on cold starts, confirm correct oil grade for the ambient. |
| 8 | Oil separator differential pressure too high | Plugged oil separator element, common near end of service life or accelerated by degraded oil or dusty intake air. | Replace the oil separator element and reset the service counter. Change oil and oil filter at the same time. |
| 13 | Frequency converter signals fault (no release) | The VFD (on variable-speed models) has faulted or is not sending its ready/release signal to the FOCUS controller. | Read the fault on the drive display, clear it, and check the release wiring between the drive and controller. Address the underlying drive fault before restart. |
| 16 | Net pressure transmitter faulty | The system/network pressure transmitter is out of range or reading implausibly, often a failed sensor or wiring/connector issue. | Check the transmitter wiring and connector, compare its reading to a known gauge, and replace the transmitter if it is out of tolerance. |
| 22 | Inner hood temperature too high | Elevated temperature inside the enclosure from restricted ventilation, dirty coolers, a failing hood/ventilation fan, or high ambient temperature. | Clean coolers and enclosure air paths, verify the ventilation fan runs, and improve room ventilation. Let the unit cool before restart. |
| 23 | Cylinder head temperature too high | On piston/reciprocating models, overheating of the cylinder head from poor cooling, low oil, or overload. | Check cooling airflow to the head, verify oil level, and allow the unit to cool. Investigate load and valve condition if it recurs. |
| 24 | Oil level too low | Low oil charge from consumption, a leak, or high carry-over, detected by the oil level sensor. | Top up with the correct BOGE-specified oil, inspect for leaks, and check for excessive oil carry-over (separator condition) if the loss is repeated. |
| 32 | Net pressure transmitter wire breakage | Open circuit in the network pressure transmitter signal wiring, a loose connector, or a failed sensor. | Inspect and reseat the transmitter connector, check for broken or chafed signal wires, and replace the transmitter if the wiring is intact. |
| 38 | Excessive current compressor motor | Motor drawing over-current from mechanical binding in the airend, over-pressure operation, low voltage, or phase imbalance. | Measure running amps and supply voltage on all three phases, check for airend drag or over-pressure, and confirm the overload setting matches the nameplate. |

## How to troubleshoot Boge Compressor

Start every BOGE fault the same way: read the exact code or message on the FOCUS (or Base/RATIO) controller, note whether it is a warning or a shutdown, and let the machine cool and fully depressurize before opening any panel. Most BOGE shutdowns fall into three families, and the family tells you where to look first.

Temperature faults (final compression temperature, motor temperature, inner hood temperature) are the most common and almost always trace to heat rejection, not the sensor. Check oil level and oil condition first, then clean the oil cooler and aftercooler fins from the inside out, then confirm the cooling and enclosure fans actually spin at full speed. A weak or failed single-phase fan capacitor is an easy-to-miss cause that produces repeat overheating shutdowns.

Differential-pressure faults (suction filter, oil filter, oil separator) are maintenance items. They mean a consumable is plugged, so replace the named element rather than resetting and running on. The oil separator, oil filter, and oil should generally be changed together, and the separator plugs early in dusty air or when the oil is degraded.

Electrical and sensor faults (wrong rotational direction, excessive motor current, transmitter faulty or wire breakage, frequency converter fault) call for a meter. Verify supply voltage and phase balance on all three phases, check overload settings against the motor nameplate, and inspect transmitter connectors and wiring before condemning a sensor. Wrong rotation after any electrical work is fixed by swapping two supply phases.

Call a BOGE-authorized service provider when temperature shutdowns persist after cleaning and an oil/filter service, when the airend shows drag or unusual noise, when a VFD throws its own fault, or any time separator-housing reassembly and factory oil and torque specs are involved. Do not defeat a shutdown to keep a unit in production, since final-compression-temperature and over-current trips protect the airend and motor from expensive damage.

## Frequently asked questions

### What does BOGE FOCUS error code 1 mean?

Code 1 is final compression temperature too high (above roughly 110°C). It is a protective shutdown. The usual causes are a dirty oil cooler, low or degraded oil, a weak cooling fan, or high ambient temperature. Check oil and clean the cooler before restarting, and never bypass this trip since it protects the airend.

### My BOGE keeps flagging oil separator differential pressure. What do I do?

That fault (code 8 on FOCUS) means the oil separator element is plugged. Resetting without changing it just wastes energy, since a restricted separator raises power draw well before it trips. Replace the separator element and change the oil and oil filter at the same time, then reset the service counter.

### The compressor tripped on wrong rotational direction after electrical work. How is it fixed?

Code 4, wrong rotational direction, means the three-phase supply is wired out of phase, usually right after an install or panel change. Swap any two of the three incoming supply phases, reverify rotation, and confirm before running. Running a screw airend backwards can damage it, so do not defeat the check.

### What is the difference between a warning and a shutdown on a BOGE controller?

Service-due and some differential-pressure messages are warnings that let the unit keep running so you can plan maintenance, while temperature, over-current, rotation, and low-oil faults are shutdowns that stop the machine to prevent damage. Address warnings promptly, because an ignored warning like a plugging filter often becomes a temperature shutdown.

### Do BOGE compressors need a specific oil for repairs?

Yes. BOGE specifies particular oil types, and separator housing reassembly has factory torque specs. Using the wrong oil accelerates separator plugging, oil-filter DP faults, and carry-over. For anything beyond routine top-up and element changes, use BOGE-specified oil or contact an authorized service provider.
