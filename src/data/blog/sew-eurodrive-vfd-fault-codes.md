---
title: "SEW-Eurodrive VFD Fault Codes — Complete Troubleshooting Guide"
description: "SEW-Eurodrive MOVITRAC, MOVIDRIVE, and MOVIMOT fault codes. What each fault means and how to fix it."
pubDatetime: 2026-04-28T00:00:00Z
modDatetime: 2026-04-28T00:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - electrical
  - vfd
  - sew-eurodrive
---

## SEW-Eurodrive VFD Fault Codes — What They Mean

SEW-Eurodrive manufactures gearmotors, variable speed drives, and servo systems used extensively in material handling, conveyor systems, packaging, and industrial automation. Their drive product lines include MOVITRAC (basic VFDs), MOVIDRIVE (servo and vector drives), MOVIMOT (integrated motor/drive units), and the newer MOVI-C platform.

Fault codes appear on the seven-segment display as a capital F followed by two digits (F01, F10, etc.). Warning codes appear as a lower-case r or H prefix in some firmware versions.

**Product families covered:**
- **MOVITRAC B / MOVITRAC LTP** — basic frequency inverters
- **MOVIDRIVE B / MDX61B** — servo and vector drives
- **MOVIMOT** — integrated drive/motor units, fault codes transmitted via fieldbus
- **MOVI-C / MOVIAXIS** — modular servo drive system

---

## Accessing Fault History

**Keypad (DBG60B or built-in):**
1. Navigate to **Parameters** → **P007** (fault memory / fault history)
2. The last 5 faults display with: fault code, fault class, operating hours at time of fault, and drive status at fault

**MOVITOOLS MotionStudio (PC software):**
1. Connect via USB or RS485
2. Open **Parameter Tree** → **Unit Functions** → **Fault Memory**
3. Download and view full fault history with operating data at time of fault

**Key parameter numbers for fault information:**
- **P007**: Fault memory (last 5 faults)
- **P810/P811/P812**: Fault counter per fault class
- **P950/P951**: Unit fault code and fault class readback

---

## Overcurrent and Output Faults

### F01 — Overcurrent in Output Stage

What it means: Output current exceeded the overcurrent shutdown threshold (typically 150–200% of rated current).

Causes (in order of frequency):
1. Motor cable too long without output reactor — cable capacitance causes current spikes
2. Motor insulation failure — measure insulation resistance >1MΩ phase-to-ground
3. Output short circuit — wiring fault between drive and motor
4. Rapid acceleration ramp — too short for motor/load inertia
5. Drive power module (IGBT) failure

Diagnosis:
- Disconnect motor cable at drive. If fault clears at startup: motor or cable is the fault. If fault fires with no motor connected: drive output stage is failed.
- Measure motor winding resistance phase-to-phase (should be within 5%) and phase-to-ground (>1MΩ).
- Check acceleration ramp time — **P130** (acceleration time). Increase if too short.

Fix:
- Add output choke (reactor) for cables >50m
- Increase acceleration ramp time
- Replace motor if insulation failed
- Replace IGBT module if drive output stage faulted

**Parameter to check:** P130 (ramp-up time), P131 (ramp-down time)

---

### F02 — Overvoltage in DC Link

What it means: DC bus voltage exceeded the limit (typically 800–850VDC for 480V drives, 420VDC for 240V drives).

Causes:
1. Deceleration ramp too short — regenerative energy has nowhere to go
2. Braking resistor not connected or undersized
3. Braking chopper (internal or external) failed
4. Incoming line voltage too high
5. Load driving the motor (crane lowering, overhauling load)

Diagnosis:
- Check if fault only occurs during deceleration → extend deceleration ramp or install/verify braking resistor
- Check incoming voltage under load — should not exceed 10% above rated

Fix:
- Extend deceleration ramp (P131)
- Install correctly sized braking resistor and connect to BR+/BR- terminals
- Replace internal braking chopper if defective
- Add line reactor for voltage spike protection

**Parameter to check:** P131 (ramp-down time), P740 (braking resistor type/P741 braking resistor value)

---

### F03 — Short Circuit at Drive Output

