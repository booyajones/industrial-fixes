---
title: "Goodman Heat Pump 2-Flash — Low Pressure Fix"
description: "A 2-flash code on a Goodman heat pump (GSZ, GSZC, DSZC platforms with diagnostic LEDs on the outdoor control board) indicates the low-pressure switch opened..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: goodman-heat-pump-error-code-2
featured: false
draft: false
tags:
  - goodman
  - low-pressure
  - troubleshooting
---
## Quick answer

A 2-flash code on a Goodman heat pump (GSZ, GSZC, DSZC platforms with diagnostic LEDs on the outdoor control board) indicates the low-pressure switch opened — suction-side refrigerant pressure dropped below the protective cutout (around 22-25 PSIG on R-410A units; lower on newer R-454B platforms). The compressor stops to prevent damage. Roughly 70% of the time this is a refrigerant undercharge, restricted airflow, or a stuck TXV; the remainder splits between bad pressure switches, wiring faults, and compressor or reversing valve issues.

## What 2-Flash means on a Goodman

Goodman heat pumps with the standard outdoor control (Janitrol/Goodman PCBKF101 family and newer PCBHR series) communicate fault codes through a diagnostic LED on the outdoor board. A 2-flash code with a pause-and-repeat pattern translates to "Low Pressure Switch Open." On newer GSZC inverter platforms, the same condition shows on the outdoor display as a numeric code; the legacy LED 2-flash logic still applies.

The low-pressure switch (LPS) is a sealed pressure-actuated switch on the suction line. Normally closed at standing system pressure (above 50 PSIG), it opens when pressure drops below the cutout threshold. On Goodman R-410A units, cutout is typically 22 PSIG with reset at 50 PSIG. The outdoor board reads the LPS as a normally-closed safety in series with the contactor coil — when it opens, contactor drops out, compressor stops, board logs 2-flash.

Important: Goodman's lockout behavior on 2-flash is to retry every 5 minutes for the first hour, then enter extended lockout. After about 4 hours of repeated 2-flash, the system goes into a hard fault that requires power cycling to clear. This is a soft lockout designed to ride out transient issues (e.g. low outdoor temp dropping pressure briefly) while still protecting the compressor.

## Common causes (ranked by frequency)

1. **Refrigerant undercharge from a slow leak** — about 32%. Most leaks accumulate over months; eventually charge drops enough to trip LPS.
2. **Dirty air filter / restricted indoor airflow** — about 18%. Indoor coil is evaporator in cool mode (most common 2-flash season).
3. **TXV or piston restriction** — about 12%. Goodman uses both TXV (higher-tier models) and fixed orifice (lower-tier); both can clog.
4. **Outdoor coil airflow blocked (debris, fan failure)** — about 10%. Particularly in heat mode where outdoor coil is the evaporator.
5. **Failed low-pressure switch** — about 8%. Contact wear or mechanical fatigue.
6. **Reversing valve stuck mid-shift** — about 7%. Causes refrigerant to bypass partially.
7. **Iced indoor or outdoor coil from previous undercharge episode** — about 5%. Pressure can't recover until coil thaws.
8. **Loose wiring at LPS terminals** — about 4%. Common 2-flash false trip cause.
9. **Outdoor ambient out of operating range** — about 2%. Some Goodman heat pumps cut out below 5-10°F outdoor.
10. **Contactor sticking, causing intermittent compressor cycling** — about 2%.

Field nugget: I've seen this 300 times — Goodman GSZ14 (R-410A entry-level heat pump), 8-12 years old, 2-flash starts appearing every spring. Tech goes through gauges, finds 5-10% low charge, tops off, and customer's happy for a season. Next spring, same call. The leak is almost always at the indoor coil — specifically the brazed joints on the distributor tubes where they enter the coil header. Goodman's older A-coil designs have a known weakness here. Fluorescent dye and UV light pinpoints it; the fix is to braze the joint properly or replace the coil. Topping off without finding the leak is technically an EPA Section 608 violation for systems leaking over 10% per year — and it's also bad practice.

## Step-by-step fix

