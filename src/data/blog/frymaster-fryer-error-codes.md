---
title: "Frymaster Fryer Error Codes — Complete Fix Guide"
description: "Frymaster fryer error codes for M4000, MJCF, MJH, and FPH series. What each code means and how to fix it."
pubDatetime: 2026-04-27T20:00:00Z
modDatetime: 2026-04-27T20:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - commercial-kitchen
  - frymaster
---

Every minute your Frymaster fryer is down costs money. The line backs up, product gets held, and your manager starts looking over your shoulder. The faster you decode what that error code actually means, the faster you get back to service.

This guide covers the complete Frymaster error code list for the 3000, 4000 (SMART4U), and M4000 controllers found on MJCF, MJH, RE series, and FPH fryers. Each code includes the root cause, a diagnostic sequence, and fix steps ordered by how often that cause shows up in the field.

---

## Frymaster Controller Types: Know What You Have

Before you start diagnosing, identify your controller:

**3000 Controller** — Found on older MJCF, MJH, and M3000 series gas and electric fryers. Single-lane or split-vat configurations. Error codes display as E-numbers (E03, E06, etc.). Access the error log by pressing TEMP to display OFF, then navigate to the Tech Mode E-Log.

**4000 / SMART4U Controller** — Found on RE series and newer MJCF/MJH variants. Touchscreen interface. Stores the last 10 errors with timestamps. Access via Menu > Information > E-Log.

**M4000 Controller** — McDonald's LOV (Low Oil Volume) series. High-precision oil management. Error log accessible via the Info/Stats menu. Codes align with the 3000/4000 family but include additional LOV-specific filtration faults.

**FPH Series** — Filter/pump-equipped fryers with dedicated filtration controller faults. Same base error set as above, with E09–E24 filtration and drain codes most relevant.

---

## Full Error Code Table

| Code | Display Message | Meaning |
|------|----------------|---------|
| E01 | REMOVE DISCARD (Right) | Cook started on split vat at wrong setpoint |
| E02 | REMOVE DISCARD (Left) | Cook started on left vat at wrong setpoint |
| E03 | TEMP PROBE FAILURE | Temperature probe out of range |
| E04 | HI 2 BAD | High limit 2 reading out of range |
| E05 | HOT HI 1 | Oil over 410°F — emergency shutoff |
| E06 | HEATING FAILURE | Heating circuit component failure |
| E07 | ERROR MIB SOFTWARE | Internal MIB software fault |
| E08 | ERROR ATO BOARD | ATO board connection lost or failed |
| E09 | ERROR PUMP NOT FILLING | Filter pump not filling — dirty pad or bypass |
| E10 | ERROR DRAIN VALVE NOT OPEN | Drain valve failed to open |
| E11 | ERROR DRAIN VALVE NOT CLOSED | Drain valve failed to close |
| E12 | ERROR RETURN VALVE NOT OPEN | Return valve failed to open |
| E13 | ERROR RETURN VALVE NOT CLOSED | Return valve failed to close |
| E14 | ERROR AIF BOARD | AIF board missing or failed |
| E15 | ERROR MIB BOARD | MIB board connection lost |
| E16 | ERROR AIF PROBE | AIF RTD out of range |
| E17 | ERROR ATO PROBE | ATO RTD out of range |
| E19 | M3000 CAN TX FULL | CAN communication between controllers lost |
| E20 | INVALID CODE LOCATION | SD card removed during firmware update |
| E21 | CHANGE FILTER PAPER | 24/25-hour filter timer expired, or dirty filter logic triggered |
| E22 | OIL IN PAN ERROR | Oil detected in filter pan unexpectedly |
| E23 | CLOGGED DRAIN (Gas) | Vat did not drain during filtration |
| E24 | AIF BOARD OIB FAILED (Gas) | Oil-back sensor failed |
| E25 | RECOVERY FAULT | Recovery time exceeded limit (1:40 electric / 2:25 gas) |
| E26 | RECOVERY FAULT CALL SERVICE | Recovery fault repeated two or more consecutive cycles |
| E27 | LOW TEMP ALARM | Oil dropped 30°F below setpoint (idle) or 45°F (cook) |
| E28 | HIGH TEMP ALARM | Oil rose 40°F above setpoint |

---

## Detailed Fault Diagnosis and Fix Steps

### E03 — TEMP PROBE FAILURE

**What it means:** The temperature-sensing probe (RTD or thermocouple depending on fryer model) is reading outside of valid range — typically below –40°F or above 600°F — which tells the controller the circuit is open, shorted, or the probe has failed.

