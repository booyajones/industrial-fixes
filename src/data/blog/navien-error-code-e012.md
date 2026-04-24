---
title: "Navien Error Code E012 — Flame Loss During Operation Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-04-08T08:00:00Z
modDatetime: 2024-04-08T08:00:00Z
slug: navien-error-code-e012
featured: false
draft: false
tags:
  - boiler
  - navien
  - flame-sensor
  - tankless
description: "Navien E012 error code means the flame was lost during operation. This guide covers diagnosis and fixes for the Navien E012 flame loss fault on tankless and combi units."
---

## Error Code: Navien E012

**What it means:** Navien error code E012 indicates flame loss during operation — the burner lit successfully, but the flame extinguished before the heating cycle completed. The flame sensor detected an active flame at startup, but the signal dropped to zero mid-cycle. The control board interprets this as an abnormal flame loss and shuts down the unit. E012 is distinct from E001 (which is a failure to ignite in the first place) — E012 means ignition was successful but the flame couldn't sustain itself. Reset with the power button.

## Common Causes

- **Dirty or weakly reading flame sensor** — Even a flame sensor that can produce enough microamp signal at initial ignition may lose signal during modulation (as the burner steps down in BTU output). The low-fire signal is weaker and harder to detect through a contaminated rod.
- **Low gas pressure during operation** — Gas pressure can be adequate at startup but drop below minimum during high-demand periods (other appliances firing simultaneously, long gas runs, undersized piping). Pressure drops cause flame instability.
- **Combustion air starvation** — Blocked air intake or exhaust venting causes incomplete combustion and flame instability. On Navien PVC-vented units, check both the intake and exhaust vent terminations.
- **Condensate backup** — On condensing units, water buildup in the heat exchanger due to a slow condensate drain can interfere with combustion.
- **Fan or blower fault** — The combustion air blower controls the air-fuel ratio. A slow or failing blower causes a rich mixture that is unstable.

## Diagnosis Steps

1. Clean the flame sensor rod — even if E001 was not occurring, a marginally contaminated sensor may pass ignition but fail at modulation. Remove the front cover, locate the sensor rod, clean with emery cloth.
2. Inspect both vent pipe connections. Verify the intake is pulling fresh outdoor air and the exhaust is fully expelling combustion gases. A blocked exhaust on a concentric vent system will recirculate exhaust gas and choke combustion.
3. Check for simultaneous gas demand: does E012 occur more frequently when the clothes dryer, range, or boiler fires at the same time? If yes, gas pressure drop under combined load is the cause.
4. Inspect the condensate drain: is it flowing freely during and after operation? A slow drain can back up into the heat exchanger.
5. Listen to the combustion blower during startup — it should spin up quickly and run smoothly. Irregular or slow blower indicates motor wear or debris in the blower wheel.

## Fix

Clean the flame sensor first. If E012 occurs at low-fire modulation specifically, the sensor is the likely cause.

For venting issues: Navien units require specific vent termination clearances — minimum 12 inches above grade, away from corners, windows, and gas meters. Any obstruction at the termination cap must be cleared.

If gas pressure is the cause: a gas plumber needs to upsize the supply piping or install a dedicated line for the Navien unit.

For a worn combustion blower: replace the combustion blower assembly. Navien blower assemblies are model-specific.

## Parts

| Part | Where to Buy |
|------|-------------|
| Flame sensor rod assembly | RepairClinic, SupplyHouse |
| Combustion blower motor | SupplyHouse, Grainger |
| Condensate drain assembly | Amazon, RepairClinic |

## When to Call a Technician

Gas pressure diagnosis requires a licensed gas technician with a manometer. Combustion blower replacement and heat exchanger inspection require opening the unit's combustion chamber — a licensed plumber or HVAC tech should handle this on warranty units to preserve coverage.
