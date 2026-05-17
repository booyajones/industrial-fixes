---
title: "PTAC Error Codes — All Brands Complete Fix Guide"
description: "PTAC error codes for Amana, GE, LG, Islandaire, and Friedrich. What each code means and how to fix it."
pubDatetime: 2026-04-27T20:00:00Z
modDatetime: 2026-04-27T20:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - hvac
  - ptac
---

Hotel and motel maintenance techs often service dozens of identical PTAC units across a property. When a guest calls the front desk at midnight about a dead unit, you need to know within 60 seconds whether the fix is a reset, a filter clean, or a part swap. This guide covers every error code across the major PTAC brands — Amana, GE Zoneline, LG, Friedrich, and Islandaire — with brand-specific diagnostic mode entry, code meanings, and concrete fix steps.

---

## What Is a PTAC?

A Packaged Terminal Air Conditioner (PTAC) is a self-contained heating and cooling unit installed through an exterior wall. The entire refrigerant circuit — compressor, condenser, evaporator, and controls — is in one chassis. Models include cooling-only (PTC), heat pump with electric backup (PTH), and electric heat with cooling (PTAC).

Because PTACs share a wall sleeve, swapping a failed unit takes under 30 minutes for a trained tech. The question is almost always: **replace the unit or fix the fault?**

Use this guide to decide.

---

## Brand-by-Brand Error Code Reference

### AMANA PTH / PTC Series

Amana PTACs are the most common in U.S. hotels. The PTH series is a heat pump model; PTC adds electric strip heat. Both use the same control board and diagnostic system.

#### Entering Diagnostic Mode — Amana

1. Locate the UP (+) and DOWN (–) arrow buttons on the control panel.
2. Hold UP and DOWN simultaneously, then press **COOL twice** while holding both.
3. If no fault is present, the display shows **—** (two dashes).
4. If a fault exists, the fault code appears on the display.

#### Resetting an Amana PTAC

1. Ensure the unit is plugged in.
2. Remove the front panel to access the master switch.
3. Turn the master switch OFF for at least 5 seconds.
4. Hold COOL and HEAT simultaneously, then turn the master switch back ON.
5. A red indicator near the OFF button confirms a successful reset.

#### Amana Error Code Table

**Failure Codes (require part replacement)**

| Code | Meaning | Component | Fix |
|------|---------|----------|-----|
| F1 | Indoor black thermistor AND wireless thermostat both failed | Both components | Replace both thermistor and thermostat |
| F2 | Wireless thermostat failed; indoor black thermistor OK | Wireless thermostat | Replace wireless thermostat |
| F3 | Indoor black thermistor failed; thermostat OK | Black indoor thermistor | Replace indoor thermistor |
| F4 | Red indoor thermistor failed | Red indoor thermistor | Replace red indoor thermistor |
| F5 | Wireless thermostat signal lost | Wireless thermostat | Replace wireless thermostat |
| F6 | Yellow indoor discharge thermistor out of tolerance | Yellow indoor discharge thermistor | Replace yellow discharge thermistor |
| D4 | Exit temperature sensor failed | Exit tube sensor | Reset; if persists, replace sensor |

**Refrigeration Errors (cooling circuit issues)**

| Code | Meaning | Typical Cause | Fix |
|------|---------|--------------|-----|
| C1 | Indoor coils freezing | Dirty air filter, low refrigerant, failed blower | Clean filter; check refrigerant; inspect blower |
| C3 | Indoor coils freezing (second trigger condition) | Same as C1 | Same as C1 |
| C4 | Indoor coils freezing (third trigger condition) | Low refrigerant, dirty coil | Call refrigeration tech for refrigerant check |
| C6 | Component performance fault — overall | Compressor, blower, or fan motor degraded | Inspect all three; replace failed component |
| C7 | Freeze warning — coils approaching freeze point | Low refrigerant, restricted airflow | Clean filter; call tech for refrigerant check |

**Airflow Alerts**

| Code | Meaning | Cause | Fix |
|------|---------|-------|-----|
| C2 | Indoor air recirculating — unit cannot draw fresh air | Dirty filter, failed vent seal, vent door open | Clean filter; check vent seal; close vent door |
| C5 | Outdoor coils overheating | Blocked condenser, debris on outside of sleeve | Clear debris from outdoor side of unit |
| L6 | Discharge air too hot | Restricted airflow, dirty filter | Clean filter; clear obstruction around indoor side |
| LC | Outdoor thermistor reading excessive heat | Dirty condenser coils, failed condenser fan | Clean coils; inspect condenser fan motor |
| L7 | Outdoor unit power issue | Insufficient power to outdoor section | Call licensed tech |

