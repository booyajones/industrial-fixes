---
title: "Ingersoll Rand R-Series Fault Codes: Xe Controller Guide"
description: "Ingersoll Rand R-Series fault codes for Xe-70M/90M/145M and Intellisys controllers. Alarm (A:) and trip (E:) codes with real causes and fixes."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-05-01T08:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - compressor
  - ingersoll-rand
  - industrial
---

# Ingersoll-Rand R-Series Compressor Fault Codes

Ingersoll-Rand R-Series rotary screw compressors (R7.5–R90) use the Intellisys® controller for monitoring and fault management. Faults display on the Intellisys panel as text messages. The controller logs fault history with timestamps and run hours.

## R-Series Fault Code Table

| Fault | Fault Description | Common Cause | Action |
|-------|------------------|--------------|--------|
| HIGH TEMP | High discharge temperature | Cooler dirty, low oil, high ambient | Clean cooler, check oil level |
| HIGH TEMP WARN | Temperature warning | Approaching shutdown threshold | Pre-clean cooler before shutdown |
| STAR DELTA FAULT | Starter transition fault | Contactor or timing issue | Check starter sequence |
| OVERLOAD | Motor overload trip | Motor overload or high current | Check motor amps and load |
| HIGH PRESSURE | Discharge pressure too high | Excessive demand or closed valve | Check discharge valve |
| LOW INLET PRESSURE | Inlet filter restricted | Dirty inlet filter | Replace inlet air filter |
| OIL FAULT | Low oil pressure | Low oil, failed oil pump | Check oil level and pump |
| PHASE FAULT | Phase loss or imbalance | Supply fault | Check input voltage |
| EMERGENCY STOP | E-stop activated | E-stop button pressed | Check E-stop circuit |
| SERVICE LEVEL 1 | Preventive maintenance due | Hours elapsed | Perform scheduled PM |
| SERVICE LEVEL 2 | Major PM due | Major service interval | Perform major PM |
| SENSOR FAULT | Temperature sensor failure | Failed thermistor | Replace temperature sensor |
| DRAIN FAULT | Auto-drain failure | Solenoid drain valve stuck | Check drain valve operation |

## Most Common R-Series Faults

### HIGH TEMP — High Discharge Temperature
Ingersoll-Rand R-Series maximum discharge temperature is typically 235°F (113°C) for standard models. High temp shutdowns are almost always caused by dirty oil coolers or dirty air coolers. Blow cooler fins with low-pressure air or wash with coil cleaner. Check oil level with the unit loaded and running.

### OVERLOAD — Motor Overload
Check three-phase supply voltage and balance. A 5% voltage imbalance can cause 25%+ current imbalance. Reset the overload relay after determining the cause. Check unloader operation — if the unit is starting under load, motor current is excessive on startup.

### LOW INLET PRESSURE — Inlet Filter
Ingersoll-Rand R-Series inlet filters have a differential pressure switch that triggers this alarm when restriction is excessive. Check filter element — replace at the service interval or when restriction is detected. Do not operate the compressor with a dirty filter; accelerated airend wear results.

### SERVICE LEVEL 1/2
The Intellisys controller tracks service intervals by run hours. Level 1 is typically the oil filter and separator element interval (every 2,000 hours). Level 2 is the major service interval (airend inspection, oil change, full filter replacement). Perform maintenance and reset the service timer in the Intellisys menu.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Inlet air filter | [Amazon](https://www.amazon.com/dp/B0CLBFXLYJ?ascsubtag=ecf-ingersoll-rand-r-series-faults&tag=errorcodefixes-20) \| Replace at scheduled interval |
| Oil filter element | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ingersoll-rand-r-series-faults&k=Oil+filter+element&tag=errorcodefixes-20) \| IR-specific — match model |
| Oil separator element | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ingersoll-rand-r-series-faults&k=Oil+separator+element&tag=errorcodefixes-20) \| Replace at Level 2 interval |
| Compressor oil | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ingersoll-rand-r-series-faults&k=Compressor+oil&tag=errorcodefixes-20) \| IR synthetic — model-specific |
| Auto-drain solenoid valve | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ingersoll-rand-r-series-faults&k=Auto-drain+solenoid+valve&tag=errorcodefixes-20) \| Check for stuck-open or stuck-closed |
| Temperature sensor | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-ingersoll-rand-r-series-faults&tag=errorcodefixes-20) \| Match Intellisys controller input type |
> **Pro tip:** Ingersoll-Rand Intellisys controllers on networked compressor rooms can be monitored remotely via the IR Connect app. Fault alerts can be sent to maintenance personnel by email or text, enabling faster response to high-temperature events before the compressor shuts down.

