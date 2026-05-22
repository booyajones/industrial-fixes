---
title: "Pitco Fryer Error Code E6 — High Temp Limit Fix"
description: "Pitco commercial fryer error E6 means the high-limit safety switch has opened — oil temperature exceeded the safety threshold (typically 460-475°F). The..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Marcus Webb"
slug: pitco-fryer-error-code-e6
featured: false
draft: false
tags:
  - pitco
  - high-temperature-limit
  - troubleshooting
---
## Quick answer

Pitco commercial fryer error E6 means the high-limit safety switch has opened — oil temperature exceeded the safety threshold (typically 460-475°F). The fryer immediately shuts off heat and posts E6 until manually reset. About 55% of E6 events in busy restaurants are caused by oil level too low (oil overheats locally above the heating element), not by an actual control thermostat failure. Always check oil level first.

## What E6 means on a Pitco fryer

Pitco gas and electric commercial fryers (SG14, SG18, SE14, SE18, Frialator and Solstice series, plus the high-end Solstice Supreme with the I12 control) use a dual-thermostat safety architecture: an operating thermostat (or electronic temperature controller on newer units) that controls normal frying temperature (325-375°F typically), and a separate high-limit safety thermostat (typically a manual-reset bimetallic switch) set to 460-475°F.

When oil temperature exceeds 460-475°F, the high-limit switch opens, breaking the gas valve safety circuit (on gas units) or the heating element contactor (on electric units), and the control board posts E6. The display shows "E6" or "HI-LIMIT" depending on model. The fryer cannot restart until: (1) oil cools back below the limit setpoint, AND (2) the manual reset button on the high-limit switch is pressed.

On Pitco Solstice and Supreme models with the I12 (and newer I12+ digital controllers), E6 is part of a broader fault code system (E1-E9) — E1 through E5 are related faults (sensor open, sensor shorted, ignition failure, communication, etc.), and E6 specifically is high-limit. The I12 controller stores fault history accessible by entering programming mode.

The reason high-limit trips are so dangerous on a fryer: an over-temperature oil event can ignite (peanut oil flashpoint is around 540°F, but oil can autoignite above 700°F if exposed to flame or hot surface). The high-limit switch's job is to cut heat well before oil reaches anywhere near flashpoint.

## Common causes (ranked by frequency)

In commercial fryer service:

1. **Oil level too low** — about 35%. Without enough oil to absorb burner heat, local hotspots above the burner tubes exceed the limit.
2. **Failed operating thermostat (stuck on)** — about 20%. The controller doesn't cycle the heat off at setpoint, so oil keeps heating until the limit catches it.
3. **Carbon buildup on burner tubes (gas) or element (electric)** — about 12%. Localized hotspot.
4. **High-limit switch drifted low (now opens at 420°F instead of 470°F)** — about 10%. Switch is aging.
5. **Temperature sensor (RTD or thermocouple) failure reading low** — about 8%. Controller thinks oil is cooler than actual.
6. **Gas valve stuck open / partial sticking** — about 6%.
7. **Failed controller relay (stuck on)** — about 5%.
8. **Wiring issue (high-limit lead shorted to a heated surface)** — about 2%.
9. **Oil contamination (water in oil causes rapid heating events)** — about 2%.

**Pro nugget:** Pitco fryer oil capacity is exact — printed on the lip of the well, typically 40-50 lbs of oil for SG14-class fryers. Restaurants commonly run "low" for a few hours before topping off, especially during high-volume periods. The fryer is designed to operate at the **fill line**, not below. Below the fill line, oil thermal mass drops, burner tubes are partially exposed in gas units, and the operating thermostat (which senses from a fixed depth in the well) reads oil that's mostly hot while burners are still firing — the result is overshoot past the limit. Train staff to top off oil to the fill line every shift. This is the single most preventable cause of E6.

## Step-by-step fix

Before you start: shut off gas at the appliance gas cock (gas units) or kill the breaker (electric units). Allow the unit to cool fully — fryer oil at operating temperature is 350°F and a splash burn from hot oil is severe.

1. **Confirm the code.** Display reads E6, HI-LIMIT, or LOCK. On Pitco I12 controllers, the code may alternate with "RESET" to remind staff to push the reset button.

2. **Check oil level.** Look at the fill line on the well. Oil should be at or just above the line. If below, top off with fresh oil to the line — most likely root cause and easy fix.

3. **Press the high-limit reset.** Allow oil to cool below 400°F. Locate the high-limit switch — typically a small button on the side or back of the fryer with a red cap. Press firmly until you feel/hear a click. Reset is mechanical and only works when oil is below setpoint.

4. **Inspect burner tubes (gas) or heating element (electric).** Pull the front cover (typically 2-4 screws). On gas units, look at the burner tubes inside the well — should be clean, uniform. Carbon buildup on the tubes acts as insulation and creates hotspots. On electric units, look at the element — should be free of carbon scale.

