---
title: "Graco Pump Fault Codes — Complete Troubleshooting Guide"
description: "Graco pump fault codes for Merkur, President, Husky, and SaniForce series. What each fault means and how to fix it."
pubDatetime: 2026-04-27T23:00:00Z
modDatetime: 2026-04-27T23:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - pump
  - graco
---

Graco uses two very different fault systems across its pump line. Air-operated pumps like the Merkur, President, Husky, and SaniForce usually do not show numeric fault codes on the pump itself. They fail by symptom: runaway, low output, icing, leaking checks, or stall. Electric E-Flo systems do show real electronic fault codes through the display, the control module, and the motor power LED blink sequence.

This guide covers both sides of that split so you can troubleshoot the actual Graco hardware in front of you.

## Which Graco Pumps Actually Show Fault Codes?

| Pump family | Typical fault display | What you usually see |
|---|---|---|
| Merkur airless / finishing pumps | Usually no onboard numeric code unless DataTrak is fitted | Runaway trip, low output, worn packings, stalled air motor |
| President pumps | Usually symptom-based, sometimes DataTrak alarms | Runaway, low pressure, check valve wear, stall |
| Husky diaphragm pumps | Symptom-based | Stall, no prime, cavitation, air valve sticking |
| SaniForce sanitary diaphragm / piston pumps | Symptom-based | No prime, check ball wear, leaking diaphragm, low output |
| E-Flo DC / E-Flo SP / E-Flo iQ | Electronic event codes and motor LED blink codes | Overcurrent, pressure, flow, encoder, temperature, voltage, communication |

If you are working on a Graco pump with an **ADM**, **ADCM**, **E-Flo control module**, or **motor power LED**, use the electronic codes first. If you are working on a plain air-operated pump, use the mechanical symptom table first.

## How to Read Graco E-Flo Faults

### On E-Flo DC motors
The power indicator LED on the motor blinks a repeating sequence. Example: **1-2** means one blink, pause, then two blinks, then repeat.

### On E-Flo SP and E-Flo iQ systems
The display logs alphanumeric codes such as:
- **P1C_** low pressure
- **P3C_** high pressure
- **T4M_** high motor temperature
- **CBD_** communication error
- **DB1_** pump not primed

### Alarm reset
1. Fix the cause first.
2. Press the **Reset / Cancel** key on the control module or ADM.
3. If the code returns immediately, do not keep resetting. The system is still seeing the fault.

### Alarm history access
On ADCM-based E-Flo systems:
1. Scroll to the run screens that show the alarm log.
2. Graco stores the **last 20 alarms** with date and time.
3. Record the code before clearing it.

---

## Graco E-Flo DC Motor and Control Codes

The most useful E-Flo DC codes come from Graco's control module tables and motor blink codes.

### K4D_ / K3D_ — Pump Runaway or High Speed

**Blink code:** K4D_ commonly maps to the maximum speed alarm function on the E-Flo DC control family.

**Meaning:** Flow or cycle rate exceeded the maximum target. On real equipment, this often means the pump ran away because the fluid side lost resistance.

**Most common causes:**
1. Empty supply drum or tote
2. Burst hose or major fluid leak downstream
3. Prime / flush valve left open
4. Check valve not seating
5. Flow limit set too low in the active profile

**Diagnosis steps:**
1. Check fluid supply first.
2. Inspect the outlet hose and gun for rupture or open path.
3. Check whether the system is still in prime or flush mode.
4. On E-Flo systems with profile control, verify the maximum flow setting in Setup Screen 3 and the alarm action in Setup Screen 4.

**Fix:**
Refill the fluid supply, close bypass paths, repair leaks, then reset the alarm.

---

### P1I_ / P2I_ — Low Pressure

**Blink code:** 1-3 for alarm on many E-Flo DC advanced setups.

**Meaning:** Outlet pressure fell below the minimum setpoint. If the profile is configured for alarm, the pump shuts down.

**Most common causes:**
1. Supply container empty
2. Pump not primed
3. Intake check held open by debris
4. Worn packings or piston seal leakage
5. Pressure transducer installed but reading wrong

**Diagnosis steps:**
1. Confirm there is fluid in the supply container.
2. Prime the pump at low speed.
3. Watch pressure on the transducer reading screen if transducer 1 is installed.
4. If the motor runs but pressure never builds, inspect lower packings and check valves.

