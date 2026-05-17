---
title: "Vaillant Boiler Fault Codes — Complete Fix Guide"
description: "Vaillant boiler fault codes for ecoTEC, ecoFIT, and turboTEC series. What each code means and how to fix it."
pubDatetime: 2026-04-27T22:00:00Z
modDatetime: 2026-04-27T22:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - boiler
  - vaillant
---

Vaillant boilers — the ecoTEC Plus, ecoTEC Pro, ecoFIT Pure, and turboTEC Plus — display fault codes on the front panel when a lockout or fault condition is detected. The code appears as **F.XX** (fault) or **S.XX** (status). Faults lock the boiler out and require a reset. Status codes are informational and clear automatically.

This guide covers every common Vaillant fault code, what triggers it, what to check, and how to fix it. DIY-friendly fixes are clearly marked. Anything involving gas components requires a Gas Safe (UK) or qualified HVAC technician.

---

## How to Read a Vaillant Fault Code

On ecoTEC and ecoFIT models, the code appears in the display window — typically two characters after the **F** prefix. On older turboTEC models the display may show just a numeric blink sequence.

**To reset after a lockout:** Hold the reset button (flame symbol) for 3 seconds. If the fault clears and the boiler fires, monitor for recurrence. If the same fault returns within an hour, do not keep resetting — diagnose the root cause.

**Service menu access (ecoTEC Plus/Pro):** Press and hold the Mode and Eco buttons simultaneously for 5 seconds. Use the +/- arrows to navigate parameters. Parameter d.000 shows a live fault log. Exit by pressing Mode.

---

## Vaillant Fault Codes — Full List

### F.00 — Flow Temperature Sensor Interrupted

**Display:** F.00  
**Meaning:** The NTC sensor measuring flow (supply) temperature has an open circuit or is disconnected.

**Causes (most to least likely):**
1. Electrical connector loose or corroded at the NTC sensor
2. NTC sensor itself failed (open circuit)
3. Wiring harness damage between PCB and sensor
4. PCB input circuit fault

**Fix steps:**
1. Turn off boiler, isolate power.
2. Locate the flow NTC sensor on the primary heat exchanger outlet pipe — it's a small cylindrical probe with a two-pin connector.
3. Unplug and re-seat the connector. Check for corrosion or pushed-back pins.
4. Measure NTC resistance with a multimeter: at 20°C it should read approximately 10 kΩ; at 80°C approximately 1.5 kΩ. Out-of-range = sensor failed.
5. If wiring and connector are good and sensor reads correctly, suspect PCB.
6. Replace NTC sensor if faulty — it's a DIY-friendly part on most models.

---

### F.01 — Return Temperature Sensor Interrupted

**Display:** F.01  
**Meaning:** The NTC sensor measuring return (flow-back) temperature has an open circuit.

**Causes:**
1. Disconnected or corroded return NTC connector
2. Failed return NTC sensor
3. Wiring fault

**Fix steps:** Same diagnosis as F.00 but for the return pipe sensor, which is located on the incoming return leg, typically lower on the heat exchanger assembly. Resistance values at temperature are identical.

---

### F.10 — NTC Flow Temperature Sensor Short Circuit

**Display:** F.10  
**Meaning:** The flow NTC sensor is reading a short circuit — resistance is near zero — which the PCB interprets as an impossible temperature reading.

**Causes:**
1. NTC sensor internally shorted
2. Wiring chafed and shorting to ground or adjacent wire
3. Water ingress into connector

**Fix steps:**
1. Disconnect the NTC. If resistance now reads correctly (open/high), the sensor is shorted — replace it.
2. If resistance is still near zero with sensor disconnected, the fault is in the wiring harness or PCB.
3. Inspect wiring for melted insulation or pinch points near heat exchanger.

---

### F.22 — Low Water Pressure

**Display:** F.22  
**Meaning:** System water pressure has dropped below 0.5 bar. This is the most common Vaillant fault and is almost always a DIY fix.

