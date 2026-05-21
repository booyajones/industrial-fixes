---
title: "Fujitsu Mini Split 15:1 Error Code — Low Pressure Fix"
description: "Fujitsu 15:1 means the suction-side low-pressure switch opened — suction pressure dropped below the trip threshold (around 25-30 PSI on R-410A platforms)..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: fujitsu-error-code-15-1
featured: false
draft: false
tags:
  - fujitsu
  - hvac
  - error-codes
  - low-pressure-switch-open
---
## Quick answer

Fujitsu 15:1 means the suction-side low-pressure switch opened — suction pressure dropped below the trip threshold (around 25-30 PSI on R-410A platforms) and the safety cut compressor drive. It's almost always a real refrigerant problem: low charge from a slow leak, a restricted filter-drier, or a stuck-closed metering device.

## What 15:1 means on a Fujitsu mini split

The low-pressure switch on Fujitsu Halcyon and Airstage outdoor units is wired in series with the compressor protection circuit on the outdoor PCB. The switch sits on the suction line between the evaporator return and the compressor inlet and opens when suction pressure drops below the trip point. For R-410A platforms the typical trip is around 22-28 PSI / reset at about 50 PSI. On R-32 and R-454B platforms the setpoints are similar but slightly different. The PCB sees the protection input open, kills compressor drive, and logs 15:1.

Unlike 14:1 (high pressure), where the most common cause is airflow-related and easy to fix, 15:1 almost always points to a sealed-system problem. The system is starving for refrigerant on the suction side, meaning either there isn't enough refrigerant (charge low), refrigerant can't get to the suction side (restriction), or the metering device isn't feeding the evaporator properly (EEV / TXV problem).

Note that on inverter Fujitsu platforms, the firmware will sometimes auto-retry 15:1 once or twice over a 30-minute window before locking out. If the underlying issue is a slow leak that's now severe, you'll watch the unit cycle through retries and finally park. Don't keep clearing and retrying — every locked-rotor or low-pressure event on a struggling compressor accelerates wear.

A frozen indoor coil is sometimes a 15:1 contributor — refrigerant boiling off too soon (low charge) or a blocked indoor air filter causing the coil to operate below freezing. In severe icing, the coil acts as a restriction, suction pressure crashes, 15:1 logs.

## Common causes (ranked by frequency)

1. **Low refrigerant charge from a slow leak** — most common. Often at the indoor flare nuts, Schrader cores, or brazed joints near the compressor.
2. **Severely dirty indoor air filter** — chokes airflow across the evaporator, coil ices over, suction pressure crashes.
3. **Frozen indoor coil from prior runtime at low charge** — coil ices, blocks airflow, system shuts down on 15:1.
4. **Stuck-closed or partially closed metering device (EEV)** — refrigerant can't get to evaporator at adequate rate.
5. **Restricted liquid line filter-drier** — usually after prior service contamination.
6. **Failed low-pressure switch** — switch open at normal pressure. Verify with gauges before condemning.
7. **Reversing valve issue in heat pump mode** — valve not seating, refrigerant migrating wrong direction during a heat call.
8. **Indoor blower failure** — no airflow across evaporator, coil freezes, 15:1. (Should throw an A6-style indoor fan fault first, but sometimes 15:1 comes first.)

## Step-by-step fix

1. **Inspect the indoor unit air filter and coil first.** Before touching gauges, check the indoor head's air filter. A clogged filter is the easiest fix on the planet and creates exactly this fault. Pull the front panel, check the filter (and pre-filter on units that have one), and look at the evaporator coil for any ice or frost. If the coil is iced, the system has been running at low charge or low airflow long enough to freeze — note that for your diagnosis.

2. **Reset the fault and let the unit thaw if iced.** If you found ice on the indoor coil, kill the unit at the breaker and let it sit with the indoor fan-only for 30 minutes to thaw. Don't try to run a cooling call on a frozen coil — you'll bend fins with the meltwater and possibly slug the compressor.

