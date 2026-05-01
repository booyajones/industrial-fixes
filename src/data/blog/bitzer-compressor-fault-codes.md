---
title: "Bitzer Compressor Fault Codes — Complete Troubleshooting Guide"
description: "Bitzer scroll, reciprocating, and screw compressor fault codes. What each code means and how to fix it."
pubDatetime: 2026-04-27T21:00:00Z
modDatetime: 2026-04-27T21:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - compressor
  - bitzer
---

Bitzer is one of the most widely installed compressor brands in commercial refrigeration and HVAC. The **CSVH scroll**, **ECOLINE reciprocating**, and **CSH/HSK screw** series are found in supermarket racks, industrial refrigeration systems, and chiller applications worldwide. When a Bitzer compressor faults, the protection device — whether a **BITZER IQ Module**, **CM-RC-01**, **OLC-D1**, or older **BMSK (Bitzer Motor Safety Controller)** — generates a fault code via LED pattern, Modbus register, or the BEST SOFTWARE dashboard. This guide covers the full fault code set with causes, diagnosis procedures, and reset steps written for commercial refrigeration technicians.

## Jump to Section

- [Bitzer Protection Module Overview](#bitzer-protection-module-overview)
- [Accessing Fault History](#accessing-fault-history)
- [E01 — High Pressure Cutout](#e01--high-pressure-cutout)
- [E02 — Low Pressure Cutout](#e02--low-pressure-cutout)
- [E03 — High Discharge Temperature](#e03--high-discharge-temperature)
- [E04 — Motor Overload / Winding Temperature](#e04--motor-overload--winding-temperature)
- [E05 — Oil Pressure Differential Fault](#e05--oil-pressure-differential-fault)
- [E06 — Phase Fault](#e06--phase-fault)
- [E07 — Motor Protection (PTC / Thermistor)](#e07--motor-protection-ptc--thermistor)
- [E08 — Suction Pressure Fault](#e08--suction-pressure-fault)
- [BMSK LED Fault Codes](#bmsk-led-fault-codes)
- [IQ Module Alarm and Warning Codes](#iq-module-alarm-and-warning-codes)
- [SEG Controller Codes](#seg-controller-codes)
- [Modbus Alarm Register Reference](#modbus-alarm-register-reference)
- [Parts Reference Table](#parts-reference-table)

---

## Bitzer Protection Module Overview

Bitzer compressors use several generations of protection and control modules. Knowing which module is installed determines which codes apply:

**BMSK (Bitzer Motor Safety Controller)** — older mechanical relay-based protection module. Uses LED flash patterns to signal fault type. Found on older ECOLINE and semi-hermetic units. No data bus.

**OLC (Oil Level Controller / OLC-D1)** — monitors oil level via capacitive sensor on the oil sight glass. Faults via relay output.

**IQ MODULE (CM-RC-01)** — smart electronic module introduced with the ECOLINE generation. Controls oil heater, VARISTEP capacity control, monitors all sensors, and communicates via Modbus RTU. Can be read and configured with Bitzer **BEST SOFTWARE** (free download at bitzer.de) or **BEST APP** (iOS/Android).

**CSV (Compressor Safety and Voltage monitor)** — module for screw compressors with extended data logging and Modbus alarm list (firmware 2.21+).

**LOGVIEW** — standalone fault logger available for some compressor lines. Stores detailed operating data and alarm history.

For all modern Bitzer ECOLINE compressors with the IQ Module, the **BEST SOFTWARE** provides the most complete fault diagnosis: real-time sensor readings, alarm history, LED status, and Modbus communication — all in one interface.

---

## Accessing Fault History

### Via BEST SOFTWARE (IQ Module / CM-RC-01)

1. Download BEST SOFTWARE from **bitzer.de/en/downloadcenter** (free, Windows).
2. Connect to the IQ Module via **Bluetooth** (built into CM-RC-01) or **USB-to-RS485 adapter** on the Modbus RTU terminal.
3. Open the **Alarm List** — displays all current alarms with severity (warning, critical, fault).
4. Open the **Data Log** — time-stamped record of operating data and alarm events.
5. The alarm list is also accessible via Modbus since firmware 2.21 (see Modbus Alarm Register Reference below).

### Via BEST APP

1. Install BEST APP on iOS or Android (search "BITZER BEST APP").
2. Connect via Bluetooth to the IQ Module.
3. Navigate to **Alarms** — shows current faults and history.
4. Use **Data Log** to export operating data for trend analysis.

### Via BMSK LED Patterns

The BMSK module communicates faults via the red LED:

- **Continuous steady red** — motor protection tripped (PTC thermistor)
- **1 flash** — high pressure cutout
- **2 flashes** — low pressure cutout
- **3 flashes** — oil differential pressure fault
- **4 flashes** — discharge temperature fault
- **5 flashes** — phase fault (phase loss or reversal)
- **Rapid flashing** — internal BMSK fault

Count flashes in each group, with a pause between groups. Each flash sequence repeats.

---

## E01 — High Pressure Cutout

**Code:** E01 | **Severity:** Fault (compressor shutdown) | **LED:** 1 flash (BMSK)  
**Display message:** "High pressure cutout — check condenser and refrigerant charge"

### What Triggers It

The high pressure switch or high pressure transducer connected to the protection module detected discharge pressure above the safety cutout setpoint. Typical cutout values:
- R-404A / R-449A: 26–28 bar (377–406 psi)
- R-134a: 17–19 bar (247–276 psi)
- R-407C: 27–29 bar (392–421 psi)

### Causes (in order of frequency)

1. **Condenser fouling** — dirty condenser coils (air-cooled) or fouled tube bundle (water-cooled)
2. **Condenser fan failure** — one or more fans not running or running backwards
3. **High ambient temperature** — exceeds design conditions for the condenser
4. **Non-condensables** — air in the system raises head pressure without increasing refrigerant charge
5. **Refrigerant overcharge** — excess refrigerant floods the condenser
6. **Condenser water flow fault** (water-cooled) — pump failure, valve closed, fouled tubes
7. **High pressure switch stuck or miscalibrated** — check switch setpoint and contact operation

### Diagnosis Steps

1. Read discharge pressure on a gauge set at the service valve — compare to system design pressure.
2. Check condenser approach temperature (condensing temp minus ambient). Should be 10–15°F on air-cooled. Higher indicates fouling.
3. Verify all condenser fans are running at correct speed and direction. Reversed fan blade or reversed motor rotation drastically reduces airflow.
4. Check for non-condensables: after machine has run, allow it to equalize and read static pressure. If pressure is higher than the expected saturation pressure for the ambient temperature, suspect non-condensables.
5. Check the high pressure switch calibration — compare the switch trip point to the manufacturer's setpoint. A switch that trips below specification may have a weak spring.

### Reset Procedure

The high pressure switch is typically a manual reset type — press the reset button on the switch after pressure has dropped below the differential reset point. On systems with the IQ Module, clear the fault in BEST SOFTWARE after correcting the root cause. Do not reset repeatedly without addressing the cause — repeated high pressure trips damage compressor valves.

---

## E02 — Low Pressure Cutout

**Code:** E02 | **Severity:** Fault | **LED:** 2 flashes (BMSK)  
**Display message:** "Low pressure cutout — check suction pressure and refrigerant levels"

### What Triggers It

Suction pressure dropped below the low pressure cutout setpoint. This protects the compressor from running unloaded and prevents evaporator freezing.

### Causes (in order of frequency)

1. **Refrigerant leak / undercharge** — most common
2. **Evaporator icing** — evaporator coil frosted over, blocking airflow and refrigerant flow
3. **Expansion valve malfunction** — TXV stuck closed or underfeeding
4. **Solenoid valve not opening** — liquid line solenoid failing to open on a call
5. **Filter-drier restricted** — excessive pressure drop across the drier
6. **Low suction pressure switch setpoint** — check against design specification

### Diagnosis Steps

1. Check suction pressure and compare to saturation temperature on a P-T chart. Saturation temp should be 15–20°F below evaporator temperature.
2. Inspect evaporator for ice build-up — if iced, initiate defrost cycle and correct the defrost timing.
3. Verify liquid line solenoid operation — listen for click when energized, feel for temperature differential across it.
4. Check TXV superheat at the evaporator outlet — low superheat indicates flooding; high superheat (above 15°F) indicates starvation (TXV, low charge, drier restriction).
5. Measure pressure drop across the filter-drier with a gauge at each port — more than 2 psig drop indicates restriction.
6. Check sight glass — bubbles at design conditions indicate low charge.

### Reset Procedure

Low pressure cutouts are often automatic reset types (reset automatically when pressure rises above the differential point). If the LPC trips repeatedly, it indicates a real system condition — do not short the LPC. Find and fix the root cause.

---

## E03 — High Discharge Temperature

**Code:** E03 | **Severity:** Fault | **LED:** 4 flashes (BMSK)  
**Display message:** "High discharge temperature — check oil injection and compression ratio"

### What Triggers It

The discharge temperature sensor at the compressor head detected temperature above the cutout setpoint. Typical cutouts:
- ECOLINE reciprocating: 230°F (110°C)
- CSVH scroll: 250°F (121°C)
- CSH screw: 220°F (104°C)

High discharge temperature is one of the most damaging fault conditions for a compressor — it causes oil carbonization, valve damage, and accelerated wear.

### Causes (in order of frequency)

1. **High compression ratio** — combination of high head pressure and low suction pressure
2. **Low refrigerant charge** — insufficient refrigerant mass flow reduces cooling of discharge gas
3. **Oil injection failure** (screw compressors) — oil injection is primary cooling method; flow restriction causes high discharge temp
4. **Liquid injection failure** (equipped models) — economizer or liquid injection not functioning
5. **Worn discharge valves** (reciprocating) — re-compression of hot discharge gas
6. **Discharge temp sensor fault** — verify with a contact thermometer at the discharge port

### Diagnosis Steps

1. Calculate compression ratio: P_discharge (absolute psia) / P_suction (absolute psia). For most refrigerants, CR above 8:1 will produce excessive discharge temperature.
2. If CR is normal but discharge temp is high, check liquid or oil injection operation.
3. For screw compressors (CSH/HSK): check oil injection pressure — should be 2–4 bar above suction pressure. Low differential indicates oil pump or filter issue.
4. Measure discharge temperature with an independent contact thermometer at the sensor location — if the sensor reading matches the actual temperature, the root cause is in the refrigeration system.
5. For ECOLINE reciprocating: check cylinder head condition. A cracked head gasket allows hot discharge gas to re-circulate.

### Reset Procedure

Allow the compressor to cool down — typically 15–30 minutes. Reset via BEST SOFTWARE or the manual reset button on the BMSK. If the temperature fault trips within the first few minutes of restart, the root cause is not resolved.

---

## E04 — Motor Overload / Winding Temperature

**Code:** E04 | **Severity:** Fault | **LED:** Continuous steady red (BMSK — PTC trip)  
**Display message:** "Motor overload / winding temperature — check motor current and cooling"

### What Triggers It

Motor winding temperature exceeded the PTC thermistor trip threshold (typically 130–145°C for Bitzer motors). Or, on older systems, the motor overload relay tripped on sustained overcurrent.

### Causes (in order of frequency)

1. **Motor running in excessive compression ratio** — overloaded compressor draws excessive current
2. **Low supply voltage** — causes higher current at the same power output
3. **Phase imbalance** — unequal phase voltages increase motor heating
4. **Failed motor cooling** — on refrigerant-cooled motors, suction gas cools the motor. Low suction gas causes motor overheating.
5. **Starting too frequently** — excessive start-stop cycling without adequate off-time
6. **Motor winding degradation** — aged or partially failed winding increases resistance and heating

### Diagnosis Steps

1. Measure all three phase currents with a clamp meter. Compare to motor FLA (nameplate or Bitzer data sheet). More than 10% above FLA is a problem.
2. Measure supply voltage at the motor terminals — check all three phases and verify balance within 2%.
3. For hermetic/semi-hermetic: verify suction gas temperature. Suction gas above 65°F (18°C) may not provide adequate motor cooling on refrigerant-cooled designs.
4. Check start frequency — most Bitzer compressors specify maximum 10–12 starts per hour.
5. After the motor cools, measure winding resistance — asymmetry between phases indicates winding fault.

### Reset Procedure

The PTC thermistor resets automatically when the motor cools below the reset temperature (approximately 10–20°C below the trip threshold). Do not force-reset the BMSK while the motor is still hot — this will result in immediate re-trip and may cause winding damage.

---

## E05 — Oil Pressure Differential Fault

**Code:** E05 | **Severity:** Fault | **LED:** 3 flashes (BMSK)  
**Display message:** "Oil pressure differential fault — check oil pump and separator"

### What Triggers It

The differential pressure between the oil pump outlet and suction pressure dropped below the minimum required for lubrication. The protection module measures the difference between oil pressure and suction pressure. If this differential falls below 0.8–1.0 bar (12–15 psi) for more than 120 seconds, the compressor trips.

This fault applies to compressor types with dedicated oil pumps: primarily ECOLINE and older semi-hermetic reciprocating units. Scroll compressors (CSVH) do not have separate oil pump circuits.

### Causes (in order of frequency)

1. **Low oil level** — oil migrated to the system during previous operation
2. **Plugged oil filter** — restricts oil pump output
3. **Oil pump failure** — internal wear or seized
4. **Oil diluted with refrigerant** — excessive refrigerant dissolved in oil, reducing viscosity
5. **Oil pressure differential switch fault** — switch or transducer reading incorrect

### Diagnosis Steps

1. Check the oil sight glass — oil level should be visible. If no oil visible, locate migrated oil and recover it from evaporators, long suction lines, and accumulator.
2. Check oil pressure at the oil pump outlet test port — compare to Bitzer specifications (typically 2–4 bar above suction pressure during operation).
3. Inspect the oil filter — if overdue for replacement or if measurable pressure drop exists across it, replace.
4. Check the crankcase heater — if the heater failed or was not energized before startup, refrigerant saturation in the oil dilutes viscosity and reduces oil pressure.
5. Test the oil differential pressure switch calibration independently.

### Reset Procedure

Restore oil level and verify oil pressure is within specification. Reset via BMSK reset button or BEST SOFTWARE. Allow 2–3 minutes of stable operation to confirm the fault does not return.

---

## E06 — Phase Fault

**Code:** E06 | **Severity:** Fault | **LED:** 5 flashes (BMSK)  
**Display message:** "Phase fault — check power supply"

### What Triggers It

The phase monitoring detects a phase loss, phase reversal (wrong rotation direction), or severe phase imbalance (typically more than 10% voltage asymmetry between phases).

### Causes (in order of frequency)

1. **Phase loss** — blown fuse on one phase, loose terminal, or utility supply issue
2. **Phase reversal** — phases connected in wrong sequence (common after service or new installation)
3. **Phase imbalance** — one phase significantly lower than the others
4. **Contactor contact failure** — one contact of the compressor contactor not making full contact

### Diagnosis Steps

1. Measure all three supply phases at the compressor contactors — check both voltage level and balance (within 2% of each other).
2. If any phase reads near zero, check the fuse on that phase and the contactor contact for that phase.
3. For phase reversal: verify correct phase sequence with a phase rotation meter. For Bitzer compressors, correct rotation is specified in the technical data sheet (view through sight glass if visible).
4. On hermetic compressors where direction can't be verified directly: check suction and discharge pressure — correct direction produces immediate pressure differential. Wrong direction barely affects pressures.

### Reset Procedure

Correct the phase issue. Swap any two phases if reversal is confirmed (power down completely first). Reset fault via BMSK or BEST SOFTWARE.

---

## E07 — Motor Protection (PTC / Thermistor)

**Code:** E07 | **Severity:** Fault  
**Display message:** "Motor thermistor trip — winding temperature protection"

On systems using a separate motor protection relay (MP10, PTC relay) rather than the BMSK, a motor thermistor trip may appear as E07 or as a relay output that feeds the control circuit.

### What Triggers It

PTC thermistors embedded in the motor windings exceeded the trip threshold.

### Causes and Diagnosis

Same as E04 — refer to the Motor Overload section above. E07 vs E04 distinction: E07 is specifically the thermistor trip (PTC resistance exceeded threshold), while E04 may encompass overcurrent relay trips on older systems. On IQ Module systems, both are reported in the alarm list.

---

## E08 — Suction Pressure Fault

**Code:** E08 | **Severity:** Warning (typically)  
**Display message:** "Suction pressure out of range"

On IQ Module-equipped compressors, suction pressure is monitored via a transducer. E08 may indicate suction pressure approaching the evaporator freezing limit (warning) or persistently below the minimum operating pressure (fault).

### Diagnosis

- Check suction pressure and compare to the evaporating temperature limit for the refrigerant in use.
- On CO₂ (R-744) transcritical systems: evaporator pressure must stay above triple point (~5.2 bar absolute). CO₂ system low pressure faults have more severe consequences than conventional refrigerant systems.
- Verify suction pressure transducer calibration by comparing to a reference gauge at the same port.

---

## BMSK LED Fault Codes

| LED Pattern | Fault | Action |
|------------|-------|--------|
| Steady red (no flash) | Motor protection (PTC trip) | Allow motor to cool; check power and load |
| 1 flash | High pressure cutout | Check condenser and pressure switch |
| 2 flashes | Low pressure cutout | Check refrigerant charge and TXV |
| 3 flashes | Oil pressure differential fault | Check oil level and oil pump |
| 4 flashes | High discharge temperature | Check compression ratio and liquid injection |
| 5 flashes | Phase fault | Check phase voltage and sequence |
| Rapid continuous | Internal BMSK fault | Replace BMSK module |
| Green only | Normal operation | No fault |

**Reading flash codes:** Count the flashes in one group (before the pause). The pause between groups is approximately 2–3 seconds. Codes repeat continuously until reset.

---

## IQ Module Alarm and Warning Codes

The Bitzer IQ Module (CM-RC-01) categorizes events as **warnings** (continue operation, alert operator) and **faults** (compressor shutdown). Key alarm codes accessed via BEST SOFTWARE or Modbus:

| Code | Category | Description |
|------|----------|-------------|
| A01 | Fault | High pressure cutout |
| A02 | Fault | Low pressure cutout |
| A03 | Fault | High discharge temperature |
| A04 | Fault | Motor overload / PTC trip |
| A05 | Fault | Oil pressure differential |
| A06 | Fault | Phase fault |
| A07 | Warning | Discharge temp approaching limit (pre-trip) |
| A08 | Warning | Motor thermistor approaching limit |
| A09 | Warning | Oil level low (OLC-D1 connected) |
| A10 | Warning | Operating hours service due |
| A11 | Fault | Internal IQ Module fault — check wiring |
| A12 | Warning | Suction pressure low — approaching LPC |
| A20 | Fault | Communication loss with Modbus master |
| W01 | Warning | High pressure pre-alarm |
| W02 | Warning | Low pressure pre-alarm |

On the BEST APP or BEST SOFTWARE, alarms show with a timestamp, the sensor value at the time of alarm, and a help text with recommended actions.

---

## SEG Controller Codes

Some Bitzer screw compressor systems use a **SEG (Screw Electronic Control)** unit or a **CSV (Compressor Safety and Voltage)** controller that displays more detailed fault codes. On CSV-equipped units (firmware 2.21+), the Modbus alarm list is the primary diagnostic tool.

Key SEG/CSV alarm categories:

| Category | Code Range | Description |
|----------|-----------|-------------|
| Pressure | 100–109 | High/low pressure faults on HP and LP circuits |
| Temperature | 200–209 | Discharge, suction, motor, and oil temperature faults |
| Motor | 300–309 | Overload, phase fault, PTC trip, start fault |
| Oil | 400–409 | Oil pressure differential, oil level, oil temperature |
| Communication | 500–509 | Modbus loss, watchdog fault |
| Internal | 600–609 | CSV hardware fault, sensor fault |

For the full CSV alarm list, access via **BEST SOFTWARE > CSV > Alarm List** or read Modbus holding registers at the addresses specified in the CSV operating manual.

---

## Modbus Alarm Register Reference

The IQ Module (firmware 2.21+) exposes the alarm list via Modbus RTU. Key register addresses:

| Register | Description |
|----------|-------------|
| 1000 | Alarm list — number of active alarms |
| 1001–1010 | Active alarm codes (slots 1–10) |
| 1011 | Fault log — number of logged events |
| 1012–1061 | Fault log entries (code, timestamp, sensor value) |
| 2000 | Compressor status (running/stopped/fault) |
| 2001 | Discharge temperature (°C × 10) |
| 2002 | Suction pressure (bar × 100) |
| 2003 | Discharge pressure (bar × 100) |
| 2004 | Motor current (A × 10) |
| 2005 | Oil pressure differential (bar × 100) |

Default Modbus settings: **9600 baud, 8-N-1, address 1** (configurable via BEST SOFTWARE). The CSV and IQ Module support Modbus RTU only — not Modbus TCP.

---

## Parts Reference Table

| Part | Application | Notes |
|------|-------------|-------|
| BMSK-2 (motor safety controller) | Semi-hermetic reciprocating | Current version. Replaces BMSK-1 (no Modbus) |
| IQ Module CM-RC-01 | ECOLINE reciprocating | Includes Bluetooth and Modbus RTU |
| OLC-D1 (oil level controller) | Reciprocating with oil separator | Capacitive oil level sensor |
| OLC-L1 (oil level controller) | Screw compressors | Specific to screw compressor oil circuit |
| High pressure switch | All models | Specify refrigerant and cutout pressure; manual or auto reset |
| Low pressure switch | All models | Specify refrigerant and cutout pressure |
| Discharge temperature sensor | ECOLINE / CSH / HSK | NTC type; verify connection to IQ module or BMSK |
| Oil differential pressure switch | ECOLINE reciprocating | DPS model; specify differential setpoint |
| Oil filter (replaceable element) | ECOLINE / CSH screw | Replace annually or on oil pressure fault |
| Crankcase heater | All models | Order by compressor model and voltage (110V/230V) |
| Motor PTC thermistor (replacement) | Semi-hermetic motors | Must match winding temperature rating |
| CSV controller | CSH/HSK screw | Screw-specific safety controller with Modbus |

*Use Bitzer's model identification tool at bitzer.de/en/products to confirm replacement part compatibility. Always provide the compressor serial number when ordering — motor and protection module specs vary by production date.*

---

## Technician Notes

- **BEST SOFTWARE is your diagnostic tool** — every Bitzer tech should have it installed. The Bluetooth connection to the IQ Module takes 30 seconds and gives you the full alarm history, real-time sensor readings, and operating statistics. Diagnosis time drops dramatically compared to traditional gauge-set work alone.
- **Crankcase heater discipline** — Bitzer compressors should have the crankcase heater energized whenever the compressor is off in an ambient temperature below 77°F (25°C). Heater failure leads to refrigerant migration into the oil sump, which causes low oil pressure faults and compressor damage on the next start.
- **Oil change intervals** — ECOLINE compressors use polyolester (POE) oil. POE absorbs moisture rapidly when exposed to atmosphere — always cap oil containers immediately. Oil should be changed per Bitzer's recommendation (typically every 4–6 years or after any motor fault that may have caused overheating and oil carbonization).
- **High pressure switch reset habit** — get in the habit of checking the system condition (pressures, condenser approach, fan operation) before resetting a high pressure switch. Resetting a HP switch into a running compressor without addressing the cause is the most common way to destroy a compressor in a single service call.
- **Phase rotation on new installations** — always check phase rotation with a meter before energizing a new or relocated Bitzer compressor. A single phase-reversed compressor will build very little pressure and may not trip any safety within the brief diagnostic period, but it runs backwards and will fail from oil starvation.

## Where to Buy Replacement Parts

Find replacement parts for Bitzer compressors on Amazon:

- [Bitzer Compressor Parts & Accessories](https://www.amazon.com/s?k=Bitzer+compressor+parts&tag=errorcodefixes-20)
- [Bitzer Crankcase Heater Replacement](https://www.amazon.com/s?k=Bitzer+crankcase+heater+replacement&tag=errorcodefixes-20)
- [Bitzer High Pressure Switch & Sensors](https://www.amazon.com/dp/B013J2J97A?tag=errorcodefixes-20)