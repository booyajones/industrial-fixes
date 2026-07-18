---
title: "Generac Generator Fault Codes: Meanings, Causes & Fixes"
description: "Generac generator fault codes for Guardian, Protector and PowerPact: alarm meanings, likely causes, and step-by-step fixes from overcrank to aux shutdown."
pubDatetime: 2026-04-22T19:00:00Z
modDatetime: 2026-04-22T19:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - generator
  - generac
  - electrical
---

## Generac Generator Error Codes — Quick Reference

Generac standby generators display alarm codes on the Evolution controller display. Alarms are classified as Warnings (generator continues to run) or Shutdowns (generator stops and requires reset). The controller also stores fault history for the last 50 events. Access fault history: Menu → View History.

| Code | Type | Meaning | Quick Fix |
|------|------|---------|-----------|
| 1100 | Warning | Low battery | Charge or replace battery |
| 1200 | Warning | Low coolant | Add coolant; check for leaks |
| 1205 | Shutdown | High coolant temperature | Check coolant; check fan |
| 1300 | Warning | Low oil pressure warning | Check oil level |
| 1302 | Shutdown | Low oil pressure shutdown | Add oil; check for leaks |
| 1400 | Warning | Overcrank warning | Check battery; check starter |
| 1401 | Shutdown | Overcrank — failed to start | Check fuel, spark, battery |
| 1500 | Shutdown | Overspeed | Governor fault; speed sensor |
| 1501 | Shutdown | Underspeed | Engine load, governor fault |
| 1600 | Shutdown | Overfrequency | Governor problem |
| 1601 | Shutdown | Underfrequency | Engine load, governor |
| 1700 | Shutdown | Overvoltage | Voltage regulator fault |
| 1701 | Shutdown | Undervoltage | AVR fault; load too high |
| 1900 | Shutdown | RPM sense loss | Magnetic pickup fault |
| 2100 | Warning | Check | General warning — see history |
| 2800 | Warning | Low fuel | Add fuel |
| 2900 | Shutdown | High AC voltage | Voltage regulator fault |

## Most Common Faults

### 1401 — Overcrank Shutdown (Failed to Start)
The most common Generac fault, especially on generators that are not exercised regularly. The engine cranked the maximum number of times without starting. 

**Most common causes and fixes:**
1. **Low battery:** Even if the battery holds a static charge, it may lack cranking amps. Test with a battery load tester. Generac uses 12V Group 26 or similar batteries — replace every 3–4 years.
2. **Stale fuel:** Gasoline degrades in 30–60 days. If the generator hasn't run on fresh fuel in months, drain the carburetor and add fresh fuel.
3. **Choke stuck:** On air-cooled generators, the automatic choke can stick. Check the choke plate on the carburetor — it should be nearly closed on a cold start.
4. **Spark plug fouled:** Remove and inspect the spark plug. A black, sooty plug indicates a rich condition; a white plug indicates lean. Gap should be 0.028–0.030 inches.

### 1302 — Low Oil Pressure Shutdown
The oil pressure sensor detected pressure below the minimum safe level. Always check the oil level first — if it's low, add the correct viscosity oil (typically SAE 5W-30 for most Generac air-cooled engines). If oil level is correct, the oil pressure sensor may have failed, or the engine may have an internal oil pressure issue (worn pump, worn bearings).

### 1205 — High Coolant Temperature (Liquid-Cooled Models)
Check the coolant level in the radiator overflow reservoir and the radiator itself. Inspect the radiator fins for debris (leaves, dirt). Verify the cooling fan is operating when the engine is running. Check the thermostat — a stuck-closed thermostat will rapidly overheat the engine.

### 1500 / 1501 — Overspeed / Underspeed
Engine speed is directly tied to output frequency (60 Hz requires ~3600 RPM for 2-pole alternators). Speed issues indicate:
- **Overspeed:** Governor spring has broken or governor linkage is stuck open
- **Underspeed:** Engine is overloaded, governor is stuck closed, or low fuel pressure
Check the governor linkage and spring on air-cooled units. On electronic governors, check the governor actuator wiring.

### 1900 — RPM Sense Loss
The magnetic pickup sensor (Hall effect sensor) that monitors flywheel speed has failed or lost its signal. This sensor is mounted close to the flywheel ring gear. Check the gap between the sensor tip and the ring gear teeth (typically 0.020–0.030 inches). Also inspect the sensor wiring for damage.

## Generac Weekly Exercise Reminder
Generac generators should run under load for 20+ minutes per week. Configure the exercise schedule on the Evolution controller: Menu → Setup → Exercise. Generators that only run the 5-minute default exercise cycle accumulate carbon deposits and are more likely to fail to start during actual outages.

## When to Call a Pro
Voltage regulator faults (1700, 1701, 2900) and governor problems require a Generac-certified service technician. Do not attempt to adjust AVR (automatic voltage regulator) trim pots without proper load bank equipment.

## More Generac Generator fault codes

Compiled from manufacturer service manuals and authorized documentation.

