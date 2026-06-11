---
title: "Hussmann Refrigeration Case Error Codes — Complete Fix Guide"
description: "Hussmann refrigeration display case error codes for Impact and Quantum series. What each code means and how to fix it."
pubDatetime: 2026-04-27T22:00:00Z
modDatetime: 2026-04-27T22:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - refrigeration
  - hussmann
money_part: "NTC 10K case sensor"
---

Hussmann display cases — the Impact reach-in, Quantum multi-deck, QM Plus, island cases, and NAV series — use integrated case controllers to monitor temperature, manage defrost cycles, and alert technicians to faults. Depending on the case age and configuration, controls range from the simple **Safe-NET III** single-zone controller to the more sophisticated **EPC-1000** and **E*Vue** networked controllers used in large supermarket installations.

This guide covers common Hussmann alarm codes across controller types, what triggers each, and how to diagnose and reset it. Context throughout is supermarket and grocery distribution, where case availability directly affects product loss and compliance with food safety regulations.

---

## Hussmann Controller Overview

Understanding which controller is in your case is the first step:

| Controller | Found On | Interface | Network Capable |
|-----------|----------|-----------|-----------------|
| Safe-NET III | Older Impact reach-in, small cases | LED + 2-digit display | No |
| EPC-1000 | Quantum, mid-range cases | LCD display + keypad | Yes (RS-485) |
| E*Vue | Quantum, Impact multi-deck, island | Backlit LCD, menu-driven | Yes (LAN/BACnet) |
| NAV Series | Current production Impact, Quantum | Color touchscreen | Yes |
| MagPak | Self-contained packaged systems | LCD | Yes |

For Safe-NET III, faults display as **E1** or **E2** with LED indicators. For EPC-1000 and E*Vue, fault messages are text strings. For NAV series, alarms appear in a dedicated alarm log screen.

---

## Accessing Fault History

### Safe-NET III
Faults are indicated in real time only — no historical log. Note the LED/code behavior immediately when the alarm activates.

### EPC-1000
1. Press **MENU** on the keypad.
2. Navigate to **ALARMS** → **ALARM LOG**.
3. Active and historical alarms are listed with timestamp.
4. To clear acknowledged alarms: **MENU** → **ALARMS** → **CLEAR ALARMS** (requires supervisor password, default: 1234).

### E*Vue Controller
1. From the main screen, press **ALARMS** tab.
2. All active alarms appear in red; historical cleared alarms in gray.
3. Press individual alarm for detail view (includes sensor ID, first occurrence time, current reading).
4. To acknowledge: press alarm entry → **ACKNOWLEDGE**.
5. To clear: press alarm entry → **CLEAR** (alarm must be resolved first or will immediately re-alarm).

### NAV Series
1. Tap **ALARM** icon (bell) at top of touchscreen.
2. Current alarms list with priority level (Critical / Warning / Info).
3. Tap alarm for detailed diagnostic view.
4. Swipe right to acknowledge, long-press to clear.

---

## Hussmann Alarm Codes — Safe-NET III (LED Display)

### E1 — Case Temperature Sensor Failure

**Display:** E1 + flashing red LED  
**Meaning:** The case air temperature sensor (control sensor, Pb1) has failed or is disconnected. The controller cannot read case temperature.

**Controller response:** Depending on Safe-NET III configuration:
- Refrigeration runs continuously (fail-safe mode)
- Refrigeration turns off (fail-safe protect mode)
- Duty cycle operation (compressor cycles on/off on fixed timer)

**Causes:**
1. Sensor probe shorted or open circuit
2. Sensor wiring connector corroded or disconnected at controller
3. Sensor physically displaced from mount position inside case

**Diagnosis:**
1. Measure sensor resistance at controller terminal: NTC sensors typically read 10 kΩ at 25°C / 77°F. Open circuit (OL) = failed. Near-zero = shorted.
2. Inspect sensor wire path for damage from cleaning water or impact.
3. Verify sensor is located correctly in the return air path — not touching the evaporator coil or stored product.

**Fix:**
1. Replace case temperature sensor (NTC 10K type — verify against case wiring diagram).
2. Re-run sensor wire through the original path away from drip zone and door gaskets.
3. After replacement: observe case temperature on display to confirm sensor reads correctly for 30 minutes before clearing alarm.