**Causes:**
1. Radiator bleed valve left open after bleeding
2. Slow leak at radiator valves, pipe joints, or pump seal
3. Pressure relief valve (PRV) discharging (sign: water from doom overflow pipe outside)
4. Expansion vessel waterlogged

**Fix steps — Re-pressurising (most common):**
1. Locate the filling loop — usually a silver or grey flexi-hose with two isolation valves under the boiler.
2. Open both valves slowly until the pressure gauge reads 1.5 bar.
3. Close both valves tightly.
4. Press the reset button on the boiler.
5. Boiler should fire and pressure hold. If pressure drops again within days, there is a leak — find it before refilling again.

**If PRV keeps discharging:**  
Expansion vessel pre-charge pressure may be too low or the vessel membrane has failed. Check vessel charge pressure via the Schrader valve (like a bike tyre valve) — should be 0.75–1.0 bar for most domestic systems. Re-charge with a pump or replace the expansion vessel.

---

### F.28 — Ignition Failure (No Flame Detected)

**Display:** F.28  
**Meaning:** The boiler attempted to ignite and the ionisation rod detected no flame signal within the trial-for-ignition period.

**Causes:**
1. Gas supply interrupted — meter turned off, pre-payment meter out of credit, supply issue
2. Gas valve not opening (electrical or mechanical)
3. Electrode gap wrong or electrode cracked/carbonised
4. Ignition lead broken or tracking to earth
5. Ionisation rod dirty, cracked, or lead fault
6. PCB output fault (no spark voltage)

**Fix steps:**
1. Check other gas appliances in the property are working. If not, call your gas supplier.
2. Verify gas isolation valve at boiler is open (handle inline with pipe = open).
3. Reset boiler and listen for the spark clicking. No clicking = no spark signal — check ignition lead and electrode.
4. If sparking occurs but no ignition: gas valve issue or gas pressure too low for the area.
5. Check ionisation rod for carbon deposits — clean gently with fine emery cloth. Ensure clearance gap to burner is approximately 3–4 mm.
6. **Gas valve and PCB work must be done by a qualified engineer.**

---

### F.29 — Ignition Failure After Flame Loss During Operation

**Display:** F.29  
**Meaning:** The boiler lit successfully but the flame went out during operation and failed to re-ignite within the retry period.

**Causes:**
1. Gas supply fluctuation (pressure drop mid-cycle)
2. Ionisation rod intermittent — dirty or cracked ceramic
3. Gas valve solenoid intermittently not holding open
4. Flue products recirculating (blocked or restricted flue)
5. Condensate pipe partially blocked causing restriction

**Fix steps:**
1. Distinguish from F.28: F.29 means the boiler fires but the flame is unstable or drops.
2. Inspect ionisation rod — this is the most common culprit. Cleaning or replacement is DIY-capable with power isolated.
3. Check flue terminal outside for obstruction (bird nest, ice in cold weather, debris).
4. Check condensate trap is not blocked.
5. Persistent F.29 after cleaning ionisation rod usually means gas valve or PCB.

---

### F.32 — Fan Fault / Speed Out of Range

**Display:** F.32  
**Meaning:** The boiler fan (flue fan) is not reaching the required RPM before the boiler attempts to fire. The PCB monitors fan speed via the Hall sensor and will lockout if speed is incorrect.

**Causes:**
1. Fan motor bearing worn — fan spins slowly or intermittently
2. Fan impeller obstructed with debris or condensate ice (winter)
3. Hall effect speed sensor on fan failed
4. PCB not supplying correct voltage to fan
5. Wiring connector to fan loose

**Fix steps:**
1. With power isolated, manually spin the fan impeller — it should spin freely and smoothly. Resistance or grinding = bearing worn, replace fan assembly.
2. Check fan connector for corrosion. Reseat.
3. Check for debris in the fan housing, particularly after long idle periods.
4. With power on (take care), measure fan supply voltage at the connector: typically 24V or 230V depending on model. No voltage = PCB output fault.
5. Fan assemblies for ecoTEC are available as direct replacements — this is a Gas Safe engineer task as the flue must be partially dismantled.

---

### F.36 — Flue Gas Sensor Fault

