---
title: "Vacon VFD Fault Codes — Complete Troubleshooting Guide"
description: "Vacon VFD fault codes for Vacon 100, Vacon NXP, and Vacon 10 series. What each fault means and how to fix it."
pubDatetime: 2026-04-27T23:00:00Z
modDatetime: 2026-04-27T23:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - electrical
  - vfd
  - vacon
---

Vacon drives — now part of the Danfoss portfolio after the 2014 acquisition — use a two-layer fault system: a Fault Code (F1, F2, F3...) that tells you the category, and either a Subcode (NXP/NXS series) or Fault ID (Vacon 100 series) that tells you the exact cause. Skipping the subcode and jumping straight to "F1 Overcurrent = bad motor" is how you replace parts that don't need replacing. This guide covers both layers for Vacon 100 FLOW/INDUSTRIAL/HVAC, Vacon NXP, and Vacon 10.

## How Vacon Fault Numbering Works

| Code Type | Display Format | Example | What It Means |
|---|---|---|---|
| Fault (NXP) | F + number + Subcode S | F1 S1 | Overcurrent — hardware trip |
| Fault (Vacon 100) | F + number + ID number | F1 ID1 | Overcurrent — hardware overcurrent |
| Alarm | A + number | A16 | Motor overtemperature warning (drive still running) |
| Warning | W + number | W10 | Input phase loss warning |

**Critical rule:** A fault trips the drive and stops the motor. An alarm is a warning only — the drive keeps running but you need to act.

## Accessing Fault History

### Vacon NXP / NXS
1. Navigate to **Main Menu → M4 Fault History**
2. Press the right arrow to enter
3. Last 30 faults stored with timestamps (operating hours) and drive state at trip

**With NCDrive PC software (preferred method):**
- Connect via RS-232 service port or USB-RS232 adapter
- Open Fault History view — shows fault code, subcode, operating hours, frequency, current, and voltage at time of trip
- Datalogger can be pre-triggered to capture pre-fault signals

### Vacon 100 INDUSTRIAL
1. Navigate to **Main Menu → Diagnostics → Fault History**
2. Last 40 faults with Real-Time Clock timestamps
3. Record the **Fault ID** before resetting — the ID is the specific cause, not just the category

### Vacon 10
1. Press MENU until you reach **F -- (Fault History)**
2. Browse with UP/DOWN arrows
3. Stores last 5 faults

---

## F1 — Overcurrent

**Display:** F1 (NXP: followed by S1–S4 subcode; Vacon 100: followed by ID 1 or ID 2)

**Meaning:** Motor phase current exceeded the instantaneous trip threshold (approximately 4× rated drive current).

### NXP Subcodes:

| Subcode | Specific Cause |
|---|---|
| S1 | Hardware trip — DC bus current sensor detected instantaneous overcurrent |
| S2 | Current cutter supervision (NXS only) |
| S3 | Current limit controller supervision — current hit the software limit and drive couldn't regulate it down |
| S4 | Software-based overcurrent fault |

### Causes (in order of likelihood):
1. Short circuit in motor cable or motor winding — most common
2. Acceleration time too short — motor draws excessive current during ramp-up
3. Sudden heavy load increase (e.g., jam in pump or fan)
4. Motor incorrectly sized for the drive
5. Motor parameter identification not run (drive using wrong current model)

### Diagnosis Steps:
1. Disconnect the motor cable at the drive output terminals (U, V, W)
2. Attempt a no-load run — if F1 still appears, the fault is in the drive itself (IGBT failure)
3. If no-load run is clean: reconnect motor and check cable for phase-to-phase or phase-to-ground short with a megohmmeter (>1 MΩ at 500V DC)
4. Check motor nameplate data against drive parameter settings (nominal current, voltage, frequency, power)
5. Run motor parameter identification: navigate to **M7 → Identification Run** — run at standstill if the load can't be disconnected

### Fix:
- Clear short circuits in cable or motor
- Increase acceleration time (parameter P3.4.1.2 on Vacon 100, or application-specific accel time on NXP)
- Run motor identification after correcting motor parameters

---

## F2 — Overvoltage

**Meaning:** The DC link voltage exceeded the hardware trip threshold. For 400V input drives, this is typically 840V DC. For 500V drives: 911V DC. For 690V drives: 1,200V DC.

### NXP Subcodes:

| Subcode | Specific Cause |
|---|---|
| S1 | Hardware trip — DC link exceeded absolute maximum |
| S2 | Overvoltage control supervision — overvoltage controller was active but couldn't prevent trip |
| S3 | LCL capacitor overvoltage ripple (AFE/NXP only) |

