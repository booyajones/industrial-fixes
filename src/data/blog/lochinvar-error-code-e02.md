---
title: "Lochinvar Knight E02 — High Limit / Stack Temp Fix"
description: "E02 on a Lochinvar Knight wall-hung (WHN, WBN) or Knight XL floor-mount condensing boiler indicates a high limit or stack temperature lockout. The SMART..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: lochinvar-error-code-e02
featured: false
draft: false
tags:
  - lochinvar
  - hydronic
  - residential
  - high-limit-stack-temp
  - troubleshooting
---
## Quick answer

E02 on a Lochinvar Knight wall-hung (WHN, WBN) or Knight XL floor-mount condensing boiler indicates a high limit or stack temperature lockout. The SMART System control saw stack temperature exceed the lockout threshold (typically 240-250°F depending on model) or saw return/supply water temp climb past the high-limit setpoint. The fix is almost always either flow restriction (low pump output, plugged strainer, closed isolation valve) or a fouled heat exchanger. Less often it's a defective stack thermistor or supply thermistor.

## What E02 means on a Lochinvar Knight

The Knight series (WHN/WBN 55-399 wall-hung, WBN/KHN 400-800 Knight XL floor-mount) runs on the SMART System or SMART TOUCH 2.0 controls. E02 maps to "Stack Temperature / High Limit" depending on platform.

Specifically, the SMART System monitors three temperatures continuously:
- **Supply (outlet) temperature** — measured at the HX outlet. Lockout default 200°F (adjustable).
- **Return (inlet) temperature** — measured at the HX inlet. Used for ΔT logic.
- **Stack (flue gas) temperature** — measured in the flue collar. Lockout fixed at 240°F (250°F on some XL models).

If supply temp exceeds the high-limit setpoint, or stack temp exceeds 240°F, the SMART System shuts the gas valve and posts E02. The boiler will not retry until the temperatures drop and you reset.

Why does stack temp climb that high on a condensing boiler? It shouldn't. A properly operating Lochinvar Knight runs stack temp 110-160°F under normal load — that's the whole point of condensing. Stack temp at 240°F means either flow is so restricted that water isn't pulling heat out of the HX (so the HX is overheating and pushing heat out the flue), or the HX fireside is so fouled that combustion gas isn't transferring heat to the water (so flue temp rises). Either way, E02 is telling you the boiler is losing efficiency and approaching unsafe conditions.

## Common causes (ranked by frequency)

1. **Low flow through the HX from a failing or undersized circulator** — about 28%. Pump can't move design flow; ΔT widens, supply temp spikes, stack temp follows.
2. **Plugged HX-side strainer or isolation valve partially closed** — about 18%. Common after recent service work where someone forgot to fully reopen a ball valve.
3. **Air binding in the HX or system high points** — about 14%. Trapped air reduces effective flow through HX.
4. **Fouled HX (fireside or waterside scale)** — about 12%. Hard-water deposits or combustion soot insulating the HX.
5. **Stack thermistor drifted or failed shorted** — about 8%. Thermistor reads high when stack is actually cooler.
6. **Supply thermistor failed or loose** — about 6%. Reads false high.
7. **Glycol percentage too high** — about 5%. Glycol over 50% reduces heat transfer dramatically; supply temp climbs to compensate.
8. **Misconfigured ΔT or pump-speed parameters in SMART System setup** — about 5%. Often after a control swap.
9. **Heat exchanger nearing end of life (corrosion or cracking)** — about 4%. Internal restriction.

Field nugget: I've seen this 300 times — Knight WHN-150 throws E02 in a tight loop, technician chases ignition, gas pressure, and ends up replacing thermistors. The fix nine times out of ten is one specific thing: someone closed the isolation ball valve below the boiler during a service call (often on a 2-pipe HX configuration), forgot, and the customer ran for hours on starved flow. The handle is in the OFF position 2 feet below the boiler. You walk up, see the handle perpendicular to the pipe, turn it 90°, and the boiler runs perfectly. Always confirm both supply and return isolation valves are fully open before you start swapping parts. Knight isolation valves have a small green dot or "OPEN" indicator that lines up with the pipe — check it.

