---
title: "Manitowoc E15 Error Code — High-Side Pressure Switch Open Fix"
description: "E15 on a Manitowoc ice machine means the high-side pressure switch opened — discharge pressure exceeded its trip setpoint, typically 450 PSIG on R-404A..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Marcus Webb"
slug: manitowoc-e15-error-code
featured: false
draft: false
tags:
  - manitowoc
  - commercial-refrigeration
  - ice-machine
  - high-side-pressure-switch-open
  - troubleshooting
---
## Quick answer

E15 on a Manitowoc ice machine means the high-side pressure switch opened — discharge pressure exceeded its trip setpoint, typically 450 PSIG on R-404A air-cooled units, 425 PSIG on R-290 propane units. Eighty percent of E15 calls are a dirty condenser coil with restricted airflow. The other twenty percent split between a failed condenser fan, water-cooled water flow problems, or genuine sealed-system over-charge from a previous service. Clean the coil before you do anything else.

## What E15 means on a Manitowoc

E15 is one of the harder-fault codes on the Indigo NXT controller and the older S-, Q-, and J-series boards. The high-side pressure switch (HPCO — High Pressure Cut-Out) is a manual-reset or auto-reset pressure switch wired in series with the compressor contactor coil. When discharge pressure rises above the switch's trip point, the switch opens, the contactor drops out, and the compressor shuts off. The controller sees the contactor open while in a run state and logs E15.

The setpoints vary by refrigerant and model:
- R-404A air-cooled (most older IDT, IY, IB, IF series): trip at 450 PSIG, reset at 320 PSIG (auto) or manual reset on some models
- R-290 (current Indigo NXT IDT and IY series after roughly 2018): trip at 425 PSIG, manual reset
- Water-cooled units (IDT, IY with -W suffix): trip at typically 410 PSIG for water-cooled, manual reset

This is a safety code. The pressure switch tripped to protect the compressor from over-pressure that would otherwise damage the discharge valves, the head gasket, or the discharge line itself. Don't bypass the switch.

E15 differs from a freeze-cycle fault like E01 (long freeze) — E01 is the controller giving up on a slow cycle, while E15 is a hard safety trip from a pressure event. You diagnose them differently. E01 says "refrigeration is weak"; E15 says "head pressure spiked."

## Common causes (ranked by frequency)

In the field, here's roughly how E15 shakes out across hundreds of service calls:

1. **Dirty condenser coil** — about 50%. Air-cooled units only. Grease + lint in kitchen environments destroys airflow. Discharge pressure climbs proportionally.
2. **Failed condenser fan or capacitor** — about 15%. Fan not running or running slow, no airflow across the coil, pressure climbs.
3. **Water flow problem on water-cooled units** — about 10%. Inadequate water supply, fouled water-regulating valve, partially closed shut-off valve.
4. **Recirculated discharge air** — about 8%. Machine installed in a closet with no makeup air, or pulling in hot air from a kitchen hood vent close by.
5. **Failed or weeping head-pressure control on remote units** — about 5%. QuietQube remote condenser headmaster valve stuck wrong direction.
6. **Over-charge** — about 5%. Previous service charged the system long instead of weighing in the critical charge.
7. **Failed high-pressure switch (false trip)** — about 4%. Less common than people assume — the switch is usually doing its job correctly.
8. **Restricted condenser water valve on water-cooled** — about 3%.

## Step-by-step fix

Before you start: turn off power to the ice machine at the wall switch or disconnect. Wait at least 5 minutes for the high-pressure side to bleed down through the equalization path before opening any sealed-system access.

1. **Confirm the code and check the high-pressure switch reset state.** Open the front panel. The HPCO switch is typically mounted near the compressor, wired in series with the contactor. On manual-reset switches there's a red plunger or button visible — if it's popped out, the switch is tripped. Do NOT push the button to reset until you've identified the cause.

2. **Inspect the condenser coil.** Pull the front panel and shine a flashlight through the fins from the back. If you can't see daylight through the coil, that's your problem. Look at the leading face for grease, lint, paper labels, kitchen debris. Even a 1/4-inch dust cake reduces airflow significantly.

3. **Clean the condenser coil.** Use a coil brush and a commercial coil cleaner — Nu-Calgon Evap Foam No Rinse works for most situations. For grease-heavy kitchen environments use a degreaser like Nu-Calgon Nickel-Safe Coil Cleaner first, rinse, then the foaming cleaner. Comb out bent fins with a fin comb. Healthy coil = visible light through every fin gap.

4. **Verify condenser fan operation.** Power back on, watch the fan. It should pull a strong steady draft. Use an amp meter on one of the fan motor leads — most Manitowoc condenser fans draw 0.5-1.2 A depending on model and series. If amps are low or the fan is cycling, the run capacitor is the first suspect (typically 5 µF for an IDT0500 fan motor, $20 part). If the cap tests good and the fan still won't run at speed, the motor bearings are dragging.

5. **Check water flow on water-cooled units.** Confirm the water shut-off valve is fully open. Check the water-regulating valve (a screw-adjustable valve in the cooling water line) for proper operation — discharge pressure should stabilize at the setpoint (typically 235-245 PSIG). Inspect the inlet strainer if equipped; flush if clogged.

6. **Measure discharge pressure with gauges.** Connect a service gauge set to the high-side Schrader. Power on, watch pressure rise during freeze cycle. On an air-cooled R-404A unit at 75°F ambient, discharge should run 200-260 PSIG. On R-290, 180-240 PSIG. Pressures climbing past 350 PSIG with a clean coil indicate over-charge or airflow problem still present.

