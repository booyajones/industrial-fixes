---
title: "Champion UH130 Error Code — Fill Cycle Fault Fix"
description: "A Champion UH130 fill-cycle fault means the wash tank didn't reach proper water level in the timeout window — typically a clogged fill valve inlet screen, a..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Marcus Webb"
slug: champion-uh130-error-code
featured: false
draft: false
tags:
  - champion
  - fill-cycle-failure-no-fill
  - troubleshooting
---
## Quick answer

A Champion UH130 fill-cycle fault means the wash tank didn't reach proper water level in the timeout window — typically a clogged fill valve inlet screen, a stuck low-water probe (the UH130 uses conductivity probes, not a float), or scale on the probe surfaces. Don't replace the control board until you've cleaned the probes and verified the fill solenoid valve.

## What the fill-cycle fault means on a Champion UH130

The Champion UH130 is an undercounter high-temperature dishwasher used in cafes, small restaurants, and break-room installations. Unlike float-switch machines like the Jackson Conserver, the UH130 uses **conductivity probes** to detect water level in the wash tank — two stainless rods of different lengths that report water-at-level by completing a circuit through the water itself. The shorter "high level" probe sits at fill-complete height; the longer "low level" probe sits near the tank bottom and detects when water has drained.

The fill fault (sometimes shown as "FILL" or "F1" on the LED display depending on UH130 sub-model and firmware revision) triggers when the controller energizes the fill solenoid valve and doesn't see the high-level probe report water-at-level within the timeout — typically 5-7 minutes on most UH130 revs. The board kills the fill output, displays the fault, and disables wash to protect the pump from dry-running.

Conductivity probes have a specific failure mode that's foreign to float-switch techs: **mineral scale and grease deposits insulate the probe surface**, so the probe doesn't see continuity through the water even though water has reached the probe tip. The unit can have a tank visibly filled with water and still throw the fill fault if the high-level probe is coated. Cleaning the probes is step one on any UH130 fill fault.

Other causes parallel the standard fill-fault list: clogged solenoid inlet screen, low water pressure, failed solenoid coil, failed control board input. But probes come first because that's where 60% of these failures live.

## Common causes (ranked by frequency)

1. **Scaled or grease-coated water level probes** — most common UH130 issue. Probes need quarterly to monthly cleaning depending on water hardness.
2. **Clogged fill solenoid inlet screen** — sediment from building supply, especially after building plumbing work.
3. **Low water supply pressure** — UH130 spec is 20-90 PSI flowing; below 20 won't fill in time.
4. **Failed fill solenoid valve coil** — coil open or shorted, valve won't open when energized.
5. **Failed probe sensing input on the control board** — board doesn't see the probe signal even when water is at level. Less common than probe scaling.
6. **Broken or kinked supply hose** — typically braided stainless flex on UH130 installations. Internal kink restricts flow.
7. **Drain solenoid stuck open** — water enters but drains simultaneously, never reaches level. Listen for drain sound during fill.

## Step-by-step fix

1. **Power down the UH130 at the disconnect.** Lockout-tagout. UH130 is typically 120 V single-phase, but the heater element circuit may be 208/240 V depending on configuration.

2. **Verify water supply pressure.** Connect a pressure gauge at the supply hose connection. Champion spec is 20-90 PSI flowing. Below 20 PSI causes fill faults. Above 90 risks valve damage. Building supply valves under sinks are often partially closed by accident — check that the angle stop is fully open.

3. **Drain the wash tank.** Open the door, pull the rack, lift wash arms. Drain manually using the drain lever. Pull the strainer baskets and inspect for debris.

4. **Inspect and clean the water level probes.** This is the single highest-yield diagnostic step. The probes sit at the back of the wash tank, typically mounted through a stainless block on the rear wall. There are two: a short probe (high level / fill complete) and a long probe (low level / dry-fire protection). Pull the probes by unscrewing the retaining nut, inspect the tips. You'll likely see white mineral scale or a slimy grease/food deposit coating the stainless. Clean with a green Scotchbrite pad under running water until the metal is bright. For heavy scale, soak in a delimer solution (Champion DelimePlus or equivalent) for 20-30 minutes before scrubbing.

5. **Inspect and clean the fill solenoid inlet screen.** Disconnect the supply hose at the fill valve inlet. Pull the inlet screen (typically a 40-60 mesh stainless screen at the valve port). Sediment, scale, and pipe-dope debris will clog it. Clean or replace.

6. **Test the fill solenoid valve coil electrically.** With power restored, command an initial fill (close door, machine should start a fill cycle). Measure voltage at the fill valve coil — should be 120 VAC. With voltage present and valve still closed, coil is failed. Measure coil resistance off-power: typically 1.5-2.5 kΩ on a 120 V coil. Replace if open or shorted.

7. **Verify drain solenoid is closed during fill.** The UH130 drain solenoid should be closed (valve seated, no water flow to drain) during fill. If the drain valve is leaking by — common after years of use — you'll hear water trickling to the drain during fill. Test by capping the drain temporarily (or by removing the drain hose at the trap and watching for flow during fill). A leaking drain valve needs replacement.

