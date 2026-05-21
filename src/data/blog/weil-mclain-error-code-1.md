---
title: "Weil-McLain Code 1 — No Flame Sensed Fix"
description: "Code 1 on a Weil-McLain Gold or Ultra Series boiler means the boiler attempted ignition but did not prove flame within the trial-for-ignition window..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: weil-mclain-error-code-1
featured: false
draft: false
tags:
  - weil-mclain
  - hydronic
  - residential
  - no-flame-sensed
  - troubleshooting
---
## Quick answer

Code 1 on a Weil-McLain Gold or Ultra Series boiler means the boiler attempted ignition but did not prove flame within the trial-for-ignition window (typically 4-7 seconds depending on platform). The U-Control or boiler integrated module energized the spark/HSI and the gas valve, but the flame rectification current dropped below the lockout threshold. Most of the time it's a dirty flame rod or a gas supply problem; less often it's the ignitor, gas valve, or control board.

## What Code 1 means on a Weil-McLain

On Ultra Series and WM97+ boilers, the integrated U-Control monitors flame via a flame-rectification probe (a stainless steel rod sitting in the burner flame). Flame current is read in microamps DC — Weil-McLain spec is typically 1.5-6 µA DC steady, with 4-6 µA being healthy on Ultra and WM97+. The board needs at least 0.8-1.0 µA to "prove" flame. If after the ignition trial the board doesn't see at least the minimum current, it shuts the gas valve and posts Code 1.

On Gold series GV90+ and earlier CGi cast-iron units, Code 1 maps to the same condition — flame not proved on ignition — but the hardware is slightly different: a separate primary ignition control (Honeywell S86 or Fenwal 35-series) communicates with the boiler module. The same field-fix logic applies.

What makes Code 1 useful is that it tells you ignition was attempted. So you can immediately rule out the "no gas valve activity" failures — pressure switch, vent blockage, blocked condensate — those throw different codes (typically Code 4 or Code 6 on Ultra). Code 1 means gas valve opened, spark or HSI fired, but flame never established or wasn't sensed.

Modern Ultra boilers will attempt three trials before hard-locking on Code 1; after the third failure the boiler enters a lockout that requires manual reset (hold RESET for 3-5 seconds). The "soft retry" history is stored — you can pull it up via the diagnostic menu and see whether the unit succeeded on later attempts even though it logged Code 1.

## Common causes (ranked by frequency)

1. **Dirty or oxidized flame rod** — about 35%. A film of oxide, dust, or combustion soot insulates the rod and drops microamp reading below threshold.
2. **Low gas pressure (supply or manifold)** — about 20%. Inlet pressure below 5" w.c. natural gas or 11" w.c. propane during firing starves the burner.
3. **Cracked or open hot surface igniter / weak spark** — about 12%. HSI doesn't reach ignition temp; spark electrode gap wrong or shorted.
4. **Bad flame rod or cracked ceramic insulator** — about 10%. Rod itself is shorted or burned through.
5. **Gas valve drift (low manifold pressure or non-opening)** — about 8%. Honeywell VR8200/VR8205 or Robertshaw 7000 valve drifts low or stops opening.
6. **Polarity reversed at the boiler** — about 5%. Hot and neutral swapped at the supply — kills flame rectification.
7. **Cracked / wet ignition wire** — about 5%. HV lead to spark electrode arcs to ground inside the boiler.
8. **U-Control board failure (flame amp circuit)** — about 3%. Rare but happens.
9. **Wet or contaminated burner head** — about 2%. Common after flooding or condensate leak.

Field nugget: I've seen this 300 times — boiler runs fine through November, throws Code 1 in mid-January after a cold snap. Customer says "it was working fine yesterday." Almost always one of two things: gas pressure droop (utility supply pressure sagged during a cold-snap demand spike and never recovered) or a marginal flame rod that finally tipped over the edge. Clue: if you can fire the boiler and it runs but the flame current reads 1.0-1.5 µA, you're not really "fixed" — you're one bad cycle from another Code 1. Get flame current above 3 µA before you leave.

