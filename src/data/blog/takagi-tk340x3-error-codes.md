---
title: "Takagi TK-340X3-NIH Commercial Tankless Water Heater Error Codes"
description: "Complete fault code reference for the Takagi TK-340X3-NIH condensing commercial tankless water heater, covering all error codes, condensate neutralizer faults, secondary heat exchanger diagnostics, and step-by-step repair procedures."
pubDatetime: 2026-04-25T00:00:00Z
author: "James Rutherford"
tags:
  - hvac
  - error-codes
---

The Takagi TK-340X3-NIH is a commercial-grade condensing tankless water heater producing up to 340,000 BTU/hr — capable of serving large apartment buildings, hotels, and commercial facilities. Its condensing design extracts additional heat from flue gases, hitting up to 95% efficiency, but that efficiency comes with added components: a secondary heat exchanger, a condensate neutralizer system, and more sensors than a typical tankless unit. When any of these fault, the unit displays a specific error code and shuts down.

This guide covers every Takagi TK-340X3-NIH error code in detail.

## What Does the Takagi TK-340X3-NIH Error Code Mean?

Each error code on the TK-340X3-NIH identifies the system that forced the heater into protection mode. One code may point to ignition, another to condensate drainage, and another to a sensor on the primary or secondary heat exchanger. These codes matter because a commercial condensing unit can damage itself fast when gas flow, water flow, or condensate drainage falls out of spec.

## How to Read TK-340X3-NIH Error Codes

Error codes display on the front panel digital readout. When a fault occurs, the unit shuts down and shows a two or three-digit number. Some codes require a manual reset; others self-clear when conditions normalize. To reset a manual-lockout fault:

1. Turn the unit off using the power switch
2. Wait 30 seconds
3. Turn the unit back on

If the fault recurs immediately, the underlying condition is still present and must be resolved before the unit will operate.

---

## Takagi TK-340X3-NIH Error Code Reference

### Error 11 — No Ignition (Ignition Failure)
The burner failed to ignite within the ignition trial period. This is one of the most common faults on any gas tankless water heater.

**Causes:**
- No gas supply (closed valve, low gas pressure, empty tank for LP units)
- Igniter electrode fouled or cracked
- Gas valve failure
- Blocked flue preventing proper combustion air flow
- Low inlet water pressure (under 15 PSI)

**Fix:**
1. Verify the gas shutoff valve is fully open
2. Check gas pressure at the unit — minimum inlet pressure is 4" WC for natural gas, 8" WC for LP
3. Inspect the igniter electrodes for carbon buildup or cracking — clean with fine steel wool or replace
4. Check the flue for blockages (bird nests, debris)
5. Verify adequate water flow through the unit before calling for ignition

### Error 12 — Flame Failure (Flame Lost During Operation)
The unit ignited successfully but the flame sensor lost signal during operation. Different from Error 11 (ignition failure) — the burner lit and then went out.

**Causes:**
- Flame sensor (flame rod) fouled with carbon or oxidation
- Gas supply interruption during operation
- Combustion chamber draft problems
- Dirty burner assembly

**Fix:** Clean or replace the flame rod. The flame rod is a metal probe that sits in the burner flame — carbon buildup insulates it and prevents the control board from reading flame presence. Clean with fine steel wool or an emery cloth. If cleaning doesn't resolve it, replace the sensor.

### Error 13 — Abnormal Combustion / Air Intake Issue
The unit detected abnormal combustion conditions, often related to combustion air supply.

**Causes:**
- Recirculated flue gas being drawn into the air intake
- Negative pressure in the equipment room
- Air intake screen blocked (debris, insects, ice)
- Combustion air and exhaust vents too close together

**Fix:** Inspect the air intake screen. Verify that intake and exhaust vent terminations are separated per Takagi's installation requirements (minimum 12" apart on the same wall). In commercial installations, check for negative pressure in the mechanical room — exhaust fans or HVAC equipment can depressurize the space.

### Error 14 — Thermal Fuse Blown
The manual-reset thermal fuse opened. This fuse is a one-time safety device that blows when the unit overheats.

**Causes:**
- Blocked heat exchanger (scale buildup)
- Low water flow through the heat exchanger
- Fan motor failure (insufficient exhaust draft)
- Recirculated flue gases causing overtemperature