What it means: A direct short circuit detected at the drive output terminals. The drive detects this through zero-crossing current measurement.

Causes:
1. Motor cable phase-to-phase short — usually at connector or where cable was pinched
2. Motor terminal box internal short
3. Motor winding inter-turn short (catastrophic)
4. Drive output terminal wiring error

Diagnosis: Isolate the motor completely, check motor terminal box, inspect cable for damage.

---

### F04 — Earth Fault (Ground Fault)

What it means: Phase-to-earth (phase-to-ground) current exceeded the monitoring threshold.

Causes:
1. Motor insulation failure to ground — especially in wet/humid environments
2. Damaged motor cable — insulation worn through at cable carrier
3. Motor winding contamination (moisture, oil, coolant)
4. Motor cable too long without proper shielding

Diagnosis: Megohm test — disconnect motor from drive, measure each phase to ground. Should be >1MΩ at 500VDC test voltage.

---

## Overvoltage and Undervoltage Faults

### F06 — Undervoltage in DC Link

What it means: DC bus voltage dropped below the operational minimum during run.

Causes:
1. Mains power dip or outage
2. Undersized power supply for multiple drives on shared DC bus
3. Fuse blown in incoming power section
4. Loose power connection causing intermittent supply

Fix: Check incoming voltage. Verify all power connections are tight. If mains power is unreliable, add an input line reactor for ride-through.

---

### F07 — Speed Monitoring Fault (Tachometer/Encoder)

What it means: Actual speed deviated too far from commanded speed, or encoder/tachometer feedback was lost.

Causes:
1. Encoder cable damaged or connector loose
2. Encoder failure — check supply voltage at encoder (typically 5V or 24V)
3. Slip in mechanical coupling between motor and encoder
4. Speed feedback gain parameters set incorrectly
5. Motor load too heavy for current speed limits

**Parameter to check:** P140 (maximum speed), P341 (encoder pulses per revolution), P342 (encoder supply voltage)

---

## Thermal and Temperature Faults

### F10 — Drive Overtemperature

What it means: The heatsink or internal temperature exceeded the shutdown limit (typically 80–85°C heatsink).

Causes:
1. Ambient temperature too high in control cabinet (>40°C / 104°F)
2. Cabinet cooling fan failed
3. Drive cooling fan (internal) failed
4. Drive mounted too close to other heat sources
5. Duty cycle too high for derating conditions

Fix: Clean drive heatsink fins. Verify cabinet cooling fan. Check mounting orientation (drives must mount vertically). Derate the drive for high-ambient installations.

---

### F43 — Motor Overtemperature (PTC/NTC Thermistor)

What it means: The motor's embedded thermistor (PTC or NTC type) reported motor temperature above the trip limit.

Causes:
1. Motor overloaded — verify torque and current against rated values
2. Motor cooling fan failed (for TEFC motors, the fan is on the motor shaft — check at low speed operation)
3. Blocked motor ventilation
4. Incorrect thermistor type configured (PTC vs NTC selection)

**Parameter to check:** P120 (motor thermistor monitoring enable/type)

---

## Braking Faults

### F21 — Brake Fault

What it means: The mechanical brake integrated with the gearmotor did not confirm open/closed state within the expected time.

Causes (SEW gearmotors with integrated brake):
1. Brake coil failure — measure coil resistance (should match nameplate)
2. Brake rectifier failure (internal to drive or external box)
3. Brake airgap too large — worn brake lining
4. Brake contactor/relay failure
5. Missing or incorrect brake supply voltage

Diagnosis: Measure voltage at brake coil terminals during an open command. Should equal rated brake voltage (typically 24VDC or 205VAC).

**Parameter to check:** P830 (brake function), P831/P832 (brake opening/closing delay times)

---

## Encoder and Feedback Faults

### F44 — Encoder Fault

What it means: Encoder supply voltage or signal levels are outside tolerance. Typically: no signal, or signal level too low.

Causes:
1. Encoder cable broken — check pin by pin at the D-sub connector
2. Encoder power supply failed — measure at encoder connector
3. Encoder internal failure — mechanical damage (bearing, disk)
4. EMI interference — check shielding, shield connected at drive end only