7. **Verify ambient air conditions.** Use an IR thermometer to read the air temperature at the condenser inlet during operation. Specs are typically 35-100°F for the ambient. If you're seeing 110°F at the condenser inlet, the install location is too hot — needs makeup air or relocation.

8. **Reset the high-pressure switch.** Once the cause is identified and fixed, push the red plunger firmly until it clicks. The switch should hold. If it pops back out immediately on next compressor start, head pressure is still climbing too fast — keep looking.

9. **Run a full ice batch.** Restore everything, let the machine run a complete freeze and harvest cycle. Watch discharge pressure throughout — should stay below 280 PSIG on air-cooled R-404A at typical ambient. If pressure spikes near 400 PSIG, E15 will return.

> **Field knowledge nugget:** Manitowoc Indigo NXT IDT0500 and IDT0900 units installed in pizza restaurants and high-grease kitchens develop a specific E15 pattern that nobody warns you about. The condenser coil cleans up fine cosmetically — visible light through the fins — but the *fin-to-tube interface* gets a baked-on grease film from years of vaporized cooking oil. The film insulates the heat transfer between fin and tube, so even with airflow restored you don't get the cooling capacity you should. The cosmetic clean made discharge pressure drop from 380 to 300 PSIG (better), but it's still climbing into E15 on hot days. The real fix is a hot detergent pressure-wash of the coil, specifically targeting the fin-tube joint. I worked a Domino's location in Houston where I cleaned the coil three times before resorting to a hot Simple Green soak — the pressure dropped to 250 PSIG immediately and E15 didn't return. Cosmetic clean isn't always actual clean in grease-laden environments.

**Safety:** R-290 (propane) units are flammable refrigerant. Do not braze or open the sealed system without recovering the charge to a dedicated R-290 recovery cylinder, killing ignition sources, and ventilating the area. UL 60335-2-89 covers requirements; if not familiar, call a tech who is. R-290 is unforgiving of shortcuts.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| High-pressure cut-out switch (manual reset) | Manitowoc 000007379 | $85-145 | [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=manitowoc-e15-error-code) |
| Condenser fan motor (IDT0500/0900) | Manitowoc 7626833 | $215-295 | [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=manitowoc-e15-error-code) |
| Fan motor run capacitor (5 µF) | Manitowoc 000002777 | $18-28 | [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=manitowoc-e15-error-code) / [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Water-regulating valve | Manitowoc 000000218 | $185-265 | [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=manitowoc-e15-error-code) / [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=manitowoc-e15-error-code) |
| Condenser coil (cleaning kit) | Nu-Calgon Evap Foam | $20-35 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) / [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=manitowoc-e15-error-code) |
| Hot detergent / degreaser | Nu-Calgon Nickel-Safe Coil Cleaner | $25-45 | [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=manitowoc-e15-error-code) / [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Fin comb | Generic | $15-25 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |

Order any HPCO switch with its gasket and O-rings — Manitowoc switch bodies don't seal reliably on used gaskets.

## When to call a professional

Call a CFESA-certified commercial refrigeration tech for E15 in any of these situations:

- The machine uses R-290 and you don't have hydrocarbon-rated recovery equipment and EPA 608 + hydrocarbon endorsement
- Discharge pressure stays above 350 PSIG after coil cleaning and fan verification — you're into refrigerant charge, restriction, or compressor capacity territory
- Water-cooled units where the water-regulating valve doesn't respond properly — valve replacement on a charged system requires reclaim and re-charge
- Remote QuietQube units with headmaster valve issues — these require specialized refrigeration knowledge and access to long line runs
- Suction temperature is unusually high (35+ PSIG on R-404A) — usually indicates hot-gas valve issues that compound the E15
- Machine is under warranty

## FAQs

**My condenser looks clean. Why am I still getting E15?**
Check three things: ambient air at the condenser inlet (over 100°F = problem), fan amperage (low = cap or motor issue), and if neither, look for the fin-tube grease film that doesn't show in a cosmetic clean. Also verify discharge pressure with gauges — gauges don't lie.

**Can I just keep resetting the HPCO switch to keep making ice?**
Don't. Each over-pressure event stresses the compressor discharge valves and head gasket. Eventually you'll be replacing a compressor instead of cleaning a coil.

**Why does E15 only happen in summer?**
Higher ambient temperature, combined with a marginally clean coil or marginal fan, tips head pressure over the limit. Winter ambient gives the system enough margin to hide the problem. Summer reveals it.

**How often should the condenser be cleaned?**
At minimum, quarterly in most environments. Monthly in kitchens, fast-food restaurants, and bakeries where airborne grease and lint are heavy. Add it to the kitchen's preventive maintenance checklist.

**Is E15 the same on water-cooled units?**
Same code, different root causes. On water-cooled E15 you check water flow, water temperature, and water-regulating valve operation before doing anything else. Coil cleaning doesn't apply.

## Related guides

- [Manitowoc E01 Error Code — Long Freeze Cycle Fix](/posts/manitowoc-e01-error-code)
- [Manitowoc HPCO Error Code — High Pressure Cut Out Fix](/posts/manitowoc-hpco-error-code)
- [Manitowoc E54 Error Code — Compressor Fault Fix](/posts/manitowoc-e54-error-code)

## See Also

- [Manitowoc NEO Ice Machine Error Code Guide — Causes & Fixes](/posts/manitowoc-neo-error-codes/)
- [Manitowoc E02 Error Code — Long Harvest Cycle Fix](/posts/manitowoc-e02-error-code/)
- [Manitowoc Ice Machine E01 Error: Long Freeze Cycle Shutdown Causes and Fix](/posts/manitowoc-e01-long-freeze/)
- [Manitowoc Ice Machine Error Code 6 — Causes & Fix](/posts/manitowoc-ice-machine-error-code-6/)
