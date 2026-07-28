---
title: "Buderus Boiler Fault Code A1 — Causes & Fix"
description: "What Buderus Logamax/Logano fault code A1 means, why the service alert fires, and how to fix it step by step."
pubDatetime: 2026-04-22T15:00:00Z
modDatetime: 2026-04-22T15:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - boiler
  - buderus
money_part: "NTC temperature sensor"
most_likely_cause: "Failed boiler temperature sensor (NTC)"
---

## What this code means
Fault code A1 on a Buderus Logamax or Logano boiler typically indicates a service-required alert or a short-circuit/open-circuit condition on a sensor circuit — most often the boiler water temperature sensor (NTC sensor on the supply or return). On Logamax Plus GB142 and GB162 condensing models, A1 frequently means the boiler temperature sensor (TS) has failed or its circuit is interrupted. The boiler may continue operating at a reduced or fixed output, or may lock out entirely depending on which sensor has faulted.

## Common Causes

- **Failed boiler temperature sensor (NTC)** — The NTC thermistor measuring supply water temperature drifts out of spec or develops an open circuit, triggering A1 on Buderus's Logamatic control platform.
- **Loose or corroded sensor connector** — The sensor wire connector can loosen from vibration or corrode in damp boiler rooms, producing an intermittent open circuit that the controller reads as a fault.
- **Blocked condensate siphon (condensing models)** — A blocked condensate trap on the GB142/GB162 can restrict flue flow, causing the boiler to abort startup and display A1 as a startup lockout on some firmware versions.
- **Service interval reached** — On boilers with a Logamatic control module (RC35, RC300 series), A1 can also flag when the boiler has accumulated the programmed service hours and the maintenance interval reminder has activated.

## Step-by-Step Fix {#fix}

1. **Read the full fault display** — Buderus controls often display both a fault code and a sub-code. Record both — "A1" combined with a sub-code narrows the exact circuit that has faulted.
2. **Inspect the boiler temperature sensor** — Locate the NTC sensor on the supply pipe or boiler header. Disconnect the connector and measure resistance at the operating water temperature using the Buderus NTC resistance-temperature table (typically 2.5–10 kΩ at heating range temperatures). Replace a sensor that reads open or far outside spec.
3. **Reseat sensor connectors** — Even if the sensor measures correctly, disconnect and firmly reseat the connector. Corrosion on the pins can be cleaned with electrical contact cleaner.
4. **Clear the condensate drain** — On GB142/GB162 condensing boilers, confirm the siphon trap is full of water and the drain line is clear. A dry trap passes flue gas backward and can trigger safety shutdowns.
5. **Reset the service reminder** — If A1 is a service reminder, navigate to the Logamatic control's service menu and reset the interval counter after completing the maintenance tasks.
6. **Reset the boiler** — After addressing the root cause, reset from the control panel. The boiler should restart and complete a normal firing sequence.

## Parts Often Needed

| Part | Notes |
|------|-------|
| NTC temperature sensor | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-buderus-boiler-fault-code-a1&tag=errorcodefixes-20) \| Match the Buderus part number for the specific model (GB142, GB162, etc.) |
| Condensate siphon / trap | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-buderus-boiler-fault-code-a1&k=Condensate+siphon+%2F+trap&tag=errorcodefixes-20) \| Buderus OEM; condensing models require the correct internal volume |
## When to Call a Pro

Buderus/Bosch-Thermotechnik equipment requires a registered technician for warranty work and for setting combustion parameters. If A1 is accompanied by combustion anomalies (sooting, flame color issues, CO alarm), do not attempt to reset — call a licensed heating engineer.
