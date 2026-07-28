---
title: "Hoshizaki Ice Machine E9 Error Code — Compressor Overload Fault Fix"
author: "James Rutherford"
pubDatetime: 2026-04-26T17:00:00Z
modDatetime: 2026-04-26T17:00:00Z
slug: hoshizaki-e9-error-compressor
featured: false
draft: false
tags:
  - ice-machine
  - hoshizaki
  - commercial-refrigeration
  - compressor
description: "Hoshizaki ice machine E9 error code means compressor overload or thermal cutout. Learn the causes, how to diagnose the compressor and start relay, and when to call a tech."
---

## Error Code: Hoshizaki Ice Machine E9

**What it means:** The E9 error code on Hoshizaki commercial ice machines indicates that the compressor has overloaded or tripped its internal thermal cutout. Hoshizaki's control board monitors the compressor circuit and, when it detects abnormally high current draw or loss of the compressor signal, it shuts down the machine and displays E9 to prevent catastrophic compressor failure.

Hoshizaki is one of the leading commercial ice machine brands in North America, found in restaurants, hotels, hospitals, and convenience stores. An E9 fault in a commercial kitchen is a serious, time-sensitive problem — no ice machine means immediate operational impact. Understanding the cause quickly is critical.

**Important:** E9 is a high-severity fault. The compressor is the most expensive single component in the machine (often $500–$1,500+ in parts alone). Before assuming the compressor has failed, always verify the start relay and capacitor first — these are far cheaper and are common failure points.

## Common Causes

- **Failed start relay or start capacitor** — The start relay or capacitor assists the compressor through startup. A failed relay is the most common non-compressor cause of E9 and costs under $30 to replace.
- **Compressor motor winding failure** — One or more motor windings have shorted or opened, preventing the compressor from starting or running. This typically requires compressor replacement.
- **High head pressure / refrigerant overcharge** — Excessively high discharge pressure forces the compressor to work harder than its thermal overload allows, tripping the cutout.
- **Restricted refrigerant circuit** — A blocked expansion valve or refrigerant restriction causes abnormal pressure conditions that overwork the compressor.
- **Dirty condenser coil (air-cooled models)** — A clogged condenser forces the compressor to run against elevated head pressure. This is the most preventable cause of E9.
- **Inadequate ventilation around the unit** — Insufficient clearance or high ambient temperature (above 100°F / 38°C) pushes the compressor beyond its design limits.

## Step-by-Step Diagnosis {#step-by-step-fix}

1. **Let the machine cool down.** Disconnect power and wait 30–45 minutes. The compressor's internal thermal overload may have tripped from overheating. After cooling, restore power and attempt a restart. If the machine runs normally, suspect a heat or ventilation issue. If E9 returns within one freeze cycle, continue diagnosis.

2. **Inspect and clean the condenser coil.** On air-cooled models, the condenser is either on the top or the rear of the machine. Use a coil brush and compressed air (or a vacuum) to remove debris from between the fins. Even moderate fouling can cause E9 during warm weather.

3. **Verify clearances.** Hoshizaki specifies minimum clearances on all sides and the top. Check the installation manual for your model. A unit pushed against a wall or in an undercounter cavity with no airflow will recirculate hot air directly into the condenser.

4. **Test the start relay.** Disconnect power. Locate the compressor terminal cover on the compressor body. Remove the relay (it simply plugs onto the compressor terminals). Shake it — a rattling sound indicates internal failure. Test continuity with a multimeter between the two terminal pins: should read near 0 Ω (closed). Replace if open or rattling.

5. **Test the run capacitor.** Use a capacitor meter to test the capacitor's actual microfarad reading versus the stamped rating. A reading 20% or more below rated value means the capacitor needs replacement.

6. **Test compressor motor windings.** With power off, disconnect all wires from the compressor terminals (labeled C, S, R for common, start, run). Measure resistance between each pair:
   - C to S: should read a specific value (check service manual)
   - C to R: should read a specific value
   - S to R: should equal approximately C-S + C-R
   - Any terminal to ground: must read OL (open) — a reading to ground confirms a shorted winding = compressor failure

7. **Check refrigerant pressures (technician step).** If wiring and electrical components check out, a technician should connect gauges to assess high-side and low-side pressures during operation, looking for overcharge or restriction.

## How to Fix It

- **Dirty condenser:** Clean thoroughly. Many E9 events in summer months are resolved by cleaning alone.
- **Failed start relay:** Replace with an exact OEM match for your Hoshizaki model. This is a DIY-friendly repair.
- **Failed capacitor:** Replace with exact µF-rated match.
- **Failed compressor:** Requires a certified HVAC/R technician. Compressor replacement involves recovering refrigerant, brazing, evacuating, and recharging the system. On older machines, compare repair cost to machine replacement cost.

## Parts You May Need

- [Hoshizaki Compressor Start Relay Replacement](https://www.amazon.com/s?ascsubtag=ecf-hoshizaki-e9-error-compressor&k=Hoshizaki+ice+machine+compressor+start+relay&tag=errorcodefixes-20)
- [Hoshizaki Run Capacitor Ice Machine](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-hoshizaki-e9-error-compressor&tag=errorcodefixes-20)
- [Commercial Ice Machine Condenser Coil Cleaner](https://www.amazon.com/s?ascsubtag=ecf-hoshizaki-e9-error-compressor&k=commercial+ice+machine+condenser+coil+cleaner&tag=errorcodefixes-20)
- [Refrigeration Compressor Multimeter Test Kit](https://www.amazon.com/dp/B08ZJSN5X3?ascsubtag=ecf-hoshizaki-e9-error-compressor&tag=errorcodefixes-20)
- [Capacitor Meter HVAC](https://www.amazon.com/s?ascsubtag=ecf-hoshizaki-e9-error-compressor&k=capacitor+meter+HVAC+refrigeration&tag=errorcodefixes-20)

## When to Call a Technician

Any diagnosis involving refrigerant pressures requires EPA 608 certification and manifold gauges. Compressor replacement requires brazing, evacuation, and refrigerant handling — all technician-required tasks. If the compressor winding test shows a short to ground or open circuit between motor windings, the compressor has failed and must be replaced by a certified refrigeration technician. Do not attempt to restart a compressor with a known winding failure — it will draw locked-rotor amperage, potentially damaging wiring and the control board.

## Related Error Codes

- [Hoshizaki E7 Error Code — High-Side Pressure Switch Fault](/posts/hoshizaki-e7-pressure-switch/)
- [Hoshizaki E8 Error Code — Low-Side Pressure Switch Fault](/posts/hoshizaki-e8-low-side-pressure/)
- [Hoshizaki E1 Error Code — Freeze Cycle Timeout](/posts/hoshizaki-e1-error-code/)