### Causes (in order of likelihood):
1. Deceleration time too short — regenerative energy from the motor charges the DC bus
2. High supply voltage spikes from the grid
3. No braking resistor or brake chopper not enabled when running high-inertia loads
4. Overvoltage controller disabled (parameter not activated)
5. Load is generative (e.g., crane lowering, downhill conveyor)

### Diagnosis Steps:
1. Measure input voltage at the drive terminals — should be within +10% of nominal
2. Check whether F2 occurs on deceleration specifically (confirms regenerative braking cause)
3. On NXP: Check parameter P2.6.5.1 (overvoltage controller) — should be 1 or 2 for most applications
4. If braking resistor is installed: measure resistance value and compare to specifications; check wiring

### Fix:
- Increase deceleration time (P3.4.1.3 on Vacon 100, or application-specific decel time)
- Enable overvoltage controller: set to 1 (no ramp, P-type) or 2 (with ramp, PI-type) on NXP
- Install braking resistor and chopper for high-inertia loads
- For continuous regenerative loads (cranes, compressors): consider AFE (Active Front End) unit

> **Parts needed:** Braking chopper module (VBRC series, drive-specific), braking resistor (sized per application load calculation)

---

## F3 — Ground Fault (Earth Fault)

**Meaning:** The sum of the three phase currents is not zero, indicating current is flowing to ground through an insulation fault.

### Causes (in order of likelihood):
1. Insulation failure in motor cable — especially on long cable runs with moisture ingress
2. Motor winding insulation degraded — common in older motors or after thermal stress
3. dU/dt or sine wave filter malfunction (if installed between drive and motor)
4. Cable routed through conduit with damaged sections

### Diagnosis Steps:
1. Disconnect the motor and motor cable at the drive output
2. Megohmmeter test the motor cable: each phase to ground at 500V DC — should be >1 MΩ
3. Separately megohmmeter test the motor windings: each winding to frame at 500V DC
4. If both test clean: inspect the dU/dt or sine filter if one is installed

### Fix:
- Replace damaged motor cable — use VFD-rated cable with symmetrical shielding
- Rewind or replace motor if insulation resistance is below 1 MΩ
- Ensure cable shield is properly terminated at both ends (motor frame and drive PE terminal)

> **Note:** On IT (floating/ungrounded) networks, the F3 threshold may need adjustment — consult the NXP application manual for the earth fault supervision parameter.

---

## F5 — Charging Switch Fault

**Meaning:** The DC bus precharge circuit did not complete correctly. The drive sent a start command but the charging switch status feedback indicated the switch is still open.

### Causes:
- Defective precharge relay or thyristor
- Wiring fault on the charging switch feedback signal
- Damaged charging resistor (NXP larger frames use a separate resistor)
- Control board communication fault with the power board

### Diagnosis Steps:
1. Power off and wait 5 minutes for DC bus to discharge fully
2. Inspect the precharge circuit board in the power unit (typically in the rectifier section)
3. Check the feedback signal wiring between the power board and control board

### Fix:
F5 almost always requires power unit inspection or replacement. Reset the fault and restart once — if it returns immediately, do not continue cycling power. Contact your Danfoss distributor with the full fault history.

---

## F6 / F9 — Undervoltage

**Display:** F9 on NXP (Vacon 100 uses F9, ID 80)

**Meaning:** The DC link voltage dropped below the minimum operating threshold during run. For 400V drives, this is typically below 330V DC.

### NXP Subcodes:

| Subcode | Specific Cause |
|---|---|
| S1 | DC link too low during run — supply voltage dip or momentary interruption |
| S2 | No data from power unit — communication loss between power and control boards |
| S3 | Undervoltage control supervision |

### Causes (in order of likelihood):
1. Supply voltage sag or momentary interruption (most common on HVAC/pump applications)
2. Blown input fuse
3. Input contactor opened during run
4. Supply voltage too low (utility problem or transformer undersized)
5. Internal precharge fault (F5 and F9 appearing together)

### Diagnosis Steps:
1. Check input voltage with a power quality meter — look for sags during startup of large motors on the same circuit
2. Check input fuses — use a DMM to verify continuity with the drive powered down
3. If F9 appears at startup only: the precharge may not be completing before the run command

### Fix:
- Verify supply voltage is within drive specification (typically +10/-10% of nominal)
- Replace blown input fuses (use semiconductor-type fuses on larger drives)
- For frequent voltage sags: enable undervoltage restart (auto-restart parameter)
- Install line reactor on input to buffer voltage transients

