---
title: "Sabroe Compressor Fault Codes — Complete Troubleshooting Guide"
description: "Sabroe industrial refrigeration compressor fault codes for SAB series screw and reciprocating compressors. What each alarm means and how to fix it."
pubDatetime: 2026-04-27T23:00:00Z
modDatetime: 2026-04-27T23:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - compressor
  - refrigeration
  - sabroe
---

Sabroe industrial refrigeration compressors use controller-based shutdown IDs, not generic motor fault lights. On SAB screw compressors and HPC reciprocating packages, the controller watches suction pressure, discharge pressure, discharge temperature, oil differential pressure, oil temperature, filter differential pressure, motor protection, and communication signals. When any monitored point crosses its shutdown threshold, the controller stops the compressor and logs an alarm or shutdown ID.

This guide covers the Sabroe SAB 128, SAB 163, SAB 202 screw compressor family, HPC reciprocating packages, and the controller environment you will see on UniSAB III or SABview-style HMIs.

## How Sabroe Alarm IDs Work

Sabroe controllers separate **alarms** from **shutdowns**:

- **Alarm**: the compressor keeps running, but the controller warns you that an operating limit is close or already exceeded.
- **Shutdown**: the controller stops the compressor immediately or after the programmed delay.

On UniSAB III screw compressor packages, the most important shutdown and alarm IDs are:

| ID | Alarm / Shutdown Text |
|---|---|
| 31 | Low suction pressure alarm + shutdown |
| 32 | High suction pressure alarm |
| 35 | Low discharge pressure shutdown |
| 36 | High discharge pressure alarm + shutdown |
| 37 | High discharge temperature alarm + shutdown |
| 38 | Low oil pressure (differential pressure) alarm + shutdown |
| 41 | Low oil temperature alarm + shutdown |
| 42 | High oil temperature alarm + shutdown |
| 43 | High oil filter differential pressure alarm + shutdown |
| 44 | Oil system error shutdown |
| 46 | Compressor motor overload shutdown |
| 47 | Compressor motor error / emergency stop / HP shutdown |
| 49 | High motor temperature shutdown |
| 57 | High differential pressure (Pc minus Pe) alarm + shutdown, HPC only |
| 69 | Low discharge gas superheat alarm + shutdown |
| 84 | Low lubricating pressure alarm + shutdown |
| 86 | High internal suction pressure alarm + shutdown |
| 87 | High pressure ratio alarm + shutdown |
| 91 | High separator flow alarm |
| 92 | Low main oil pressure alarm |
| 93 | Oil system error alarm or no evaporator flow shutdown |
| 94 | No condenser flow shutdown |
| 95 | High process in temperature alarm + shutdown |
| 96 | Low process in temperature alarm + shutdown |
| 97 | Emergency stop shutdown |
| 104 | Low-low oil pressure shutdown |
| 105 | Oil pump low pressure alarm + shutdown |

For HPC reciprocating compressors, the core IDs stay similar, but you also see high oil pressure, intermediate pressure, and high liquid level alarms.

## How to View Alarm History on Sabroe Controllers

### UniSAB III
1. Press **F1 / Menu** from the default screen.
2. Open **Alarm** to view active alarms.
3. Open **Shutdown** to view active shutdowns.
4. Open **History → Shutdown** to review stored shutdown events.
5. Use **Measured Values**, **Input State**, and **Output State** under History to see what the controller saw when the trip happened.

### SABview / Sabroe HMI workflow
Most SABview HMIs follow the same logic even if the graphics differ:
1. Open the alarm banner.
2. Enter **Active Alarms**.
3. Open **Alarm History** or **Shutdown History**.
4. Record suction pressure, discharge pressure, oil differential pressure, oil temperature, discharge temperature, and motor current before resetting.

### Reset procedure
On UniSAB III, press **F4 / RESET**. The controller will only clear a shutdown if the trip condition has disappeared. If the root cause is still present, the controller keeps the shutdown active and flashes red again.

---

## ID 36, High Discharge Pressure Alarm + Shutdown

**Meaning:** The condensing side pressure rose above the alarm limit and then crossed the shutdown limit. On standard screw packages, the factory high discharge pressure setting is often 15 bar alarm and 16 bar shutdown for lower-pressure setups. On HPC high-pressure machines, the factory values run much higher, commonly 33 bar alarm and 35 bar shutdown.

**Most common causes:**
1. Condenser fans not running or rotating the wrong way
2. Evaporative condenser water problem, scaling, or spray failure
3. Liquid line or discharge line valve partly closed
4. Non-condensables in the refrigeration circuit
5. Condenser fouled with dirt, oil film, or scale
6. Ambient temperature higher than the design condition