---

### E2 — Evaporator Temperature Sensor Failure

**Display:** E2 + flashing red LED  
**Meaning:** The evaporator coil temperature sensor (Pb2, defrost termination sensor) has failed.

**Significance:** The evaporator sensor is what the controller uses to terminate a defrost cycle — when it reads ≥55°F (13°C), defrost heaters are switched off. Without this sensor, the controller cannot end defrost by temperature, causing one of two failure modes:
- **Defrost runs on time only:** Risk of overlong defrost, product warming.
- **Defrost lockout:** Case refuses to defrost, causing progressive frost buildup.

**Causes:**
1. Evaporator sensor cable chafed on coil fins (common — fins are sharp)
2. Sensor lead damaged by repeated freeze/thaw cycling
3. Sensor cable compressed under evaporator cover during service

**Diagnosis:**
1. With case powered, check for E2 on display.
2. Measure sensor resistance at controller P2 terminals: same NTC profile as case sensor.
3. Inspect sensor location — it should clip to the evaporator coil fins at the manufacturer-specified position (typically mid-coil).

**Fix:**
1. Replace sensor. Use manufacturer-specified sensor or equivalent NTC 10K with stainless sheath rated for low-temperature use.
2. Re-secure sensor to coil with the original clip, not cable ties (cable ties can be cut by ice).
3. Route lead to avoid contact with coil fins. Use foam sleeve where necessary.

---

### Red LED Solid at Startup — Firmware Fault

**Display:** Solid red LED immediately on power-up  
**Meaning:** Controller firmware has corrupted. Controller is not operating.

**Fix:**
1. Power cycle controller. If LED returns immediately to solid red: firmware failure confirmed.
2. Controller replacement required. Do not attempt to reprogram Safe-NET III — it is not field-programmable.
3. Before replacement: document current settings (temperature setpoint, defrost schedule, fan delay) from the case configuration label inside the case door frame.

---

### Red LED On During Operation — Temperature Alarm

**Display:** Solid red LED (no E code)  
**Meaning:** Case temperature is outside the configured alarm band — either too warm or too cold.

**Causes (too warm):**
1. Door left open or door gasket damaged
2. Evaporator coil iced over (blocked airflow)
3. Refrigeration system fault (loss of refrigerant, condenser dirty, compressor fault)
4. Defrost frequency too low — ice accumulation

**Causes (too cold):**
1. Temperature setpoint too low
2. Refrigerant overcharge
3. Expansion valve hunting

**Fix steps — Too warm:**
1. Check door seal integrity — run hand around perimeter of closed door. Air movement = bad gasket.
2. Inspect evaporator coil through the fan-access panel: heavy frost/ice = defrost problem.
3. Initiate manual defrost via controller: hold the **DEF** button (if present) or navigate to **MANUAL DEFROST** in menu. After defrost completes, monitor case temperature.
4. If case does not cool after manual defrost: refrigeration system issue — escalate to refrigeration technician.

---

## EPC-1000 and E*Vue Text Alarm Codes

### T-STAT FAIL / DEFROST TERM FAIL — Defrost Termination Thermostat Fault

**Display:** T-STAT FAIL or DEFROST TERM FAIL  
**Meaning:** The mechanical defrost termination thermostat (snap-disc type, typically set to open at 55°F/13°C on coil) has failed open or is not responding.

**Causes:**
1. Snap-disc thermostat failed in open position — contacts never close, defrost can't confirm termination
2. Thermostat clip loose — thermostat not contacting coil surface
3. Wiring from thermostat to controller broken

**Diagnosis:**
1. With case in defrost and evaporator above setpoint, measure continuity across thermostat terminals: closed = good; open (OL) = failed.
2. For EPC-1000: navigate to **DIAGNOSTICS** → **INPUT STATUS** to view defrost termination input state in real time.

**Fix:**
1. Replace snap-disc thermostat. Use the correct temperature rating for the case (low-temp cases use higher rating snap-discs).
2. Clip replacement thermostat firmly to coil body at the factory-specified location (typically marked with a sticker inside the evaporator housing).
3. Manual defrost after repair to verify controller terminates correctly.

---

