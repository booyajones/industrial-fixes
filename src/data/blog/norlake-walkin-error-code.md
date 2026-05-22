---
title: "Norlake Walk-In Error Code — Defrost Issue Fix"
description: "Norlake commercial walk-in cooler and freezer controllers (typically Heatcraft Beacon II or KE2 Evap Efficiency in newer installs, Danfoss EKC in older)..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Marcus Webb"
slug: norlake-walkin-error-code
featured: false
draft: false
tags:
  - norlake
  - defrost-cycle-failure
  - troubleshooting
---
## Quick answer

Norlake commercial walk-in cooler and freezer controllers (typically Heatcraft Beacon II or KE2 Evap Efficiency in newer installs, Danfoss EKC in older) display "dF" (defrost active), "Er 02" (defrost terminator fault), or persistent ice buildup symptoms when the defrost cycle isn't completing properly. The single most common cause I see is a failed defrost terminator (snap-disc thermostat) on the coil — the controller initiates defrost, but the terminator never reaches its 55°F open setpoint, so defrost runs to its time-limit fail-safe instead of completing properly. Replace the terminator before the heater.

## What defrost faults mean on Norlake walk-ins

Norlake is one of the major US walk-in cooler/freezer manufacturers, with cabinets shipped from their Hudson, Wisconsin facility paired with Heatcraft, Russell, or Larkin/Bohn refrigeration systems. Norlake walk-in controllers handle: refrigeration on/off based on room thermostat, scheduled defrost cycles (typically 1-4 per day on freezers), fan delay during defrost, and condensate drain heat tape.

The defrost cycle on a typical Norlake walk-in freezer works as follows:

1. Controller initiates defrost at a scheduled time (every 6-8 hours typically)
2. Compressor and evap fans stop
3. Defrost heater (1500-3000W resistance heater wrapped around the evap coil) energizes
4. Heat melts ice off the coil; meltwater drips into a drain pan
5. Drain line heat tape stays energized to keep drain unfrozen
6. Defrost terminator (snap-disc on the coil) opens when coil reaches 55°F, signaling defrost complete
7. Controller stops the heater, runs evap fans alone for a brief drip-down period
8. Compressor restarts; system returns to cooling

If any step fails: heater doesn't run, terminator doesn't open, drain freezes, or controller mistimes the cycle — ice builds up on the coil over hours/days until air circulation collapses and the walk-in warms.

The controller's "defrost time-out" is a fail-safe: if the terminator doesn't open within (typically) 45 minutes, the controller ends the defrost cycle regardless. This prevents endless heating, but it also means a failed terminator results in partial defrosts that leave residual ice.

## Common causes (ranked by frequency)

In Norlake walk-in service experience:

1. **Failed defrost terminator (snap-disc thermostat)** — about 30%. Stuck closed or drifted to open at the wrong temp.
2. **Failed defrost heater** — about 22%. Resistance element open after years of thermal cycling.
3. **Drain line frozen (drain heat tape failed)** — about 18%. Water can't escape, refreezes on coil.
4. **Defrost contactor failure** — about 8%. Relay/contactor that powers the heater stuck or open.
5. **Controller schedule misconfigured (defrosts too few or too many)** — about 6%.
6. **Door left open repeatedly (excessive moisture loading)** — about 5%. Massive frost growth between defrost cycles.
7. **Refrigerant low (coil runs colder than design)** — about 4%. More frost than spec'd, defrost cycle can't keep up.
8. **EC fan motor failure causing post-defrost airflow collapse** — about 4%.
9. **Controller hardware failure** — about 2%.
10. **Wiring or sensor harness damage** — about 1%.

**Pro nugget:** Norlake walk-ins have a documented drain-line freezing problem on freezer installations where the drain line runs through unheated space. The factory ships a basic heat tape on the drain, but in extremely cold ambient (a Wisconsin January, for example), the heat tape can be insufficient if the line is more than a few feet long. Drain freezes, meltwater backs up into the evap pan during defrost, refreezes immediately, and the next defrost cycle has even more ice. **Field fix**: upgrade the drain heat tape to a higher wattage (typically 12 W/ft minimum for cold-climate installs), and add insulation around the drain run. This isn't an OEM-recommended fix but it's the only thing that works in extreme climates. Make sure the heat tape is properly bonded/grounded.

## Step-by-step fix

Before you start: walk-ins are 208V/240V single or 3-phase. Lock and tag the disconnect. Allow ice to melt fully before disassembling the coil — wet, cold components are dangerous to work with.

1. **Read controller fault history.** Heatcraft Beacon II: hold "menu" for 5 seconds, scroll to "fault history." KE2: enter service menu, view alarm log. Note any "dF" defrost faults and their timestamps.

2. **Visual inspection of evap coil.** Open the evap housing (typically 2-4 thumb screws on the front). Look at the coil — should be free of ice during normal operation. Heavy ice = defrost system not working. Note where ice is heaviest (top of coil vs. bottom vs. drain pan).

3. **Defrost terminator test.** Locate the terminator — a small disc thermostat clipped to the coil suction line or evap fins. Ohm-test at room temp: should be open. Cool with ice or by pulling and submerging in ice water — should close. Heat with a heat gun to 55-60°F — should re-open. A terminator that doesn't toggle correctly is bad.

