---
title: "Scotsman Ice Machine Error Code 1 — High Pressure Cutout Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-04-16T08:00:00Z
modDatetime: 2024-04-16T08:00:00Z
slug: scotsman-ice-machine-error-code-1
featured: false
draft: false
tags:
  - refrigeration
  - scotsman
  - ice-machine
description: "Scotsman ice machine error code 1 means the high pressure cutout has tripped. This guide covers diagnosis and fixes for the Scotsman Code 1 high pressure fault."
---

## Error Code: Scotsman Code 1

**What it means:** Scotsman error code 1 (displayed as 1 flash or "E1" on Prodigy-series machines) indicates a high pressure cutout. The high pressure safety switch is wired in series with the compressor control circuit. When refrigerant discharge pressure exceeds the switch setpoint — typically 400 PSIG on R404A systems or 450 PSIG on R448A/R449A systems — the switch opens, cutting power to the compressor. The machine shuts down and displays Code 1. On Scotsman Prodigy machines, the machine will attempt automatic restart after the high pressure switch resets (it is an auto-reset type). Multiple consecutive Code 1 faults indicate a persistent issue.

## Common Causes

- **Dirty condenser (air-cooled units)** — The most common cause by a wide margin. A clogged condenser coil prevents heat rejection, causing discharge pressure to climb. On air-cooled machines in dusty or greasy environments, the condenser can clog within 1–3 months.
- **Inadequate condenser airflow** — The machine is installed without adequate clearance (Scotsman requires minimum 6" on intake sides, 12" on discharge), or is recirculating its own hot exhaust air.
- **High ambient temperature** — Air-cooled machines installed in locations above 100°F will have chronically elevated head pressure.
- **Overcharge of refrigerant** — Excess refrigerant in the system floods the condenser and raises head pressure. Caused by previous incorrect service.
- **Failed condenser fan motor** — On machines with a separate condenser fan, a failed motor stops airflow entirely, causing rapid head pressure rise.
- **Refrigerant non-condensable contamination** — Air or nitrogen in the refrigerant circuit raises discharge pressure above the system's normal operating profile.

## Diagnosis Steps

1. Inspect and clean the condenser coil. On air-cooled units, use compressed air or a coil cleaner to remove dust, grease, and debris from the fins. This single step resolves Code 1 in the majority of field calls.
2. Check installation clearances: measure distance from the machine sides and top to walls or adjacent equipment. Compare to Scotsman installation requirements in the spec sheet.
3. Verify the condenser fan is running during operation. On Prodigy cube machines, the fan should run during freeze and harvest cycles. A fan that isn't spinning (motor failed, blade loose) causes rapid Code 1.
4. If the condenser is clean and the fan is running: measure discharge pressure with a manifold gauge set. Pressure above the HP switch setpoint during normal ambient conditions indicates refrigerant system issues (overcharge, non-condensables, liquid line restriction).
5. Check the liquid line sight glass (if present) during operation. Bubbling at normal ambient temperatures can indicate low charge or restriction, not overcharge — low charge causes liquid flashing which can trigger HP switch at moderate discharge levels.

## Fix

Clean the condenser thoroughly — this is a maintenance task that resolves the majority of Code 1 faults. Use Nu-Brite or equivalent commercial coil cleaner for grease-fouled condensers. Rinse with water if the location permits.

If the condenser fan has failed: replace the fan motor. Scotsman condenser fans are application-specific — order by machine model number. Most are single-speed permanent split capacitor (PSC) motors.

If refrigerant system issues are present (overcharge, non-condensables, restriction): a licensed EPA 608-certified technician must diagnose and correct the refrigerant circuit.

## Parts

| Part | Where to Buy |
|------|-------------|
| [Scotsman condenser fan motor](https://www.amazon.com/dp/B0D2L5NSMM?tag=errorcodefixes-20) | RepairClinic, SupplyHouse |
| [Coil cleaner (Nu-Brite or equivalent)](https://www.amazon.com/s?k=Coil+cleaner+%28Nu-Brite+or+equivalent%29&tag=errorcodefixes-20) | Amazon, Grainger |
| [High pressure switch](https://www.amazon.com/dp/B013IHQ8CU?tag=errorcodefixes-20) | RepairClinic, SupplyHouse |

## When to Call a Technician

All refrigerant-side diagnosis and repair requires an EPA 608-certified technician. Condenser cleaning and fan motor replacement are within the scope of a competent appliance or facilities technician.

## Related Articles

- [Scotsman C0522 Error Codes — Fix Guide](/posts/scotsman-c0522-error-codes/)
- [Scotsman HID312 Error Codes — Fault Code Diagnostic Guide](/posts/scotsman-hid312-error-codes/)
- [Scotsman HID525 Error Codes — Complete Guide](/posts/scotsman-hid525-error-codes/)
- [Scotsman Ice Machine Complete Troubleshooting Guide — All Error Codes](/posts/scotsman-ice-machine-complete-guide/)
- [Scotsman Ice Machine Error Code 2 — Causes & Fix](/posts/scotsman-ice-machine-error-code-2/)