**Fix:** The thermal fuse must be physically replaced — it does not self-reset. Locate the fuse on the heat exchanger body. Before replacing, identify and fix the root cause of overheating, or the new fuse will blow again. Descale the heat exchanger if scale buildup is the cause.

### Error 16 — Hot Water Outlet Overtemperature
The outlet temperature sensor detected water temperature above the safety threshold (typically above 203°F).

**Causes:**
- Low water flow rate triggering excessive temperature rise
- Temperature setpoint set too high combined with low demand
- Outlet temperature sensor failure (reading falsely high)
- Broken temperature limiting valve

**Fix:**
1. Verify the minimum flow rate is being met — check all open fixtures
2. Check the outlet temperature sensor resistance
3. Lower the temperature setpoint if set above 140°F
4. If the fault appears with normal flow, the sensor may have failed

### Error 19 — Flame Rod Circuit Fault
The flame rod circuit detected an abnormal electrical condition (not just carbon fouling).

**Fix:** This error often indicates a wiring problem in the flame sensor circuit or a cracked insulator on the flame rod. Inspect the flame rod ceramic insulator — cracks allow the electrode to short to ground. Replace the flame rod assembly if cracked.

### Error 31 — Inlet Thermistor Failure
The cold water inlet temperature sensor has failed or is reading out of range.

**Fix:** Locate the inlet thermistor (typically a clip-on or immersion sensor on the cold water inlet pipe). Disconnect and measure resistance — at 68°F (20°C), most NTC sensors read approximately 10kΩ. Replace if out of spec.

### Error 32 — Outlet Thermistor Failure
The hot water outlet temperature sensor has failed.

**Fix:** Same procedure as Error 31, applied to the outlet thermistor. These sensors are typically interchangeable — verify part compatibility with the TK-340X3-NIH service manual.

### Error 33 — Heat Exchanger Thermistor Failure
The primary heat exchanger temperature sensor failed.

**Fix:** This sensor is embedded in or adjacent to the primary heat exchanger. Replacement requires partial disassembly of the unit. Verify sensor resistance before ordering parts — a disconnected plug is a common cause of this code.

### Error 41 — Exhaust Fan / Combustion Fan Fault
The combustion air fan failed to reach the required RPM or the fan speed sensor detected an abnormal condition.

**Causes:**
- Fan motor bearing failure
- Fan blade blocked or damaged
- Fan speed sensor failure
- Control board output failure

**Fix:** Test the fan motor for free rotation — bearings should spin smoothly with no grinding. Check that the fan blade isn't blocked by debris. If the motor runs but slowly, the motor winding may be degrading — replacement is the fix.

### Error 51 — Gas Valve Fault
The gas valve actuator circuit detected an abnormal condition or the valve failed to operate as commanded.

**Fix:** This usually requires a gas valve replacement. Verify 24VAC supply voltage to the valve before condemning it. A failed valve solenoid coil will show open resistance — test with a multimeter.

### Error 61 — Combustion Fan Motor Fault (Persistent)
Similar to Error 41 but indicates a persistent or hard fan failure versus a transient event.

**Fix:** Fan motor replacement.

### Error 65 — Water Flow Sensor Fault
The water flow sensor (turbine) failed or is producing an out-of-range signal.

**Causes:**
- Debris in the flow sensor
- Sensor bearing seized
- Control board input failure

**Fix:** Remove and clean the flow sensor turbine — hard water deposits are a common cause of turbine seizure. If cleaning doesn't restore function, replace the sensor.

### Error 71 — Gas Ignition Control Board Fault
The gas ignition module detected an internal fault. Usually a board replacement is required.

**Fix:** Check all wiring connections to the ignition board before condemning it — loose plugs are a common false positive. If wiring is intact, replace the ignition board.

### Error 79 — Condensate Drain Problem
The condensate sensor or drain system detected a problem. On condensing units like the TK-340X3-NIH, flue gas condensate must drain continuously. A blocked drain backs up acidic condensate and can damage the secondary heat exchanger.

**Causes:**
- Blocked condensate drain line
- Clogged condensate neutralizer (needs media replacement)
- Frozen condensate drain (cold climates)
- Condensate sensor failure

**Fix:**
1. Locate and clear the condensate drain line
2. Check the condensate neutralizer — the limestone media inside neutralizes acidic condensate. Replace media annually in commercial applications (see Parts section below)
3. In cold climates, ensure the drain has proper slope and is not exposed to freezing temperatures
4. Test the condensate sensor for continuity if the drain appears clear

