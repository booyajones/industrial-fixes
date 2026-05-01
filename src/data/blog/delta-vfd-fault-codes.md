---
title: "Delta VFD Fault Codes — Complete Troubleshooting Guide"
description: "Delta VFD fault codes for VFD-C2000, VFD-MS300, VFD-E, and VFD-B series. What each code means and how to fix it."
pubDatetime: 2026-04-27T20:00:00Z
modDatetime: 2026-04-27T20:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - electrical
  - vfd
  - delta
---

Delta VFDs are workhorses — they run pumps, fans, conveyors, compressors, and HVAC systems in facilities worldwide. When one trips, you need to know fast whether you're looking at a quick parameter fix or a hardware failure that needs a spare drive.

This guide covers the complete fault code set for the **VFD-C2000**, **VFD-MS300**, **VFD-CP2000**, **VFD-E**, **VFD-B**, and **VFD-M** series. Each fault includes the display code, what it means electrically, the most common causes in order of frequency, which parameters to check, and concrete fix steps.

---

## How Delta VFDs Display Faults

All Delta drives show fault codes on the LED or LCD keypad. The drive stores the last **4–5 faults** in the fault history (the C2000 stores up to 10, accessed via parameter **06-17**).

**Reading fault history on C2000/MS300:**
1. Press MENU on the keypad.
2. Navigate to **Fault Record** (or access via Pr. 06-17 on older models).
3. The display shows faults labeled D1 through D10 (most recent = D1), each with a fault code number.

**Reading fault history on VFD-E/VFD-B:**
1. Press MODE until you reach the parameter display.
2. Navigate to **d.xx** (fault code parameters).
3. The five most recent faults are stored. Wait 5 seconds after clearing before resetting.

**Reset methods (all series):**
- Press RESET/STOP on the keypad after fault is resolved.
- Apply a RESET signal to the designated digital input terminal (configure via parameters).
- Cycle power — only use this if the fault is confirmed resolved, not as a troubleshooting step.

---

## Complete Fault Code Reference

### Overcurrent Faults

| Code | Display | Fault Name | Trigger Condition |
|------|---------|-----------|------------------|
| ocA | ocA | Overcurrent during Acceleration | Current exceeded limit while ramping up |
| ocd | ocd | Overcurrent during Deceleration | Current exceeded limit while ramping down |
| ocn | ocn | Overcurrent during Constant Speed | Current exceeded limit at steady state |
| ocS | ocS | Overcurrent at Stop | Current spike detected at stop command |
| oc / OC | oc | General Overcurrent | IGBT overcurrent protection tripped |
| Aoc | Aoc | U-phase Overcurrent before Run | Phase U short before motor starts |
| boc | boc | V-phase Overcurrent before Run | Phase V short before motor starts |
| coc | coc | W-phase Overcurrent before Run | Phase W short before motor starts |

### Overvoltage Faults

| Code | Display | Fault Name |
|------|---------|-----------|
| ovA | ovA | Overvoltage during Acceleration |
| ovd | ovd | Overvoltage during Deceleration |
| ovn | ovn | Overvoltage during Constant Speed |
| ovS | ovS | Overvoltage at Stop |
| ov / OV | ov | General DC Bus Overvoltage |

### Undervoltage / Low Voltage Faults

| Code | Display | Fault Name |
|------|---------|-----------|
| LvA | LvA | Low Voltage during Acceleration |
| Lvd | Lvd | Low Voltage during Deceleration |
| Lvn | Lvn | Low Voltage during Constant Speed |
| LvS | LvS | Low Voltage at Stop |
| Lu / LU | Lu | DC Bus Undervoltage |

### Thermal and Overload Faults

| Code | Display | Fault Name |
|------|---------|-----------|
| oH1 | oH1 | IGBT Heatsink Overheat |
| oH2 | oH2 | Internal Temperature Overheat (C2000) |
| oL | oL | Drive Overload (150% for 60 sec exceeded) |
| oL1 | oL1 | Electronic Thermal Overload Trip |
| oL2 | oL2 | Motor Overload |
| OrP | OrP | Output Phase Loss (Phase Loss Protection) |
| oPL1 | oPL1 | U-Phase Output Phase Loss |
| OSL | OSL | Slip Error |

### Ground and Short Circuit Faults