## Step-by-step fix

Safety first: kill power at the boiler service switch and shut off the manual gas valve before opening the burner compartment. Natural gas and propane both displace oxygen and can pool; ventilate the boiler room before relighting. Carbon monoxide is a real risk if the burner is partially combusting — never bypass flame proving. Plug a portable low-level CO monitor in the boiler room while you troubleshoot.

1. **Read the fault and check history.** Confirm Code 1 on the U-Control display. On Ultra and WM97+ boilers, scroll the diagnostic menu to "FAULT HISTORY" — note any other codes recently logged (especially Code 4 — vent/airflow — which can cause secondary flame failures).

2. **Verify gas is on and reaching the boiler.** With the boiler off, confirm the manual shutoff is open and the gas meter shows pressure. If another gas appliance is in the building, fire it (water heater, range) to verify supply. If you have a manometer, tap into the inlet pressure port on the gas valve and measure: natural gas should be 5-10.5" w.c. static and not drop below 5" w.c. during firing; propane should be 11-13" w.c. static, 11" w.c. minimum during firing.

3. **Pull and inspect the flame rod.** Power off. Open the burner compartment. The flame rod is a single stainless rod (not paired) with one ceramic insulator and a single wire going back to the U-Control. Pull the rod assembly, inspect: the rod tip should be silver-gray or light tan oxide — heavy black or white scale insulates it. Clean with 0000 steel wool or a green Scotch-Brite pad. Do not use sandpaper — grit embeds in the rod. Inspect the ceramic insulator for cracks (a hairline crack lets flame rod ground to the burner body — kills flame current). If cracked, replace the entire rod assembly.

4. **Check the ignitor or spark electrode.** Hot surface ignition (HSI) on most modern Weil-McLain Ultra boilers: pull the HSI, check for cracks. Resistance should be 40-90Ω cold for nitride HSI; open circuit means cracked. For spark ignition (older Gold series), check electrode gap — should be 0.10-0.125" (2.5-3.2 mm) for most platforms. Look for cracked ceramic or carbon tracking down the side of the electrode (a black streak = HV leakage to ground).

5. **Inspect and clean the burner.** While the burner is exposed, look for moisture (condensate leaking from above), spider webs (yes, really — propane systems especially), or rust flakes in the burner ports. Vacuum gently with a shop vac. On Ultra Series with mesh burners, do not poke at the mesh — replace if damaged.

6. **Verify polarity at the line cord/wiring.** Plug a 3-light outlet tester into the boiler's branch circuit (or test with a multimeter): hot to ground should read 115-125V, neutral to ground should read less than 2V. Reversed polarity kills flame rectification — the flame rod relies on the rectifying property of the flame requiring a proper hot/neutral relationship. Reversed polarity = perfect flame, zero microamps.

7. **Restore power and measure flame current under fire.** Reset the boiler (hold RESET 3-5 sec). Set thermostat above setpoint to trigger a call for heat. While the boiler attempts ignition, watch through the inspection port. With a DC microamp meter in series on the flame rod lead (disconnect the rod wire at the U-Control, put the meter in line, reconnect): healthy reading is 4-6 µA DC steady. Anything 2-4 µA is marginal; below 2 µA you're going to fail again. Below 1 µA = lockout.

