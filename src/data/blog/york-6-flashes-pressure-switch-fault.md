---
title: "York Furnace 6 Flashes Error Code — Pressure Switch Fault Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-15T08:00:00Z
modDatetime: 2024-03-15T08:00:00Z
slug: york-6-flashes-pressure-switch-fault
featured: false
draft: false
tags:
  - hvac
  - york
  - furnace
  - pressure-switch
description: "York furnace 6 flashes error code indicates an inducer pressure switch fault — here's how to diagnose and fix it on York, Coleman, and Luxaire furnaces."
---

## Error Code: York Furnace 6 Flashes

**What it means:** Six LED flashes on a York, Coleman, or Luxaire furnace indicate an inducer pressure switch fault. The control board energized the draft inducer motor, waited for the pressure switch to close (confirming adequate negative pressure in the heat exchanger), and the switch never closed — or it closed and reopened during operation. After timing out, the board locks out and repeats the 6-flash sequence.

York, Coleman, and Luxaire are all manufactured by Johnson Controls and share the same control platform, so this diagnostic applies to all three brands.

## Common Causes

- **Clogged condensate drain line** — On 90%+ efficiency furnaces, blocked condensate drainage causes water to back up into the pressure switch tubing, holding the switch open. This is the single most common cause of a York 6-flash fault.
- **Failed or stuck pressure switch** — The switch diaphragm cracks or the contacts corrode, preventing closure even with adequate inducer suction.
- **Weak or failed inducer motor** — If the inducer isn't spinning fast enough, it won't generate sufficient negative pressure to trip the switch. A motor drawing high amperage or running slowly is near end of life.
- **Cracked or disconnected pressure switch hose** — The small rubber or silicone tubing that runs from the inducer housing to the pressure switch can crack, kink, or pull loose, breaking the vacuum signal.
- **Blocked flue or intake** — A bird nest, ice, or debris in the PVC flue or intake pipe restricts airflow, preventing the inducer from building adequate pressure drop.

## Step-by-Step Fix {#step-by-step-fix}

1. **Power down the furnace.** Set the thermostat to OFF and turn off the furnace disconnect switch. Wait 60 seconds before opening the cabinet.

2. **Locate the pressure switch.** On most York 80% units, there is one pressure switch mounted near the inducer assembly. On 90%+ (condensing) units, there are typically two switches — one for the inducer and one for the secondary heat exchanger. The 6-flash code typically points to the primary inducer switch.

3. **Inspect the pressure switch hose.** Trace the small diameter rubber tubing from the inducer housing port to the switch fitting. Look for kinks, cracks, or disconnected ends. Blow gently through the hose to confirm it's clear. Replace with matching ID silicone tubing if cracked.

4. **Check for water in the hose.** On a 90%+ unit, tip the hose downward — water may drain out. If water is present, the condensate drain is blocked. Clear the drain trap and drain line (usually a 3/4" PVC line running to a floor drain or condensate pump). On York units, the drain trap is often serviceable by removing a single screw cap.

5. **Test the pressure switch with a multimeter.** Set to continuity or resistance. With the furnace off and hose disconnected, the switch should read OPEN (no continuity). Gently apply suction to the switch port with a hand vacuum pump or by mouth — the switch should click closed (continuity) at the rated trip point (typically –0.50 to –1.20" W.C. depending on model). If it won't close or stays closed, the switch is failed.

6. **Inspect the inducer motor.** Restore power temporarily and watch the inducer spin up. Listen for grinding, squealing, or sluggish startup. Measure amperage with a clamp meter — compare to the motor nameplate. An inducer running hot or drawing over nameplate amps is failing.

7. **Check the flue pipe.** Walk outside and visually inspect the PVC termination. Look for blockages, ice buildup, or debris. On two-pipe systems, verify both the intake and exhaust pipes are clear.

8. **Replace the pressure switch if faulty.** The OEM York replacement for most mid-range units is part **025-27766-000** (~$35). Always verify the part number against the wiring diagram inside your furnace's cabinet door — York uses multiple switch ratings across its product line.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Part Number | Typical Cost | [Where to Buy](https://www.amazon.com/s?k=Where%20to%20Buy&tag=errorcodefixe-20) |  |------|------------|-------------|-------------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | York Pressure Switch (primary) | 025-27766-000 | [$30–$45](https://www.amazon.com/s?k=%2430%E2%80%93%2445&tag=errorcodefixe-20) | Repair Clinic / Amazon |
| [Inducer Draft Motor (if failed)](https://www.amazon.com/s?k=Inducer%20Draft%20Motor%20(if%20failed)&tag=errorcodefixe-20) | S1-32435820000 | $180–$280 | [Repair Clinic / HVAC distributor](https://www.amazon.com/s?k=Repair%20Clinic%20%2F%20HVAC%20distributor&tag=errorcodefixe-20) |  | Pressure Switch Tubing (bulk) | [Generic 3/16" ID silicone](https://www.amazon.com/s?k=Generic%203%2F16%22%20ID%20silicone&tag=errorcodefixe-20) | $5–$10 | Amazon / hardware store | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Condensate Drain Trap | S1-37327820000 | [$18–$30](https://www.amazon.com/s?k=%2418%E2%80%93%2430&tag=errorcodefixe-20) | Repair Clinic |

## When to Call a Professional

If the flue or intake is blocked with ice, do not attempt to run the furnace. On cold days, ice can reblock a cleared line within hours — the root cause is usually flue pipe that runs too horizontally, is too close to the ground, or has inadequate slope. Correcting the flue routing requires a licensed HVAC contractor. Similarly, if the inducer motor has failed, replacement on a York 90%+ unit involves removing the secondary heat exchanger in some configurations — a job that requires experience to avoid damaging the plastic heat exchanger. A cracked or failed secondary heat exchanger is a carbon monoxide risk and must be confirmed clear before returning the unit to service.

> **Pro tip:** York furnaces with a 6-flash fault that clears on its own during warm weather and returns every winter almost always have a condensate freeze problem. The fix is adding freeze protection to the condensate line or rerouting it away from exterior walls — not replacing parts.
