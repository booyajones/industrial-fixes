---
title: "Trane / American Standard 4-Blink Error Code — Limit Circuit Trip Fix"
description: "A 4-blink code on a Trane or American Standard furnace means the high-limit safety circuit opened — the heat exchanger or supply plenum got hotter than the..."
pubDatetime: 2026-05-20T17:00:00Z
modDatetime: 2026-05-20T17:00:00Z
author: "Dana Kowalski"
slug: trane-4-blink-error-code
featured: false
draft: false
tags:
  - trane
  - hvac
  - error-codes
  - limit-circuit-trip-open
---
## Quick answer

A 4-blink code on a Trane or American Standard furnace means the high-limit safety circuit opened — the heat exchanger or supply plenum got hotter than the limit switch's trip temperature, usually 170°F to 200°F. The board cut the gas, ran the blower on high to cool things down, and flashed the code. Almost every time this is an airflow restriction: filter, blower wheel, or duct issue. The limit switch is rarely the actual problem; it's just the witness.

## What 4-blink means on a Trane / American Standard

On Trane and American Standard furnaces (same parent company, Trane Technologies; same boards, same parts), the integrated furnace control LED flashes diagnostic codes through the sight glass on the lower door. Count four slow blinks, two-second pause, four more — that's 4-blink. On XV and XC variable-speed platforms with an alphanumeric display, you'll see "4" or "41."

The limit circuit on a Trane consists of one or more thermal-disc switches wired in series — typically a main high-limit on the heat exchanger or supply plenum, plus flame rollout switches near the burners. Any of them opening triggers the 4-blink. The main limit is automatic-reset; the rollout switches are usually manual-reset (small red button on the switch body).

Trip temps are stamped on the switches themselves. You'll see markings like "L170" (170°F), "L200" (200°F), or "F300" (300°F for a rollout). When the disc opens, the board sees the limit string break, shuts the gas valve immediately, and runs the blower to dump heat out of the exchanger. This protects the heat exchanger from thermal cycling damage, which is the failure mode that leads to cracks and CO leaks.

## Common causes (ranked by frequency)

1. **Restricted filter** — about 30%. Top of the list on every brand.
2. **Closed or blocked supply registers** — about 20%. Especially in zoned systems.
3. **Dirty blower wheel** — about 15%. Caked dust between blades.
4. **Failed or weak blower motor / capacitor** — about 10%.
5. **Restricted return** — about 8%. Undersized, crushed flex, dirty return grille filter.
6. **A/C coil clogged** (upflow with coil above furnace) — about 7%.
7. **Overfired gas valve** — about 5%. Manifold pressure too high.
8. **Tripped rollout switch from previous event** — about 3%. Won't reset itself.
9. **Cracked heat exchanger hot spot** — about 2%.

Field nugget: the limit switch is almost never the actual fault — but on Trane XV80 and XV95 platforms specifically, I've seen the main limit drift low over time (a 200°F switch that now opens at 175°F). If you've ruled out every airflow issue and the temperature rise is well within spec but you're still tripping, the limit itself has lost calibration. They're inexpensive — swap it as a diagnostic. But do not lead with that.

## Step-by-step fix

Power down at the disconnect before opening panels. The blower may still be running on cooldown for a few minutes after a 4-blink; let it finish before pulling things apart.

1. **Check and replace the filter.** Pull the filter. Hold it up — if you can't see light through it, replace. For most Trane residential units, MERV 8-11 in the correct slot size is safe. If the prior owner installed a MERV 16 in a thin 1" slot, you've found your problem. Always confirm the airflow arrow points toward the furnace.

2. **Walk every supply and return register.** Open all supplies. Confirm none are blocked by furniture, rugs, or closed dampers. Pull return grilles and look for dust mats or anything blocking the return airflow path.

3. **Inspect the blower wheel.** Pull the blower door and the blower assembly (usually 2-3 screws and a wire harness). Look directly into the wheel. Dust caked between blades looks like felt — it can cut CFM by 30-50%. Pull the wheel from the housing if needed and clean with a stiff brush or wash in a parts sink. Reinstall, making sure the set screw on the wheel hub is tight against the motor shaft.

4. **Check the blower capacitor (PSC motors).** Many Trane units use PSC blower motors with a separate run capacitor. Pull the cap, measure with a capacitance meter — should read within ±6% of the printed value (commonly 5, 7.5, or 10 µF for blowers). Out of spec, replace. A weak cap means the motor never reaches rated RPM, so airflow drops.

5. **Measure temperature rise.** With heating call active and the system running, measure return air temp at the return drop and supply temp about 3 feet downstream in the supply plenum (out of line-of-sight from the heat exchanger). Subtract return from supply. Compare to the nameplate temp rise on the unit door — typically 35-65°F for 80% AFUE Trane models, 30-60°F for 90% AFUE. If you're above range, airflow is still inadequate or the unit is overfired.