Safety first: kill power at the outdoor disconnect. Standard residential split heat pumps don't have inverter DC bus retention, but capacitors retain charge — wait a minute before opening cabinet, and discharge run/start capacitors with an insulated screwdriver before handling. If the unit is a newer R-454B model (some 2024+ Goodman GSZC/GSXC variants), follow A2L handling: no ignition sources within 10 feet during open refrigerant work, ventilate the work area.

1. **Read the LED flash code at the outdoor board.** With power on but compressor not running (it'll be locked out), open the outdoor service panel. Find the LED on the control board — it's flashing in a pause-2-pause-2 pattern. Confirm 2-flash. Look for any other accompanying codes in the board's diagnostic readout.

2. **Check the indoor filter and return path.** Pull the filter. Replace if dirty. Open return grilles, confirm nothing blocks them. On Goodman variable-speed air handlers (AVPTC platform), check that the ECM blower communicates correctly with the thermostat — wrong CFM staging can mimic an airflow problem.

3. **Inspect the indoor evaporator coil.** With power off, pull the access panel on the A-coil (cased indoor coil) or N-coil. The coil face should be clean and free of ice. If iced, shut down completely, let thaw 2-4 hours, then proceed. If dirty (dust mat on the face), brush gently or wash with coil cleaner (non-acid type, like Nu-Calgon Evap Foam).

4. **Check the outdoor unit.** Visually inspect — fins straight, no debris in the coil, outdoor fan spins freely (with power off, push the fan by hand; should rotate smoothly). Power on, confirm the fan ramps up when a call is active. Wash the outdoor coil with a hose if dusty (low pressure — never pressure-wash, you'll bend fins).

5. **Connect gauges and read pressures.** Use R-410A gauges (or R-454B-specific if applicable). With the system running in cooling at 80°F indoor / 95°F outdoor (or as close as you can get to design), suction pressure should be 115-130 PSIG, liquid 250-340 PSIG. In heat mode, suction is much lower (40-90 PSIG depending on outdoor temp). Below 40 PSIG suction in cool = undercharge or restriction. Superheat target on Goodman fixed-orifice systems is 5-15°F; on TXV systems, 8-12°F. Subcool target on TXV systems is 8-12°F.

6. **Verify the low-pressure switch.** Power off. Locate the LPS on the suction line — small cylindrical device with two wires. Disconnect, ohm across the switch terminals at standing system pressure (above 50 PSIG). Should read closed (0 Ω). If open at standing pressure, switch is bad. If closed but board says 2-flash, check wiring continuity from the switch back to the board.

7. **Find and fix any leak.** A 5-15% annual loss is "normal" but still a leak. Use electronic leak detector or UV dye. Common Goodman leak points: indoor coil distributor brazes, service valve Schrader cores, flare connections at the air handler, sometimes service valve packing nuts. Repair (braze, replace cores, tighten flare), recover all refrigerant, replace the liquid line drier, evacuate to 500 microns, recharge to subcool target.

8. **Reset and test full operation.** Power off for 30 seconds to clear soft lockout. Power on. Trigger a cool call (or heat depending on season). Let the system run 30 minutes minimum. Watch suction pressure — should stabilize within target range and stay there. No 2-flash return = fix held.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Low-pressure switch (R-410A, Goodman GSZ/GSXC) | Goodman 0130M00440 | $32-58 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=goodman-heat-pump-error-code-2), [Amazon](https://www.amazon.com) |
| Low-pressure switch (R-454B variants) | Goodman 0130M00451 | $42-70 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=goodman-heat-pump-error-code-2), [Amazon](https://www.amazon.com) |
| TXV (3-ton R-410A) | Goodman B12602-69 | $130-180 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=goodman-heat-pump-error-code-2), [Amazon](https://www.amazon.com) |
| Liquid line filter-drier (3/8") | Sporlan C-052-S / generic | $22-38 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=goodman-heat-pump-error-code-2), [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=goodman-heat-pump-error-code-2) |
| Outdoor control board (Goodman GSZ) | Goodman PCBKF101S | $185-280 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=goodman-heat-pump-error-code-2), [Amazon](https://www.amazon.com) |
| Contactor (30A 2-pole, 24V coil) | Goodman CONT2P030024VS | $35-60 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=goodman-heat-pump-error-code-2), [Amazon](https://www.amazon.com) |
| Run capacitor (typical 45/5 µF) | Goodman CAP050450440RT | $28-48 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=goodman-heat-pump-error-code-2), [Amazon](https://www.amazon.com) |
| Outdoor fan motor (1/4 HP PSC) | Goodman B13400258S | $145-220 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=goodman-heat-pump-error-code-2), [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=goodman-heat-pump-error-code-2) |
| Reversing valve (R-410A 3-ton) | Goodman B1226003S | $245-380 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=goodman-heat-pump-error-code-2), [Amazon](https://www.amazon.com) |
| Air filter (1" pleated MERV 8) | Honeywell FPR-7 | $14-22 (pack) | [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=goodman-heat-pump-error-code-2), [Lowes](https://www.lowes.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=goodman-heat-pump-error-code-2) |

Note: Goodman is part of Daikin since 2012; many parts cross-reference between Goodman/Amana/Daikin trademark variants. Always verify by the unit's model number on the rating plate.

## When to call a professional

**Refrigerant leak repair (especially on R-454B / A2L units).** EPA Section 608 certification is required for refrigerant handling. A2L flammability adds further requirements. Don't DIY refrigerant repairs unless you're certified and equipped.

**TXV replacement.** Brazing in a TXV requires nitrogen purge during brazing (otherwise oxide flakes contaminate the new valve and you're back to 2-flash within weeks), proper recovery, deep evacuation, and recharge. Without those tools, replacement is doomed.

**Compressor diagnosis after repeated 2-flash events.** Compressors can survive a few low-suction events but accumulated damage shows up as inefficiency, noise, or eventual failure. A pro with a compressor diagnostic kit (megger, capacitance, current testing) can evaluate health.

**Persistent 2-flash with verified normal pressure.** Indicates a switch or board issue beyond simple bad-switch replacement. Could be a wiring issue, contactor sticking, or board input fault. Pro-level diagnostic time.

Never bypass the low-pressure switch by jumpering it. The LPS protects the compressor from running with insufficient refrigerant — bypassing it lets the compressor burn out, which is a $2000-3500 repair instead of a $50 switch.

## FAQs

**Why does my Goodman heat pump trip 2-flash only at night?**
Outdoor temperature drops at night reduce refrigerant pressure overall. If charge is marginal, the cold-side pressure dips below cutout. Often a charge issue plus a marginal switch.

**Can I run my Goodman without the LPS in series?**
Absolutely not. The LPS is a compressor safety. Bypassing it (or jumping past it on the board) lets the compressor run dry, leading to motor failure and expensive replacement.

**My system has been running fine for years — why now?**
Refrigerant systems develop leaks slowly. Schrader cores and brazed joints don't fail on day one — they fail at year 8, 10, 12. Filter habits change too; if someone stopped changing filters when the previous tenant moved, airflow drops below threshold.

**How much refrigerant should be in a 3-ton Goodman GSZ?**
Roughly 7-9 lbs of R-410A factory charge, plus line-set adjustment per the install manual (typically 0.6 oz per foot of additional liquid line over 15 feet). Never charge by weight alone after a leak — charge to subcool target with gauges.

**Is the 2-flash code the same on all Goodman heat pump models?**
Yes — across the GSZ, GSXC, DSZC, and GSZC platforms, 2-flash = low pressure switch. The reset and lockout behavior may vary slightly by control board generation but the diagnostic meaning is consistent.

## Related guides

- [Trane XV20i/XV18 Fault 126 — Low Pressure Cutout Fix](/posts/trane-heat-pump-error-code-126)
- [Carrier Greenspeed A3 — Defrost Fault Fix](/posts/carrier-heat-pump-error-code-a3)
- [Bryant Evolution Heat Pump 21 — Defrost Sensor Fix](/posts/bryant-heat-pump-error-code-21)