8. **Reassemble, restore power, and observe a full fill cycle.** Close the door. The machine should begin fill, water should flow in steadily, level should reach the high probe in 3-4 minutes, and the machine should transition to ready state. If the fill fault returns, recheck probe cleanliness — probes need to be bright stainless on the tip, not just clean-looking. Also recheck probe wire continuity: with probes removed and wires disconnected, measure resistance from probe wire end to the controller's probe input pin. Should be a short (under 1 Ω). Open wire indicates broken conductor inside the wiring loom.

> **Field knowledge nugget:** On Champion UH130 machines used in coffee shops and cafes that wash a lot of milk-based dishware (latte cups, milk frothing pitchers), I see a specific fill-fault pattern related to milk fat coating the conductivity probes. Milk proteins denature in the wash cycle and coat surfaces, including the probes. Standard delimer doesn't touch protein deposits — you need a *protein-specific* cleaner like an enzymatic cleaner or a high-alkaline degreaser (pH 12-13) to break down the coating. The diagnostic tell: a coffee-shop UH130 throws fill faults more frequently than identical machines in other accounts; probe surfaces look "clean" but have a slightly waxy feel when you run a finger across them. Fix is a 30-minute soak in Champion Pro Pots (or similar high-alkaline detergent at 4x normal concentration), followed by a Scotchbrite scrub. After cleaning, recommend the account add a monthly enzyme deep-clean to their PM schedule. The probe-cleaning kit (Champion 6685-PROBE-XX or similar Champion part numbers in the 6685- family) includes a recommended cleaning protocol — use it as a customer education tool. Coffee accounts that do quarterly probe cleaning rarely throw fill faults.

**Safety:** UH130 machines use commercial dishwasher detergent (high alkalinity, typically pH 12-13) and rinse-aid sanitizer (acidic, often pH 2-3). When servicing the chemical injector lines or pump body, flush all chemical lines with clean water before opening fittings — undiluted chemical can splash into eyes or skin. Wear chemical-resistant gloves and eye protection. The detergent supply often runs from a 5-gallon pail outside the machine; verify the chemical pickup tube is fully out of the pail before disconnecting any line. Reference the chemical manufacturer's MSDS.

## Parts that may need replacement

| Part | OEM Number (typical) | Typical Cost | Where to Buy |
|---|---|---|---|
| Water level probe assembly | Champion 6685-PROBE-XX | $85–$155 | [Parts Town](https://www.partstown.com?aff=PLACEHOLDER-PT) |
| Fill solenoid valve | Champion 0512127 | $145–$245 | [Parts Town](https://www.partstown.com?aff=PLACEHOLDER-PT) |
| Drain solenoid valve | Champion 0512128 | $165–$265 | [Parts Town](https://www.partstown.com?aff=PLACEHOLDER-PT) |
| Solenoid inlet screen | universal 1/2 FPT | $8–$20 | [Parts Town](https://www.partstown.com?aff=PLACEHOLDER-PT) / [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Control board (UH130) | Champion 0511125 | $385–$585 | [Parts Town](https://www.partstown.com?aff=PLACEHOLDER-PT) |
| Probe cleaning kit | Champion delimer + Scotchbrite | $25–$50 | [Parts Town](https://www.partstown.com?aff=PLACEHOLDER-PT) |

Order replacement probes with new sealing washers — the through-tank o-ring on the probe stem doesn't reliably reseat.

## When to call a professional

Call a CFESA-certified commercial dishwasher tech if:

- You've cleaned probes, replaced the fill valve, and verified building supply pressure, and the fill fault still recurs. Board input failure is real but rare.
- The machine is under Champion warranty (typically 1 year parts and labor). Authorized servicer required.
- You suspect a building plumbing issue (intermittent pressure drops, sediment from new construction). Coordinate with the building plumber.
- The chemical injector system needs work — chemical pumps, lines, and check valves are a separate discipline and chemical exposure risk.
- The control board replacement requires firmware-level configuration that the part doesn't include.

## FAQs

**Why does my Champion UH130 throw fill faults more often than my old float-switch dishwasher?**
Conductivity probes are inherently more sensitive to surface contamination than mechanical float switches. They give faster fault detection but require more cleaning maintenance. Build a quarterly probe-cleaning task into the PM schedule.

**Can I just keep cleaning the probes or do I need to replace them?**
Cleaning works until the stainless probe tips are pitted or worn thin. Once you can see visible erosion on the tip, the probe surface area is small enough that contact reliability drops and you'll see intermittent fill faults even after cleaning. At that point, replace.

**Does water hardness affect the UH130 fill fault rate?**
Yes, significantly. Above 7 grains per gallon hardness, expect monthly probe cleaning. Above 15 grains, install a water softener — the UH130's stainless probes, heater element, and pump seal will all benefit.

**My UH130 fills the tank but still shows the fill fault — what's happening?**
That's the classic probe-coating symptom. The water reached the probe, but the probe surface can't see continuity through the water because of insulating deposits. Clean the probes.

**Should I bypass the probes to make the machine run?**
No. The probes are also low-water protection for the wash heater element. Running without working level detection can dry-fire the heater and destroy it (and possibly cause a fire). Fix the probe issue properly.

## Related guides

- [Jackson Conserver Series Error 1 — Low Water Fix](/posts/jackson-conserver-error-1)
- [Hobart AM15 Error 1-1 — Wash Motor Overload Fix](/posts/hobart-am15-error-1-1)
- [Meiko/Ecolab Commercial Dishwasher Error Code Reference](/posts/ecolab-meiko-error-code)