5. **Test the operating thermostat / controller.** Restore power, set oil temp to 350°F, and watch with a calibrated probe (an infrared gun aimed at the oil surface or a deep-fry thermometer inserted into the oil). Oil should cycle around setpoint with ±10°F overshoot. If oil climbs past 400°F without the controller cycling heat off, the thermostat or controller has failed.

6. **Test the high-limit switch.** Pull the switch from its mounting (typically a snap-disc on the well or a probe inserted into a port). Ohm-test at room temp — should be closed (continuity). Bench-test by heating with a heat gun — should open at the stamped setpoint (typically 460-475°F). Replace if it opens at a lower temp.

7. **Test the temperature sensor.** Ohm-test the RTD or thermocouple. Pitco typically uses a Pt100 RTD (100 ohms at 0°C; about 250 ohms at 350°F). Verify the reading. Replace if reading is wildly off.

8. **Inspect for gas valve sticking (gas units).** If the controller is commanding heat off but burners stay lit, the gas valve is stuck open — gas leak hazard, immediate replacement.

9. **Replace components as needed and restore.** Replace failed parts, reassemble, restore gas/power, top off oil to fill line. Run a heat cycle to 350°F and verify normal cycling without E6.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| High-limit switch (manual reset, 460°F) | Pitco PP10078 | $85-145 | [PartsTown](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=pitco-fryer-error-code-e6), [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=pitco-fryer-error-code-e6) |
| Operating thermostat (mechanical) | Pitco PP10079 | $115-185 | [PartsTown](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=pitco-fryer-error-code-e6), [Amazon](https://www.amazon.com) |
| I12 digital controller | Pitco P5047541 | $385-585 | [PartsTown](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=pitco-fryer-error-code-e6), [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=pitco-fryer-error-code-e6) |
| Temperature sensor RTD (Pt100) | Pitco PP10078E | $85-145 | [PartsTown](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=pitco-fryer-error-code-e6), [Amazon](https://www.amazon.com) |
| Gas valve (natural gas, Solstice) | Pitco PP10612 | $385-585 | [PartsTown](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=pitco-fryer-error-code-e6), [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=pitco-fryer-error-code-e6) |
| Heating element (electric, 14 kW) | Pitco PP10080 | $445-585 | [PartsTown](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=pitco-fryer-error-code-e6), [Amazon](https://www.amazon.com) |
| Burner tube assembly (gas) | Pitco PP10081 | $245-385 | [PartsTown](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=pitco-fryer-error-code-e6) |
| High-limit reset button cap | Pitco PP10082 | $15-25 | [PartsTown](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=pitco-fryer-error-code-e6), [Amazon](https://www.amazon.com) |
| Deep-fry thermometer (calibration) | Taylor 3506FS | $35-65 | [Amazon](https://www.amazon.com), [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=pitco-fryer-error-code-e6) |
| Digital manometer | Dwyer 475-1-FM | $185-235 | [Amazon](https://www.amazon.com) |

PartsTown is primary distributor for Pitco. Confirm part numbers by serial — Pitco changes part numbers across Solstice generations.

## When to call a professional

Call a licensed commercial gas-fitter or appliance tech when:

- The gas valve needs replacement. Pitco gas valves require leak-testing after install.
- E6 returns repeatedly after a high-limit replacement. Suggests the operating thermostat or controller is failing to regulate.
- You smell unburned gas. Immediate shutdown and evacuation; this is a fire risk.
- The fryer is under Pitco warranty (typically 1 year parts and labor; some Solstice Supreme models have extended 2-year warranties on the I12 controller).
- AHJ inspection required after any safety-system component replacement (most jurisdictions).

## FAQs

**Why does E6 happen during lunch rush?**
Lunch rush = high cooking volume = staff don't keep up with oil top-off. Oil drops below the fill line, thermal mass drops, hotspots form, E6 trips.

**Can I press reset and keep frying?**
Reset only — without identifying the cause — means E6 will return, possibly with a more serious oil temperature event next time. Always check oil level and bench-test the high-limit if E6 trips more than once.

**My fryer oil is rancid and dark. Is that a problem?**
Yes. Polymerized oil has lower heat capacity and forms gum on the burner tubes / element. Switch out oil per manufacturer schedule (typically every 3-7 days depending on use).

**Will running the fryer without oil damage it?**
Catastrophic damage within minutes. Burner tubes warp, element fails, well stress-cracks. The high-limit catches this normally — but if the limit has drifted or failed, the unit destroys itself quickly.

**Difference between Pitco E6 and E5?**
E5 = ignition failure (no flame proved on gas units). E6 = high-limit trip. Different paths.

## Related guides

- [Vulcan Convection Oven F-Code Error — Gas Oven Fix](/posts/vulcan-convection-oven-error-code)
- [Garland Char-Broiler Error Code — Safety Lockout Fix](/posts/garland-charbroiler-error-code)
- [Master-Bilt Walk-In Error Code — Controller Fault Fix](/posts/master-bilt-error-code)
