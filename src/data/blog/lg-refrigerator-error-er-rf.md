---
title: "LG Refrigerator Error ER RF — Evap Fan Motor Fix"
description: "LG error code \"ER rF\" (sometimes shown as \"Er rF\" or simply \"rF\" on older models) means the freezer evaporator fan motor isn't sending its expected RPM..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Industrial Error Code Fixes"
slug: lg-refrigerator-error-er-rf
featured: false
draft: false
tags:
  - lg
  - evaporator-fan-motor-failure
  - troubleshooting
---
## Quick answer

LG error code "ER rF" (sometimes shown as "Er rF" or simply "rF" on older models) means the freezer evaporator fan motor isn't sending its expected RPM feedback signal back to the main control board — the fan is either stopped, locked by ice buildup, or the BLDC motor's Hall sensor has failed. Roughly 45% of the time it's frost buildup binding the fan blade, not a dead motor. Inspect for ice before ordering the motor.

## What ER rF means on an LG refrigerator

LG French-door and side-by-side refrigerators built since about 2010 (LFX/LMX series, LFXS/LMXS, LRMVS, LRFVS, LSXC, and many others) use a brushless DC (BLDC) evaporator fan motor in place of the older shaded-pole AC motors found on legacy units. The BLDC motor includes integrated Hall-effect sensors that report rotor position and speed back to the main PCB via a small 4-pin connector (12V, ground, PWM speed command, RPM feedback). The board commands a target RPM (typically 1800-2400 RPM depending on cooling demand), and the motor reports back its actual RPM via a digital pulse train on the feedback line.

ER rF (refrigeration fan error) fires when the board sends a PWM command but receives no RPM feedback within a watch window — typically 30-60 seconds. The board doesn't distinguish between "motor isn't getting 12V" and "motor is locked" and "Hall sensor failed" — all three conditions present as identical no-feedback errors. Newer LG models with Smart Diagnosis (the 3-second held button + phone microphone diagnostic) can decode this further; older models just show ER rF on the display and shut down the freezer fan.

When the freezer fan stops, the freezer warms slowly because cold air no longer circulates from the evaporator over the food. The fresh-food side warms faster because LG's design relies on freezer-side air being pushed into the fresh-food compartment through a damper. After 4-8 hours of ER rF you'll typically see freezer at 20-30°F (rising) and fresh food at 50-55°F (warming fast). Total food loss within 24 hours if not addressed.

## Common causes (ranked by frequency)

In LG refrigerator service experience:

1. **Ice buildup on the fan blade or in the evaporator compartment** — about 45%. Failed defrost cycle let ice grow around the fan, eventually binding the rotor.
2. **Failed BLDC fan motor (Hall sensor or windings)** — about 25%. Motor itself dead, common after 6-10 years.
3. **Wiring harness fault between motor and PCB** — about 12%. The 4-pin connector at the back of the freezer compartment is exposed to moisture and corrodes.
4. **Failed defrost heater or defrost thermostat** — about 8%. Heater doesn't run; ice accumulates and eventually binds the fan. Looks like a fan problem but is actually a defrost system problem.
5. **Failed main PCB (rare but happens)** — about 6%. The fan motor driver circuit on the board has failed.
6. **Door not closing fully (humid air infiltration)** — about 3%. Excess moisture creates abnormal frost, which then binds the fan.
7. **Wrong replacement motor installed (incorrect RPM range)** — about 1%. Universal motor doesn't match LG's PWM protocol.

**Pro nugget:** LG BLDC evaporator fan motors carry the 6500-series part numbers (6500JB1011A, 6500JB2002K, 6549JB2001A — variants by model year and freezer size). When you replace the motor, **inspect the defrost heater and defrost thermostat at the same time**. The most common LG failure pattern: defrost thermostat fails open → defrost cycle never runs → ice grows in the evaporator compartment over 2-3 months → ice eventually binds the fan blade → ER rF appears. If you replace just the fan motor without addressing the defrost system, the new fan will get stuck in 8-12 weeks. Always pull and bench-test the defrost thermostat (should read closed below 30°F, open above 50°F) and ohm-test the defrost heater (typically 30-50 ohms) when servicing ER rF.

## Step-by-step fix

Before you start: unplug the refrigerator. Remove all food to a cooler. Allow 24-48 hours for thorough defrosting if the evaporator is iced over.

1. **Confirm the code and history.** Read the display for "ER rF" or "rF." On models with Smart Diagnosis, hold the diagnostic button for 3 seconds, run the LG ThinQ app's diagnosis from the LG Smart Diagnosis menu, and confirm the fault code. Older displays just show ER rF.

2. **Remove the freezer back panel.** With the unit unplugged, pull all freezer drawers, ice maker bin, and shelves. Remove the rear panel of the freezer compartment (typically 4-6 screws and a few snap-clips). Set aside the panel and any insulation.