---

## F7 — Motor Overtemperature (Calculated)

**Meaning:** The drive's internal thermal model has calculated that the motor has exceeded its thermal limit. This uses the measured current profile over time — it does not require a physical temperature sensor.

### Causes:
1. Motor overloaded — running at above 100% rated current for extended periods
2. Motor cooling fan not running (on externally-cooled motors)
3. Motor thermal model parameters incorrect (wrong motor data entered)
4. Duty cycle too heavy for motor thermal class

### Diagnosis Steps:
1. Check motor current on the drive display — compare to motor nameplate rated current
2. Verify motor thermal protection parameters match the nameplate (nominal current, motor thermal time constant)
3. On externally-ventilated motors: confirm the cooling fan is running at full speed

### Fix:
- Reduce motor load or increase motor/drive sizing
- Correct motor parameter data in the drive (run motor identification)
- For motors with PT100 or PTC thermistors: use the physical sensor input (F29/F56) rather than relying solely on the calculated model

> **Parameter to check:** Motor nominal current (must match nameplate exactly), motor thermal time constant

---

## F8 — System Fault

**Meaning:** F8 is a wrapper code for internal drive faults. The subcode (S1–S50 on NXP, specific IDs on Vacon 100) identifies the actual problem.

### Critical Subcodes:

| Subcode | Meaning | Action |
|---|---|---|
| S1 | ASIC phase feedback fault | Internal hardware — contact distributor |
| S4 | ASIC trip | Internal hardware — contact distributor |
| S6 | Charging switch feedback error | Check precharge circuit |
| S8 | No power to driver card | Check 24V aux supply in power unit |
| S9/S10 | Power unit communication fault | Check fiber/cable between control and power boards |
| S30 | OPTAF: STO channels different | STO wiring mismatch — check safety relay wiring |
| S31 | OPTAF: Thermistor short circuit | Thermistor input shorted; check jumper X12 if not using thermistor |
| S48 | OPTAF: Therm Trip (HW) parameter/jumper mismatch | Set parameter to match the X12 jumper position |

**For F8 S30 (most common on new installations):**
The Safe Torque Off (STO) system requires both channels to be in the same state. If STO is not being used, both SD1 and SD2 terminals must have +24V (or use the factory jumper). If one channel is active and the other isn't, F8 S30 trips.

---

## F9 — Underload (Motor Underload Protection)

**Note:** On NXP this is Fault 17 (Motor Underload). On Vacon 100 it is F17. Do not confuse with F9 Undervoltage.

**Meaning:** The motor is drawing significantly less current than expected for its speed. This protects processes where a drop in load indicates a problem (broken belt, empty pump, conveyor jam).

### Causes:
1. Pump running dry — cavitating or no fluid in the system
2. Drive belt broken on a fan or blower
3. Coupling sheared between motor and load
4. Underload protection parameters set too aggressively for the application

### Diagnosis Steps:
1. Check if the connected load is actually turning — verify mechanically
2. On pump applications: check suction strainer and verify fluid supply
3. Review underload protection parameters — the underload curve can be adjusted to reduce false trips

### Fix:
- Restore the load (fix the belt, prime the pump, etc.)
- If false trips are frequent: adjust the underload protection minimum torque threshold and delay time

> **HVAC application note:** Underload protection is extremely useful on AHU (Air Handling Unit) applications — an F17/F9 underload during normal operation almost always means a broken fan belt.

---

## F10 — Input Phase Loss

**Meaning:** One of the three supply phases is missing or significantly unbalanced.

### Causes:
1. Blown main input fuse on one phase
2. Open phase in the supply cable
3. Contactor with one welded-open contact
4. Supply transformer with a failed winding

### Diagnosis Steps:
1. Measure all three input voltages at the drive input terminals with the drive powered (use a DMM with clamps on the input terminals while power is live — use appropriate PPE)
2. Compare L1-L2, L2-L3, L1-L3 — all should be within 3% of each other
3. Check input fuses with a DMM after powering down

### Fix:
- Replace blown fuse (use semiconductor-type HRC fuses on the drive input)
- Repair or replace supply cabling if open phase found

> **Note:** Vacon drives will typically show F10 as an alarm/warning (A10) before it trips as a fault, giving you a window to investigate before the drive shuts down.

---

## F14 — Drive Overtemperature

**Meaning:** The heat sink temperature exceeded the trip threshold. For most 400V drives: >90°C (194°F). For 690V FR6 frames: >77°C (171°F).

