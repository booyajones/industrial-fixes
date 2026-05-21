---
title: "Lennox Error Code 240 — Ignitor Failed Fix"
description: "Error code 240 on a Lennox furnace — shown on the alphanumeric display of G24M, G50, G60, SLP98V, and EL296V control boards — means the hot surface igniter..."
pubDatetime: 2026-05-20T17:00:00Z
modDatetime: 2026-05-20T17:00:00Z
author: "Dana Kowalski"
slug: lennox-error-code-240
featured: false
draft: false
tags:
  - lennox
  - hvac
  - error-codes
  - ignitor-failed
---
## Quick answer

Error code 240 on a Lennox furnace — shown on the alphanumeric display of G24M, G50, G60, SLP98V, and EL296V control boards — means the hot surface igniter (HSI) failed the board's pre-ignition self-check. The board reads cold resistance through the HSI circuit and saw either an open circuit, a short, or a resistance outside the expected 40-90Ω band. About 80% of the time the cure is a $50 igniter; the other 20% it's a wiring fault, a bad ignitor harness, or rarely, a control board issue.

## What 240 means on a Lennox

Lennox went to alphanumeric diagnostic codes on most modern boards — you'll see "240" displayed as digits, not as a count of LED flashes. The code dictionary in the installer's manual labels 240 as "Hot Surface Ignitor Failed" or "Ignitor Circuit Failed." This is one of Lennox's hard-fault codes: the board will not attempt ignition while 240 is active, and the system will not clear the code on its own — you have to fix it and either cycle power or use the diagnostic clear function on the board.

Here's what the board is actually doing. On every heat call, before energizing the HSI, the Lennox board pulses a tiny test voltage through the HSI element and measures the resistance. A Lennox-standard nitride HSI (Norton/CoorsTek 27W92 family is the most common OEM) reads about 50-90Ω cold. If the resistance is OL (open circuit — element cracked through), too low (short), or drastically out of band, the board posts 240 and never moves to the ignition sequence.

This is genuinely useful — older furnaces would energize a cracked HSI, see no flame, lock out on a flame-prove error, and you'd chase the wrong fault. The 240 cuts straight to "your igniter is the problem."

## Common causes (ranked by frequency)

1. **Cracked or open HSI element** — about 65%. Nitride HSIs are durable but they do fail, especially after 5-10 years of cycling.
2. **Broken HSI lead wire or melted lead insulation** — about 12%. The leads run close to the burner box and can melt.
3. **Bad HSI connector / harness plug** — about 10%. Spade terminals corrode, the molex plug pin pushes back.
4. **Cracked ceramic HSI base** — about 5%. The HSI element looks OK but the ceramic carrier is cracked, breaking continuity intermittently.
5. **Wrong HSI installed (silicon carbide instead of nitride, or vice versa)** — about 4%. Resistance differs significantly between the two types.
6. **Control board HSI driver failure** — about 4%. Rare but possible, especially on older units.

Field nugget: when a homeowner reports the furnace "worked fine yesterday, threw 240 this morning," the HSI is almost certainly cracked. Nitride HSIs fail in a specific pattern — they cycle through hundreds of thermal stresses just fine, then one cycle they crack on cooldown. The crack opens the circuit, and the next start posts 240. This is not a worn-down failure; it's a one-cycle failure. So even a "newish" HSI (3-4 years old) is a fair suspect.

## Step-by-step fix

Safety first: kill power at the furnace disconnect. Wait at least five minutes after a cycle for the HSI to cool. Nitride HSIs are brittle and can crack if you touch the element with bare fingers — skin oils create thermal stress points. Use a clean cloth or gloves.

1. **Confirm the code on the display.** Open the lower door, find the control board (Lennox G24M, G50, G60, SLP98, EL296 platforms have a 2-3 digit alphanumeric display). Cycle through any history codes — most Lennox boards show "240" as the active code and may also display recent history (often by pressing a small button labeled "MORE" or "STATUS"). Note any other codes alongside 240; they can point to harness issues.

2. **Power down and locate the HSI.** It's just inside the burner box — a small element on a ceramic base, mounted with one or two screws, with two wire leads running to a quick-disconnect plug. The plug usually has a small clip you have to depress.

3. **Visually inspect.** Look at the HSI element. Cracks are usually obvious — you'll see a fissure across the element, sometimes a piece broken off entirely. The ceramic base should be intact. Check the lead wires for melted insulation, especially near the burner box. If you see bare copper or charred insulation, the leads are compromised even if the element looks intact.

4. **Cold-resistance test.** With the HSI fully disconnected from the board, put a multimeter on the lowest ohm scale and probe across the two element terminals. A healthy Lennox nitride HSI reads 40-90Ω at room temperature. The 27W92-family OEM HSI typically reads 50-70Ω. Open circuit (OL) means the element is cracked through. Below 5Ω means it's shorted. Outside 40-90Ω = replace.

5. **Inspect the HSI plug and harness.** On the board side, the HSI plug is usually a 2-pin polarized connector. Pull it off, look for corrosion on the pins, check that the pins aren't pushed back into the housing. With the HSI disconnected, you can also probe continuity through the harness from the plug to wherever it connects on the burner side — should be near-zero ohms on both leads.

