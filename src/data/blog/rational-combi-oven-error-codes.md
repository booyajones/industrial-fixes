---
title: "Rational iCombi Classic & Pro Error Codes: E01, Service 20.x, 21, 26 Fixes"
description: "Every Rational iCombi Classic and iCombi Pro error code explained. E01 board fault, Service 20.x sensor codes, Service 21, Service 26, and legacy SCC WE codes. Step-by-step diagnosis with OEM part numbers for commercial kitchen technicians."
pubDatetime: 2026-04-27T18:00:00Z
modDatetime: 2026-04-27T18:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - oven
  - rational
  - combi-oven
  - foodservice
  - commercial-kitchen
---

## Rational Combi Oven Error Codes — Quick Reference

Rational combi ovens (SCC WE, iCombi Pro, iCombi Classic) display service codes and error messages when a system goes out of spec. On the SCC WE platform, these appear as "Service XX" on the display. The iCombi Pro and iCombi Classic show text-based error messages in the control panel, but the underlying fault categories map to the same systems.

| Code | System | Meaning | Priority |
|------|--------|---------|----------|
| Service 10 | Water/Boiler | SC pump not draining | High |
| Service 11–14 | Water/Boiler | Steam generator fill faults | High |
| Service 20.x | Sensors | Thermocouple failure | High |
| Service 21 | PCB | Voltage/current fault on main board | Critical |
| Service 25 | Cleaning | CleanJet water flow fault | Medium |
| Service 26–27 | Drain | Drain valve position fault | Medium |
| Service 28 | Boiler | Steam generator overtemp | High |
| Service 29 | PCB | Control panel overheating | High |
| Service 30 | Humidity | Emergency humidity control active | Medium |
| Service 31.x | Core Probe | Core temperature probe fault | Medium |
| Service 32–33 | Gas | Ignition box fault (gas units) | Critical |
| Service 34.x | Bus | Bus signal communication fault | High |
| Service 40–44 | Cleaning | Care system fault | Medium |
| Service 60 | Gas | Ignition box initialization error | Critical |
| Service 100 | Water | SC pump / level electrode failure | High |

---

## Water and Steam Generator Faults (Service 10–14, 100)

These are the most frequently seen codes on Rational combi ovens. Hard water, scale buildup, and solenoid failures account for the majority of calls.

### Service 10 — SC Pump High Water Level / Drain Failure

The self-cleaning (SC) pump failed to drain during a cleaning cycle, or the drain hose is blocked.

**Causes (most common first):**
1. Blocked drain hose or kink in SC pump tubing
2. Defective SC pump motor (seized or burned out)
3. Calcified level probe giving false high-water reading

**Diagnosis and fix:**
1. Run the drain function test from the oven's service menu and watch the drain outlet — is water moving?
2. With power off, trace the SC pump hose from the pump outlet to the drain. Remove any kinks or blockages.
3. If no water moves at all, check voltage at the SC pump motor during a drain cycle (should see full line voltage). No voltage = PCB relay failure. Full voltage but no movement = pump motor dead.
4. If the pump runs but water doesn't flow, check for scale bridging across the level probe. Clean with descaler.

**Parts:** SC pump motor, drain valve assembly, level electrode.

### Service 11 — CDS Sensor Sending Too Many Pulses

The CDS (conductivity/flow) sensor is counting too many pulses during a steam generator refill, which means water is leaking back into the system when it shouldn't be.

**Causes:**
1. Air-break valve above the steam generator not closing during fill cycle
2. Leak in water pipework supplying the steam generator
3. CDS sensor miscalibrated (should be set to 1,000 pulses per liter)
4. Level electrode fault

**Fix:**
1. Confirm air-break valve closes fully when fill starts — watch it during a live fill cycle.
2. Inspect all water connections between the inlet solenoid and the steam generator for seeping joints.
3. Check CDS sensor calibration in service menu — recalibrate to 1,000 pulses/liter if off.
4. Test level electrode resistance. An intermittent short causes false signals.

### Service 12 — CDS Sensor Without Signal

The CDS sensor has no signal despite the level electrode confirming water is present. The oven can't measure water flow into the steam generator.

**Causes:**
1. Low incoming water pressure (minimum required: 30–45 psi depending on model)
2. Defective CDS sensor
3. Wiring fault between CDS sensor and PCB