| Code | Display | Fault Name |
|------|---------|-----------|
| GFF | GFF | Ground Fault (output to earth) |
| b4GFF | b4GFF | Ground Fault detected before run |

### Communication Faults

| Code | Display | Fault Name |
|------|---------|-----------|
| CE- | CE01–CE10 | Communication Error (RS485/Modbus) |
| AErr | AErr | Analog Signal Error (ACI input) |

### External and Safety Faults

| Code | Display | Fault Name |
|------|---------|-----------|
| EF | EF | External Fault (EF terminal active) |
| bb | bb | External Base Block |
| STo | STo | Safe Torque Off — safety function activated |
| STL1 | STL1 | Channel 1 (S1~DCM) Safety Loop Error |
| STL2 | STL2 | Channel 2 (S2~DCM) Safety Loop Error |
| STL3 | STL3 | Internal Safety Loop Error |

### Software and Hardware Faults

| Code | Display | Fault Name |
|------|---------|-----------|
| cFA | cFA | Auto Ramp Fault |
| code | codE | Software Protection Failure |
| PdEF | PdEF | Parameter Default Mismatch |

---

## Detailed Fault Diagnosis and Fix Steps

### ocA — Overcurrent During Acceleration

The most common fault across all Delta VFD series. The drive's output current exceeded the overcurrent threshold while the motor was accelerating from zero or a lower speed.

**Causes in order of frequency:**
1. **Acceleration time too short** — motor cannot ramp up fast enough for the load inertia
2. **Motor undersized or load torque too high at startup** — especially on conveyors with high static friction or centrifugal pumps
3. **Motor output wiring short circuit** — insulation breakdown between phases, or between phase and ground at U/T1, V/T2, W/T3
4. **Torque boost (Pr.07-02) set too high** — excessive V/F boost at low speed drives excess current
5. **Drive output power too small for motor** — motor FLA exceeds drive capacity
6. **Motor winding degraded** — partial winding failure increases current draw

**Parameters to check:**
- **Pr.01-09 / Pr.01-10** — Acceleration time 1 (increase to reduce current during ramp)
- **Pr.07-02** — Torque compensation (reduce if set above 5%)
- **Pr.06-03** — Overcurrent stall prevention level (set to 120–150% for most loads)

**Fix steps:**
1. Increase acceleration time by 20–50% and retry. If the fault clears, the ramp was too aggressive for the load.
2. Disconnect the motor and test the drive in no-load mode — if ocA clears, the fault is load-related, not drive-related.
3. Megger test the motor leads U/V/W to ground. Reading below 1 MΩ indicates insulation breakdown — replace motor leads or motor.
4. Check all terminal connections at the drive output for tightness. A loose connection under high current creates heat and intermittent faults.
5. Reduce Pr.07-02 torque compensation to 0 and test. If resolved, the boost was masking a motor sizing issue.
6. If none of the above, verify drive output current rating matches or exceeds motor FLA. If undersized, install the correct drive.

---

### ocd — Overcurrent During Deceleration

Current spike while the drive is slowing the motor. The motor's regenerative energy cannot be absorbed fast enough.

**Causes in order of frequency:**
1. **Deceleration time too short** — most common cause by a wide margin
2. **No braking resistor on high-inertia load** — the DC bus cannot absorb energy fast enough
3. **Deceleration time set to zero** — motor free-coasts instead of controlled ramp

**Parameters to check:**
- **Pr.01-11 / Pr.01-12** — Deceleration time 1 (increase)
- **Pr.06-01** — Overcurrent stall prevention during deceleration

**Fix steps:**
1. Double the deceleration time and retry.
2. For high-inertia loads (fans, flywheels, large conveyors): add a braking resistor and braking unit if not already installed.
3. Enable overvoltage stall prevention during deceleration (Pr.06-01) — this automatically extends decel time when the DC bus rises.

---

### GFF — Ground Fault

The output current to ground is excessive — a phase-to-earth path exists at the motor, cable, or drive output.

**Causes in order of frequency:**
1. **Motor winding insulation failure** — moisture ingress, overheating, or age
2. **Cable insulation damage** — particularly in cable trays with abrasion or areas with rodent exposure
3. **Cable run too long** — distributed capacitance of long motor cables can trigger GFF on sensitive drives, particularly MS300
4. **Drive output power module failure** — internal IGBT failure with phase-to-ground path

