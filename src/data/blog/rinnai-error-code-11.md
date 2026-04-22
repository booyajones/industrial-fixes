---
title: "Rinnai Error Code 11 — No Ignition Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-04-09T08:00:00Z
modDatetime: 2024-04-09T08:00:00Z
slug: rinnai-error-code-11
featured: false
draft: false
tags:
  - boiler
  - rinnai
  - tankless
  - ignition
description: "Rinnai error code 11 means the tankless water heater failed to ignite. This guide covers every cause and fix for the Rinnai Code 11 ignition failure."
---

## Error Code: Rinnai 11

**What it means:** Rinnai error code 11 indicates an ignition failure — the unit attempted to light the burner but could not establish a confirmed flame within the ignition trial period. Rinnai tankless water heaters (V-series, RU-series, RUC-series) attempt 3 ignition trials; if all fail, the unit locks out with Code 11 displayed on the controller. The unit must be reset by pressing the On/Off button or cycling power. Code 11 can be caused by gas supply issues, igniter problems, or sensing circuit failures.

## Common Causes

- **Gas supply not open or air in line** — The most common cause on new installations or after any gas interruption. The manual shutoff valve must be fully open. Air purging requires multiple reset attempts.
- **Low gas pressure** — Rinnai requires 3.5" W.C. minimum inlet pressure for natural gas (8.0" W.C. for propane). Pressure drops from shared gas runs or undersized meter cause Code 11.
- **Dirty or failed flame sensor** — Rinnai uses a flame rod sensor. A contaminated rod does not pass adequate microamps to confirm flame, causing the board to cut gas and log Code 11.
- **Spark igniter failure** — Carbon-fouled spark electrodes or a cracked ceramic insulator prevent reliable ignition spark.
- **Blocked or disconnected vent** — A blocked exhaust vent causes the unit to detect exhaust backpressure and prevent ignition. Common on horizontal vents that develop ice blockages in cold climates.
- **Water flow below minimum** — Rinnai requires minimum 0.5–0.75 GPM flow to activate. A low-flow fixture or partially closed shutoff may not activate the unit, which presents as ignition failure if the burner never fires.

## Diagnosis Steps

1. Check water flow: open a hot water tap fully. The unit should activate (hear the gas valve and igniter). If nothing activates, the flow is below the activation threshold — check for partially closed isolation valves.
2. Verify gas supply: confirm the manual gas shutoff is open. Check other gas appliances. For a new installation, attempt 5–8 reset cycles to purge air from the line.
3. Inspect the venting: for horizontal PVC-vented units, look at the exterior termination cap. Verify it is not blocked with ice, debris, or bird nests. Check the concentric vent pipe for disconnected joints.
4. Access the combustion chamber (power off and gas closed): inspect the spark electrode. The electrode tip should be free of carbon and positioned approximately 3–4mm from the ground plate. Clean or adjust as needed.
5. Inspect the flame sensor rod. Clean with 320-grit sandpaper or steel wool. The rod should be bright metal, not coated with white or brownish deposits.

## Fix

For air-in-line: reset and retry 5–10 times over 15 minutes. Gas will eventually purge through. On propane systems, also verify the tank has adequate fuel — propane regulators can freeze up in very cold weather, restricting flow.

For a dirty spark electrode: clean the tip with fine sandpaper, verify the 3–4mm gap is maintained. For a dirty flame sensor: clean the rod. If the rod is corroded through or the ceramic insulator is cracked, replace the igniter/sensor assembly.

For blocked venting: clear the blockage and restore unrestricted airflow. If the vent termination cap has failed (warped, corroded), replace it with a Rinnai-approved termination kit.

Low gas pressure requires a licensed gas plumber to inspect the supply system and meter capacity.

## Parts

| Part | Where to Buy |
|------|-------------|
| Rinnai igniter / flame sensor assembly | RepairClinic, SupplyHouse |
| Vent termination cap / kit | SupplyHouse, Amazon |
| Isolation valve (ball valve) | Grainger, Amazon |

## When to Call a Technician

If Code 11 persists after purging air, cleaning the igniter, and checking venting, a licensed plumber or gas technician should inspect the gas supply pressure and valve operation. Rinnai gas valve replacement must be performed by a licensed technician — the gas valve is interlocked with pressure switches and the PCB in ways that require proper testing equipment to verify after replacement.