**Fix:**
1. Check static and dynamic water pressure at the oven inlet. At less than 30 psi, the CDS reed switch won't operate reliably.
2. If pressure is good, swap the CDS sensor. They're inexpensive and fail regularly in hard-water areas.
3. Check connector pins on CDS sensor harness for corrosion.

**Parts:** CDS flow sensor.

### Service 13 — Steam Generator Not Refilling During Steam Mode

The steam generator ran dry during a cooking session. This is a forced-fill error — the PCB tried to fill the boiler but the level electrode didn't confirm water arrival.

**Causes:**
1. Level electrode 0-1 signal not reaching PCB (wiring fault)
2. Water supply valve partially closed
3. Inlet solenoid valve Y1 not opening fully

**Fix:**
1. Access service/diagnostic mode. Trigger a manual fill and watch the level electrode signal on the diagnostic screen — it must flip from 0 to 1 when the boiler fills.
2. Verify the manual water shut-off valve is fully open.
3. Test inlet solenoid Y1: apply 24V AC and verify valve opens. Replace if it doesn't.

### Service 14 — Level Electrode Not Recognizing Water

The CDS sensor measured enough pulses (water entered), but the level electrode never detected it. This is almost always a water quality issue.

**Causes:**
1. Water conductivity too low — common with RO (reverse osmosis) or softened water without re-mineralization
2. Scaled level electrode not making contact
3. Defective level electrode

**Fix:**
1. Test water conductivity. Rational requires 200–600 µS/cm at the oven inlet. Pure RO water is typically 5–20 µS/cm — far too low.
2. If conductivity is correct, clean the level electrode with descaler.
3. If conductivity is out of spec, install a water treatment/blending system to bring it into range. This is not optional — it will cause recurring faults.
4. Replace electrode if cleaning doesn't resolve it.

### Service 100 — SC Pump Defective or Level Electrode Calcified

Escalated version of Service 10. The error is set and latched — requires a successful abort/rinse program to clear after repair.

**Fix:** Same diagnosis as Service 10, but assume the pump or electrode has failed outright. Replace, then run rinse/abort program to reset.

---

## Thermocouple and Temperature Sensor Faults (Service 20.x, 28)

### Service 20.x — Defective Thermocouple

Rational SCC WE ovens have multiple thermocouples. The fault code's decimal suffix identifies which probe failed. These can also appear combined when multiple probes fail simultaneously.

| Code | Thermocouple | Location |
|------|-------------|----------|
| 20.1 | B1 | Cabinet (main cavity) |
| 20.2 | B2 | Quenching/control sensor |
| 20.4 | B4 | Humidity sensor |
| 20.8 | B5 | Steam generator |
| 20.6 | B2 + B4 | Two probes failed |
| 20.12 | B4 + B5 | Two probes failed |

**Causes (most common first):**
1. Thermocouple wire broken or burnt through near the probe tip
2. Connector corrosion at PCB end — common in high-steam environments
3. Probe contaminated with grease or cleaning chemicals

**Diagnosis:**
1. Disconnect the suspect thermocouple at the PCB connector. Measure resistance end-to-end — a good Type K thermocouple reads a few ohms at room temperature, open circuit = dead probe.
2. With a multimeter set to millivolts (mV), measure the thermocouple output at room temp — should read approximately 0–2 mV. At 200°C, expect ~8 mV.
3. Inspect connector pins for green corrosion. Clean with contact cleaner and check seating.

**Fix:** Replace the identified thermocouple. Run a heat cycle to confirm fault clears.

**Parts:** Rational cabinet thermocouple (B1), quenching sensor (B2), humidity sensor (B4), steam generator thermocouple (B5).

### Service 28 — Steam Generator Thermocouple B5 Above 180°C

The steam generator overheated. At 180°C (356°F), the boiler has run dry or the heating element is buried in limescale and cycling poorly.

**Causes:**
1. Steam generator running without sufficient water (link to Service 13/14 — water supply faults)
2. Heavy limescale on heating element creating a hotspot
3. Defective temperature limiter (thermal cutout)

**Fix:**
1. Allow oven to cool. The fault indicator clears automatically once B5 drops below 110°C.
2. Once cool, remove steam generator access panel and inspect heating element for scale.
3. If heavily scaled, perform a professional descale (acid descale of the steam generator, not just the cavity). This is not the same as the CleanJet cycle.
4. If scaling is minimal, check the level electrode and water supply (see Service 13/14 above).
5. Replace thermal limiter if it has tripped and won't reset.

