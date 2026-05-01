---
title: "Mycom Compressor Fault Codes — Complete Troubleshooting Guide"
description: "Mycom reciprocating and screw compressor fault codes for N-series and F-series. What each alarm means and how to fix it."
pubDatetime: 2026-04-28T00:00:00Z
modDatetime: 2026-04-28T00:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - compressor
  - refrigeration
  - mycom
---

MYCOM compressors — built by Mayekawa Manufacturing — are workhorses in industrial refrigeration. You'll find them in cold storage facilities, food processing plants, and industrial process cooling running ammonia (NH3), HFCs, or hydrocarbon refrigerants. When a MYCOM trips, your refrigeration system is down and product is at risk. This guide covers the alarm codes and fault conditions for MYCOM N-series reciprocating and F-series single-screw compressors, including the ComPAC controller.

## Jump to Section

- [MYCOM Compressor Overview](#mycom-compressor-overview)
- [Protection Device Architecture](#protection-device-architecture)
- [ComPAC Controller Navigation](#compac-controller-navigation)
- [High Discharge Pressure (HP Trip)](#high-discharge-pressure-hp-trip)
- [Low Oil Pressure (OP Trip)](#low-oil-pressure-op-trip)
- [Discharge Temperature Fault](#discharge-temperature-fault)
- [Low Suction Pressure](#low-suction-pressure)
- [Motor Overload](#motor-overload)
- [Liquid Slugging](#liquid-slugging)
- [Vibration Alarm](#vibration-alarm)
- [Cooling Water Fault](#cooling-water-fault)
- [Communication and Controller Faults](#communication-and-controller-faults)
- [Reset Procedures](#reset-procedures)
- [Replacement Parts](#replacement-parts)

---

## MYCOM Compressor Overview

MYCOM (the brand name used by Mayekawa for industrial refrigeration compressors) covers two main compressor architectures in industrial installations:

**N-series Reciprocating Compressors** (N6, N8, N10, N12 — 6, 8, 10, and 12 cylinder)
- Open drive, belt or direct-coupled
- Used for ammonia, R404A, propane refrigerant systems
- Capacity controlled by cylinder unloaders (solenoid valve actuated)
- Typical applications: blast freezing, cold storage, process cooling

**F-series Single-Screw Compressors** (F6, F8, F10)
- High-capacity industrial screw design
- Variable capacity via slide valve
- More common in large ammonia refrigeration plants

Both series use external protection packages — typically PLC-based (Allen Bradley, Siemens) or the Mayekawa **MYPRO TOUCH+** (formerly ComPAC) controller. The controller monitors all protection devices and logs alarms with timestamps.

---

## Protection Device Architecture

MYCOM compressors use three tiers of protection:

| Protection Device | Abbreviation | Function |
|---|---|---|
| High Pressure Cutout | HP | Shuts down on high discharge pressure |
| Low Oil Pressure Protection | OP | Shuts down on low differential oil pressure |
| Low Pressure Control | LP | Controls capacity steps via suction pressure |
| Discharge Temperature Switch | DT | Shuts down on excessive discharge temperature |
| Motor Overload | OL | Thermal/electronic overload on motor |
| No-Flow (Cooling Water) | WF | Shuts down if cooling water flow is lost |

All HP and OP trips are **manual reset** — the condition must be resolved and the safety must be manually reset before restart. LP trips are auto-reset.

**Critical rule:** Never reset a compressor after an HP or OP trip without determining why it tripped. Back-to-back resets with an unresolved fault cause bearing damage and compressor failure.

---

## ComPAC Controller Navigation

The MYPRO TOUCH+ (and older ComPAC) provides:

- **Main screen:** Current pressures, temperatures, current, capacity step, run/stop status
- **Alarm history:** Time-stamped log of all trips with operating data at time of fault
- **Trend data:** Real-time and historical charts of key parameters
- **Manual control:** Capacity step override, manual start/stop for maintenance

### Accessing Alarm History on MYPRO TOUCH+

1. From the main screen, tap **Alarm** (bell icon or alarm button).
2. Select **History** to view past events or **Active** for current alarms.
3. Each event shows: fault type, timestamp, suction pressure, discharge pressure, discharge temperature, oil pressure differential, and current at fault time.
4. Use this data before reset — it tells you what the compressor was doing at the moment of shutdown.

### Accessing Alarm History on ComPAC (Legacy)

1. Press **ALARM LOG** button on the ComPAC panel.
2. Scroll through numbered alarm events. Most recent is first.
3. Press **PRINT** (if printer is connected) or document manually before reset.

---

## High Discharge Pressure (HP Trip)

**Alarm text:** `HP TRIP` / `HIGH PRESSURE CUTOUT` / `DISCHARGE PRESSURE HIGH`

**Trigger:** Discharge pressure has reached the HP cutout setpoint. For ammonia systems, typical HP setpoint is 2.0–2.7 MPa (gauge) depending on system design. The mechanical HP switch (if installed) also trips a separate circuit.

**Causes:**

*Air-cooled condensing:*
- Condenser coils blocked with ice, frost, or debris
- Condenser fan motor failure or running backwards
- High ambient temperature exceeding design conditions
- Refrigerant overcharge (high subcooling + high head pressure)
- Non-condensable gases (air/nitrogen) in the system — pressure gauge needle vibrates

*Water-cooled condensing (common in NH3 systems):*
- Condenser water pump failure
- Condenser water inlet temperature too high
- Condenser tube fouling or scale buildup
- Water-regulating valve malfunction
- Insufficient condenser water flow — check strainer and valve positions

**Diagnosis:**
1. Check discharge pressure at time of trip (ComPAC alarm history).
2. For water-cooled: verify condenser water pump is running, measure inlet/outlet water temperatures.
3. For air-cooled: inspect coils, check fan rotation and amperage.
4. Check subcooling — high subcooling with high head pressure indicates overcharge or non-condensables.
5. To check for non-condensables: isolate the condenser, allow system to equalize overnight, compare discharge pressure to ambient temperature saturation pressure for your refrigerant. If pressure is higher than expected, non-condensables are present.

**Reset:** Manual reset. For systems with a mechanical HP pressure switch (separate from the ComPAC), reset the mechanical switch first, then reset the ComPAC/control panel.

**Operating limit (M-series NH3):** Maximum discharge pressure 2.6 MPa (gauge) for standard units; 2.0 MPa for units equipped with shut-off valves.

---

## Low Oil Pressure (OP Trip)

**Alarm text:** `OP TRIP` / `LOW OIL PRESSURE` / `OIL PRESSURE FAULT`

**Trigger:** The differential oil pressure (oil supply pressure minus suction pressure) has dropped below the minimum setpoint. Per MYCOM specification, minimum oil pressure differential is typically **suction pressure + 0.15 MPa**. The OP device has a 30-second time delay to allow the oil system to build pressure on startup before the protection becomes active.

**Causes:**
- Low oil level in the crankcase — check oil sight glass
- Oil pump failure — worn gears, damaged shaft, or failed coupling
- Plugged oil filter — check pressure drop across filter inlet/outlet
- Oil pressure regulating valve set incorrectly or stuck open
- Refrigerant migration into oil (off-cycle refrigerant condensing in crankcase — oil appears foamy on startup)
- Oil strainer blocked (100-mesh strainer in suction line to oil pump)
- Suction pressure too high, reducing differential (excessive suction = OP trips even with normal oil pressure)

**Diagnosis:**
1. Check oil level at the sight glass — should be between lower and upper marks (10–90% of sight glass).
2. Start compressor briefly in manual mode (if safe) and observe oil pressure gauge — if it does not build within 30 seconds, OP trips normally.
3. Measure oil pressure at the pump outlet and compare to required differential: P_oil_supply = P_suction + 0.20–0.25 MPa (per MYCOM specification).
4. Shut down, remove the oil strainer from the main bearing head, and inspect for debris.
5. Change oil filter element if differential across filter exceeds 15–20 psid.
6. Check for refrigerant migration: if the crankcase oil is heavily diluted with refrigerant, it will appear foamy and the oil level may read high in the sight glass. Running the crankcase heater for 8–12 hours before restart drives refrigerant out of the oil.

**Reset:** Manual reset. Resolve oil system fault before restart.

**Oil pressure setpoint (from MYCOM documentation):**
- Minimum oil supply pressure: suction pressure + 0.15 MPa
- Maximum oil pump differential: 0.5 MPa
- Oil supply temperature range: 30–60°C

---

## Discharge Temperature Fault

**Alarm text:** `DISCHARGE TEMP HIGH` / `DT TRIP` / `HIGH DISCHARGE TEMPERATURE`

**Trigger:** Discharge gas temperature has exceeded the cutout setpoint. MYCOM's maximum discharge temperature specification is **160°C**. A warning typically triggers at 140–150°C.

**Causes:**
- High compression ratio (high discharge pressure combined with low suction pressure)
- Insufficient suction superheat — too much superheat entering compressor
- Cooling water flow failure (water-cooled head cover not receiving adequate flow)
- Discharge valve wear — leaking discharge valves allow hot discharge gas to re-expand back into cylinder
- High-stage discharge recirculating to low-stage suction (two-stage system misconfiguration)
- Oil cooler failure — oil temperature too high, heat transfer to refrigerant

**Diagnosis:**
1. Check compression ratio: (P_discharge + 1 atm) / (P_suction + 1 atm). Ratios above 8:1 will cause high discharge temperatures in most refrigerants.
2. Verify cooling water flow to head covers and oil cooler — feel for even temperature across all head jacket connections.
3. Check suction superheat — excessive superheat (>20°C) means the gas entering the compressor is already hot.
4. For discharge valve wear: after cooling, remove head covers and inspect valve plates for wear. Compare valve seat height to the 0.15mm minimum per MYCOM specifications.

**Discharge temperature monitoring:** MYCOM's daily inspection protocol requires recording discharge temperature every 2–3 hours. A trend of rising discharge temperature over days indicates a deteriorating condition before a fault trip occurs.

---

## Low Suction Pressure

**Alarm text:** `LOW SUCTION PRESSURE` / `LP TRIP` / `SUCTION PRESSURE LOW`

**Trigger:** Suction pressure has fallen below the LP setpoint. The LP device also controls capacity unloading steps.

**Causes:**
- Low refrigerant charge
- Liquid line restriction — filter-drier plugged, solenoid valve partially closed, liquid line valve not fully open
- Evaporator coil frosted over — insufficient defrost cycles
- Load side valve not fully open
- Expansion valve not opening properly
- Suction line restriction (rare — check for inadvertently closed suction valve)

**Diagnosis:**
1. Check suction pressure at the compressor suction stop valve.
2. Inspect liquid line sight glass for bubbles — flashing in the liquid line indicates refrigerant shortage or pressure drop.
3. Check evaporator coil condition — heavy frost accumulation reduces evaporator capacity and causes suction pressure to fall.
4. Verify all suction stop valves are fully open.
5. Check expansion valve operation: for thermostatic expansion valves, verify bulb is securely attached to suction line and not displaced.

**Low pressure control (LP) function:**
The LP device on MYCOM reciprocating compressors also controls capacity steps by monitoring suction pressure. When suction pressure drops below the unload setpoint, cylinders are unloaded via solenoid valve. This is automatic and does not generate a fault alarm — it is normal capacity control. A fault trip only occurs if pressure drops to the cutout setpoint.

---

## Motor Overload

**Alarm text:** `MOTOR OVERLOAD` / `OL TRIP` / `OVERCURRENT`

**Trigger:** Motor current has exceeded the thermal overload relay setting for a sustained period, or the overload has detected a phase imbalance or single-phase condition.

**Causes:**
- Mechanical overload — compressor binding from:
  - Liquid refrigerant flooding the cylinders on startup
  - Foreign material ingested through the suction filter
  - Worn bearings with increased friction
- Excessive compression ratio (high differential pressure) forcing motor to work harder
- Voltage imbalance on motor supply (>2% imbalance causes significant derating)
- Single-phasing at motor terminals
- Overload relay set below motor FLA
- Belt over-tension (belt-driven units) — excessive side load on crankshaft

**Diagnosis:**
1. Measure three-phase voltage at motor terminals under load. Calculate imbalance.
2. Check three-phase current — compare all phases. Any significant imbalance indicates wiring or motor issue.
3. Verify overload relay setting matches motor FLA on nameplate.
4. For belt-driven units: check belt tension per MYCOM specification. Over-tensioned belts cause high bearing loads.
5. Check for liquid slugging: crankcase frosted on exterior during or after startup indicates liquid refrigerant reaching the compressor.

**Reset:** Allow motor to cool for 10–15 minutes. Resolve root cause before restart.

---

## Liquid Slugging

Liquid slugging is not always a discrete fault code — it manifests as one of several symptoms:

**Signs of liquid slugging:**
- Unusual knocking or hammering sound at startup or during operation
- Crankcase frosted on exterior surface
- Oil pressure drops suddenly after startup
- HP trip following an erratic suction pressure spike
- Discharge pressure gauge needle deflecting erratically

**Causes:**
- Refrigerant migration into crankcase oil during off-cycle (refrigerant condenses in crankcase)
- Expansion valve flooding — too much refrigerant reaching suction
- Flooded evaporator during startup before superheat is established
- Suction line liquid trap — liquid accumulating in low points in the suction piping

**Prevention and diagnosis:**
1. Ensure crankcase heaters are energized during all off-cycle periods. MYCOM heaters should run continuously when compressor is off.
2. At startup, verify crankcase oil is clear, not foamy. Foamy oil indicates significant refrigerant dilution.
3. Per MYCOM operating limits: maximum degree of superheat entering the compressor is 20°C. Ensure suction superheat is measured and controlled.
4. If slugging is suspected during operation: close the suction stop valve partially to reduce refrigerant flow until conditions stabilize, then gradually reopen.

---

## Vibration Alarm

**Alarm text:** `VIBRATION HIGH` / `VIBRATION WARNING` / `VIB ALARM`

**Trigger:** Vibration sensor (if equipped on MYPRO TOUCH+ units) has exceeded warning or cutout threshold.

**MYCOM vibration standards (from engineering documentation):**

| Zone | Vibration Velocity | Action |
|---|---|---|
| A or B | < 7.1 mm/s rms | Normal operation |
| C | 7.1–18 mm/s rms | Investigate cause |
| D | > 18 mm/s rms | Stop immediately |

**Causes of excessive vibration:**
- Loose foundation bolts or baseframe
- Belt drive misalignment or worn belts
- Worn bearings (main bearings, connecting rod bearings)
- Liquid slugging — hydraulic shock in cylinders
- Resonance from connected piping — piping natural frequency matching compressor excitation frequency
- Coupling misalignment (direct-coupled units)

**Diagnosis:**
1. Measure vibration at the bearing housings in all three axes.
2. Inspect foundation bolts for looseness.
3. Check belt tension and V-belt condition.
4. Inspect piping supports — loose or missing pipe supports allow piping to resonate with compressor excitation.
5. If vibration increases gradually over weeks, worn bearings are likely. Schedule overhaul.

---

## Cooling Water Fault

**Alarm text:** `COOLING WATER FAULT` / `NO FLOW ALARM` / `WATER FLOW LOW`

**Trigger:** Cooling water flow to the water-cooled head covers and/or oil cooler has been interrupted.

**Important:** On MYCOM water-cooled compressors, cooling water **must flow during operation**. Loss of cooling water causes overheating of head covers and oil. MYCOM documentation states: cooling water must stop flowing when the compressor is NOT running to prevent refrigerant condensation in the crankcase.

**Causes:**
- Cooling water pump failure
- Cooling water supply valve partially or fully closed
- Water flow switch faulty or set too high
- Scaled or blocked cooling water passages
- Pressure loss in cooling water supply

**Diagnosis:**
1. Verify cooling water pump is running — check pump status and motor amperage.
2. Measure cooling water flow rate and temperature differential across the oil cooler.
3. Check water flow switch: remove the switch and test continuity with water flowing.
4. Inspect cooling water piping for blockages — scale buildup is common in hard water areas.

**MYCOM cooling water limit:** Cooling water outlet temperature must not exceed 50°C. Cooling water pressure must not exceed 0.6 MPa (gauge).

---

## Communication and Controller Faults

### MYPRO TOUCH+ Communication Error

**Cause:** Lost communication between the MYPRO TOUCH+ panel and field instruments (pressure transducers, temperature sensors, motor protection relay).

**Diagnosis:**
1. Check all wiring connections to the MYPRO TOUCH+ analog and digital input modules.
2. Verify sensor power supply voltage (typically 24VDC).
3. Check for corroded or loose terminal block connections — industrial refrigeration environments are humid and corrosive.
4. For Modbus/RS485 sensors: check termination resistors (120Ω at each end of the bus).

### Sensor Out of Range

**Cause:** A pressure transducer or temperature sensor is reading outside its configured range. Common on startup after sensor replacement if wrong sensor range is selected.

**Fix:** Verify sensor range matches the MYPRO TOUCH+ configuration. Replace sensor if actual value is within range but reading is erratic (failing transducer).

---

## Reset Procedures

### Standard Reset Sequence

1. **Identify the fault** — read alarm history before touching anything.
2. **Document conditions at fault** — suction pressure, discharge pressure, discharge temperature, current, oil pressure from alarm history.
3. **Resolve the fault condition** — do not reset until the cause is corrected.
4. **Reset mechanical safeties** — HP switch and OP device may have separate manual reset buttons (pushbutton or pull-and-turn type on the pressure switch body).
5. **Reset the control panel** — press RESET or ALARM RESET on ComPAC/MYPRO TOUCH+.
6. **Verify before restart** — check oil level, verify cooling water flow, check suction and discharge valves are open.
7. **Start and monitor** — watch discharge pressure and temperature for first 10 minutes after restart.

### Startup After Extended Outage

Per MYCOM operating instructions, before restarting after any extended off period:

1. Check oil level is within 10–90% of sight glass.
2. Verify crankcase oil is clear (not foamy from refrigerant dilution). If foamy: run crankcase heater for 8+ hours before restart.
3. Verify oil temperature is ≥ 30°C before starting.
4. Check all suction and discharge stop valves are in correct position.
5. Manually rotate crankshaft (or jog briefly) and verify oil pressure builds within the 30-second OP timer period.

### Start/Stop Limits

MYCOM specifies the following start/stop limits for reciprocating compressors:
- Maximum 3 starts per hour
- Minimum 5-minute stop time between starts
- Minimum 15-minute run time per start cycle

Exceeding these limits causes excessive motor heating and mechanical wear.

---

## Replacement Parts

| Part | Application | Notes |
|---|---|---|
| **Oil filter element** | All N-series, F-series | Replace at 100-hour initial run, then every 3,000 hours or annually |
| **Oil strainer (100-mesh)** | All N-series | Clean at initial run and every 3,000 hours |
| **Discharge valve plate** | N-series | Replace when wear exceeds 0.20mm at seat. NH3 and HFC/propane types differ — confirm before ordering |
| **Suction plate valve** | N-series | Inspect at overhaul. Replace if seat contact depth > 0.20mm |
| **Valve spring (discharge)** | N-series | Replace at every overhaul (periodic wear item) |
| **Valve spring (suction)** | N-series | NH3 type: 10/cylinder; HFC/propane: 6/cylinder |
| **Piston rings** | N-series | Replace when abutment joint gap exceeds 2.5mm |
| **Cylinder sleeve** | N-series | Replace when bore exceeds 146.2mm (nominal 146mm) |
| **Oil pump assembly** | N-series | Replace if oil pressure cannot be maintained with filter and strainer clean |
| **Mechanical seal assembly** | N-series | Replace if oil leakage exceeds 12 cc/hour |
| **Pressure transducers (suction, discharge, oil)** | All models | Verify replacement matches existing signal range (0–10V, 4–20mA) |
| **Discharge temperature thermostat/sensor** | All models | Check winding/resistance per replacement instructions |
| **Crankcase heater** | All models | 100W–500W depending on model; test continuity before installation |

---

## Maintenance Schedule (MYCOM Specification)

| Interval | Task |
|---|---|
| Daily (every 2–3 hours) | Record suction pressure, discharge pressure, oil pressure, discharge temperature, oil level, current |
| Monthly | Belt tension check, protection device operation test, oil analysis |
| 100 hours | Oil change, oil strainer clean, oil filter replacement |
| 3,000 hours | Oil change, strainer clean, filter replacement, suction filter inspection |
| First overhaul (4,000–8,000 hrs depending on speed) | Piston rings, valve plates, valve springs, cylinder sleeve inspection |
| Second overhaul (8,000–16,000 hrs) | Full disassembly including crankshaft, main bushings |

First overhaul interval is earlier for higher-speed operation:
- 800–1,200 RPM: First overhaul at 8,000 hours or 1 year, whichever comes first
- 1,200–1,500 RPM: First overhaul at 4,000 hours or 1 year

## Where to Buy Replacement Parts

Find replacement parts for Mycom compressors on Amazon:

- [Mycom Compressor Parts & Accessories](https://www.amazon.com/s?k=Mycom+compressor+parts&tag=errorcodefixes-20)
- [Industrial Compressor Oil Filter Replacement](https://www.amazon.com/s?k=industrial+compressor+oil+filter+replacement&tag=errorcodefixes-20)
- [Compressor Discharge Temperature Sensor](https://www.amazon.com/dp/B09FFFPF5L?tag=errorcodefixes-20)