8. **Check manifold pressure under fire.** With the boiler firing on high, measure manifold pressure at the gas valve outlet port. Most Ultra Series natural gas spec: 3.5" w.c. on high fire (modulating). Propane spec: 10.0" w.c. high fire. Adjust at the valve only if you have a manometer and the Weil-McLain spec sheet — random adjustments will make CO emissions skyrocket. Combustion analysis is the right tool: CO2 8.8-9.2%, CO under 100 ppm air-free, O2 around 4-6% on most Ultra units.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Flame sensor / rod assembly (Ultra) | Weil-McLain 511-330-115 | $48-75 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com) |
| Flame sensor (Gold GV90+) | Weil-McLain 511-330-082 | $40-65 | [Supply House](https://www.supplyhouse.com), [Amazon](https://www.amazon.com) |
| Hot surface igniter (nitride, Ultra) | Weil-McLain 511-330-127 | $75-115 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com) |
| Spark electrode (Gold series) | Weil-McLain 511-330-070 | $35-55 | [Supply House](https://www.supplyhouse.com), [Amazon](https://www.amazon.com) |
| Gas valve (Honeywell modulating, Ultra) | Honeywell VR8615V / WM 383-500-655 | $290-460 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com) |
| Ignition cable (HV lead, Gold) | Weil-McLain 511-330-052 | $18-30 | [Supply House](https://www.supplyhouse.com), [Amazon](https://www.amazon.com) |
| U-Control board (Ultra) | Weil-McLain 383-500-630 | $480-720 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com) |
| Burner gasket | Weil-McLain 386-700-022 | $14-28 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com) |

A note on flame rods: they are technically a wear item, especially in propane installations where the alkaline combustion byproducts attack the stainless. A flame rod that cleans up nicely but reads 2 µA under fire is at end of life — replace, don't reuse.

## When to call a professional

**You can't establish flame after cleaning the rod, replacing the HSI, and verifying gas pressure.** At that point you're looking at gas valve replacement (specialty regulated component, must match Weil-McLain's part number for the platform) or U-Control board. Both require setup procedures and combustion analysis you shouldn't do without a CCAB or BPI-certified analyzer.

**Combustion smells, soot, or yellow flames.** If you do get the boiler firing but the flame is yellow-tipped, lazy, or you smell aldehydes (sharp, acrid), the burner is starved for air, over-fueled, or the heat exchanger is partially blocked. CO production at that point is uncontrolled. Combustion analysis is the only safe way forward.

**Repeated Code 1 after professional service.** If multiple visits don't resolve it, the issue may be upstream — gas meter regulator on the supply, undersized supply pipe, or a buried supply leak. Your utility can pressure-test the meter and supply line at no cost in most service areas.

Never bypass the flame proving circuit. A boiler running with gas valve open and no flame proven is dumping unburned natural gas into the heat exchanger and vent — explosion and CO risk are both real. Code 1 is doing its job.

## FAQs

**Why does my Ultra fire on first try but Code 1 after a few cycles?**
Marginal flame rod. The first fire after a long off cycle is the rod's best shot — combustion byproducts haven't built up yet. After a few cycles, oxide film grows and the microamp signal drops below threshold. Clean or replace the rod.

**Can a dirty heat exchanger cause Code 1?**
Indirectly. A heavily fouled heat exchanger reduces airflow, which alters flame stability and can move the flame off the rod. But you'd see other codes first (high stack temp, ΔT issues). Clean the HX during annual service regardless.

**My Ultra trips Code 1 only on high fire.**
Gas pressure droop. Inlet pressure is fine at low fire but sags below 5" w.c. on high. Check supply pipe sizing (Weil-McLain Ultra 155 wants 3/4" minimum within 20 feet of the meter) and confirm utility supply pressure with a manometer.

**I cleaned the flame rod and the boiler ran. Now it's back to Code 1 a week later.**
Either you didn't clean thoroughly enough or the rod is at end of life. At $50-75 retail, just replace it. Don't chase a marginal rod through multiple cleanings.

**Is propane more prone to Code 1 than natural gas?**
Yes, slightly. Propane combustion produces more sulfur and alkaline byproducts that foul flame rods faster. Annual flame rod cleaning is wise on LP systems.

## Related guides

- [Weil-McLain Code 3 — Low Water Cutoff Fix](/posts/weil-mclain-error-code-3)
- [Burnham/U.S. Boiler Fault Code 2 — Ignition Lockout Fix](/posts/burnham-error-code-2)
- [Navien NPE/NCB Code E003 — Ignition Failure Fix](/posts/navien-error-code-e003)
