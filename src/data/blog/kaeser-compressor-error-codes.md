---
title: "Kaeser Compressor Fault & Error Codes: Causes and Fixes"
description: "Kaeser compressor fault and error codes for Sigma Control and Sigma Control Mobil: what each alarm means, the likely cause, and how to fix or reset it."
pubDatetime: 2026-04-22T19:00:00Z
modDatetime: 2026-04-22T19:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - compressor
  - kaeser
  - industrial
money_part: "Temperature or pressure sensor"
---

## Kaeser Compressor Error Codes — Quick Reference

Kaeser screw compressors with Sigma Control controllers report warnings and shutdowns for temperature, pressure, service intervals, and sensor faults. The Sigma Control panel may show text alarms rather than short numeric codes, depending on controller generation.

| Alarm | Meaning | Quick Fix |
|-------|---------|-----------|
| Final Compression Temp High | Compressor too hot | Clean coolers; check oil |
| Motor Protection Trip | Main motor overload | Check load and contactor |
| Sensor Fault | Bad temp/pressure sensor | Inspect and replace sensor |
| Dryer Fault | Integrated dryer issue | Check condenser and dryer circuit |
| Service Due | Scheduled maintenance due | Perform PM and reset counter |
| Emergency Stop | E-stop active | Reset and inspect loop |
| Pressure Switch Fault | Control pressure issue | Check transducer and loading controls |
| Phase Fault | Supply power issue | Check voltage balance |

## Most Common Faults

### Final Compression Temperature High
Kaeser packages are efficient, but they still depend on clean cooling surfaces and correct oil flow. Blow out coolers, verify cabinet fans run properly, and confirm the oil level is correct with the unit in the proper state per Kaeser instructions.

### Sensor Fault
Before replacing expensive valves or motors, compare the controller reading to an independent gauge or temperature probe. Kaeser sensor failures are common enough that a bad sensor should always be on the suspect list.

