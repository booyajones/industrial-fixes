---
title: "Bradford White Infiniti K Tankless Water Heater Error Codes"
description: "Full fault code reference for the Bradford White Infiniti K condensing tankless water heater, covering all error codes, condensate drain faults, scale sensor diagnostics, and controller troubleshooting with step-by-step repair guides."
pubDatetime: 2026-04-25T00:00:00Z
author: "James Rutherford"
tags:
  - hvac
  - error-codes
---

The Bradford White Infiniti K Series is the premium condensing tankless line from Bradford White — a manufacturer known for high-quality water heaters made in the United States. The Infiniti K models (including the RKTM-199-NLX and similar models) deliver up to 199,000 BTU/hr with condensing efficiency, achieving up to 96% AFUE. The condensing design means added components — a secondary heat exchanger, a condensate collection system, and a scale sensor — all of which contribute their own fault modes.

This guide covers every Bradford White Infiniti K error code and what to do about each one.

## What Does the Bradford White Infiniti K Error Code Mean?

The displayed code tells you which part of the heater stopped operating within its safety limits. On the Infiniti K, that often means ignition, venting, condensate drainage, scale buildup, or a failed temperature sensor. Because this is a condensing tankless model, codes tied to the secondary heat exchanger and condensate system deserve quick attention.

## How to Read Infiniti K Error Codes

Error codes display on the front panel display as two-digit numbers. The unit also has a fault history log accessible through the navigation buttons. When a fault occurs:

1. The unit shuts down
2. The error code displays on the panel
3. The status LED may flash to indicate fault status

To reset most faults: press the Reset button on the front panel. If the fault is not auto-resettable (hard lockout), you must resolve the underlying condition and cycle power.

---

## Bradford White Infiniti K Error Codes

### Error 10 — Ignition Failure
The unit attempted to ignite the burner but did not detect flame within the ignition trial period.

**Causes:**
- Gas supply valve closed or low gas pressure
- Spark electrode gap incorrect or electrode fouled
- Gas valve not opening (solenoid failure)
- Blocked flue exhaust or air intake
- Flow below minimum activation threshold

**Fix:**
1. Confirm the gas supply valve is fully open
2. Check gas pressure at the unit — minimum 4" WC for natural gas, 8" WC for LP
3. Inspect the igniter electrode for carbon fouling or cracking
4. Check flue and air intake for blockage (insects, debris, ice in cold weather)
5. Verify minimum water flow — Infiniti K units require approximately 0.5 GPM to initiate

### Error 11 — Flame Loss During Operation
The unit lit successfully but lost flame signal during a heating cycle. The controller detected the flame rod stop reading current mid-operation.

**Causes:**
- Flame rod fouled with carbon buildup
- Gas supply pressure fluctuation (low during high-demand events)
- Burner assembly dirty

**Fix:** Clean or replace the flame rod. The rod should be a clean metal probe — carbon buildup is resistive and prevents proper ionization current. Clean with fine emery cloth. Also verify gas pressure remains adequate during high-demand events (other appliances running simultaneously).

### Error 12 — Abnormal Combustion
The unit detected abnormal combustion characteristics — often related to improper air-to-fuel ratio or recirculated flue gases.

**Causes:**
- Air intake screen obstructed
- Exhaust and intake terminations too close together (short-circuiting)
- Negative pressure in mechanical room
- Dirty burner or heat exchanger causing incomplete combustion

**Fix:** Inspect intake screen and verify vent terminations meet minimum separation requirements per the installation manual. Check for any nearby exhaust sources that could contaminate intake air.

### Error 14 — Thermal Fuse (Manual Reset Required)
The high-limit thermal fuse opened due to an overtemperature condition. This is a one-time fuse — it must be physically replaced.

**Causes:**
- Scale buildup on the primary heat exchanger restricting heat transfer
- Fan motor failure reducing exhaust draft
- Blocked flue

**Fix:** Do not simply replace the fuse and restart — identify the root cause first. If scale buildup is suspected, perform a descaling flush before replacing the fuse. Check fan motor operation. Replace the thermal fuse (part specific to the Infiniti K model).

### Error 16 — Outlet Temperature Too High
The hot water outlet temperature exceeded the upper safety limit (typically above 185°F).

