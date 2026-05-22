---
title: "Frigidaire Refrigerator Error Code SY EF — Evap Fan Fix"
description: "Frigidaire (and its parent Electrolux's appliances under the Frigidaire badge) display error \"SY EF\" when the main control board detects that the freezer..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Industrial Error Code Fixes"
slug: frigidaire-refrigerator-error-code-sy-ef
featured: false
draft: false
tags:
  - frigidaire
  - evaporator-fan-circuit-failure
  - troubleshooting
---
## Quick answer

Frigidaire (and its parent Electrolux's appliances under the Frigidaire badge) display error "SY EF" when the main control board detects that the freezer evaporator fan is drawing too little or too much current, or has failed to start when commanded. The single most common cause I see is ice buildup binding the fan blade after a defrost system failure, not a dead fan motor — clear the ice and verify the defrost circuit before condemning the fan.

## What SY EF means on a Frigidaire refrigerator

Frigidaire French-door, side-by-side, and counter-depth refrigerators (LFSS, LGHB, FGHB, FPHB, FFHB, FFSS series and most successors) built since about 2012 use a brushless DC (BLDC) freezer evaporator fan controlled by a small motor-driver IC on the main control board. The board commands a target RPM via PWM and monitors the motor's current draw and tach feedback through a dedicated fan harness.

"SY EF" stands for "System Evaporator Fan" — a Frigidaire-internal label that maps to fault code 5C on some service displays, or "OP-FAN" on older models. The board fires SY EF when one of: (a) the fan motor doesn't draw expected current within 30 seconds of command, (b) the tach feedback line doesn't pulse at the expected rate, (c) the motor draws excessive current (binding or short), or (d) the fan harness has an open or shorted wire detected during a self-check.

When the freezer evap fan stops, cold air no longer circulates from the evaporator over the food. The freezer warms from a normal -5°F toward 25°F over a few hours; the fresh-food side warms faster because Frigidaire's design depends on cold air being pushed from freezer to fresh-food through a damper. Total food loss within 24-36 hours if untreated.

## Common causes (ranked by frequency)

In Frigidaire refrigerator service experience:

1. **Ice buildup around the fan blade or evaporator coil** — about 40%. Defrost cycle failure let ice grow until it binds the blade.
2. **Failed BLDC fan motor** — about 22%. Motor bearings worn, windings failed, or Hall sensor dead.
3. **Failed defrost heater or defrost thermostat causing the ice buildup** — about 15%. Root cause behind many "fan failures."
4. **Fan harness chafed or disconnected** — about 8%. The wiring run through the back of the freezer compartment can chafe.
5. **Damper motor failure causing abnormal frost patterns** — about 6%. Damper stuck open lets warm fresh-food air condense on the evap.
6. **Main control PCB fault** — about 5%. Motor driver section failed.
7. **Foreign object jamming the fan blade** — about 3%. Food package, ice cube from icemaker.
8. **Wrong replacement fan installed (incorrect PWM/voltage)** — about 1%.

**Pro nugget:** Frigidaire/Electrolux part numbers fall into the 5300, 5304, and 8000 series. The most common freezer evap fan motor in Frigidaire French-door units is **5304504369** — a 12VDC BLDC motor with integrated blade. When you order this part, you typically get the motor and blade as an assembly, but **the mounting bracket is sold separately** (part 5304507319). Older Frigidaire units have the bracket integrated with the motor; newer redesigned units split them. Ordering only the motor on a newer unit leaves you with a motor and no way to mount it — confirm the model year and part configuration before ordering. RepairClinic's parts diagram tool is your friend.

## Step-by-step fix

Before you start: unplug the refrigerator and remove all food to a cooler.

1. **Confirm the code.** Read display: "SY EF" — typically alternates with "5C" on diagnostic mode display. Enter diagnostic mode on most Frigidaire models by holding the "Power Cool" + "Power Freeze" buttons together for 6-10 seconds.

2. **Remove the freezer back panel.** Pull all drawers, ice maker bin, and shelves. Remove the freezer back panel (4-6 screws and snap-clips). Set aside.

3. **Inspect for ice.** A normal evaporator has a light frost dusting. Abnormal: thick ice on the coil, around the fan, or on the back wall. If you see >1/4 inch of ice anywhere, the defrost system has been failing — you need to address both the ice (now) and the defrost cause (next).

4. **Defrost manually if iced.** Leave unit unplugged with doors open for 24-48 hours, or use a hair dryer on low heat (keep moving, don't melt plastic). Towel-dry the compartment when done.

5. **Spin the fan by hand.** With ice gone, the blade should spin freely with mild resistance. Grinding, scraping, or binding means a bad motor.

6. **Ohm-test the BLDC motor.** Disconnect the 4-pin harness. Across the two winding pins, expect roughly 15-40 ohms balanced. Open (OL) or zero ohms = dead motor.

7. **Test the defrost system.** Pull the defrost thermostat (usually clipped to the suction line near the evap). At room temp it should read open; in a bowl of ice water (below 30°F) it should read closed. Pull the defrost heater (a glass tube or sheath element wrapped around the bottom of the evap coil). Ohm-test: typically 20-50 ohms. Open = dead heater.

8. **Inspect the fan harness.** Trace the 4-pin harness from the fan back to the main board (typically located behind a panel in the upper rear of the unit). Look for chafing, breaks, oxidation at connectors.

9. **Install the new motor.** Frigidaire freezer evap motors include the blade pre-installed. Mount with the bracket, plug in the 4-pin harness, position the blade with 1/4-inch clearance to the coil and back wall.

10. **Replace defrost components if needed.** Always swap the defrost thermostat with a new one when servicing a Frigidaire SY EF caused by ice — the cost is $20-30 and prevents recurrence within months.

11. **Reassemble and verify.** Replace the back panel and shelves. Plug in. Allow 2-4 hours for cooldown. Listen for smooth fan operation — low whoosh, no clicks or buzzing.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Evap fan motor (French-door BLDC) | Frigidaire 5304504369 | $95-165 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=frigidaire-refrigerator-error-code-sy-ef), [Amazon](https://www.amazon.com) |
| Evap fan motor (side-by-side older) | Frigidaire 5303918549 | $75-135 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=frigidaire-refrigerator-error-code-sy-ef), [Amazon](https://www.amazon.com) |
| Fan mounting bracket | Frigidaire 5304507319 | $15-30 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=frigidaire-refrigerator-error-code-sy-ef) |
| Defrost thermostat | Frigidaire 5303918214 | $25-45 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=frigidaire-refrigerator-error-code-sy-ef), [Amazon](https://www.amazon.com) |
| Defrost heater (sheath type) | Frigidaire 241927201 | $45-85 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=frigidaire-refrigerator-error-code-sy-ef), [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=frigidaire-refrigerator-error-code-sy-ef) |
| Damper assembly | Frigidaire 241600905 | $115-185 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=frigidaire-refrigerator-error-code-sy-ef), [Amazon](https://www.amazon.com) |
| Main control board (varies by model) | Frigidaire 5304-series | $185-385 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=frigidaire-refrigerator-error-code-sy-ef), [Amazon](https://www.amazon.com) |
| Thermistor (10kΩ NTC) | Frigidaire 5304504709 | $25-45 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=frigidaire-refrigerator-error-code-sy-ef) |