6. **Replace the HSI.** Order the correct OEM part — for most Lennox 80% AFUE units, that's Lennox 27W92 or 33M50 (universal Norton). For 90%+ AFUE units, often Lennox 78H56 or the EL/SLP series equivalents. Cross-check the part number on the original. Install the new HSI, mount with the original screws, plug in the harness. Do not touch the element with bare fingers — use the cardboard sleeve the part ships with.

7. **Clear the code and test fire.** Restore power. Most Lennox boards auto-clear 240 when the HSI passes its next self-check. If the code persists with a known-good new HSI, you have a wiring or board issue. With code cleared, set thermostat above setpoint and watch a full cycle: inducer → pressure switch → HSI glows orange-white (45-60 seconds for nitride) → gas valve opens → flame establishes → blower delays then runs.

8. **Verify flame current.** With burners firing, measure flame current with a meter in series with the flame sensor lead — set to DC microamps. Lennox spec is 2-6 µA DC; below 0.7 µA the board cannot reliably prove flame and you'll get inconsistent operation. If flame current is low after the HSI fix, clean the flame sensor with 0000 steel wool while you have everything apart.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Hot surface igniter (nitride, common 80% AFUE) | Lennox 27W92 / 100946-01 | $40-70 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Hot surface igniter (90% AFUE platforms) | Lennox 78H56 / 100946-04 | $50-85 | [RepairClinic](https://www.repairclinic.com), [Home Depot](https://www.homedepot.com) |
| Universal HSI (Norton 271N) | Norton / White-Rodgers 767A-373 | $25-45 | [Amazon](https://www.amazon.com), [Lowes](https://www.lowes.com) |
| HSI wiring harness | Lennox 33M50 | $20-35 | [RepairClinic](https://www.repairclinic.com) |
| Flame sensor | Lennox 69M15 / 27W23 | $25-45 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Integrated control board | Lennox 47W37 / 103217-01 (G60) | $300-460 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |

Note: silicon carbide HSIs (older Lennox style) and nitride HSIs are *not* interchangeable without confirming the board supports the new element's resistance profile. The 27W92 family is nitride. The older 14J11 family was silicon carbide. If you swap one type for the other, the board may post 240 again because the resistance doesn't match the expected range. Always match element type.

## When to call a professional

**Replaced HSI, code returns.** If a known-good new HSI throws 240 immediately on the first heat call, you have either a control board fault (HSI driver circuit damaged) or harness short you couldn't find. Board replacement on Lennox can be $300-500 in parts plus an hour of labor with proper configuration; worth a pro who has the model-specific install sheet.

**Burnt or melted wiring on the burner side.** Melted insulation in the burner area is a sign of higher-than-normal heat exposure — could mean misaligned burners, a partial gas valve issue, or a vent restriction causing flame to creep upstream. The wiring is easy to fix; the underlying cause needs combustion analysis.

**Repeated HSI failures within 12 months.** If you're on your second or third HSI in a year, something is killing them prematurely — typically excessive voltage (line voltage above 130V) or vibration. A pro can verify supply voltage and check mounting integrity.

Never bypass the 240 fault by jumpering anything. The HSI circuit and the flame-prove circuit are gas safety systems. Bypassing means uncontrolled gas flow into the heat exchanger — fire and CO risk.

## FAQs

**My display shows "240" then changes to "224" — are these the same?**
No. 224 on most Lennox platforms is a "low flame sense current" code, different from 240's pre-ignition HSI fault. Address whichever code is active most recently. If both alternate, fix the HSI first (240) then re-test for the flame sense issue.

**Can I use a universal HSI from Home Depot?**
Often yes — the Norton universal kits (767A-373 and similar) come with multiple mounting brackets and work on most Lennox 80% AFUE units. Match the resistance band (most universals are 40-75Ω, within Lennox spec). Read the install sheet — some universals require trimming the mounting bracket.

**The HSI glows but the furnace still throws 240. Possible?**
Unusual but possible if the HSI is intermittent — element shows continuity when cool and fails only at temperature. Cold-test it; if it's borderline (just inside the 40-90Ω band), swap it. They're cheap.

**How long does an HSI last?**
Average life is 5-8 years of normal use. Heavy cycling (small house with oversized furnace, short-cycling thermostat) shortens it. Long shoulder seasons with hundreds of starts a month wear them faster than steady winter operation.

**I replaced the igniter and it still won't light — what now?**
Code 240 should clear after replacement if the HSI is the issue. If you've replaced the HSI and the *unit still won't ignite* but no longer shows 240, you've moved on to a different problem — usually gas supply, flame sensor, or a separate fault code. Recheck the display.

## Related guides

- [Trane 2-Blink Error Code — External Lockout Fix](/posts/trane-2-blink-error-code)
- [Goodman 3-Flash Error Code — Pressure Switch Open Fix](/posts/goodman-3-flash-error-code)
- [York 1-Blink Error Code — Pressure Switch Stuck Closed Fix](/posts/york-error-code-1)