**Parts:** Steam generator heating element, thermal limiter, level electrode.

---

## PCB and Electrical Faults (Service 21, 23, 24, 29)

### Service 21 — Voltage / Current Monitoring Error

The main control PCB detected a voltage or current reading outside expected range. This code requires a factory-trained technician — but here's what they'll be checking:

On SCC WE 101/201 models, key voltages at the main PCB:
- 18V from transformer T1
- 12V regulated on PCB
- High current on MMI (bit 4)
- High current on drain valve M7 (bit 8)
- High current on humidity valve Y5 (bit 9)

**Causes:**
1. Shorted solenoid valve or motor pulling excessive current
2. Transformer T1 output degraded
3. PCB component failure

**Fix:** Run through each bit value to isolate which subsystem is drawing excessive current. Disconnect solenoids and motors one by one to identify the overloaded circuit before replacing the PCB.

### Service 23 — SSR Steam Short Circuit

The solid-state relay (SSR) controlling the steam heating element has failed shorted — it's passing current even when it shouldn't be.

**Fix:** Replace the SSR for steam heating. SSRs fail shorted far more often than open. Do not operate the oven with a shorted SSR — the element will overheat.

### Service 24 — SSR Hot Air Short Circuit

Same as Service 23 but on the hot-air heating SSR.

**Fix:** Replace the hot-air SSR.

### Service 29 — PCB Temperature Above 85°C

The control panel electronics are overheating. Left uncorrected, this shortens board life significantly.

**Causes (most common first):**
1. Blocked or dirty air filter on the control panel
2. Cooling fan for control panel not running
3. Control panel gasket damaged or missing, allowing oven heat into the panel cavity
4. External heat source nearby (adjacent high-heat equipment)

**Fix:**
1. Clean the air filter — this is a maintenance item that gets neglected. Replace if damaged.
2. Verify cooling fan spins freely and runs during operation. Check fan connector and winding resistance.
3. Inspect door gasket between the control panel and oven body. Replace if deformed or torn.

**Parts:** Control panel cooling fan, control panel air filter, control panel gasket.

---

## Humidity and Differential Pressure Faults (Service 30, 36, 37)

### Service 30 — Emergency Humidity Control Active

The humidity control device (pressure sensor P1 / differential pressure sensor) is non-functional. The oven falls back to a secondary control algorithm using the quenching sensor B2 — cooking continues but with reduced humidity precision.

**Causes:**
1. Defective differential pressure sensor P1
2. Blocked pressure sensing port (grease or condensate)
3. Wiring fault to P1

**Fix:**
1. In diagnostic mode, verify P1 reading — at rest (no cooking) it should read near zero differential pressure.
2. Clean pressure port if clogged with grease buildup.
3. Replace P1 if readings are erratic or absent.

### Service 36 — Differential Pressure Sensor P1 Defective

Direct confirmation P1 has failed outright (vs. Service 30 which can be a soft fault).

**Fix:** Replace differential pressure sensor P1.

### Service 37 — P1 Reading Out of Expected Range

P1 is functional but reading outside its calibration range.

**Fix:** Check the rubber sensing hoses connected to P1 for kinks, disconnection, or moisture blockage. Blow clear with compressed air if needed.

---

## Core Temperature Probe Faults (Service 31.x)

The multi-point core probe is a needle probe with multiple sensing points along its length. Like Service 20.x, the decimal suffix is additive.

| Code | Probe Point | Location |
|------|------------|----------|
| 31.1 | Shaft probe | Near handle |
| 31.2 | 5th probe | Near shaft |
| 31.4 | 4th probe | Middle section |
| 31.8 | 3rd probe | Mid-tip |
| 31.16 | 2nd probe | Near tip |
| 31.32 | 1st probe | Tip |
| 31.12 | 3rd + 4th | Two points failed |

**Causes:**
1. Probe physically bent or dropped — cracks internal conductors
2. Probe storage jack not making contact
3. Liquid ingress through tip seal

**Fix:**
1. Remove probe and test each section with a multimeter. Compare resistance readings tip-to-connector.
2. Check the jack/storage port for bent pins or corrosion.
3. If individual segments read open circuit or wildly out of spec, replace the probe.

**Parts:** Rational multi-point core temperature probe.

---

## Gas Ignition Faults (Service 32, 33, 60) — Gas Models Only

