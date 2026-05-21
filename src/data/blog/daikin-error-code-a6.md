---
title: "Daikin A6 Error Code — Indoor Fan Motor Fix"
description: "Daikin A6 means the indoor PCB commanded the indoor blower motor to a target RPM and didn't see the feedback tach signal come back where it expected — the..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: daikin-error-code-a6
featured: false
draft: false
tags:
  - daikin
  - hvac
  - error-codes
  - indoor-fan-motor-fault
---
## Quick answer

Daikin A6 means the indoor PCB commanded the indoor blower motor to a target RPM and didn't see the feedback tach signal come back where it expected — the motor is stalled, locked, or the Hall-effect feedback line is broken. The two most common real causes are a binding bearing on the cross-flow blower wheel and a chafed feedback wire at the motor connector, not a fried PCB.

## What A6 means on a Daikin mini split

Daikin uses BLDC (brushless DC) blower motors on virtually all modern indoor heads. The indoor PCB sends a PWM speed command and a separate DC power rail to the motor, and the motor returns a tach pulse train back to the PCB as RPM feedback. The firmware compares commanded RPM to measured RPM. If the measured RPM is zero, locked at a wrong value, or the feedback signal goes missing entirely, the PCB logs A6 and disables the call.

A6 includes several sub-failure modes that show as the same code:

- **Locked rotor** — wheel won't turn. Could be a seized bearing, a foreign object jammed in the wheel, or the wheel rubbing on the housing.
- **Stalled rotor under load** — wheel turns at startup but bogs down when the head tries to move air. Usually a marginal bearing or a partially shorted winding.
- **Broken feedback** — the motor is spinning fine, but the Hall-effect feedback line is open and the PCB can't see it. The unit may even seem to work for a brief moment before logging A6.
- **PCB output stage fault** — the motor drive transistors on the indoor PCB failed and aren't sourcing proper drive voltage.

The first three are repairable with motor or wiring replacement. The fourth is a PCB swap.

A6 on most M-series wall-mount heads (FTX, FTXS, FTKR, FTKN) is the cross-flow tangential blower behind the front panel. On MLZ cassettes it's the centrifugal blower above the drain pan. On SEZ ducted heads it's a forward-curved squirrel cage. The diagnostic approach differs slightly by form factor but the code logic is identical.

## Common causes (ranked by frequency)

1. **Bearing seizure on the cross-flow wheel** — most common on units 6+ years old. Wheel turns by hand with grinding resistance.
2. **Foreign object in the wheel** — child's toy, leaf, dust mat fragment. Wheel locked solid.
3. **Chafed Hall feedback conductor at the motor harness** — feedback open, motor itself fine.
4. **Failed BLDC motor windings** — winding open or shorted. Motor coast-tests with rough drag and uneven detents.
5. **Loose blower wheel set screw** — wheel slips on motor shaft, motor spins, wheel doesn't, no airflow but no fixed RPM signal either.
6. **Failed indoor PCB motor drive section** — rare, but board output stage can fail. Last on the list.
7. **Wrong replacement motor used in prior repair** — non-OEM BLDC with different Hall pulse count will misread.

## Step-by-step fix

1. **Kill power at the indoor breaker.** Wait at least 60 seconds for any residual DC bus voltage in the motor drive to bleed. Open the front cover and pop the front panel off the unit.

2. **Spin the blower wheel by hand.** With power off, reach into the air discharge slot and rotate the cross-flow wheel. It should spin freely, coast a few revolutions after a flick, and have no grinding or detent feel. A wheel that won't budge or grinds is a mechanical problem — bearing seizure, foreign object in the wheel, or wheel rubbing on the housing.

3. **Inspect for foreign objects and wheel-to-housing rub.** Shine a light along the length of the cross-flow wheel. Look for trapped lint, leaves, plastic fragments. Check that the wheel sits centered in the housing — a wheel that's slipped on the shaft can rub the housing on one end. The wheel set screw on Daikin FTX heads is usually a single 3 mm Allen accessed from the right end of the wheel through a small port.

4. **Pull the motor harness connector at the indoor PCB.** Look at the connector pins — usually 5 or 7 pins depending on motor style: DC power (V+), ground, PWM control input, Hall feedback signal output, and sometimes a fault-indication line. Check for corrosion or backed-out pins. Measure DC voltage on the V+ pin with power restored momentarily — you should see approximately 280-320 VDC on most platforms (this is rectified line voltage internal to the indoor PCB; **do not** probe this with the cover off and bare hands — use insulated probes).

5. **Measure motor winding resistance phase-to-phase.** With the motor disconnected from the PCB, measure between the three motor power leads. On a residential BLDC indoor motor you should read about 10-30 Ω phase-to-phase, all three readings within about 10%. An open phase or wildly imbalanced readings condemns the motor.

6. **Check the Hall feedback continuity end-to-end.** With the motor disconnected, ohm the Hall signal wire from the motor's signal pin to the corresponding pin at the PCB connector. Should be a short — under 1 Ω. If it reads open, you have a chafed wire somewhere in the run, usually where the harness exits the motor housing or where it routes past the blower bearing block.

7. **Replace the motor or the harness as needed.** Daikin cross-flow motors are model-specific (FTXS09 uses a different motor than FTXS24). OEM part numbers vary; check the Daikin parts diagram for your exact model. Aftermarket BLDC motors with different Hall pulse counts will misread — use the OEM part. When replacing a cross-flow motor, the wheel-to-motor coupling is press-fit on some platforms and set-screw on others — note which during disassembly.