**Causes in order of frequency:**
1. Probe connector unplugged or corroded at the harness junction
2. Probe cable damaged — frayed insulation from heat exposure or grease buildup
3. Probe element failed (open circuit internally)
4. Controller input circuit failed

**Fix steps:**
1. Shut the fryer off immediately. Do not attempt to run with a failed probe — the fryer has no temperature feedback.
2. Let the frypot cool. Pull the probe connector at the controller harness and inspect for corrosion, moisture, or pushed-back pins. Reseat firmly.
3. Use a multimeter on the probe leads. A standard RTD probe should read approximately 100–110 ohms at room temperature. An open circuit or near-zero ohm reading confirms probe failure.
4. If the probe measures correctly but the code persists after reconnecting, suspect the wiring harness between the probe and controller. Check for breaks or heat damage along the wire path.
5. Replace the probe if out of spec. Replace the controller board if the probe measures correctly but the fault persists.

**Note on E04 (HI 2 BAD):** Same diagnostic logic applies. E04 specifically points to the high-limit thermostat circuit rather than the cooking probe. Test the high-limit thermocouple separately.

---

### E05 — HOT HI 1

**What it means:** The oil temperature has exceeded 410°F (210°C) — the upper safety threshold for non-CE fryers. At this temperature, the high-limit has tripped and cut off heat. This is a critical safety condition.

**Causes in order of frequency:**
1. Controller setpoint drifted or was changed to an unsafe value
2. Temperature probe failure causing the controller to continue heating without feedback (often follows E03)
3. Contactor stuck closed — heat element or burner running continuously
4. High-limit thermostat failure (stuck open previously, then reseat caused overshoot)

**Fix steps:**
1. Shut the fryer off immediately. This is not a code to reset and ignore.
2. Allow oil to cool. Do not drain hot oil.
3. Check the setpoint is correct for the product being cooked (typically 325°F–375°F).
4. After cooling, inspect the contactor — if you can hear it clicking on and off normally during a test heat cycle, the control circuit is functioning.
5. Verify the probe reads accurately at known temperature (use a calibrated thermometer in the oil alongside the probe).
6. If the high-limit tripped, the fryer will not heat until it resets. Some models require manual reset at the high-limit thermostat body (located on the frypot). Follow the reset procedure in the service manual.
7. If the fryer repeatedly overshoots, replace the probe and recheck. If still overshooting, replace the controller.

---

### E06 — HEATING FAILURE

**What it means:** The controller sent a heat signal but did not detect the expected result — either the gas valve did not open, the ignition did not establish flame, or an electric contactor did not pull in. This code covers the entire heating circuit.

**Causes in order of frequency (gas fryers):**
1. Gas valve off at the source (first thing to check — simple operator error)
2. Air in gas lines during initial startup or after maintenance
3. Ignition module failure — spark not firing or flame not being sensed
4. Gas valve solenoid failed (no click when the controller calls for heat)
5. Open high-limit thermostat (not reset after a previous E05)
6. Failed interface board or loose wiring harness connector

**Causes in order of frequency (electric fryers):**
1. Contactor not pulling in (coil failed or 24V control signal missing)
2. Heating element open circuit
3. Open high-limit
4. Failed controller output

**Fix steps (gas):**
1. Confirm gas is on at the shutoff valve. This sounds obvious, but it accounts for a large percentage of E06 calls.
2. For air in lines: cycle the fryer off, wait 30 seconds, and try again. Air purges on the second or third ignition attempt in most cases.
3. Listen for the igniter spark — you should hear clicking for 90 seconds during the ignition trial. No clicking means the ignition module or spark cable is at fault.
4. Check the flame sensor rod. Carbon buildup on the sensing electrode causes the module to cut out even with a good flame. Clean with fine steel wool.
5. Check the gas valve with a manometer — incoming and manifold pressure should match the rating plate spec.
6. Inspect the high-limit reset button on the frypot body.

**Fix steps (electric):**
1. Check incoming power — full voltage at L1/L2/L3 to the power board.
2. Verify 24V control signal is reaching the contactor coil when the controller calls for heat.
3. Use a clamp meter on the heating element leads during a heat call — no current flow means the contactor is not pulling in or the element is open.
4. Check element resistance with power off: a standard element should be within 10% of the nameplate spec.

---

### E09 — PUMP NOT FILLING

**What it means:** During a filtration cycle, the filter pump ran but the return oil sensor detected no oil returning — usually because the filter pad is so clogged it is blocking flow, or the bypass has been activated.

**Causes:**
1. Filter pad (paper) at end of service life — heavily loaded with breading, sediment, or carbonized particles
2. Filter pad installed backward or creased
3. Filter pump motor or impeller worn
4. Filter bypass valve was manually opened and not closed

