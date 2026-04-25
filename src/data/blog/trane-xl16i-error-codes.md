---
title: "Trane XL16i Error Codes — Heat Pump Fault Code Diagnostic Guide"
description: "Complete Trane XL16i heat pump error codes: LED flash sequences, ComfortLink II fault codes, common causes, step-by-step fixes, and parts guide."
pubDatetime: 2026-04-24T08:00:00Z
modDatetime: 2026-04-24T08:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - trane
  - heat-pump
  - error-codes
  - diagnostics
---

## Trane XL16i Error Codes — What They Mean

The Trane XL16i (model numbers 4TWR4, 4TWR6, 4TWR8) is a 16–17 SEER single-stage communicating heat pump using the Climatuff scroll compressor and R-410A refrigerant. It is part of Trane's ComfortLink II communicating system, which means fault codes are displayed two ways:

1. **ComfortLink II thermostat display** — When paired with a ComfortLink II thermostat (XL950, XL850, XL824), fault codes appear as numeric codes on the screen along with a plain-language description.
2. **Outdoor board LED flash codes** — The outdoor control board has a diagnostic LED that blinks two-digit fault codes. These display when a ComfortLink thermostat is not connected, or for additional diagnostics.

To read the LED: open the electrical compartment panel on the side of the outdoor unit (2–4 screws). Count slow blinks (tens digit), then fast blinks (ones digit). A 3-1 code = three slow blinks, pause, one fast blink.