**Causes:**
- Very low water flow through the unit
- Temperature setpoint too high
- Outlet temperature sensor failure (reading too low, causing overcorrection)

**Fix:** Verify flow rate is adequate. Check outlet sensor resistance. Reduce setpoint to 120–140°F if set higher.

### Error 29 — Scale Sensor Fault
The Bradford White Infiniti K includes a scale detection sensor (a proprietary feature called the Intellistat scale sensor on some models) that monitors for mineral scale accumulation in the heat exchanger. Error 29 indicates the scale sensor detected unacceptable scale buildup, or the sensor itself has failed.

**This is an important maintenance alert.** Scale buildup in a condensing heat exchanger is destructive — it reduces efficiency, causes overtemperature, and can cause premature heat exchanger failure.

**Fix:**
1. **Perform a descaling flush.** Use a commercially available descaler solution (white vinegar or purpose-built tankless descaler). The Infiniti K typically has service ports on the inlet and outlet lines designed for flush connection.
2. **Re-test after descaling.** If Error 29 clears after flushing, scale was the cause. Implement a regular descaling schedule (annually in hard water areas).
3. **If Error 29 persists after descaling,** the scale sensor itself may have failed. Locate the sensor in the heat exchanger section and test for proper resistance/continuity per the service manual.

### Error 31 — Inlet Temperature Sensor Fault
The cold water inlet thermistor failed or is reading outside the valid range.

**Fix:** Locate the inlet thermistor and check the connector first — loose plugs are common after installation or service. Test thermistor resistance at known water temperatures. Replace if out of spec.

### Error 32 — Outlet Temperature Sensor Fault
The hot water outlet thermistor failed.

**Fix:** Same procedure as Error 31. Test outlet thermistor resistance and replace if failed.

### Error 33 — Secondary Heat Exchanger Sensor Fault
The temperature sensor monitoring the secondary (condensing) heat exchanger failed or is reading abnormally.

**What it means:** The secondary heat exchanger is what makes the Infiniti K condensing — it extracts additional heat from flue gases and produces condensate as a byproduct. If the sensor monitoring it fails, the controller can't manage the condensing process properly.

**Fix:** Test the secondary HX thermistor. Also inspect the secondary heat exchanger for scale buildup or corrosion — if the unit has been running with an unaddressed condensate drain problem (Error 79/condensate faults), the secondary HX may have been damaged.

### Error 34 — Flue Temperature Too High
The flue gas temperature exceeded safe limits, indicating incomplete heat transfer.

**Causes:**
- Heavy scale buildup on primary heat exchanger
- Fan motor underperforming
- Blocked heat exchanger fins

**Fix:** Descale the unit. Test the exhaust fan operation.

### Error 41 — Fan Motor Fault
The combustion air/exhaust fan failed to reach the required RPM or the tachometer signal is absent.

**Fix:** Test the fan motor for free rotation. Check the tachometer signal from the motor. If the motor is seized or the tachometer is failed, replace the fan motor assembly.

### Error 51 — Gas Valve Fault
The gas valve solenoid circuit detected an abnormal condition.

