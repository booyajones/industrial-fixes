---
title: "York TG9 Furnace Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to York TG9 furnace error codes, LED flash sequences, common fault causes, and step-by-step repair procedures for HVAC technicians."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - york
  - furnace
money_part: "Hot surface igniter"
---

## York TG9 Furnace Error Codes — What They Mean

The York TG9 is a 96% AFUE two-stage variable-speed gas furnace. It is part of York's Affinity series and uses a communicating control board when connected to a York proprietary thermostat, or a standalone LED diagnostic when used with a conventional thermostat. The TG9 uses an ECM blower motor for variable airflow and a two-stage gas valve for comfort-based modulation. It vents via PVC condensing flue and produces condensate requiring a drain trap.

## York TG9 LED Flash Code Reference

| Flash Sequence | Fault |
|---|---|
| 1 flash | Normal — waiting for call |
| 2 flashes | Pressure switch stuck open |
| 3 flashes | Pressure switch stuck closed |
| 4 flashes | High-limit switch open |
| 5 flashes | Ignition lockout — 3 failed attempts |
| 6 flashes | Rollout switch open |
| 7 flashes | Flame sensed without gas valve call |
| 8 flashes | Inducer motor speed fault |
| 9 flashes | Blower motor fault |
| 10 flashes | Control board fault |
| 11 flashes | Communication fault (if connected to York thermostat) |
| Rapid | Low voltage — below 18VAC |

## Common Causes by Code

- **2 flashes — Pressure switch open** — The TG9 is a 90%+ condensing furnace — the condensate system is part of the pressure switch circuit. A blocked condensate drain line fills the secondary heat exchanger with water and prevents proper inducer draft, causing the pressure switch to stay open. Clean the condensate trap and check the drain line.
- **4 flashes — Limit open** — ECM blower motor fault (Code 9) can cascade into a limit fault (Code 4) if the blower fails to run at the correct speed. Check ECM connector before chasing airflow restriction.
- **5 flashes — Ignition lockout** — Confirm gas supply. Check HSI igniter (should glow brightly within 30 seconds). Clean the flame sensor. If the TG9 lights then goes off within 3 seconds, the flame sensor needs cleaning — this is the most common York TG9 service call.
- **8 flashes — Inducer motor speed** — The TG9 ECM inducer motor feeds tachometer feedback to the control board. If the motor spins but at the wrong speed, the board flags Code 8. Check the tach signal wire connector at the inducer.
- **9 flashes — Blower motor fault** — ECM blower motor communication fault. Check the 5-pin communication connector at the motor and at the board. Measure 120VAC supply to the motor.

## Step-by-Step Fix {#fix}

1. **Read the LED** — The York TG9 LED is inside the control compartment, visible through the observation window in the lower panel. Count the flash sequence (flashes, then pause, then repeat).
2. **For 2 flashes (pressure switch)** — Locate the condensate trap (under the secondary heat exchanger or inside the furnace cabinet). Remove the trap and flush it with water. Reconnect and restart. If the fault clears, the condensate drain was blocked.
3. **For 5 flashes (ignition lockout)** — Reset by pressing the board's reset button or cycling power at the furnace switch. Watch the ignition sequence on restart: inducer → pressure switch closes → igniter heats → gas valve opens. Each step should happen in sequence within 30–60 seconds.
4. **For 8 flashes (inducer speed)** — Check the inducer motor tach wire. It is a small-gauge wire (often white or yellow) connected to a 3-pin connector on the inducer motor. Verify the connector is fully seated.
5. **For 9 flashes (blower)** — Verify the ECM motor is getting 120VAC at the motor power connector. Check the communication cable (5-pin) between the motor module and the board. If the motor runs but slowly, the motor module may need replacement.

## Parts Often Needed

| Part | Notes |
|---|---|
| Hot surface igniter | [Amazon](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-york-tg9-furnace-error-codes&tag=errorcodefixes-20) \| Silicon nitride; specific to TG9 model |
| Flame sensor | [Amazon](https://www.amazon.com/s?k=Flame+sensor&tag=errorcodefixes-20) \| Rod-type; clean before replacing |
| Condensate trap | [Amazon](https://www.amazon.com/dp/B077J4Y763?ascsubtag=ecf-york-tg9-furnace-error-codes&tag=errorcodefixes-20) \| PVC trap assembly; critical to pressure switch operation |
| ECM blower motor module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-york-tg9-furnace-error-codes&k=ECM+blower+motor+module&tag=errorcodefixes-20) \| Module only — verify motor spins freely before replacing |
| Inducer motor assembly | [Amazon](https://www.amazon.com/dp/B00FDZ90B2?ascsubtag=ecf-york-tg9-furnace-error-codes&tag=errorcodefixes-20) \| ECM type; includes tach feedback |
| Pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-york-tg9-furnace-error-codes&tag=errorcodefixes-20) \| Check tubing and condensate trap first |
## When to Call a Pro

The York TG9 ECM motor and variable-speed control logic require familiarity with York's communicating control system. If the TG9 is installed with a York proprietary thermostat and showing thermostat-level fault codes, a York dealer with system diagnostic tools is needed for full root-cause analysis. Rollout switch trips (Code 6) must be investigated for heat exchanger integrity before returning to service.
