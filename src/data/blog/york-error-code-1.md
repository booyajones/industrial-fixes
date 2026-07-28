---
title: "York 1-Blink Error Code — Pressure Switch Stuck Closed Fix"
description: "A 1-blink code on a York furnace means the pressure switch was already closed when the board started the ignition sequence — before the inducer (draft..."
pubDatetime: 2026-05-20T17:00:00Z
modDatetime: 2026-05-20T17:00:00Z
author: "Dana Kowalski"
slug: york-error-code-1
featured: false
draft: false
tags:
  - york
  - hvac
  - error-codes
  - pressure-switch-stuck-closed-at-startup
---
## Quick answer

A 1-blink code on a York furnace means the pressure switch was already closed when the board started the ignition sequence — before the inducer (draft motor) had a chance to develop vacuum. The board's safety logic requires the switch to be open at rest and close only after the inducer pulls draft. If it's already closed, something is wrong — usually a stuck pressure switch, but it can also be a wiring short or, occasionally, residual draft from a previous cycle that hasn't fully released.

## What 1-blink means on a York

York furnaces flash diagnostic codes through an LED on the integrated control board, visible through the sight glass on the lower door. Modern York Affinity models (and the LX, TM9, TG9 series) use either a flashing LED or a small alphanumeric display — same code dictionary either way. Count one slow flash, two-second pause, one more flash; that's 1-blink, "Pressure Switch Stuck Closed."

The pressure switch is a normally-open diaphragm switch wired into the ignition sequence as a safety. The board expects this sequence:

