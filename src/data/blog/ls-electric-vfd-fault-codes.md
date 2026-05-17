---
title: "LS Electric VFD Fault Codes — Complete Troubleshooting Guide"
description: "LS Electric (LG) VFD fault codes for iS7, iG5A, iP5A, and SV series. What each code means and how to fix it."
pubDatetime: 2026-04-27T22:00:00Z
modDatetime: 2026-04-27T22:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - electrical
  - vfd
---

LS Electric VFDs, including the iG5A, iP5A, S100, iS7, and older SV series, use short trip codes on the keypad when they stop on protection. The code identifies the condition, but the fix usually comes from three checks: when the fault happened, what the drive was doing at the time, and whether the problem sits in the motor, the wiring, or the drive itself.

## Fault History and Reset

- **iG5A / iP5A:** Open the **DRV** or **FLT** group. Recent trips are stored in the fault history parameters.
- **iS7:** Open the **PRT** group. **PRT-10 through PRT-14** store the last five trips with snapshot data.
- **S100:** Open the **FAULT** group and read **FLT-01 through FLT-05**.

Reset with the keypad **STOP/RESET** key, a remote reset input, or a full power cycle after the DC bus has discharged.

---

## Fault Codes — Full Reference

### OCT / Over Current1 — Overcurrent Trip

**Display:** OCT or Over Current1  
**Meaning:** Output current exceeded the inverter's rated overcurrent threshold. This is the most common fault across all LS Electric drives.

**Causes (most to least likely):**
1. Acceleration time too short for load inertia — motor draws excessive current during ramp-up
2. Load has increased beyond motor/drive rating
3. Motor started into an already-spinning load (flying restart without speed search)
4. Output wiring short circuit
5. Motor winding shorted between phases or to ground
6. IGBT output module failed

**Parameter checks:**
- **ACC time (DRV group or BAS group):** Increase acceleration time. Rule of thumb: for conveyor loads, minimum 5–10 seconds; for compressor/fan loads, 10–30 seconds.
- **Torque boost (BAS-15 on iG5A):** If set too high, boost causes excessive current at low speed. Reduce by 1–2% increments.
- **Speed search (CON-60 on iS7):** Enable speed search if motor may be coasting when drive starts.

**Fix steps:**
1. Check fault snapshot current value — if trip current is just above rated, it's a load issue; if it's 2–3× rated, it's a short or hardware fault.
2. Disconnect motor leads and test motor winding resistance: phase-to-phase should be equal (within 5%); phase-to-ground should be >1 MΩ.
3. Verify output cables are not chafed or touching conduit ground.
4. If motor and wiring are good: increase ACC time and reduce torque boost, then test.
5. Persistent OCT with motor disconnected = IGBT fault — drive service required.

---


### OVT / Over Voltage — DC Bus Overvoltage

**Display:** OVT or Over Voltage  
**Meaning:** The DC bus voltage exceeded the safe limit (approximately 400V for 230V drives, 800V for 460V drives). Most commonly occurs during deceleration when regenerative energy from the load charges the DC bus.

**Causes:**
1. Deceleration time too short — high-inertia loads (fans, flywheels) regenerate back into DC bus during braking
2. Braking resistor not connected, undersized, or resistor protection disabled
3. Input voltage too high (supply voltage above rated by >10%)
4. Load driving the motor (overhauling load — crane lowering, downhill conveyor)

**Parameter checks:**
- **DEC time (DRV group):** Increase deceleration time.
- **Braking resistor enable (CON or BRK group):** Verify DB resistor is enabled in parameters and resistor is connected.
- **Overvoltage stall (CON group):** Enable overvoltage stall function — this temporarily reduces deceleration rate to prevent bus from climbing further.

**Fix steps:**
1. Check fault snapshot DC bus voltage — if it peaked at trip, it was regenerative.
2. Increase DEC time progressively until OVT stops occurring.
3. If load is overhauling (e.g., crane/hoist lowering): braking resistor is mandatory. Size the resistor correctly: resistor resistance = DC bus voltage² ÷ drive rated braking power. LS Electric specifies resistor values by drive frame size — consult the drive's installation manual.
4. Check input supply voltage with a meter. Tap change at transformer if supply is high.

---

### LVT / Low Voltage — DC Bus Undervoltage

**Display:** LVT or Low Voltage or UV  
**Meaning:** DC bus voltage dropped below the minimum operational level (approximately 200V for 230V drives, 400V for 460V drives).

**Causes:**
1. Input power supply dip or momentary outage
2. Input phase loss (one of three phases missing — drive runs on single-phase DC bus)
3. Input fuse or circuit breaker blown
4. Incoming supply too low (transformer tap wrong, long cable run voltage drop)
5. Magnetic contactor on input side has fault

