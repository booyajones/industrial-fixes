---
title: "Weil-McLain Code 3 — Low Water Cutoff Fix"
description: "Code 3 on a Weil-McLain Gold or Ultra Series boiler (Ultra 80/105/155/230/310/399, GV90+, and WM97+ platforms) indicates a low water cutoff (LWCO) lockout —..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: weil-mclain-error-code-3
featured: false
draft: false
tags:
  - weil-mclain
  - hydronic
  - residential
  - low-water-cutoff
  - troubleshooting
---
## Quick answer

Code 3 on a Weil-McLain Gold or Ultra Series boiler (Ultra 80/105/155/230/310/399, GV90+, and WM97+ platforms) indicates a low water cutoff (LWCO) lockout — the boiler control has determined that system water is either physically low in the heat exchanger or the LWCO probe/float is not seeing water. The boiler will not light until the LWCO is satisfied. Roughly 70% of the time you've got a real low-water condition from a tiny leak or expansion tank failure; the other 30% is a fouled probe, a failed LWCO module, or wiring.

## What Code 3 means on a Weil-McLain

Weil-McLain integrates the LWCO logic into the U-Control / UIM (Ultra Integrated Module) on Gold and Ultra Series boilers. On older Gold GV/CGi-platform boilers, you'll see Code 3 as a flash sequence on the diagnostic LED. On Ultra and WM97+ units, "3" appears as a numeric fault code on the boiler display, often paired with the message "LWCO" or "LOW WATER."

Mechanically, the LWCO is one of two designs depending on the model:

- **Probe-type LWCO (most Ultra and WM97+ residential):** a conductive probe threaded into the supply riser or the boiler block itself. The probe completes a low-voltage circuit through the water; when water drops below the probe, resistance spikes to infinity and the control posts Code 3.
- **Float-type LWCO (some Gold and commercial-converted units):** a McDonnell & Miller 67 or RB-24 style float chamber on the boiler near the supply. Float drops, switch opens, circuit breaks.

The control will not allow firing while Code 3 is active — this is a hard ASME/CSD-1 safety lockout. On most Ultra boards the code persists until the LWCO senses water *and* you press the reset (typically holding the RESET button 3-5 seconds).

Worth knowing: Weil-McLain's LWCO test routine on Ultra series fires every 24 hours of runtime. If the probe is borderline-fouled, the boiler may run normally for weeks and then post Code 3 right after a self-test — homeowner reports "it just stopped" with no obvious leak. That's a fouled probe, not a leak.

## Common causes (ranked by frequency)

1. **Real low-water condition from a slow leak** — about 35%. Air-vent drips, a weeping relief valve, or a circulator flange leak slowly drop system pressure until water uncovers the probe.
2. **Failed/waterlogged expansion tank** — about 20%. Tank loses its air charge, system pressure swings wildly, relief valve dumps water, system runs low.
3. **Fouled or scaled LWCO probe** — about 18%. Hard water and ferrous oxide buildup insulate the probe tip; it can't sense water even when water is present.
4. **Defective LWCO probe or module** — about 12%. The probe itself or the integrated LWCO circuit on the U-Control fails.
5. **Loose probe wiring or harness corrosion** — about 8%. Spade terminal corrosion at the probe pigtail.
6. **Closed feed valve or stuck makeup water (autofeed) valve** — about 5%. System ran low and the autofeeder couldn't refill it.
7. **Air bound near the probe** — about 2%. An air pocket trapped at the probe location reads as "no water."

Field nugget: I've seen this 300 times — a homeowner calls in February with Code 3, you arrive and gauge reads 12 PSI cold (looks fine), you reset the boiler and it runs. Two weeks later, Code 3 again. The pattern is almost always a waterlogged expansion tank. The system has just enough water to satisfy the LWCO at cold pressure, but as the boiler heats to 180°F the pressure spikes to 28-30 PSI, the relief valve weeps, and over weeks the system slowly bleeds down. Check the expansion tank air charge with a tire gauge with the water side isolated — should be 12 PSI (residential) or matched to system fill pressure. If it reads 0 or you get water out the Schrader, the tank is shot.