**Diagnosis sequence:**
1. Disconnect the motor cable at the drive output terminals (U/T1, V/T2, W/T3). Attempt to run the drive in no-load mode.
   - If GFF **clears**: fault is in the motor or cable, not the drive.
   - If GFF **persists**: the drive's internal power module has failed. Replace the drive.
2. With drive powered down, megger test the motor terminals phase-to-ground at 500V DC. Any reading below 1 MΩ is a fail.
3. Inspect the motor cable for visible damage. On long cable runs (over 50m), consider adding an output line reactor or dV/dt filter.

**MS300-specific note:** The MS300 is particularly sensitive to GFF due to its internal current sensing architecture. If the motor, cable, and cable length are all within spec and GFF persists, the drive itself is typically the failure point and should be replaced.

---

### OV / ovA / ovd — DC Bus Overvoltage

The DC bus voltage exceeded the maximum allowable value (400V DC for 230V class drives, 800V DC for 460V class drives).

**Causes in order of frequency:**
1. **Deceleration too fast** — motor regeneration drives DC bus voltage up faster than it can dissipate
2. **Input voltage too high** — line voltage above the drive's rated maximum input
3. **Voltage transients on the supply** — power factor correction banks switching, nearby large motor starts
4. **No braking resistor** on regenerative or high-inertia applications

**Parameters to check:**
- **Pr.00-10** — Display DC bus voltage (monitor during fault condition)
- **Pr.06-01** — Overvoltage stall prevention (enable to auto-extend decel time)

**Fix steps:**
1. Measure supply voltage at R/S/T terminals under load — should be within ±10% of rated voltage.
2. Enable overvoltage stall prevention.
3. Increase deceleration time.
4. If the application involves regenerative braking, install a braking resistor and braking unit sized to the motor's regenerated energy.
5. For overvoltage at stop (ovS): the issue is typically a voltage transient at the input. Add a line reactor (3–5% impedance) ahead of the drive.

---

### UV / Lu / LvA — DC Bus Undervoltage

DC bus voltage dropped below the minimum threshold — typically 200V DC for 230V class, 400V DC for 460V class.

**Causes in order of frequency:**
1. **Input supply voltage too low** — line voltage sag, especially at startup of large nearby loads
2. **Phase loss on input** — one phase of R/S/T is missing
3. **Blown input fuse or tripped breaker** on one phase
4. **Input contactor or disconnect partially open**
5. **Weak or failing input rectifier bridge**

**Fix steps:**
1. Measure all three phases at R/S/T with a true-RMS meter under load. A balanced three-phase supply within ±5% is required.
2. Check all input fuses — a single blown fuse creates a single-phase condition that drives undervoltage.
3. If all input voltages are correct, the drive's input rectifier bridge may be failing. This is a drive-level repair.

---

### oH1 — IGBT Heatsink Overheat

The heatsink temperature sensor on the main IGBT module exceeded the protection threshold (typically 90–100°C depending on series).

**Causes in order of frequency:**
1. **Ambient temperature exceeds 40°C (104°F)** — Delta drives are rated for 40°C ambient. In hot electrical rooms or enclosures with poor ventilation, this is exceeded regularly.
2. **Cooling fan failed or blocked** — the drive's internal fan runs continuously at full load. Fan failure is the most common hardware cause of oH1.
3. **Heatsink fins clogged** — dust and lint accumulation in industrial environments
4. **Drive operating above rated current continuously** — derating is required above 40°C

**Fix steps:**
1. Measure ambient air temperature at the drive's air intake. If above 40°C, the drive must be derated or the enclosure must be cooled.
2. Listen and feel for fan operation. A seized fan bearing is audible. Replace the cooling fan — this is a standard wear item on any VFD.
3. Remove the drive from the cabinet and blow out the heatsink with compressed air (2–3 bar). Lint and dust can completely block fin passages.
4. Verify clearance above and below the drive in the enclosure — Delta requires at minimum 50mm clearance top and bottom for proper airflow.
5. If the drive is at or below 40°C ambient with a working fan and clear heatsink and still faults on oH1, the thermistor on the heatsink may have failed. This typically requires a board-level repair.

---

### oL / oL1 / oL2 — Drive and Motor Overload