**Display:** F.36  
**Meaning:** The flue gas temperature sensor (located in the flue outlet path) has detected an out-of-range reading or the sensor has failed.

**Causes:**
1. Flue gas sensor NTC failed (open or short)
2. Actual flue gas overheat — restricted flue, combustion issue
3. Wiring fault to sensor

**Fix steps:**
1. Check flue terminal is not blocked or restricted.
2. Inspect flue gas sensor connector and wiring.
3. Measure sensor resistance — values follow same NTC profile as flow/return sensors.
4. If sensor is good and flue is clear but fault persists, suspect PCB.

---

### F.57 — Comfort Relay (Pump) Fault

**Display:** F.57  
**Meaning:** The boiler PCB cannot detect the comfort relay or there's a fault in the pump circuit. Common on ecoTEC models with the EBus/OpenTherm controller interface.

**Causes:**
1. PCB relay fault
2. External 230V device (secondary pump, zone valve) overloading the boiler's relay output
3. Wiring fault on the pump/relay circuit

**Fix steps:**
1. Check any external wiring connected to the boiler's switched live or pump terminals.
2. Disconnect external zone valves or secondary pumps and test boiler alone.
3. If the fault clears with external loads removed, the relay is being overloaded — fit an external relay.
4. If fault persists with nothing external connected, PCB relay has failed — engineer required.

---

### F.61–F.64 — Gas Valve Fault Series

**Display:** F.61, F.62, F.63, F.64  
**Meaning:** These codes indicate a fault in the gas valve control circuit. Each sub-code narrows the fault:

