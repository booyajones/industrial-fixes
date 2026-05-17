---
title: "Emerson VFD Fault Codes — Complete Troubleshooting Guide"
description: "Emerson VFD fault codes for EV series, Commander, and Mentor MP drives. What each code means and how to fix it."
pubDatetime: 2026-04-27T22:00:00Z
modDatetime: 2026-04-27T22:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - electrical
  - vfd
  - emerson
---

Emerson rebranded the Control Techniques drive lineup under its industrial automation division — the Commander SK, Commander C300, and Mentor MP DC drive all carry Emerson branding but are Control Techniques products underneath. Since Nidec acquired Control Techniques in 2012, you may see any of these names on the drive nameplate: Emerson, Control Techniques, Nidec, or Leroy-Somer. The fault codes are identical regardless of badge.

This guide covers the full trip code list for the Commander SK (the most widely deployed unit), along with Commander C300 and Mentor MP specifics, parameter references, and a parts table for the most common hardware replacements.

---

## Jump to Fix

- [OI.AC — Output Overcurrent](#oiac--output-overcurrent)
- [OU — DC Bus Overvoltage](#ou--dc-bus-overvoltage)
- [UU — DC Bus Undervoltage](#uu--dc-bus-undervoltage)
- [O.ht1 / O.ht2 / O.ht3 / O.ht4 — Overtemperature](#oht1--oht2--oht3--oht4--overtemperature)
- [O.Ld1 — User Output Overload](#old1--user-output-overload)
- [It.AC — I²t Output Overload](#itac--it-output-overload)
- [Ph — Input Phase Loss](#ph--input-phase-loss)
- [SCL — Serial Communications Loss](#scl--serial-communications-loss)
- [EEF — EEPROM Trip](#eef--eeprom-trip)
- [HFxx — Hardware Faults](#hfxx--hardware-faults)
- [Mentor MP Trip Codes](#mentor-mp-dc-drive-trip-codes)
- [Auto-Reset Configuration](#auto-reset-configuration)
- [Parts Table](#parts-table)

---

## Which Drive Do You Have?

**Commander SK** — Compact general-purpose AC drive, 0.25 kW to 132 kW. Single or three-phase input. LED display with alphanumeric trip codes (flashing). Introduced around 2002, widely used through 2020s.

**Commander C300** — Mid-range AC drive, 0.37 kW to 250 kW. Clearer LCD display. More advanced control modes including closed-loop vector. Trip codes share most Commander SK codes but add C300-specific ones.

**Mentor MP** — DC regenerative drive, 25 A to 1850 A. Used for DC motor control, winding applications, and retrofit of older DC systems. Has its own trip code set.

The nameplate will show the model number starting with "SK" (Commander SK), "C3" (C300), or "MP" (Mentor MP).

---

## Commander SK / C300 Fault Code Reference Table

| Code | Meaning | Most Common Cause | Fix |
|------|---------|-------------------|-----|
| **UU** | DC bus under-voltage | Low AC supply; loose input wiring | Check input voltage at L1/L2/L3 terminals. Acceptable range: ±10% of rated supply |
| **OU** | DC bus over-voltage | Deceleration ramp too fast; regenerative load | Increase decel ramp time (Pr 02.21 / Pr 02.22). Add braking resistor |
| **OI.AC** | Output instantaneous overcurrent | Motor/cable short; insufficient autotune | Check motor cable insulation with megger. Re-run autotune (Pr 05.12 = 1) |
| **OI.br** | Braking resistor overcurrent | Resistor value too low; excessive braking cycles | Check resistor ohm value against spec. Increase decel ramp time |
| **O.SPd** | Overspeed | Load driving motor above setpoint | Check mechanical coupling. Reduce speed reference or add speed feedback |
| **It.AC** | I²t output overload | Sustained overcurrent below OI.AC threshold | Reduce load. Check motor tuning. Verify current limits in Pr 04.07 |
| **It.br** | I²t on braking resistor | Braking resistor energy limit reached | Check braking cycle time. Verify resistor watt rating |
| **O.ht1** | IGBT overheat (thermal model) | Drive overloaded; ambient too high | Reduce duty cycle. Check enclosure ventilation |
| **O.ht2** | Heatsink over-temperature | Internal fan failed; blocked vents | Check internal cooling fan. Clean heatsink fins. Reduce ambient temp |
| **O.ht3** | Drive overheat (extended thermal model) | Similar to O.ht1, longer duration | As O.ht1. Check mounting — drives need 100 mm clearance top and bottom |
| **O.ht4** | Power module rectifier overheat | Heavy regenerative operation; high ambient | Check ambient. Consider derating. Verify input reactor is installed |
| **th** | Motor thermistor trip | Motor overheated | Check motor temperature. Verify PTC thermistor wiring at T1/T2 |
| **O.Ld1** | +24V / digital output overload | Short on user +24V terminal | Disconnect external wiring from +24V terminal. Check for wiring short |
| **SCL** | Serial comms loss timeout | Comms cable fault; master controller offline | Check RS485/fieldbus cable. Verify master controller heartbeat. Check Pr 11.24 timeout setting |
| **Ph** | Input phase loss or imbalance | Supply fuse blown; loose input terminal | Check L1/L2/L3 fuses. Measure phase balance. Only applies to three-phase units |
| **EEF** | EEPROM data loss | Parameter corruption after power interruption | Set default parameters: Pr 00.00 = 1253 (European defaults) or 1254 (US). Reconfigure drive |
| **rS** | Stator resistance measurement failure | Motor too small; motor disconnected | Verify motor is wired and correct size for drive. Re-autotune |
| **tunE** | Autotune incomplete | Run command removed before completion | Restart autotune. Maintain run command until complete |
| **cL1** | Analog input current loss | 4-20 mA signal dropped below 3 mA | Check signal source. Verify wiring continuity. Check Pr 07.10 mode setting |
| **CL.bt** | Control word trip | Remote control system sent trip command | Check PLC/SCADA control logic. Check Pr 06.42 |
| **C.dAt** | SmartStick no data | New/blank SmartStick installed | Program SmartStick or install one with valid data |
| **C.Acc** | SmartStick read/write fail | Dirty or damaged SmartStick contacts | Re-seat SmartStick. Replace if fault persists |
| **C.rtg** | SmartStick rating mismatch | SmartStick from different drive rating used | Use SmartStick programmed on matching drive size |
| **OVL.d** | I×t overload | Motor current sustained above rated | Reduce load. Check application acceleration profile |
| **br.rS** | Braking resistor overload | Braking resistor approaching thermal limit | Reduce braking frequency. Check Pr 10.30–10.39 |
| **FAIL** | SmartStick read fail | Read attempted while drive running | Disable drive before reading SmartStick |

---

## OI.AC — Output Overcurrent

**What it means:** The drive detected an instantaneous overcurrent on its output. This is the drive protecting itself and the motor from a dead short or extreme load spike.

**Causes in order of frequency:**

1. Phase-to-phase or phase-to-ground short in motor cable
2. Motor winding fault (insulation breakdown)
3. Drive requires autotune — stator resistance Pr 05.17 is incorrect
4. Ramp times too short for load inertia
5. Motor too large for drive (check drive amp rating vs motor FLA)

**Fix steps:**

1. Disconnect the motor cable at the drive output terminals (U, V, W)
2. Megger test the motor and cable at 500V DC — phase-to-phase and phase-to-ground. Any reading below 1 MΩ indicates a fault
3. If cable/motor checks out, reconnect and re-run stationary autotune: set Pr 05.12 = 1, apply run command
4. If OI.AC occurs only during acceleration, increase Pr 02.11 (acceleration ramp)
5. If OI.AC occurs at steady speed, check for mechanical overload or binding

**Related parameters:** Pr 04.07 (current limit), Pr 05.12 (autotune enable), Pr 05.17 (stator resistance)

---

## OU — DC Bus Overvoltage

**What it means:** The DC bus voltage exceeded the safe limit. For 400V drives this is typically 820V DC; for 200V drives around 415V DC.

**Causes in order of frequency:**

1. Deceleration ramp time too short — motor regenerates energy back into the bus faster than it can be dissipated
2. Load is actively driving the motor (conveyor, crane, elevator, fan with high inertia)
3. Supply voltage too high (overvoltage on the incoming supply)
4. Braking resistor not connected or undersized

**Fix steps:**

1. Increase deceleration time: Pr 02.21 (standard decel) or check Pr 02.22–02.24 for ramp 2/3/4
2. Enable voltage-controlled decel (overvoltage ride-through): check Pr 02.08 for ramp hold
3. If frequent OU on regenerative loads, install a dynamic braking resistor on terminals BR+ and BR−
4. Verify incoming supply voltage is within spec on all three phases

**Braking resistor minimum values (approximate):**
- 0.75 kW drive: 200Ω minimum
- 2.2 kW drive: 100Ω minimum
- 7.5 kW drive: 33Ω minimum
- 22 kW drive: 18Ω minimum

---

## UU — DC Bus Undervoltage

**What it means:** DC bus dropped below minimum threshold. 400V drives trip below approximately 390V DC.

**Causes:**
- Input supply voltage too low or dipping under load
- Blown input fuse or MCB
- Loose input terminal connection
- Drive powered from external DC supply with insufficient voltage

**Fix steps:**

1. Measure line-to-line voltage at the drive input terminals under load
2. Check input fuses/MCBs — replace if blown
3. Torque-check all input terminals (L1/L2/L3 and PE)
4. If supply is marginal, check for other large loads on the same circuit causing voltage dip

---

## O.ht1 / O.ht2 / O.ht3 / O.ht4 — Overtemperature

These four codes represent different layers of thermal protection:

| Code | Sensor | Trigger |
|------|--------|---------|
| O.ht1 | IGBT thermal model (software) | Drive overloaded sustained |
| O.ht2 | Heatsink thermistor (hardware) | Heatsink temp > max (typically 90°C) |
| O.ht3 | Extended thermal model | Longer-term overload pattern |
| O.ht4 | Power module rectifier thermistor | Rectifier temperature too high |

**Fix steps for all:**

1. Check internal cooling fan is spinning — on size B/C frames (0.75–7.5 kW) there is one fan at the top of the heatsink. On larger frames, multiple fans
2. Clean heatsink fins — remove accumulated dust and debris
3. Verify mounting clearances: minimum 100 mm above and below drive, 50 mm each side
4. Check ambient temperature — Commander SK rated to 40°C ambient at full load. Above 40°C requires derating
5. If O.ht4, check if large braking cycles are driving rectifier heating — add an input reactor

**Fan replacement:** Commander SK cooling fan connector is a 2-pin plug on the drive PCB. Match the voltage (typically 24V DC internal fan) and physical size to the frame.

---

## O.Ld1 — User Output Overload

**What it means:** The +24V user supply (terminal 22 on most SK frames) is sourcing too much current. Typically caused by too many devices powered from this supply or a wiring short.

**Fix:** Disconnect external wiring from terminal 22 progressively, starting with the last-connected device. When fault clears, isolate the overloaded device. Maximum current from this terminal is 200 mA on Commander SK.

---

## It.AC — I²t Output Overload

**What it means:** The motor current exceeded the rated level for long enough that the cumulative I²t heating model tripped the drive. Unlike OI.AC (instantaneous), It.AC is a sustained overload.

**Common causes:**
- Motor current limit set too high for motor rating
- Mechanical overload — pump cavitation, conveyor jam, fan blade fouling
- Motor ambient temperature too high, reducing its own thermal capacity

**Fix:** Reduce load, or if load is correct, verify Pr 04.07 (current limit) matches motor FLA. Check Pr 04.15–04.16 for overload thresholds.

---

## Ph — Input Phase Loss

**What it means:** One of the three input phases is missing or severely imbalanced. Only applies to three-phase rated drives — dual-rated 200/400V units may not trigger this.

**Fix steps:**
1. Check all three input fuses/MCBs upstream of the drive
2. Measure phase-to-phase voltages at L1/L2/L3 — should be within 2% of each other
3. Check input terminal torque — loose terminals cause high-resistance connections that look like phase loss
4. Inspect input contactor contacts if a contactor is upstream

---

## SCL — Serial Communications Loss

**What it means:** The drive is set to run under remote serial control (RS485 Modbus, CTNet, or fieldbus) and has lost communication from the master for longer than the timeout period.

**Fix steps:**
1. Check serial cable integrity — RS485 is differential pair; check for broken wire or connector oxidation
2. Verify network termination resistors are installed at both ends of the RS485 bus
3. Check master controller (PLC/DCS/SCADA) — is it sending the heartbeat/poll as expected?
4. Review Pr 11.24 (comms timeout) — if set too short for the application, increase it
5. Check Pr 11.22 (Modbus address) matches the address the master is polling

---

## EEF — EEPROM Trip

**What it means:** Drive detected parameter data corruption, typically after a power interruption during a parameter write.

**Fix:** Load factory defaults and reconfigure from scratch:
- Press and hold the MODE button while powering up (some models)
- Or set Pr 00.00 = 1253 (50 Hz defaults) or 1254 (60 Hz defaults) and press Enter
- Reinstate all application-specific parameters from a saved record

Always record parameter settings after commissioning — CTSoft (free from Control Techniques/Nidec) can save a full parameter file.

---

## HFxx — Hardware Faults

HF codes indicate internal drive hardware failures. The number after HF indicates the specific fault:

| Code | Fault |
|------|-------|
| HF01 | Watchdog processor failure |
| HF05 | Control supply voltage fault |
| HF07 | Current sensor fault |
| HF20 | DSP communication failure |
| HF22 | Analog input circuit fault |

**Important:** Most HF faults cannot be reset by the user. A power cycle (turn off, wait 5 minutes, power on) is the first attempt. If the HF code returns on every power-up, the drive requires repair or replacement. Hardware faults typically indicate a PCB or power module failure — not something caused by the application.

---

## Mentor MP DC Drive Trip Codes

The Mentor MP is a regenerative DC drive used with separately-excited DC motors. It shares some naming conventions with the Commander series but has its own trip set:

| Code | Meaning | Common Fix |
|------|---------|------------|
| **OI.AC** | Armature current overcurrent | Check motor armature for shorts; reduce acceleration rate |
| **OI.F** | Field overcurrent | Check field wiring; verify field resistance |
| **OU** | DC bus overvoltage | Same as Commander SK — check decel ramp and supply |
| **UU** | DC bus undervoltage | Check AC supply voltage and fuses |
| **O.ht1** | Drive thermal model trip | Reduce load duty cycle |
| **O.ht2** | Heatsink temperature | Check cooling fans and ambient |
| **O.SPd** | Motor overspeed | Check speed feedback (tacho/encoder); check armature voltage |
| **Enc** | Encoder fault | Check encoder cable continuity; check supply voltage at encoder |
| **ENC.Ph** | Encoder phase error | Swap A and B channels; check encoder PPR setting in Pr 03.26 |
| **ENC.L** | Encoder loss | Encoder signal dropped — check cable and connections |
| **Fld.L** | Field loss | Field current dropped below minimum — check field contactor, field fuse, field winding continuity |
| **th** | Motor thermistor | Motor overtemperature |
| **SCL** | Serial comms loss | Same as Commander SK |

### Mentor MP Parameter Notes

- **Pr 03.26** — Encoder lines per revolution (PPR). Must match encoder nameplate
- **Pr 04.13** — Armature current limit. Should be set to 150% motor FLA maximum for starting
- **Pr 05.14** — Field current setpoint. Check motor nameplate for rated field current
- **Pr 08.22** — Motor thermistor enable. Set to 1 if PTC thermistor connected, 0 if not

---

## Viewing Trip History

The Commander SK stores the last 10 trips in:
- **Pr 10.20** — Most recent trip
- **Pr 10.21** — Second most recent
- **Pr 10.29** — Oldest stored trip

To access these: press MODE repeatedly to reach Level 3 (or use CTSoft / Connect software). The trip history shows the fault code and, on more advanced drives, the drive state at the time of trip (speed, current, voltage).

**CTSoft** (free download from nidec-drives.com) provides trip history with freeze-frame data: DC bus voltage, output current, and speed at the moment of trip. Essential for diagnosing intermittent faults.

---

## Auto-Reset Configuration

To configure automatic restarts after certain trip types:

- **Pr 10.33** — Number of auto-reset attempts (0 = disabled, up to 5)
- **Pr 10.34** — Auto-reset delay time (seconds)
- **Pr 10.35–10.39** — Select which trip codes trigger auto-reset

**Recommended settings for pumps and fans:**
- Pr 10.33 = 3 (three attempts)
- Pr 10.34 = 10 (10-second wait between attempts)
- Enable auto-reset for: UU, OU, O.ht1, SCL — but not for OI.AC or HF codes (hardware/mechanical faults should require human attention)

---

## Parts Table

| Component | Application | Part Notes |
|-----------|------------|------------|
| **Braking resistor** | Commander SK any frame | Match ohm value to drive frame size. CT part numbers: SK-BR1 (small frames) through SK-BR7 (large). Can substitute generic resistors if wattage and ohms match spec sheet |
| **Internal cooling fan** | Commander SK Frame B–E | 24V DC fans. Frame B: 60×60 mm. Frame C: 80×80 mm. Frames D/E: 120×120 mm. Nidec/CT part or equivalent Sunon/Delta |
| **SmartStick** | Commander SK/C300 | Parameter backup card — CT part number SM-Applications or SK-SD-PG. Stores complete parameter set |
| **RS485 communication card** | Commander SK | SM-Serial option module for RS485/Modbus RTU. Part: SM-Serial |
| **Encoder feedback module** | Commander SK, Mentor MP | SM-Encoder-Plus option module for ABZ encoder feedback |
| **Encoder cable** | Mentor MP / Commander C300 | Shielded twisted pair, minimum 4 pair. Ground shield at drive end only. Belden 9728 or equivalent |
| **Input line reactor** | Any frame | AC line choke reduces harmonics and protects rectifier. CT part: LAC-xxx. 3–5% impedance recommended |
| **EMC filter** | Any frame | Required for CE compliance. CT part: EMC-BLF-xxx (external filter) |
| **Control Techniques CTSoft** | All Commander/Mentor | Free software for parameter management and diagnostics. Available at nidec-drives.com |

---

## Common Misdiagnoses

**"The drive faults immediately on power-up."**
Often not the drive. Check: (1) Are all three input phases present? Ph fault may display before any other check runs. (2) Is DC bus pre-charge circuit working? A bad pre-charge resistor causes UU or HF at power-up.

**"OI.AC only happens in winter/summer."**
Seasonal OI.AC: in summer, higher ambient causes motor winding resistance to increase slightly — drive sees more current for same load. Check motor cooling, verify motor is not undersized for the application.

**"Drive works fine but trips SCL once a week."**
Intermittent SCL is almost always a wiring problem: loose RS485 connector, missing termination resistor, or ground loops on the comms bus. Check every connection in the serial daisy chain.

**"Replaced the drive, same fault."**
If an HF code or OI.AC returns immediately on a new drive, the problem is external: motor short, output cable fault, or mechanical overload. Do not assume a new drive is problem-free until motor and cable are confirmed clean.

---

## Reset Procedure

Three ways to reset a tripped Commander SK:

1. **Keypad:** Press the red STOP/RESET button
2. **Digital input:** Toggle the enable/reset digital input (Terminal B4 on most frames) from High → Low → High
3. **Serial comms:** Send a reset command via Modbus or CTNet

**Important:** Always investigate and fix the root cause before resetting. A drive that trips immediately after reset has an active fault — repeated resets without investigation can cause permanent damage, particularly for OI.AC faults.

## Where to Buy Replacement Parts

Find replacement parts for Emerson (Control Techniques) VFDs on Amazon:

- [Emerson Control Techniques VFD Replacement Parts](https://www.amazon.com/s?i=industrial&k=Emerson+Control+Techniques+VFD+drive+replacement+parts&tag=errorcodefixes-20)
- [VFD Drive Cooling Fan Replacement](https://www.amazon.com/s?i=industrial&k=VFD+drive+cooling+fan+frame+size&tag=errorcodefixes-20)
- [VFD Semiconductor Fuse Replacement](https://www.amazon.com/s?i=industrial&k=VFD+semiconductor+fuse+fast+blow&tag=errorcodefixes-20)