**Diagnosis steps:**
1. Read the live discharge pressure on the controller before reset.
2. Check condenser fan contactors, overloads, and VFD status.
3. Verify condenser water flow or evaporative spray operation.
4. Compare actual condensing pressure to site ambient conditions.
5. Check whether the discharge pressure climbed slowly, which points to condenser performance, or jumped fast, which points to a closed valve or trapped non-condensables.

**Fix:**
Restore condenser capacity first. Clean condenser surfaces, restore fan or pump operation, open closed valves, and purge non-condensables if the plant procedure allows it.

---

## ID 31, Low Suction Pressure Alarm + Shutdown

**Meaning:** Suction pressure dropped below the low alarm limit and then below the shutdown limit while the compressor was running.

**Most common causes:**
1. Starved evaporator or low refrigerant feed
2. Solenoid valve closed upstream of the evaporator
3. Expansion valve misadjusted or plugged
4. Evaporator iced up, fan failure, or poor airflow
5. Suction filter or strainer restriction
6. Compressor loading too hard for the available load

**Diagnosis steps:**
1. Compare suction pressure to evaporator temperature and superheat.
2. Look at evaporator fans, liquid feed, and frost pattern.
3. Check whether the controller had the compressor loaded high when the trip happened.
4. Review alarm history for low superheat or low process temperature events near the same timestamp.

**Fix:**
Restore evaporator load or liquid feed. If the compressor unloaded too slowly, reduce capacity manually after restart and watch suction stabilize.

---

## ID 37, High Discharge Temperature Alarm + Shutdown

**Meaning:** The discharge gas temperature crossed the high alarm and then high shutdown limit. On many SAB screw compressors, factory shutdown starts around 100°C. On HPC and other reciprocating high-pressure packages, the shutdown limit can run around 125°C and higher depending on design.

**Most common causes:**
1. Low suction pressure or starved evaporator
2. Wrong volume ratio setting or Vi slide setting on screw compressors
3. Oil cooling failure
4. Too little refrigerant injection on machines equipped for injection cooling
5. Dirty oil cooler or poor cooling water flow
6. Compression ratio too high for the operating condition

**Diagnosis steps:**
1. Check suction pressure first. Low suction often drives high discharge temperature.
2. Check oil temperature and oil cooler performance.
3. On screw compressors with Vi control, verify the Vi position and whether the controller is regulating or stuck.
4. Review discharge superheat if the machine calculates it.

**Fix:**
Correct the load condition before chasing sensors. Restore suction pressure, fix oil cooling, and verify Vi control.

---

## ID 38, Low Oil Pressure Alarm + Shutdown

**Meaning:** The controller calculated low oil differential pressure. On Sabroe packages, the controller usually calculates oil differential as oil pressure after the filter minus suction pressure, with model-specific exceptions.

**Factory references from UniSAB III:**
- Many SAB 120 to 151 and SAB 193 to 355 screw compressors use about **1.5 bar low alarm** and **1.0 bar low shutdown**.
- HPC reciprocating units commonly use **4.0 bar low alarm**, **3.5 bar low shutdown**, and **0.5 bar low-low shutdown**.

**Most common causes:**
1. Low oil level in the separator or oil receiver
2. Oil pump not starting or losing pressure
3. Oil too hot and too thin
4. Oil filter heavily restricted
5. Pressure transmitter drift or failed wiring
6. Refrigerant dilution in the oil

**Diagnosis steps:**
1. Check the oil level in the separator sight glass while the machine runs.
2. Compare live oil pressure and suction pressure values on the controller.
3. Confirm oil pump operation on packages that use a pump.
4. Check whether ID 43 or ID 105 also appeared. Those often point to the real cause.
5. Inspect oil for foaming, which often shows refrigerant dilution.

**Fix:**
Do not keep resetting a low oil pressure trip. Verify oil level, oil pump operation, oil filter condition, and oil temperature before restart.

---

## ID 41, Low Oil Temperature Alarm + Shutdown

**Meaning:** Oil temperature fell below the safe minimum. Sabroe manuals call out **40°C** as a common low shutdown threshold for many screw packages and **40°C** as the minimum oil temperature before startup on SAB 202 units.

**Most common causes:**
1. Oil heater failed during standstill
2. Heater contactor or fuse failed
3. Unit power turned off during shutdown, so the heater never kept the oil warm
4. Temperature sensor drift

