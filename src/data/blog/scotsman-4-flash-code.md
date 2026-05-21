---
title: "Scotsman 4-Flash Code — High Discharge Temperature Fix"
description: "Four flashes on a Scotsman Prodigy (or \"DT High\" / \"Discharge Temp\" on Prodigy Plus) means the discharge-line temperature sensor has read above the safety..."
pubDatetime: 2026-05-20T17:00:00Z
modDatetime: 2026-05-20T17:00:00Z
author: "Marcus Webb"
slug: scotsman-4-flash-code
featured: false
draft: false
tags:
  - scotsman
  - commercial-refrigeration
  - ice-machine
  - high-discharge-temperature
  - troubleshooting
---
## Quick answer

Four flashes on a Scotsman Prodigy (or "DT High" / "Discharge Temp" on Prodigy Plus) means the discharge-line temperature sensor has read above the safety setpoint — typically 250-275°F depending on model and firmware — and the controller has shut the compressor down to save it. This is a protection code, not a nuisance code. Ignore it and you will be replacing a compressor inside of a month. In my experience the cause splits about 50% airflow/condenser, 25% low charge, 15% compressor cooling problems (fan, oil migration), and 10% sensor or wiring issues.

## What the 4-flash code means on a Scotsman

Discharge temperature is the temperature of the refrigerant gas leaving the compressor head. On a healthy R-404A Scotsman Prodigy in a 70°F ambient with a clean condenser, you should see discharge-line temps around 160-200°F mid-freeze. The compressor itself is rated to keep going up to about 250°F at the discharge line — above that, oil starts breaking down, motor windings cook, and the compressor begins a slow death.

Scotsman protects against this with a discharge thermistor (separate part from the harvest and bin thermostats) bonded to the discharge line within an inch or two of the compressor outlet. When the thermistor reads above the firmware setpoint, the board opens the compressor contactor and logs a 4-flash. The unit will retry after a cooldown period — typically 10 minutes — and lock out after 3 consecutive trips.

Diagnostic entry: hold OFF+ON for 5 seconds on Prodigy; menu navigation on Prodigy Plus. Look at the trip history and the time between trips. A unit tripping every 25 minutes during a freeze cycle has a continuous problem (condenser, charge); a unit tripping once a day during the hottest part of service has a marginal problem (borderline airflow, borderline charge).

**Critical safety note: a 4-flash means metal got dangerously hot.** Discharge line at trip can be 250°F+ — that's enough to give you a serious burn through gloves. Let the unit sit 15 minutes before you put a hand or a clamp meter probe on the discharge line.

## Common causes (ranked by frequency)

1. **Dirty condenser or restricted airflow** — same as the 2-flash but more severe. The head pressure climbs higher, the compression ratio climbs, and discharge temp goes through the roof.
2. **Low refrigerant charge** — undercharge means less mass flow returning to cool the compressor motor (especially on hermetic and semi-hermetic compressors that use suction gas for motor cooling). Discharge temps climb fast.
3. **Failed condenser fan motor** — fan running slow, fan running backwards (after a previous motor swap with wrong rotation), or fan dead. Head pressure spikes immediately.
4. **Air recirculation / install clearance violation** — operator pushed the unit against a wall, ambient air re-circulates through the condenser, effective ambient climbs to 110-120°F.
5. **High ambient room temperature** — mechanical room at 100°F+, no make-up air, summer in a Houston taqueria. Sometimes the install itself is the failure.
6. **Failed discharge thermistor** — sensor reads high when discharge is actually normal. Less common, but real, especially on units past 8 years.
7. **Compressor mechanical issue** — internal valve plate leak or piston blow-by causes inefficient compression, longer cycles, and elevated discharge temps. Diagnose last.

## Step-by-step fix

1. **Let the unit cool, then read history.** Do not start poking around a unit that just tripped a 4-flash — the discharge line is dangerously hot. Wait 15 minutes minimum. Then enter diagnostic mode, pull history. Note the 4-flash count, time stamps, and any other concurrent codes. A 4-flash plus a 2-flash usually means progressive condenser fouling; a 4-flash alone, especially intermittent, points to charge or airflow.

