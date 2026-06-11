---
title: "Laars Boiler Fault Codes — Complete Fix Guide"
description: "Laars boiler fault codes for Laars Mighty Therm, Pennant, and NeoTherm series. What each code means and how to fix it."
pubDatetime: 2026-04-27T23:00:00Z
modDatetime: 2026-04-27T23:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - boiler
  - laars
money_part: "Hot surface igniter"
---

Laars boilers — the Mighty Therm 2, Pennant hydronic boilers, and NeoTherm NTH/NTHN modulating series — all use different control systems. The Mighty Therm 2 and Pennant use a Honeywell S8600 or similar ignition control with LED flash codes. The NeoTherm NTH uses a dedicated touchscreen controller (or EMEA display on newer units) that shows numbered fault codes in an orange bar at the bottom of the screen. This guide covers all three platforms.

## Understanding the Two Platforms

| Platform | Display Type | Code Format |
|---|---|---|
| NeoTherm NTH / NTHN (080–1000 MBH) | Touchscreen or EMEA digital display | Numbered codes 1–200+ in orange bar |
| Mighty Therm 2 | LED indicator lights (L1/L2/L3) + flash codes | Flash sequence on indicator LED |
| Pennant (PNCH/PNCV) | Single LED + optional ignition control display | LED flash patterns + lockout light |

On the NeoTherm, faults are either **Holds** (H) or **Lockouts** (L):
- **Hold**: The boiler pauses firing but will automatically retry once the condition clears. No manual reset required.
- **Lockout**: The boiler stops and requires a manual reset to restart. Repeated lockouts indicate a persistent fault.

---

## NeoTherm NTH Fault Codes

### Resetting the NeoTherm
To reset after a Lockout:
1. Press and hold the **RESET** button on the touchscreen for 3 seconds
2. On EMEA display models: press the dedicated reset button next to the display
3. If the fault returns within 3 ignition attempts, do not keep resetting — investigate the root cause

### Codes 1–10: Internal Controller Faults

These codes indicate a problem with the controller module itself, not with the external boiler components. Always reset first — if the code returns, replace the ignition module.

| Code | Description | Hold/Lockout | Action |
|---|---|---|---|
| 1 | Unconfigured safety data | Lockout | New device needs setup and safety verification; replace if repeats |
| 2 | Waiting for safety data verification | Lockout | Re-enter configuration, verify safety params, reset to complete |
| 3 | Internal fault: Hardware fault | Hold | Reset module; replace if repeats |
| 4 | Internal fault: Safety relay key feedback error | Hold | Reset module; replace if repeats |
| 5 | Internal fault: Unstable power (DC/DC output) | Hold | Check 24V power supply to module; replace if repeats |
| 6 | Internal fault: Invalid processor clock | Hold | Reset module; replace if repeats |
| 7 | Internal fault: Safety relay drive error | Hold | Reset module; replace if repeats |
| 8 | Internal fault: Zero crossing not detected | Hold | Check line voltage to controller; replace module if repeats |
| 9 | Internal fault: Flame bias out of range | Hold | Inspect flame sensor and wiring; replace module if repeats |
| 10 | Internal fault: Invalid burner control state | Lockout | Reset module; replace if repeats |

---

### Code 110 / 111 — High Limit Tripped

**Display:** "HIGH LIMIT FAULT" or similar text with code 110 or 111

**Meaning:** The supply water temperature exceeded the manual reset high limit setting (typically 210°F / 99°C on heating boilers). The boiler will not restart until the high limit is manually reset AND the condition that caused overheating is corrected.

**Causes (in order of likelihood):**
1. No or insufficient water flow through the boiler — pump failure, closed isolation valve, air-locked system
2. Heat demand is satisfied but boiler kept firing — outdoor reset or setpoint issue
3. High limit aquastat set too low for the application
4. Heat exchanger fouled with scale (restricts heat transfer, causes localized overheating)
5. Circulator pump impeller clogged with debris

