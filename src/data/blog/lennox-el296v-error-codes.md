---
title: "Lennox EL296V Error Codes — Variable-Speed Furnace Diagnostic Guide"
description: "Lennox EL296V error codes: complete fault code reference, LED flash sequence guide, common causes, step-by-step fixes, and OEM parts list for this two-stage variable-speed gas furnace."
pubDatetime: 2026-04-24T08:00:00Z
modDatetime: 2026-04-24T08:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - lennox
  - furnace
  - error-codes
  - diagnostics
---

## Lennox EL296V Error Codes — What They Mean

The Lennox EL296V is a two-stage, variable-speed ECM blower, 96% AFUE gas furnace. It is one of Lennox's most capable residential furnaces, designed for zoning systems, communicating iComfort setups, and high-comfort applications. When paired with an iComfort thermostat, fault codes appear directly on the thermostat display as 3-digit codes. When operating standalone (non-communicating), fault codes blink on the furnace control board's status LED.

**Reading the LED blink code:** The LED blinks a pattern of slow flashes followed by fast flashes. For example: 4 slow blinks, pause, 3 fast blinks = error code 4-3 (listed as "43" in this guide). The full code repeats after a 3-second pause.

The EL296V uses the same Lennox diagnostic code system as the SLP98V and SL280UHV. This means each code has its own dedicated diagnostic path — and most codes have dedicated articles on this site.