**Fix:**
Prime the pump, repair intake checks, replace worn lower packings, or replace the outlet pressure transducer if the mechanical pressure is normal but the display reads low.

---

### P4I_ / P3I_ — High Pressure

**Blink code:** 1-4 for alarm on many E-Flo DC advanced setups.

**Meaning:** Outlet pressure exceeded the maximum target or maximum alarm setpoint.

**Most common causes:**
1. Downstream filter or hose plugged
2. Gun, dispense valve, or applicator blocked
3. Pressure setpoint too high
4. Back pressure regulator closed too far
5. Fluid too viscous for the line size and temperature

**Diagnosis steps:**
1. Relieve pressure safely before disconnecting anything.
2. Check downstream filters first.
3. Compare transducer pressure to a mechanical gauge if you suspect sensor drift.
4. Inspect the BPR setting if the system uses one.

**Fix:**
Clear the restriction, lower the pressure target, and restart at a low cycle rate.

---

### A4N_ — Overcurrent / Motor Fault

**Blink code:** 6 on many E-Flo DC motors.

**Meaning:** Motor current exceeded the allowed value. Graco lists this as current above 13A or a hardware overcurrent trip at 20A.

**Most common causes:**
1. Pump lower mechanically tight from dried material
2. Pressure target set too high for the selected lower size
3. Gearbox drag or damaged motor bearings
4. Wiring issue causing high current draw
5. Product too cold or too heavy for the setup

**Diagnosis steps:**
1. Relieve fluid pressure and try jogging the pump slowly.
2. Decouple the lower from the motor if needed. If the motor now runs clean, the lower is the problem.
3. Inspect the displacement rod for dried coating buildup.
4. Check whether the correct lower size was configured in Setup Screen 5.

**Fix:**
Clean or rebuild the lower, correct the profile settings, and inspect the motor or gearbox if current remains high with the lower disconnected.

---

### T2D_ — Motor Temperature Sensor Fault or Low Temperature

**Blink code:** 3-5 on E-Flo DC.

**Meaning:** The internal thermistor is disconnected, damaged, or reading below the valid range.

**Most common causes:**
1. Motor temperature sensor wiring fault
2. Failed thermistor
3. Connector loose after maintenance

**Diagnosis steps:**
1. Inspect the motor sensor connector first.
2. Check for pin damage or moisture entry.
3. If wiring is intact and the fault stays active, replace the temperature sensor assembly or motor electronics as specified by Graco.

---

### T3D_ / T4D_ / T4M_ — High Motor Temperature

**Meaning:** The motor reached temperature cutback or full overtemperature shutdown.

**Most common causes:**
1. Motor cooling blocked by dust, coating overspray, or enclosure heat
2. Continuous operation at high load
3. Lower friction too high
4. Ambient temperature too high

**Diagnosis steps:**
1. Check motor cooling air path.
2. Check current draw and cycle rate.
3. If temperature climbs fast with low fluid pressure, suspect motor cooling or sensor issues.
4. If temperature climbs with high current, suspect mechanical drag in the lower.

**Fix:**
Clear airflow, reduce load, and repair the lower if it drags.

---

### V1I_ / V1M_ — Low Voltage or AC Power Loss

**Blink code:** 2 or 2-6 depending on the exact event.

**Meaning:** Input power dropped below the drive's acceptable range or AC power disappeared.

**Most common causes:**
1. Weak plant supply voltage
2. Loose disconnect or terminal lug
3. Undersized circuit feeding the pump
4. Broken disconnect switch

**Diagnosis steps:**
1. Measure supply voltage at the disconnect and at the motor input terminals.
2. Inspect fuses, breaker, and disconnect switch.
3. Check whether the event happens only during start, which points to voltage drop under load.

**Fix:**
Restore stable supply voltage and tighten power connections.

---

### V4I_ / V4M_ — High Voltage

**Blink code:** 3 on some E-Flo DC event maps.

**Meaning:** Input voltage exceeded the allowed range.

**Most common causes:**
1. Wrong supply voltage connected to the motor
2. Faulty transformer or plant power issue
3. Wiring error after electrical work

**Fix:**
Confirm the motor nameplate voltage and correct the incoming supply before restart.

---

### CCN_ / CAC_ / CBD_ — Communication Error

**Meaning:** The display, control board, or motor lost CAN or board-to-board communication.

**Most common causes:**
1. Loose CAN cable
2. Display or motor board powered down
3. Damaged communication cable
4. Duplicate module or addressing issue in multi-pump setups

