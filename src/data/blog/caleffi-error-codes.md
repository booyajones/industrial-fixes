---
title: "Caleffi Hydronic System Fault Codes — Complete Guide"
description: "Caleffi hydronic system fault codes for zone valves, mixing valves, electronic controllers, and SEPcal separators: fault indicators, failure modes, and fixes."
pubDatetime: 2026-04-22T19:00:00Z
modDatetime: 2026-04-22T19:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - plumbing
  - caleffi
  - hydronic
---

## Caleffi Hydronic Fault Indicators — Quick Reference

Caleffi manufactures hydronic heating components including zone valves, thermostatic mixing valves, automatic air vents, dirt and magnetic separators (Discaldirt, Dirtmag), and electronic differential pressure controllers. Most Caleffi components are mechanical — faults appear as operational symptoms rather than numeric codes. The Caleffi iSolar and electronic controller products display numeric faults.

| [Device](https://www.amazon.com/s?ascsubtag=ecf-caleffi-error-codes&k=Device&tag=errorcodefixes-20) | Fault Indicator | Meaning | Quick Fix |
|--------|----------------|---------|-----------|
| [Zone Valve (6130, 6150)](https://www.amazon.com/s?ascsubtag=ecf-caleffi-error-codes&k=Zone+Valve+%286130%2C+6150%29&tag=errorcodefixes-20) | No/slow travel | Actuator motor worn | Replace actuator head |
| [Zone Valve](https://www.amazon.com/s?ascsubtag=ecf-caleffi-error-codes&k=Zone+Valve&tag=errorcodefixes-20) | No power — valve stuck | Thermal actuator seized | Replace head; check 24VAC |
| [Mixing Valve (521, 5230)](https://www.amazon.com/s?ascsubtag=ecf-caleffi-error-codes&k=Mixing+Valve+%28521%2C+5230%29&tag=errorcodefixes-20) | Temp too high | Cartridge fouled | Clean or replace cartridge |
| [Mixing Valve](https://www.amazon.com/s?ascsubtag=ecf-caleffi-error-codes&k=Mixing+Valve&tag=errorcodefixes-20) | Temp unstable | Pressure differential too high | Install balancing valve |
| [iSolar controller](https://www.amazon.com/s?ascsubtag=ecf-caleffi-error-codes&k=iSolar+controller&tag=errorcodefixes-20) | E1 | Collector sensor fault | Check sensor wiring; replace sensor |
| [iSolar controller](https://www.amazon.com/s?ascsubtag=ecf-caleffi-error-codes&k=iSolar+controller&tag=errorcodefixes-20) | E2 | Tank sensor fault | Check sensor wiring; replace sensor |
| [iSolar controller](https://www.amazon.com/s?ascsubtag=ecf-caleffi-error-codes&k=iSolar+controller&tag=errorcodefixes-20) | E3 | Overtemperature — collector | Check for stagnation condition |
| [iSolar controller](https://www.amazon.com/s?ascsubtag=ecf-caleffi-error-codes&k=iSolar+controller&tag=errorcodefixes-20) | E5 | Pump fault | Check circulator; check wiring |
| [Discaldirt/Dirtmag](https://www.amazon.com/s?ascsubtag=ecf-caleffi-error-codes&k=Discaldirt%2FDirtmag&tag=errorcodefixes-20) | Indicator full | Magnetic filter needs cleaning | Clean magnetic filter |

## Most Common Faults

### Zone Valve Actuator Failure
Caleffi Series 6130 (electric motorized) and Series 6150 (thermal) zone valves are common in residential radiant heating and hydronic distribution systems. 

**Motorized (6130) actuator failure:** The actuator motor drives the valve open against a spring-return. A failed motor results in a valve that stays closed (no heat to zone) or stuck open (zone cannot be shut off). Test by applying 24VAC directly to the actuator terminals — if the valve body moves, the actuator is fine and the wiring or zone controller is the issue. If the valve doesn't move with direct 24VAC, replace the actuator.

**Thermal actuator (6150) failure:** The wax-element actuator expands when heated by the 24VAC heating element, pushing the valve open. A failed element means the valve stays closed. Test: after 3–5 minutes with 24VAC applied, the valve stem should extend. If it doesn't move, replace the actuator head.

### Caleffi Mixing Valve (521/5230) — Temperature Issues
Caleffi thermostatic mixing valves maintain a fixed mixed water temperature. Failure modes:
- **Outlet too hot:** Thermostatic element has failed open to hot side. Replace the thermostatic cartridge.
- **No hot water at outlet:** Check valve has failed or element is stuck closed. Also verify hot water supply temperature is at least 10°F above the mixing valve set point.
- **Inconsistent temperature:** Large differential between hot and cold supply pressures. Install Caleffi pressure-compensating cartridges or add balancing valves.

### Caleffi Discaldirt and Dirtmag — Maintenance Indicators
The Discaldirt (dirt separator) and Dirtmag (magnetic dirt separator) do not have electronic fault indicators — maintenance is indicated by the amount of material accumulated in the collection chamber. Inspect the blowdown chamber monthly during initial system operation and quarterly thereafter. Heavy debris accumulation in the first few months is normal for new systems.

For the Dirtmag: remove the magnetic cartridge, wipe off the collected iron particles with a cloth, and reinstall. Do this quarterly or when you see reduced separator performance.

### iSolar E3 — Collector Overtemperature
In solar thermal systems, stagnation occurs when collector temperature exceeds 302°F (150°C) — typically during periods of high insolation with no heat demand. The iSolar controller halts the pump to protect glycol fluid from degradation. Stagnation is normal but should be minimized by properly sizing the solar loop. If E3 appears frequently, review system design and glycol concentration.

## Caleffi Air Vent Maintenance

Caleffi DISCAL automatic air vents and Series 502 float-type air vents should be inspected annually. A stuck-open air vent will continuously weep water. Close the service cap, then reopen — this often re-seats the valve. If still leaking, replace the air vent float assembly.

## When to Call a Pro
Zone valve actuator replacement is straightforward — most technicians can swap an actuator in 15 minutes without draining the system. However, if the valve body itself leaks from the packing or ball seal, the system must be drained and the valve body replaced — a job for a licensed plumber.

<!-- INTERNAL-LINK-AUTO -->
**Related:** [Rheem Performance Platinum PDN tankless error codes](/posts/rheem-performance-platinum-pdn-error-codes/)

