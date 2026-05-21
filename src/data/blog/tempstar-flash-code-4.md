---
title: "Tempstar 4-Flash Error Code — Limit Switch Fix"
description: "A Tempstar 4-flash code means the integrated furnace control opened the gas valve on a heat call, but a high-limit safety switch (either the primary heat..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: tempstar-flash-code-4
featured: false
draft: false
tags:
  - tempstar
  - hvac
  - error-codes
  - limit-switch-open
---
## Quick answer

A Tempstar 4-flash code means the integrated furnace control opened the gas valve on a heat call, but a high-limit safety switch (either the primary heat exchanger limit or a rollout switch) opened during the run and shut off the gas. Roughly 55% of the time the root cause is restricted airflow — a dirty filter, closed registers, or a dirty A-coil — not a failed limit, so check airflow before swapping any safety switches.

## What 4-flash means on a Tempstar

Tempstar is one of the International Comfort Products (ICP) brands, alongside Heil, Comfortmaker, Day & Night, Arcoaire, and KeepRite. All six brands share the same Lewisburg, Tennessee assembly line and use identical part numbers — only the cabinet sticker and dealer channel differ. A Tempstar 4-flash diagnostic code, a Heil 4-flash, and a Comfortmaker 4-flash all point to the same underlying condition with the same diagnostic path.

The 4-flash code on the diagnostic LED behind the lower door means: one of the limit switches in the safety string opened during a heat call. The ICP control board doesn't distinguish between the primary high-limit (on the heat exchanger top plate) and the rollout switches (near the burner assembly) at the LED level — both fault types throw a 4-flash code. Newer ICP boards (post-2018 SmartLight variants) split this into 4-flash for primary limit and 5-flash for rollout; older boards lump them together.

The primary limit is a normally-closed thermal disc, typically rated 180-200°F auto-reset, sensing temperature at the heat exchanger top plate. When supply air temperature exceeds the rating, the disc opens, breaking the 24V safety string. The board immediately shuts the gas valve, runs the blower at high speed to dump heat from the exchanger, and posts a 4-flash. After the limit cools and resets (typically 60-90 seconds), the board allows a normal restart — but if the limit opens three more times in a row, the board enters lockout per the same 3-strike rule used on Carrier and Bryant ICP boards.

Rollout switches are manual-reset thermal switches mounted near the burner assembly, with red push-button resets sticking out the front. They sense flame escaping the heat exchanger entrance, which happens when the heat exchanger is restricted (rust scale, soot, partial blockage) or when the inducer fails to maintain draft mid-cycle. A rollout open is a more serious condition than a primary limit open — it means flame escaped its intended path.

## Common causes (ranked by frequency)

In residential ICP service experience:

1. **Restricted return airflow (dirty filter)** — about 40%. The single most common cause.
2. **Dirty A-coil downstream of the furnace** — about 15%. The coil is a flow restriction even with AC off.
3. **Closed supply registers (homeowner trying to save energy)** — about 12%.
4. **Failed blower capacitor or aging PSC motor** — about 10%.
5. **Failed primary limit switch (drifted low)** — about 8%.
6. **Heat exchanger partial blockage (rust, scale)** — about 6%.
7. **Tripped rollout switch (more serious — flame escape)** — about 5%.
8. **Improper duct sizing on original install** — about 3%.
9. **Control board fault on the safety sensing input** — about 1%.

**Pro nugget:** Tempstar/Heil/Comfortmaker primary limit switches in the N9MSE and N9MSB 90% AFUE series are typically rated 200°F auto-reset (HQ1003779HW). The factory uses 195°F switches in the western US distribution and 200°F in the eastern US — the difference accounts for varying altitudes and ambient temps. If you ship a Tempstar from a Florida warehouse to a Denver job site, the spec'd 195°F switch may trip during normal high-altitude operation. The fix is the regionally-correct switch number, not a higher-rated generic. Check the ICP altitude conversion guide for any install over 4000 ft elevation.

## Step-by-step fix

Before you start: turn off power at the furnace switch and gas at the gas cock. Wait 5 minutes for cool-down.

1. **Confirm the code and inspect rollouts.** Open the lower door, watch the LED for 4-flash. Then open the upper burner door and look at the rollout switches (one or two red buttons near the burner box). If a button is "popped" (sticking out farther than its sister), the rollout has tripped. Note this — it changes the diagnostic urgency.

2. **Change the filter.** Pull the existing filter. If it's darker than light gray on the dirty side, install a fresh one of the same MERV rating. Do not jump to MERV-13 from MERV-8 — the higher pressure drop will cause more limit trips on the existing blower.

3. **Walk every register.** Open any closed supply registers and unblock any return grilles. ICP minimum airflow on a 3-ton system is 1050 CFM (350 CFM/ton); each closed register drops you 50-100 CFM.