**Diagnosis steps:**
1. Check cable seating at the display and motor.
2. Check indicator LEDs on the motor control board.
3. In multi-pump setups, isolate to one pump if needed and bring modules back online one at a time.

**Fix:**
Repair the network first. Many "pump fault" calls on E-Flo SP and E-Flo iQ systems are really communication faults.

---

### WSC_ — Zero Setting on Active Profile

**Meaning:** The active profile is configured with 0 pressure or 0 flow, so the motor refuses to run.

**Most common causes:**
1. Profile never finished during setup
2. Wrong profile selected after power cycle
3. Operator cleared a target value by mistake

**Fix:**
Open the active profile, enter valid target values, activate the profile, then restart.

---

### WSD_ — Invalid Lower Size

**Meaning:** The motor was operated before the lower size was set up in the software.

**Fix:**
Go to **Setup Screen 5**, select the installed lower size, save it, then restart. Graco specifically throws this fault when the motor sees no valid lower configuration.

---

### WBD_ / WSC_ / Encoder Faults

**Meaning:** The motor cannot trust the encoder or stroke calibration.

**Most common causes:**
1. Encoder failed
2. Position sensor loose
3. Stroke calibration interrupted
4. Mechanical binding stopped normal motion during calibration

**Fix:**
Inspect the encoder and position sensor, then rerun calibration. If calibration fails again, replace the encoder kit or position sensor kit.

> **Common parts:** Graco encoder replacement kit **24U938**, position sensor kit **24W920**.

---

## E-Flo SP and E-Flo iQ System Codes You Will Actually See in the Field

Current E-Flo SP and E-Flo iQ systems use Graco Help codes such as these:

| Code | Meaning | First thing to check |
|---|---|---|
| DB1_ / DB2_ | Pump not primed | Fluid supply, intake checks, prime mode |
| DD3_ / DD4_ | Pump diving | Air entrainment, empty supply, unstable inlet |
| P1C_ / P2C_ | Low pressure | Empty supply, worn packings, leak |
| P3C_ / P4C_ | High pressure | Plugged line, blocked gun, closed valve |
| P6D_ | Outlet pressure sensor fault | Transducer wiring or failed sensor |
| MG2_ | Low filter pressure | Restriction upstream or filter issue |
| MG3_ | High filter pressure | Plugged filter |
| T2J_ / T2D_ | Motor temp sensor fault | Sensor or harness |
| T4M_ | High motor temperature | Cooling, load, mechanical drag |
| V1M_ | Low voltage | Supply voltage or disconnect |
| V4M_ | High voltage | Wrong incoming supply |
| CBD_ / CAC_ | Communication error | CAN cable, power to driver |
| WMC_ | Control board fault | Board replacement may be required |
| WMN_ | Software mismatch | Display and motor software versions |
| WSU0 | USB configuration error | Bad update or wrong configuration file |

These codes show up on the ADM and in the event log. Graco's online help lets you search the exact code if you need the factory decision tree.

---

## Mechanical Faults on Merkur and President Pumps

Merkur and President pumps often fail by symptom, not by display code.

### Runaway / overspeed

**Meaning:** The pump cycles much faster than normal because fluid resistance disappeared.

**Most common causes:**
1. Fluid supply empty
2. Intake ball check not sealing
3. Piston valve worn
4. Leak in hose, gun, or fittings

**Fix:**
Refill and reprime. If speed still runs away, inspect the intake valve and piston packings.

### Pump stalls under pressure

**Most common causes:**
1. Air supply too low on air-operated models
2. Fluid dried on displacement rod
3. Air motor spool or pilot valve dirty
4. Outlet line plugged

**Fix:**
Check air supply, clean the air motor, and inspect the displacement rod and outlet path.

### Low output on both strokes

**Most common causes:**
1. Restricted air or fluid supply
2. Worn piston packings
3. Fluid too heavy to prime
4. Obstructed hose or gun

**Fix:**
Clear restrictions, increase supply pressure within rating, and rebuild the lower if packings are worn.

### Low output on one stroke only

**Most common causes:**
1. Intake ball check worn or held open
2. Piston valve worn or held open

**Fix:**
Disassemble the lower and service the check valves.

---

## Husky Diaphragm Pump Faults

Husky pumps usually show operating symptoms rather than numeric codes.