---

### F45 — Encoder Count Error

What it means: Encoder count direction doesn't match expected, or count error detected.

Causes:
1. Encoder wired in reverse — swap A and A-bar (differential) or swap tracks
2. Encoder resolution parameter set incorrectly
3. Mechanical coupling slip — encoder moving at different rate than motor

**Parameter to check:** P341 (encoder pulses/rev), P342 (encoder supply), P345 (encoder direction reversal)

---

## Communication Faults

### F60 — RS485 / Fieldbus Communication Timeout

What it means: The drive expected a command from the fieldbus (PROFIBUS, DeviceNet, CANopen, EtherNet/IP) but didn't receive one within the watchdog timeout.

Causes:
1. PLC program stopped or fault condition
2. Communication cable disconnected
3. Fieldbus master went offline
4. Address conflict on the bus
5. Watchdog timeout set too short for the application cycle time

Fix: Verify PLC is running and outputting process data. Check cable. Increase watchdog timeout (P883).

**Parameter to check:** P883 (bus timeout), P885 (bus response on timeout)

---

### F61 — SBus (Synchronous Bus) Communication Error

What it means: SEW's internal synchronous bus (MOVILINK) between drive and option card lost communication.

Causes:
1. Option card (fieldbus interface, encoder card) not seated properly
2. Option card failure
3. Option card firmware incompatible with drive firmware

Fix: Reseat option card. Verify firmware versions match.

---

## MOVIMOT Specific Faults

MOVIMOT units transmit fault codes via the connected fieldbus (AS-Interface, PROFIBUS, etc.). The fault code appears in the status word.

**MOVIMOT common faults:**
- **0x01** — Motor overtemperature
- **0x02** — Overcurrent
- **0x04** — Overvoltage
- **0x08** — AS-i communication fault (check AS-i cable voltage: 28–32VDC)
- **0x10** — Undervoltage
- **0x20** — Blocking fault (motor stalled)

Reset MOVIMOT faults: cycle power or send reset command via fieldbus.

---

## Clearing Faults and Reset Methods

**Manual reset:**
1. Remove the fault condition
2. Press the **STOP/RESET** key on the keypad (DBG60B)
3. Or send binary signal to the reset input (P601)

**Auto-reset (P630):** SEW drives support automatic fault reset after a configurable delay. Set P630 to the number of auto-reset attempts allowed. Use carefully — auto-reset on mechanical faults can cause damage.

**Factory reset:** Parameter **P700** — restores all parameters to factory defaults. Use only as last resort.

---

## Parts Reference

| Component | Application | Notes |
|---|---|---|
| Braking Resistor | Overvoltage prevention | Size per drive kW and duty cycle |
| Output Reactor (Choke) | Long cable protection | Required for cables >50m |
| DBG60B Keypad | Local operation/programming | Plug-in, works across drive families |
| Encoder Cable | Speed feedback | Shielded, twisted pair, shield at drive end |
| Brake Rectifier | Integrated brake supply | Match motor brake voltage rating |
| Fieldbus Option Card | Communication | Match fieldbus type: PROFIBUS, EtherNet/IP |
| Fan Module | Drive cooling | Model-specific, available as replacement part |

SEW-Eurodrive service: 1-864-439-7537 (US). MOVITOOLS MotionStudio is free for download from SEW's website.

---

## Amazon Affiliate Links

- [Braking Resistor 100W 100 Ohm](https://www.amazon.com/s?i=industrial&k=braking+resistor+100w+VFD+drive&tag=errorcodefixes-20)
- [Output Line Reactor 3-Phase VFD](https://www.amazon.com/s?i=industrial&k=output+line+reactor+3+phase+VFD&tag=errorcodefixes-20)
- [PTC Thermistor Motor Protection](https://www.amazon.com/s?i=industrial&k=PTC+thermistor+motor+protection+sensor&tag=errorcodefixes-20)
- [Shielded Encoder Cable 5-Pin](https://www.amazon.com/s?i=industrial&k=shielded+encoder+cable+industrial&tag=errorcodefixes-20)