## Step-by-step fix

Safety first: kill power at the boiler service switch. The Knight HX can hold water at 200°F+ even after lockout — let it cool to under 100°F before opening anything in the water path. Wear gloves. Condensate is acidic (pH 3.5-4.5); the Knight's neutralizer cartridge should be checked annually. If you have glycol in the system (typical for radiant or snowmelt), capture it for proper disposal — don't dump into a drain.

1. **Confirm the fault and read parameters.** On the SMART System display, navigate to FAULT HISTORY — confirm E02. Check live readings: supply temp, return temp, stack temp. If stack temp is reading 245°F+ with the boiler shut down for 10+ minutes, the stack thermistor is failed shorted. If stack temp drops normally after shutdown, the trip was real.

2. **Verify both isolation valves are fully open.** Look at the supply and return isolation valves below the boiler. Handle should be parallel to the pipe (open). The Knight ships with a 1" sweat-or-NPT isolation kit (Lochinvar WHN-IK) that includes ball valves with detent stops — partial-open positions feel different from fully open. Confirm fully open.

3. **Bleed air aggressively.** Find the manual bleed at the top of the HX (Knight has a brass bleed screw on the supply manifold). Open until you get a steady stream of water — should take 10-30 seconds. Walk the rest of the system: bleed each zone, bleed each radiator, verify automatic float vents at high points are not capped. Air in the HX is a common silent E02 cause.

4. **Check pump operation.** With a call for heat, the boiler will start its sequence — fan ramps up, pre-purge, ignition, then circulator (or HX-side circ on primary/secondary systems) energizes. Place your hand on the circulator: you should feel motor warmth and vibration. If the circ housing is cold and silent, the circ is dead or no power. Check voltage to circ — should be 115V from the boiler's circ output. If voltage is present and circ is silent, replace the circ (Taco 0015e3 or Grundfos UPS15-58FC are common Lochinvar replacements). If circ is running, verify flow direction (arrow on housing).

5. **Inspect waterside strainer.** Knight installations should include a 40-mesh Y-strainer on the return. Close isolation valves, drain the strainer cap, pull the screen. Flush with water. If the screen is loaded with black ferrous sludge, the system has untreated air infiltration corroding iron components — beyond cleaning the strainer, dose with a hydronic chemical treatment (Fernox F1 or Sentinel X100) and monitor.

6. **Inspect HX fireside.** Power off, gas off. Remove the front cabinet, pull the burner assembly (carefully — gasket is one-time-use on many models; have a replacement on hand). Look into the HX combustion chamber. Should be a uniform dull silver or light tan. White scale or heavy soot = fouled HX. Light soot you can vacuum gently; heavy fouling needs a Lochinvar-approved HX cleaning service or HX replacement. Do not use acid descalers on the fireside.

7. **Check the stack thermistor.** Power off. The stack thermistor is a small probe in the flue collar, usually with a 2-wire connector to the SMART System. Disconnect and read resistance with a multimeter at room temperature — should be approximately 10kΩ at 77°F (25°C) for the NTC 10K thermistor Lochinvar uses on most Knight platforms. Cross-check against the install manual's resistance/temperature table. If grossly out of spec, replace.