### Error 90 — Communication Fault (External Controller)
The unit lost communication with an external controller (building management system, cascade controller, or remote control).

**Fix:** Check the communication wiring and protocol settings. Verify the external controller is operating correctly.

### Error 99 — Lockout After Multiple Fault Attempts
The unit has attempted to restart too many times and entered a hard lockout.

**Fix:** Resolve the underlying fault code that caused repeated lockouts (check the fault history if available), then perform a manual reset — disconnect power for 60 seconds.

---

## How to Fix It

1. **Record the error code** before resetting — it may not reappear immediately and you'll lose the diagnostic data.
2. **Check gas supply first** for ignition faults — verify the shutoff valve is open and gas pressure meets minimum requirements.
3. **Inspect the condensate system** on any condensing unit — a blocked condensate drain triggers cascading faults and can destroy the secondary heat exchanger within weeks.
4. **Test sensors before replacing boards** — thermistors fail far more often than control boards.
5. **Check water flow** — the TK-340X3-NIH has a minimum flow requirement (typically 0.5 GPM) before it will fire.
6. **Descale annually** in hard water areas — scale buildup is the root cause of multiple errors on condensing units.

---

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| [Takagi Condensate Neutralizer Replacement Media](https://www.amazon.com/s?i=industrial&k=condensate+neutralizer+media+limestone+tankless+water+heater&tag=errorcodefixes-20) | Error 79 — required annual maintenance on condensing units | $15–$40 |
| [Tankless Water Heater Flow Sensor](https://www.amazon.com/s?i=industrial&k=tankless+water+heater+flow+sensor+turbine&tag=errorcodefixes-20) | Error 65 — replaces seized or debris-clogged flow sensor | $20–$55 |
| [NTC Thermistor Sensor 10K Water Heater](https://www.amazon.com/s?i=industrial&k=NTC+thermistor+10K+water+heater+sensor&tag=errorcodefixes-20) | Errors 31, 32, 33 — inlet/outlet/heat exchanger sensor replacement | $10–$30 |
| [Tankless Water Heater Descaler Kit](https://www.amazon.com/s?i=industrial&k=tankless+water+heater+descaling+flush+kit&tag=errorcodefixes-20) | Annual maintenance to prevent scale-related faults and overtemperature | $25–$60 |
| [Flame Rod / Ionization Sensor](https://www.amazon.com/s?i=industrial&k=flame+rod+ionization+sensor+gas+water+heater&tag=errorcodefixes-20) | Errors 12, 19 — flame detection sensor replacement | $15–$45 |

---

## When to Call a Pro

For a commercial unit of this capacity, call a licensed technician for:

- **Error 14 (thermal fuse)** — root cause diagnosis required before replacement, or the new fuse will blow immediately
- **Error 51 (gas valve)** — gas valve work requires a licensed gas fitter in most jurisdictions
- **Any repair involving gas piping or refrigerant** — safety and code compliance
- **Secondary heat exchanger damage** — if Error 79 was left unaddressed for weeks, the secondary HX may be corroded and need replacement
- **Error 71 (ignition board)** — board-level diagnosis to confirm before spending on a replacement board

---

## Frequently Asked Questions

**Q: How often should the condensate neutralizer media be replaced on the TK-340X3-NIH?**

A: In commercial applications with high hot water demand, replace the neutralizer media every 6–12 months. The limestone media (calcium carbonate) neutralizes acidic condensate — as it saturates, pH rises and the neutralizer stops working, eventually causing Error 79. Inspect the media color: fresh media is white/gray; exhausted media turns dark and compacts.

**Q: Error 11 appears but gas supply is confirmed. What else could cause it?**

A: After confirming gas supply, the next most common causes are a fouled igniter electrode (clean the carbon off with fine sandpaper) and a blocked flue. Also check minimum water flow — the TK-340X3-NIH won't attempt ignition below its minimum flow threshold, which can look like an ignition failure when it's actually a flow problem.

**Q: Can multiple TK-340X3-NIH units be cascaded?**

A: Yes — Takagi offers cascade controllers for linking multiple units. Error 90 appears when the cascade communication fails. Verify RS-485 wiring and termination resistors at each unit in the cascade if this error appears in a multi-unit installation.