**Fix steps:**
1. Stop the filtration cycle.
2. Drain and cool the oil. Remove and inspect the filter pad — a collapsed or severely darkened pad confirms blockage.
3. Replace with a fresh filter pad, installed flush and flat in the filter pan.
4. Verify the bypass valve (if present) is fully closed.
5. If a new pad does not resolve it, verify the pump is running at speed and there are no cracks in the filter pan gasket allowing air infiltration.

---

### E10 / E11 — DRAIN VALVE NOT OPEN / NOT CLOSED

**What it means:** During a filtration sequence, the controller sent a signal to open (E10) or close (E11) the drain valve, but the confirmation switch did not confirm the valve reached the commanded position within the time allowed.

**Causes:**
1. Drain valve actuator (solenoid or motor) failed
2. Valve mechanically jammed with solidified shortening
3. Confirmation microswitch out of position or failed
4. Wiring harness connector at the valve loose or corroded

**Fix steps:**
1. At cool-down, attempt to manually operate the drain valve.
2. Inspect for solidified oil around the valve seat — this is common when fryers sit idle and shortening hardens in the valve.
3. Gently warm the valve area (not with a torch — use a heat gun at low temperature) to soften hardened shortening.
4. Test the valve solenoid for continuity and correct resistance per the parts spec.
5. Inspect the microswitch alignment and adjustment. Most confirmation switches can be repositioned without replacing the entire valve assembly.

---

### E12 / E13 — RETURN VALVE NOT OPEN / NOT CLOSED

Same diagnostic approach as E10/E11. The return valve controls oil flow back from the filter pan into the frypot. Solidified shortening and actuator failure are the dominant causes.

---

### E19 — M3000 CAN TX FULL (CAN Communication Lost)

**What it means:** On multi-vat fryers with a Master Interface Board (MIB), the controllers communicate over a CAN bus. E19 means the communication link is saturated or broken.

**Causes:**
1. Loose CAN cable connector between one of the cooking controllers and the MIB
2. Software version mismatch — one controller was updated without the others
3. Failed CAN transceiver on one of the boards
4. Defective controller

**Fix steps:**
1. Power off the fryer. Reseat each CAN bus connector — these are typically labeled on the back of each computer module.
2. Press TEMP on each controller display to check the software version number. All controllers in the same fryer system must run the same version.
3. If one controller shows no version or a different version, it may need a software update or replacement.
4. If all connections are secure and versions match, swap the suspect controller.

---

### E21 — CHANGE FILTER PAPER

**What it means:** Not an equipment fault. The 24-hour (or 25-hour on some models) filter change timer has expired, or the dirty-oil detection logic has triggered early based on oil quality. The fryer will not allow cooking until the filter is changed and the alert is acknowledged.

**Fix steps:**
1. Complete the filtration cycle if oil is at temperature.
2. Replace the filter pad.
3. Press YES to acknowledge and reset the timer.
4. If the code triggers before 24 hours, the dirty-oil algorithm detected elevated debris — inspect and change the pad even if it looks serviceable.

---

### E25 / E26 — RECOVERY FAULT / RECOVERY FAULT CALL SERVICE

**What it means:** Recovery time is how long the fryer takes to return to setpoint after a cook load is dropped. E25 triggers when recovery exceeds the limit once (1:40 for electric, 2:25 for gas). E26 triggers when it exceeds the limit on two or more consecutive cycles.

**Causes:**
1. Heating element degraded (electric) — reduced output extends recovery time
2. Gas orifice partially blocked or regulator pressure low
3. Burner tubes partially clogged with carbon deposits
4. Load too large for the fryer capacity
5. Temperature setpoint too close to the high-limit safety threshold, causing the controller to throttle back

**Fix steps for E25 (single occurrence):**
1. Clear the alarm with YES. Check if the cook load was within the recommended basket capacity.
2. Verify oil temperature is at setpoint before dropping product.
3. Check burner operation — a healthy gas fryer should show a strong, uniform blue flame.

**Fix steps for E26 (recurring):**
1. Inspect heating elements with a clamp meter for full current draw.
2. Check gas supply pressure at the manifold — should match the spec on the rating plate.
3. Remove and inspect burner tubes for carbon accumulation.
4. If neither supply nor load explains the slow recovery, the fryer is likely at end of life for its heating components.

---

### E27 — LOW TEMP ALARM

**What it means:** Oil temperature dropped more than 30°F below setpoint during idle mode, or more than 45°F during a cook cycle. Usually an informational alarm but indicates the fryer cannot maintain temperature.

**Common causes:** Large cook load dropped without pressing the cook timer first, fryer setpoint too low for volume, heating element underperforming.