4. **Inspect the A-coil.** Pull the coil access panel above the furnace (or in a horizontal install, on the side). The coil fins should be clean and uniformly spaced. A coil packed with dust or pet hair acts as a flow restriction and overheats the furnace. Brush or vacuum lightly, or call for chemical cleaning.

5. **Measure temperature rise.** With a probe in the supply plenum and one in the return, fire the furnace and let it run 5 minutes. Tempstar data tag specs are typically 35-65°F rise. Above 65°F means inadequate airflow → limit trips. Below 35°F means oversized blower or overfiring.

6. **Ohm-test the primary limit.** Power off, pull both wires from the primary limit. At room temperature, the switch should read closed (continuity). If it reads open, replace it.

7. **Reset any tripped rollouts and verify ignition.** Push in the rollout button(s) firmly until you feel them click home. If a rollout has tripped, you need to identify *why* before restoring service — it doesn't trip without cause. Inspect the heat exchanger for cracks, the inducer for partial failure, and the burner alignment.

8. **Run a full cycle and monitor.** Restore power and gas. Initiate a heat call. Watch through the LED and verify normal sequence: inducer → pressure switch closes → HSI warmup → gas valve → flame → blower delay → blower on at heat speed. Continue running for 15 minutes and watch for the 4-flash code to return. If it does on the same cycle, the limit is still tripping under load — re-check airflow.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Primary limit switch (200°F auto-reset) | ICP HQ1003779HW | $35-55 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Rollout switch (manual reset, 350°F) | ICP HQ1011875HW | $25-40 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Auxiliary limit (blower deck) | ICP HQ1008420TW | $30-50 | [RepairClinic](https://www.repairclinic.com) |
| PSC blower motor 1/2 HP | ICP HC45TQ118 | $245-340 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Blower run capacitor 7.5µF/370V | Generic | $18-32 | [Amazon](https://www.amazon.com), [Home Depot](https://www.homedepot.com) |
| Integrated furnace control (SmartLight) | ICP 1183620 | $185-265 | [RepairClinic](https://www.repairclinic.com) |
| Digital manometer | Dwyer 475-1-FM | $185-235 | [Amazon](https://www.amazon.com) |
| Temperature probe set | Fluke 80PK | $85-130 | [Amazon](https://www.amazon.com) |

Tempstar/Heil/Comfortmaker cross-reference: every part above interchanges between these three brands without modification. ICP also sells these to KeepRite (Canada), Day & Night (commercial dealers), and Arcoaire (legacy) with identical part numbers — only the cabinet color and trim ring differ.

## When to call a professional

Call a licensed tech when:

- A rollout switch tripped. This points to flame escape from the heat exchanger and demands inspection of the exchanger for cracks. Combustion analysis with a CO probe is the next step. Do not reset rollouts and restore service without identifying the cause.
- You've fixed airflow, replaced the limit, and 4-flash returns within 1-2 cycles. The next step is investigation of a partial heat exchanger blockage (rust scale, water damage) — needs borescope inspection.
- You see soot on the burners or yellow flames. Combustion problem requires gas pressure check, draft measurement, and possible burner cleaning — tech work.
- The unit is under ICP warranty. Parts warranty is 5 years standard, 10 with registration; self-replace of the heat exchanger or board voids it.

## FAQs

**My rollout tripped but everything looks fine. Can I just push it back in?**
Push it in to confirm the unit will run, but do NOT consider the problem solved. The rollout doesn't open without flame escape, and flame escape means a heat exchanger condition that needs combustion analysis to verify. Schedule a tech.

**Filter is clean. A-coil is clean. Registers are open. 4-flash still happens. What's next?**
Measure static pressure with a manometer. Above 0.8 inches WC means the duct system is too restrictive — you need duct modifications (return drop, supply trunk size). Below that, suspect a marginal blower motor or capacitor.

**My Tempstar tripped 4-flash on the hottest day in summer. Why on a hot day?**
On a hot day with AC running, the return air going into the furnace cabinet is warm; when the AC then cycles off and heat eventually comes on (a temperature drop overnight), the supply air starts higher than designed and can climb past the limit faster. Modest issue — usually pairs with marginal airflow on the heat side.

**Will a smart thermostat cause 4-flash?**
A smart thermostat that calls W1 + W2 (two-stage heat) on a unit wired single-stage can over-fire. Verify wiring matches the unit's spec — Y, W, G, R, C are standard; a stray W2 jumper to W1 makes a single-stage unit run at hypothetical "high" continuously.

**Difference between 4-flash and 6-flash?**
4-flash = limit tripped. 6-flash = inducer/draft problem (no draft developed, or inducer failed mid-cycle). Different diagnostic paths — check the LED carefully.

## Related guides

- [Heil 3-Flash Error Code — Pressure Switch Fix](/posts/heil-flash-code-3)
- [Payne Error Code 31 — Pressure Switch Fix](/posts/payne-error-code-31)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code)