## Step-by-step fix

Safety first: kill power at the boiler service switch. Boilers retain hot water and steam under pressure even when off — let the unit cool below 100°F before opening anything. Carbon monoxide is a real risk with gas-fired boilers; never bypass safety controls including LWCOs. If you have to drain water for service, glycol-protected systems (common in radiant) require proper recovery and pH testing on refill — straight tap water will dilute glycol below the 30% freeze-protection threshold.

1. **Read the fault display and check system pressure.** With the boiler powered (but not firing because of the lockout), confirm Code 3 on the U-Control display. Read the system pressure gauge on the supply riser. Residential cold-fill should be 12-15 PSI; hot operating around 18-22 PSI. Below 8 PSI cold = definite low-water condition.

2. **Look for leaks.** Walk the entire loop with a flashlight. Common drip points: air vent caps (the brass auto-vent at the high point), circulator flange gaskets, drain valves at low points, relief valve discharge pipe (look for white mineral residue at the floor drain or termination — that's a clue the valve has been weeping). On Ultra boilers, also check the condensate trap and PVC condensate line for cracks.

3. **Test the expansion tank.** Isolate the tank if possible (most installations have no isolation valve — you'll need to drain pressure off the system or use the tank's Schrader). Press a screwdriver tip on the Schrader. Air should hiss out; if water comes out, the bladder is ruptured and the tank is dead. With water side isolated, gauge the air pre-charge with a tire pressure gauge — should match cold fill pressure (12 PSI for most residential applications, higher for tall installations).

4. **Add water (if system is genuinely low) and bleed air.** Open the manual fill valve or operate the autofeeder until cold pressure reads 12-15 PSI. Bleed each high-point air vent and zone bleeder. On Ultra boilers with the integrated air separator, verify the float vent on the separator opens (you should hear a brief hiss when system pressure is high). Bleed air at the LWCO probe location specifically — an air pocket here keeps the probe dry.

5. **Inspect and clean the LWCO probe.** Power off, drain system pressure below the probe location. Unscrew the probe (typically 3/4" NPT, located on the supply riser or boiler block, often the only sensor with a single ring-terminal pigtail and a ceramic body). The tip should look like clean brass or stainless. If it's coated in black ferrous gunk, scale, or thread sealant residue, clean it gently with 0000 steel wool or fine sandpaper — do not file or scratch deeply. Inspect the ceramic insulator for cracks. Reinstall with fresh PTFE tape (not pipe dope on the threads near the tip — dope can foul the sensing surface).

6. **Verify probe wiring continuity.** With the probe out of the boiler and dry, you should read open circuit between the probe tip and the boiler ground (the probe body). When the tip is submerged in tap water, resistance should drop to roughly 5-50 kΩ. If it reads short circuit dry, the probe is internally shorted — replace. Confirm the pigtail spade connector at the U-Control is clean and tight; the wire color is typically yellow or violet on Ultra/WM97+ harnesses.

7. **Reset and observe the first cycle.** Restore power. Hold the RESET button (on Ultra series, it's labeled and sits on the right side of the U-Control display) for 3-5 seconds. The control should clear Code 3, run its self-test (about 10-20 seconds), and proceed to a call for heat. Watch the display through ignition: pre-purge → ignition trial → flame established → modulation. Code 3 should not return.

8. **If Code 3 returns immediately after reset with water present**, the probe or U-Control LWCO circuit is bad. Confirm by jumping the probe input *for a one-time diagnostic only* (never leave a jumper in place) — if the boiler fires with the probe input shorted, the probe is bad. If Code 3 persists even with the input jumped, the U-Control LWCO circuit is the fault.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| LWCO probe (Ultra Series) | Weil-McLain 511-330-105 | $85-120 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com) |
| LWCO probe (Gold GV90+) | Weil-McLain 511-330-095 | $75-110 | [Supply House](https://www.supplyhouse.com), [Amazon](https://www.amazon.com) |
| McDonnell & Miller 67 float LWCO (commercial conversions) | M&M 67-LWCO | $230-340 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com) |
| Expansion tank (Amtrol Extrol 30) | Amtrol EX-30 / Weil-McLain 386-700-040 | $55-85 | [Supply House](https://www.supplyhouse.com), [Home Depot](https://www.homedepot.com) |
| 30 PSI relief valve | Watts 174A / Weil-McLain 511-330-066 | $35-55 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com) |
| Float-type air vent | Taco 400-4 / Maid-O-Mist | $12-22 | [Supply House](https://www.supplyhouse.com), [Amazon](https://www.amazon.com) |
| U-Control board (Ultra) | Weil-McLain 383-500-630 | $480-720 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com) |
| Autofill valve (Watts) | Watts 1156F | $65-95 | [Supply House](https://www.supplyhouse.com), [Home Depot](https://www.homedepot.com) |

A note on probe interchange: Weil-McLain LWCO probes look similar across the line but the resistance calibration and thread length differ between Gold and Ultra. Don't substitute a 511-330-095 (Gold) for a 511-330-105 (Ultra) — the tip length is different and the seal won't seat right in the Ultra block.

## When to call a professional

**Repeated Code 3 with no visible leak.** If you've replaced the probe, verified the expansion tank, and the system still loses pressure over weeks, you likely have a microleak in the heat exchanger itself or in a buried PEX run. Hydrostatic leak testing (pressurize to 50 PSI cold, isolate and watch for 24 hours) plus a thermal camera survey is the right next step — and that's pro work.

**Heat exchanger weeping condensate that looks like water loss.** On condensing Ultra boilers, internal heat exchanger corrosion can mimic a leak. You need combustion analysis (target 8.8-9.2% CO2 on natural gas, CO below 100 ppm air-free) and a borescope inspection. If you smell anything off near the boiler — sweet, metallic, or sulfurous — get out and call a pro. CO from a cracked heat exchanger is a real risk.

**Glycol systems with persistent low pressure.** Refilling glycol-protected systems with straight water dilutes freeze protection below safe levels. A pro should pull a sample, test pH (target 8.0-10.0 for inhibited propylene glycol), test glycol percentage with a refractometer, and refill with the correct premixed solution.

Never disable the LWCO. Some old-timers will install a jumper "until the part comes in" — this is illegal under ASME CSD-1 and your insurance won't cover the resulting damage if the boiler runs dry. Dry-fire on a cast iron boiler cracks sections; dry-fire on a stainless Ultra heat exchanger warps it.

## FAQs

**Why does my boiler post Code 3 only in the morning?**
Overnight cooldown drops system pressure as water contracts. If your cold-fill pressure is borderline (8-10 PSI instead of 12-15), the morning low can uncover the probe. Bump cold-fill pressure to 12-15 PSI and verify the expansion tank holds proper air charge.

**Can I clean the probe without draining the system?**
No. The LWCO probe is in pressurized hot water. Drain pressure off the boiler and let it cool before pulling the probe. You'll lose 2-5 gallons; have a bucket ready.

**Is the LWCO required by code?**
On most modern hydronic boilers, yes — ASME CSD-1 and most state mechanical codes require a low-water cutoff on any boiler over 400,000 BTU input or any boiler with automatic firing in unattended applications. Most residential installations include one regardless because the boiler comes with it integrated.

**My pressure gauge reads 18 PSI cold — why is Code 3 active?**
First, verify the gauge — they fail. Tee in a known-good 0-60 PSI gauge at a drain valve. If actual pressure is fine, the probe is fouled or failed. If actual pressure is much lower than the gauge shows, the gauge is the fault and the system is genuinely low.

**Will resetting Code 3 with a jumper let the boiler run safely?**
No, and don't do it. The LWCO is the last-line safety preventing dry-fire damage and potential rupture. Fix the underlying cause.

## Related guides

- [Weil-McLain Code 1 — No Flame Sensed Fix](/posts/weil-mclain-error-code-1)
- [Burnham/U.S. Boiler Fault Code 2 — Ignition Lockout Fix](/posts/burnham-error-code-2)
- [Lochinvar Knight E02 — High Limit / Stack Temp Fix](/posts/lochinvar-error-code-e02)