**Fix:** Press YES to clear. If the alarm triggers without a corresponding large load, investigate the heating system using the E06 diagnostic steps.

---

### E28 — HIGH TEMP ALARM

**What it means:** Oil temperature rose 40°F above the setpoint. Warning stage before E05. The fryer has not yet tripped the high limit, but it is heading there.

**Causes:** Probe calibration drift, controller setpoint set too high, or contactor not dropping out properly.

**Fix:** Confirm the setpoint is correct. Verify the probe is accurate. If oil temperature continues rising beyond the setpoint without the controller cutting off heat, the contactor is suspect — check that it opens when the controller de-energizes the coil.

---

## How to Access the Error Log

**3000 Controller:**
1. Press and hold the TEMP button until the display shows the software version (about 3 seconds).
2. Navigate to TECH MODE using the up/down arrows.
3. Enter the tech code if prompted (default: 1234).
4. Select E-LOG. The last 10 errors display with timestamps.

**4000 / SMART4U Controller:**
1. From the main menu, press MENU > INFORMATION > E-LOG.
2. Errors display in order from most recent.
3. Each entry shows the error code, date, time, and fryer temperature at fault time.

---

## Frymaster Parts Reference

| Part | Part Description | Applies To |
|------|-----------------|-----------|
| Temperature probe (RTD) | Primary frypot temperature sensor, 2-wire RTD | MJCF, MJH, M3000/M4000 |
| High-limit thermostat | Safety cutoff at 410°F–425°F | All gas and electric models |
| Ignition module | Electronic spark-to-flame controller | Gas models (MJCF, MJH) |
| Igniter electrode assembly | Spark rod + ground rod in burner | Gas models |
| Flame sensor rod | Ionization sensing probe for flame confirmation | Gas models |
| Drain valve solenoid | Electrically actuated drain valve | MJCF, FPH, RE series |
| Return valve assembly | Return-line valve for filtration circuit | FPH, built-in filter models |
| Filter pump motor | Circulates oil during filtration | FPH, built-in filter models |
| MIB board | Master Interface Board — central communication hub | Multi-vat MJCF/MJH |
| 3000/4000 controller | Main cooking computer | MJCF, MJH, M3000, RE |
| Contactor (electric) | High-current switching relay for heating elements | Electric models only |
| Heating element | Immersion element, wattage per model | Electric models only |

---

## Quick-Clear Procedures

**Clearing a fault alarm:** Press YES when the alarm is active. This silences the alarm and clears the display but does not resolve the underlying fault — it will return if not fixed.

**Factory reset (Tech Mode):** Navigate to Tech Mode > Reset > Factory Reset. This returns the controller to default settings and clears all error logs. Use with caution — setpoints and custom programs will be lost.

**Manual high-limit reset:** If E05 has tripped, the high-limit thermostat on the frypot body (typically a small button on the thermostat housing) must be manually pressed to restore operation. The controller alone cannot reset a mechanically tripped high-limit.

---

## When to Call a Factory Authorized Service Agent

Some Frymaster faults require a licensed FAS (Factory Authorized Service) technician:

- **E05 (HOT HI 1)** that recurs after a verified probe and setpoint check
- **E06** on gas fryers where the gas valve, ignition module, and supply pressure have all been verified normal — this often indicates a controller board failure that must be diagnosed with Frymaster service software
- **E26 (RECOVERY FAULT CALL SERVICE)** that persists after burner/element inspection
- Any fault involving the MIB board or CAN bus if individual controller swap does not resolve the issue
- Any situation where oil temperature cannot be reliably controlled

Frymaster's technical support line is available 24/7 for service center coordination on in-warranty equipment.

---

## Parts and Supply Links

For replacement probes, high-limits, igniters, and control boards:

- **[Frymaster Temperature Probe (RTD)](https://www.amazon.com/s?i=industrial&k=frymaster+temperature+probe+RTD&tag=errorcodefixes-20)** — verify OEM part number before ordering
- **[Frymaster Ignition Module Replacement](https://www.amazon.com/s?i=industrial&k=frymaster+ignition+module+commercial+fryer&tag=errorcodefixes-20)**
- **[Frymaster High Limit Thermostat](https://www.amazon.com/s?i=industrial&k=frymaster+high+limit+thermostat&tag=errorcodefixes-20)**
- **[Commercial Fryer Filter Pads](https://www.amazon.com/s?i=industrial&k=commercial+fryer+filter+pads&tag=errorcodefixes-20)**
- **[Drain Valve Solenoid Commercial Fryer](https://www.amazon.com/s?i=industrial&k=frymaster+drain+valve+solenoid&tag=errorcodefixes-20)**