| Code | Meaning |
|------|---------|
| F.61 | Gas valve control fault — solenoid open circuit or PCB output |
| F.62 | Gas valve relay stuck on (detected gas valve energised when it shouldn't be) |
| F.63 | EEPROM write fault during gas valve operation |
| F.64 | Flow/return NTC temperature exceeded safety limit while valve open |

**Fix steps:**
- **F.61:** Check gas valve solenoid coil resistance (typically 30–60 Ω). Out of spec = replace valve. Also check wiring from PCB to valve.
- **F.62:** This is a safety-critical fault — gas valve may be stuck open. Do not reset repeatedly. Isolate gas. Call engineer immediately.
- **F.63:** EEPROM fault — usually PCB replacement.
- **F.64:** Check both flow and return NTCs (F.00/F.01 diagnosis). If sensors are fine, PCB or heat exchanger scale causing overheat.

**Gas valve work must be done by Gas Safe registered engineer. Do not attempt solenoid replacement on live boiler.**

---

### F.71–F.77 — Sensor Fault Series

**Display:** F.71 through F.77  
**Meaning:** Extended sensor fault series. Most common on ecoFIT and ecoTEC Pro:

| Code | Sensor |
|------|--------|
| F.71 | Flow sensor — sensor signal implausible (wrong temperature reading) |
| F.72 | Return sensor — reading implausible |
| F.73 | DHW (hot water) NTC sensor fault |
| F.74 | DHW temperature sensor reading too high |
| F.75 | Pressure sensor fault — sensor signal not plausible |
| F.76 | Heat exchanger overheat sensor triggered |
| F.77 | Flue/condensate neutraliser sensor fault |

**Fix steps:**
- For F.71/F.72: Check NTC sensors as per F.00/F.01 procedure. Also check for partial blockage in heat exchanger (sludge build-up reduces temperature differential and makes readings look implausible).
- For F.75: Check pressure sensor wiring. Pressure sensors are separate from mechanical gauges — measure output voltage (typically 0.5V–4.5V over range).
- For F.76: Overheat condition — check pump is running, system has adequate flow, no airlock in heat exchanger.
- For F.77: Check condensate pipe is clear and draining freely.

---

### F.83 — No Temperature Rise Detected / Condensate Fault

**Display:** F.83  
**Meaning:** The boiler fired and ran but no temperature rise was detected at the flow sensor. Also triggered by condensate issues on some firmware versions.

**Causes:**
1. No water flow through heat exchanger (pump not running, airlock, closed valve)
2. Condensate pipe frozen (common in cold weather — pipe runs outside)
3. Condensate trap blocked
4. Flow NTC has failed and is reading ambient temperature

**Fix steps — Frozen condensate (most common in winter):**
1. Locate the white condensate pipe (usually 21.5mm white plastic) — it typically exits the boiler base and runs to an outside drain.
2. Pour warm (not boiling) water over the external section, or wrap with a hot water bottle.
3. Once clear, reset boiler.
4. Insulate the external condensate pipe to prevent recurrence.

**For airlock/no flow:**
1. Check pump is running (should be audible).
2. Bleed any air from radiators.
3. Check all system isolation valves are open.

---

### F.91 — EEPROM Fault (PCB Fault)

**Display:** F.91  
**Meaning:** The PCB's non-volatile memory (EEPROM) has a read or write error. This is almost always a PCB replacement.

**Causes:**
1. PCB memory chip failed
2. Firmware corruption from power surge
3. Component failure on PCB

**Fix steps:**
1. Try power cycling the boiler (isolate supply for 5 minutes). Rarely fixes EEPROM faults but worth trying.
2. If fault persists, PCB replacement is required.
3. Note: On newer ecoTEC models, the PCB stores system parameters in EEPROM. When replacing, the engineer may need to re-enter system configuration.

---

## Pressure Top-Up Procedure (F.22 Detailed)

This procedure applies to all Vaillant ecoTEC, ecoFIT, and turboTEC models:

1. **Check current pressure** on the analogue gauge (front of boiler or pipe-mounted). Target: 1.0–1.5 bar cold, up to 2.0 bar when hot.
2. **Locate the filling loop** — silver braided flex under the boiler with two quarter-turn valves. If no flexi loop, there may be a permanent filling valve (lever or key-operated).
3. **With boiler cool:** Open one filling valve slowly, then open the second. Watch pressure gauge.
4. **Stop at 1.5 bar.** Close both valves. Do not overfill — pressure above 3 bar will open the PRV.
5. **Reset and test.** Pressure should hold within 0.1 bar after a full heating cycle.

If pressure drops more than 0.2 bar per week, there is a leak. Common locations: radiator valve packings, pump shaft seal, system filter housing, flexible hoses, heat exchanger microleaks.

---

## Parts Reference Table

| Part | Typical Vaillant numbers |
|------|--------------------------|
| Flow NTC sensor | 0020025248, 0020040239 |
| Return NTC sensor | 0020025247, 0020040240 |
| Pressure sensor | 0020116914, 0020193991 |
| Fan assembly | 0020135502, 0020204192 |
| Gas valve | 0020053968, 0020074079 |
| PCB | 0020132764, 0020135764 |

Verify part numbers against the boiler data plate before ordering.

---

## When to Call an Engineer

Call a Gas Safe registered engineer for:
- Any F.61–F.64 fault (gas valve circuit)
- F.28/F.29 when gas supply is confirmed good (ignition/combustion work)
- F.32 fan replacement (flue must be dismantled)
- F.91 PCB replacement
- Any fault that recurs within 24 hours after reset
- Evidence of gas smell — ventilate, evacuate, call emergency gas line (0800 111 999 in UK)

Do not keep resetting a boiler that repeatedly locks out on the same code. Each reset re-attempts ignition or re-energises components that may already be in a failed state.


## Where to Buy Replacement Parts

Find replacement parts for Vaillant boilers on Amazon:

- [Vaillant Boiler Parts & Spares](https://www.amazon.com/s?ascsubtag=ecf-vaillant-boiler-fault-codes&k=Vaillant+boiler+parts&tag=errorcodefixes-20)
- [Vaillant Ignition Electrode Replacement](https://www.amazon.com/s?ascsubtag=ecf-vaillant-boiler-fault-codes&k=Vaillant+boiler+ignition+electrode+replacement&tag=errorcodefixes-20)
- [Vaillant NTC Thermistor & Sensor Replacement](https://www.amazon.com/s?ascsubtag=ecf-vaillant-boiler-fault-codes&k=Vaillant+boiler+NTC+thermistor+sensor&tag=errorcodefixes-20)