2. **Verify condenser fan operation.** Power up the unit and watch the condenser fan. It should start with the compressor. Confirm direction — air should be moving outward through the condenser, not inward (a swapped motor running backwards will look like it's running fine but airflow is reversed). Check fan RPM by ear and by hand — a motor with worn bearings runs slow and you'll feel the warm motor housing. **Field insight: on C0322 and C0530 Prodigy units, the condenser fan motor (12-2509-21) develops a noticeable bearing whine 6-12 months before failure. If the motor whines on startup or you can feel rotor wobble with the fan stopped, replace it during the same visit even if it's still spinning — once it fails completely the unit will trip a 4-flash within hours and you'll be back.**

3. **Inspect and clean the condenser.** Same procedure as the 2-flash guide. Pull the front panel, vacuum the face, comb the fins, treat with coil cleaner if grease-loaded. Check the back side of the coil too — restaurant air pushes oils through the coil and they build on the leeward side.

4. **Confirm install clearances.** Minimum 6 inches on all sides for air-cooled units. Reach behind the unit, feel for warm re-circulating air. If the install is tight to a wall, the customer fix is either rearranging the install or going to a water-cooled head — there's no service fix for a violated airflow envelope.

5. **Take operating pressures and discharge temp.** Manifold gauges on R-404A air-cooled at 70°F ambient: suction 12-22 psig, discharge 200-240 psig, discharge line temp 160-200°F. If discharge is 270°F+ and discharge pressure is normal-to-low, you have a charge or motor-cooling problem, not a head-pressure problem. If both discharge pressure and discharge temp are high, you have a condenser/airflow problem. The combination tells you where to look.

6. **Leak-check before adding charge.** If you suspect undercharge, find the leak before topping off. Electronic detector, soap test all brazed joints, Schraders, and flares. Most common leaks I find on 5+ year Prodigys: suction Schrader o-ring, capillary-to-receiver flare on legacy models, and rotalock fitting at the compressor on Prodigy Plus.

7. **Verify discharge thermistor.** Disconnect the thermistor leads at the control board. Measure resistance — value depends on model but most Scotsman discharge thermistors are 10kΩ NTC, reading roughly 10kΩ at 77°F and dropping logarithmically as temp rises (around 1kΩ at 200°F). If the resistance is wildly off ambient at room temp, replace the thermistor (OEM 12-2913-01 on most Prodigy Plus heads).

8. **Diagnose compressor only after eliminating everything else.** A failing compressor with internal blow-by will show low compression ratio, low capacity, long cycles, and elevated discharge temps even with a clean condenser and full charge. Compression test or amp draw vs. nameplate is the giveaway — low amp draw with poor cooling = bad compressor. This is contractor-level work, not a field swap on a kitchen call.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|------|------------|--------------|--------------|
| Condenser fan motor (C0322/C0530) | 12-2509-21 | $158-$235 | [Parts Town](https://partstown.com) |
| Condenser fan blade | 02-3413-21 | $32-$54 | [Parts Town](https://partstown.com) |
| Discharge thermistor | 12-2913-01 | $62-$95 | [Parts Town](https://partstown.com) |
| Condenser air filter | 02-3927-01 | $18-$32 | [Parts Town](https://partstown.com) |
| Compressor (C0530 R-404A) | 12-2820-21 | $720-$1,050 | [Parts Town](https://partstown.com) |
| Coil cleaner (no-rinse, foaming) | — | $22-$35 | [Amazon](https://amazon.com) |
| Clamp meter with temp probe (Fluke 902 FC) | — | $325-$420 | [Amazon](https://amazon.com) |
| Pipe-mount thermocouple | — | $18-$32 | [Amazon](https://amazon.com) |

## When to call a professional

A 4-flash is a "stop and think" code. If you're not 608-certified and the problem isn't obviously condenser cleaning or a swappable fan motor, call a refrigeration contractor. Compressor replacement, leak repair, charge work — all of it is sealed-system. The wrong move here will cost the customer a compressor inside of two months.

If the unit is under 5 years and you suspect compressor failure, contact Scotsman tech support before opening the system — there are warranty pathways that get voided by unauthorized work, and a free or discounted compressor under warranty is worth a phone call.

## FAQs

**Q: The unit ran fine all winter and started throwing 4-flash codes when it got hot. Charge?**
A: Maybe, but more likely an airflow margin that was good enough at 65°F ambient and isn't at 90°F. Clean the condenser, verify fan operation, check install clearances. If all that's good and the unit still trips on hot days, take pressures during a hot-day cycle — borderline charge will show up as low subcooling under stress.

**Q: Discharge line is hot but discharge pressure looks normal. How is that possible?**
A: Suction-cooled motor running short on suction gas, usually from undercharge or a restricted metering device. Motor heat goes into the discharge gas. Check superheat — if it's 25°F+ at the compressor inlet, you've got a starved evaporator and the motor is cooking itself.

**Q: I replaced the condenser fan motor and the rotation is opposite. Now what?**
A: Pull the blade, flip the motor 180° on its mount if the design allows, or swap the blade to match the new direction (some Scotsman fan motors are reversible by leadwire selection — check the wiring diagram on the cover). Don't leave a fan running backwards even for a test — head pressure will spike in seconds.

**Q: How do I measure discharge line temp accurately?**
A: Pipe-mount thermocouple clamped to the discharge line within 6 inches of the compressor outlet, with insulation taped over the clamp. Reading the discharge line with an infrared gun gives you spotty readings because the line surface is shiny copper. Clamp-on thermocouple is the only way to get an accurate, repeatable number.

**Q: The unit trips a 4-flash, sits, restarts, runs fine for an hour, trips again. Pattern?**
A: That's an intermittent — usually a fan motor that runs OK cold and slows when hot (worn bearings + thermal expansion), or a borderline-charged system that only trips during peak heat-load mid-cycle. Watch a full cycle with gauges and a clamp meter on the fan motor. The numbers right before the trip will tell you which it is.

## Related guides

- [Scotsman 2-Flash Code — Long Freeze Cycle](/posts/scotsman-2-flash-code)
- [Scotsman 3-Flash Code — Long Harvest Cycle](/posts/scotsman-3-flash-code)
- [Scotsman 5-Flash Code — Pressure Sensor Fault](/posts/scotsman-5-flash-code)
