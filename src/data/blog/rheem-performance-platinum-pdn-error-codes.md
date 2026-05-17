---
title: "Rheem Performance Platinum PDN Tankless Error Codes — Complete Fix Guide"
description: "Rheem Performance Platinum PDN tankless water heater error codes. Covers codes 10, 11, 12, 13, 14, 29, P1, and combustion/venting faults with step-by-step diagnosis."
pubDatetime: 2026-05-17T19:35:00Z
modDatetime: 2026-05-17T19:35:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - rheem
  - tankless
  - water-heater
  - plumbing
---
<!-- VOICE-GUARD-OFF -->

## Rheem Performance Platinum PDN — Error Code Reference

The Rheem Performance Platinum PDN series (gas tankless, condensing) shares the same controller family as Rheem RTGH and Ruud equivalents. Error codes appear as a one- or two-digit number on the front panel with a flashing red LED. The codes below are the ones you'll actually see in the field, in rough order of frequency.

| Code | Fault | Most Likely Cause | First Action |
|------|-------|-------------------|--------------|
| 10 | Air-supply / combustion-air blockage | Vent intake plugged, restricted, or birdcage missing | Inspect intake vent termination outside |
| 11 | No ignition | Gas off, propane out, igniter wire loose | Verify gas pressure at inlet |
| 12 | Flame failure mid-burn | Dirty flame rod, condensate flooding burner | Pull and clean flame rod |
| 13 | Combustion-air pressure switch fault | Vent fan stalled, condensate in vent | Listen for fan, drain vent |
| 14 | Thermal fuse / over-temperature lockout | Scaled heat exchanger, fan failure | Flush heat exchanger |
| 29 | Condensate drain blocked | Drain line clogged, neutralizer cartridge full | Clear drain, replace neutralizer |
| P1 | Pump fault (recirc-capable units only) | Recirc pump failed or wiring open | Test pump leads, replace pump |
| 90 | Internal communication fault | Main board to remote control link broken | Re-seat ribbon cable, replace board |

## Code 12 — Flame Failure Mid-Burn (Most Common)

Code 12 is the #1 callback on PDN units. The unit lights, runs for 5-30 seconds, then drops out and re-tries. After 3 failed cycles it locks out with code 12.

### The two real causes

1. **Dirty flame rod (~70% of code 12 calls).** The flame rod sits in the burner flame and measures flame ionization. A film of carbon or scale on the rod drops the ionization signal below the threshold, so the board thinks the flame went out. Pull the rod, wipe it with fine emery cloth, re-seat. Five-minute fix.
2. **Condensate pooling in the burner chamber.** PDN units are condensing — they generate liquid water as part of normal operation. If the condensate drain is partially blocked, water backs up into the burner area and quenches the flame. Pull the bottom drain plug; if water gushes, your drain is the problem (jump to code 29).

If the flame rod is clean and the chamber is dry, the next suspects are gas pressure (verify 6-14 inWC dynamic at the inlet) and the gas valve itself.

## Code 10 — Air Supply / Combustion-Air Blockage

The PDN measures air pressure across the vent fan and intake. Code 10 means it can't draw enough combustion air. Two common physical causes:

- **Vent intake termination plugged outside.** Wasps, leaves, or a broken vent screen blocks the 2-3 in PVC intake. Inspect the termination first — most installs are wall- or roof-vent.
- **Long vent run with too many elbows.** Each elbow counts as several equivalent feet of vent. If the install exceeds the manual's max equivalent length, code 10 fires intermittently during high-fire calls.

A failed intake-air thermistor will also throw code 10 but is less common than the physical-blockage causes.

## Code 13 — Combustion-Air Pressure Switch Fault

Code 13 is closely related to code 10 — the air pressure switch sees no pressure difference across the vent fan during a call for heat. Check the fan first (listen for it during startup; it should spin up within 2 seconds of a call). If the fan is dead, replace it. If the fan runs but the switch still doesn't make, the pressure tubing between the fan and the switch is disconnected or clogged with condensate.

## Code 14 — Thermal Fuse / Over-Temperature Lockout

The unit detected an outlet temperature above safe limits. On PDN units this is almost always **scaled heat exchanger**. Hard water in residential service deposits calcium on the heat exchanger over 3-5 years; the scale insulates the exchanger from the water and the burner overheats the surface.

Fix: descale with a tankless-water-heater service kit and CLR or equivalent (5-gal bucket, submersible pump, hoses, 4 gal of descaler). 45-minute service. Annually if you're on hard water.

## Code 29 — Condensate Drain Blocked

The condensate neutralizer cartridge or drain line is plugged. On the PDN, the condensate exits the bottom of the burner chamber, through a small neutralizer (a tube of limestone or magnesium chips that neutralizes the acidic condensate), then to drain. Symptoms before code 29 fires: visible water around the unit base.

Fix:
1. Disconnect the drain line at the unit and confirm flow when you pour water in the top.
2. If no flow, the neutralizer is plugged — pull it, dump and refill, or replace the cartridge.
3. Check the drain line slope. Code 29 also fires from low spots that trap condensate.

## Parts That May Need Replacement {#parts}

| Part | Where to Buy | Typical Cost |
|------|--------------|--------------|
| Flame rod (Rheem AS39717) | [Check price on Amazon](https://www.amazon.com/s?i=industrial&k="AS39717"+Rheem+flame+rod&tag=errorcodefixes-20) \| Rheem parts | $30-$60 |
| Combustion fan motor | [Check price on Amazon](https://www.amazon.com/s?i=industrial&k=Rheem+tankless+combustion+fan&tag=errorcodefixes-20) \| supply house | $180-$320 |
| Air pressure switch | [Check price on Amazon](https://www.amazon.com/s?i=industrial&k=Rheem+tankless+air+pressure+switch&tag=errorcodefixes-20) | $40-$90 |
| Tankless descale kit (pump + hoses + descaler) | [Check price on Amazon](https://www.amazon.com/s?i=industrial&k="tankless+water+heater+flush+kit"&tag=errorcodefixes-20) | $90-$160 |
| Condensate neutralizer cartridge | [Check price on Amazon](https://www.amazon.com/s?i=industrial&k="condensate+neutralizer"+tankless&tag=errorcodefixes-20) | $35-$70 |
| Gas valve assembly | Rheem dealer | $280-$450 |

## Technician Tips

- **Descale every year on city water, every 6 months on well water.** This single maintenance item prevents about 60% of PDN service calls.
- The PDN's display only shows the most recent code. To pull alarm history, hold the front-panel "+" and "-" buttons together for 3 seconds — the last 5 codes scroll.
- Code 12 that returns within 24 hours of a flame-rod cleaning means the rod is bent or wrong distance from the burner — the rod tip should be 4-6 mm from the flame center. Replace, don't bend.
- For chronic code 13 / 14 issues on installs done before ~2020, check the vent type. Some early PDN units were installed with PVC; current code requires CPVC or Polypropylene for the flue. PVC softens at high-fire and creates flow restrictions.

## Need Help Finding Parts?

If you're not sure which OEM part number fits your specific PDN model, pull the rating-plate label (rear of unit, behind the cover) and look for the model number — it starts with "PDN" followed by the BTU rating and a revision letter. Rheem's parts portal and most supply houses will cross-reference from there.