**System Mode / Operational Codes (informational)**

| Code | Meaning | Action |
|------|---------|--------|
| FP | Freeze protection active — ambient below 40°F | Move to warmer environment or let temperature rise |
| EH | Emergency Hydronic mode — compressor bypassed, using hot water coil | Turn on EHH switch; verify hydronic supply |
| EO | Service board configuration error | Reset unit |
| HP | Heat Sentinel mode — overtemp protection active | Allow unit to cool; no action required |
| LS | Load shedding — compressor and electric heat cut off | Turn on LS switch at electrical panel |
| Op / Up | Open door or window detected | Close the door or window near the unit |
| ON | Wired thermostat mode active, wireless expected | Change thermostat configuration in settings |
| Br | Brown-out protection — incoming voltage too low | Check breaker, verify 208V/230V supply |

---

### GE Zoneline AZ Series

GE Zoneline PTACs (AZ45, AZ65, AZ75 series) use a two-part diagnostic system: **LED blink codes** on the power board and **display codes** on the control panel. When a fault is active, the LED on the power board blinks repeatedly in bursts with a pause between cycles — count the blinks per burst.

#### GE Diagnostic Blink Codes and Display Codes

| LED Blinks | Display Code | Fault | Description |
|-----------|-------------|-------|-------------|
| 1 | No Err | Normal | No faults detected |
| 2 | E2 | Indoor air temperature probe failure | Indoor ambient thermistor shorted or open |
| 3 | E3 | Outdoor air temperature probe failure | Outdoor thermistor shorted or open |
| 4 | E4 | Communication failure | Display board cannot communicate with power board |
| 5 | E5 | Keypad fault — key stuck | One or more buttons on display board stuck or shorted |
| 6 | E6 | Remote thermostat input failure | Wired thermostat input circuit fault |
| 7 | E7 | Linesync timing failure | Power board cannot read 60 Hz line sync — power quality issue |
| 8 | E8 | Outdoor coil switch open — compressor disabled | Outdoor coil freeze stat or high-pressure switch open |
| 9 | E9 | Hydronic switch open | Hydronic heating coil switch circuit open (if configured) |
| 10 | E10 | Configuration read failure | Internal EEPROM configuration data corrupt |
| 11 | E11 | Module mismatch | Display board connected to incompatible power board revision |

#### Entering GE Zoneline Diagnostic Mode

1. On AZ45/AZ65 models with a digital display: press and hold the **Fan** and **Unit On/Off** buttons simultaneously for 5 seconds.
2. The display enters diagnostic mode and shows any stored fault codes.
3. On models without a digital display: use the LED blink codes on the power board — access by removing the front panel and observing the indicator LED while power is applied.

#### GE E2 — Indoor Air Temperature Probe

The indoor thermistor reads temperature for the control board to regulate cooling and heating. A failed probe causes erratic setpoint behavior or total control board lockout.

**Fix steps:**
1. Locate the indoor thermistor — a small bead thermistor typically clipped to the return air intake area behind the filter.
2. With the unit unplugged, disconnect the thermistor connector and measure resistance. At room temperature (~70°F), most PTAC thermistors measure approximately 10kΩ.
3. An open circuit (infinite resistance) or a short (near 0Ω) confirms thermistor failure.
4. Replace the thermistor. In most GE Zoneline units, the thermistor is a plug-in component costing $15–$30 from PTAC parts suppliers.
5. If resistance is in spec but E2 persists, the fault may be on the power board's sensor input circuit — replace the power board.

#### GE E4 — Communication Failure

The display board and power board communicate over a serial connection via the ribbon cable or connector bundle linking the two boards.

**Fix steps:**
1. Unplug the unit.
2. Inspect the connector between the display board and power board. Corrosion on pins is common in humid coastal environments.
3. Reseat the connector. If pins are corroded, clean with electrical contact cleaner.
4. If the connector is secure and clean but E4 persists, check the compatibility — E11 (module mismatch) often accompanies E4 when a replacement display board of the wrong revision is installed.
5. If all connections are correct, the power board has likely failed and needs replacement.

