---
title: "York 4 Flashes Error Code — Open Limit Device Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-31T08:00:00Z
modDatetime: 2024-03-31T08:00:00Z
slug: york-4-flashes-error-code
featured: false
draft: false
tags:
  - hvac
  - york
  - furnace
  - limit-switch
description: "York 4 flashes means the high limit switch opened due to overheating. This guide covers every cause and fix for the York furnace 4-flash open limit fault."
---

## Error Code: York 4 Flashes

**What it means:** Four flashes on a York furnace diagnostic LED indicates an open high limit device. York furnaces (including Coleman and Luxaire, which share the same boards) use a normally-closed high limit switch mounted in the heat exchanger plenum. This switch opens when supply air temperature exceeds its rated setpoint — typically 160–180°F. When the limit opens, the gas valve closes immediately but the blower continues to run until the plenum cools and the limit resets. If the underlying cause of overheating is not addressed, the limit will trip repeatedly, and the board may lock out.

## Common Causes

- **Dirty air filter** — Blocked return airflow is the primary cause in the majority of cases. The heat exchanger cannot shed heat fast enough.
- **Blocked supply or return ducts** — Closed registers, furniture blocking returns, or crushed flex duct restricts airflow.
- **Blower motor or capacitor failure** — A blower running below rated RPM cannot move enough air over the heat exchanger.
- **Dirty evaporator coil** — A clogged coil downstream of the furnace creates backpressure and reduced airflow.
- **Limit switch failure** — A limit switch that trips at a lower temperature than its rating (due to age or internal contact corrosion) will fault even when the system is not actually overheating.

## Diagnosis Steps

1. Inspect and replace the air filter. If it is gray, matted, or visibly clogged, that is your cause.
2. Check all supply registers and return grilles. All should be fully open and unobstructed.
3. With the furnace running, measure the temperature rise: place a probe in the return air plenum and one in the supply plenum. Delta should be 40–70°F. Above 70°F confirms restricted airflow.
4. Listen to the blower — it should start within 30–60 seconds of heat call and reach full speed. Sluggish start or low noise level points to a failing capacitor or motor.
5. If airflow is correct and fault persists, use a multimeter to check the limit switch with power off and furnace cold. It should read continuity (closed). OL on a cold limit = failed switch.

## Fix

Fix airflow first. Replace the filter. Open all registers. If the capacitor reads below 10% of rated MFD, replace it before replacing the motor. Blower capacitors on York/Coleman furnaces are typically 5–7.5 MFD and available from any HVAC parts supplier.

If the limit switch has failed, replace it. York furnaces use multiple limit switch ratings across their model lineup — match the temperature rating and mounting style exactly. Order using the furnace model number.

## Parts

| Part | Where to Buy |
|------|-------------|
| [High limit switch](https://www.amazon.com/s?k=High+limit+switch&tag=errorcodefixes-20) | RepairClinic, SupplyHouse |
| [Blower motor run capacitor](https://www.amazon.com/s?k=Blower+motor+run+capacitor&tag=errorcodefixes-20) | Grainger, Amazon |
| [PSC blower motor](https://www.amazon.com/s?k=PSC+blower+motor&tag=errorcodefixes-20) | RepairClinic, Grainger |

## When to Call a Technician

If the 4-flash fault persists after filter replacement and airflow correction, have a licensed HVAC technician inspect the heat exchanger for cracks before continued operation.

## Related Articles

- [York 2 Flashes Error Code — Causes & Fix](/posts/york-2-flashes-error-code/)
- [York 3 Flashes Error Code — Causes & Fix](/posts/york-3-flashes-error-code/)
- [York 5 Flashes Error Code — Causes & Fix](/posts/york-5-flashes-error-code/)
- [York Furnace 6 Flashes Error Code — Pressure Switch Fault Fix](/posts/york-6-flashes-pressure-switch-fault/)
- [York 7 Flashes Error Code — Ignition Lockout Fix](/posts/york-7-flashes-error-code/)
