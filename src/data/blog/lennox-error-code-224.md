---
title: "Lennox Error Code 224 — HSI Relay Failure Fix"
description: "Lennox error code 224 — displayed on the alphanumeric LED of G24M, G50, G60, SLP98V, EL296V, and similar Lennox boards — means the control's HSI (hot..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: lennox-error-code-224
featured: false
draft: false
tags:
  - lennox
  - hvac
  - error-codes
  - hsi-relay-failure
---
## Quick answer

Lennox error code 224 — displayed on the alphanumeric LED of G24M, G50, G60, SLP98V, EL296V, and similar Lennox boards — means the control's HSI (hot surface ignitor) relay self-test failed. The board energized the HSI relay, sensed back through the HSI current shunt, and either saw no current when current was commanded or saw current when no current was commanded. This is a hard fault — the board will not attempt ignition. Cause is most often a failed control board relay (board replacement), occasionally a wiring issue between board and HSI, rarely an HSI lead-in problem that backs up into the relay sense circuit.

## What error 224 means on a Lennox

Lennox went to alphanumeric diagnostic codes on most modern boards. The code "224" displays as actual digits, not as a count of LED flashes. The installer's manual code dictionary labels 224 as "HSI Relay Fail" or "Hot Surface Ignitor Relay Failure."

What the board is doing: before energizing the HSI for a normal ignition cycle, the board verifies the HSI relay is in a known-good state. It cycles the relay (briefly), measures current through a shunt or CT in the HSI circuit, and compares against expected behavior. The board expects:
- Relay open: zero current through the HSI circuit
- Relay closed: a specific current range based on HSI resistance and applied voltage

If the relay welds closed (current always flowing), the board sees current with relay commanded open — 224. If the relay fails to close (no current when commanded), the board sees zero current with relay commanded closed — also 224. If the relay closes but a different problem (broken HSI, open lead) prevents current flow, the board still sees the no-current condition and reports 224.

This is distinct from code 240 (HSI Failed) — 240 checks the HSI element resistance directly, while 224 checks the relay function. They have different root causes and different repair paths.

## Common causes (ranked by frequency)

1. **Welded HSI relay on control board** — about 50%. Long-term HSI cycling fatigues the relay contacts, eventually welding closed or burning open. Board replacement.
2. **Open HSI relay contacts (failed to close)** — about 20%. Same mechanism, different failure mode. Still board replacement.
3. **Broken HSI lead wire or connector** — about 10%. The wire between the board and the HSI element has broken inside its insulation; the relay closes but no current flows.
4. **HSI element open** — about 8%. The ignitor element itself has failed open. (Note: pure HSI failure usually shows as code 240 first; if the failure mode looks like both 240 and 224, suspect the element.)
5. **HSI ground fault** — about 5%. The HSI lead has chafed to ground, board sees current flowing with relay open (leakage path) and reports relay welded.
6. **Wrong HSI installed** — about 4%. Silicon carbide HSI installed where a nitride was specified (or vice versa); resistance differs, current through the shunt is out of expected range.
7. **Failed control board relay sense circuit (separate from the relay itself)** — about 3%. The current shunt or its op-amp has failed, board mis-reads relay state.

**Pro nugget:** Lennox SLP98V and EL296V boards have a known HSI relay aging pattern where the relay starts producing intermittent 224s about 100,000+ cycles in (roughly 8-12 years on a normally-cycled residential furnace). Symptom: works fine for weeks, then throws 224 on one cold morning, clears on power cycle, runs fine again, throws another 224 a week later. Once you see two 224s in a month on a board 8+ years old, plan board replacement. Don't wait for the relay to weld closed mid-cycle — that's an HSI-on-continuously condition that can damage the burner cell or warp the HSI mounting bracket.

## Step-by-step fix

Before you start: power off at the furnace switch, gas off at the gas valve. Let the unit cool. The HSI is immediately downstream of where ignition occurs and is fragile.

1. **Confirm the code on the display.** "224" alphanumeric, not three flashes. Photograph the wiring diagram inside the door for reference.

2. **Inspect the HSI lead wires and connector.** Remove the burner cover. The HSI has two wires — typically with high-temp insulation, ending in a small molex connector or two spade terminals at the board. Look for: chafing on sheet metal edges, melted insulation from contact with the burner cell, pulled-out spade lugs, and corrosion at any connection.

3. **Test HSI resistance.** Power off, disconnect the HSI leads at the board. Set a multimeter to ohms and probe across the two HSI lead ends. A nitride HSI reads typically 40-90 Ω cold. An open HSI reads OL. A shorted HSI reads near 0 Ω. If the HSI is open or shorted, replace it before troubleshooting further.