3. **Inspect the evaporator and fan for ice.** A normal LG evaporator coil has a light dusting of frost — uniform across all fins. An abnormal evaporator is packed with ice between the fins, around the fan, and across the back wall. If you see thick ice (>1/4 inch on the fan blade or in the coil), you have a defrost system failure, not just a fan motor failure.

4. **Defrost manually if iced.** Two options: (a) leave the unit unplugged with doors open for 24-48 hours to thaw naturally, with towels in place to catch meltwater, or (b) use a low-heat hair dryer to accelerate (don't melt the plastic — keep the dryer moving and at low heat). Once the ice is fully gone, towel-dry the evaporator compartment.

5. **Spin the fan blade by hand.** With ice cleared, spin the fan blade. It should rotate freely with no scraping, no grinding, no binding. If the fan binds even with no ice present, the bearings are shot — order a new motor.

6. **Ohm-test the BLDC motor.** Disconnect the 4-pin motor connector. With a meter on resistance, check the windings (between pins 1 and 2 on most LG BLDCs — refer to the wiring diagram on the unit). Expect 20-80 ohms across the windings. Open (OL) or shorted (zero ohms) means a dead motor.

7. **Test the defrost system.** With the unit still unplugged, ohm-test the defrost thermostat (also called bimetal thermostat) — should read closed below 30°F, open above 50°F. Pull it out of the freezer to room temp, watch it open. Ohm-test the defrost heater — typically 30-50 ohms for an LG. Either failure means the heater isn't running and ice will return.

8. **Install the new motor.** LG evap fan motors come with the fan blade pre-installed on the shaft. The motor mounts with 2-3 screws and the 4-pin connector. Position the blade so it has clearance from the coil and the back wall (about 1/4-inch all around).

9. **Reassemble and restore power.** Replace the back panel, drawers, and shelves. Plug in. Allow 2-4 hours for the freezer to cool back to setpoint. Listen for the fan running — should be a low whoosh, no clicking, no buzzing. Verify ER rF does not return.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Evap fan motor BLDC (French door, common) | LG 6500JB1011A | $85-145 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Evap fan motor BLDC (LFX larger French door) | LG 6549JB2001A | $115-175 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Evap fan motor (side-by-side, older) | LG 6500JB2002K | $75-125 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Defrost thermostat (bimetal) | LG 6615JB2002L | $25-45 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Defrost heater (sheath type) | LG 5300JJ2001A | $45-85 | [RepairClinic](https://www.repairclinic.com) |
| Main control PCB (varies by model) | LG EBR-series (model-specific) | $185-385 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Fan motor connector / wiring harness | LG model-specific | $15-35 | [RepairClinic](https://www.repairclinic.com) |

The LG 6500JB1011A is the most common French-door evap fan motor and fits LFX25974ST, LMXS27626S, LFXS28968S, LMXS30776S, and dozens of related models from 2013-2020. Confirm fit with your model number before ordering.

## When to call a professional

Call an appliance tech when:

- You replaced the fan motor, the defrost system tests OK, and ER rF returns within days. The next step is investigation of the main PCB's fan driver circuit — board replacement requires careful matching of the EBR part number to the exact model.
- You see refrigerant oil residue on the evaporator coil or hear a hiss. Refrigerant leak — needs an EPA-certified tech.
- The fresh-food side stays warm even after the fan and defrost system are confirmed working. That points to a damper motor or main PCB issue.
- Unit is under LG warranty (sealed system is typically 7-10 years; major components 1 year). Authorized service required.

## FAQs

**The fan ran fine after I cleared the ice. Should I still replace the motor?**
If the fan spun freely by hand after de-icing and the ER rF code cleared, the motor is probably OK. But you absolutely must fix the defrost system — the ice is going to return in 2-3 months and bind the fan again.

**Can I use a universal evap fan motor on my LG?**
Not safely. LG's BLDC motors use a proprietary PWM speed command and feedback protocol. Universal motors are typically AC shaded-pole and won't work with the LG board's drive signal. Order the OEM part.

**My LG is 3 years old and has ER rF. Is this a recall?**
There were LG French-door defrost system class actions in 2017-2019 covering certain LFX, LMX, and LFXS models. Check the LG warranty database with your serial number; if it's covered, LG will service for free.

**Will resetting the refrigerator clear ER rF?**
Temporarily. If you unplug for 30 seconds and plug back in, the code clears — but if the underlying motor or ice problem isn't fixed, ER rF returns within hours. Not a real fix.

**Difference between ER rF and ER FF?**
ER rF = refrigerator fan (freezer evap fan). ER FF = freezer fan (a separate fan on some larger French-door models with two-evaporator systems). Different fans, similar diagnostic paths but different parts.

## Related guides

- [LG Washer Error LE — Motor Lock Fix](/posts/lg-washer-error-le)
- [LG Dishwasher Error IE — Water Inlet Fix](/posts/lg-dishwasher-error-ie)
- [GE Refrigerator Error Code Er — Diagnostic Guide](/posts/ge-refrigerator-error-code-er)