### HTR FAIL / DEFROST HEATER FAIL — Defrost Heater Fault

**Display:** HTR FAIL or DEFROST HEATER FAIL  
**Meaning:** The controller attempted to run a defrost cycle and detected that the heater circuit is open — no current draw from the defrost heater.

**Causes:**
1. Defrost heater element burned out (open filament)
2. Heater wiring fuse blown (inline fuse in heater circuit)
3. Wiring from controller to heater disconnected
4. Heater contactor or relay failed (on large multi-deck cases with external heater contactors)

**Diagnosis:**
1. **Isolate power to the case before testing heaters.**
2. Disconnect heater leads and measure resistance: typical glass tubular defrost heaters read 10–50 Ω depending on wattage. Open circuit = burned out.
3. Check inline fuse in heater circuit (if fitted) — typically 15A or 20A ceramic fuse in a fuse holder near the case controller.
4. For multi-deck cases with multiple heater circuits: test each circuit independently. Individual section heaters can fail while others remain good.

**Fix:**
1. Replace burned-out heater element. Match wattage, voltage, and length to original specification.
2. After replacement: run manual defrost cycle and verify heater current draw with a clamp meter. Verify defrost terminates within expected time (typically 20–45 minutes depending on frost load).

---

### FAN FAIL / EVAP FAN FAIL — Evaporator Fan Motor Fault

**Display:** FAN FAIL or EVAP FAN FAULT  
**Meaning:** The evaporator fan motor(s) are not running when commanded, or a fan monitoring circuit detected stalled fan(s).

**Causes:**
1. Fan motor bearing seized (common after prolonged operation)
2. Fan blade jammed with ice or debris
3. Motor capacitor failed (shaded-pole motors do not use capacitors, but PSC motors do)
4. Fan motor winding burned out
5. Fan delay relay failed

**Diagnosis:**
1. During normal operation (not defrost), fan blades should be visible spinning through the evaporator access panel.
2. Listen for grinding or humming without rotation — bearing failure or jammed blade.
3. Measure motor winding resistance and run capacitor value (if PSC type).
4. Check fan delay relay — after defrost, fans are delayed 3–5 minutes on low-temp cases to prevent warm moist air from blowing onto coil.

**Fix:**
1. Replace stalled or failed fan motor. Document blade diameter, motor frame size, and airflow direction (arrow on motor housing) before removal.
2. For evaporator fan delay issues: verify relay operation by shorting contacts temporarily — if fans run, relay coil or contacts have failed.
3. After replacement: observe multiple defrost cycles to confirm fans restart correctly post-defrost.

---

### TEMP ALARM / PRODUCT TEMP ALARM — Product Temperature Exceeded

**Display:** TEMP ALARM or HI TEMP ALARM  
**Meaning:** Case product temperature (measured by case air sensor or secondary product probe) has exceeded the high-temperature alarm setpoint. On food safety-critical cases, this alarm may also transmit to store monitoring systems.

**Response protocol (supermarket context):**
1. Check actual product temperature with a calibrated probe thermometer — not just the case display.
2. Document temperature and time of alarm for food safety records.
3. Identify cause before resetting alarm.

**Common causes:**
1. Recent restocking with warm product
2. Door left open or poor door seal
3. Heavy frost on evaporator coil
4. After-hours store temperature rise (HVAC shutdown)
5. Refrigeration system fault

**Fix:**
1. For post-restocking alarms: allow 1–2 hours for case to recover. Acknowledge alarm. If temperature does not recover to setpoint within 2 hours, investigate refrigeration system.
2. For recurring daily alarms at same time: check defrost schedule — defrost cycle may be too long, or high-temperature alarm threshold may be too close to defrost peak.

---

### DOOR ALARM / DOOR OPEN — Door Open or Switch Fault

**Display:** DOOR ALARM or DOOR OPEN  
**Meaning:** The door position switch is indicating the door has been open beyond the configured time threshold (typically 30–120 seconds).

**Causes:**
1. Door actually open (restocking operation)
2. Door switch (magnetic reed switch or mechanical switch) failed in open position
3. Door not fully closing — hinge adjustment, warped door, gasket preventing full closure

