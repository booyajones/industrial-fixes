---
title: "Wilo Pump Fault Codes — Complete Troubleshooting Guide"
description: "Wilo pump fault codes for Stratos, TOP-S, and Yonos series. What each code means and how to fix it."
pubDatetime: 2026-04-27T22:00:00Z
modDatetime: 2026-04-27T22:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - pump
  - wilo
---

Wilo is a German pump manufacturer with a large presence in HVAC, building services, and industrial circulation applications. Their smart pump lines — particularly the Stratos MAXO and Yonos MAXO — are standard equipment in commercial heating and cooling systems across Europe, North America, and globally.

When a Wilo pump faults, it displays an E-code (error) or W-code (warning) on the integrated display. Errors stop the pump; warnings allow the pump to continue but flag a condition that requires attention. This guide covers the Stratos MAXO, Stratos GIGA, TOP-S, Yonos MAXO, and CronoLine series, with full fault code tables, diagnosis procedures, and BMS/building automation interface notes.

---

## Jump to Fix

- [E401 — Unstable Power Supply](#e401--unstable-power-supply)
- [E404 — Motor/Electronics Fault](#e404--motorelectronics-fault)
- [E006 — Rotating Field Error](#e006--rotating-field-error)
- [E014 — Leakage Detection](#e014--leakage-detection)
- [E040 — Level Sensor Fault](#e040--level-sensor-fault)
- [E062 — Dry Running / Low Water Level](#e062--dry-running--low-water-level)
- [E066 — High Water Alarm](#e066--high-water-alarm)
- [E068 — External OFF Signal Active](#e068--external-off-signal-active)
- [E080 — Pump Fault](#e080--pump-fault)
- [E085 / E141 — Pump Running Time Exceeded](#e085--e141--pump-running-time-exceeded)
- [E090 — Float Switch Plausibility Error](#e090--float-switch-plausibility-error)
- [E140 — Pump Starts Exceeded](#e140--pump-starts-exceeded)
- [W572 — Warning: System Pressure](#w572--warning-system-pressure)
- [Faults Without Error Codes](#faults-without-error-codes)
- [BMS / Building Automation Interface](#bms--building-automation-interface)
- [Reset Procedure](#reset-procedure)
- [Parts Table](#parts-table)

---

## Which Wilo Pump Do You Have?

**Stratos MAXO** — High-efficiency ECM motor, integrated display with full text and e-code readout, Modbus/BACnet/LON capable. Used in HVAC hydronic systems. Replaces Stratos series. Available 25–100 mm connections.

**Stratos GIGA** — Inline, high-flow commercial and industrial hydronic applications. Similar control interface to Stratos MAXO.

**Yonos MAXO** — Compact high-efficiency pump for residential and light commercial hydronic heating. Simplified display (LED indicator) compared to Stratos MAXO.

**TOP-S** — Standard inline circulation pump for heating and cooling. Basic 3-speed selection, no integrated display or e-codes — faults are symptom-based (won't run, low flow, noise).

**CronoLine** — High-efficiency inline pump for HVAC. Configurable via display.

**Note on code numbering:** Wilo's error code numbering varies somewhat between the pump-specific series (Stratos MAXO uses E4xx codes prominently) and the associated controller or building automation module (which uses E0xx, E1xx codes). The codes listed below are organized by series where relevant.

---

## Full Error Code Reference

| Code | Fault | Series | Auto-Reset? |
|------|-------|--------|-------------|
| **E401** | Unstable power supply | Stratos MAXO | No — manual |
| **E404** | Motor / electronics fault | Stratos MAXO | No — manual |
| **E006** | Rotating field error (phase sequence) | Stratos GIGA, CronoLine | Auto if corrected |
| **E014.x** | Leakage / moisture detected | Any with moisture probe | Manual |
| **E040** | Level sensor fault | Systems with level sensor input | Auto if sensor reconnects |
| **E062** | Dry running protection / min. water level | Waste water / flood systems | Manual** |
| **E066** | High water alarm | Waste water / flood systems | Manual |
| **E068** | External OFF contact active | Any with external control input | Auto when contact clears |
| **E080.x** | Pump fault (overload/contactor/motor) | Multi-pump controllers | Manual** |
| **E085.x** | Pump running time monitoring exceeded (old firmware) | Multi-pump controllers | Manual*** |
| **E090** | Float switch plausibility error | Waste water systems | Check and reset |
| **E140.x** | Maximum pump starts exceeded | Multi-pump controllers | Manual*** |
| **E141.x** | Pump running time exceeded (new firmware) | Multi-pump controllers | Manual*** |
| **W572** | System pressure warning | Stratos MAXO | Auto (warning only) |

---

## E401 — Unstable Power Supply

**What it means:** The pump's internal power monitoring detected voltage instability — typically a voltage sag, spike, or momentary dropout on the supply.

**Causes:**
1. Supply voltage outside acceptable range — Stratos MAXO accepts 1× 230V ±10% or 3× 400V ±10%
2. Voltage sag caused by other large loads starting on the same circuit (motors, compressors)
3. Loose supply terminal connections at the pump or upstream
4. Undersized cable causing voltage drop under load

**Fix steps:**
1. Check supply voltage at the pump terminals with a multimeter while the pump is attempting to run — should be within ±10% of rated voltage
2. Check upstream wiring: circuit breaker/MCB, cable size, terminal torque at all connection points
3. If voltage sags when the pump starts, check if a soft-start or reduced-voltage starting can help, or verify cable size is adequate for the pump FLA plus startup inrush
4. On shared circuits with other loads, check if the fault correlates with another large motor starting

---

## E404 — Motor / Electronics Fault

**What it means:** The pump's internal electronics detected a fault in the motor drive circuit or ECM motor — this is the Stratos MAXO's primary hardware fault code.

**Causes:**
1. Pump rotor mechanically blocked — debris or scale in the pump volute
2. Motor winding fault (unusual on ECM motors but possible after flooding or severe overheating)
3. Internal electronics fault — drive board or motor controller failure
4. Pump operated dry (no water) — ECM motors in wet-rotor pumps rely on system water for cooling and lubrication

**Fix steps:**
1. **Check for a blocked rotor** — this is the most common cause. Power off the pump. Locate the bleed screw on the front of the motor head (flat-head slot). Remove the screw. Insert a flat-blade screwdriver into the slot on the shaft end. Attempt to turn the shaft manually — it should turn freely with moderate resistance. If it does not move or is very stiff, the rotor is blocked
2. To clear a blocked rotor: leave the bleed screw removed, turn the shaft back and forth to dislodge debris. Refill and reinstall the bleed screw
3. Check system water is present and flowing — a dry pump will fault on E404. Verify the system is full and pressurized before restarting
4. If rotor turns freely and water is present: E404 indicates an internal electronics failure. Wilo factory service or pump replacement required
5. Wilo's guidance video for E404 specifically covers the rotor-unblocking procedure — available at wilo.com/gb/en/Support

**Reset:** After clearing the mechanical cause, power cycle the pump (off 10 seconds, on). If E404 returns within seconds of restart without any mechanical binding, the drive board has failed.

---

## E006 — Rotating Field Error

**What it means:** The pump detected incorrect phase rotation (clockwise vs. counterclockwise) or is being operated on single-phase power when three-phase input is required.

**Applies to:** Stratos GIGA, CronoLine, and other three-phase Wilo pumps.

**Fix steps:**
1. Swap any two of the three phase conductors at the pump terminal block — this reverses phase sequence
2. Alternatively, if the pump is fed through a VFD or soft starter, check the output phase rotation setting on the controller
3. If the application requires single-phase operation on a pump that specifies three-phase, this is incorrect installation — consult Wilo for single-phase rated models
4. If phase rotation monitoring is causing nuisance trips and the application requires both rotation directions (e.g., reversible pump), disable the monitoring: menu 5.68 (see pump manual for menu access procedure)

---

## E014 — Leakage Detection

**What it means:** The moisture/leakage probe installed in the motor housing or adjacent to the pump detected water intrusion.

**Fix steps:**
1. Locate the moisture probe connection — typically a two-wire connector at the motor head or accessory port
2. Inspect the pump for visible water leakage: shaft seal, housing joints, pump connections
3. If the pump is dry and there is no visible leakage, check the probe wiring for a short or damaged insulation (shorted probe causes false leakage signal)
4. Shaft seal replacement is required if the seal is leaking — this is a workshop repair
5. After repair and drying, reconnect probe and manually reset the alarm

---

## E040 — Level Sensor Fault

**What it means:** The external level sensor connected to the pump controller has lost signal — open circuit or sensor failure.

**Fix steps:**
1. Check the cable from the level sensor to the pump/controller — look for breaks, cut cables, or corroded connectors
2. Verify sensor supply voltage is present at the sensor
3. Replace the sensor if cable checks out and signal is absent

---

## E062 — Dry Running / Low Water Level

**What it means:** The dry-running protection tripped. On drainage/waste water pumps, this means the water level dropped below the minimum before the pump was switched off. On fill systems, it means the minimum level was not reached.

**Causes:**
- Drainage application: Pump ran the sump dry. Normal if the cycle is complete; fault if it keeps tripping
- Fill application: Water supply is insufficient or interrupted

**Fix steps:**
1. Check the float switch — inspect for physical damage, debris fouling the float, or incorrect installation height
2. Verify float switch wiring to the pump controller
3. On drainage systems: if the pump regularly runs dry, reposition the float switch to switch off the pump at a higher water level
4. Manual reset required** — cannot auto-reset to prevent damage from repeated dry starts

---

## E066 — High Water Alarm

**What it means:** Water level exceeded the high-water setpoint. On drainage/waste water systems, this is a critical alarm indicating the pump(s) are not keeping up with inflow.

**Fix steps:**
1. Check if the pump is running — E066 with pump stopped indicates E080 pump fault is also active
2. Verify pump operation: check motor current, check for blocked impeller
3. Check high-water float switch for correct position and operation
4. If inflow rate exceeds pump capacity, additional pumps may be required

---

## E068 — External OFF Signal Active

**What it means:** A digital input configured as "External OFF" has been activated — an external device (BMS, safety system, PLC) has commanded the pump to stop.

**Fix steps:**
1. Check the building management system or control panel for an active stop command
2. Verify the wiring at the External OFF input terminal — a shorted wire or wiring error can cause a false signal
3. Check the current connection diagram in the pump manual for terminal identification
4. If the external OFF should not be active, check the upstream control system for errors

---

## E080 — Pump Fault

**What it means:** The pump controller detected a pump-side fault. Depending on firmware version, this can mean:

- Firmware up to 2.01: No feedback from the motor contactor; bimetallic overload tripped; motor current monitoring tripped; single-phase operation on three-phase unit
- Firmware 2.02 and later: All of the above plus: no pump connected; motor current monitoring potentiometer at zero

**Fix steps:**
1. Check the motor overload relay or bimetallic strip — manual reset may be required on the overload
2. Verify motor contactor operation: listen for click on start command; check contactor coil voltage
3. Check rated current setting on the current monitoring potentiometer — if set to zero, the pump will always fault. Set to the pump's rated current from nameplate
4. For firmware 2.02+: verify the pump is connected. The minimum current monitoring detects no pump as a fault
5. Check motor current: clamp-meter on one phase during run. Should be within nameplate FLA

---

## E085 / E141 — Pump Running Time Exceeded

**What it means:** The pump ran continuously for longer than the configured maximum running time. This is a monitoring function to detect system conditions where a pump runs non-stop when it should cycle (e.g., a sump pump running for 4 hours straight may indicate a water ingress problem).

**Fix steps:**
1. Investigate why the pump is running continuously — is there unusual water ingress, a system demand spike, or a failed second pump in a duty/assist configuration?
2. Check that other pumps in the system are operational
3. If the continuous run is normal for the application, increase the running time monitoring limit or disable the monitoring function
4. Manual reset required — cannot auto-reset without investigation

---

## E090 — Float Switch Plausibility Error

**What it means:** The float switches are in an impossible sequence — for example, the high-water float is indicating "wet" while the low-water float is indicating "dry." This cannot be physically correct and indicates wiring error or float failure.

**Fix steps:**
1. Check float switch wiring — verify each float connects to its correct input terminal
2. Manually raise and lower each float to confirm correct operation: low float should switch at low level, high float at high level
3. Replace any float that does not switch at its correct level

---

## E140 — Pump Starts Exceeded

**What it means:** The pump has exceeded the configured maximum number of starts per hour. This protects the motor from overheating due to frequent starting (each motor start generates heat from inrush current).

**Causes:**
- Very short system cycle time causing rapid on/off cycling
- Incorrect switching point settings (e.g., on-level and off-level too close together)
- Failed second pump causing first pump to overwork

**Fix steps:**
1. Check system cycle time — adjust switch-on/switch-off levels to increase time between starts
2. Verify other pumps in parallel systems are running
3. Check for external control signals causing rapid cycling

---

## W572 — Warning: System Pressure

**What it means:** W572 is a warning (not an error) on the Stratos MAXO indicating a system pressure condition — typically that the pump is detecting unusually low or high differential pressure that falls outside expected parameters. The pump continues to run.

**Fix steps:**
1. Check system static pressure — add water to a heating/cooling system or check the expansion vessel charge
2. Verify no air pockets are present in the system — bleed all radiators and high points
3. Check if any isolation valves are partially closed
4. If system pressure checks out and W572 persists, verify the pump's Δp setpoint is appropriate for the installation (accessible via display menu)
5. In Wilo's Stratos MAXO guidance video (resolving E404 and W572), the W572 is often resolved by ensuring the system is fully filled and bled

---

## Faults Without Error Codes

TOP-S and basic Wilo circulation pumps do not have display screens or error codes. Diagnosis is symptom-based:

| Symptom | Possible Cause | Fix |
|---------|---------------|-----|
| Pump connected but does not run; green LED off | Fuse blown; ground fault interrupter tripped; electrical fault | Check/replace fuse. Reset GFCI. Call service if fuse blows repeatedly |
| Pump connected but does not run; green LED on | Undervoltage; winding damage; failed capacitor (single-phase) | Check voltage at terminals. Replace capacitor (1-phase pumps only). Call service for winding fault |
| Pump runs but output too low; green LED on | Foreign body in impeller; wrong rotation direction; shut-off valve not fully open | Disassemble pump head and remove debris. Swap two phases (3-phase) to reverse rotation. Open valves fully |
| Pump noisy; green LED on | Air in pump; cavitation (insufficient suction pressure); foreign body; wrong rotation | Vent pump/system. Increase system feed pressure. Remove debris. Check rotation |
| Pump runs; motor overheating | Pump blocked; ambient too high; motor overloaded | Check impeller for debris. Verify pump is not dead-headed (discharge valve must be open) |

---

## BMS / Building Automation Interface

Wilo Stratos MAXO and Stratos GIGA support multiple BMS protocols:

**Modbus RTU (RS485):**
- Available via the integrated RS485 terminal block or as a plug-in module
- Standard Wilo Modbus address 1 (configurable via display menu)
- Key registers: pump status, setpoint, current speed, current flow rate, fault code
- Refer to Wilo Modbus documentation for full register map

**BACnet MS/TP:**
- Available via optional BACnet module (Wilo-IF-Module BACnet)
- Supports BACnet objects for setpoint control, status, and alarm reporting

**LON (LonWorks):**
- Available via optional LON module
- Supports nviSpeed, nviFlowRequest, and fault reporting network variables

**SSM / SBM Relay (potential-free contacts):**
- SSM (collective fault signal): closes on any active error. Wire to BMS digital input
- SBM (collective run signal): closes when pump is running. Wire to BMS for run confirmation
- Both are potential-free changeover contacts. Configure behavior via display menu:
  - SSM can be configured as normally open or normally closed
  - SBM can indicate "power on," "ready," or "motor running"

**Setting access via display:**
On Stratos MAXO, press and hold the display button to enter the menu. Navigate using the +/− buttons. Menu 4.24 shows the software version. Fault history is accessible in the diagnostics menu. Most BMS configuration is under Menu 5 (inputs/outputs) and Menu 6 (communication).

---

## Reset Procedure

**Stratos MAXO:**
Most errors require a manual reset via the integrated display. Press and hold the button on the display until the error is acknowledged (typically 3 seconds). If the error condition is still present, the error will return immediately after reset.

**Power cycle reset:** Turn off the supply isolator, wait 30 seconds, restore power. This will clear any non-latched faults. Latched faults (E062, E080) require the cause to be resolved and a manual display reset.

**E404 reset after unblocking rotor:** Power cycle only — do not attempt to reset via display while rotor is blocked.

---

## Accessing Menu Mode

On Stratos MAXO:
1. Short press the control button: cycle through setpoint and operating mode display
2. Press and hold 3 seconds: enter main menu
3. Navigate using +/− buttons
4. Confirm selection with button press
5. Menu 4: Device information (software version at Menu 4.24)
6. Menu 5: Configuration (inputs, outputs, monitoring functions)
7. Menu 6: Communication settings (Modbus address, protocol)

For the fault signal assistant and detailed menu descriptions, visit: wilo.com and navigate to Support → Fault Signal Assistant.

---

## Parts Table

| Component | Fits | Part Notes |
|-----------|------|------------|
| **Motor/pump unit (complete)** | Stratos MAXO 25–65 | Stratos MAXO uses a wet-rotor motor integrated with the pump. When E404 indicates electronics failure, the motor/pump assembly is typically replaced as a unit. Order by connection size and max head (e.g., Stratos MAXO 25/0.5–8) |
| **Control board / electronics** | Stratos MAXO | Internal drive electronics. Wilo service part only — not available through standard distribution. Requires Wilo service center |
| **Float switch** | Waste water / drainage models | SPST or SPDT float switch, cable-mounted. Specify cable length and switching level height. Wilo or generic equivalent (e.g., Speroni, FS series) |
| **Level sensor (submersible)** | DrainLift / waste water | Hydrostatic pressure sensor or float switch depending on model. Specify 4–20 mA or switch output |
| **RS485 / Modbus interface module** | Stratos MAXO, Stratos GIGA | Wilo-IF-Module RS485. Plugs into communication slot on motor head |
| **BACnet module** | Stratos MAXO | Wilo-IF-Module BACnet MS/TP. Requires BACnet license activation |
| **Moisture/leakage probe** | Any model with E014 input | Two-wire resistive probe. Wilo accessory part. Used with optional protection relay |
| **Shaft seal kit** | TOP-S, CronoLine, Stratos GIGA | Model-specific mechanical seal. Specify pump model number and connection size. Common suppliers: Roten, Burgmann, AES |
| **Capacitor** | TOP-S single-phase models | CBB60 or MKP capacitor. Specify µF value and voltage from pump nameplate. Standard capacitor — available from electrical suppliers |
| **Terminal box / cover** | Any model | Wilo part. Required if original is damaged or missing — prevents water ingress to electrical connections |

---

## Scheduled Maintenance to Prevent Faults

**Annual (minimum):**
- Verify system pressure and top up if low — low system pressure causes E401 and reduces pump life
- Bleed any air from system — air causes cavitation and can trigger dry-run protection faults
- Check all isolation valves are fully open on both pump suction and discharge
- On waste water pumps: inspect impeller for debris, especially rags and fibrous material

**Every 2–3 years:**
- Lubricate motor bearings on non-wet-rotor models (TOP-S, CronoLine larger frame sizes) — check manual for lubrication specification
- Inspect shaft seal for weeping — early seal weepage is normal on mechanical seals; active dripping requires seal replacement

**After any system work (pipe modifications, chemical dosing):**
- Bleed all high points in the system
- Verify pump setpoint is still appropriate for modified system resistance
- Flush and inspect strainer/filter if installed upstream of pump

## Where to Buy Replacement Parts

Find replacement parts for Wilo pumps on Amazon:

- [Wilo Pump Replacement Parts](https://www.amazon.com/s?k=Wilo+pump+replacement+parts&tag=errorcodefixes-20)
- [Wilo Circulator Pump Seal & Gasket Kit](https://www.amazon.com/s?k=Wilo+circulator+pump+seal+gasket&tag=errorcodefixes-20)
- [Wilo Pump Control Module Replacement](https://www.amazon.com/s?k=Wilo+pump+control+module+replacement&tag=errorcodefixes-20)