### Service 32.x — Ignition Box Failure

The ignition module failed to complete its self-test or isn't communicating.

| Code | Affected Unit |
|------|--------------|
| 32.0 | Top ignition box |
| 32.1 | Bottom ignition box (floor models) |
| 32.2 | Both ignition boxes |

**Fix:** Replace the ignition box identified by the suffix. Before replacing, verify gas supply is present and spark electrode condition is good — a fouled electrode can fool the ignition module into a false lockout.

### Service 33.x — Ignition Wiring / Gas Valve Fault

The ignition box is present but the wiring to it or the gas valve is suspect.

**Fix:**
1. Check spark electrode wiring — cracks in high-voltage ignition cable cause misfire.
2. Verify gas valve opens on demand using a manometer downstream of the valve.
3. Replace ignition cable or gas valve as needed.

### Service 60 — Ignition Box Incorrect Initialization (Gas)

On startup, the ignition box returned an unexpected initialization state.

**Fix:**
1. Check gas pressure settings in service menu — incorrect settings can prevent proper ignition box startup.
2. Power cycle the oven and run the SD Repair program from the service menu.
3. If fault recurs, replace the ignition module.

### "rES" — Gas Reset / Lockout

Displayed as "rES" or "RESET" on the panel. The oven locked out after three failed ignition attempts.

**Fix:**
1. Verify gas supply valve is fully open and supply pressure is within spec (check nameplate).
2. Confirm gas hose/flex connector is secure and not kinked.
3. If gas is confirmed present, the ignition electrode or ignitor module needs attention.

---

## Bus Communication Faults (Service 34.x, 35)

### Service 34.x — Bus Signal Problem

The oven's internal communication bus lost contact with a component. The decimal suffix identifies which component.

| Code | Component |
|------|----------|
| 34.1 | Top fan motor |
| 34.2 | Bottom fan motor |
| 34.4 | Top ignition module |
| 34.8 | Bottom ignition module |
| 34.12 | Both ignition modules |

**Causes:**
1. Loose or corroded bus cable connector
2. Damaged bus cable (often happens during cleaning if water gets into connectors)
3. Component failure (motor controller, ignition module)

**Fix:**
1. Locate the bus cable connectors for the affected component — usually accessible from the motor/burner area.
2. Reseat connectors and check for bent pins.
3. Inspect cable insulation for burns or chafing.
4. If cable is intact, replace the component identified in the code.

**Parts:** Bus cable harness, fan motor assembly, ignition module.

### Service 35 — Ultravent Bus Signal Lost

The external ultravent (ventilation exhaust hood interface) is disconnected or unplugged.

**Fix:** Reconnect the ultravent communication cable. If the unit operates without an ultravent, verify settings — some installations require this connection to be stubbed out with a terminator.

---

## Cleaning System Faults (Service 25, 26, 27, 40–44)

### Service 25 — CleanJet Water Flow Fault

During a CleanJet+Care cycle, the oven detected inadequate water spraying into the cavity. Specifically: the cavity fan motor didn't show the expected increase in load when water should have been hitting the fan wheel.

**Causes (most common first):**
1. Water supply pressure too low during cleaning cycle
2. Moistening valve Y3 or spray nozzle clogged
3. CDS sensor not sending pulses during cleaning
4. Rack or trolley not fully inserted (required for proper water distribution)

**Diagnosis:**
1. Start a CleanJet cycle and observe the nozzle — is water spraying into the blower area?
2. Check dynamic water pressure at the oven during the cycle.
3. Remove and clean the cleaning injection nozzle — they clog with limescale.
4. Verify GN racks are fully seated in the oven.

**Parts:** Moistening valve Y3, injection nozzle.

### Service 26 — Drain Valve Won't Open (Permanently Closed)

The drain valve microswitch never confirmed the "open" position.

**Fix:**
1. Run drain valve function test. The valve should stroke open and the microswitch should click.
2. Check the drain valve microswitch — replace if it's not triggering.
3. Inspect the valve actuator for seized or stripped gears.
4. In basic settings: verify drain valve timing ratio is set correctly (1/4 open : 3/4 closed, e.g. 9 sec open : 27 sec closed).
5. If valve mechanism is failed, replace the drain valve assembly.

**Parts:** Drain valve assembly with microswitch.

### Service 27 — Drain Valve Won't Close

Same actuator assembly, opposite failure — valve is stuck open or the closed-position microswitch isn't triggering.