[Jump to Fix](#step-by-step-fix)

### XL16i LED Flash Code Reference

| Flash Code | Fault Description | Priority |
|------------|------------------|---------|
| 1-0 | Normal operation | — |
| 2-1 | Discharge line temperature sensor fault | Medium |
| 2-2 | Outdoor ambient temperature sensor fault | Medium |
| 3-1 | Low-pressure switch open / low refrigerant | High |
| 3-2 | High-pressure switch open / dirty coil or fan | High |
| 4-1 | Compressor start fault — hard start or capacitor | High |
| 4-2 | Compressor thermal overload tripped | High |
| 5-1 | Outdoor fan motor fault | High |
| 5-2 | Defrost control fault | Medium |
| 6-1 | Low-ambient lockout (below 0°F) | Low |
| 6-2 | High-discharge temperature protection | High |
| 7-1 | ComfortLink II communication fault | Medium |
| 7-2 | SAB data bus error | Medium |
| 8-1 | Control board fault — replace board | High |
| Steady on | System powered — no fault | — |

### ComfortLink II Thermostat Codes (XL950 / XL850)

When connected to a ComfortLink II thermostat, the XL16i reports faults with numeric codes in the **Alerts** menu (hold the Equipment button, then select Alerts). Common codes:

| Code | Description |
|------|------------|
| 173 | Low pressure switch — compressor off |
| 175 | High pressure switch — compressor off |
| 178 | Discharge temperature too high |
| 179 | Outdoor ambient sensor fault |
| 180 | Defrost sensor fault |
| 185 | Communication loss — outdoor unit |
| 190 | Compressor module fault |

## Common Causes

- **3-1 Low pressure fault:** Refrigerant leak or low charge. On the XL16i, the most common leak points are the Schrader valve cores, the flare fittings at the service valves, and the evaporator coil (if the indoor unit is original and more than 10 years old). Low pressure can also occur in heating mode if the outdoor coil is heavily iced and the defrost cycle is failing.

- **3-2 High pressure fault:** Dirty condenser coil is the primary culprit — the XL16i uses a louvered aluminum-fin coil that traps cottonwood, grass clippings, and dirt on the back side (interior of the coil). Also check for a failed outdoor fan motor or capacitor; if the fan isn't spinning, head pressure climbs quickly.

- **4-1 Compressor start fault:** The run capacitor (dual-rated for compressor and fan) is the first suspect. A capacitor that tests 20% or more below its rated µF value causes compressor hard starts and this code. Also check line voltage — the XL16i requires 208–240VAC at the unit; voltages below 197VAC cause start failures.

- **4-2 Compressor overload:** The scroll compressor has an internal thermal overload. This trips when the compressor runs excessively hot due to high head pressure, refrigerant overcharge, lack of suction superheat (liquid slugging), or a failing compressor winding. Allow the compressor 30–45 minutes to cool before attempting restart.

- **5-2 Defrost fault:** The XL16i uses a time-temperature defrost control. The defrost thermostat is clipped to the outdoor coil and must close below approximately 28°F. A failed defrost thermostat, failed defrost board relay, or failed reversing valve prevents defrost from completing. You'll see a heavily iced outdoor coil (more than a thin frost layer) and reduced heating performance.

- **7-1 Communication fault:** This code fires when the outdoor unit loses contact with the air handler or thermostat over the ComfortLink II data bus (the 4-conductor communication cable). Check for loose wire connections at the thermostat, air handler, and outdoor unit control board. A damaged or incorrectly wired communication cable also triggers this code.

## Step-by-Step Fix {#step-by-step-fix}

**Safety first:** Turn off the thermostat, flip the outdoor disconnect switch, and turn off the circuit breaker at the panel. Capacitors hold lethal charge — discharge before touching with a 20kΩ resistor.

1. **Record the fault code.** Open the outdoor electrical compartment and write down the LED flash pattern before cutting power. The code clears when power is removed.

2. **For 3-1 (low pressure) — check airflow first.** Replace the indoor filter. Confirm all supply and return registers are open. If this clears the fault, low airflow was restricting refrigerant evaporation. If it comes back, you have a refrigerant issue — call a tech.

3. **For 3-2 (high pressure) — clean the coil.** With power off, use a garden hose (gentle pressure, NO pressure washer) to rinse the outdoor coil from the inside out through the top of the cabinet. Clear debris from around the base of the unit. Inspect the outdoor fan — it should spin freely by hand.

4. **Test the run capacitor (for 4-1 fault).** Discharge the capacitor (short its terminals through a 20kΩ resistor or 60W bulb). Use a capacitor tester or multimeter in capacitance mode. The HERM terminal should read within 10% of the compressor µF rating; the FAN terminal within 10% of the fan rating. Replacement is a common DIY fix.

5. **Test the contactor.** With power off, inspect the contact points — they should be smooth and silver. Blackened or pitted contacts indicate a failed contactor. Replacement is $20–$45 and is a recommended preventive replacement every 5–8 years.

6. **Check communication wiring (for 7-1 fault).** Trace the 4-wire communication cable from the outdoor unit to the air handler terminal board. Confirm the colors match the terminal labels (typically R, C, Y1, and the ComfortLink data wires). Reseat all connectors. Swap the data wire terminals and restore them in sequence to identify intermittent connections.

7. **Test the defrost thermostat (for 5-2 fault).** Disconnect the defrost thermostat (clipped to the outdoor coil header tube). At room temperature it should read OL (open). Place it in a cup of ice water — below 30°F it should show continuity. If it doesn't close in cold water, it's failed. Replacement part is under $20.

8. **For persistent faults after checks above:** If the fault returns within 1–2 heat/cool cycles, the issue is refrigerant charge, a failing compressor, or a control board fault. These require licensed HVAC service.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Typical Cost | Where to Buy |
|------|-------------|---------------|
| Dual run capacitor — 45/5 µF 440VAC (match label) | $15–$35 | [Amazon](https://www.amazon.com/s?k=45+5+uf+440v+dual+run+capacitor&tag=errorcodefixes-20) |
| Contactor — 2-pole, 40A, 24V coil | $20–$45 | [Amazon](https://www.amazon.com/s?k=40+amp+2+pole+contactor+24v+coil+hvac&tag=errorcodefixes-20) |
| Defrost control board (Trane #CNT04062 or CNT05028) | $55–$140 | [Amazon](https://www.amazon.com/s?k=Trane+defrost+control+board+CNT05028&tag=errorcodefixes-20) |
| Defrost thermostat — outdoor coil clip-on | $12–$28 | [Amazon](https://www.amazon.com/s?k=defrost+thermostat+heat+pump+coil+clip&tag=errorcodefixes-20) |
| Reversing valve solenoid coil — 24VAC | $30–$65 | [Amazon](https://www.amazon.com/s?k=reversing+valve+solenoid+coil+24VAC&tag=errorcodefixes-20) |
| Outdoor fan motor — 1/5 or 1/4 HP, 208–230V (match specs) | $90–$210 | [Amazon](https://www.amazon.com/s?k=outdoor+condenser+fan+motor+230v+heat+pump&tag=errorcodefixes-20) |
| XL16i outdoor control board (Trane OEM — match model) | $90–$200 | [Amazon](https://www.amazon.com/s?k=Trane+XL16i+outdoor+control+board&tag=errorcodefixes-20) |

## When to Call a Professional

**DIY-friendly repairs:** Run capacitor, contactor, defrost thermostat, communication wire re-termination — these are accessible with basic electrical knowledge and do not require refrigerant handling.

**Call a licensed HVAC tech for:**
- Low pressure fault (3-1) that returns after filter change — refrigerant leak or charge issue requires EPA 608 certification to diagnose and repair.
- High discharge temperature (6-2) with no obvious cause — points to low refrigerant charge or a failing compressor.
- Compressor overload (4-2) that trips repeatedly — the compressor may have a failing winding. An ohm test of the winding should show balanced resistance across all three phases within 5%.
- Reversing valve stuck — requires brazing to replace (refrigerant recovery first).

Tell the tech: *"Trane XL16i, ComfortLink II system, fault code [X], here's what I've tested..."* — having the code and your diagnosis narrows the service call significantly.

## See Also

- [Trane XR15 Heat Pump Error Codes — Complete Guide](/posts/trane-xr15-error-codes/)
- [Trane XR14 Error Codes — Diagnostic Guide](/posts/trane-xr14-error-codes/)
- [Trane XR13 Error Codes — Diagnostic Guide](/posts/trane-xr13-error-codes/)
- [Trane ComfortLink II Error Codes — Communicating System Faults](/posts/trane-comfortlink-ii-error-codes/)
- [Trane XV20i Variable-Speed Heat Pump Error Codes](/posts/trane-xv20i-heat-pump-error-codes/)
- [Heat Pump Error Code Guide — All Brands](/posts/heat-pump-error-code-guide/)