**Diagnosis steps:**
1. Check actual oil temperature on the controller.
2. Verify heater current draw or heater contactor status.
3. Confirm the unit stayed energized during standstill. Sabroe specifically warns operators not to remove power because the oil heater must stay active.

**Fix:**
Let the oil reach operating temperature before restart. Repair the heater circuit if the temperature never rises.

---

## ID 42, High Oil Temperature Alarm + Shutdown

**Meaning:** Oil temperature climbed above the permitted limit. Sabroe commonly sets the high alarm near 60 to 75°C and shutdown near 65 to 80°C on screw compressors, depending on the model.

**Most common causes:**
1. Oil cooler fouled or scaled
2. Cooling water flow low or absent
3. Thermostatic oil valve stuck
4. Discharge gas too hot, which heats the oil system
5. Wrong oil grade

**Diagnosis steps:**
1. Check oil cooler entering and leaving temperatures.
2. Check water flow across the oil cooler if water-cooled.
3. Check the thermostatic oil valve position and response.
4. Compare oil temperature to discharge temperature and load.

**Fix:**
Restore oil cooling and confirm the correct oil grade for the refrigerant and operating range.

---

## ID 43, High Oil Filter Differential Pressure Alarm + Shutdown

**Meaning:** Pressure drop across the oil filter exceeded the alarm and shutdown limit. Sabroe manuals call for filter replacement once the pressure drop exceeds about **0.7 bar** on SAB 202 operating guidance. UniSAB III factory alarm settings often run around **0.7 to 1.2 bar**, depending on the compressor family.

**Most common causes:**
1. Oil filter plugged with wear debris or sludge
2. Cold oil causing temporarily high pressure drop after startup
3. Wrong viscosity oil
4. Contamination after maintenance work

**Diagnosis steps:**
1. Check whether the high filter differential clears as oil warms up.
2. Compare filter differential pressure at startup and after 15 to 20 minutes.
3. Cut open the old filter after replacement if you suspect bearing wear.

**Fix:**
Replace the oil filter. If the new filter plugs quickly, stop and inspect bearings, oil condition, and internal wear sources.

---

## ID 46, Compressor Motor Overload Shutdown

**Meaning:** The motor overload protection opened.

**Most common causes:**
1. High compression ratio
2. High condensing pressure
3. Power supply imbalance or one phase missing
4. Mechanical drag in the compressor
5. VSD current limit or overload condition

**Diagnosis steps:**
1. Read motor current and compare to nameplate full-load amps.
2. Check phase voltages and current balance.
3. Review whether discharge pressure or pressure ratio alarms happened first.
4. Listen for abnormal compressor noise after you isolate power.

**Fix:**
Do not simply reset the overload and restart. Confirm that motor current returned to normal and that process pressures make sense.

---

## ID 47, Compressor Motor Error / Emergency Stop / HP Shutdown

**Meaning:** The controller saw an external motor protection or emergency stop event. The same ID can appear for motor guard trips, emergency stop activation, or a hardwired high-pressure safety input.

**Diagnosis steps:**
1. Check the emergency stop station first.
2. Inspect the motor starter or protection relay for a trip flag.
3. Check hardwired HP cutout devices in the panel.

**Reset:**
Correct the field condition, then press **F4 / RESET**. If the machine is in remote or auto mode, it may restart on its own when you clear the shutdown. Make sure the system is ready before reset.

---

## ID 49, High Motor Temperature Shutdown

**Meaning:** The motor thermistor input tripped.

**Most common causes:**
1. True motor overheating from overload
2. Cooling fan failure on air-cooled motor
3. High ambient temperature in the machine room
4. Failed thermistor cable or loose terminal

**Diagnosis steps:**
1. Compare motor temperature trip timing with motor current history.
2. If current stayed normal, inspect the thermistor circuit for damage.
3. Check airflow across the motor body.

---

## Vibration Faults on Sabroe Packages

Many newer Sabroe screw packages use the Sabroe Vibration Monitoring system. The package may show a dedicated vibration alarm in the package PLC or pass it to UniSAB as an external or user alarm.

**Meaning:** Bearing vibration exceeded the warning or shutdown threshold.

**Most common causes:**
1. Bearing wear
2. Coupling misalignment
3. Pipe strain on the compressor nozzles
4. Loose skid bolts or frame resonance

**Diagnosis steps:**
1. Review vibration trend, not just the trip point.
2. Compare drive-end and non-drive-end readings.
3. Check coupling alignment and pipe support.

