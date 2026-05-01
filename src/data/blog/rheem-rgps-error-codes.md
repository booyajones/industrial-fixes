---
title: "Rheem RGPS Furnace Error Codes — Flash Code Diagnostic Guide"
description: "Complete guide to Rheem RGPS series furnace error codes and flash sequences, covering pressure switch, ignition, limit, and rollout faults with step-by-step fixes."
pubDatetime: 2026-04-22T22:00:00Z
modDatetime: 2026-04-22T22:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - rheem
  - furnace
---

## Rheem RGPS Furnace Error Codes — What They Mean

The Rheem RGPS is a high-efficiency (96% AFUE) single-stage gas furnace in the Classic Plus series. It uses PVC venting and a condensate management system. Faults are communicated through a diagnostic LED on the control board — viewable through the sight glass on the lower access panel. Flash sequences identify specific fault conditions.

[Jump to Fix](#fix)

## Rheem RGPS Flash Code Reference

| Flash Code | Meaning |
|------------|---------|
| 2 flashes | Lockout — failed ignition (3 attempts) |
| 3 flashes | Pressure switch fault |
| 4 flashes | Open high-limit switch |
| 5 flashes | Flame sensed — gas valve not energized |
| 6 flashes | Rollout switch open |
| 7 flashes | Limit cycle lockout (excessive trips) |
| 8 flashes | Low flame signal / dirty flame sensor |
| 9 flashes | Reversed AC power polarity |
| 10 flashes | Low-fire pressure switch fault (two-stage) |
| 11 flashes | Auxiliary limit or secondary limit fault |
| 12 flashes | Gas valve relay fault |
| 13 flashes | Inducer failed to reach speed |

## Common Causes by Code

- **Code 2 — Ignition lockout** — Rheem RGPS uses a hot surface ignitor (HSI) that can crack from thermal cycling. Inspect the ignitor without touching it. Also check gas pressure — many RGPS lockouts result from low gas pressure on cold days when demand is high.
- **Code 3 — Pressure switch** — The RGPS has a PVC secondary heat exchanger that drains condensate continuously during operation. Pressure switch faults frequently trace to a plugged condensate drain trap or drain line, causing condensate to back up into the secondary heat exchanger and alter inducer backpressure.
- **Code 4 — High limit** — Check the main filter and all supply registers. The RGPS requires minimum 350 CFM per ton of cooling capacity — undersized ductwork is a common installation fault that causes repeated limit trips.
- **Code 6 — Rollout** — Rollout switches on the RGPS are mounted on the burner manifold. Manual reset required. Causes: cracked primary heat exchanger, excess gas pressure, blocked burner ports.
- **Code 11 — Auxiliary limit** — The RGPS has an additional limit switch on the secondary heat exchanger. This switch trips when the secondary heat exchanger overheats — usually from condensate backup or restricted secondary airflow.
- **Code 13 — Inducer RPM** — The RGPS control board monitors inducer speed. A worn inducer motor bearing or a clogged inducer wheel (common in dusty environments) causes this code.

## Step-by-Step Fix {#fix}

1. **Identify the flash code** — Observe the LED pattern through the lower door sight glass. Record all flashes; some codes require counting to 13.
2. **For Code 2** — Listen during the ignition trial (you'll hear the gas valve click). If the ignitor glows but no flame, check gas supply pressure at the valve inlet (should be 3.5–7" W.C. for natural gas). If no glow, test ignitor continuity.
3. **For Code 3** — Clear the condensate drain. The RGPS condensate trap is inside the cabinet; access by removing the lower access panel. Flush with water to confirm flow. Also check the exterior drain termination (where the PVC exits the house) for freezing in cold weather.
4. **For Code 4 and 7** — Change the filter. Check all supply vents for furniture or rug blockage. If the furnace short-cycles (shuts off after 2 minutes), the limit is tripping on every call — airflow is severely restricted.
5. **For Code 6** — Locate rollout switches on the burner bracket. Check continuity. If tripped, inspect the heat exchanger before resetting. Look for orange or sooty deposits around the burner opening.
6. **For Code 13** — Remove the blower wheel cover and inspect the inducer wheel for lint or debris. Spin the wheel by hand — it should rotate freely without dragging.
7. **Reset** — Cycle the disconnect switch off for 60 seconds, then restore power and set thermostat to heat.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hot surface ignitor | [Amazon](https://www.amazon.com/dp/B00BTLLJ40?tag=errorcodefixes-20) \| 120V silicon nitride; Rheem-specific part |
| Condensate trap | [Amazon](https://www.amazon.com/dp/B077J4Y763?tag=errorcodefixes-20) \| Inside cabinet; replace if cracked or heavily scaled |
| Pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?tag=errorcodefixes-20) \| Two on two-stage RGPS; confirm part numbers |
| Flame sensor | [Amazon](https://www.amazon.com/dp/B0CZ7M9V4D?tag=errorcodefixes-20) \| Clean first; replace if damaged |
| Inducer motor assembly | [Amazon](https://www.amazon.com/dp/B00FDZ90B2?tag=errorcodefixes-20) \| With mounting plate; common on older RGPS |
| Auxiliary limit switch | [Amazon](https://www.amazon.com/dp/B0BN3TRG9R?tag=errorcodefixes-20) \| Located on secondary heat exchanger |
## When to Call a Pro

A cracked primary or secondary heat exchanger is a carbon monoxide risk. If the rollout switch trips, do not reset more than once without professional heat exchanger inspection. Also, any smell of gas near the furnace requires immediate shutdown, evacuation, and a call to your gas utility.

## Related Articles

- [Rheem Classic Series Furnace Error Codes — Complete Guide](/posts/rheem-classic-furnace-error-codes/)
- [Rheem Air Handler E1 Error Code — Causes & Fix](/posts/rheem-error-code-e1/)
- [Rheem Furnace 2 Flashes — Pressure Switch Fault](/posts/rheem-furnace-2-flashes/)
- [Rheem Furnace 3 Flashes Error Code — Causes & Fix](/posts/rheem-furnace-3-flashes/)
- [Rheem Furnace 4 Flashes — Open High Temperature Limit Fix](/posts/rheem-furnace-4-flashes/)