**Diagnosis Steps:**
1. Let the boiler cool to below 160°F (71°C) before attempting reset
2. Check water flow: open all isolation valves, verify circulator pump is running and producing flow
3. Feel the supply and return piping — both should be warm, not supply hot/return cold
4. Check system pressure gauge: should read 12–25 PSI on a closed loop residential/light commercial system
5. Check pump operation by listening for it and feeling for vibration

**Fix:**
1. Restore water flow (open valves, bleed air from system, repair or replace pump)
2. Press the manual reset button on the high limit aquastat (typically on the front of the boiler, requires pressing with a screwdriver or pen)
3. Increase high limit setpoint if it was factory-set too low for the application
4. Descale heat exchanger if water hardness has caused scaling

> **Manual reset location on NeoTherm:** The high limit aquastat reset button is typically accessible through a small access panel on the front or side of the boiler. Check the installation manual for your specific model.

---

### Code 115 / 116 — Low Water Pressure

**Display:** "LOW WATER PRESSURE" or "PRESSURE FAULT"

**Meaning:** System water pressure dropped below the minimum threshold (typically 5–10 PSI depending on configuration). The boiler will not fire below this threshold to prevent dry-fire damage to the heat exchanger.

**Causes (in order of likelihood):**
1. Water leak in the system — check visible piping and fittings
2. Expansion tank failed or waterlogged (causes pressure relief valve to open repeatedly)
3. Pressure relief valve weeping or open, discharging water
4. Auto-fill valve (feed valve) closed or failed on systems with make-up water
5. Recent service work with system drained and not fully refilled

**Diagnosis Steps:**
1. Check the pressure gauge — a reading below 10 PSI on a cold system indicates low fill
2. Look for wet spots under the boiler or along piping
3. Check the pressure relief valve outlet (may be piped to a floor drain) — is water dripping?
4. Locate the expansion tank (usually near the boiler) — if it feels full of water (heavy, no air cushion), it is waterlogged

**Fix:**
1. Locate and repair any leaks
2. Re-pressurize the system via the make-up water valve or manual fill valve to 12–15 PSI cold
3. If expansion tank is waterlogged: drain and re-pressurize it to the correct pre-charge (typically 12 PSI air, set with a bicycle pump) or replace the tank
4. If the PRV keeps opening: the cause is expansion tank failure, not an excess pressure condition

---

### Code 120 / 121 — Ignition Lockout (Flame Failure)

**Display:** "IGNITION LOCKOUT" or "FLAME FAILURE" — this is the most common fault on all Laars boilers

**Meaning:** The boiler attempted to light and either:
- The igniter never produced a flame, or
- A flame was detected but then lost within the trial-for-ignition period, or
- The flame rod detected no flame during the trial period

**Causes (in order of likelihood):**
1. Dirty or failed flame sensor (flame rod) — most common cause
2. Gas supply interrupted or insufficient pressure
3. Failed igniter (cracked, high resistance, or open circuit)
4. Gas valve not opening (failed coil, wiring issue, or no 24V signal)
5. Air in gas line after a gas outage (needs to purge)
6. Blocked vent or air intake (pressure switch not allowing trial)
7. Failed control board or ignition module

**Diagnosis Steps:**
1. Confirm gas is on: check other gas appliances in the building
2. Attempt a manual reset and watch/listen for the ignition sequence:
   - You should hear the blower start (pre-purge)
   - Then a click (spark igniter) or a glow (hot surface igniter)
   - Then gas valve open (faint hiss)
   - Then flame
3. If no spark: test igniter resistance — hot surface igniter should read 40–100 Ω cold; open circuit = failed
4. If spark present but no flame: gas supply issue or gas valve
5. If flame lights but then shuts off: dirty flame sensor — clean with fine steel wool or emery cloth (do not use sandpaper)

**Flame Sensor Cleaning Procedure:**
1. Turn off power to the boiler
2. Locate the flame sensor rod (a metal rod positioned in the burner flame path, connected by a single wire)
3. Remove the single wire connection
4. Unscrew the flame sensor mounting screws (typically two screws)
5. Lightly abrade the rod with fine steel wool or emery cloth — remove any white oxide buildup
6. Reinstall and test