**Fix:**
Treat vibration trips as mechanical warnings. Do not run repeated restart cycles until you inspect bearings and alignment.

---

## Communication Faults and Controller Errors

Sabroe controllers can also stop a machine for communication or control faults.

### Common IDs
- **55 PMS error shutdown**
- **72 No communication to PLC shutdown**
- **89 VSD link missing alarm / general drive error shutdown**
- **90 Feedback error from VSD shutdown**
- **91 Drive link error shutdown**

**Most common causes:**
1. Loose serial or network cable
2. VSD powered down while controller still runs
3. PLC offline or fieldbus watchdog timeout
4. Incorrect node address after maintenance

**Diagnosis steps:**
1. Check whether the compressor can read live drive data such as speed and current.
2. Inspect communication LEDs on the drive and controller.
3. Check recent parameter or wiring changes.

**Fix:**
Restore the communication link first. If the drive link returns and all permissives are healthy, clear the shutdown and confirm the controller sees valid drive feedback.

---

## Interlock Trip Sequence You Should Check First

When a Sabroe compressor trips, check interlocks in this order:

1. Emergency stop active
2. Motor protection active
3. Oil pressure healthy
4. Oil temperature above minimum startup level
5. Suction pressure and discharge pressure inside limits
6. Condenser and evaporator flow proven
7. Drive or PLC communication healthy

That order saves time because oil pressure, emergency stop, and motor protection trips often block every other restart attempt.

---

## Parts Reference Table

| Part | Application | Notes |
|---|---|---|
| Oil filter element | SAB 128/163/202, HPC | Replace when differential pressure rises; investigate debris source if repeat plugging occurs |
| Oil separator level switch | Screw packages with oil system error alarm | Trips ID 44 or related oil system alarms |
| Pressure transmitter, Danfoss AKS 3000 | Suction, discharge, oil pressure | Sabroe commonly uses -1 to 9 bar, -1 to 25 bar, or -1 to 59 bar transmitters |
| Pt100 temperature sensor | Discharge temp, oil temp, process temp | Check resistance and wiring before replacing controller |
| Vibration sensor | Packages with Sabroe Vibration Monitoring | Trend bearings and coupling condition |
| Oil heater | Standstill oil temperature protection | Critical for avoiding low oil temperature trips |
| Oil pump | Screw and HPC packages with pumped oil system | Check set points and start timers in controller |
| Position transmitter | Capacity slide and Vi slide on SAB screw compressors | Bad feedback can cause capacity or Vi position faults |

---

## Maintenance Checks That Prevent Most Trips

Sabroe operating guidance for SAB 202 units calls for daily logging of:
- suction pressure
- condensing pressure
- oil differential pressure
- oil level
- suction gas superheat
- discharge pipe temperature
- oil condition
- motor power draw

Also check oil filter pressure drop. Sabroe guidance says to replace the filter as soon as the pressure drop exceeds **0.7 bar** to avoid a forced shutdown.

## Quick Fault Reference

| Symptom | First ID to check | Likely cause |
|---|---|---|
| Compressor trips on hot day | 36 | Condenser problem or non-condensables |
| Compressor trips after low load period | 31 or 37 | Starved evaporator, low suction |
| Trip after startup | 41 or 38 | Oil too cold or oil differential not established |
| Repeated oil alarms | 38, 43, 105 | Low oil level, blocked filter, weak pump |
| Motor trip with normal pressures | 46 or 49 | Electrical issue or motor cooling problem |
| Controller says drive link missing | 89, 90, 91 | VSD or communication fault |
| HPC unit trips on pressure spread | 57 | Pc minus Pe too high |

If a Sabroe machine gives you multiple alarms at once, trust the first one in history, not the last one on screen. The last alarm often shows the consequence. The first alarm usually shows the cause.

## Where to Buy Replacement Parts

Find replacement parts for Sabroe (Johnson Controls) compressors on Amazon:

- [Sabroe Compressor Parts](https://www.amazon.com/s?ascsubtag=ecf-sabroe-compressor-fault-codes&k=Sabroe+compressor+parts&tag=errorcodefixes-20)
- [Industrial Screw Compressor Oil Filter](https://www.amazon.com/s?ascsubtag=ecf-sabroe-compressor-fault-codes&k=industrial+screw+compressor+oil+filter+replacement&tag=errorcodefixes-20)
- [Compressor Pressure Transducer & Sensor Kit](https://www.amazon.com/s?ascsubtag=ecf-sabroe-compressor-fault-codes&k=compressor+pressure+transducer+sensor+replacement&tag=errorcodefixes-20)