---
title: "Hoshizaki E6 Error Code — Causes & Fix"
description: "What Hoshizaki ice machine error code E6 means, why the refrigerant circuit faults, and how to fix it."
pubDatetime: 2026-04-22T10:00:00Z
modDatetime: 2026-04-22T10:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - refrigeration
  - hoshizaki
---

## Hoshizaki E6 Error Code — What It Means

Error code E6 on a Hoshizaki ice machine (KM, KMD, FS, DCM, AM series) indicates a refrigerant circuit fault — the machine completed a freeze cycle but the harvest cycle exceeded the maximum allowed time without the thermistor detecting the expected temperature rise. This typically means the machine is not harvesting ice properly, which points to low refrigerant charge, a defective hot gas valve, or a harvesting system problem.

[Jump to Fix](#fix)

## Common Causes

- **Low refrigerant charge** — Insufficient refrigerant reduces the system's capacity to move heat during the harvest cycle, extending harvest time beyond the maximum and tripping E6.
- **Failed hot gas solenoid valve** — Hoshizaki machines use a hot gas bypass valve to divert hot refrigerant discharge gas through the evaporator to melt ice off the plate. A failed or stuck-closed solenoid prevents harvesting.
- **Dirty condenser coil** — High head pressure from a dirty condenser reduces refrigerant mass flow through the system, affecting both freeze and harvest performance.
- **Thermistor fault** — A drifting thermistor that does not detect the temperature rise during harvest causes the control board to time out and generate E6.

## Step-by-Step Fix {#fix}

1. **Clean the condenser coil** — Power off the machine and clean the condenser fins with a coil cleaner and low-pressure rinse. Confirm the condenser fan is running at speed. High head pressure from a dirty condenser mimics refrigerant undercharge.
2. **Check the hot gas solenoid valve** — During a harvest cycle, you should hear the solenoid valve click open. Confirm 24VAC at the solenoid coil terminals during harvest. If voltage is present but the valve is silent, the coil or plunger is failed — replace the hot gas valve assembly.
3. **Monitor harvest thermistor temperature** — Connect a temperature meter probe to the evaporator outlet or use the machine's diagnostic mode to monitor the harvest thermistor. During harvest, temperature should rise from below 0°C to around 40–50°C within 2–3 minutes. Failure to rise indicates low refrigerant or a failed valve.
4. **Have refrigerant charge checked** — Only a licensed HVAC/R technician with manifold gauges and a recovery cylinder can check and correct refrigerant charge on an E6. Low charge requires leak search before recharge.
5. **Clear E6 and test** — After corrections, clear the fault per model-specific instructions (typically by cycling the Off/On switch or pressing the reset button on the control board). Run a complete freeze-harvest cycle and observe.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hot gas solenoid valve | Hoshizaki OEM; match model and coil voltage |
| Harvest thermistor | Match KM or FS series connector |
| Condenser coil cleaner | Nu-Calgon Coil-Aid or equivalent |
| Refrigerant (R-404A or R-448A) | Licensed tech required for handling |

## When to Call a Pro

Refrigerant system diagnosis and repair on commercial ice machines requires EPA 608 certification and commercial refrigeration experience. E6 caused by low charge also requires a leak search — operating with a known leak is illegal under EPA Section 608 regulations.
