---
title: "Electrolux Washer Error Code E20 — Drain Pump Fix"
description: "Electrolux washer error E20 (also displayed as \"EF\" on some models) means the control board energized the drain pump but didn't see the wash water drop to..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Industrial Error Code Fixes"
slug: electrolux-washer-error-code-e20
featured: false
draft: false
tags:
  - electrolux
  - drain-failure
  - troubleshooting
---
## Quick answer

Electrolux washer error E20 (also displayed as "EF" on some models) means the control board energized the drain pump but didn't see the wash water drop to the expected level within the timeout window — typically 8-10 minutes. About 50% of E20 codes are caused by a clogged pump filter at the bottom front of the machine, not a failed pump. Pull the filter access panel and clean before assuming a dead pump.

## What E20 means on an Electrolux washer

Electrolux front-load washers (EFLW, EIFLS, EWFLS series, and the Perfect Steam and Wave-Touch models) drain through a 1.25-inch hose from the bottom of the outer tub into a centrifugal drain pump (about 60-90 watts), then through a 1-inch standpipe hose to the home's drain. The pump runs at constant speed when energized and pulls water out at roughly 12-15 GPM under no head.

E20 fires when the pressure transducer reading (the same sensor that detects fill level) doesn't decrease to the "tub empty" threshold within the watch window. The board doesn't distinguish between "pump not running" and "pump running but flow blocked" and "pump running but pressure sensor isn't reading the drop" — all three look identical at the code level.

The drain pump on an Electrolux front-loader includes a removable filter (a coarse mesh basket) accessible behind a small panel at the bottom front of the washer. The filter catches coins, bra wires, screws, and bobby pins that fall into the pump from clothes pockets. Over 1-3 years of household use, the filter accumulates enough debris to significantly restrict flow. Most users don't know the filter exists — it's a documented service interval but rarely performed.

## Common causes (ranked by frequency)

In Electrolux front-load washer service experience:

1. **Clogged pump filter at the front-bottom access panel** — about 35%. The single most common cause.
2. **Clogged drain hose (lint, soap scum buildup)** — about 18%. The internal corrugations of the corrugated hose trap lint.
3. **Failed drain pump motor** — about 14%. Pump bearings fail, impeller wears, or motor windings open.
4. **Clogged standpipe or home drain** — about 10%. The home-side standpipe partially blocked, washer can't push water out.
5. **Coin or hard object jammed in the pump impeller** — about 8%. Foreign object passed the filter or filter was removed.
6. **Pressure transducer or air dome clogged** — about 6%. Sensor not reading the level drop.
7. **Failed main control PCB** — about 5%. Pump driver circuit failed.
8. **Drain hose kinked behind the washer** — about 4%. Storage of cleaning supplies pinched the hose.

**Pro nugget:** Electrolux drain pumps are typically the Askoll M50, M60, or similar Italian-made centrifugal pump. The pump's impeller has a small rare-earth magnet ring around it that interlocks with the motor's magnetic field — when a coin or hard object jams between the impeller and the housing, the magnet can demagnetize from the impact. After demagnetization, the pump may appear to run (you hear the motor) but produces no flow because the impeller no longer locks to the motor field. Symptom: motor hums or runs at full speed but the tub doesn't drain. Test: pull the pump, manually spin the impeller with the motor energized — if you can stop it with your fingers, the magnet is dead and the pump needs replacement, not just cleaning.

## Step-by-step fix

Before you start: shut off both water supplies, unplug the washer.

1. **Confirm the code.** Display reads "E20" or "EF" depending on model. Some Electrolux models also display "20" or include the sub-code "E21" (pump motor not responding) — different but related codes.

2. **Access the pump filter.** At the bottom front of the washer, there's a small access panel (typically 4-6 inches square, snaps off with finger pressure or a flat-blade screwdriver in a corner notch). Behind it: a small drain hose with a cap, and the pump filter access cap (round knob, twist counter-clockwise).

3. **Drain residual water first.** Pull the small drain hose, hold the end in a shallow pan, remove the cap, let water drain. Have a large pan ready — sometimes there's a gallon or more of water trapped in the tub. When flow stops, replace the cap.

4. **Remove and clean the filter.** Twist the larger filter cap counter-clockwise (it usually has finger ribs for grip). Pull the filter out. It'll be wet and possibly contain coins, lint, hair, small clothing. Rinse under tap water, check for cracks or missing pieces. Reinstall.

5. **Check the pump impeller.** With the filter out, look into the pump housing with a flashlight. The impeller is visible at the back of the housing. Reach in carefully with a finger or chopstick and spin the impeller. It should rotate freely. If you feel grit or a hard object, remove it.