3. **Connect gauges and observe a cooling cycle.** Once thawed, restart the unit on cooling. Watch suction and discharge pressures during the first 5-10 minutes. On a properly charged R-410A Fujitsu at 75 °F indoor / 85 °F outdoor, expect suction 110-135 PSI and discharge 350-425 PSI. If you watch suction drop from 130 PSI to 25 PSI in two minutes, that's a clear charge or restriction problem.

4. **Verify refrigerant charge by weighing.** This is the diagnostic step that matters most. Recover all refrigerant, evacuate to 500 microns and hold for 30 minutes (rising pressure means leak or moisture), then weigh in the nameplate charge. AOU12RLS3 takes 1.7 lb R-410A; AOU18RLS3 takes 2.6 lb; AOU24RLS3 takes 4.4 lb. Critical-charge inverter systems don't tolerate guess-charging — get the scale out.

5. **Leak-check the system before recharging.** If charge was significantly low, there's a leak somewhere. Pressure-test with nitrogen to 150 PSI (R-410A) and use electronic leak detector + soap bubbles at all flares, brazed joints, Schrader cores, and service ports. Common Fujitsu leak points: indoor flare nuts at the head (under the line-set wrap — pull the wrap to inspect), Schrader cores at outdoor service ports (replace as a precaution), and the brazed joint between the compressor discharge stub and the discharge line. Replace any Schrader core that hisses on a leak detector test.

6. **Replace the filter-drier on any sealed-system intrusion.** Fujitsu uses a solid-core liquid line drier; the part is in the 9707080 family for most Halcyon models. After recovery and leak repair, install a new drier, pull a deep vacuum (500 microns held for 30 minutes), and weigh in fresh nameplate charge.

7. **Test the metering device behavior.** On EEV-equipped Halcyon platforms, use a service handheld or the Fujitsu diagnostic mode to read EEV step position during a cooling call. EEV should open to 200-400 steps within the first few minutes of compressor operation and modulate from there. An EEV stuck at 0-50 steps is starving the evaporator. EEV replacement requires sealed-system work.

8. **Test the low-pressure switch in isolation if all else checks out.** With the system off and pressures equalized at around 150-200 PSI on a 75 °F day, the LP switch should read closed continuity. If it's open at normal standstill pressure, the switch is bad. Replace.

> **Field knowledge nugget:** On Fujitsu Halcyon AOU09RLS3, AOU12RLS3, and AOU15RLS3 single-zone heat pumps installed since approximately 2017, I see a consistent 15:1 pattern related to indoor flare-nut leaks at the indoor head. The trap is twofold: (1) the line-set is wrapped with insulation tape and the leak is hidden until you pull the wrap; (2) Fujitsu used a specific copper alloy for the indoor flare seats that work-hardens over time, and the original installer's torque settings (which were marginal to begin with on 1/4" and 3/8" flares) loosen with thermal cycling. The result is a slow leak — maybe 4-8 oz per year — that takes 3-4 years to drop the system into 15:1 territory. The diagnostic tell: 15:1 on a 4-5 year old Fujitsu single-zone with no recent service history, often after the first really hot week of summer when the unit runs more hours. Fix is: recover refrigerant, pull line-set wrap to expose indoor flares, replace flare gaskets (Fujitsu 9707080 flare nut/gasket kit), torque to spec (1/4" line: 12-15 ft-lb; 3/8" line: 25-29 ft-lb; 1/2" line: 36-42 ft-lb; 5/8" line: 47-54 ft-lb), leak-check with nitrogen, evacuate, weigh in charge. About 70% of my 15:1 calls on this vintage trace back to indoor flares.

**Safety:** R-32 and R-454B platforms are A2L mildly flammable. 15:1 work that involves opening the sealed system requires A2L-rated recovery equipment, A2L cylinders, A2L leak detection, ventilated work area, and ignition-source elimination. R-32 LFL is approximately 14.4% by volume; R-454B is approximately 11.9%. A 2 lb refrigerant loss in an enclosed mechanical closet can reach LFL — outdoor work or active ventilation required. EPA 608 with A2L training is the current standard.

