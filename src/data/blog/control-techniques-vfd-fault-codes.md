---
title: "Control Techniques VFD Fault Codes — Complete Troubleshooting Guide"
description: "Control Techniques Unidrive M, Unidrive SP, and Commander SK fault codes. What each code means and how to fix it."
pubDatetime: 2026-04-27T21:00:00Z
modDatetime: 2026-04-27T21:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - electrical
  - vfd
money_part: "Braking resistor"
---

Control Techniques (now Nidec) drives are found across industrial conveyors, pumps, fans, compressors, and machine tool spindle applications. The **Unidrive M** series (M200 through M700), **Unidrive SP**, and **Commander SK/C300** share a common fault naming convention — trip codes that appear on the drive keypad display or via parameter readback. This guide covers every common trip code with causes, parameter checks, and fix procedures written for industrial maintenance technicians.

## Jump to Section

- [How Control Techniques Trips Work](#how-control-techniques-trips-work)
- [Accessing Trip History](#accessing-trip-history)
- [OI.AC — Output Overcurrent](#oiac--output-overcurrent)
- [OU — DC Bus Overvoltage](#ou--dc-bus-overvoltage)
- [UV — Undervoltage](#uv--undervoltage)
- [OHt.drive — Drive Overtemperature](#ohtdrive--drive-overtemperature)
- [OHt.th — Motor Thermistor Overtemperature](#ohtth--motor-thermistor-overtemperature)
- [O.SPd — Overspeed](#ospd--overspeed)
- [Ph — Input Phase Loss](#ph--input-phase-loss)
- [I.Old — Current Overload](#iold--current-overload)
- [OI.Br — Braking Resistor Overcurrent](#oibr--braking-resistor-overcurrent)
- [HF Series — Hardware Faults](#hf-series--hardware-faults)
- [SL — Serial Communications Loss](#sl--serial-communications-loss)
- [Additional Trip Codes](#additional-trip-codes)
- [Auto-Reset Configuration](#auto-reset-configuration)
- [Trip History Access and Parameter Checks](#trip-history-access-and-parameter-checks)
- [Parts Reference Table](#parts-reference-table)

---

## How Control Techniques Trips Work

When a trip condition occurs, the Control Techniques drive:

1. Immediately disables the output to the motor (coast to stop)
2. Displays the trip code on the keypad
3. Logs the trip in the **trip log** (last 10 trips stored)
4. Holds the trip state until manually reset (or auto-reset fires if configured)

**Two categories:**

- **Trips** — latching faults that disable the drive. Require a reset before the drive can run.
- **Sub-trips** — on Unidrive M series, many trips have a sub-trip number that provides more diagnostic detail. Access via Pr **10.020** (trip 0 sub-trip) through Pr **10.029**.

**Trip vs. Alarm vs. Warning:**  
A **Trip** stops the drive. An **Alarm** or **Warning** (displayed as a flashing code on some models) is a pre-trip condition — the drive is still running but approaching a limit. React to alarms before they become trips.

**Model differences:**  
- **Unidrive M200/M300** — compact drives, keypad with 5-character display
- **Unidrive M400** — adds onboard PLC and extended I/O
- **Unidrive M600/M700** — high-performance servo/closed-loop drives
- **Unidrive SP** — legacy high-performance drive (predecessor to M700)
- **Commander SK** — simple AC drive for basic applications
- **Commander C300** — mid-tier drive with Ethernet option

Trip codes are consistent across the family with minor exceptions for model-specific features.

---

## Accessing Trip History

### Via Keypad

1. Navigate to **Menu 10** (Diagnostics) on the keypad.
2. **Pr 10.020** — Most recent trip (trip 0)
3. **Pr 10.021** through **Pr 10.029** — Trip history (trips 1–9, oldest last)
4. Each trip parameter shows the trip code number. To decode: cross-reference the number against the trip list in the drive's user guide.
5. On **Unidrive M** series, use **Pr 10.070** through **Pr 10.079** for sub-trip codes corresponding to each trip history entry.

### Via Control Techniques Connect (PC Software)

1. Connect a USB cable to the drive (Unidrive M series have a USB port on the keypad).
2. Open **Control Techniques Connect** software.
3. Go to **Diagnostics > Trip Log** — view all 10 trips with sub-codes, timestamp (if RTC fitted), and operating conditions at the time of trip (output frequency, current, DC bus voltage).

### Via Parameters

For advanced diagnostics, key parameters at time of trip are latched:

| Parameter | Description |
|-----------|-------------|
| Pr 10.040 | Output frequency at last trip |
| Pr 10.041 | Output current at last trip |
| Pr 10.042 | DC bus voltage at last trip |
| Pr 10.043 | Drive temperature at last trip |
| Pr 10.044 | Motor thermistor resistance at last trip |

---

## OI.AC — Output Overcurrent

**Display:** `OI.AC`  
**Full name:** Output instantaneous overcurrent  
**Sub-trip:** Pr 10.070 (sub-trip number gives axis/phase detail on M600/M700)

### What Triggers It

The instantaneous output current exceeded the drive's hardware overcurrent trip threshold — typically 200–220% of rated drive current. This is a fast hardware trip, not a software overload.

**Important:** OI.AC cannot be reset for 10 seconds after it trips. This is by design to allow DC bus capacitors to recover.

### Causes (in order of frequency)

1. **Short circuit on the output cable** — phase-to-phase or phase-to-ground fault at the motor or in the cable
2. **Motor insulation failure** — aged or failed winding insulation causing a ground fault
3. **Output cable too long** — capacitive charging currents exceed hardware trip on startup
4. **Acceleration ramp too short** — motor slips poles and draws instantaneous overcurrent
5. **Feedback device fault** (M600/M700 closed-loop) — incorrect feedback causes unstable current regulation
6. **Auto-tune issue** — if the trip occurred during or after auto-tune, incorrect motor parameters can cause current instability

### Diagnosis Steps

1. **Disconnect the motor and run the drive with no load.** If OI.AC still trips, the drive hardware is suspect.
2. **Megger the motor and cable** — test insulation resistance phase-to-phase and phase-to-ground. Should be >1 MΩ; below 1 MΩ indicates insulation failure.
3. **Check cable length** — refer to the drive's maximum cable length table for the frame size. Excessive capacitance may require an output filter (Pr **05.024** — set to 1 to enable software current limiting on ramp).
4. **Extend the acceleration ramp** — increase Pr **02.011** (acceleration rate) to a lower value (longer ramp).
5. **Check feedback device** (closed-loop) — verify encoder connections and cable shielding.
6. **Re-run auto-tune** if motor parameters are suspect (Pr **05.012** = 1 for stationary auto-tune).

### Parameter Checks

| Parameter | Description | Check |
|-----------|-------------|-------|
| Pr 05.007 | Motor rated current | Must match motor nameplate |
| Pr 05.009 | Motor rated voltage | Must match motor nameplate |
| Pr 02.011 | Acceleration ramp (s/100Hz) | Increase if ramp-related |
| Pr 05.024 | Motor cable capacitance mode | Set to 1 for long cable |

---

## OU — DC Bus Overvoltage

**Display:** `OU`  
**Full name:** DC bus overvoltage

### What Triggers It

The DC bus voltage exceeded the overvoltage trip threshold:
- 400V drives: trip at approximately 830 VDC
- 200V drives: trip at approximately 415 VDC

### Causes (in order of frequency)

1. **Deceleration ramp too short** — regenerated energy from decelerating load charges the DC bus
2. **No braking resistor installed** — the drive has no way to dissipate regenerative energy
3. **Braking resistor circuit fault** — resistor open, wiring fault, or braking IGBT failed
4. **High inertia load** — large fans, flywheels, or centrifuges regenerate large energy on decel
5. **Supply voltage high** — grid voltage above rated input range
6. **Supply transient** — voltage spike from utility switching

### Diagnosis Steps

1. **Check incoming supply voltage** — measure all three phases at the drive input terminals. On a 400V drive, input should be 380–480 VAC. Above 480V continuously indicates supply issue.
2. **Extend the deceleration ramp** — increase Pr **02.021** (deceleration rate). This is the fix for the majority of OU faults.
3. **Install or check braking resistor** — if a braking resistor is fitted, check resistance with a multimeter (should match the drive's minimum braking resistance specification). Check wiring continuity to the BR terminals.
4. **Enable dynamic braking** — verify Pr **10.030** (braking resistor enable) is set correctly.
5. **Check braking IGBT** — if the resistor checks out, the braking transistor in the drive may be failed. This requires drive replacement or repair.

### Parameter Checks

| Parameter | Description | Check |
|-----------|-------------|-------|
| Pr 02.021 | Deceleration rate (s/100Hz) | Increase to avoid OU on decel |
| Pr 06.071 | Braking resistor enable | Set to 1 if resistor fitted |
| Pr 10.030 | Braking resistor thermal protection | Configure for resistor power rating |

---

## UV — Undervoltage

**Display:** `UV`  
**Full name:** DC bus undervoltage

### What Triggers It

DC bus voltage dropped below the undervoltage trip threshold — approximately 200 VDC on 400V drives.

### Causes (in order of frequency)

1. **Power supply interruption** — momentary voltage sag or supply dropout
2. **Input fuse blown** — one or more input fuses open
3. **Input contactor not fully closing** — intermittent contact
4. **Low supply voltage** — utility voltage below acceptable range
5. **Single phase loss** (see also Ph fault) — one phase missing charges bus only on two phases

### Diagnosis Steps

1. Measure AC input voltage at the drive terminals during operation — check for voltage sags under load.
2. Inspect all three input fuses for continuity.
3. Check input contactor operation — verify all three contacts closing cleanly.
4. If UV fires momentarily on startup only, verify the power supply can handle drive inrush. Some small transformers sag during drive startup.

**Note:** UV trips are often transient and auto-reset if configured. A persistent UV fault indicates a continuous supply issue.

---

## OHt.drive — Drive Overtemperature

**Display:** `OHt.drive`  
**Full name:** Drive heatsink overtemperature

### What Triggers It

The drive's internal heatsink temperature exceeded the overtemperature threshold (typically 100–105°C).

### Causes (in order of frequency)

1. **Clogged or failed cooling fans** — most common cause in dusty environments
2. **Inadequate ventilation** — drive installed in a sealed enclosure without airflow
3. **Switching frequency too high** — higher switching frequency increases drive losses
4. **Ambient temperature too high** — enclosure or room temperature above drive rating (typically 40–45°C max)
5. **Drive overloaded** — operating above rated current continuously
6. **Heatsink clogged with debris** — compressed air to clean the heatsink fins

### Diagnosis Steps

1. **Check cooling fans** — the drive's internal fans should spin freely. Listen for bearing noise. Replace if failed.
2. **Clean the heatsink** — use compressed air to blow out dust from heatsink fins.
3. **Check enclosure ventilation** — verify airflow in and out of the enclosure. Add exhaust fans if needed.
4. **Reduce switching frequency** — Pr **05.018** (switching frequency). Reducing from 12 kHz to 6 kHz significantly reduces drive losses.
5. **Check ambient temperature** — install a thermometer in the enclosure and log temperature over a shift.

### Parameter Checks

| Parameter | Description | Action |
|-----------|-------------|--------|
| Pr 07.004 | Heatsink temperature | Read current temperature |
| Pr 05.018 | PWM switching frequency | Reduce to lower drive losses |

---

## OHt.th — Motor Thermistor Overtemperature

**Display:** `OHt.th`  
**Full name:** Motor thermistor overtemperature

### What Triggers It

The motor thermistor (PTC or NTC) connected to the drive's thermistor input exceeded the trip threshold. This protects the motor windings from thermal damage.

### Causes (in order of frequency)

1. **Actual motor overheating** — motor is genuinely too hot. Check load and cooling.
2. **Motor thermistor open circuit** — PTC sensor or wiring failed open
3. **Motor cooling fan failure** — on TEFC motors, the shaft-mounted cooling fan may be failed or blocked
4. **Thermistor input parameter misconfigured** — Pr **07.015** thermistor type set incorrectly

### Diagnosis Steps

1. Measure thermistor resistance at the motor terminal box. A healthy PTC thermistor reads under 1,500 Ω at room temperature. An open thermistor reads infinite Ω — replace the sensor.
2. Check motor cooling fan operation — verify it spins and airflow over the motor is unobstructed.
3. Verify thermistor wiring continuity from motor terminal box to drive thermistor input terminals.
4. If no thermistor is installed, the thermistor input terminals should be linked per the drive manual — an open circuit will cause OHt.th.

### Parameter Checks

| Parameter | Description | Check |
|-----------|-------------|-------|
| Pr 07.015 | Thermistor type | Match to installed thermistor (PTC/NTC) |
| Pr 07.014 | Motor protection enable | Confirm thermistor protection enabled |

---

## O.SPd — Overspeed

**Display:** `O.SPd`  
**Full name:** Motor overspeed

### What Triggers It

The motor speed (measured via encoder feedback on closed-loop drives, or estimated on open-loop) exceeded the overspeed trip threshold — typically 120–130% of maximum speed.

### Causes (in order of frequency)

1. **Closed-loop feedback failure** — if encoder feedback is lost, the drive may demand full voltage and the motor overspeeds
2. **Speed reference runaway** — analog input noise or misconfigured reference causes commanded speed above maximum
3. **Incorrect maximum speed setting** — Pr **01.006** (maximum reference) set too high for the application
4. **Overshooting deceleration** — on regenerative loads, speed momentarily exceeds target

### Diagnosis Steps

1. Check encoder feedback connections — loose encoder cable causes speed feedback loss and runaway.
2. Check the analog speed reference input — verify Pr **01.037** (analog input value) during operation. Noise on the 0–10V input can spike the speed reference.
3. Verify maximum speed parameters (Pr **01.006**, **01.008**) are set appropriate for the application.
4. On open-loop drives, O.SPd from a frequency drive may indicate the motor is being driven beyond synchronous speed by the load (pumped-up phenomenon on centrifugal loads).

---

## Ph — Input Phase Loss

**Display:** `Ph`  
**Full name:** Input phase loss

### What Triggers It

One of the three AC input phases is missing or significantly lower than the others.

### Causes (in order of frequency)

1. **Blown input fuse** — most common. Check all three input fuses.
2. **Loose terminal connection** — one phase wire loose at the drive input terminals or upstream
3. **Upstream circuit breaker contact failure** — one pole of a 3-pole breaker not making contact
4. **Utility supply problem** — actual phase loss from the supply

### Diagnosis Steps

1. Measure voltage at the drive input terminals — check all three phases (L1-L2, L2-L3, L1-L3). A missing phase will read zero on two of three measurements.
2. Check all three input fuses with a multimeter.
3. Check the input terminal torque — loose connections on one phase cause intermittent Ph trips under load.

**Note:** Single-phase operation is possible on some 200V drives. Check Pr **06.046** (single phase input enable) — if enabled, the Ph trip is disabled. This should NOT be enabled on 400V 3-phase drives.

---

## I.Old — Current Overload

**Display:** `I.Old`  
**Full name:** Motor current overload (I²t thermal overload)

### What Triggers It

The drive's software thermal model detected sustained overcurrent. Unlike OI.AC (hardware overcurrent), I.Old is a time-integrated overload — the motor has been running above the rated current threshold for long enough that the thermal model predicts winding damage.

### Causes (in order of frequency)

1. **Mechanical overload** — load increased (jammed conveyor, seized bearing, thick material)
2. **Incorrect motor rated current** — Pr **05.007** set higher than motor nameplate, allowing overload to run without protection
3. **Running at low speed for extended periods** — shaft-mounted cooling fans lose effectiveness below 20–25 Hz; motor overheats even at rated current
4. **Motor undersized for the application** — continuous load exceeds motor rating

### Diagnosis Steps

1. Monitor output current vs. motor rated current (Pr **05.007**). If current is consistently near or above rated, the mechanical system is overloaded.
2. Verify Pr **05.007** matches the motor nameplate rated current exactly.
3. Check for mechanical issues in the driven load — bearings, couplings, gearboxes.
4. For low-speed continuous applications, consider a motor with forced ventilation (external blower) independent of shaft speed.

### Parameter Checks

| Parameter | Description | Check |
|-----------|-------------|-------|
| Pr 05.007 | Motor rated current | Must match nameplate |
| Pr 04.015 | Overload accumulator (%) | Shows thermal model state (100% = trip) |
| Pr 04.016 | Overload time limit | Configure per application requirements |

---

## OI.Br — Braking Resistor Overcurrent

**Display:** `OI.Br`  
**Full name:** Braking resistor overcurrent

### What Triggers It

The instantaneous current through the braking resistor exceeded the hardware limit, or the braking resistor thermal model (calculated from switching duty cycle) detected an overload.

### Causes (in order of frequency)

1. **Braking resistor value too low** — resistance below the drive's minimum specified braking resistance causes excessive peak current
2. **Braking resistor failed short circuit** — resistor winding shorted
3. **Continuous regeneration** — load regenerates continuously and resistor is not rated for 100% duty cycle
4. **Braking IGBT failed** — shorted braking transistor continuously discharges DC bus through resistor

### Diagnosis Steps

1. Measure braking resistor resistance with a multimeter — compare to specified value. Resistance below minimum indicates resistor is shorted or wrong part installed.
2. Calculate the minimum resistor value for your drive using: R_min = V_dc² / P_peak (where V_dc is the DC bus voltage and P_peak is the drive's maximum braking power — see drive catalog).
3. If resistor is correct value and fault persists, check the braking IGBT by measuring collector-emitter voltage across the braking transistor with the drive powered down.

---

## HF Series — Hardware Faults

**Display:** `HF01` through `HF20` (and higher on some models)  
**Full name:** Hardware fault (internal drive fault)

Hardware faults indicate internal drive electronics failure. They are distinguished from application faults because they cannot be resolved by correcting the external system.

| Code | Description | Typical Cause |
|------|-------------|---------------|
| HF01 | Internal power supply fault | Internal ±15V/5V supply failure |
| HF02 | Internal hardware fault | Gate driver, IGBT control fault |
| HF03 | EEPROM read/write fault | Parameter memory failure |
| HF04 | Watchdog fault | Processor lock-up, usually transient |
| HF05 | Control board hardware fault | Analog/digital circuit fault |
| HF06 | Power board hardware fault | Power stage fault |
| HF07 | Encoder power supply fault | 5V/15V encoder supply failure |
| HF10 | Overcurrent at power-up | Drive damaged, possible short at output |
| HF15 | IGBT overcurrent | Power stage transistor fault |

### Diagnosis and Action

1. **Power cycle the drive** — transient HF faults (HF04 watchdog) often clear on power cycle.
2. **Check for connected fault** — HF10 and HF15 may be caused by a failed external component (shorted motor or cable). Disconnect the motor and power cycle. If HF clears, the motor or cable is the problem.
3. **Persistent HF faults** — hardware faults that return after power cycle require drive repair or replacement. Contact Control Techniques/Nidec service or an authorized repair center.
4. **Record all HF faults** — HF faults are stored in the trip log. Provide the full HF sequence to the repair center.

---

## SL — Serial Communications Loss

**Display:** `SL`  
**Full name:** Serial communications loss

### What Triggers It

The drive lost communication with a serial fieldbus master — Modbus RTU, CANopen, PROFIBUS DP, DeviceNet, or Ethernet IP depending on the installed option module.

### Causes (in order of frequency)

1. **PLC or master controller stopped sending messages** — PLC faulted, program stopped, or communication scan rate too slow
2. **Fieldbus cable fault** — wiring damage, connector issue, or incorrect termination
3. **Option module fault** — the fieldbus option module (SI-PROFIBUS, SI-CANopen, etc.) failed
4. **Communication timeout setting too short** — Pr **xx.013** (comms timeout) configured too aggressively

### Diagnosis Steps

1. Check the PLC or master controller — verify it is running and actively writing to the drive.
2. Inspect fieldbus cable integrity and termination resistors (120 Ω on both ends of Modbus/CANopen RS-485 networks; PROFIBUS also requires correct termination).
3. Check option module LEDs — most SI option modules have status LEDs visible through the drive front cover. A flashing or red LED indicates the module-level fault.
4. Increase the communications timeout parameter to confirm the fault is timeout-related.

### Parameter Checks

| Parameter | Description | Check |
|-----------|-------------|-------|
| Pr xx.013 | Communications timeout | Increase if timeout too aggressive |
| Pr xx.006 | Comms node address | Verify matches master configuration |
| Pr xx.007 | Baud rate | Must match master and all devices on bus |

---

## Additional Trip Codes

| Code | Name | Common Cause | Fix |
|------|------|-------------|-----|
| `ENC1` | Encoder channel 1 fault | Encoder wire broken or connector fault | Inspect encoder cable and connector |
| `ENC2` | Encoder channel 2 fault | Encoder A/B signal fault | Check encoder signal with oscilloscope |
| `ENC8` | Encoder signal loss | Complete encoder feedback loss | Replace cable or encoder |
| `d5` | Destination parameter invalid | Application program parameter error | Review application program |
| `dF` | Drive format error | Drive type/firmware mismatch | Contact CT service |
| `C.Acc` | Control word access violation | Fieldbus writing to locked control | Review fieldbus application |
| `It.br` | Braking resistor I²t overload | Resistor insufficient for duty cycle | Increase resistor power rating |
| `PSd` | Position controller out-of-range | Position reference exceeded limits | Check position profile and limits |
| `UFAIL` | User defined trip | Application software triggered trip | Review user application logic |

---

## Auto-Reset Configuration

Control Techniques drives support automatic trip reset, useful for applications where transient trips (voltage sag, momentary overload) would cause nuisance shutdowns.

**Key parameters:**

| Parameter | Description | Typical Setting |
|-----------|-------------|----------------|
| Pr 10.034 | Number of auto-resets | 3–5 (set 0 to disable) |
| Pr 10.035 | Auto-reset delay time (s) | 5–30 seconds |
| Pr 10.036 | Auto-reset trip mask | Bit field — select which trips can auto-reset |

**Caution:** Do not configure auto-reset for hardware faults (HF series), OI.AC on output short circuit, or motor thermistor faults. Auto-resetting into a hard fault repeatedly will damage the drive or cause mechanical hazards.

**Best practice:** Enable auto-reset only for UV (voltage sag recovery) and OHt.drive (transient temperature) with a 10-second delay. Require manual reset for all overcurrent and hardware faults.

---

## Trip History Access and Parameter Checks

### Key Diagnostic Parameters (Unidrive M Series)

| Parameter | Description |
|-----------|-------------|
| Pr 10.020 | Most recent trip code |
| Pr 10.021–10.029 | Trip history (1–9) |
| Pr 10.070–10.079 | Sub-trip codes for each trip history entry |
| Pr 10.040 | Output frequency at last trip |
| Pr 10.041 | Output current at last trip |
| Pr 10.042 | DC bus voltage at last trip |
| Pr 10.043 | Drive temperature at last trip |
| Pr 04.015 | Motor overload accumulator (0–100%) |
| Pr 07.004 | Drive heatsink temperature (°C) |
| Pr 05.007 | Motor rated current |
| Pr 01.006 | Maximum speed reference |

### Common Pr Misconfigurations That Cause Repeated Trips

1. **Pr 05.007 set too high** — if motor rated current is set above the actual motor nameplate value, I.Old protection will not trip in time to prevent motor damage. Set to nameplate exactly.
2. **Pr 02.011 / 02.021 ramp rates set too short** — causes OI.AC on acceleration and OU on deceleration. Set ramp times appropriate for the load inertia.
3. **Pr 05.018 switching frequency too high** — causes OHt.drive in high-ambient or poorly ventilated locations. Reduce to the minimum acceptable for the application.
4. **Pr 07.015 thermistor type mismatch** — causes spurious OHt.th trips. Verify PTC vs. NTC vs. KTY type matches the installed motor sensor.
5. **Pr xx.013 comms timeout too short** — causes SL faults during brief communication gaps. Increase to 2–5 seconds minimum.

---

## Parts Reference Table

| Part | Application | Notes |
|------|-------------|-------|
| Braking resistor | All drives with regenerative loads | Match resistance and wattage to drive spec |
| SI-PROFIBUS option module | Unidrive M fieldbus | Verify model compatibility — M200/M300/M400/M600/M700 have different slots |
| SI-CANopen option module | Unidrive M fieldbus | Same as above |
| SI-Ethernet option module | Unidrive M / Modbus TCP | Enables Modbus TCP / EtherNet/IP |
| Encoder feedback interface (EF) | Unidrive M600/M700 | Match to encoder type (incremental/absolute/SinCos) |
| Motor PTC thermistor | TEFC motors | 1kΩ PTC type standard for CT default Pr 07.015 |
| Keypad (remote) | All models | Use CT Connect keypad for remote mounting |
| Drive cooling fan (replacement) | Unidrive M frame C and above | Fan failure is common — stock replacements on high-production lines |
| Input fuses (semiconductor type) | All models | Must be semiconductor (fast-blow) type — standard fuses are NOT acceptable |

*Part numbers vary by drive frame size and rating. Use Control Techniques Partner Portal or contact Nidec/CT distributor for current part numbers. Always specify drive model, frame size, and firmware version when ordering option modules.*

---

## Technician Notes

- **CT Connect software is free** — download from Control Techniques website. It turns any trip history into a readable, time-stamped log and makes parameter backup/restore trivial. Install it on your service laptop before the next drive call.
- **Semiconductor fuses are mandatory** — standard T-rated fuses do not blow fast enough to protect drive IGBTs. Using the wrong fuse type means the fuses survive the fault but the drive dies. Always use the semiconductor fuse type specified in the drive manual.
- **Ground the cable shields** — screen the motor cable at both ends, grounding the shield to the drive enclosure through a dedicated EMC cable gland. Unshielded motor cables cause OI.AC and drive reset issues on sensitive drives.
- **Modbus RTU 120-ohm termination** — exactly two termination resistors on any RS-485 Modbus network — one at each physical end. Adding extra termination resistors causes signal integrity issues and SL faults. Count your terminators.
- **HF faults mean repair** — don't spend time trying to fix the external system on an HF fault. The drive hardware is failed. Replace or send for repair, then identify whether the external fault caused the internal hardware damage.

## Where to Buy Replacement Parts

Find replacement parts for Control Techniques VFDs on Amazon:

- [Control Techniques VFD Drive Replacement Parts](https://www.amazon.com/s?ascsubtag=ecf-control-techniques-vfd-fault-codes&k=Control+Techniques+VFD+drive+replacement+parts&tag=errorcodefixes-20)
- [Control Techniques Braking Resistor](https://www.amazon.com/s?ascsubtag=ecf-control-techniques-vfd-fault-codes&k=Control+Techniques+braking+resistor&tag=errorcodefixes-20)
- [VFD Drive Cooling Fan Replacement](https://www.amazon.com/s?ascsubtag=ecf-control-techniques-vfd-fault-codes&k=VFD+drive+cooling+fan+replacement&tag=errorcodefixes-20)