### NXP Subcodes:

| Subcode | Specific Location |
|---|---|
| S1 | Overtemperature in unit, board, or individual output phases |
| S2 | Power board specifically |
| S3 | Liquid cooling flow (liquid-cooled NXP only) |
| S4 | ASIC board or driver boards |

### Causes (in order of likelihood):
1. Cooling fan failed or clogged with dust
2. Ambient temperature too high (above rated 40°C / 104°F without derating)
3. Switching frequency set too high for the load and ambient temperature
4. Heat sink fins clogged with debris
5. Incorrect mounting (inadequate clearance above/below drive)

### Diagnosis Steps:
1. Open the drive enclosure door and listen for the cooling fan — on smaller drives it runs continuously; on larger ones it cycles
2. Inspect heat sink fins — use compressed air to clear debris
3. Measure ambient temperature at the drive intake
4. Check switching frequency parameter — some applications run with higher-than-necessary switching frequencies

### Fix:
- Replace cooling fan (common failure on drives >5 years old)
- Add forced ventilation to the enclosure
- Reduce switching frequency (costs slightly higher motor noise, saves drive temperature)
- For liquid-cooled NXP: check coolant flow rate and inlet temperature

> **Parts needed:** Cooling fan (Ebm-papst or equivalent, frame-specific), IP54 door fan kit for sealed enclosures

---

## F22 — Parameter Fault

**Meaning:** A checksum error in the drive's parameter storage. Parameters may be corrupted or inconsistent.

### Causes:
- Power loss during a parameter save operation
- Memory chip degradation (older drives)
- Parameter conflict from software download

### Fix:
1. Note any custom parameter settings first (or use NCDrive to upload/download parameter files)
2. Reset factory defaults: navigate to **System Menu → Load Factory Defaults**
3. Re-enter critical parameters (motor data, application settings, I/O assignments)
4. If fault persists: the control board may need replacement

---

## F29 — Thermistor Fault (Option Board Input)

**Meaning:** The thermistor input on an option board (typically OPTAF) detected motor overtemperature OR the input is open-circuit when it should be connected.

### Critical Note for Unused Thermistor Inputs:
If the thermistor function is not used and the OPTAF board is installed, the thermistor input terminals **must be short-circuited** (jumpered). An open-circuit input will read as infinite resistance, which the drive interprets as a tripped thermistor (motor too hot).

### Causes:
- Motor thermistor (PTC) has reached trip temperature
- Thermistor cable disconnected or broken
- Thermistor input not short-circuited when unused
- Thermistor short circuit (NXP S1: hardware short circuit on the input)

### Diagnosis Steps:
1. Measure thermistor resistance at the motor: cold motor PTC should read <1500 Ω; >4000 Ω indicates trip
2. Check cable from motor to drive for continuity and shorts
3. If not using a physical thermistor: verify terminals are jumpered

---

## F52 — Keypad / Panel Communication Fault

**Meaning:** Communication between the keypad and the drive control board was lost.

### Causes:
- Keypad cable disconnected or damaged
- Panel connected and then removed during operation (if configured as the control source)
- EMI interference on the keypad cable in noisy installations

### Fix:
- Reconnect or replace the keypad cable
- If control is from remote I/O (not keypad), ensure the control source parameter is set correctly — the drive should not trip on keypad loss if keypad isn't the active control source

---

## F53 / F54 — Fieldbus and Slot Faults

**F53 — Fieldbus Communication Fault:**
The fieldbus master (PLC) has not communicated with the drive within the watchdog timeout.

**Causes:**
- PLC program stopped or in stop mode
- Fieldbus cable disconnected
- Wrong drive address or baud rate
- Fieldbus terminating resistors missing

**F54 — Slot Fault:**
An option board in a drive slot failed or was removed.

**Fix for F54 when board was intentionally removed:**
Navigate to the System Menu and acknowledge the hardware change to clear the fault. The drive retains the slot configuration until explicitly reset.

---

## Accessing Parameters: Lock/Unlock

### Vacon NXP / NXS — Parameter Lock
- Navigate to **M7 → System → Password**
- Default password: 0
- Enter password to unlock write access

### Vacon 100 — Parameter Lock
- Navigate to **Main Menu → System → Security → Password**
- Locked parameters show a padlock icon on the keypad
- Can also be controlled via digital input (Parameter Lock DI)

---

## Fault History Access — Step by Step