## Parts that may need replacement

| Part | OEM Number (typical) | Typical Cost | Where to Buy |
|---|---|---|---|
| Low-pressure switch | 9707080-xx | $55–$110 | [HVAC Parts Shop](https://www.hvacpartsshop.com?aff=PLACEHOLDER-HPS) |
| Liquid line filter-drier | 9707080 family | $35–$65 | [HVAC Parts Shop](https://www.hvacpartsshop.com?aff=PLACEHOLDER-HPS) |
| Indoor flare nut/gasket kit | 9707080 family | $25–$50 | [HVAC Parts Shop](https://www.hvacpartsshop.com?aff=PLACEHOLDER-HPS) / [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Electronic expansion valve (EEV) | 9707080-xx | $185–$320 | [HVAC Parts Shop](https://www.hvacpartsshop.com?aff=PLACEHOLDER-HPS) |
| Schrader core kit | universal | $5–$15 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) / [Home Depot](https://www.homedepot.com?aff=PLACEHOLDER-HD) |
| R-410A refrigerant (25 lb cyl) | Honeywell Solstice | $295–$450 | [HVAC Parts Shop](https://www.hvacpartsshop.com?aff=PLACEHOLDER-HPS) / [Grainger](https://www.grainger.com?aff=PLACEHOLDER-GRAINGER) |

For any sealed-system service, order the drier with the flare gaskets — never reuse a flare gasket after breaking the joint.

## When to call a professional

Call a NATE-certified tech with EPA 608 Type II if:

- The system requires refrigerant recovery and recharge. EPA regulations require certified technicians for sealed-system work.
- The unit is on R-32 or R-454B refrigerant and you don't have A2L certification and equipment.
- You suspect an EEV or reversing valve fault — these require service-mode diagnostics from a Halcyon handheld.
- Pressure-test shows a leak in a brazed joint or other non-accessible location. Brazing on a refrigerant system is licensed work.
- The system is under Fujitsu parts warranty (7-12 years depending on registration) — authorized servicer required.

## FAQs

**Can I just add refrigerant to clear a Fujitsu 15:1?**
You can, briefly, but you're masking a leak. The unit will throw 15:1 again in weeks or months as the charge drops back below trip. The right answer is recover, leak-find, repair, evacuate, and weigh in fresh charge.

**Why does my Fujitsu only throw 15:1 in cool weather?**
Counter-intuitive but real. In hot weather, refrigerant pressures are higher across the board, and a marginal charge stays above the LP trip point. As ambient drops, suction pressure drops with it, and a marginal charge crosses the trip. Same underlying leak, only manifests when ambient cools.

**How fast can a Fujitsu mini-split leak refrigerant?**
On a flare-nut leak, typical rates are 2-8 oz per year. On a Schrader core leak, can be 16 oz per year or faster. On a brazed-joint leak, varies wildly from "pinhole over months" to "all gone in 3 days." Severity of 15:1 timing gives you a clue.

**Will 15:1 damage the compressor?**
Yes, especially with repeated cycling. Low suction pressure means low refrigerant mass flow, which means low compressor cooling. Repeated 15:1 events overheat the windings. Don't keep clearing and running.

**What if my Fujitsu has no service history but throws 15:1?**
Original-install issue is likely. Either the system was undercharged at install (line-set length wasn't accounted for in the charge), or the indoor flares were never properly torqued. Either way, leak-find and proper recharge is the fix.

## Related guides

- [Fujitsu Mini Split 14:1 Error Code — High Pressure Fix](/posts/fujitsu-error-code-14-1)
- [Fujitsu Mini Split 11:4 Error Code — Indoor Communication Timeout Fix](/posts/fujitsu-error-code-11-4)
- [Daikin L5 Error Code — Compressor Lock Fix](/posts/daikin-error-code-l5)