[Jump to Fix](#step-by-step-fix)

### EL296V Complete Error Code Reference

| Code | Category | Fault Description |
|------|----------|------------------|
| 11 | Pressure | Low-pressure switch stuck open — no call for heat |
| 12 | Pressure | Low-pressure switch stuck open — during call for heat |
| 13 | Pressure | Limit switch fault history present |
| 14 | Pressure | High-pressure switch stuck open |
| 15 | Pressure | High-pressure switch stuck closed |
| 21 | Ignition | Rollout switch open (requires manual reset) |
| 22 | Ignition | Ignition failure — no flame on trial |
| 23 | Ignition | Flame sensed out of sequence |
| 24 | Ignition | Secondary voltage fault |
| 25 | Pressure | Pressure switch cycling during call for heat |
| 31 | Limit | High limit tripped — overheating detected |
| 32 | Limit | Low limit tripped |
| 33 | Limit | Limit switch opened 5+ times — lockout |
| 34 | Limit | Ignition proving fault — flame lost after proving |
| 41 | Motor | Inducer motor RPM failure |
| 42 | Motor | Indoor (blower) ECM motor fault |
| 43 | Motor | Indoor blower motor fault — check ECM module |
| 44 | Motor | ECM motor fault during variable speed ramp |
| 45 | Motor | Igniter fault — open or failed silicon nitride igniter |
| 52 | Power | Low flame signal — weak flame sense or dirty rod |
| 56 | Power | Induced draft fault — pressure switch not closing |
| 58 | Power | Power interruption — furnace cycled on/off during heating |

### Most Searched EL296V Codes

**Code 31 — High Limit Tripped:**
The most common fault on the EL296V. The high-limit switch opens when the heat exchanger temperature exceeds the rated limit (typically 170–200°F). Cause is almost always restricted airflow: dirty filter, blocked return, or malfunctioning ECM blower. Unlike single-speed furnaces, the EL296V's variable-speed blower should ramp up automatically in response to temperature rise — if the blower doesn't respond, the ECM module may be failing.

**Code 22 — Ignition Failure:**
The EL296V uses a silicon nitride hot surface igniter rated for approximately 7–10 years. After the ignition lockout, the board will retry 3 times before locking out with code 22. Check the igniter resistance (should be 15–100 Ω when cold on SiN igniters) and inspect for cracks or contamination.

**Code 42/43 — ECM Blower Motor Fault:**
The EL296V's variable-speed blower uses a communicating ECM motor. When the motor reports a fault to the control board, codes 42 or 43 appear. Check all electrical connections at the motor, the data cable from the board to the motor, and the 120/240VAC power terminals. The ECM module (the black "brain box" attached to the motor) can fail independently of the motor windings and is replaceable without replacing the full motor assembly.

**Code 56 — Pressure Switch Not Closing:**
The EL296V has a two-stage inducer and two-stage pressure switches. In first-stage heat, the low-stage pressure switch must close. In second stage, the high-stage switch must close. A code 56 means the appropriate switch did not close during the inducer pre-purge. Check for blocked condensate drain, cracked inducer housing, or a pressure switch hose that has slipped off its port.

## Common Causes

- **Code 31 / 33 (high limit):** Dirty air filter is #1. The EL296V's variable-speed blower can compensate for moderate airflow restriction, but it has a maximum RPM ceiling. A severely clogged filter still causes limit trips. Also inspect the blower wheel for dust caking — a caked blower wheel reduces airflow 30–40% even with a new filter.
- **Code 22 (ignition failure):** Failed or cracking silicon nitride igniter, gas supply issue (verify gas valve opens — you should hear a click and smell gas briefly), failed gas valve.
- **Codes 41/42/43 (motor faults):** ECM module failure, loose data cable, supply voltage issue. The EL296V requires a clean 120VAC supply — voltage sags below 105VAC cause motor fault codes.
- **Code 56 (pressure switch):** Blocked condensate drain is a very common cause. The EL296V is a high-efficiency (condensing) furnace — it produces condensate. A clogged drain creates back-pressure that the inducer can't overcome, so the pressure switch never closes.
- **Code 21 (rollout switch):** A rollout switch trip is a serious safety event. It means flame is leaving the combustion chamber in the wrong direction (rollout). Cause: blocked flue, cracked heat exchanger, failed inducer. Requires manual reset button on the rollout switch — but do not reset without finding the root cause.

## Step-by-Step Fix {#step-by-step-fix}

**Safety:** Turn off the furnace at the thermostat. Flip the furnace power switch (located on the side of the furnace near the door) to OFF. For gas issues, turn off the gas shutoff valve on the gas line upstream of the furnace.

1. **Write down the error code.** The LED blinks on the circuit board inside the burner compartment (lower door). Count the slow-fast pattern. Some board revisions also have a small LCD strip that shows the last 5 faults — check for that before cutting power.

2. **Code 31/33 — high limit — replace the filter first.** Pull the filter and check it against light. If you can't see light through it, replace it immediately. Also inspect the blower wheel through the lower compartment — if it's caked with gray fuzz, clean it before resetting.

3. **Code 22 — test the igniter.** Turn off the gas and power. Remove the igniter (two screws, one wire harness plug). Inspect for cracks — even a hairline crack causes intermittent failure. Test resistance with a multimeter (15–100 Ω is normal for silicon nitride igniters). A reading of OL = failed, replace.

4. **Code 56 — check the condensate drain.** Locate the condensate drain line (white PVC pipe, exits at the bottom of the furnace). Pour a cup of water into the condensate trap — if it doesn't drain freely, the trap or drain line is blocked. Clear with a wet/dry vac or by blowing compressed air through the drain.

5. **Codes 42/43 — check ECM motor connections.** Open the blower compartment (lower door). Locate the ECM motor — it has two connectors: a large power connector and a smaller data connector. Firmly reseat both. Also check the 5-pin data cable that runs from the circuit board to the motor (it can work loose over time). If reseating clears the fault, the connection was intermittent.

6. **Code 21 — rollout switch (requires professional follow-up).** The manual-reset rollout switch is a red or white button on the burner panel near the heat exchanger opening. Press and hold 3 seconds to reset. IMPORTANT: A tripped rollout switch indicates a potential heat exchanger crack or flue blockage — do not continue operating without professional inspection.

7. **For any code that returns after your fix:** The EL296V stores a fault history. After completing your repair, run the furnace through 2–3 full heat cycles and monitor for recurrence. If the same code returns, the root cause has not been resolved.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Typical Cost | Where to Buy |
|------|-------------|---------------|
| Silicon nitride igniter (Lennox #31W22 / Honeywell Q4100C universal) | $25–$65 | [Amazon](https://www.amazon.com/s?k=silicon+nitride+igniter+Lennox+furnace+Q4100&tag=errorcodefixes-20) |
| High limit switch (Lennox OEM — match temp rating) | $20–$55 | [Amazon](https://www.amazon.com/s?k=Lennox+high+limit+switch+furnace&tag=errorcodefixes-20) |
| Pressure switch — low stage (Lennox OEM) | $25–$60 | [Amazon](https://www.amazon.com/s?k=Lennox+furnace+pressure+switch+two+stage&tag=errorcodefixes-20) |
| ECM blower motor module (Lennox #100662-01 or match module) | $180–$450 | [Amazon](https://www.amazon.com/s?k=Lennox+ECM+blower+motor+module+variable+speed&tag=errorcodefixes-20) |
| Control board (Lennox OEM — match board number on label) | $200–$500 | [Amazon](https://www.amazon.com/s?k=Lennox+EL296V+control+board&tag=errorcodefixes-20) |
| Condensate trap / drain assembly | $12–$35 | [Amazon](https://www.amazon.com/s?k=furnace+condensate+trap+drain+kit+PVC&tag=errorcodefixes-20) |
| Rollout switch (manual reset, Lennox OEM) | $15–$40 | [Amazon](https://www.amazon.com/s?k=Lennox+furnace+rollout+switch+manual+reset&tag=errorcodefixes-20) |

## When to Call a Professional

**DIY-accessible repairs** on the EL296V: Igniter replacement, filter change, condensate drain cleaning, pressure switch hose reconnection, ECM connector reseating.

**Call a licensed HVAC tech for:**
- Code 21 (rollout switch) — requires combustion analysis and heat exchanger inspection before resuming operation.
- Code 41 (inducer motor failure) — inducer replacement requires gas line procedures.
- Codes 42/43 that return after connector reseating — the ECM module or blower assembly requires hands-on diagnosis with a communicating tool (Lennox's iComfort Diagnostic Tool reads live data).
- Any code 22 that persists after igniter replacement — may indicate gas valve failure or a combustion air/venting issue.

> **EL296V owner tip:** The EL296V's iComfort thermostat displays error codes in plain English. If your thermostat shows "Code 31 — High Limit Fault," that's exactly what's in this article. Take a photo of the thermostat display — it captures the code, the date/time, and the number of occurrences, which is extremely useful information for your technician.

## See Also

- [Lennox Furnace Error Codes — Master Reference](/posts/lennox-furnace-error-codes/)
- [Lennox SLP98V Error Codes — Variable-Capacity Furnace Guide](/posts/lennox-slp98v-error-codes/)
- [Lennox SL280UHV Error Codes — Two-Stage Variable-Speed Guide](/posts/lennox-sl280uhv-error-codes/)
- [Lennox Error Code 434 — Ignition Lockout Fix](/posts/lennox-error-code-434/)
- [Lennox Error Code 411 — High Limit Diagnosis](/posts/lennox-error-code-411/)
- [Lennox iComfort Error Codes — Communicating System Guide](/posts/lennox-icomfort-error-codes/)

## Related Articles

- [Lennox Error Code 292 — Ignition Failure Fix](/posts/lennox-292-error-code/)
- [Lennox Elite Series Furnace Error Codes — Fault Code Diagnostic Guide](/posts/lennox-elite-series-furnace-codes/)
- [Lennox 103 Error Code — Causes & Fix](/posts/lennox-error-code-103/)
- [Lennox Error Code 111 — Causes & Fix](/posts/lennox-error-code-111/)
- [Lennox Error Code 114 — Causes & Fix](/posts/lennox-error-code-114/)