8. **Reassemble, restore power, and watch the start.** With the front panel off, command a fan-only call at low speed and watch the wheel ramp up. It should start within 1-2 seconds, hold steady at low speed, then step up smoothly through medium and high. A wheel that hunts or oscillates points to a marginal motor or a wrong Hall feedback count. A wheel that starts and stops once and re-logs A6 means the PCB is still seeing a feedback fault.

> **Field knowledge nugget:** On Daikin FTX/FTXS09 and FTXS12 series wall-mount heads installed in coastal or high-humidity environments, I find a specific A6 pattern related to the cross-flow wheel bearing block on the right-hand side (the non-motor end). The bearing is a small ball bearing pressed into a plastic bearing block, and salt-laden air over a few years corrodes the bearing race. The symptom: A6 only on the first start of the morning after the unit has been off overnight, clearing if you wait 30 minutes and try again. What's happening is the bearing has enough drag when cold to keep the wheel from reaching commanded RPM, so the PCB logs A6 — but as the bearing warms slightly from the motor's heat, drag drops and the unit will run. Fix is replacement of the right-end bearing block (Daikin sells it as a kit, in the 4017019 family for FTXS09/12), about $35 and a 30-minute job. You'll see the wheel run smoothly afterward and the morning A6 stops. Motor current on these units sits around 0.15-0.35 A on low and up to 0.7 A on high; if you measure higher than that, suspect bearing drag or wheel rub.

**Safety:** R-454B refrigerant on newer Daikin equipment is A2L mildly flammable. A6 work is air-side and doesn't normally touch refrigerant, but inspect the indoor coil while you're inside the head — any oil staining or hissing sound is a refrigerant leak, and on R-454B you need to ventilate and use an A2L-rated leak detector. LFL is approximately 11.9% by volume. EPA 608 with A2L endorsement applies to any sealed-system work.

## Parts that may need replacement

| Part | OEM Number (typical) | Typical Cost | Where to Buy |
|---|---|---|---|
| Indoor BLDC blower motor (FTXS09/12) | 4017019-xx (model specific) | $165–$285 | [HVAC Parts Shop](https://www.hvacpartsshop.com?aff=PLACEHOLDER-HPS) / [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Cross-flow wheel bearing block kit | 4017019 family | $30–$55 | [HVAC Parts Shop](https://www.hvacpartsshop.com?aff=PLACEHOLDER-HPS) |
| Indoor controller PCB | 4017019-xx | $245–$380 | [HVAC Parts Shop](https://www.hvacpartsshop.com?aff=PLACEHOLDER-HPS) |
| Motor harness assembly | varies | $35–$60 | [HVAC Parts Shop](https://www.hvacpartsshop.com?aff=PLACEHOLDER-HPS) |
| Cross-flow blower wheel | varies by model | $45–$95 | [HVAC Parts Shop](https://www.hvacpartsshop.com?aff=PLACEHOLDER-HPS) |

Order the wheel set screw and Allen key with the motor — Daikin sets are 3 mm metric and easy to strip if you use the wrong size.

## When to call a professional

Call a NATE-certified tech if:

- The blower motor measures bad on the windings and the replacement is a model-specific OEM part that's hard to source. Aftermarket motors with wrong Hall pulse counts will keep throwing A6.
- The system is under the original 10-year Daikin parts warranty — the motor swap should be done by an authorized servicer to preserve coverage.
- You've replaced the motor and bearing and A6 still appears within 24 hours. That points to a PCB driver issue and is worth a board swap and a tech-support consultation.
- The unit is on R-454B refrigerant and you find any indication of refrigerant leakage during the diagnostic — that's an A2L event and requires proper recovery procedures.
- The blower wheel itself is cracked or chipped — a broken wheel can throw debris into the coil and cause secondary damage.

## FAQs

**Can A6 be caused by a dirty filter?**
Indirectly, yes. A severely clogged filter starves the airflow, the blower works harder, and over time accelerates bearing wear. A6 from a freshly dirty filter is rare; A6 because the filter has been dirty for 18 months and the bearing finally died is common.

**Why does my Daikin A6 happen only in the morning?**
Classic bearing-drag symptom. The bearing has enough static drag when cold to prevent the motor from reaching commanded RPM on the first start. As the bearing warms, drag drops and the unit runs. See the field nugget above — bearing block replacement is the fix.

**Will a generic BLDC motor work as a Daikin replacement?**
Usually not. Daikin BLDC indoor motors use specific Hall pulse counts and PWM response curves that the indoor PCB expects. A generic motor with a different Hall count will misread RPM and throw A6 even when spinning fine. Use OEM.

**How long should an indoor blower motor last?**
On a residential Daikin used 6-9 months per year in typical conditions, 8-12 years is normal. Coastal or high-humidity installations drop that to 5-8 years due to bearing corrosion. Heavy commercial cycling can shorten it further.

**Is the indoor blower motor the same as the outdoor fan motor?**
No. Outdoor fan motors are larger BLDC units with different electrical specs and a different code (P-series codes, not A6). Don't substitute one for the other.

## Related guides

- [Daikin U4 Error Code — Indoor-Outdoor Communication Fix](/posts/daikin-error-code-u4)
- [Daikin C4 Error Code — Indoor Heat Exchanger Thermistor Fix](/posts/daikin-error-code-c4)
- [Daikin L5 Error Code — Compressor Lock Fix](/posts/daikin-error-code-l5)