8. **Verify pH and glycol percentage.** Knight HX warranty requires fill water pH 6.5-8.5 (some sources say 6.0-8.5 with neutralizing media downstream). Use pH strips on a drained sample. For glycol systems, pull a refractometer reading — propylene glycol should be 30-50% for freeze protection without excessive heat-transfer penalty. Over 50% glycol = poor heat transfer, climbing supply temps, E02 risk.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Stack thermistor (Knight WHN/WBN) | Lochinvar 100130388 | $48-75 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com) |
| Supply/return thermistor (NTC 10K) | Lochinvar 100209345 | $35-55 | [Supply House](https://www.supplyhouse.com), [Amazon](https://www.amazon.com) |
| Circulator (Taco 0015e3) | Taco 0015e3-1IFC / replaces 100208632 | $310-440 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com) |
| Circulator (Grundfos UPS15-58FC) | Grundfos 59896341 | $280-380 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com) |
| Y-strainer 1" (return line) | Webstone H-44705 | $35-55 | [Supply House](https://www.supplyhouse.com), [Home Depot](https://www.homedepot.com) |
| Isolation valve kit (Knight WHN) | Lochinvar WHN-IK / 100211062 | $95-145 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com) |
| Burner gasket | Lochinvar 100208234 | $24-42 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com) |
| SMART System control (Knight WHN) | Lochinvar 100212430 | $620-850 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com) |
| Condensate neutralizer media (refill) | Lochinvar 100165660 | $32-55 | [Supply House](https://www.supplyhouse.com), [Amazon](https://www.amazon.com) |

A note on thermistor swaps: Lochinvar uses NTC 10K thermistors throughout the Knight platform, but the connector pinout, probe length, and seal vary by sensor location (stack vs. supply vs. return vs. DHW). Always order by Lochinvar part number, not generic NTC 10K — the probe must seat correctly in its well or it will read wrong.

## When to call a professional

**Repeated E02 after verifying flow and thermistors.** If you've confirmed proper flow (Lochinvar specifies 7-15 GPM on WHN-150 at design ΔT of 30°F), good water chemistry, clean strainer, and known-good thermistors, you're looking at HX fouling or HX failure. HX cleaning or replacement on a Knight is several hours of skilled work — and the warranty register matters if the HX is under 5 years old.

**Knight WBN platform with persistent E02 and visible HX corrosion.** Some WBN-platform HXes had a known design vulnerability to acidic condensate when neutralizers were neglected. Lochinvar has issued service bulletins on specific serial ranges. A pro with Lochinvar warranty access should review serial number against published bulletins.

**Suspected combustion problem causing high stack temp.** If stack temp climbs even with verified flow, the cause may be excess gas input (over-firing) or insufficient combustion air. Combustion analysis is needed: target ~9.0% CO2, <100 ppm CO air-free, O2 around 4-6% on most Knight models firing natural gas. This requires a CCAB or BPI-certified analyzer.

**System glycol issues.** Refilling a glycol system with straight water dilutes freeze protection. A pro should refractometer-test and pH-test before recharging with the correct premixed Lochinvar-approved glycol blend (Cryo-Tek 100/-50 or Dowfrost HD).

## FAQs

**Why does E02 only trip during a high heat call, not on a DHW call?**
Heating calls usually run longer and push the HX harder. If flow is marginal, you'll hit the high limit on heating before DHW (which is usually shorter and uses the DHW heat exchanger and pump differently on combi configurations).

**My Knight runs fine for 3-4 weeks then throws E02 — what's slowly degrading?**
Common pattern is air slowly accumulating in the HX from a microscopic system leak that pulls air on cool-down. The system bleeds water at relief and pulls air at vacuum-prone points. Find the leak (sometimes a weeping circ flange or air vent), fix it, and the E02 stops.

**Can I bypass the high limit temporarily?**
No — the high limit is a CSD-1 safety. Boilers above 200°F supply temp produce hazardous steam flashing potential and exceed the design rating of most hydronic system components. Never bypass.

**What's the difference between the Knight WHN and WBN E02?**
Same code, same cause set, slightly different control hardware. WBN is the older Knight platform (SMART System v1.x), WHN is the current platform (SMART TOUCH 2.0). Diagnostic menus look different but troubleshooting logic is the same.

**Should I add hydronic treatment chemicals?**
Yes, if you don't already have them. Lochinvar approves Fernox F1, Sentinel X100, or similar non-toxic corrosion inhibitors. Dose per manufacturer instructions — typically 1 quart per 25 gallons of system water. Reduces sludge, scale, and air corrosion long-term.

## Related guides

- [Weil-McLain Code 3 — Low Water Cutoff Fix](/posts/weil-mclain-error-code-3)
- [Burnham/U.S. Boiler Fault Code 2 — Ignition Lockout Fix](/posts/burnham-error-code-2)
- [Navien NPE/NCB Code E003 — Ignition Failure Fix](/posts/navien-error-code-e003)