## Related Articles

- [Air Compressor Fault Codes: Complete Guide](/posts/air-compressor-fault-codes/)
- [Atlas Copco Air Compressor Fault Codes — Complete Guide](/posts/atlas-copco-compressor-fault-codes/)
- [BOGE Air Compressor Error Codes - Complete Guide](/posts/boge-compressor-error-codes/)
- [Chicago Pneumatic Compressor Fault Codes — Complete Guide](/posts/chicago-pneumatic-compressor-faults/)
- [CompAir Air Compressor Fault Codes - Complete Guide](/posts/compair-compressor-fault-codes/)

## More Ingersoll Rand R Series fault codes

Compiled from manufacturer service manuals and authorized documentation.

| Code | What it means | Likely cause | How to fix |
| --- | --- | --- | --- |
| E:0010 | Emergency Stop - 24 Vac not detected on terminal R1C. | E-stop button pressed, or a break/loose connection in the emergency-stop circuit or its 24 Vac supply. | Confirm the E-stop button is released and twisted out, then check wiring and the 24 Vac feed to terminal R1C before resetting. |
| E:0020 | Main or blower motor overload (digital input C2). | Motor overload relay tripped from high current, voltage imbalance, or mechanical load on the main or cooling-fan motor. | Check three-phase voltage and balance, measure motor amps, inspect the airend and fan for binding, then reset the overload once the cause is cleared. |
| E:0115 | Pressure sensor fault - 4-20 mA signal out of range (<3.8 mA or >20.8 mA). | Failed pressure transducer, damaged wiring, or a loose connector on the pressure sensor loop. | Inspect the sensor harness and connector, verify the 4-20 mA loop, and replace the pressure transducer if the signal stays out of range. |
| E:0119 | Excess pressure - shutdown limit exceeded. | Discharge pressure rose past the trip setpoint, typically from a stuck inlet/blowdown valve, failed pressure regulation, or closed downstream isolation. | Verify plant demand and that discharge valves are open, check inlet valve and pressure regulation, and confirm the setpoint is correct. |
| E:0125 | Temperature sensor fault - signal out of range (below -50 C or above 250 C). | Open or shorted discharge temperature sensor, or damaged sensor wiring/connector. | Check the sensor connector and wiring for damage, and replace the airend discharge temperature sensor if the reading is out of range. |
| E:0129 | Excess temperature - shutdown limit exceeded. | Airend discharge temperature passed the trip threshold, usually from a dirty cooler, low oil, high ambient, or restricted airflow. | Clean the oil and air coolers, check oil level with the unit loaded and running, verify cooling-fan operation, and improve ventilation. |
| E:0866 | Power supply 24V DC low. | Failing 24 V DC supply, overloaded control circuit, or a fault drawing down the controller power rail. | Measure the 24 V DC rail under load, check for shorted sensors/solenoids on the supply, and replace the power supply if it cannot hold voltage. |
| A:0060 | High separator element delta-P (if installed). | Oil separator element is loading up and the pressure drop across it has climbed to the alarm threshold. | Plan to replace the separator element soon; a clogged separator raises energy use and can carry oil downstream. |
| A:2118 | High pressure: alarm limit exceeded (warning, unit keeps running). | Discharge pressure reached the warning threshold below the trip limit, often from low demand or regulation drifting high. | Check the target pressure setpoint and regulation, and confirm the inlet/blowdown valve is modulating correctly before it escalates to a trip. |
| A:2128 | High temperature: alarm limit exceeded (warning, unit keeps running). | Discharge temperature reached the warning threshold, an early indicator of cooling or oil problems before shutdown. | Clean coolers, check oil level and cooler airflow now to head off an E:0129 excess-temperature shutdown. |
| A:2816 | Power failure detected (warning). | The controller logged a loss or interruption of supply power. | Confirm stable incoming power and connections; investigate the plant electrical supply if the warning recurs. |
| A:4804 | Service due - the service-interval hours counter has reached zero. | Scheduled maintenance interval has elapsed based on run hours. | Perform the due maintenance (filters, oil, separator as applicable) and reset the service timer in the controller menu. |


