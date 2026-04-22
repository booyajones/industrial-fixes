---
title: "Mitsubishi E3 Error Code — Indoor Fan Motor Fault Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-04-06T08:00:00Z
modDatetime: 2024-04-06T08:00:00Z
slug: mitsubishi-e3-error-code
featured: false
draft: false
tags:
  - hvac
  - mitsubishi
  - mini-split
  - fan-motor
description: "Mitsubishi E3 error code means the indoor fan motor has failed or is not operating within spec. This guide covers diagnosis and fixes for the Mitsubishi mini-split E3 fault."
---

## Error Code: Mitsubishi E3

**What it means:** Mitsubishi error code E3 indicates an indoor fan motor fault. The indoor unit fan (cross-flow blower motor) is controlled by the indoor PCB via a PWM signal. The motor's built-in Hall effect sensor sends feedback to the board confirming actual RPM. If the motor fails to reach the commanded speed within the startup period — or if speed drops below minimum threshold during operation — the indoor board faults with E3 and shuts down the system. This prevents the evaporator coil from freezing and protects the motor from thermal overload.

## Common Causes

- **Failed indoor fan motor** — DC brushless fan motors in Mitsubishi indoor units fail at the Hall effect sensor, motor windings, or the integrated motor driver. Common on units 8–15 years old.
- **Blocked cross-flow blower** — Mold, dust buildup, or a foreign object jamming the blower scroll prevents the fan from reaching speed. The board detects the stall.
- **Failed indoor PCB** — The indoor board's PWM driver circuit can fail, preventing the motor from receiving correct drive signals even if the motor itself is functional.
- **Motor connector fault** — A loose or corroded connector at the motor harness breaks the signal loop between the motor Hall sensor and the board.
- **Frozen evaporator coil** — A severely iced coil can physically block the blower from rotating, causing E3 as a secondary fault.

## Diagnosis Steps

1. Power off the unit for 30 minutes. Remove the front panel and filter to inspect the blower wheel. Look for debris, mold buildup (a common issue in humid climates), or ice on the evaporator fins.
2. Try to rotate the blower wheel by hand with the unit powered off. It should spin freely with slight bearing resistance. If it's stiff, stuck, or grinds: the motor bearings have failed or there is debris in the scroll.
3. Restore power and initiate a fan-only mode. The blower should start immediately. Listen for: smooth operation (normal) vs. humming without spin (motor trying but not running) vs. complete silence (motor or PCB failure).
4. If the motor hums but doesn't start: check the motor connector at both the motor and PCB. Unplug and inspect for bent or corroded pins. Reconnect and test.
5. If the motor is silent with good connections: the motor or PCB fan driver circuit has failed. A technician can isolate using a DC motor resistance test and a working substitute motor.

## Fix

Clean the blower wheel thoroughly if buildup is found — use a coil cleaner or diluted bleach solution and a soft brush. A clogged blower wheel is a common E3 cause in humid markets and requires no parts.

If the motor has failed (won't spin freely, humming without rotation, or winding tests open), replace the indoor fan motor. Mitsubishi indoor fan motors are DC brushless units specific to the indoor model number — verify the part number against the wiring diagram inside the indoor unit.

If wiring and motor are correct and the fault persists, the indoor PCB fan driver has failed. Replace the indoor PCB.

## Parts

| Part | Where to Buy |
|------|-------------|
| Indoor fan (cross-flow blower motor) | SupplyHouse, Grainger |
| Indoor unit PCB | SupplyHouse, RepairClinic |
| Coil cleaner / no-rinse coil spray | Amazon, Grainger |

## When to Call a Technician

DC brushless motor replacement in Mitsubishi indoor units requires removing the indoor unit from its mounting plate and disassembling the blower housing. A licensed tech with experience on ductless systems can complete this repair in 1–2 hours. If the outdoor refrigerant circuit is not involved, this is a non-refrigerant repair (no EPA certification needed for the motor swap itself).
