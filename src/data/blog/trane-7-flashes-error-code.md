---
title: "Trane 7 Flashes Error Code — Gas Valve Circuit Fault Fix"
author: "Marcus Webb"
pubDatetime: 2024-03-26T08:00:00Z
modDatetime: 2024-03-26T08:00:00Z
slug: trane-7-flashes-error-code
featured: false
draft: false
tags:
  - hvac
  - trane
  - furnace
  - gas-valve
description: "Trane 7 flashes means a gas valve circuit fault or ignition lockout after multiple attempts. This guide covers diagnosis and fixes for Trane furnace Code 7."
---

## Error Code: Trane 7 Flashes

**What it means:** Seven flashes on the Trane furnace diagnostic LED indicates a gas valve circuit fault or ignition lockout. The board energizes the gas valve and igniter, waits for flame confirmation from the flame sensor, and if flame is not detected after the allotted ignition trial period, shuts off the gas valve. After three consecutive failed ignition attempts, the board locks out and displays 7 flashes. The furnace will not attempt another ignition until power is cycled or the lockout timer expires (typically 60 minutes).

## Common Causes

- **Dirty or failed flame sensor** — The flame sensor is a metal rod that detects flame via electrical conductance. A layer of oxidation on the sensor rod insulates it, preventing proper flame signal. This is the most common cause of repeated ignition failure.
- **Weak or failed hot surface igniter** — The igniter must reach 1800–2000°F to ignite gas. A cracked or weakened igniter may glow dimly but fail to ignite gas consistently.
- **No gas supply or insufficient gas pressure** — A closed manual gas shutoff, a tripped meter, or low inlet pressure will prevent ignition regardless of igniter and sensor condition.
- **Failed gas valve** — A gas valve that receives the signal but does not open will cause repeated ignition failure. Confirm 24V AC is present at the valve terminals during ignition trial before condemning the valve.
- **Cracked igniter** — A hairline crack in the igniter can cause intermittent failure — the igniter glows but breaks the circuit under thermal stress.

## Diagnosis Steps

1. Cycle power to reset the lockout. Watch the ignition sequence: inducer starts → pressure switch closes → igniter glows → gas valve opens → burner lights. Identify where the sequence stops.
2. Remove the flame sensor rod (usually a single screw mount near the burner). Inspect the rod — it should be shiny metal. If it has a white, gray, or brownish coating, clean it with fine steel wool or emery cloth. Reinstall and test.
3. With the furnace in ignition trial, observe the hot surface igniter through the sight glass (or with furnace door cracked). It should glow bright orange-white within 30–45 seconds. A dull red or no glow indicates igniter failure.
4. With a multimeter, check the igniter resistance at room temperature (typically 40–90 ohms for silicon nitride igniters). An OL (open) reading means the igniter is cracked and must be replaced.
5. Confirm gas supply: check that the manual shutoff valve on the gas line to the furnace is fully open (handle parallel to pipe = open). If other gas appliances in the home are working, the supply is fine.

## Fix

Clean the flame sensor first — it takes 5 minutes and resolves this fault in the majority of cases. If cleaning doesn't help, replace the sensor ($15–25 part).

If the igniter is dim or measures OL resistance, replace it. Handle igniters only by the ceramic base — skin oils on the rod reduce life significantly. Match the igniter by furnace model number, not just voltage — Trane uses both 80V and 120V igniters depending on model.

If the gas valve is not opening (no gas smell, no ignition) but the igniter glows correctly, measure 24V AC at the gas valve operator terminals during ignition trial. If voltage is present but no gas flows, the valve has failed internally and must be replaced by a licensed tech.

## Parts

| Part | Where to Buy |
|------|-------------|
| [Flame sensor](https://www.amazon.com/s?k=Flame+sensor&tag=errorcodefixes-20) | RepairClinic, Amazon |
| [Hot surface igniter (match model)](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-trane-7-flashes-error-code&tag=errorcodefixes-20) | RepairClinic, SupplyHouse |
| [Gas valve](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-trane-7-flashes-error-code&tag=errorcodefixes-20) | SupplyHouse, Grainger |
| [Control board](https://www.amazon.com/s?k=Control+board&tag=errorcodefixes-20) | RepairClinic, Grainger |

## When to Call a Technician

Gas valve replacement and gas pressure adjustment require a licensed HVAC technician. Flame sensor cleaning and igniter replacement are appropriate for a confident DIYer comfortable with basic HVAC service.

## Related Articles

- [Trane 1 Flash Error Code — Causes & Fix](/posts/trane-1-flash-error-code/)
- [Trane Error Code 126 — Ignition Lockout Fix](/posts/trane-126-error-code/)
- [Trane 2 Flashes Error Code — Causes & Fix](/posts/trane-2-flashes-error-code/)
- [Trane 3 Flashes Error Code — Pressure Switch Fault Fix](/posts/trane-3-flashes-error-code/)
- [Trane 3 Flash Pressure Switch Fault — Detailed Diagnosis Guide](/posts/trane-3-flashes-pressure-switch/)

## See Also

- [Trane AC E2 Error Code — Sensor and Communication Fault Fix](/posts/trane-e2-ac-sensor-fault/)
- [Trane 8 Flashes Error Code — Causes & Fix](/posts/trane-8-flashes-error-code/)
- [Trane XV20i Error Code 79: Communicating Thermostat Fault Fix](/posts/trane-error-79-xv20i/)
- [Trane 1 Flash Error Code — Causes & Fix](/posts/trane-1-flash-error-code/)