6. **Verify gas manifold pressure.** Connect a digital manometer to the gas valve outlet test port with burners firing. NG should read 3.5" WC at the manifold; LP should read 10" WC. If it's high, the valve regulator is set too high — turn the adjustment screw clockwise in small increments to lower pressure (1/4 turn at a time, remeasure). Overfiring puts more BTU into the heat exchanger than the airflow can carry away.

7. **Reset any tripped rollout switches.** Look at the burner box for small thermal-disc switches with a red reset button on top. If the button is popped up, press it back down. If a rollout actually tripped, you had flame outside the burner box — that's a serious finding. Look for soot on the burners, distorted burner tubes, or evidence of flame impingement on the heat exchanger.

8. **Inspect the heat exchanger.** With a flashlight and a small mirror or borescope, look down each cell. Cracks tend to appear at the bottom welds and along bends. Trane stainless heat exchangers (XR80, XL80) have a different failure pattern than the aluminized ones — but any visible crack or fissure means the exchanger must be replaced. Stop using the furnace until it's resolved; cracked exchanger = CO into supply air.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Main high limit switch (L200) | Trane LMT01062 / SWT02927 | $30-50 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-4-blink-error-code), [Amazon](https://www.amazon.com) |
| Flame rollout switch (manual reset) | Trane SWT02926 / SWT02928 | $25-45 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-4-blink-error-code), [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-4-blink-error-code) |
| Blower motor (PSC, 1/2 HP) | Trane MOT09255 / 5SME39SL0671 | $260-420 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-4-blink-error-code), [Amazon](https://www.amazon.com) |
| Blower wheel | Trane BLW01267 | $50-90 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-4-blink-error-code) |
| Run capacitor (7.5/370V) | Generic | $12-22 | [Amazon](https://www.amazon.com), [Lowes](https://www.lowes.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-4-blink-error-code) |
| Filter (20x25x4 media cabinet) | Various MERV 8-11 | $20-40 ea | [Amazon](https://www.amazon.com), [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-4-blink-error-code) |
| Integrated control board | Trane CNT06077 / D341396P01 | $220-360 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-4-blink-error-code), [Amazon](https://www.amazon.com) |

Cross-brand note: American Standard equivalents (Freedom 80, Gold S8X1, Silver S8B1) use the same part numbers. Original-sticker check is always the safe move.

## When to call a professional

**Cracked heat exchanger.** Period. If you see any crack, fissure, or rust-through, the unit cannot be safely operated and replacement requires brazing skill, EPA 608 (refrigerant handling on heat-pump-paired units), and combustion testing. Most Trane heat exchangers are warrantied 10-20 years — you'll likely get the part free, but labor and the analysis are pro work.

**Static pressure above 1.0" WC** even after a new filter and a clean blower wheel. That means a permanent duct restriction — undersized return, kinked flex, collapsed liner inside a wall cavity. Fixing duct systems is invasive and worth a pro's eye.

**Repeat rollout trips.** A rollout switch that has tripped once and reset cleanly is a warning. If it trips again, you have flames rolling out of the burner box, which is both a CO and a fire hazard. Could be a heat exchanger restriction, a vent draft problem, or burner misalignment — none of which are homeowner repairs.

## FAQs

**The blower keeps running even with the thermostat off — is that the same code?**
The 4-blink will trigger continuous blower operation as a cooldown response. Once the limit cools and closes (auto-reset), the blower should stop. If it never stops, you have a separate issue — likely a stuck blower relay on the board or a thermostat wire short.

**My main limit switch reads continuity at room temp. Is it good?**
At room temp it should be closed (continuity). It opens only when hot. To test without heat, you can use a heat gun *gently* on the disc body — but be careful, you can permanently damage the switch with excessive heat. Better diagnostic: measure temperature rise during a normal cycle and see if you're tripping at a reasonable plenum temp.

**Will closing the basement registers help me save energy?**
No, and on a Trane with a relatively tight ECM blower curve it can push you straight into a 4-blink. Closing more than ~20% of registers raises static pressure and drops airflow below safe minimums.

**My system is two-stage — does that change anything?**
Two-stage units (XV80, XC95) usually have a separate high-fire limit and low-fire limit, or one limit with two trip points handled in firmware. The diagnostic is the same — find the airflow restriction. If only high-fire trips, you have marginal airflow that's adequate for low-fire but not high-fire.

**My nameplate says "Temperature Rise 40-70°F" — what does that mean?**
That's the spec range for supply-return temp differential during normal operation. Below 40°F you have too much airflow (unit will run too cool, possibly condense on the exchanger if it's an 80%). Above 70°F you have too little airflow, which is what trips the 4-blink. Aim for the middle of the range.

## Related guides

- [Trane 2-Blink Error Code — External Lockout Fix](/posts/trane-2-blink-error-code)
- Goodman 4-Flash Error Code — Limit Switch Open Fix
- [Lennox Error Code 240 — Ignitor Failed Fix](/posts/lennox-error-code-240)