#### GE E11 — Module Mismatch

This code appears when a display board is replaced with an incompatible revision. GE Zoneline has multiple display board variants across the AZ45/AZ65/AZ75 product line.

**Fix steps:**
1. Note the model number on the unit's rating label inside the access door.
2. Verify the replacement display board part number is correct for that specific model and revision — not just the BTU capacity.
3. If the board was replaced as part of a repair, swap it for the correct revision.

---

### LG LP Series PTACs

LG LP series PTACs (LP071CED3A, LP121CED3A, LP151CED3A) use the **CH** fault code system familiar from LG mini-splits.

#### LG PTAC Error Code Table

| Code | Fault | Meaning |
|------|-------|---------|
| CH01 | Indoor room temperature sensor (TA) failure | Indoor ambient thermistor open or shorted |
| CH02 | Indoor coil temperature sensor (TC) failure | Evaporator coil thermistor open or shorted |
| CH03 | Outdoor temperature sensor failure | Outdoor ambient thermistor fault |
| CH05 | Communication error — indoor to outdoor | Signal wire fault between indoor control and outdoor PCB |
| CH06 | Outdoor fan motor locked or failed | Fan motor not rotating at startup |
| CH07 | Outdoor pipe temperature sensor failure | Outdoor liquid line thermistor fault |
| CH10 | Indoor fan motor speed fault | Indoor blower not reaching commanded speed |
| CH21 | High-pressure protection | High-pressure switch opened — refrigerant, blockage, or dirty coil |
| CH22 | Low-pressure protection | Low refrigerant level or blocked metering device |
| CH38 | Discharge temperature too high | Compressor discharge overheating — high load or restricted refrigerant flow |
| CH44 | Communication error (control board to power board) | Internal board communication fault |

#### Entering LG Diagnostic Mode

1. Press and hold the **MODE** and **FAN** buttons simultaneously for approximately 3 seconds.
2. The unit enters diagnostic mode — the display scrolls through any stored fault codes.
3. If no code is shown, the unit is functioning normally.
4. To clear codes: power cycle the unit (disconnect power for 30 seconds).

#### LG CH01 / CH02 — Temperature Sensor Faults

LG sensors are NTC thermistors. CH01 is the room-air sensor; CH02 is the coil sensor directly clamped to the evaporator coil.

**Fix steps:**
1. Access the evaporator coil (remove front panel and filter). The CH02 sensor is typically a small thermistor probe clipped into the evaporator coil fins.
2. Measure resistance: at 77°F (25°C), the LG thermistor should read approximately 10kΩ (check model-specific service data for exact values).
3. Replace the failed thermistor. Verify the replacement sensor type matches the original (resistance curve must match).
4. Reconnect and power on. Clear fault with a power cycle.

#### LG CH21 — High-Pressure Protection

The high-pressure switch cut the compressor circuit. Most common causes: dirty outdoor coil, ambient temperature too high, refrigerant overcharge, or restricted airflow at the outdoor side.

**Fix steps:**
1. Power off the unit and let the system equalize for 5 minutes.
2. Inspect the outdoor face of the unit through the wall sleeve. Clear any debris, lint, or leaves blocking the condenser.
3. Check if outdoor ambient temperature is within the rated operating range (typically 65–115°F for cooling mode).
4. If the coil is clean and ambient is in range, the system may be overcharged or have a blockage — call a licensed refrigeration technician.

---

### Friedrich EP / PH Series PTACs

Friedrich EP (cooling-only) and PH (heat pump) series PTACs are common in hotels, universities, and senior living facilities. Friedrich uses a numeric error code system displayed on the unit's LCD panel.

#### Friedrich PTAC Error Code Table

