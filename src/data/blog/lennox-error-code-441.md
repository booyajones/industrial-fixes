---
title: "Lennox Error Code 441 — Limit Device Fault"
description: "Lennox error code 441 signals a limit device has opened during operation. This guide covers which limit tripped, why, and how to fix it without replacing parts unnecessarily."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - lennox
  - furnace
  - hvac
  - error-code
  - limit-switch
---

## Lennox Error Code 441 — Limit Device Open

Lennox error code 441 means **a limit device (high-limit switch) opened during furnace operation**. This is a safety shutdown — the furnace detected overheating conditions and shut off the burners to protect the heat exchanger.

Code 441 appears on Lennox SL280, EL280, SL297, and related models that use the Lennox iComfort or communicating control system. It may display as "441" or "Limit Device Open" on the thermostat or furnace diagnostic LED.

## What Limit Devices Are on Lennox Furnaces

| Device | Location | Trip Temp |
|---|---|---|
| Primary high-limit switch | On heat exchanger | 150–200°F |
| Secondary high-limit switch | Blower compartment (some models) | 130–150°F |
| Rollout limit switch | Burner area | 200–250°F |
| Auxiliary limit switch | Flue outlet area (condensing) | 175°F |

Code 441 typically points to the **primary high-limit switch**.

## Why the Limit Opens

The limit switch is doing its job — something is causing the heat exchanger to overheat. Find the cause before the heat exchanger cracks.

### Airflow Problems (Most Common)

- **Dirty air filter** — replace immediately, this is #1
- **Closed or blocked supply/return registers**
- **Dirty blower wheel** — caked dust reduces CFM significantly
- **Undersized duct system** — causes high static pressure, low airflow
- **Failed blower motor or capacitor** — blower not running at proper speed

### Heat Exchanger Problems

- **Cracked heat exchanger** — hot gases recirculate into blower compartment, heating the limit switch prematurely
- **Restricted heat exchanger** — scale or debris buildup (rare)

### Thermostat/Control Issues

- **Continuous fan mode** — some configurations cycle burners too fast
- **IFC board fault** — incorrect burner-to-blower timing

## Fix It Step by Step

**Step 1 — Replace air filter.** Non-negotiable. If you haven't done this in 3 months, it's suspect.

**Step 2 — Check all registers and returns.** Walk every room. Open every supply register. Move furniture blocking floor returns.

**Step 3 — Let furnace cool 20–30 minutes.** The limit will auto-reset when it cools (most Lennox limits are auto-reset, not manual). Then power cycle the thermostat.

**Step 4 — Check blower operation.** When heat comes on, the blower should start within 30–60 seconds. If it doesn't, check the run capacitor on the blower motor — a weak capacitor causes the motor to run slow or not at all.

**Step 5 — Clean the blower wheel.** Remove the blower assembly and use a vacuum/brush to clean the blades. A dirty blower can lose 40% of its airflow.

**Step 6 — If 441 persists with good airflow**, have a tech check for a cracked heat exchanger (combustion analyzer, visual inspection with camera scope).

## Parts You May Need

| Part | Cost |
|---|---|
| Air filter (MERV 8–11) | $10–30 |
| Blower motor run capacitor | $15–40 |
| High-limit switch (OEM) | $30–70 |
| Blower motor | $150–400 |

## Lennox iComfort Codes Related to 441

If you have an iComfort thermostat, the system may also log:
- **440** — Limit device still open after blower ran for extended period
- **442** — Limit device opened on 2nd stage burner
- **443** — Limit tripped too many times (lockout)

These escalating codes indicate the limit trip is frequent — get it diagnosed before 443 locks out the system entirely.