### Dryer Fault
If the package has an integrated refrigerated dryer, the dryer can trip independently of the compressor. Check condenser cleanliness, ambient temperature, and whether the dryer fan is running.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Temperature or pressure sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-kaeser-compressor-error-codes&k=Temperature+or+pressure+sensor&tag=errorcodefixes-20) \| Common controller alarm source |
| Service kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-kaeser-compressor-error-codes&k=Service+kit&tag=errorcodefixes-20) \| Oil, separator, filters |
| Cabinet fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-kaeser-compressor-error-codes&k=Cabinet+fan&tag=errorcodefixes-20) \| Overheat alarms often trace here |
| Dryer condenser fan / contactor | [Search on Amazon](https://www.amazon.com/s?ascsubtag=ecf-kaeser-compressor-error-codes&k=Kaeser+Dryer+condenser+fan+%2F+contactor&tag=errorcodefixes-20) \| On integrated dryer faults |
## When to Call a Pro
Kaeser Sigma Control diagnostics are much easier with factory documentation and service access. If alarms persist after PM work, involve a Kaeser-trained compressor tech before the airend is damaged.

## More Kaeser Compressor fault codes

Compiled from manufacturer service manuals and authorized documentation.

| Code | What it means | Likely cause | How to fix |
| --- | --- | --- | --- |
| 1200 | Compressor unit overheating - shutdown alarm (Sigma Control Mobil / MOBILAIR portable compressors) | Airend discharge temperature exceeded the safe limit, usually from a dirty/blocked cooler, low or degraded cooling oil, high ambient temperature, or a failed cooling fan. | Let the unit cool, clean the cooler core, check cooling-oil level and condition, confirm the fan runs, and verify airflow around the enclosure before restarting. |
| 1201 | Compressor final pressure too high - shutdown alarm (Sigma Control Mobil / MOBILAIR). OEM manual label: compressor pressure too high. | System pressure rose above the shutdown threshold, often from a stuck regulation/inlet valve, a faulty pressure sensor, or a blocked minimum-pressure/relief valve. | Check the pressure regulation and inlet valve, compare the sensor reading to a known-good gauge, and inspect the pressure-relief and minimum-pressure valves. |
| 1304 | Controller power supply fault (Sigma Control Mobil / MOBILAIR). OEM manual label: power supply. | Supply voltage to the controller is out of range - low battery, bad charging voltage, loose power connection, or a blown fuse. | Check battery and charging voltage, tighten and inspect power connections, and verify controller supply fuses. |
| 1400 | Quick stop / emergency stop active (Sigma Control Mobil / MOBILAIR) | The emergency-stop (mushroom) button is pressed or the safety circuit is open. | Confirm the area is safe, release the E-stop, and inspect the safety loop and any remote stop contacts before resetting. |
| 1410 / 1411 | Open circuit (1410) or short circuit (1411) in the oil separator tank pressure sensor (Sigma Control Mobil / MOBILAIR) | The separator-tank pressure sensor or its wiring has failed open or shorted. | Check the sensor wiring and connector, verify the reading against a mechanical gauge, and replace the pressure sensor if faulty. |
| 1414 / 1415 | Open circuit (1414) or short circuit (1415) in the compressor unit temperature sensor (Sigma Control Mobil / MOBILAIR) | The airend/discharge temperature sensor, its connector, or wiring has failed open or shorted. | Inspect the sensor connector and harness for damage or corrosion, measure the sensor resistance against spec, and replace the sensor if out of range. |
| 2200 / 2201 | Maintenance due: replace compressor cooling oil and filter at 1000h (2200); clean or change compressor air filter at 250h (2201) (Sigma Control Mobil / MOBILAIR) | A scheduled service interval has been reached; not a fault. | Perform the indicated service (oil and filter, or air filter) and reset the maintenance counter rather than just clearing the message. |
| 3100 | Engine oil pressure too low - warning on diesel-driven units (Sigma Control Mobil / MOBILAIR) | Low engine oil level or low oil pressure on the drive engine of a portable compressor. | Stop and check engine oil level and condition; if pressure is genuinely low, do not run the engine until the cause is found. |
| 3130 | Fuel level low - warning on diesel-driven units (Sigma Control Mobil / MOBILAIR) | Fuel in the tank has dropped below the low-level threshold. | Refuel; if the tank is not actually low, check the fuel level sensor and wiring. |
| 3200 | Compressor overheating - warning, pre-shutdown (Sigma Control Mobil / MOBILAIR) | Airend temperature is climbing toward the shutdown limit; typically early-stage cooler fouling, low oil, or reduced airflow. | Address it before it escalates: clean the cooler, check oil level and quality, and confirm fan operation and ambient airflow. |

## How to troubleshoot Kaeser Compressor

Kaeser controllers come in a few generations, and the diagnostic path depends on which one you have. Stationary rotary screw packages (SM, SK, ASD, BSD, DSD and similar) with Sigma Control or Sigma Control 2 mostly show plain-text alarms and warnings on the panel rather than short numeric codes. Portable MOBILAIR units with Sigma Control Mobil use four-digit numeric codes, where the first digit is the type (1 = alarm/shutdown, 2 = maintenance, 3 = warning) and the second digit is the location (1 = engine, 2 = compressor unit, 3 = controller, 4 = general). Read the code with that structure in mind before you start pulling parts.

Start by separating a warning from a shutdown. A warning means the machine is still running but a value is drifting; a shutdown alarm means the controller has already stopped the unit to protect it. Note the exact alarm text or code and the reading that tripped it, because Kaeser stores an alarm and operating history you can scroll back through.

Check the cheap, common causes first. The single most frequent Kaeser alarm family is high airend discharge temperature. Before replacing valves, motors, or the airend, clean the cooler core, verify the cooling-oil level and condition, confirm the cooling fan actually runs, and make sure the enclosure has adequate airflow and the room is not too hot. Sensor faults are the next most common category: a bad temperature or pressure sensor throws an alarm even when the machine is mechanically fine, so compare the controller's reading against an independent gauge or probe before condemning hardware. For overload, phase, or emergency-stop alarms, work the electrical side (voltage balance, overload relay setting, E-stop loop, door switches).

Safety and when to call a pro: always let the unit cool and relieve system pressure before opening any component, and lock out power before touching electrical parts. If a temperature or pressure alarm keeps returning after you have cleaned the coolers, corrected the oil, and confirmed the sensor, stop running the machine and bring in a Kaeser-trained technician. Continuing to run through a genuine high-temperature or low-oil-pressure alarm risks destroying the airend, which is by far the most expensive repair on the machine.

## Frequently asked questions

### Does my Kaeser compressor show numeric error codes or text alarms?

It depends on the controller. Stationary rotary screw units with Sigma Control or Sigma Control 2 usually display plain-text alarms and warnings on the panel. Portable MOBILAIR units with Sigma Control Mobil show four-digit numeric codes, where the first digit is the type (1 = alarm, 2 = maintenance, 3 = warning) and the second is the location (1 = engine, 2 = compressor, 3 = controller, 4 = general).

### What is the most common Kaeser alarm?

High airend discharge temperature. It is almost always caused by a dirty or blocked cooler, low or degraded cooling oil, a failed cooling fan, or high ambient temperature. Clean the cooler, check the oil, and confirm the fan runs before suspecting anything expensive.

### My Kaeser keeps throwing a sensor fault. Do I replace the sensor right away?

Not immediately. First compare the controller's reading against an independent gauge or temperature probe, and inspect the sensor connector and wiring for damage or corrosion. Kaeser temperature and pressure sensors do fail, but a loose or damaged connector produces the same open-circuit or short-circuit alarm and is free to fix.

### Can I just clear a Kaeser service or maintenance message?

You can, but you should not. Maintenance messages like the oil/filter or air-filter reminders mean a service interval has been reached. Perform the actual service, then reset the maintenance counter. Clearing the message without doing the work leaves the machine running past its service life.

### When should I stop running the compressor and call a technician?

If a high-temperature or low-oil-pressure alarm keeps returning after you have cleaned the coolers, corrected the oil, and verified the sensor, stop. Running through a genuine temperature or oil-pressure alarm risks damaging the airend, which is the costliest repair on the unit. A Kaeser-trained tech has the factory diagnostics and service access to isolate the root cause.
