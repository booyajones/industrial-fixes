---
title: "York Chiller Fault Codes — Complete Troubleshooting Guide"
description: "York chiller fault codes for YVAA, YVFA, YWHA, and OptiView series. What each alarm means and how to fix it."
pubDatetime: 2026-04-28T00:00:00Z
modDatetime: 2026-04-28T00:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - hvac
  - chiller
  - york
---

York chillers — now part of Johnson Controls — use the **OptiView Control Center** across the YVAA (air-cooled screw), YVFA (VSD air-cooled screw), YWHA (water-cooled), and YT (centrifugal) product families. When a fault triggers, the OptiView logs it with timestamp and operating data. This guide covers the most common York chiller fault codes, what causes each one, and how to diagnose and reset.

## Jump to Section

- [OptiView Control Center Overview](#optiview-control-center-overview)
- [Fault Code Structure](#fault-code-structure)
- [Accessing OptiView Alarm History](#accessing-optiview-alarm-history)
- [High Pressure Cutout Faults](#high-pressure-cutout-faults)
- [Low Pressure Cutout Faults](#low-pressure-cutout-faults)
- [Motor and Electrical Faults](#motor-and-electrical-faults)
- [Oil System Faults](#oil-system-faults)
- [Evaporator and Temperature Faults](#evaporator-and-temperature-faults)
- [VSD Faults (YVFA Models)](#vsd-faults-yvfa-models)
- [Sensor Faults](#sensor-faults)
- [Guide Vane and Capacity Control Faults (YT)](#guide-vane-and-capacity-control-faults-yt)
- [Reset Procedures](#reset-procedures)
- [Replacement Parts](#replacement-parts)

---

## OptiView Control Center Overview

The OptiView Control Center is York's standard controller for mid-to-large commercial and industrial chillers. It provides:

- 10.4" color touchscreen interface
- Real-time operating parameters (all pressures, temperatures, currents)
- Complete alarm and fault log with operating data at time of fault
- Remote communications (ModBus, BACnet, LonWorks options)
- Service mode for manual operation of actuators

OptiView severity classifications:

| Classification | Behavior |
|---|---|
| **Safety Cutout** | Immediate compressor shutdown, manual reset required |
| **Fault/Inhibit** | Compressor shutdown, condition must clear |
| **Warning** | No shutdown — operator notification only |
| **Start Inhibit** | Prevents startup but no active fault |

---

## Fault Code Structure

York/OptiView faults are displayed as text strings rather than numeric codes, though the system assigns internal code numbers visible in service tools. Faults are categorized as:

- **System Faults** — affect entire chiller (both refrigerant circuits)
- **Circuit Faults** — affect a single refrigerant circuit (Sys 1 or Sys 2)
- **VSD Faults** — specific to variable-speed drive units

The OptiView displays the fault type, circuit (if applicable), current operating parameters, and previous 5 shutdown causes.

---

## Accessing OptiView Alarm History

### From the Control Panel

1. From the main screen, press **History** or navigate to **Main Menu → History**.
2. The OptiView stores the **last 25 fault events** with time, date, and full operating snapshot.
3. Each entry includes: leaving chilled water temp, entering/leaving condenser temp, suction pressure, discharge pressure, motor amps, VSD status (if applicable), oil pressure.
4. Press any entry to expand the full data set.

### Viewing Unit Log Data

York's **unit log** (also accessible from History) records operating data every 5 minutes during normal operation. This is distinct from fault history and provides trend data to identify developing problems before they trip the chiller.

### With JCI Service Tools (Tech View)

Johnson Controls Tech View software provides deeper diagnostics:
- Full alarm history export
- Real-time trending of all parameters
- Override capability for component testing
- Fault code lookup with detailed diagnostic guidance

---

## High Pressure Cutout Faults

### System Fault: High Discharge Pressure (Hardware — HPCO)

**Fault code:** Code 48 (internal) — `HIGH DISCHARGE PRESSURE (HARDWARE - HPCO)`

**Trigger:** The mechanical high-pressure cutout switch (HPCO) has opened. This is a hardware safety independent of the OptiView software logic.

**Applies to:** YVAA, YVFA, YWHA, YT

**Causes (YVAA/YVFA air-cooled):**
- Dirty or blocked condenser coils — the #1 cause on air-cooled units
- Condenser fan failure or incorrect rotation
- High ambient temperature
- Refrigerant overcharge
- Non-condensable gases

**Causes (YWHA water-cooled):**
- Insufficient condenser water flow
- High condenser entering water temperature
- Fouled condenser tubes
- Condenser water valve not fully open

**Diagnosis:**
1. Check condenser coil condition — clean with low-pressure water if fouled.
2. Verify all condenser fans are running and rotating in the correct direction (airflow should be up through the coil on most YVAA units).
3. For water-cooled: measure condenser water pressure drop and flow rate. Compare to design values.
4. Check subcooling at liquid line — high subcooling (+10°F above normal) indicates overcharge.

**Reset:** Latching. Reset at OptiView after condition resolves. The mechanical HPCO switch on older YVAA/YWHA units may also require manual reset (pushbutton on switch body).

---

### System Fault: High Discharge Pressure (Software)

**Fault code:** Code 27 — `HIGH DISCHARGE PRESSURE (SOFTWARE)`

**Trigger:** OptiView software has detected discharge pressure above the software cutout threshold (typically set 5–10 psi below the hardware HPCO). This trips the compressor before the mechanical switch activates.

**Diagnosis:** Same as hardware HPCO. The software trip is a precautionary shutdown that allows for a more controlled unload sequence before full trip.

---

### System Fault: High Discharge Pressure Rate

**Fault code:** Code 55 — `HIGH DISCHARGE PRESSURE RATE`

**Trigger:** The rate of discharge pressure rise is too steep, indicating a rapid deterioration in condensing conditions.

**Causes:**
- Sudden fan motor failure during high ambient conditions
- Rapid fouling (e.g., plastic bag or debris across coil face)
- Condenser water flow suddenly reduced

---

## Low Pressure Cutout Faults

### System Fault: Low Suction Pressure

**Fault code:** Code 30 — `LOW SUCTION PRESSURE`

**Trigger:** Suction pressure has reached the cutout threshold.

**Causes:**
- Low refrigerant charge
- Expansion device not opening (EXV motor failure, plugged orifice)
- Low chilled water load with unit not unloading fast enough
- Evaporator freeze — reduced heat transfer raises compression work
- Filter-drier restriction (frost on inlet is a diagnostic sign)

**Diagnosis:**
1. Check refrigerant charge — suction superheat at compressor should be 8–15°F.
2. Verify EXV (Electronic Expansion Valve) position in OptiView service menus.
3. Check chilled water flow rate and entering/leaving temperature differential.
4. Inspect filter-drier — if inlet is cold and outlet is warm, the drier is causing a pressure drop restriction.

---

### System Fault: Low Suction Pressure — Smart Freeze

**Fault code:** Code 52 — `LOW SUCTION PRESSURE SMART FREEZE`

**Trigger:** The "Smart Freeze Protection" algorithm on newer OptiView units has detected suction temperature approaching the evaporator freeze point.

This is a more sensitive protection than a simple pressure cutout — it monitors suction saturation temperature vs. leaving chilled water temperature and shuts down earlier to protect the evaporator from freeze damage.

**Causes:** Same as standard low suction pressure fault, plus:
- Water flow below minimum for the unit (check evaporator water flow rate)
- Flow switch not operating correctly

---

### System Fault: Low Leaving Chilled Liquid Temperature

**Fault code:** Code 3 — `LOW CHILLED LIQUID TEMPERATURE`

**Trigger:** Leaving chilled water temperature has dropped to the cutout setpoint (typically 36°F or 2°C for water systems).

**Causes:**
- Load drops to near zero with chiller still running at minimum capacity
- Water flow through evaporator too low
- Setpoint error (setpoint set too close to cutout)

**Reset:** Non-latching in most cases — the chiller will restart automatically when leaving water temperature rises above the restart setpoint.

---

## Motor and Electrical Faults

### System Fault: Motor Current Overload (Hardware)

**Fault code:** Code 17 — `MOTOR CURRENT OVERLOAD (HARDWARE)`

**Trigger:** The motor protection relay or CT-based overload detection has tripped on sustained overcurrent.

**Causes:**
- High compression ratio forcing motor harder
- Voltage imbalance (>2% causes motor derating)
- Mechanical overload — compressor binding
- Single-phasing at motor terminals

**Diagnosis:**
1. Measure three-phase voltages at motor terminals and calculate imbalance.
2. Compare measured current to motor nameplate FLA.
3. Check for high discharge pressure conditions simultaneously — high head increases motor load.

---

### System Fault: Motor Current Overload (Software)

**Fault code:** Code 43 — `MOTOR CURRENT OVERLOAD (SOFTWARE)`

**Trigger:** OptiView has calculated motor utilization above threshold based on CT readings. Typically trips at 110–115% of FLA setting.

---

### System Fault: Control Voltage

**Fault code:** (varies) — `SYSTEM FAULT: CONTROL VOLTAGE`

**Trigger:** Control power supply voltage is outside the acceptable range for the OptiView and associated controls.

**Causes:**
- Control transformer failure
- Blown fuse in control circuit
- Low incoming voltage causing control transformer output to sag
- Failed relay or contactor coil loading down the 24V supply

**Diagnosis:**
1. Measure 24VAC or 115VAC (depending on model) at the control transformer secondary.
2. Check all control fuses.
3. Verify control transformer primary voltage is within ±10% of rated voltage.

---

### System Fault: Single Phase Input (Unit)

**Fault code:** Code 14 — `SINGLE PHASE INPUT (UNIT)`

**Trigger:** One phase of the three-phase power supply is missing or significantly unbalanced at the unit disconnect.

**Causes:**
- Blown main fuse in one phase
- Failed main disconnect contactor
- Utility supply issue
- Loose power connection

**Diagnosis:** Measure voltage on all three phases at main disconnect. If one phase is missing, check upstream fuses and connections.

---

## Oil System Faults

### System Fault: High Differential Oil Pressure

**Fault code:** Code 28 — `HIGH DIFFERENTIAL OIL PRESSURE`

**Trigger:** Oil pressure differential (oil supply minus suction pressure) is too high, indicating a blockage in the oil return circuit or a malfunctioning oil pressure regulating valve.

**Causes (YVAA screw compressors):**
- Plugged oil separator return line
- Oil thermostatic valve stuck closed (oil too cold to circulate)
- Oil filter heavily fouled, creating excessive pressure drop

---

### System Fault: Low Differential Oil Pressure

**Fault code:** Code 29 — `LOW DIFFERENTIAL OIL PRESSURE`

**Trigger:** Oil pressure differential has dropped below minimum required for compressor bearing lubrication.

**Causes:**
- Oil pump failure
- Low oil level in separator
- Oil filter element plugged (paradoxically can also cause high differential — depends on where pressure is measured)
- Oil pressure transducer failure
- Oil diluted with refrigerant (foamy oil)

**Diagnosis:**
1. Check oil level in separator sight glass (unit running or just stopped).
2. Measure oil pressure differential from OptiView History.
3. Check oil filter replacement interval — York recommends annual replacement.
4. For units with high hours since last service: refrigerant dilution is common if crankcase heaters failed.

---

### System Fault: High Oil Temperature

**Trigger:** Oil temperature has exceeded the warning or cutout threshold.

**Causes:**
- Oil cooler fouled or refrigerant charge low (reducing oil cooling effectiveness on refrigerant-cooled oil circuits)
- High discharge temperature transferring heat to oil
- Oil cooler bypass valve stuck open

---

## Evaporator and Temperature Faults

### Evaporator Anti-Freeze Pump Fault

**Fault code:** Code 20 — `EVAP ANTI-FREEZE PUMP FAULT`

**Trigger:** The evaporator antifreeze pump (if equipped) has failed or flow switch is not satisfied.

**Causes:**
- Anti-freeze pump motor failure
- Anti-freeze flow switch not calibrated correctly
- Glycol solution too thick (overly concentrated) reducing pump efficiency

---

### System Fault: High Motor Temperature

**Fault code:** Code 36 (YVAA-specific) — `HIGH MOTOR TEMPERATURE`

**Trigger:** Motor winding temperature sensor has detected overtemperature.

**Causes:**
- High ambient temperature at motor location
- Poor ventilation around motor
- Motor overloaded (high compression ratio)
- Cooling refrigerant flow through motor reduced (hermetic motor cooling)

---

### System Fault: Low Heat Exchanger Temperature

**Fault code:** Code 21 — `LOW HEAT EXCHANGER TEMPERATURE`

**Trigger:** Heat exchanger (evaporator) refrigerant temperature has approached the freeze protection threshold.

**Causes:** Same as Low Chilled Liquid Temperature — loss of water flow is the primary cause.

---

## VSD Faults (YVFA Models)

The YVFA uses a Variable Speed Drive (VSD) to vary compressor speed based on load. VSD faults generate a separate fault category.

### VSD Fault: Communications Failure

**Fault code:** Code 7 — `VSD COMMUNICATIONS FAILURE`

**Trigger:** Communication between the OptiView and the VSD control board has been interrupted.

**Causes:**
- Loose or damaged VSD communication cable
- VSD control board power supply failure
- VSD software mismatch
- Electrical noise interference on communication cable

**Diagnosis:**
1. Check all VSD communication wiring connections.
2. Verify VSD power supply — look for fault indicators on VSD display.
3. Power cycle the VSD (with appropriate safety precautions — DC bus must discharge before working on VSD).

---

### VSD Fault: Initialization Failure

**Fault code:** Code 4 — `VSD INITIALIZATION FAILURE`

**Trigger:** VSD fails to complete its startup self-test sequence.

**Causes:**
- VSD parameters not configured for the motor installed
- VSD firmware incompatible with OptiView version
- VSD internal fault (gate driver, DC bus)

---

### VSD Fault: High Baseplate Temperature

**Fault code:** Code 45 — `HIGH BASEPLATE TEMPERATURE`

**Trigger:** VSD heat sink temperature has exceeded limits.

**Causes:**
- VSD cooling pump (glycol-cooled VSD units) failure
- Blocked VSD cooling circuit
- Ambient temperature at VSD too high
- VSD running at high output current for extended period

---

### VSD Fault: High VSD Ambient Temperature

**Fault code:** Code 13 — `HIGH VSD AMBIENT TEMPERATURE`

**Trigger:** Air temperature at the VSD enclosure has exceeded limits.

**Fix:** Check VSD enclosure ventilation. Verify that any cooling fans in the VSD enclosure are running.

---

### VSD Fault: High Harmonic Filter Temperature

**Fault code:** Code 19 — `HIGH HARMONIC FILTER TEMPERATURE`

**Trigger:** On units equipped with harmonic filters (line reactors or active filters), the filter temperature has exceeded limits.

**Fix:** Check harmonic filter cooling ventilation. Verify filter connections are tight (loose connections cause resistive heating).

---

### VSD Fault: Low DC Bus Voltage / Pre-charge Fault

**Fault codes:** Code 37/38 — `PRE-CHARGE LOW DC BUS VOLTAGE` / `PRE-CHARGE DC BUS VOLTAGE IMBALANCE`

**Trigger:** During VSD startup pre-charge phase, DC bus voltage is not building correctly.

**Causes:**
- Pre-charge resistor failed
- Pre-charge contactor fault
- One phase of supply missing
- DC bus capacitor failed

**Safety note:** Never work on VSD until DC bus voltage is confirmed at 0V. Fully charged DC bus can hold lethal voltage for several minutes after power removal.

---

## Sensor Faults

### System Fault: CT Plug Fault

**Fault code:** Code 18 — `CT PLUG FAULT`

**Trigger:** Current transformer (CT) plug is not connected or signal is out of range.

**Fix:** Verify CT wiring connections. Check CT plug is fully seated in OptiView input module.

---

### System Fault: Sensor Failure

**Fault code:** Code 34 — `SENSOR FAILURE`

**Trigger:** One or more temperature or pressure sensors is reading outside its configured range.

**Diagnosis:**
1. OptiView will identify which sensor is out of range.
2. Check sensor wiring for shorts, opens, or moisture intrusion.
3. For pressure transducers: verify supply voltage (typically 5VDC or 24VDC) and signal output.
4. For thermistors: check resistance vs. temperature chart.

---

### System Fault: Low Motor Current

**Fault code:** Code 35 — `LOW MOTOR CURRENT`

**Trigger:** Motor current is significantly below expected value for operating conditions. Indicates the compressor is not loaded as expected.

**Causes:**
- Compressor running but not pumping refrigerant (lost suction)
- Broken belt or coupling failure (belt-drive units)
- Capacity control solenoid stuck open (compressor unloaded when should be loaded)

---

## Guide Vane and Capacity Control Faults (YT Centrifugal)

### Guide Vane Fault

**Trigger:** OptiView has detected the guide vane position is not matching the commanded position.

**Causes:**
- Guide vane actuator motor failure
- Guide vane position sensor failure
- Guide vane mechanical binding
- Actuator coupling or linkage broken

**Diagnosis:**
1. Navigate to **OptiView → Service → Manual Operation → Guide Vane**.
2. Command the guide vane to 100% and observe actual position feedback.
3. If guide vane does not respond, check actuator motor power and position sensor wiring.
4. Verify guide vane moves freely by manually rotating shaft (compressor off, vented).

---

### Isolation Valve Failed to Close/Open

**Fault codes:** Code 53/54 — `ISOLATION VALVE FAILED TO CLOSE` / `ISOLATION VALVE FAILED TO OPEN`

**Trigger:** Compressor isolation valve end switch has not confirmed the commanded position within the required time.

**Causes:**
- Actuator failure
- End switch wiring fault
- Valve mechanically stuck

---

## Reset Procedures

### Fault Reset (General)

1. Navigate to **Main Menu → Reset** or press the dedicated **RESET** button on the OptiView panel.
2. For Safety Cutouts (hardware), the fault condition must have cleared and the trip setpoint not exceeded before reset will be accepted.
3. If reset is refused: the fault condition is still active. Check current operating parameters — they are visible on the main screen.

### Accessing Unit History Before Reset

York technicians should **always** review fault history before clearing a latching alarm. The OptiView stores data at fault time — once the system is running again, the fault timestamp and operating data remain in history, but confirming conditions before reset helps root-cause analysis.

### Clearing VSD Faults

VSD faults may require additional steps:
1. Resolve the fault condition.
2. Reset at OptiView.
3. If VSD fault persists: power cycle the VSD by cycling the unit disconnect (with appropriate safety steps) and allow DC bus to fully discharge before re-energizing.

---

## Replacement Parts

| Part | Application | Notes |
|---|---|---|
| **Discharge pressure transducer** | YVAA, YVFA, YWHA | Verify signal type (0–5V, 4–20mA) and range |
| **Suction pressure transducer** | YVAA, YVFA, YWHA | Match exact replacement to original |
| **Leaving chilled water temp sensor** | All models | 10K NTC thermistor; verify curve vs. OptiView config |
| **Entering/leaving condenser temp sensors** | All models | Immersion or strap-on depending on application |
| **Oil pressure transducer** | YVAA, YVFA screw | Differential type; check thread size and range |
| **OptiView Control Board** | All models | Requires full re-commissioning by JCI service |
| **VSD IGBT module** | YVFA | Match to VSD frame size — not interchangeable between frames |
| **VSD cooling pump** | YVFA glycol-cooled VSD | Replace if flow rate is insufficient |
| **EXV motor/valve assembly** | YVAA, YVFA | Test motor winding resistance before replacing valve |
| **Condenser fan motor** | YVAA, YVFA | Verify HP, RPM, rotation direction matches |
| **High-pressure cutout switch** | YVAA, YVFA, YWHA | Check factory-set trip pressure matches unit design |
| **Oil filter element** | All screw-compressor models | Annual replacement minimum |

---

## Common York OptiView Setup Errors

**VSD not configured for connected motor:** The OptiView must have motor FLA and voltage programmed correctly for current limit protection to function. After motor or VSD replacement, verify all motor parameters match nameplate.

**Incorrect refrigerant circuit count:** YVAA comes in single and dual-circuit versions. Circuit count must be configured correctly or alarms trip on non-existent circuits.

**Flow switch not commissioned:** Chilled water flow switch must be tested during commissioning. An uncalibrated or bypassed flow switch is the most common cause of low-flow damage on York chillers.

**Setpoint winter/summer conflicts:** Discharge pressure limiting setpoints designed for summer operation may not match winter ambient temperatures — the unit will keep trying to limit capacity before the circuit is fully stable. Review seasonal setpoints annually.

**Service mode left active:** After maintenance, confirm no actuators or setpoints are left in manual/override mode. OptiView will indicate service mode on the main screen, but technicians sometimes overlook this when handing the unit back.

## Where to Buy Replacement Parts

Find replacement parts for York chillers on Amazon:

- [York Chiller Parts & Controls](https://www.amazon.com/s?ascsubtag=ecf-york-chiller-fault-codes&k=York+chiller+parts&tag=errorcodefixes-20)
- [York HVAC Pressure Transducer & Sensor](https://www.amazon.com/s?ascsubtag=ecf-york-chiller-fault-codes&k=York+HVAC+pressure+transducer+sensor&tag=errorcodefixes-20)
- [York OptiView Control Panel Components](https://www.amazon.com/s?ascsubtag=ecf-york-chiller-fault-codes&k=York+chiller+control+panel+parts&tag=errorcodefixes-20)

## See Also

- [York TG9 Furnace Error Codes — Fault Code Diagnostic Guide](/posts/york-tg9-furnace-error-codes/)
- [York 2 Flashes Error Code — Causes & Fix](/posts/york-2-flashes-error-code/)
- [York 2-Blink Error Code — Pressure Switch Stuck Open Fix](/posts/york-error-code-2/)
- [York Furnace Error Code E5 — High Limit Tripped](/posts/york-furnace-error-code-e5/)