**Fix:** Same as Service 26. Run abort/rinse program after repair to reset the error.

### Service 40 — Care Pump Not Functioning

The Care pump (which injects Rational CARE tabs dissolved in solution) isn't delivering chemical to the steam generator.

**Fix:**
1. Confirm Rational CARE tabs are loaded correctly.
2. Check the hose from Care pump outlet — kinks are the most common cause.
3. Run pump function test. If pump motor runs but no flow, check for blockage in the care container pickup or outlet line.
4. Replace Care pump M12 if motor is dead.

**Parts:** Care pump M12, care pump hose.

### Service 41 — Moistening Valve Y3 / CDS Fault During Care Cycle

Solenoid valve Y3 (moistening) is defective, the valve is blocked, or the CDS sensor isn't pulsing during the care cycle.

**Fix:**
1. Test Y3 solenoid — apply 24V AC, confirm it opens and passes water.
2. Clean valve seat and strainer on Y3 inlet.
3. Check CDS sensor signal during a manual fill event.
4. Resolve the underlying issue, then reset via a successful rinse program.

### Service 42 — Care Solenoid Y4 / Hose Fault

The care chemical delivery solenoid Y4 or its supply hose is blocked or defective.

**Fix:** Same approach as Service 41. Inspect Y4 and the care supply line for blockages. Clear or replace, then run rinse to reset.

### Service 43 — Solenoid Passing Water (Won't Close)

One of Y1, Y3, or Y4 is leaking through — stuck open or seal failed. The CDS sensor is counting pulses continuously even when filling should have stopped.

**Fix:**
1. Identify which solenoid by checking which circuit is active during the fault.
2. Remove and inspect valve seat — debris or limescale can hold valves open.
3. Rebuild or replace the solenoid valve.
4. Run abort program to reset.

### Service 44 — Steam Not Heating During CleanJet+Care

The cleaning cycle couldn't reach steam temperature to properly activate the cleaning chemistry.

**Causes:**
1. Steam generator heating element failure
2. Steam SSR failure
3. Water supply issue (no water in steam generator)

**Fix:** Check steam generator heating element continuity and SSR function. Run abort to reset after repair.

---

## iCombi Pro and iCombi Classic — Display Error Messages

The iCombi Pro and iCombi Classic show text errors rather than numbered service codes on their touchscreen displays. These map to the same underlying systems.

| Display Message | System | Immediate Action |
|----------------|--------|-----------------|
| "No heating — hot air" | Heating element or SSR | Check hot-air element continuity; test SSR |
| "No heating — steam" | Steam element or SSR | Check steam element; test SSR |
| "No steam generated" | Water supply or boiler | Check water pressure, inlet solenoid, steam generator level |
| "Moisture too high" | Humidity sensor / drain | Check drain valve, B4 humidity sensor, quenching sensor |
| "Moisture too low" | Humidity/steam system | Check steam injection valve, CDS sensor, water supply |
| "Door open" | Door switch | Check door closure and door microswitch |
| "Temperature sensor fault" | Cavity thermocouples | Check B1/B2 thermocouple connections; replace faulty sensor |
| "Core probe fault" | Core probe | Check probe insertion, test probe resistance |
| "Fan fault" | Convection fan motor | Check fan motor, bus cable, motor controller |
| "Cleaning system fault" | CleanJet+Care | Check water supply, nozzles, Care pump, CDS sensor |
| "Safety temperature exceeded" | Thermal overload | Allow cooling; investigate overheat root cause |

On the iCombi Pro, many of these messages come with a QR code that links to Rational's ConnectedCooking diagnostic portal. If the unit is online, this can pull live diagnostics before you arrive on site.

---

## Diagnostic Mode Access

On SCC WE models, access the hidden service menu by pressing and holding specific button combinations (varies by model year — consult the service manual for your specific serial number range). The diagnostic menu allows you to:

- Test individual solenoids, pumps, and fan motors in isolation
- Read live sensor values (temperatures, pressure sensor output)
- View error history with timestamps
- Run calibration routines for sensors

On iCombi Pro and iCombi Classic, tap the info button (ⓘ) → "Service" → enter the service PIN (factory default: 4-digit code provided by Rational to authorized technicians). This unlocks component-level testing and error logs.

---

## Preventive Maintenance Schedule