**Fix steps:**
1. Check all three input phases with a multimeter at drive input terminals — all three should be present within 5% of each other.
2. Check input fuses (for drives with fused input) — all three fuses should have continuity.
3. If voltage dips are momentary: configure **Low Voltage restart** parameter (PRT group on iS7) for auto-restart after voltage recovery.
4. For persistent low voltage: check transformer primary tap and supply cable sizing.

---

### GFT / Ground Fault Trip

**Display:** GFT or Ground Trip  
**Meaning:** A ground fault was detected on the output — current is flowing from one or more output phases to earth ground at a level exceeding the drive's ground fault threshold.

**Causes:**
1. Output cable insulation damaged — typically from pinch point in conduit or sharp edge
2. Motor winding-to-frame fault (insulation breakdown)
3. Moisture in motor or in cable termination boxes
4. Long cable run creating high capacitive leakage current (especially with high carrier frequency)

**Fix steps:**
1. Disconnect output cables from drive output terminals. Measure resistance from each cable to ground with a multimeter (for initial check) or megohmmeter (for thorough test).
2. Disconnect motor leads from motor terminal box. Measure insulation resistance motor winding-to-frame at 500V DC: >1 MΩ is acceptable.
3. If cable is faulted: locate fault (usually at conduit entry points or buried splice). Replace damaged section.
4. If insulation resistance drops on long cable runs (>100m) with high carrier frequency: reduce carrier frequency (parameter in PWM or ADV group) to reduce capacitive leakage. Also consider output line reactor or EMC filter.

---

### OHT / OHt / Over Heat — Inverter Overtemperature

**Display:** OHT, OHt, or Over Heat  
**Meaning:** The drive's internal heatsink temperature sensor exceeded the thermal protection setpoint (typically 85–95°C depending on model).

**Causes:**
1. Cooling fan failed or blocked by debris
2. Ambient temperature too high (> 50°C / 122°F for most models)
3. Drive mounted in an enclosure without adequate ventilation
4. Minimum clearances not maintained around drive body
5. Drive running at high load continuously (continuous duty requires derating at high ambient)
6. Drive output frequency too low for extended periods (motor at low speed = poor motor cooling)

**Fix steps:**
1. Check cooling fan operation: on powered drive, the fan should be audible and visible through the top vent. A fan that spins slowly, intermittently, or not at all is the most common cause of OHT.
2. Clear any debris from top inlet and bottom outlet vents.
3. Measure ambient temperature near drive air intake with a thermometer.
4. Inspect mounting: minimum clearance above and below drive (typically 100mm top, 100mm bottom, 30mm sides — check installation manual for exact values).
5. **Fan replacement:** On most LS Electric drives, the cooling fan is accessible by removing the top cover. Note fan voltage (24VDC internal or 230VAC direct) and frame size before ordering.

---

### E.LCL / IPF — Input Phase Loss

**Display:** E.LCL, IPF, or In Phase Open  
**Meaning:** One or more input phases are missing or significantly unbalanced.

**Causes:**
1. Input fuse blown on one phase
2. Magnetic contactor contact not closing on one phase
3. Supply cable connection loose at drive input terminals
4. Upstream phase loss from switchgear or transformer

**Fix steps:**
1. Measure voltage at drive input terminals L1, L2, L3 under load: all three should be present and within 3% of each other.
2. Check input fuses (if fitted) — a blown fuse on one phase causes DC bus to charge from the remaining two phases, creating a large voltage ripple that stresses capacitors and creates this fault.
3. Inspect contactor contacts — if contact resistance on one pole is high (>10 mΩ), contact replacement is needed.
4. **Note:** Some single-phase applications deliberately connect to L1 and L3 only. If configured for single-phase input, disable input phase loss detection in parameters (PRT group, phase loss detection enable/disable).

---

### OPF / Out Phase Open — Output Phase Loss

**Display:** OPF or Out Phase Open  
**Meaning:** The drive detected that one or more output phases are not carrying current — typically a broken output connection or motor winding open circuit.

**Causes:**
1. Output terminal connection loose or broken
2. Motor lead connector not fully seated at motor terminal box
3. Motor winding open circuit (burnt out)
4. Motor contactor (if fitted on output) contact failure

**Fix steps:**
1. Check all three output terminal connections at the drive — T1, T2, T3 (or U, V, W).
2. Measure resistance at motor terminal box: all three phase-to-phase readings should be equal.
3. On drives with output contactors: verify contactor closes fully on all three poles when commanded.

---