4. **Defrost heater test.** Heater is typically a coil-shaped resistance element wrapped around the bottom of the evap coil or in a cal-rod design through the coil. Ohm-test: typically 15-40 ohms for a 2000W 240V heater. Open (OL) = dead heater.

5. **Drain line test.** Pour a quart of warm water down the evap drain pan. Water should drain freely to the outside (or to a floor drain). If water backs up, the drain line is frozen or clogged. Manually defrost the line with warm water or a hair dryer.

6. **Verify drain heat tape is energized.** Walk-in interior should be cold enough that the heat tape is warm to touch (carefully — it's not hot, but you can feel the warmth). Cold heat tape during defrost = heat tape failed or disconnected. Ohm-test for typically 200-400 ohms.

7. **Initiate manual defrost.** Most Norlake controllers allow operator-initiated defrost from the service menu. Trigger and observe: heater should energize within seconds (audible click of contactor), coil should start warming, ice should visibly melt within 10-15 minutes. If heater doesn't energize at command, contactor or wiring problem.

8. **Test the defrost contactor.** With a meter on the line side, verify 240V incoming. Command defrost — contactor coil should energize. Verify 240V on the load side passing to the heater. Stuck contactor or open coil = replace.

9. **Replace failed parts.** Most common: terminator ($45-85), heater ($145-225), contactor ($85-145). Reinstall, reassemble, restore power.

10. **Verify with full defrost cycle.** Wait for the next scheduled defrost or initiate manually. Watch through the cycle. Coil should be ice-free at end of defrost; drain should be clear; refrigeration should resume normally.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Defrost terminator (snap-disc, 55°F) | Norlake 102577 | $45-85 | [PartsTown](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=norlake-walkin-error-code), [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=norlake-walkin-error-code) |
| Defrost heater (2000W, 240V coil) | Norlake 050103 | $145-225 | [PartsTown](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=norlake-walkin-error-code), [Amazon](https://www.amazon.com) |
| Defrost contactor (30A, 2-pole) | Norlake 050106 | $85-145 | [PartsTown](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=norlake-walkin-error-code), [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=norlake-walkin-error-code) |
| Heatcraft Beacon II controller | Heatcraft 25304101 | $445-685 | [PartsTown](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=norlake-walkin-error-code) |
| KE2 Evap Efficiency controller | KE2 Therm 20226 | $385-585 | [PartsTown](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=norlake-walkin-error-code), [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=norlake-walkin-error-code) |
| EC fan motor (evap, 10" blade) | Norlake 050125 | $185-285 | [PartsTown](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=norlake-walkin-error-code), [Amazon](https://www.amazon.com) |
| NTC temperature sensor (10kΩ) | Norlake 050130 | $35-65 | [PartsTown](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=norlake-walkin-error-code) |
| Drain heat tape (per foot, 12W/ft) | Generic | $5-10/ft | [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=norlake-walkin-error-code), [Amazon](https://www.amazon.com) |
| Drain pan heater | Norlake 050135 | $115-185 | [PartsTown](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=norlake-walkin-error-code), [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=norlake-walkin-error-code) |
| Interior door release | Norlake 100330 | $185-285 | [PartsTown](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=norlake-walkin-error-code) |

PartsTown carries Norlake parts and the OEM Heatcraft Beacon and KE2 controllers that ship in modern Norlake builds.

## When to call a professional

Call an EPA-certified commercial refrigeration tech when:

- The defrost issue is paired with low suction pressure or short-cycling. Refrigerant leak — needs leak detection and recovery.
- The compressor is making unusual noise or running hot. Compressor failure imminent.
- The evap coil shows oil residue. Refrigerant leak at the coil.
- The walk-in interior door release or interior light is non-functional. OSHA-required safety items.
- The unit is under Norlake warranty (typically 1 year parts and labor; some commercial accounts have extended terms).

## FAQs

**My defrost runs but ice keeps building up. Why?**
Defrost is running but not completing properly — terminator doesn't open at 55°F, so the controller cuts defrost at the 45-minute time-out before ice fully melts. Replace the terminator.

**Can I increase the defrost cycle frequency to compensate for ice buildup?**
Short-term, yes — you can increase from 4 defrosts/day to 6/day. But this is treating the symptom, not the cause. Find and fix the underlying defrost system issue.

**Why does the drain line freeze on my Norlake walk-in?**
Insufficient heat tape, especially in cold-climate installations. Upgrade to 12 W/ft or higher, add insulation around the drain run.

**My controller schedule got wiped. What are the default defrost settings?**
For a freezer at 0°F: 4 defrosts per day (every 6 hours), 45-minute max defrost duration, 55°F terminator setpoint. For a cooler at 36°F: 1-2 defrosts per day, off-cycle defrost using fans only.

**Difference between Norlake and Master-Bilt defrost systems?**
Architecturally identical — both use heater + terminator + scheduled timer. Parts often interchange between brands. The differences are in cabinet design and the specific controller shipped from factory.

## Related guides

- [Master-Bilt Walk-In Error Code — Controller Fault Fix](/posts/master-bilt-error-code)
- [Follett Ice Machine Error Code E1 — 7CI/Vu Fix](/posts/follett-ice-machine-error-code-e1)
- [Cornelius Ice Machine Error Code — Fault Diagnosis](/posts/cornelius-ice-machine-error-code)
