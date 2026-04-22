---
title: "Lennox Error Code 412 — Limit Switch Fault Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-04-02T08:00:00Z
modDatetime: 2024-04-02T08:00:00Z
slug: lennox-error-code-412
featured: false
draft: false
tags:
  - hvac
  - lennox
  - furnace
  - limit-switch
description: "Lennox error code 412 means the high limit switch has opened due to overheating. This guide covers diagnosis and fixes for the Lennox iComfort and SLP furnace limit fault."
---

## Error Code: Lennox 412

**What it means:** Lennox error code 412 (displayed on the iComfort thermostat or the furnace diagnostic LED as a 4-1-2 flash sequence) indicates an open limit switch circuit. The high limit switch in Lennox SLP, XC, and EL-series furnaces is a normally-closed device mounted on the heat exchanger or supply plenum. It opens when plenum temperature exceeds its calibrated setpoint, typically 160–200°F depending on furnace BTU rating and installation configuration. When the limit opens, the gas valve de-energizes and the blower runs in circulate mode to cool the heat exchanger. Lennox boards log the event and display Code 412.

## Common Causes

- **Clogged media or high-MERV filter** — Lennox systems are frequently paired with Healthy Climate media filters (MERV-16). These require more frequent replacement than standard 1" filters. A 6-month-old media filter may be completely clogged.
- **Blower motor failure or degraded capacitor** — Variable-speed ECM motors in Lennox SLP furnaces can fail at the module. A reduced-speed blower cannot remove heat.
- **Blocked PureAir or filtration system** — Some Lennox systems integrate PureAir or PCO filters in the return path. Blockages there restrict total system airflow.
- **Closed registers or blocked returns** — Insufficient return airflow from register management or furniture placement.
- **Limit switch failure** — The switch itself can fail open due to age or repeated thermal cycling.

## Diagnosis Steps

1. Locate and inspect the air filter. Lennox media filters often need replacement every 6–9 months in normal use, not the 12 months marked on the packaging.
2. Check the iComfort or S30 thermostat for additional fault codes alongside 412. A concurrent blower fault would point to the ECM motor.
3. Verify all supply/return registers are open and confirm the return air path is unobstructed.
4. Access the furnace and listen to the blower during heat cycle. Lennox SLP furnaces use variable-speed motors — they should ramp smoothly from low to the appropriate heating speed. Stagnation or low speed suggests ECM module failure.
5. With power off and furnace cold, measure the limit switch with a multimeter across its terminals. Continuity = normal. OL = switch has failed open and must be replaced.

## Fix

Replace the media filter first. If the blower is running at reduced speed, access the ECM module (the rectangular controller attached to the back of the blower motor). Swapping the module is less expensive than replacing the full motor — match the module part number printed on the module housing.

If the limit switch reads open when cold, replace it. Lennox sources its limit switches from several manufacturers — match the temperature rating and physical configuration using the furnace model and serial number.

After correcting the cause, clear the fault via the iComfort thermostat or by cycling furnace power.

## Parts

| Part | Where to Buy |
|------|-------------|
| High limit switch | RepairClinic, SupplyHouse |
| Lennox media filter | Amazon, SupplyHouse |
| ECM motor module | RepairClinic, Grainger |

## When to Call a Technician

If Code 412 persists after filter replacement and register correction, have a licensed HVAC tech inspect the heat exchanger. Lennox SLP furnaces are high-efficiency units — a cracked secondary heat exchanger requires professional diagnosis.