### OL / IOLT — Inverter Overload

**Display:** OL, IOLT, or Inv Over Load  
**Meaning:** The drive itself is being operated beyond its continuous current rating. Unlike motor OL protection, this protects the drive's own power devices.

**Causes:**
1. Drive undersized for actual load current demand
2. Drive ambient temperature too high (reduces thermal capacity)
3. Extended operation at low frequency (cooling fan on motor insufficient)

**Fix steps:**
1. Log running current via DriveView 9 or keypad monitor over a full duty cycle.
2. Compare to drive rated output current (nameplate). If average load is >100% or peaks above 150% for extended periods, upgrade drive frame size.
3. For duty cycles with short high-load bursts followed by light-load periods: confirm the drive is rated for intermittent duty (most are 150% for 60 seconds, 200% for 3 seconds).

---

### E-Thermal / ETH — Electronic Thermal Overload (Motor)

**Display:** E-Thermal, ETH, or E.THM  
**Meaning:** The drive's electronic thermal model estimates the motor windings have exceeded safe temperature based on current history. This simulates a bimetal overload relay in software.

**Causes:**
1. Motor overloaded beyond its service factor
2. Motor run at low frequency for extended periods (at low speed, motor fan doesn't cool the motor)
3. E-thermal protection level parameter set too low
4. Motor FLA (full load amps) set incorrectly in drive parameters

**Parameter checks:**
- **Motor rated current (BAS-13 on iG5A/iS7):** Must be set to the motor nameplate FLA. If set too low, thermal protection trips prematurely.
- **E-thermal level (PRT group):** Adjust thermal protection threshold — but do not exceed motor nameplate service factor.

**Fix steps:**
1. Verify motor FLA parameter matches motor nameplate FLA exactly.
2. Check if load has increased — conveyor accumulation, seized bearing, increased product weight.
3. For low-speed continuous applications: use a motor with a separately powered blower (inverter duty rated motor with separate cooling fan).

---

### COM / Communication Error

**Display:** COM, Comm Error, or similar  
**Meaning:** Communication between the drive and an external controller (PLC, HMI, SCADA) has been lost — or between keypad and drive CPU.

**Causes:**
1. RS-485 cable disconnected or broken
2. Communication timeout setting too tight
3. Address conflict on Modbus RTU network
4. Incorrect communication parameters (baud rate, parity, stop bits mismatch)

**Parameter checks (iG5A/iS7 COM group):**
- **COM-01:** Communication address (must be unique on network)
- **COM-02:** Baud rate (match to master — typical: 9600 or 19200 bps)
- **COM-03:** Stop bits
- **COM-06:** Communication loss trip time (increase if brief communication gaps are normal)

**Fix steps:**
1. Verify RS-485 wiring: A+ and B- terminals at drive and master device — polarity matters.
2. Check termination resistors: 120 Ω resistor required at each end of RS-485 bus run.
3. Test communication cable continuity end-to-end.
4. If using Modbus TCP (iS7 with Ethernet option): check IP address assignment and network cable.

---

## Parameter Reset, Wiring Checks, and Parts

**Factory reset:**
- **iG5A:** parameter init in the **DRV** or **FUN** group.
- **iS7:** **CNF-46**.
- **S100:** **CONFIG** → **Parameter Init**.

**Common wiring issues:**
- OCT on every start usually points to a shorted motor or output cable.
- LVT and IPF usually point to input power loss, bad fuses, or a weak contactor.
- GFT on long motor leads usually points to leakage current. Lower carrier frequency or fit an output reactor.
- OVT on decel usually means the drive needs a braking resistor or a longer deceleration time.
- COM faults usually trace back to RS-485 polarity, termination, or noise.

**Typical replacement parts:** cooling fans, braking resistors, input or output reactors, EMC filters, keypads, and communication option cards. Match the frame size and voltage class before ordering.

## Where to Buy Replacement Parts

Find replacement parts for LS Electric VFDs on Amazon:

- [LS Electric VFD Drive Replacement Parts](https://www.amazon.com/s?ascsubtag=ecf-ls-electric-vfd-fault-codes&k=LS+Electric+VFD+drive+replacement+parts&tag=errorcodefixes-20)
- [VFD Braking Resistor Replacement](https://www.amazon.com/s?ascsubtag=ecf-ls-electric-vfd-fault-codes&k=VFD+braking+resistor+replacement&tag=errorcodefixes-20)
- [VFD Keypad Display Panel Replacement](https://www.amazon.com/s?ascsubtag=ecf-ls-electric-vfd-fault-codes&k=VFD+keypad+display+panel+replacement&tag=errorcodefixes-20)