| Code | What it means | Likely cause | How to fix |
| --- | --- | --- | --- |
| 2400 | Fuse Problem (controller alarm) | Missing, blown, or damaged 7.5A ATO-type fuse in the Evolution controller, located under the rubber USB port flap on top of the controller. Generac's diagnostic manual states the 7.5 amp controller fuse is missing or blown (open). | Power down, locate the 7.5A ATO fuse under the USB flap, and inspect/replace it. Check for a wiring short that caused it to blow before returning to Auto. |
| 2099 | Wiring Error (customer-side) | Per Generac's diagnostic manual, the customer-connection low-voltage and high-voltage sensing wires are crossed, most commonly during installation. | Do not run the unit. Have the installer verify the field wiring against the wiring diagram, especially the high- vs low-voltage sensing leads, before restarting. |
| 2399 | Stepper Overcurrent alarm | Per Generac's diagnostic manual, current flow in the stepper (throttle) motor coil(s) is above specification. | Inspect the stepper motor and its wiring for a short or a binding/seized stepper. Replace the stepper motor if it draws excess current. Certified service recommended. |
| 1505 | RPM Sensor Loss (two-cylinder unit, during cranking) | A two-cylinder unit was cranking but the controller never received a valid RPM signal that the engine was turning. Generac lists likely causes as a starter-motor issue or a missing ignition pulse (loss of a primary coil); a weak or dead battery is a common upstream cause. | Load-test and charge or replace the starting battery first. Verify the starter engages and cranks at full speed, then inspect the ignition coils and their wiring. |
| 1515 | RPM Sensor Loss (single-cylinder unit, during cranking) | A single-cylinder unit was cranking but the controller never received a valid RPM signal. Generac lists the likely cause as a starter-motor issue; a weak or dead battery is a common upstream cause. | Start with the battery (charge/load-test/replace) and confirm strong cranking. Then verify the starter engages and cranks at full speed. |


## How to troubleshoot Generac Generator

Work a Generac fault from the safest, cheapest, most-likely cause outward. Before touching anything, put the generator in OFF at the controller and open the DC/battery disconnect. A generator in Auto can crank without warning and cause injury, and gaseous fuel work (LP/NG) means no open flame or sparks near the unit.

Start with the battery. A weak or dead 12V starting battery is the single most common root cause behind overcrank and RPM-sensor-loss faults, because a battery that holds a resting charge can still lack the cranking amps to spin the engine fast enough to start or to generate a valid speed signal. Load-test it rather than trusting a voltage reading, and replace batteries every 3 to 4 years as routine maintenance.

Then follow the fuel and air path. Confirm the fuel supply valve is fully open and, on LP, that the tank is not low, since low supply pressure during cranking will set a fault. On air-cooled units check the spark plug(s) and the automatic choke. On liquid-cooled units also check coolant level and the radiator for debris before assuming a sensor failed. Read the controller's stored fault history to see whether the unit is throwing one repeating code or a cascade, which tells you whether you are chasing a single component or a systemic issue like miswiring or a blown control fuse.

Know where the DIY line is. Battery, fuel supply, spark plugs, a clogged radiator, and a blown control fuse are owner-serviceable. Voltage-regulator and AVR faults, stepper/throttle-actuator faults, ignition-module faults, and any fault that persists after the basics are checked call for a Generac-certified technician, especially anything requiring a load bank or internal engine work. Never adjust voltage-regulator trim pots without proper load-bank equipment, and never bypass a shutdown alarm to force the unit to run.


## Frequently asked questions

### Why won't my Generac start and show an overcrank code?

The engine cranked but never fired. The most common cause is a weak or dead starting battery that lacks cranking amps, followed by a closed or low fuel supply, a stuck choke, or a fouled spark plug. Load-test the battery first, confirm the fuel valve is open, then check the plug and choke before suspecting anything electronic.

### How do I clear or reset a fault code on a Generac generator?

Fix the underlying condition first, then press OFF on the controller (hold it about 3 seconds to clear the alarm), then return the unit to AUTO. If the same code returns immediately, the fault is still present. Clearing a shutdown alarm without addressing the cause just lets the unit fail again.

### What does error code 2800 mean?

On Generac Evolution units, code 2800 is an Auxiliary/Emergency-Stop shutdown, meaning the controller sees an auxiliary or E-stop shutdown switch in the OFF (open) position. Confirm the E-stop is not pressed and that all shutdown switches (units 15kW and up have a second switch inside the housing) are ON, then hold OFF to clear and return to AUTO.

### How often should a Generac generator exercise itself?

Run it under its self-test exercise cycle weekly. Generators that only idle briefly, or that sit for long stretches, build carbon deposits and are more likely to overcrank and fail to start during an actual outage. Set the schedule on the Evolution controller.

### When should I call a pro instead of fixing it myself?

Battery, fuel supply, spark plugs, radiator cleaning, and a blown control fuse are DIY. Call a Generac-certified technician for voltage-regulator/AVR faults, stepper or actuator faults, ignition-module faults, or any code that returns after the basics check out, since those often need a load bank or internal engine service.


## Related guides

- [Cummins Onan Fault Codes](/posts/cummins-onan-fault-codes/)