| Code | Meaning | Protection method |
|------|---------|-----------------|
| oL | Drive overload | Drive output sustained at 150% for >60 seconds |
| oL1 | Electronic thermal overload | Drive's internal E-OL function tripped based on current vs. time curve |
| oL2 | Motor overload | Motor overcurrent relative to motor FLA parameter |

**Parameters to check:**
- **Pr.05-01** — Motor rated current (must be set to motor nameplate FLA)
- **Pr.06-03 to 06-05** — Over-torque detection settings
- **Pr.07-02** — Torque compensation

**Fix steps:**
1. Verify Pr.05-01 matches the motor nameplate FLA exactly. If the motor rated current is set too low, the E-OL trips prematurely.
2. Check for mechanical overload — a seized bearing, jammed conveyor, or closed-off pump discharge will drive current up.
3. Reduce torque compensation if set above 5% — excessive boost at low speed creates continuous elevated current.
4. For persistent oL2 with correct parameters, the motor may be undersized. Calculate required torque vs. motor rated torque.

---

### EF — External Fault

The drive's EF input terminal received an external fault signal. This is a user-wired protection input.

**Causes:**
1. External protection device (overtemperature switch, vibration sensor, process interlock) tripped
2. EF terminal wired incorrectly — wrong logic (normally open vs. normally closed)
3. Noise pickup on long EF input wire run

**Fix steps:**
1. Identify what device is wired to the EF terminal. Check whether that device has legitimately tripped.
2. Verify input logic in the drive parameters — a mismatched NO/NC configuration causes permanent EF.
3. If spurious — shorten the wire run or add a 0.1µF capacitor across the input to suppress noise.

---

### CE — Communication Error

Modbus RTU (RS-485) communication fault between the drive and a PLC, SCADA, or HMI.

**Sub-codes (C2000):**
- **CE01** — Communication checksum error
- **CE02** — Communication command error
- **CE03** — Communication data error
- **CE04** — Communication address error
- **CE10** — Communication timeout

**Causes in order of frequency:**
1. **Baud rate mismatch** between drive and master
2. **RS-485 wiring fault** — loose connection at drive terminals (SG+, SG–), missing termination resistor, or wrong pin mapping
3. **Station address conflict** — two drives with the same Modbus address
4. **Timeout parameter too tight** — drive trips on CE before the master responds

**Parameters to check:**
- **Pr.09-00** — Communication address (station number)
- **Pr.09-01** — Baud rate (match to master: 9600, 19200, 38400, 115200)
- **Pr.09-02** — Stop bits / parity
- **Pr.09-03** — Communication timeout value

**Fix steps:**
1. Confirm baud rate, data bits, stop bits, and parity match exactly between drive and master.
2. Verify the drive's station address is unique on the network.
3. Check the RS-485 cable for breaks — use a multimeter to verify continuity on both SG+ and SG–.
4. Add a 120Ω termination resistor between SG+ and SG– at the last device on the bus if not already present.
5. Increase the timeout value (Pr.09-03) if the master is slow to respond.

---

### STo — Safe Torque Off

The drive received a safety signal on its STO (Safe Torque Off) input, which immediately cuts gate drive signals to the IGBTs — the motor coasts to stop.

**This is not a fault in the traditional sense.** STo is a designed safety function per IEC 61800-5-2.

**Causes:**
1. Safety relay, guard switch, or E-stop wired to STO inputs opened intentionally
2. STO input wiring disconnected or terminal loose
3. STO function incorrectly connected for applications that don't use it (jumper missing at S1/S2)

