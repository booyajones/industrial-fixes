---
title: "Heatcraft Refrigeration Alarm 2 — Causes & Fix"
description: "What Heatcraft refrigeration alarm 2 means, why low temperature alarms trigger, and how to fix it step by step."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - refrigeration
  - heatcraft
---

## Heatcraft Refrigeration Alarm 2 — What It Means

Heatcraft Alarm 2 is a **low temperature alarm** — the refrigerated space temperature dropped below the configured low temperature setpoint. Heatcraft (a Lennox company) evaporator controllers used on walk-in coolers, freezers, and refrigerated warehouses monitor box temperature continuously; when it falls below the low limit for a sustained period, Alarm 2 is triggered. This protects product from freeze damage in cooler applications and alerts operators to potential equipment malfunction in freezer applications (where over-cooling can indicate a defrost failure or control fault).

[Jump to Fix](#fix)

## Common Causes

- **Low temperature setpoint configured too high for the application** — The alarm limit is set too close to the normal operating temperature, causing nuisance trips during normal pulldown or after defrost.
- **Defrost termination failure leaving coil in extended cooling** — If the defrost cycle runs excessively short and the coil re-ices quickly, the system may over-cool between defrosts.
- **Thermostat or temperature sensor fault** — A failing temperature sensor reads lower than actual temperature, triggering a false low-temperature alarm.
- **Refrigerant overcharge or TXV stuck open** — An overcharged system or a thermostatic expansion valve (TXV) stuck open floods the evaporator and drives box temperature lower than intended.

## Step-by-Step Fix {#fix}

1. **Check the actual box temperature** — Use an independent calibrated thermometer in the refrigerated space. Compare to the controller's displayed temperature. A significant discrepancy indicates a faulty temperature sensor.
2. **Review the alarm setpoint** — In the Heatcraft controller, check the low temperature alarm setpoint (parameter A2 or similar). Confirm it's set appropriately for the application — typically 3–5°F below the normal operating setpoint.
3. **Check the temperature sensor** — With the controller powered, disconnect the temperature sensor and measure resistance. Compare to the manufacturer's resistance-temperature curve. Replace if out-of-spec.
4. **Review defrost schedule** — Check how many defrost cycles are scheduled per day and the defrost duration. If defrosts are too short or infrequent, excess frost on the coil can cause over-cooling between cycles.
5. **Check for refrigerant overcharge symptoms** — Unusually cold suction line (sweating heavily or frosting near the compressor), high suction pressure, and consistently below-setpoint box temperatures suggest overcharge or a stuck-open TXV.
6. **Acknowledge and reset the alarm** — After diagnosis and correction, navigate to the controller's alarm menu to acknowledge and clear Alarm 2.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Box temperature sensor (NTC thermistor) | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?tag=errorcodefixes-20) \| Heatcraft model-specific; match resistance specification |
| TXV (thermostatic expansion valve) | [Amazon](https://www.amazon.com/s?k=TXV+%28thermostatic+expansion+valve%29&tag=errorcodefixes-20) \| Only if overcharge/flooding is confirmed after refrigerant work |
## When to Call a Pro

If the sensor checks out and the setpoint is correctly configured but the box is genuinely overcooling, have a licensed refrigeration technician check refrigerant charge and TXV operation. Refrigerant system work requires EPA 608 certification.