4. **Check HSI lead for ground fault.** With one HSI lead disconnected, probe from each HSI terminal to the chassis ground (cabinet metal). Should read OL — no continuity. Any reading indicates a chafed lead or HSI insulator breakdown. Replace the HSI assembly.

5. **Inspect the integrated control board.** Pull the board (with all connections labeled and photographed first) and visually inspect for: scorched relay area (the HSI relay is typically near the high-current screw terminals), discoloration on relay contacts, swollen or leaking electrolytic capacitors near the HSI driver section. Visible damage = board replacement.

6. **Check 120V power to the board.** With power on but heat call not active, meter the line voltage at the board's L1/N terminals. Should read 115-125 VAC. Marginal line voltage stresses the HSI relay and accelerates failure.

7. **Test the relay function (advanced, optional).** With the burner area visible and a meter on the HSI leads at the board (with HSI disconnected), call for heat. Watch the meter during HSI warmup phase. Should see 115-125 VAC appear at the leads when the board commands HSI on. No voltage = relay didn't close (board issue). Voltage present but no HSI current in the actual circuit (when HSI reconnected) = relay good, problem is downstream.

8. **Replace the control board.** If the board's HSI relay or sense circuit has failed, replacement is the path. Lennox uses several board families — match exactly to the model and serial of your unit. Boards are ~$300-500 for residential Lennox.

9. **After board replacement, verify with a complete cycle.** Cold start. The new board will run through its self-tests on first power-up. Should show no error on the display, then proceed to a normal heat call. Verify HSI glows orange-white during warmup (typical 30-45 seconds), gas valve opens, flame establishes, code 224 does not return.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Integrated control board (G24M/G50 family) | Lennox 81W03 | $295-440 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Integrated control board (SLP98V) | Lennox 67M41 | $445-680 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| HSI (nitride, Norton 27W92 family) | Lennox 27W92 / 78H56 | $45-75 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| HSI bracket assembly | Lennox 47W37 | $35-55 | [RepairClinic](https://www.repairclinic.com) |
| HSI wiring harness | Lennox 50J27 | $25-45 | [RepairClinic](https://www.repairclinic.com) |
| Flame sensor | Lennox 24L8501 | $35-55 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Multimeter with ohms and AC voltage | Klein MM700 | $145-195 | [Amazon](https://www.amazon.com), [Home Depot](https://www.homedepot.com) |

## When to call a professional

Call a licensed HVAC tech for 224 if:

- You confirm the relay is welded closed (you measured continuous HSI current with relay commanded off). This board needs replacement and Lennox boards are model-specific — getting the wrong board causes secondary problems.
- The furnace is a Lennox SLP98V, EL296V, or other communicating variable-speed unit. These boards interact with the iComfort thermostat and require either iComfort-aware service or specific commissioning steps after replacement.
- The HSI relay welded closed and the HSI ran continuously — there may be downstream damage (warped HSI bracket, scorched burner cell front) that needs evaluation.
- You see any sign of board scorching beyond just the relay area. Heavy damage suggests upstream power issues (surges, brownouts) that may take out the replacement board too.
- The unit is under warranty. Lennox warranty terms typically require licensed service for board replacement.

## FAQs

**Can I bypass the HSI relay and run the HSI directly off line voltage to test?**
Strongly do not do this on a furnace. The relay is part of the safety chain — bypassing it means the HSI runs continuously, including outside the proper ignition window, which can ignite gas at inappropriate times or cause HSI overheating damage. Test by measuring, not by bypassing.

**Why does my Lennox display 224 only sometimes?**
Aging relay. A relay that's intermittent today welds permanently tomorrow. Replace the board — don't wait for the failure to escalate.

**Difference between 224 and 240?**
240 = HSI element resistance out of expected range (cracked or open HSI). 224 = HSI relay failure on the control board. They check different things, have different roots, and different repairs.

**Will a power surge cause 224?**
Yes — relay contacts can weld from current transients during a surge. Whole-house surge protection at the panel ($150-300) is cheap insurance for the integrated control on any modern furnace.

**Is the Lennox iComfort thermostat affected by code 224?**
The iComfort displays the same error code 224 sent up from the integrated control. The thermostat itself isn't faulty. Don't replace the thermostat for a 224 code — the board is the problem.

## Related guides

- [Lennox Error Code 240 — Ignitor Failed Fix](/posts/lennox-error-code-240)
- [Lennox Error Code 270 — Flame Signal Lost Fix](/posts/lennox-error-code-270)
- [Carrier 33 Error Code — Limit Circuit Fault Fix](/posts/carrier-33-error-code)
