---
title: "Trane Chiller Fault Codes — Complete Troubleshooting Guide"
description: "Trane chiller fault codes for CGAM, CVHE, RTHD, and Tracer CH530 series. What each alarm means and how to fix it."
pubDatetime: 2026-04-28T00:00:00Z
modDatetime: 2026-04-28T00:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - chiller
  - trane
---

Trane chillers — whether you're running a CGAM air-cooled screw, a CVHE centrifugal, or an RTHD helical-rotary — share a common control backbone: the **Tracer CH530 controller**. When the CH530 logs an alarm, it displays a short text string and assigns the fault to a severity tier. This guide covers the most common alarm codes, what triggers each one, and how to diagnose and reset.

## Jump to Section

- [Tracer CH530 Overview](#tracer-ch530-overview)
- [Alarm Severity Tiers](#alarm-severity-tiers)
- [Navigating CH530 Alarm History](#navigating-ch530-alarm-history)
- [Compressor Faults](#compressor-faults)
- [High Pressure Faults](#high-pressure-faults)
- [Low Pressure Faults](#low-pressure-faults)
- [Motor and Electrical Faults](#motor-and-electrical-faults)
- [Oil System Faults](#oil-system-faults)
- [Evaporator and Freeze Faults](#evaporator-and-freeze-faults)
- [Communication Faults](#communication-faults)
- [Reset Procedures](#reset-procedures)
- [Replacement Parts](#replacement-parts)

---

## Tracer CH530 Overview

The Tracer CH530 is Trane's microprocessor controller used across the CGAM (air-cooled screw), CVHE/CVHG (centrifugal), RTHD (helical-rotary), RTAC, and RTWD chiller families. It provides:

- Touch-screen Human Interface (HI) at the unit
- Remote connectivity via Tracer TU service tool
- Real-time alarm logging with time/date stamps
- Event log with operating conditions at time of fault

The CH530 distinguishes between **active alarms** (currently tripped) and **historic alarms** (logged past events). Both are accessible from the front panel.

---

## Alarm Severity Tiers

| Severity | Behavior | Example |
|---|---|---|
| **Immediate Shutdown** | Compressor stops immediately | High discharge pressure trip |
| **Normal Shutdown** | Chiller unloads before stopping | Low leaving water temp |
| **Warning** | No shutdown — operator notified | High oil temperature warning |
| **Diagnostic** | Informational log entry | MP reset has occurred |

Latching alarms require manual reset after the condition clears. Non-latching alarms auto-clear once the fault condition resolves.

---

## Navigating CH530 Alarm History

### From the Human Interface

1. From the main screen, press **Alarms** (bell icon or text button depending on HI version).
2. Select **Active Alarms** for current faults or **Alarm History** for past events.
3. Tap any alarm entry to expand it — the CH530 displays the alarm text, timestamp, and operating data at time of fault (suction pressure, discharge pressure, water temperatures, current draw).
4. To clear an active alarm: resolve the condition, then press **Reset** on the alarm detail screen.

### From Tracer TU (Laptop Service Tool)

1. Connect Tracer TU to the CH530 service port via USB or Ethernet.
2. Navigate to **Chiller → Reports → Alarm Log**.
3. Export the log as CSV for detailed analysis.
4. Use **Override Mode** to energize specific contactors for diagnostic testing (requires appropriate access level).

### Alarm History Tip

The CH530 stores the last 200 alarm events. Before clearing any alarm, document the fault conditions displayed in the log — discharge temperature, pressures, and current at the moment of fault are critical for root-cause analysis.

---

## Compressor Faults

### MP: Reset Has Occurred

**Trigger:** The Main Processor (MP) on the CH530 has rebooted unexpectedly.

**Causes:**
- Transient power sag or spike at the control panel
- Low 24V control power supply voltage
- Loose wiring on the CH530 power input terminals
- Failing CH530 control board

**Diagnosis:**
1. Check control transformer output — should be 24V ±10%.
2. Inspect terminal connections at J1/J2 on the CH530 board.
3. Review alarm history: if resets correlate with compressor starts, suspect voltage dip from motor inrush.
4. Check for other simultaneous alarms that may indicate the root cause.

**Reset:** Non-latching — clears automatically. If recurring, address power quality before the CH530 board fails.

---

### Starter Fault Type I

**CH530 Text:** `STARTER FAULT TYPE I`

**Trigger:** During Y-Delta or solid-state starter startup, current was detected on current transformers (CTs) when only the 1M contactor should be closed.

**Applies to:** CVHE, CVHF, CVHG, CDHF, CDHG, RTAC, RTHD

**Causes:**
- One of the auxiliary contactors (2M or 3M) is mechanically stuck closed or has welded contacts
- Wiring error at starter — phases crossed
- CT wiring error — CTs on wrong phases

**Diagnosis:**
1. De-energize the unit and verify all contactors open freely.
2. Using a meter, check for continuity across all contactor poles when de-energized.
3. Verify CT leads are routed through the correct phase conductors.
4. Inspect contactor coils and auxiliary contacts for damage.

**Reset:** Latching. Must resolve mechanical issue before reset.

---

### Compressor Limit — Pulldown

**CH530 Text:** `COMPRESSOR LIMIT`

**Trigger:** Compressor current has reached the programmed current limit (RLA-based), and the unit is shedding load to protect the motor.

**Causes:**
- High ambient temperature driving high head pressure
- Chilled water load exceeding unit capacity
- Low refrigerant charge causing compressor to work harder
- Incorrect current limit setpoint

**Diagnosis:**
1. Check ambient conditions vs. unit operating range.
2. Compare compressor current to nameplate RLA.
3. Review refrigerant charge — suction superheat and subcooling.
4. Verify current limit setpoint in CH530 configuration menu.

**Reset:** Warning only — no shutdown. Unit auto-recovers when load reduces.

---

## High Pressure Faults

### High Discharge Pressure — Warning

**CH530 Text:** `HIGH DISCH PRESSURE WARNING`

**Trigger:** Discharge (head) pressure has exceeded the warning threshold, typically 90–95% of the high pressure cutout (HPCO) setpoint.

**Causes (CGAM air-cooled):**
- Dirty or blocked condenser coils
- Condenser fan motor failure or reverse rotation
- High ambient temperature (above unit rating)
- Non-condensable gases (air/nitrogen) in refrigerant circuit
- Refrigerant overcharge

**Causes (CVHE/CVHG water-cooled):**
- Reduced condenser water flow — check pump, strainer, valve position
- High condenser water entering temperature
- Tube fouling or scaling in condenser

**Diagnosis:**
1. For air-cooled: inspect coils for debris, verify fan motor rotation and speed.
2. Check subcooling — high subcooling with high head pressure indicates overcharge or non-condensables.
3. For water-cooled: measure condenser water flow and entering/leaving temperatures.
4. Compare discharge pressure to saturation temperature chart for refrigerant used.

**Reset:** Warning — auto-clears when pressure drops. If it progresses to HPCO trip, see below.

---

### High Discharge Pressure — Cutout (HPCO)

**CH530 Text:** `HIGH DISCH PRESSURE CUTOUT`

**Trigger:** Discharge pressure has reached the high-pressure cutout threshold — immediate compressor shutdown.

**Reset:** Latching. Resolve pressure condition before reset. On units with a manual HPCO switch (separate from CH530 logic), reset the mechanical switch first, then reset at the CH530.

**Parts to check:** High-pressure transducer (clamp-style or thread-in), HPCO pressure switch on CGAM units.

---

## Low Pressure Faults

### Low Evaporator Pressure — Warning

**CH530 Text:** `LOW EVAP PRESSURE WARNING`

**Trigger:** Evaporator (suction) pressure has dropped below the warning setpoint.

**Causes:**
- Low refrigerant charge
- Partially closed liquid line service valve
- Plugged filter-drier — check for frost on inlet
- EXV (electronic expansion valve) not opening properly
- Low chilled water flow through evaporator

**Diagnosis:**
1. Check suction pressure against saturation temperature chart — compare to leaving evaporator water temperature.
2. Inspect filter-drier for pressure drop across inlet/outlet.
3. Check EXV position feedback in CH530 service menus.
4. Verify chilled water pump is running and flow switch is satisfied.

---

### Low Evaporator Pressure — Cutout

**CH530 Text:** `LOW EVAP PRESSURE CUTOUT`

**Trigger:** Suction pressure has dropped to cutout threshold — compressor shuts down to prevent overheating and slugging.

**Reset:** Latching. On RTHD units, also check that the low-pressure switch (mechanical) has reset.

---

### Low Suction Superheat

**CH530 Text:** `LOW SUCTION SUPERHEAT`

**Trigger:** Suction superheat (suction temperature minus evaporator saturation temperature) is too low — liquid refrigerant is reaching the compressor.

**Causes:**
- EXV stuck open or hunting
- Refrigerant overcharge
- Low load with EXV not closing down
- EXV motor winding failure (resistance out of spec)

**Diagnosis:**
1. Check EXV motor winding resistance — typically 75–100 Ω per phase depending on model.
2. Review EXV control history in Tracer TU — look for hunting or full-open condition.
3. Verify suction temperature sensors are accurate — compare to calibrated thermometer.

---

## Motor and Electrical Faults

### Motor Overload

**CH530 Text:** `MOTOR OVERLOAD`

**Trigger:** Compressor motor current has exceeded the thermal overload threshold for a sustained period, or the overload relay has tripped.

**Causes:**
- Mechanical overload — compressor binding
- High discharge pressure forcing motor to work harder
- Voltage imbalance across motor phases (>2% imbalance causes significant heating)
- Worn or undersized overload relay
- Single-phasing at motor terminals

**Diagnosis:**
1. Check three-phase voltage at motor terminals — measure all three phases under load.
2. Calculate voltage imbalance: (Max deviation from average ÷ Average) × 100.
3. Check current on all three phases — unbalanced current indicates winding or supply issue.
4. Inspect overload relay contacts and trip setting vs. motor FLA.

**Reset:** Latching. Allow motor to cool 10–15 minutes before reset.

---

### Supply Voltage Fault

**CH530 Text:** `SUPPLY VOLTAGE FAULT`

**Trigger:** Line voltage at the unit is outside the acceptable operating range (typically ±10% of nameplate voltage).

**Causes:**
- Low utility voltage during peak demand periods
- Voltage drop due to undersized supply conductors
- Transformer tap set incorrectly
- High-resistance connection in main disconnect or panel

**Diagnosis:**
1. Measure line voltage at main disconnect under load.
2. Compare to rated voltage ±10% tolerance.
3. Check for voltage sag during compressor start — inrush can temporarily drop voltage.

---

## Oil System Faults

### Low Oil Pressure

**CH530 Text:** `LOW OIL PRESSURE`

**Trigger:** Oil pressure differential (oil supply minus refrigerant pressure) has dropped below the minimum required for adequate bearing lubrication.

**Applies to:** CGAM, RTHD, CVHE (gear-drive centrifugals use oil pump differently)

**Causes:**
- Oil pump failure
- Low oil level in oil separator or sump
- Oil filter plugged
- Oil pressure transducer failure
- Refrigerant migration into oil — high oil dilution after off-cycle

**Diagnosis:**
1. Check oil level at sight glass (unit must be running or recently stopped).
2. Measure differential oil pressure using CH530 service display — compare pump-on vs. off.
3. Check oil filter pressure drop (filter element typically requires replacement at 15–20 psid).
4. If unit was off for extended period, check for refrigerant migration — oil may be foamy at startup.

**Maintenance:** Change oil filter per Trane PM schedule (typically annually or 2000 hours).

---

### High Oil Temperature

**CH530 Text:** `HIGH OIL TEMPERATURE WARNING`

**Trigger:** Oil temperature has exceeded the warning threshold, typically around 160°F (71°C).

**Causes:**
- Inadequate oil cooling (oil cooler fouled or refrigerant-side low)
- High discharge temperature transferring heat to oil
- Overloaded compressor

---

## Evaporator and Freeze Faults

### Evaporator Freeze Protection

**CH530 Text:** `EVAP FREEZE PROTECTION`

**Trigger:** Leaving chilled water temperature has dropped below the freeze protection setpoint (default 36°F / 2.2°C), or the evaporator refrigerant temperature has dropped near freezing.

**Causes:**
- Chilled water flow loss — pump failure, closed valve, stuck bypass
- Load suddenly dropped to near zero with chiller still running
- Leaving water temperature setpoint set too low
- Flow switch fault — unit running without flow

**Diagnosis:**
1. Verify chilled water flow — check pump status and differential pressure.
2. Confirm flow switch is operating correctly — test continuity with flow and without.
3. Check leaving water temperature sensor accuracy vs. handheld.
4. Verify freeze protection setpoint in CH530 — should be ≥ 36°F for water systems, lower for glycol.

**Reset:** Latching. Do not restart until flow is confirmed.

---

### Low Leaving Chilled Water Temperature

**CH530 Text:** `LOW LEAVING CW TEMP`

**Trigger:** Leaving chilled water temperature has reached the low leaving water temperature (LLWT) cutout — a normal shutdown protecting the load.

**Causes:**
- Load is satisfied — normal cycling
- Chiller oversized for current load
- Setpoint too high relative to supply temperature

---

## Communication Faults

### Degraded Comm: Did Not Receive Chiller Packet

**CH530 Text:** `DEGRADED COMM`

**Trigger:** Communication between the CH530 Main Processor and one of the module processors (compressor module, refrigerant module) has been interrupted.

**Causes:**
- Loose ribbon cable or communication wire between CH530 boards
- Failed module processor board
- Electromagnetic interference affecting the communication bus
- Failed CH530 main processor

**Diagnosis:**
1. Inspect all internal wiring harnesses for looseness — vibration can work connections loose over time.
2. Check for shield continuity on communication cables.
3. Review which module is not responding — the alarm text usually identifies the source (e.g., "CKT 1" or "RefrigerantModule").
4. Swap module processors if available to isolate fault.

---

### Improper HI Configuration

**CH530 Text:** `IMPROPER HI CONFIGURATION`

**Trigger:** The Human Interface (HI) touchscreen panel is not configured correctly for the connected chiller model.

**Causes:**
- Wrong software version loaded on HI
- HI replaced with incorrect model for chiller type
- Configuration parameters corrupted

**Fix:** Use Tracer TU to verify and correct chiller configuration parameters. Match HI firmware version to CH530 controller version.

---

## Reset Procedures

### Standard Alarm Reset

1. Navigate to **Alarms → Active Alarms** on the CH530 HI.
2. Verify the fault condition has cleared (pressure, temperature, current back in range).
3. Select the alarm and press **Reset**.
4. If the alarm re-trips immediately, the condition has not been resolved.

### Unit Restart After Immediate Shutdown

1. Resolve the fault condition.
2. Reset any mechanical safeties (HPCO switch, overload relay) if applicable.
3. Reset at the CH530 HI.
4. Allow the unit to complete its pre-start checks before compressor starts.

### Factory Default Configuration Caution

Do not perform a factory reset of CH530 parameters without first documenting all setpoints and configuration values with Tracer TU. A factory reset will wipe site-specific settings including setpoints, limits, and options.

---

## Replacement Parts

| Part | Application | Notes |
|---|---|---|
| **Discharge pressure transducer** | CGAM, RTHD, CVHE | Trane OEM or equivalent Honeywell/Sensata 0–500 psi |
| **Suction pressure transducer** | CGAM, RTHD | 0–250 psi range, verify connector type |
| **Leaving water temperature sensor** | All models | 10K thermistor, confirm curve vs. CH530 config |
| **Entering/leaving CW sensor** | All models | Immersion or strap-on, 10K NTC |
| **Oil pressure transducer** | CGAM, RTHD | Differential or gauge type depending on model |
| **EXV motor assembly** | All refrigerant circuits | Test winding resistance before replacement |
| **CH530 Main Processor board** | All models | Requires re-configuration with Tracer TU |
| **CH530 Human Interface (HI)** | All models | Match part number to chiller model and firmware rev |
| **Contactor (1M, 2M, 3M)** | CVHE, RTHD starters | Match frame size and coil voltage |
| **Oil filter element** | CGAM, RTHD | Annual replacement recommended |

---

## Common Tracer CH530 Setup Errors

**Wrong chiller type configured:** The CH530 supports multiple chiller families — if the configuration doesn't match the physical unit, alarms will trip at wrong thresholds or features will be unavailable. Always verify with Tracer TU.

**Incorrect refrigerant circuit count:** CVHE and RTHD can be single or dual circuit. Misconfiguring circuit count causes communication errors and false alarms.

**Flow switch not commissioned:** Many sites bypass flow switches for commissioning and never restore them. A missing flow switch input causes CH530 to fault on low-flow conditions or fail to protect against freeze-up.

**Time/date not set:** CH530 alarm logs are useless without accurate timestamps. Set time/date at initial commissioning and after any battery-backed memory loss.

**Setpoint conflicts:** Leaving water temperature setpoint below freeze protection setpoint will cause the chiller to hunt. Verify all temperature setpoints are logically ordered (freeze protection < LLWT cutout < setpoint < HLWT cutout).

## Where to Buy Replacement Parts

Find replacement parts for Trane chillers on Amazon:

- [Trane Chiller Parts & Controls](https://www.amazon.com/s?ascsubtag=ecf-trane-chiller-fault-codes&k=Trane+chiller+parts&tag=errorcodefixes-20)
- [Trane HVAC Temperature Sensor Replacement](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-trane-chiller-fault-codes&tag=errorcodefixes-20)
- [Trane Chiller Control Board Replacement](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-trane-chiller-fault-codes&tag=errorcodefixes-20)