| Interval | Task |
|----------|------|
| Daily | Run CleanJet+Care cycle; wipe door gasket; check drain is clear |
| Weekly | Clean air injection nozzles; inspect door seal for compression damage |
| Monthly | Clean control panel air filter; check water inlet filter/strainer; inspect drain |
| Quarterly | Descale steam generator; calibrate humidity sensor; lubricate door hinges |
| Annually | Full water system inspection; replace worn thermocouples; verify SSR performance; clean fan wheel |

Water treatment is non-negotiable. Hard water without softening deposits scale on the steam generator element and level electrode at a rate that can trigger Service 10–14 faults within months of installation. Rational recommends 200–600 µS/cm conductivity at the inlet.

---

## Common Replacement Parts

| Part | Application | Notes |
|------|-------------|-------|
| Cabinet thermocouple B1 | Service 20.1 / temperature fault | [Amazon search](https://www.amazon.com/dp/B00RJF4PYQ?ascsubtag=ecf-rational-combi-oven-error-codes&tag=errorcodefixes-20) |
| Steam generator thermocouple B5 | Service 20.8 / 28 | Check Rational part numbers by model |
| CDS flow sensor | Service 11, 12, 25, 41 | [Amazon search](https://www.amazon.com/s?ascsubtag=ecf-rational-combi-oven-error-codes&k=Rational+CDS+sensor+combi+oven&tag=errorcodefixes-20) |
| Level electrode | Service 13, 14, 100 | Critical in hard-water areas |
| Drain valve assembly | Service 26, 27 | Includes microswitch |
| Steam generator heating element | Service 28, 44 | Replace as set with thermostat |
| Solid-state relay (SSR) | Service 23, 24 | Hot-air and steam SSRs are different |
| Care pump M12 | Service 40, 120 | [Amazon search](https://www.amazon.com/s?ascsubtag=ecf-rational-combi-oven-error-codes&k=Rational+care+pump+M12&tag=errorcodefixes-20) |
| Moistening solenoid Y3 | Service 25, 41 | Clean before replacing — often just scaled |
| Differential pressure sensor P1 | Service 30, 36, 37 | [Amazon search](https://www.amazon.com/s?ascsubtag=ecf-rational-combi-oven-error-codes&k=Rational+differential+pressure+sensor+combi&tag=errorcodefixes-20) |
| Multi-point core probe | Service 31.x | Confirm compatible with your model |
| Control panel cooling fan | Service 29 | [Amazon search](https://www.amazon.com/s?ascsubtag=ecf-rational-combi-oven-error-codes&k=Rational+control+panel+cooling+fan&tag=errorcodefixes-20) |
| Door gasket / door seal | Door fault, steam loss | Inspect quarterly; replace when compressed |
| Ignition module (gas models) | Service 32, 33, 60 | Match to top or bottom burner position |

---

## When to Call Rational Service

Some fault codes require factory-authorized access:

- **Service 13** (steam generator forced fill) — requires password-protected back-office software to investigate the level electrode signal properly
- **Service 21** (PCB voltage/current fault) — board-level diagnosis requires factory training and test equipment
- **Service 32/33/60** (gas ignition) — gas-system work requires certified technicians in most jurisdictions
- **Any fault after full descale and water treatment correction** — if basic faults recur after addressing root causes, there may be underlying PCB or control software issues that need Rational's diagnostic tools

Rational maintains a network of Authorized Service Agents (ASA). General Parts and other ASA providers have factory-certified technicians and OEM parts access. Rational's ConnectedCooking platform (for networked iCombi Pro units) can pull remote diagnostics and often narrows down the fault before a technician arrives.

---

## Jump to Fix

- **Service 10–14** → Check water supply valve → Test CDS sensor → Inspect level electrode → Address water quality
- **Service 20.x** → Disconnect thermocouple → Measure resistance → Replace failed sensor
- **Service 21** → Isolate subsystems → Check voltages → Call ASA
- **Service 25** → Check water pressure → Inspect cleaning nozzle → Test moistening valve Y3
- **Service 26–27** → Run drain test → Inspect valve microswitch → Replace drain assembly
- **Service 28** → Cool oven → Inspect steam generator element → Descale if needed
- **Service 29** → Clean air filter → Check cooling fan → Inspect panel gasket
- **Service 31.x** → Test probe sections → Check storage jack → Replace probe
- **Service 40** → Check Care hose for kinks → Test pump motor → Replace Care pump