**Fix steps:**
1. If the machine is safe to operate: verify the safety device on the STO circuit is reset and contacts are closed.
2. If STO is not being used: install the factory jumper between S1 and DCM, and S2 and DCM (per the drive's wiring diagram). Operating without this jumper causes STo on every power cycle.
3. If STL1/STL2/STL3 appear (internal safety loop errors): the STO circuit detected inconsistent signals between the two STO channels. This requires drive inspection or replacement.

---

### PHL / OrP — Phase Loss

Input phase loss (PHL) or output phase loss (OrP/oPL1). The drive detected missing or unbalanced phases.

**Input phase loss (PHL):**
- Check incoming fuses and all three-phase connections.
- Measure phase-to-phase voltage at R/S/T. All three should be within 3% of each other.
- A weak connection showing half-voltage on one phase is a common cause.

**Output phase loss (OrP/oPL1):**
- Disconnect the motor and check the cable.
- Inspect the drive's output terminals for a loose or burned connection on one phase.
- If the drive output shows correct voltage on all three phases but the motor still shows a phase missing, the motor's internal winding on that phase has opened.

---

## Accessing and Clearing Fault History

### VFD-C2000 — Fault History via Pr.06-17

| D number | Fault recorded |
|----------|---------------|
| D1 | Most recent fault |
| D2–D10 | Previous faults (oldest = D10) |

Access: Keypad > MENU > Parameter Settings > Pr.06-17 > scroll D1 to D10.

Each entry contains the fault code number. Cross-reference with the fault code table in Chapter 14 of the C2000 user manual.

**Clearing fault history:** Set Pr.06-17 to D1, hold ENTER — this clears the entire fault log on most firmware versions.

### VFD-MS300 — Fault History

Navigate to: Keypad > MENU > Fault Record.

Faults display as text codes (ocA, GFF, etc.) with occurrence count.

**DIAStudio (Delta's PC software):** Connect via USB and use DIAStudio's fault viewer for a timestamped fault log — significantly easier than keypad navigation on busy drives.

---

## Parameter Reset to Factory Defaults

To reset all parameters to factory default on C2000 and MS300:

1. Set **Pr.00-02** = 9 (full parameter reset) or = 10 (reset including motor parameters).
2. Press ENTER to confirm.
3. The drive resets and restarts. All custom parameters are lost.

**Warning:** Parameter reset is destructive. Before resetting, document all application-specific parameters, especially:
- Pr.01-xx (ramp times, frequency limits)
- Pr.02-xx (digital I/O mapping)
- Pr.05-01 (motor FLA)
- Pr.09-xx (communication settings)

---

## Common Misconfigurations That Cause Repeated Faults

**Motor FLA not programmed:** If Pr.05-01 (motor rated current) is left at the factory default, the electronic thermal overload calculates based on drive FLA rather than motor FLA. This causes premature oL1 on large drives with small motors, or fails to protect small motors on large drives.

**Acceleration/deceleration at minimum (0.1 seconds):** Factory default for some models is very short ramp times. On any real load, this guarantees ocA/ocd on every start. Set ramp times appropriate for your load.

**Input voltage class wrong:** A 230V drive installed on 460V will show persistent overvoltage and likely destroy the input rectifier within minutes. Always verify the drive's voltage class matches the supply before energizing.

**STO jumper missing on non-safety applications:** On C2000 and MS300 drives with STO terminals, the jumper between S1/DCM and S2/DCM must be installed if the STO function is not used. Missing this jumper produces a persistent STo fault.

---

## Parts Reference

| Part | Function | Notes |
|------|----------|-------|
| Cooling fan (replacement) | Drive thermal management | Primary wear item — replace at 2–3 years or on oH1 |
| Braking resistor | DC bus overvoltage absorption | Sized to motor HP and duty cycle — do not guess |
| Braking unit | Controls braking resistor connection to DC bus | Required for resistor >10% duty |
| Input line reactor (3–5%) | Input harmonic suppression and transient protection | Recommended on all drives >5 HP |
| Output dV/dt filter | Protects motor insulation from fast voltage edges | Required for long cable runs >50m |
| RS-485 termination resistor (120Ω) | Signal integrity on Modbus bus | Install at last drive on bus |

---

## Parts and Supply Links

- **[Delta VFD Replacement Cooling Fan](https://www.amazon.com/s?k=delta+vfd+cooling+fan+replacement&tag=errorcodefixes-20)** — verify model number before ordering
- **[VFD Braking Resistor](https://www.amazon.com/s?k=vfd+braking+resistor+dynamic+braking&tag=errorcodefixes-20)**
- **[VFD Line Reactor 3-Phase](https://www.amazon.com/s?k=vfd+line+reactor+3+phase+input&tag=errorcodefixes-20)**
- **[RS-485 Cable Shielded](https://www.amazon.com/s?k=rs485+shielded+cable+modbus&tag=errorcodefixes-20)**
- **[VFD Output dV/dt Filter](https://www.amazon.com/s?k=vfd+dvdt+filter+output+motor&tag=errorcodefixes-20)**