| Code | Fault | Description |
|------|-------|-------------|
| E1 | Indoor coil temperature sensor failure | Evaporator thermistor shorted or open |
| E2 | Room temperature sensor failure | Indoor ambient thermistor fault |
| E3 | Outdoor coil temperature sensor failure | Condenser coil thermistor fault |
| E4 | Discharge temperature sensor failure | Compressor discharge thermistor fault |
| E5 | Outdoor ambient temperature sensor failure | Outdoor ambient thermistor open or shorted |
| E6 | Communication error — control board to display | Board-to-board communication fault |
| E7 | EEPROM data fault | Configuration data checksum error on control board |
| E8 | Compressor overload or protection trip | Compressor thermal protection or high-pressure switch activated |
| E9 | Indoor fan motor fault | Indoor blower motor not operating at commanded speed |
| P1 | High-pressure protection | High-pressure cutout activated |
| P2 | Low-pressure protection | Low-pressure cutout activated — low refrigerant suspected |
| P3 | Freeze protection activated | Coil temperature below freeze threshold |
| H1 | Defrost in progress | Normal in heat pump mode — unit temporarily in defrost cycle |

#### Entering Friedrich Diagnostic Mode

1. On current EP/PH models: press and hold the **FAN** and **COOL** buttons simultaneously for 5 seconds with the unit powered on.
2. The LCD displays any active or stored fault codes.
3. On older Friedrich models without a digital display, a red fault LED on the control board blinks codes similar to GE's blink-code system.

#### Friedrich E1 / E3 — Coil Sensor Failures

Friedrich coil sensors are NTC thermistors similar to other PTAC brands. E1 is the evaporator (indoor) coil; E3 is the condenser (outdoor) coil.

**Fix steps:**
1. Access the coil the sensor monitors. Coil sensors are clipped directly into the fin array.
2. Verify the sensor clip is seated in the fins — they can dislodge during filter cleaning.
3. Measure the sensor resistance. Friedrich thermistors typically read 10kΩ at 77°F. Open or shorted = failed.
4. Replace the thermistor. Part numbers vary by model — confirm from the Friedrich parts catalog or the unit's service label.

#### Friedrich E8 — Compressor Protection

The compressor's thermal overload or the high-pressure switch opened. The compressor will not run until the protection resets.

**Fix steps:**
1. Power off the unit and allow 15–20 minutes for the compressor to cool and for the pressure to equalize.
2. Inspect the outdoor side for airflow obstructions.
3. Power the unit back on. If E8 immediately returns without a warm restart, the compressor is likely at end of life or the refrigerant circuit has a fault.
4. Recurring E8 codes without obvious cause (clean coils, normal ambient, good airflow) require a refrigeration technician.

#### Friedrich P3 — Freeze Protection

The indoor coil temperature sensor detected coil temperatures approaching freezing point. The unit will stop the compressor to allow defrost.

**Fix steps:**
1. Check the air filter — a clogged filter is the most common cause of P3 in heating and cooling mode.
2. Verify the indoor fan is running. If the blower stops running, the coil freezes rapidly.
3. If the filter is clean and the fan is operating, low refrigerant is the most common remaining cause. Call a licensed tech.
4. Allow the coil to fully defrost before re-energizing the compressor.

---

### Islandaire PTACs

Islandaire builds PTACs primarily for hospitality markets. Their control board uses the same diagnostic code architecture as Amana/GE (they source control boards from similar OEM suppliers), with E-codes for sensor faults and blink codes on the power board LED.

#### Islandaire Error Codes

| Code | Fault |
|------|-------|
| E2 | Indoor air temperature sensor failure |
| E3 | Outdoor air temperature sensor failure |
| E4 | Communication failure between display and power board |
| E5 | Keypad stuck key |
| E8 | Outdoor coil freeze stat — compressor disabled |
| E10 | Internal configuration error |
| E11 | Control board module mismatch |

Diagnostic entry and reset procedures for Islandaire are identical to GE Zoneline: count LED blinks on the power board, or enter display diagnostic mode via simultaneous button hold. Consult the model-specific service documentation for the exact button combination, as it varies by chassis generation.

---

## Cross-Brand Fault Code Comparison

| Fault Type | Amana | GE Zoneline | LG | Friedrich | Islandaire |
|------------|-------|------------|-----|-----------|-----------|
| Indoor air sensor | F1/F3 | E2 | CH01 | E2 | E2 |
| Indoor coil sensor | F6 | — | CH02 | E1 | — |
| Outdoor sensor | — | E3 | CH03 / CH07 | E3 | E3 |
| Communication | E4 | E4 | CH05 / CH44 | E6 | E4 |
| High pressure | C6 | E8 | CH21 | P1 | E8 |
| Low pressure | C1/C3 | — | CH22 | P2 | — |
| Freeze protection | FP / C7 | — | — | P3 | — |
| Compressor overload | C6 | E8 | — | E8 | E8 |
| Board config fault | EO | E10 | — | E7 | E10 |
| Board mismatch | — | E11 | — | — | E11 |
| Brownout / low voltage | Br | E7 | — | — | — |
| Fan motor fault | — | — | CH06 / CH10 | E9 | — |