6. **Tip the washer back and check the drain hose.** With the washer tipped 30 degrees onto a back-leg (have help — washers are heavy and back-tippy), inspect the drain hose run from pump to standpipe. Check for kinks, perished sections, lint accumulation visible from outside (lump-like blockages).

7. **Test the pump electrically.** Pull the back panel (4-8 screws). Locate the drain pump (about the size of a baseball, dark plastic, with a 2-wire harness from the main PCB). Ohm-test the pump terminals with the harness disconnected — typically 150-300 ohms for an Electrolux pump motor. Open (OL) means dead motor.

8. **Test the pressure transducer.** Find the small 1/4-inch air hose running from the bottom of the outer tub up to the transducer (typically on or near the main PCB). Pull the hose, blow through it gently — should pass air freely. Water in the hose means the air dome at the tub bottom is clogged with detergent residue and needs flushing.

9. **Reassemble and test.** Restore water and power. Run a Rinse & Spin cycle with no clothes. The drain should engage within 30 seconds of cycle start, water should visibly drop, and the cycle should advance to spin within 2-3 minutes. Watch E20 for return.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Drain pump assembly (Askoll M50) | Electrolux 137221600 | $85-145 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=electrolux-washer-error-code-e20), [Amazon](https://www.amazon.com) |
| Pump filter (basket only) | Electrolux 137519400 | $25-45 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=electrolux-washer-error-code-e20), [Amazon](https://www.amazon.com) |
| Drain hose (corrugated) | Electrolux 137120900 | $35-65 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=electrolux-washer-error-code-e20), [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=electrolux-washer-error-code-e20) |
| Pressure transducer | Electrolux 134762000 | $55-95 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=electrolux-washer-error-code-e20), [Amazon](https://www.amazon.com) |
| Air hose to transducer | Electrolux 137220900 | $15-25 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=electrolux-washer-error-code-e20) |
| Main PCB (varies by model) | Electrolux 134743700 | $245-485 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=electrolux-washer-error-code-e20), [Amazon](https://www.amazon.com) |
| Tub bearing kit | Electrolux 134721500 | $135-225 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=electrolux-washer-error-code-e20), [Amazon](https://www.amazon.com) |
| Stainless braided fill hose set | Generic / Camco | $15-25 | [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=electrolux-washer-error-code-e20), [Amazon](https://www.amazon.com) |

Electrolux and Frigidaire are sister brands under the same parent company; many washer parts cross between brands with shared part numbers in the 5300, 5304, 134, and 137 series.

## When to call a professional

Call an appliance tech when:

- You've cleaned the filter, drain hose, and the pump still doesn't drain. Pump bearing or impeller failure — replace the pump.
- You see water on the floor under or behind the washer. Could be a pump seal, hose failure, or tub leak.
- The washer makes a loud grinding noise during drain. Bearing failure in the pump or possibly the main tub bearing — main tub bearing replacement is 8-12 hours and often not cost-effective.
- The unit is under Electrolux warranty (typically 1 year parts; some premium models extend the motor warranty to 10 years).

## FAQs

**How often should I clean the pump filter?**
Electrolux recommends every 3-6 months. In households with heavy use or pets, monthly is better. Most users never do it — and then are surprised by E20.

**Can I run the washer to drain water if E20 shows?**
The board has paused the cycle. Cycling power may temporarily clear the code but it'll return immediately if the underlying drain restriction isn't resolved. Use the small drain hose at the filter access panel to manually drain.

**Will hot water clear a clogged drain hose?**
Soapy buildup in the corrugated drain hose can sometimes be flushed with very hot water (140°F+) but the result is temporary. Replace the hose if it's restrictive.

**My pump runs but no water comes out. What does that mean?**
Either the impeller has demagnetized (rare-earth magnet inside the rotor lost its grip — pump spins but doesn't pump), or the impeller is broken and just spinning freely. Pull the pump and inspect.

**Difference between E20 and E21?**
E20 = drain didn't complete within timeout (could be pump or restriction). E21 = pump motor didn't respond electrically (no current draw, open winding). E21 always means a dead pump; E20 can be either pump or restriction.

## Related guides

- [Frigidaire Refrigerator Error Code SY EF — Evap Fan Fix](/posts/frigidaire-refrigerator-error-code-sy-ef)
- [Frigidaire Dishwasher Error Code i30 — Water in Base Fix](/posts/frigidaire-dishwasher-error-code-i30)
- [LG Washer Error LE — Motor Lock Fix](/posts/lg-washer-error-le)