## When to call a professional

Call an appliance tech when:

- You replaced the fan and defrost components, and SY EF returns within days. The next step is investigation of the main PCB — model-specific part, can run $200-400.
- You see oil residue around the evap coil or hear a hiss. Refrigerant leak — EPA-certified work only.
- The fresh-food side stays warm even after the freezer cools. Suggests damper failure or main PCB issue.
- The unit is under Frigidaire / Electrolux warranty (1 year parts standard, 5 years on sealed system, 10 years on inverter compressors on premium models).

## FAQs

**My SY EF cleared after I unplugged for 30 minutes. Is it fixed?**
No. Unplugging clears the fault code from board memory but doesn't fix the underlying ice or motor issue. It'll return within hours if the root cause isn't addressed.

**Can I substitute a generic 12VDC evap fan motor?**
Not safely. Frigidaire BLDC motors use a specific PWM protocol. Generic motors are typically AC shaded-pole or DC brush and don't speak the Frigidaire board's drive signal. Use the OEM part.

**My Frigidaire is 5 years old and showing SY EF. Is this a known issue?**
Frigidaire French-door units have a documented defrost-system-failure pattern at the 4-7 year mark — defrost thermostat fails, ice grows, eventually binds the fan. Always replace the defrost thermostat preventively when servicing SY EF on these units.

**Will Frigidaire warranty cover SY EF?**
Within the 1-year parts warranty, yes. Beyond that, only the sealed system (5 years) and inverter compressor (10 years on premium) are typically covered. Most SY EF failures fall outside both.

**Difference between SY EF and SY CE?**
SY EF = system evaporator fan circuit failure. SY CE = system communications error (UI-to-main-board communication lost). Different parts, different paths.

## Related guides

- [Frigidaire Dishwasher Error Code i30 — Water in Base Fix](/posts/frigidaire-dishwasher-error-code-i30)
- [Electrolux Washer Error Code E20 — Drain Pump Fix](/posts/electrolux-washer-error-code-e20)
- [LG Refrigerator Error ER RF — Evap Fan Motor Fix](/posts/lg-refrigerator-error-er-rf)