**Fix:**
1. Confirm door is physically closed. Magnetic door gaskets should snap firmly to case frame.
2. Test door switch: on E*Vue, navigate to **DIAGNOSTICS** → **I/O STATUS** → **DOOR SWITCH** — should show CLOSED when door is closed.
3. Test switch with magnet (reed switch) or depress switch plunger manually: if alarm clears, switch position or door alignment is the issue.
4. Adjust door hinges if door does not close squarely. Hussmann Impact cases have field-adjustable hinge brackets.

---

### CASE CTLR COMM FAIL / CONTROLLER COMMUNICATION FAULT

**Display:** CASE CTLR COMM FAIL or COM FAULT  
**Meaning:** The store energy management system (EMS) or E*Vue network controller has lost communication with one or more case controllers on the RS-485 or LAN bus.

**Causes:**
1. RS-485 bus wiring break or loose termination
2. Case controller address conflict (duplicate address on network)
3. Controller powered off or locked up
4. Network termination resistor missing at end of RS-485 bus run

**Diagnosis:**
1. Verify the affected case controller is powered and displaying normally.
2. Check RS-485 bus wiring at the affected case — A and B terminals for correct polarity.
3. For E*Vue networked systems: the store controller network map shows each case with communication status. Identify which cases are on the same bus segment.
4. Check for duplicate controller addresses — each case controller must have a unique network address (set via DIP switches or menu on EPC-1000/E*Vue).

**Fix:**
1. Re-seat RS-485 wiring terminals at case controller.
2. If multiple consecutive cases are offline: check bus termination and mid-run splice points.
3. For address conflict: power down conflicting controllers, reassign addresses sequentially, power back up.

---

### DRAIN FAULT / DRAIN BLOCKED — Condensate Drain Fault

**Display:** DRAIN FAULT (on NAV series and some E*Vue configurations)  
**Meaning:** Condensate drain is not clearing — drain heater failure, blockage, or drain pan overflow sensor triggered.

**Causes:**
1. Drain heater burned out — drain freezes in low-temperature cases
2. Drain line blocked with debris, slime, or ice
3. Drain pan float switch triggered (overflow)

**Fix:**
1. Check drain heater continuity (same procedure as defrost heater — measure resistance with power isolated).
2. Flush drain line with warm water. Use drain cleaning brush on gravity-drain models.
3. Verify drain heater is energised correctly — it should run continuously on low-temperature cases to keep drain from freezing.

---

## Manual Defrost and Reset

- **Safe-NET III:** Hold **DEF** for 3 seconds if fitted, or power-cycle the case.
- **EPC-1000:** **MENU** → **DEFROST** → **MANUAL DEFROST**, and **MENU** → **SYSTEM** → **RESTART CONTROLLER**.
- **E*Vue:** Use the **CASE CONTROL** page for manual defrost and **SETTINGS** → **SYSTEM** → **RESTART** for a soft reset.
- **NAV Series:** Open the case page, choose **FORCE DEFROST**, then use **SETTINGS** → **SYSTEM** → **SOFT RESTART** if needed.

---

## Parts Reference Table

| Part | Application |
|------|------------|
| NTC 10K case sensor | Impact, Quantum, NAV |
| Evaporator sensor | Low and medium temp cases |
| Defrost heater element | Reach-in and multi-deck cases |
| Evaporator fan motor | Impact and Quantum |
| Drain heater | Low-temp cases |
| Safe-NET III, EPC-1000, E*Vue controller | Match controller and firmware to the case |

Source parts through Hussmann distributors or commercial refrigeration parts suppliers.

## Where to Buy Replacement Parts

Find replacement parts for Hussmann refrigeration systems on Amazon:

- [Hussmann Refrigeration Parts](https://www.amazon.com/s?ascsubtag=ecf-hussmann-refrigeration-error-codes&k=Hussmann+refrigeration+parts&tag=errorcodefixes-20)
- [Commercial Refrigeration Case Drain Heater](https://www.amazon.com/s?ascsubtag=ecf-hussmann-refrigeration-error-codes&k=commercial+refrigeration+case+drain+heater&tag=errorcodefixes-20)
- [Commercial Display Case Evaporator Fan Motor](https://www.amazon.com/dp/B01N0J3ZEH?ascsubtag=ecf-hussmann-refrigeration-error-codes&tag=errorcodefixes-20)