**Reset After Ignition Lockout:**
1. Press and hold RESET for 3 seconds on the touchscreen
2. The boiler will attempt a complete new ignition sequence
3. After three successive lockouts, the control typically enters a hard lockout requiring a power cycle (turn off the breaker for 30 seconds, then back on)

---

### Code 125 — Flue Gas / Combustion Sensor Fault

**Display:** "FLUE SENSOR FAULT" or "HIGH FLUE TEMPERATURE"

**Meaning:** Either the flue gas temperature sensor has detected excessive exhaust temperature, or the sensor itself has failed (open or short circuit).

**Causes:**
1. Condensate drain blocked on condensing models (causes flue gas temp to rise)
2. Flue sensor failed — resistance out of normal range
3. Scale buildup on heat exchanger causing poor heat transfer (flue gas exits hot because it couldn't transfer heat to water)
4. Restricted flue — partial blockage causing hot gas to back up

**Diagnosis Steps:**
1. Check flue sensor resistance at the connector — normal range varies by model; compare to the specification in the service manual
2. Inspect the condensate drain if the NeoTherm is a condensing model — clear any blockage
3. Inspect flue termination for bird nests, ice, or other blockages

**Fix:** Replace flue sensor if out of specification. Clear condensate drain.

---

### Code 128 / 130 — Gas Valve Fault

**Display:** "GAS VALVE FAULT" or "GAS VALVE OPEN TOO LONG"

**Meaning:** The control has detected an anomaly in the gas valve circuit — either the valve didn't respond correctly to an open/close command, or the valve was commanded closed but residual flame was still detected.

**Causes:**
1. Gas valve coil failed (open or short circuit)
2. Wiring connection issue at the gas valve
3. Gas valve stuck open (rare but dangerous — evacuate and call gas company)
4. 24V control signal not reaching the valve

**Fix:**
- Test 24V signal at gas valve coil terminals during call-for-heat
- Measure coil resistance: typically 40–100 Ω for most 24V gas valves; open circuit means failed coil
- If coil tests good but valve won't open: replace gas valve
- If flame detected after valve commanded closed: replace gas valve immediately — do not bypass or override

> **Parts needed:** Gas valve (Honeywell VR8200A or equivalent, model-specific), gas valve coil kit

---

### Code 135 / 136 — Flow Switch Fault

**Display:** "FLOW SWITCH FAULT" or "NO FLOW DETECTED"

**Meaning:** The flow switch in the boiler water circuit did not confirm water flow within the required time after the circulator pump started.

**Causes (in order of likelihood):**
1. System pump not running or running backwards (new pump installation with reversed wiring)
2. Flow switch stuck closed (debris fouling the paddle)
3. Flow switch wiring disconnected
4. Insufficient flow for switch to activate — minimum GPM not being met
5. Flow switch failed

**Diagnosis Steps:**
1. Confirm the circulator pump is running: listen for it, feel for vibration on the pump body
2. Locate the flow switch (typically a paddle-type switch in the supply piping near the boiler outlet)
3. With the pump running, the paddle should deflect and close the switch contacts — test with a DMM across the switch terminals (should read closed = near 0 Ω when pump is running)
4. If the pump is running and switch is closed but the fault persists: check wiring to the boiler control board

**Fix:**
- Clean debris from flow switch paddle
- Replace flow switch if failed
- Verify pump wiring and rotation direction

> **Parts needed:** Paddle-type flow switch (McDonnell Miller or Taco FS series, match the pipe size)

---

### Code 140 / 141 — Temperature Sensor Fault

**Display:** "SUPPLY SENSOR FAULT," "RETURN SENSOR FAULT," or "OUTLET SENSOR OPEN/SHORT"

**Meaning:** A temperature sensor input is reading outside the expected range — either open circuit (infinite resistance), short circuit (near-zero resistance), or out of calibration range.

**Sensor types used on NeoTherm:**
- Supply/outlet sensor: 10kΩ NTC thermistor at 77°F (25°C)
- Return sensor: same type
- Outdoor reset sensor: same type (if outdoor reset is being used)

**Diagnosis Steps:**
1. Disconnect the sensor connector at the boiler control board
2. Measure sensor resistance with a DMM:
   - At 77°F (25°C): should read approximately 10,000 Ω
   - At 140°F (60°C): should read approximately 2,500 Ω
   - At 200°F (93°C): should read approximately 900 Ω
3. If reading is ∞ (open) or 0 (short): sensor failed
4. If reading is reasonable: suspect wiring or control board

**Fix:** Replace the failed sensor. Use the correct replacement for your NTH model — the sensors are not universally interchangeable across Laars models.

---

## Mighty Therm 2 Fault Diagnosis

The Mighty Therm 2 uses a Honeywell S8610U integrated ignition control. Faults display as LED flash patterns on the ignition control board.

### LED Indicator System

The Mighty Therm 2 has three LED indicators (L1, L2, L3) on the control board:
- During normal startup, L1, L2, and L3 light sequentially
- If the sequence stops at L3 and flashes: the boiler is in ignition lockout

| Flash Pattern | Meaning |
|---|---|
| L3 stays on steady | Normal operation, boiler firing |
| L3 flashes 2 times, pause, repeat | Flame sensor (signal) fault |
| L3 flashes 3 times, pause, repeat | Ignition lockout (no flame established) |
| L3 flashes 4 times, pause, repeat | High limit tripped |
| L3 flashes 5 times, pause, repeat | Draft pressure switch fault |
| L3 flashes 7 times, pause, repeat | Low gas pressure switch fault |
| Solid red LED on control | Internal control fault — replace control |
| No LEDs lit | No power to control or blown fuse |

### Mighty Therm 2 Ignition Lockout Reset

1. Turn the main power switch OFF
2. Wait 30 seconds
3. Turn power back ON
4. The boiler will attempt a fresh ignition sequence

If the lockout recurs after 3 attempts, the control goes to hard lockout — a power cycle is required.

### Igniter Testing — Mighty Therm 2

The Mighty Therm 2 uses a hot surface igniter (HSI). To test:
1. Shut off the gas supply at the shutoff valve
2. Call for heat and observe whether the igniter glows orange/white hot
3. If no glow: check for 120VAC at the igniter leads during the trial — no voltage means control failure
4. If voltage present but no glow: igniter failed — measure resistance (40–100 Ω acceptable; >200 Ω indicates failure)

> **Parts needed:** Hot surface igniter (Laars part H0318600 or equivalent 120V HSI, silicon carbide)

---

## Pennant Boiler Fault Diagnosis

The Pennant (PNCH/PNCV) uses a Honeywell S8600 ignition control. Common faults:

### Pennant Ignition Lockout

The Pennant control board flashes a red lockout LED when the boiler fails to light after the ignition trial period.

**Reset Procedure:**
1. Press and hold the LOCKOUT RESET button on the control board for 1 second
2. The boiler will retry ignition
3. After 3 lockouts in sequence: turn off the main power switch for 1 minute before trying again

### Pennant High Limit — Manual Reset

The Pennant uses a MANUAL reset high limit control (unlike some boilers with auto-reset). Once tripped, the boiler will not fire again until the button is physically pressed.

**Location:** The manual reset high limit is on the hot water supply header, typically mounted with a red or white reset button visible on the front of the boiler.

**To reset:**
1. Allow the boiler water temperature to drop below the limit setpoint
2. Press the reset button firmly until you feel/hear it click

If the high limit trips repeatedly without apparent cause, suspect low water flow — check the circulator pump first.

### Pennant Draft Pressure Switch

The Pennant has a blocked vent pressure switch. If the switch is tripped (contacts open), the control will not allow ignition. Causes:
- Blocked flue (most common)
- Pressure switch failed with contacts open
- Tubing to the pressure switch cracked or disconnected
- Condensate in the pressure switch tubing (on installations where condensation forms)

**Test:** With the blower running (pre-purge), use a DMM to verify the pressure switch contacts close. If they don't close with good blower operation and an unblocked flue, the switch itself may have failed.

---

## Service Diagnostics Access — NeoTherm

### Accessing Service Mode (NeoTherm Touchscreen)
1. Press **MENU** on the touchscreen
2. Navigate to **Diagnostics** or **Service** menu
3. Live readings available: supply temperature, return temperature, flue gas temperature, flame signal (μA), gas valve state, pump state

### Accessing Fault History
1. From the touchscreen: **MENU → History → Fault Log**
2. Last 10–20 faults stored with timestamps
3. Export available via the Modbus RTU port on commercial installations

---

## Parts Reference Table

| Part | Application | Notes |
|---|---|---|
| Hot surface igniter | Mighty Therm 2, Pennant | Silicon carbide, 120V; check resistance 40–100 Ω cold |
| Flame sensor rod | All Laars models | Single-wire ionization rod; clean before replacing |
| High limit aquastat (manual reset) | All Laars models | Set to 210°F for heating, 200°F for water heaters |
| Gas valve (24V) | All Laars models | Honeywell VR8200 or model-specific; measure coil resistance |
| Flow switch (paddle type) | NeoTherm, Pennant | Match to pipe size (3/4" or 1"); typically SPDT paddle |
| NTC thermistor (10kΩ) | NeoTherm supply/return sensors | Model-specific; verify pin configuration |
| Ignition control module | Mighty Therm 2, Pennant | S8600/S8610 series Honeywell |
| Pressure relief valve | All Laars models | 30 PSI standard; replace when PRV is dripping |
| Expansion tank | All Laars closed-loop systems | Match to system volume; pre-charge to static fill pressure |
| Circulator pump | All Laars systems | Taco 00 series or equivalent; match GPM and head |

---

## Maintenance Schedule

| Task | Interval | Notes |
|---|---|---|
| Test flow switch operation | Annually | Verify switch closes under normal flow |
| Test high limit aquastat | Annually | Manually trip and verify lockout |
| Inspect/clean flame sensor | Annually | Fine steel wool; avoid oil from hands |
| Check system pressure | Monthly | Cold fill pressure: 12–15 PSI |
| Check expansion tank pre-charge | Annually | Should match cold fill pressure |
| Test pressure relief valve | Annually | Lift lever briefly; replace if leaking after test |
| Inspect flue and vent | Annually | Look for corrosion, blockage, animal nests |
| Check igniter resistance | Every 2 years or at annual service | >200 Ω means replace before failure |
| Flush heat exchanger (hard water areas) | Every 3–5 years | Scale reduces efficiency and causes high limit trips |

---

## Quick Fault Reference

| Symptom | First Code to Check | Likely Cause |
|---|---|---|
| No ignition, 3 attempts then lockout | Code 120 / L3 × 3 flashes | Flame sensor dirty or gas supply issue |
| Won't fire, overheat condition | Code 110 / L3 × 4 flashes | High limit tripped, check water flow |
| Low pressure alarm | Code 115 | System leak or waterlogged expansion tank |
| Short cycling, shuts off quickly | Code 120 / flame signal fault | Dirty flame sensor |
| No water flow detected | Code 135 | Pump failure or closed isolation valve |
| Sensor reading out of range | Code 140 | NTC thermistor open or short; check wiring |
| Gas valve won't open | Code 128 | 24V to valve, coil resistance check |
| Control codes 1–10 | Internal fault | Reset; replace module if repeats |

If the boiler shows the same lockout code repeatedly after resetting, stop cycling the reset button. Multiple resets without addressing the root cause can mask the fault and delay correct diagnosis.

## Where to Buy Replacement Parts

Find replacement parts for Laars boilers on Amazon:

- [Laars Boiler Parts & Accessories](https://www.amazon.com/s?ascsubtag=ecf-laars-boiler-fault-codes&k=Laars+boiler+parts&tag=errorcodefixes-20)
- [Laars Ignition Control Module Replacement](https://www.amazon.com/s?ascsubtag=ecf-laars-boiler-fault-codes&k=Laars+ignition+control+module+replacement&tag=errorcodefixes-20)
- [Laars Gas Valve Replacement](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-laars-boiler-fault-codes&tag=errorcodefixes-20)