1. Thermostat calls for heat.
2. Board energizes inducer motor.
3. Inducer pulls vacuum on the burner box / vent.
4. Pressure switch closes when vacuum hits its trip point (typically 0.4-0.6" WC for 80% AFUE, varies on 90% AFUE).
5. Board sees switch closed, energizes HSI.

On every heat call, before energizing the inducer, the board verifies the pressure switch is OPEN. If it's already closed, the board posts 1-blink and refuses to start. The logic is sound: a switch that's stuck closed means the board can't verify the inducer is actually working. The unit could start the HSI and gas valve sequence on a furnace where the vent is blocked and no draft is developing — exactly the scenario the switch exists to prevent.

## Common causes (ranked by frequency)

1. **Pressure switch stuck closed mechanically** — about 50%. Diaphragm contact welded, debris in the switch, age-related sticking.
2. **Wiring short between switch terminals** — about 20%. Pinched wire harness in the burner area, water-damaged terminal block.
3. **Wrong switch installed (lower trip pressure than spec)** — about 10%. Replacement switch with too low a setpoint closes at near-zero pressure.
4. **Pressure switch tubing condensation creating false signal** — about 8%. Water in the tube acts as a liquid switch.
5. **Inducer continuing to spin from previous cycle** — about 5%. Some 90% AFUE models with high-mass wheels coast for 30+ seconds.
6. **Board's pressure switch input damaged** — about 5%. Surge or moisture damage to the input circuit.
7. **Defective switch from factory (new replacement)** — about 2%. Rare but not zero.

Field nugget: I see this code more often on York 90% AFUE units after summer A/C use. Why? The condensate trap on the inducer can hold water all summer, and that water creates a static head that puts the pressure switch right at the edge of its trip point. On the first heating call of the fall, the switch reads "closed" because the water column inside the trap is essentially pre-loading the diaphragm. Drain the trap before the heating season — saves a service call.

## Step-by-step fix

Cut power at the disconnect before opening panels. Verify the inducer has fully stopped — on some York 90% units it can spin for 30+ seconds after power-down.

1. **Confirm the code.** Open the lower door, watch the LED through at least one full attempt to start. Confirm 1-blink. While you're there, check for any history codes the board may be storing (York Affinity boards display history on the screen; older LED boards may show recent codes by holding a button).

2. **Test the pressure switch electrically with the unit off.** Power off. Pull both wires from the pressure switch. Put a multimeter on continuity and probe across the switch's two terminals. With no vacuum applied, a single-stage switch should read OPEN (OL). If it reads continuous (zero ohms), the switch is stuck closed — replace it. If it reads open, the issue is elsewhere.

3. **Inspect the pressure switch tubing.** It's usually a 1/4" silicone or vinyl tube from the inducer port to the switch. Pull it off both ends. If water drips out, you've found at least part of your problem — water in the tube can create a static pressure signal that holds the switch partway closed. Drain the tube, then look at the condensate trap.

4. **Drain and inspect the condensate trap (90% AFUE only).** Disconnect the trap from the inducer and from the drain line. Dump it. Flush with vinegar and water. The trap should hold water but also flow freely through it — if it's clogged with biofilm, water backs up into the inducer and the pressure switch tube. Re-prime with clean water before reinstalling — a dry trap leaks flue gas.

5. **Verify the inducer is fully stopped at rest.** Power the system, wait through a full cycle, then power down at the thermostat. The inducer should spin down within about 20 seconds. If it's still spinning when the next call comes in, residual draft can hold the pressure switch closed. On variable-speed inducer models, the board controls the spin-down — if it's not happening normally, you may have an inducer or board issue.

6. **Inspect the pressure switch wiring.** Trace the wires from the switch back to the board. Look for pinched, melted, or chafed wires in the burner area. A bare conductor touching a metal panel will short the switch input to ground, which the board reads as "closed." Repair any damaged wiring with high-temp wire and proper terminal connections.

7. **Verify the switch is correct for the unit.** York uses different pressure switch setpoints across its lineup — 0.40" WC, 0.50" WC, 0.60" WC, and dual-stage variants. The setpoint is stamped on the switch face (look for "0.50 SPDT" or similar). If a previous tech installed a generic switch with the wrong setpoint, it can stay closed at rest pressures the unit normally sees. Cross-reference the model number against the York parts manual.

8. **Reassemble, restore power, and test.** From cold start, watch the full ignition sequence with the burner door off (door switch held in with tape — but verify everything is safe first). You should see: thermostat call → inducer starts → audible click as switch closes → HSI glows orange-white (30-45 seconds) → gas valve clicks → flame ignites → blower delay → blower on. If 1-blink returns, the switch is stuck — replace it.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Pressure switch (single, 0.50" WC) | York S1-02435671000 | $35-65 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=york-error-code-1), [Amazon](https://www.amazon.com) |
| Pressure switch (dual, 90% AFUE) | York S1-02441125000 | $55-95 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=york-error-code-1), [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=york-error-code-1) |
| Inducer motor assembly | York S1-32434074000 / 7062-5715 | $200-330 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=york-error-code-1), [Amazon](https://www.amazon.com) |
| Condensate trap | York S1-37315174000 | $30-50 | [Amazon](https://www.amazon.com), [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=york-error-code-1) |
| Pressure switch tubing (silicone) | Generic 1/4" | $5-10 | [Amazon](https://www.amazon.com), [Lowes](https://www.lowes.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=york-error-code-1) |
| Integrated control board (Affinity/LX) | York S1-03101932000 | $250-420 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=york-error-code-1), [Amazon](https://www.amazon.com) |
| Wiring harness (burner area) | York S1-37322097000 | $40-70 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=york-error-code-1) |

Brand note: York, Coleman, Luxaire, and Champion are all part of the Johnson Controls family (now JCI's "Heat Group") and many share OEM parts. The S1-prefix part numbers are JCI universal across these brands; check the original sticker before ordering.

## When to call a professional

**You've replaced the switch and the 1-blink returns immediately.** That points to either a board input fault or a wiring problem you couldn't isolate. Board diagnosis on the input circuit requires schematic-level testing — pro work.

**Inducer doesn't stop spinning after the cycle ends.** A variable-speed inducer that won't spin down or hum-stalls during shutdown can cause persistent pressure switch issues. The inducer motor or its driver circuit needs replacement, and on some Affinity models that's an integrated board-and-motor diagnostic.

**Repeated tripping on the first call of the season only.** If the unit works fine all winter but throws 1-blink every fall, you may have a vent or trap design issue — the system collects water during the off-season and chokes the pressure switch on first start. A pro can evaluate the venting and confirm slope, trap location, and termination height meet manufacturer spec.

Never jumper the pressure switch. I cannot stress this enough — bypassing it lets the board fire burners with no verified draft, which can fill the heat exchanger with flue gas and push CO into the house. There is no scenario in which jumpering a pressure switch is appropriate.

## FAQs

**The unit ran fine last winter — why now?**
Pressure switches age. The diaphragm membrane stiffens and the contacts can stick. A switch with five winters on it is well within its failure window. Also, condensate accumulation in the trap and tube over the off-season is a classic first-call-of-fall failure pattern.

**Can I test the switch with my mouth (sucking on the port)?**
You can, but it's imprecise and unhygienic — you're inhaling whatever is in the switch body. Better to use a manometer with a hand-pump or even a clean syringe to develop test vacuum and watch when the switch clicks closed. The trip pressure is stamped on the switch face.

**My switch has 3 terminals — which two do I test?**
On a SPDT (single-pole double-throw) switch you'll see Common, Normally Open, and Normally Closed terminals. Test between Common and Normally Open — that's the pair the board uses. With the inducer off, this pair should read open (OL). With inducer running and developing draft, it should read continuous.

**Will the furnace eventually clear the code and try again?**
Most York boards retry every 15-60 minutes depending on platform. Each retry will hit the same fault. The board won't damage itself, but you won't have heat until the switch is verified open at rest.

**The trap drained out a lot of water — should I worry about a leak?**
Some water in the trap during shoulder seasons is normal — the trap is designed to hold a water seal. A *lot* of water (filling the entire inducer area) means the drain line is restricted downstream. Verify the condensate drain is open all the way to its destination (floor drain, condensate pump, etc.).

## Related guides

- [Goodman 3-Flash Error Code — Pressure Switch Open Fix](/posts/goodman-3-flash-error-code)
- Goodman 4-Flash Error Code — Limit Switch Open Fix
- [Trane 2-Blink Error Code — External Lockout Fix](/posts/trane-2-blink-error-code)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Carrier vs Trane furnaces compared](/posts/carrier-vs-trane-furnaces/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Goodman vs Bryant furnaces compared](/posts/goodman-vs-bryant-furnaces/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Mitsubishi vs Daikin mini splits](/posts/mitsubishi-vs-daikin-mini-splits/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best combustion analyzer (2026)](/posts/best-combustion-analyzer/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best HVAC manometer (2026)](/posts/best-manometer-for-hvac/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best refrigerant gauge set (2026)](/posts/best-refrigerant-gauge-set/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best thermal imager for HVAC](/posts/best-thermal-imager-for-hvac/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best refrigerant leak detector](/posts/best-refrigerant-leak-detector/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best boiler test kit](/posts/best-boiler-test-kit/)