**Fix:** Test solenoid coil resistance (expect 20–50Ω). Verify 24VAC or 120VAC supply voltage to the valve (check the service manual for the specific model's valve voltage). Replace if the coil is open or the valve doesn't actuate with proper voltage applied.

### Error 65 — Water Flow Sensor Fault
The flow sensor turbine failed, is fouled, or is producing an erratic signal.

**Fix:** Remove and clean the turbine. Check for debris. Test the sensor output with the service diagnostic tool or verify signal at the control board connector. Replace if fouled cleaning doesn't restore function.

### Error 70 — Controller (Control Board) Fault
The main controller detected an internal fault. This is a board-level error.

**Fix:** Check all wiring harness connections to the board. Power cycle the unit. If the fault persists, the control board likely needs replacement. Document the fault code and frequency before ordering a board — some intermittent Error 70 faults are actually power quality issues (voltage sags) rather than board failures.

### Error 79 — Condensate Drain Fault
The condensate drain system detected a problem — either the drain is blocked, the condensate sensor tripped, or the neutralizer is saturated.

**This is critical on condensing units.** Blocked condensate causes acidic water to back up into the secondary heat exchanger, rapidly corroding it.

**Fix:**
1. Locate the condensate drain line and clear any blockage
2. Inspect the condensate neutralizer — replace the limestone media if saturated (it turns dark and compact)
3. In freezing climates, check for ice in the condensate drain line
4. Test the condensate sensor if the drain appears clear
5. **After clearing:** Inspect the secondary heat exchanger for corrosion damage if the drain was blocked for an extended period

---

## How to Fix It

1. **Check gas supply** for any ignition-related errors (10, 11, 12) — this eliminates the most common cause immediately.
2. **Inspect condensate drain and neutralizer** for Error 79 — this is the most maintenance-sensitive component on the Infiniti K.
3. **Flush for scale** (Error 29, Error 34, Error 14) — hard water areas require annual maintenance.
4. **Test sensors before boards** — thermistors (Errors 31, 32, 33) fail at a much higher rate than control boards.
5. **Check fan operation** for Error 41 — a seized fan bearing causes cascading faults within hours.
6. **Document fault history** — use the navigation buttons to pull the fault log before resetting, especially for intermittent faults.

---

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| [Condensate Neutralizer Limestone Media](https://www.amazon.com/s?i=industrial&k=condensate+neutralizer+limestone+media+replacement&tag=errorcodefixes-20) | Error 79 — annual replacement on condensing units | $15–$40 |
| [Tankless Water Heater Descaler Flush Kit](https://www.amazon.com/s?i=industrial&k=tankless+water+heater+descaling+flush+kit&tag=errorcodefixes-20) | Errors 14, 29, 34 — annual scale removal maintenance | $25–$60 |
| [Gas Water Heater Flame Rod Sensor](https://www.amazon.com/s?i=industrial&k=gas+water+heater+flame+rod+ionization+sensor&tag=errorcodefixes-20) | Error 11 fix — flame rod replacement | $15–$40 |
| [Bradford White Thermocouple / Thermistor](https://www.amazon.com/s?i=industrial&k=Bradford+White+water+heater+thermistor+sensor&tag=errorcodefixes-20) | Errors 31/32/33 — temperature sensor replacement | $10–$35 |
| [Condensate Drain Line Tubing](https://www.amazon.com/s?i=industrial&k=condensate+drain+line+tubing+HVAC+water+heater&tag=errorcodefixes-20) | Replace cracked or frozen condensate drain lines | $10–$25 |

---

## When to Call a Pro

Call a licensed plumber or HVAC technician for:

- **Error 14 with recurring fuse failure** — root cause diagnosis required; likely severe scale buildup or fan failure
- **Error 29 that doesn't clear after descaling** — scale sensor replacement requires component-level access
- **Error 79 with secondary heat exchanger corrosion** — secondary HX replacement is a major repair
- **Error 51 (gas valve)** — gas system work requires licensed tradespeople in most jurisdictions
- **Error 70 (control board)** — board replacement needs proper programming/setup
- **Any error where the unit won't reset** — persistent hard lockouts often require on-site diagnosis

---

## Frequently Asked Questions

**Q: How often should I descale the Bradford White Infiniti K?**

A: In areas with hard water (above 120 mg/L or 7 gpg hardness), descale annually. In soft water areas, every 2 years is acceptable. The Infiniti K's scale sensor (Error 29) will alert you when scale buildup is detected, but don't wait for the error — proactive maintenance extends heat exchanger life significantly. Replacing a failed condensing heat exchanger costs $500–$1,500 in parts and labor; a yearly descale kit costs $30.

**Q: My Infiniti K shows Error 79 but the condensate drain line looks clear. What else should I check?**

A: After confirming the drain line is clear, check the condensate neutralizer — the limestone media inside can compact and block flow even when the downstream drain is open. Also verify the condensate collection pan isn't cracked or misaligned. If drain and neutralizer are both clear, test the condensate sensor itself — a failed sensor triggers Error 79 even with perfect drainage.

**Q: What's the difference between the Bradford White Infiniti K and Infiniti S series?**

A: The Infiniti K is a condensing unit (up to 96% AFUE) with a secondary heat exchanger and condensate system. The Infiniti S is a non-condensing tankless unit (approximately 82% AFUE) without condensate components. The error code systems are similar but the Infiniti K has additional fault codes specific to the condensing components (Errors 29, 33, 79). This guide applies specifically to the Infiniti K.