---

## Diagnostic Mode Entry — All Brands Quick Reference

| Brand | Method |
|-------|--------|
| Amana PTH/PTC | Hold UP + DOWN; press COOL twice while holding |
| GE Zoneline AZ | Hold FAN + UNIT ON/OFF for 5 seconds; or count power board LED blinks |
| LG LP series | Hold MODE + FAN for 3 seconds |
| Friedrich EP/PH | Hold FAN + COOL for 5 seconds |
| Islandaire | Count power board LED blinks; or hold unit-specific button combo (check service label) |

---

## Replace vs. Repair Decision Guide

PTAC replacement is often faster and cheaper than component-level repair. Use this framework:

**Replace the unit if:**
- Compressor has failed (codes: CH21 recurring, E8 recurring, C6 with confirmed dead compressor)
- Refrigerant leak confirmed and unit is over 5 years old
- Both the power board and display board have failed
- The unit is over 8–10 years old and showing multiple simultaneous faults

**Repair the unit if:**
- Fault is a thermistor or sensor (F-codes, E2/E3, CH01/CH02) — sensors are $15–$40 and install in under 15 minutes
- Fault is a display board (E4, E11) — board swaps take under 20 minutes
- Fault is a dirty filter or coil (C2, C5, F1 filter-related) — maintenance only
- Fault is a stuck fan motor or blower — motors are $40–$80 and the unit is otherwise serviceable

**Hotel property rule of thumb:** If a unit is under 5 years old and the compressor is confirmed good, repair it. If it's over 8 years old, a replacement chassis installed in the existing wall sleeve is often the same labor cost and eliminates future call-backs.

---

## Resetting PTAC Codes by Brand

| Brand | Reset Method |
|-------|-------------|
| Amana | Master switch OFF 5 seconds; hold COOL + HEAT; switch ON |
| GE Zoneline | Power cycle at circuit breaker for 30 seconds |
| LG | Disconnect power for 30 seconds; reconnect |
| Friedrich | Power cycle at disconnect; or hold MODE button for 5 seconds if displayed |
| Islandaire | Power cycle at circuit breaker for 30 seconds |

**Note:** Resetting clears the displayed code but not the fault history (where applicable). The code will return if the root cause is not resolved.

---

## Parts Reference by Brand

| Part | Amana | GE Zoneline | Friedrich |
|------|-------|------------|----------|
| Indoor air thermistor | B1370209 series | WP12X10025 series | 60021801 series |
| Outdoor thermistor | B1370210 series | WP12X10028 series | 60021802 series |
| Control (display) board | B1370200 series | WP26X28 series | 60021200 series |
| Power board | B1370241 series | WP26X40 series | 60021250 series |
| Indoor blower motor | B1340026 series | WP6700 series | 67020000 series |
| Condenser fan motor | B1340025 series | WP6707 series | 67020100 series |
| Filter (washable) | M0-1056, M0-1057 | WP10X62 | 60130000 series |

*Always verify with your unit's full model number — BTU capacity alone does not determine part compatibility.*

---

## Parts and Supply Links

- **[Amana PTAC Thermistor Sensor Kit](https://www.amazon.com/s?i=industrial&k=amana+ptac+thermistor+sensor&tag=errorcodefixes-20)**
- **[GE Zoneline Control Board Replacement](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20)**
- **[Friedrich PTAC Parts](https://www.amazon.com/s?i=industrial&k=friedrich+ptac+replacement+parts&tag=errorcodefixes-20)**
- **[PTAC Filter Replacement Universal](https://www.amazon.com/s?i=industrial&k=ptac+replacement+filter+universal&tag=errorcodefixes-20)**
- **[PTAC Blower Fan Motor](https://www.amazon.com/s?i=industrial&k=ptac+blower+motor+replacement&tag=errorcodefixes-20)**
- **[LG PTAC Replacement Parts](https://www.amazon.com/s?i=industrial&k=lg+ptac+replacement+parts+CH+error&tag=errorcodefixes-20)**