## How to troubleshoot Ingersoll Rand R Series

Ingersoll Rand R-Series units ship with different controllers depending on age. Older machines use the Intellisys panel with plain-text messages, while current fixed-speed R-Series (roughly R7.5 through R160) use the Xe-M family (Xe-70M, Xe-90M, Xe-145M). The Xe controllers split faults into two classes you should read differently: an alarm/warning code prefixed with **A:** keeps the compressor running so you can act before it stops, and a shutdown/trip code prefixed with **E:** stops the machine immediately. Note the exact code before you reset anything, since the controller logs history with run hours and timestamps.

Start with the highest-frequency failure mode on rotary screw compressors: heat. High-temperature warnings and trips (A:2128, A:3129, E:0129) are almost always cooling problems, not a bad sensor. Check the oil level with the unit loaded and running, then inspect the oil cooler and aftercooler cores for dirt, lint, and blocked fins, confirm the cooling fan runs, and make sure the room has enough ventilation and isn't recirculating hot air. Only after cooling and oil check out should you suspect the thermostatic valve or the temperature sensor itself (E:0125 flags an out-of-range sensor signal).

For pressure faults, separate a real over-pressure event (E:0119 trip, A:2118 warning) from a sensor problem (E:0115, a 4-20 mA signal out of range). A genuine over-pressure points to plant demand, a closed downstream valve, or inlet/blowdown valve and regulation trouble; an out-of-range signal points to the transducer or its wiring. Rising separator delta-P (A:0060) and service-due (A:4804) are maintenance prompts, not breakdowns, and ignoring them raises energy cost and risks oil carryover.

Safety and escalation: these are three-phase machines with stored air pressure and hot oil. Before opening panels or touching the airend, lock out and tag out power and fully depressurize the sump and receiver. Electrical faults (E:0010 emergency stop, E:0020 motor overload, E:0866 control power) and any repeat trip after one reset are the point to bring in an authorized Ingersoll Rand service technician rather than repeatedly clearing the code. Repeated resets on an unresolved high-temperature or overload trip can destroy the airend or motor.


## Frequently asked questions

### What is the difference between an A: code and an E: code on an Ingersoll Rand Xe controller?

An A: code is an alarm or warning; the warning symbol lights steady and the compressor keeps running so you can fix the problem before it escalates. An E: code is a shutdown or trip; the trip symbol flashes and the compressor stops. Address A: codes promptly to avoid an E: trip.

### Why does my R-Series compressor keep tripping on high discharge temperature?

On rotary screw units this is almost always cooling, not a faulty sensor. Check the oil level with the machine loaded and running, clean the oil cooler and aftercooler cores, confirm the cooling fan runs, and make sure the room isn't recirculating hot air. The thermostatic valve or temperature sensor comes later in the list. Repeatedly resetting a high-temp trip risks airend damage.

### What does a pressure sensor fault (E:0115) mean and how do I fix it?

E:0115 means the pressure transducer's 4-20 mA signal is out of range (below 3.8 mA or above 20.8 mA), which is a sensor or wiring problem rather than actual high pressure. Inspect the connector and harness on the pressure sensor loop and replace the transducer if the signal stays out of range. Genuine over-pressure shows as E:0119 instead.

### My compressor shows a service-due warning (A:4804). Do I have to stop using it?

No. A:4804 is a maintenance reminder, not a fault; it appears when the run-hour service counter reaches zero. Perform the due maintenance (air and oil filters, oil, and separator as applicable) and then reset the service timer in the controller menu. Running long past it accelerates airend wear and raises energy cost.

### The controller shows a motor overload trip (E:0020). What should I check first?

Check the incoming three-phase voltage and balance first, since even a small voltage imbalance drives a large current imbalance. Then measure motor amps, verify the unit isn't starting under load, and inspect the airend and cooling fan for binding. Only reset the overload relay after you've found and cleared the cause.