### Pump will not prime
**Most common causes:**
- Suction lift too high
- Check balls stuck
- Diaphragm damaged
- Air valve not shifting

### Pump stalls
**Most common causes:**
- Sticky air valve spool
- Ice in the exhaust from wet compressed air
- Check ball jammed with debris

### Low flow or pulsing flow
**Most common causes:**
- Worn diaphragms
- Check balls or seats worn
- Inlet strainer blocked
- Suction hose collapsed

**Fix path:**
Start with clean dry air, then inspect check balls, seats, and diaphragms.

---

## SaniForce Pump Faults

SaniForce pumps fail from sanitation-related wear more often than from electronics.

### No prime or weak prime
**Most common causes:**
1. Check balls not seating because of product buildup
2. Worn seats or diaphragms
3. Air leak on the suction side
4. Product viscosity too high for the selected inlet conditions

### Low output
**Most common causes:**
1. Outlet restriction
2. Worn diaphragms or piston seals
3. Check ball wear
4. Product too cold and too thick

### Stall or erratic cycling
**Most common causes:**
1. Air valve sticking
2. Sanitary clamps loose and pulling air
3. Exhaust muffler restricted

**Fix:**
Inspect all sanitary clamps, diaphragms, and check assemblies during cleaning cycles. Product residue often causes the fault.

---

## Parts Reference Table

| Part | Application | Notes |
|---|---|---|
| Throat seal liquid and wet cup parts | Merkur / President piston pumps | Keep wet cup filled to protect packings |
| Lower packing kit | Merkur / President / E-Flo piston lowers | Use when output drops or rod leaks |
| Intake and piston check kits | Merkur / President | Worn checks cause runaway and low output |
| Diaphragm kit | Husky / SaniForce diaphragm pumps | Replace in matched pairs |
| Check ball and seat kit | Husky / SaniForce | Use when priming gets weak or flow pulses |
| Pressure transducer kit 24R050 / 24Y245 | E-Flo DC outlet pressure feedback | For pressure-controlled systems |
| Encoder kit 24U938 | E-Flo DC motors | Corrects encoder hardware faults |
| Position sensor kit 24W920 | E-Flo DC motors | Used with stroke feedback faults |
| Control board kit 24U935 | E-Flo DC advanced motors | Use after confirmed board fault |
| Valve seals, piston rods, sanitary check parts | SaniForce | Keep matched to the exact pump model and elastomer type |

---

## Quick Diagnostic Order

If you want the fastest path on a Graco pump, check in this order:

1. Is there fluid supply?
2. Is there air or electrical power?
3. Is the outlet blocked?
4. Is the pump primed?
5. Do the checks or diaphragms seal?
6. On E-Flo, what code is in the event log?
7. Does the motor LED blink a repeatable pattern?

## Quick Reference

| Symptom or code | Likely cause | First action |
|---|---|---|
| K4D_ / runaway | Empty supply or leak | Refill, inspect hose and checks |
| P1I_ low pressure | Not primed or worn lower | Prime, inspect packings |
| P4I_ high pressure | Blocked outlet | Relieve pressure, clear line |
| A4N_ overcurrent | Lower binding or overload | Decouple lower, inspect drag |
| T4M_ high motor temp | Cooling or load problem | Check airflow and current draw |
| V1M_ low voltage | Supply problem | Measure input voltage |
| CCN_ / CBD_ comms | Cable or board issue | Reseat communication cables |
| Merkur runaway | Empty drum or worn checks | Refill and inspect checks |
| Husky stall | Air valve sticking | Clean air valve, check dry air |
| SaniForce low output | Check balls or diaphragms worn | Rebuild wetted section |

If the pump has electronics, trust the code. If the pump has no electronics, trust the fluid path and the check valves first. On Graco pumps, those two rules solve most field calls.

## Where to Buy Replacement Parts

Find replacement parts for Graco pumps on Amazon:

- [Graco Pump Replacement Parts](https://www.amazon.com/s?i=industrial&k=Graco+pump+replacement+parts&tag=errorcodefixes-20)
- [Graco Husky Diaphragm Pump Repair Kit](https://www.amazon.com/s?i=industrial&k=Graco+Husky+diaphragm+pump+repair+kit&tag=errorcodefixes-20)
- [Graco Check Valve & Ball Replacement](https://www.amazon.com/s?i=industrial&k=Graco+check+valve+ball+seat+replacement&tag=errorcodefixes-20)