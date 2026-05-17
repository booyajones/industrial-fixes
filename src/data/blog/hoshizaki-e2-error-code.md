---
title: "Hoshizaki E2 Error Code — Harvest Fault Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-04-15T08:00:00Z
modDatetime: 2024-04-15T08:00:00Z
slug: hoshizaki-e2-error-code
featured: false
draft: false
tags:
  - refrigeration
  - hoshizaki
  - ice-machine
description: "Hoshizaki E2 error code means the ice machine has a harvest fault — the ice won't release from the evaporator. This guide covers diagnosis and fixes for the Hoshizaki E2 fault."
---

## Error Code: Hoshizaki E2

**What it means:** Hoshizaki error code E2 indicates a harvest fault — the ice machine completed a freeze cycle but the ice did not release from the evaporator plate within the maximum harvest time limit. On Hoshizaki crescent-cube machines, harvest is initiated by hot gas bypass from the compressor: a harvest valve diverts hot refrigerant gas through the evaporator to melt the thin adhesive bond between the ice and the evaporator surface. The machine expects ice to release and fall into the bin within 3.5 minutes (standard) from harvest initiation. If the ice has not released by that time, the board faults with E2.

## Common Causes

- **Low refrigerant charge** — Insufficient refrigerant reduces the heat delivered to the evaporator during harvest. The ice bond doesn't break and the machine times out. This is the most common cause of E2 on older machines.
- **Failed harvest valve (hot gas bypass valve)** — If the harvest solenoid valve is stuck closed or electrically failed, hot gas never reaches the evaporator. The ice cannot release regardless of cycle time.
- **Scale buildup on evaporator surface** — Mineral deposits on the evaporator cube cells change the freeze pattern and the ice-to-plate bond. The harvest hot gas cannot break through the mineralized interface efficiently.
- **High ambient temperature** — Harvest relies on a temperature differential. In very high ambient conditions, the hot gas may not be hot enough relative to ambient to produce effective evaporator warming.
- **Worn or stiff water curtain / ice guide** — On cube machines, a stiff or misaligned ice guide can mechanically block ice from falling into the bin even after the bond breaks.

## Diagnosis Steps

1. Check the ambient temperature in the equipment room. If it exceeds 100°F, this is outside Hoshizaki's rated ambient for most machines and harvest issues are expected.
2. Inspect the evaporator for scale buildup. Remove the front panel and look at the evaporator grid — heavy mineral deposits (white chalky buildup) confirm scale is the issue.
3. During a harvest cycle (when E2 is about to occur), listen for the harvest valve to click energized. No click indicates the valve is not being energized — check the board output and valve coil resistance (typically 10–20 ohms).
4. Check refrigerant sight glass (if present) during operation. Bubbles during the steady freeze cycle indicate low charge.
5. Inspect the ice guide and water curtain: verify they move freely and are not binding against the evaporator or bin opening.

## Fix

For scale buildup: perform a complete Hoshizaki descale cleaning using Hoshizaki's approved nickel-safe descaler. Run two full cleaning cycles per the service manual. Stubborn scale may require manual cleaning of the evaporator grid with a soft brush.

For a failed harvest valve: measure coil resistance across the solenoid terminals (power off). OL = open coil, replace the valve. Hoshizaki harvest valves are model-specific — order by machine model number.

For low refrigerant: a licensed EPA 608-certified refrigeration technician must recover, check for leaks, repair, and recharge the system.

## Parts

| Part | Where to Buy |
|------|-------------|
| [Hoshizaki harvest valve solenoid](https://www.amazon.com/s?i=industrial&k=Hoshizaki+harvest+valve+solenoid&tag=errorcodefixes-20) | RepairClinic, SupplyHouse |
| [Hoshizaki descaler (nickel-safe)](https://www.amazon.com/s?i=industrial&k=Hoshizaki+descaler+%28nickel-safe%29&tag=errorcodefixes-20) | Amazon, SupplyHouse |
| [Ice machine cleaner / sanitizer kit](https://www.amazon.com/s?i=industrial&k=Ice+machine+cleaner+%2F+sanitizer+kit&tag=errorcodefixes-20) | Amazon, RepairClinic |

## When to Call a Technician

Any refrigerant-related cause of E2 requires an EPA 608-certified refrigeration technician. Harvest valve replacement is within the scope of a competent appliance tech familiar with commercial ice machines. Descale cleaning is a routine maintenance task that can be performed by facility staff.

## Related Articles

- [Hoshizaki C-101BAH / C-201BAH Countertop Ice Maker Error Codes — Full Fault Guide](/posts/hoshizaki-c-101bah-error-codes/)
- [Hoshizaki DKM-500 Cube Dispenser Error Codes — Fault Code Diagnostic Guide](/posts/hoshizaki-dkm-500-error-codes/)
- [Hoshizaki Ice Machine E1 Error Code — Water Inlet Fix](/posts/hoshizaki-e1-error-code/)
- [Hoshizaki E3 Error Code — Causes & Fix](/posts/hoshizaki-e3-error-code/)
- [Hoshizaki E4 Error Code — Causes & Fix](/posts/hoshizaki-e4-error-code/)