### Vacon NXP via Keypad:
1. From main display: press right arrow
2. Navigate to **M4** (Fault History)
3. Enter the menu — shows F-codes, subcodes, and drive state at trip

### Vacon 100 via Keypad:
1. Press MENU
2. Navigate to **Diagnostics → Fault History**
3. Scroll through entries — each shows Fault Code, Fault ID, timestamp, and frequency/current/voltage at trip

### Via NCDrive (NXP) or VACON Live (Vacon 100):
Both PC tools provide far more detail than the keypad and allow parameter backup before major troubleshooting. Connect via the RS-232 service port (RJ45 to DB9 adapter, 9600 baud, 8-N-1).

---

## HVAC and Pump Application Notes

Vacon 100 FLOW/HVAC drives are optimized for fan and pump applications. Common HVAC-specific issues:

| Symptom | Likely Cause | Parameter to Check |
|---|---|---|
| F1 on startup | Acceleration too fast for high-inertia fan | Increase accel time; enable flying start |
| F2 on deceleration | Fan coasting, regenerating energy | Extend decel time or enable coast stop |
| F17 underload on pump | Pump running dry or cavitation | Check suction conditions; adjust underload curve |
| F10 input phase | HVAC power quality issue | Add line reactor; check utility supply |
| F14 drive overheat | Enclosure too warm in mechanical room | Add forced ventilation; check ambient temp |
| F52 keypad fault | Panel removed but still set as control source | Set control source to I/O; use remote control |

---

## Parts Reference Table

| Part | Application | Notes |
|---|---|---|
| Braking chopper | High-inertia decel, prevent F2 | VBRC series, must match drive frame size |
| Braking resistor | Absorbs regenerative energy | Size to duty cycle and braking power |
| PTC thermistor (motor) | Motor thermal protection input | 1K NTC or Klixon type, motor-specific |
| OPTAF safety board | STO (Safe Torque Off) function | NXP option boards; slot A |
| I/O option board | Extra digital/analog I/O | OPTB1, OPTB2 (NXP), Slot B/C |
| Cooling fan (internal) | Heat sink cooling | Ebm-papst or Sunon, frame-specific |
| Service cable | PC diagnostics connection | RS-232 RJ45-to-DB9 adapter |
| Control board (NXP) | Replace if F8 internal faults persist | VB00561 rev H or newer for OPTAF support |

---

## Quick Fault Reference

| Fault | Short Meaning | Most Common Fix |
|---|---|---|
| F1 | Overcurrent | Check motor wiring; increase accel time |
| F2 | Overvoltage | Extend decel time; add braking resistor |
| F3 | Ground fault | Megohmmeter motor cable and motor |
| F5 | Charging switch | Power down fully; check precharge circuit |
| F9 / F6 | Undervoltage | Check input fuses and supply voltage |
| F7 / F16 | Motor overtemperature (calc) | Reduce load; check motor data parameters |
| F8 | System fault | Check subcode; often STO or internal hardware |
| F10 | Input phase loss | Check fuses and supply cable |
| F14 | Drive overtemperature | Clean/replace cooling fan; check ambient |
| F17 | Motor underload | Check belt, coupling, and pump prime |
| F22 | Parameter fault | Reload factory defaults; re-enter parameters |
| F29 | Thermistor fault | Check motor thermistor or short unused input |
| F52 | Keypad fault | Check keypad cable or set control source to I/O |
| F53 | Fieldbus fault | Check PLC and fieldbus cable/termination |
| F54 | Slot fault | Reseat or acknowledge removed option board |

When contacting Danfoss/Vacon technical support, provide: drive model number (from the nameplate), firmware version (from the system menu), the complete fault history list including all subcodes/IDs, and the application parameters file if available from NCDrive or VACON Live.

## Where to Buy Replacement Parts

Find replacement parts for Vacon (Danfoss) VFDs on Amazon:

- [Vacon Danfoss VFD Drive Replacement Parts](https://www.amazon.com/s?ascsubtag=ecf-vacon-vfd-fault-codes&k=Vacon+VFD+drive+replacement+parts&tag=errorcodefixes-20)
- [Danfoss VFD Cooling Fan Replacement](https://www.amazon.com/s?ascsubtag=ecf-vacon-vfd-fault-codes&k=Danfoss+Vacon+VFD+cooling+fan+replacement&tag=errorcodefixes-20)
- [VFD Option Card & Fieldbus Module](https://www.amazon.com/s?ascsubtag=ecf-vacon-vfd-fault-codes&k=VFD+fieldbus+option+card+module&tag=errorcodefixes-20)