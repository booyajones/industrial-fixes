---
title: "Lennox Elite Series Furnace Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to Lennox Elite Series furnace error codes, LED flash sequences, alert codes, common fault causes, and step-by-step repair procedures."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - lennox
  - furnace
---

## Lennox Elite Series Furnace Error Codes — What They Mean

The Lennox Elite Series includes several residential gas furnace models: the EL195E, EL180E, EL296V, and G61MPV among others. These furnaces use Lennox's SureLight control board system, which reports faults through a status LED (flash codes) on non-communicating models or through three-digit alert codes on iComfort-enabled systems. Elite Series furnaces range from 80% to 96% AFUE and include single-stage, two-stage, and variable-speed variants.

[Jump to Fix](#fix)

## Lennox Elite Series Flash Code / Alert Code Reference

| [Flash Code](https://www.amazon.com/s?k=Flash%20Code&tag=errorcodefixe-20) | Alert Code | Fault | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | --- |---|---|
| 2 flashes | [111](https://www.amazon.com/s?k=111&tag=errorcodefixe-20) | Pressure switch stuck open |
| [3 flashes](https://www.amazon.com/s?k=3%20flashes&tag=errorcodefixe-20) | 112 | Pressure switch stuck closed | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 4 flashes | 223 | [Open high-limit device](https://www.amazon.com/s?k=Open%20high-limit%20device&tag=errorcodefixe-20) |  | 5 flashes | [224](https://www.amazon.com/s?k=224&tag=errorcodefixe-20) | Rollout switch open |
| [6 flashes](https://www.amazon.com/s?k=6%20flashes&tag=errorcodefixe-20) | 225 | Flame not established at end of trial | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 7 flashes | 411 | [Ignition lockout — 3 retries failed](https://www.amazon.com/s?k=Ignition%20lockout%20%E2%80%94%203%20retries%20failed&tag=errorcodefixe-20) |  | 8 flashes | [412](https://www.amazon.com/s?k=412&tag=errorcodefixe-20) | Flame sensed without gas valve call |
| [9 flashes](https://www.amazon.com/s?k=9%20flashes&tag=errorcodefixe-20) | 414 | Low gas pressure | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 10 flashes | 431 | [Communication fault (iComfort)](https://www.amazon.com/s?k=Communication%20fault%20(iComfort)&tag=errorcodefixe-20) |  | 11 flashes | [432](https://www.amazon.com/s?k=432&tag=errorcodefixe-20) | Blower fault |
| [12 flashes](https://www.amazon.com/s?k=12%20flashes&tag=errorcodefixe-20) | 434 | Inducer motor fault | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Rapid | 540 | [Control board fault](https://www.amazon.com/s?k=Control%20board%20fault&tag=errorcodefixe-20) | ## Common Causes by Code

- **2 flashes / Alert 111 — Pressure switch open** — On 90%+ Elite models, check the condensate drain and the secondary heat exchanger for water blockage. On 80% models, check flue gas venting for obstruction. The inducer must run and create negative pressure before the pressure switch closes.
- **4 flashes / Alert 223 — High limit** — Restricted airflow is the primary cause. Lennox Elite Series blowers use either PSC or ECM motors — on ECM models, a failed motor module can reduce airflow even with no obvious symptom.
- **5 flashes / Alert 224 — Rollout switch** — This is a safety shutdown. The rollout switch trips when flames leave the burner box — caused by a blocked heat exchanger, cracked cell, or excessive gas pressure. Do not bypass. Find the root cause.
- **6/7 flashes / Alert 225/411 — Ignition failure** — SureLight HSI igniter, gas valve, and flame sensor are all in the diagnostic path. Check gas supply, manifold pressure (3.5" WC natural gas), and igniter resistance (40–70 Ω cold for silicon nitride).
- **11 flashes / Alert 432 — Blower fault** — ECM blower motor fault or failed hall-effect sensor connection. Also check the iComfort board's blower configuration parameters — a misconfigured airflow setting can cause the motor to run at wrong speed and trigger a fault.

## Step-by-Step Fix {#fix}

1. **Check the thermostat first** — On iComfort systems, the thermostat displays the alert code number (e.g., 223) with a description. Navigate to System > Alerts. Write down the active and historical codes.
2. **For pressure switch (2 flashes / Alert 111)** — Disconnect the pressure switch tubing and blow through it — it should be clear. Connect a manometer to the inducer outlet port and confirm the inducer creates at least -0.5" WC (the switch setpoint is labeled on the switch body).
3. **For limit (4 flashes / Alert 223)** — Replace the air filter. Run the furnace with the blower door removed and measure air temperature rise across the heat exchanger — should be between 35°F and 65°F (check the nameplate for the model-specific range).
4. **For rollout switch (5 flashes / Alert 224)** — Do not reset until the cause is identified. Inspect the heat exchanger for cracks using a flashlight through the burner ports. Also measure gas manifold pressure — should be 3.5" WC natural gas, not higher.
5. **For ignition failure (7 flashes / Alert 411)** — Watch the ignition sequence through the sight glass. Time the igniter warm-up (17–40 seconds depending on model). If the igniter glows and gas doesn't light, check gas valve operation with a voltmeter at the valve terminals (24VAC on call for heat).

## Parts Often Needed | Part | [Notes](https://www.amazon.com/s?k=Notes&tag=errorcodefixe-20) |  |---|---|
| SureLight igniter | [Silicon nitride; part number varies by model](https://www.amazon.com/s?k=Silicon%20nitride%3B%20part%20number%20varies%20by%20model&tag=errorcodefixe-20) |  | Flame sensor | [Clean with fine steel wool; measure µA output](https://www.amazon.com/s?k=Clean%20with%20fine%20steel%20wool%3B%20measure%20%C2%B5A%20output&tag=errorcodefixe-20) |  | Pressure switch | [Single or dual switch depending on model](https://www.amazon.com/s?k=Single%20or%20dual%20switch%20depending%20on%20model&tag=errorcodefixe-20) |  | ECM blower motor module | [Replace module only if motor spins freely](https://www.amazon.com/s?k=Replace%20module%20only%20if%20motor%20spins%20freely&tag=errorcodefixe-20) |  | High-limit switch | [Check reset button — some are auto-reset, some manual](https://www.amazon.com/s?k=Check%20reset%20button%20%E2%80%94%20some%20are%20auto-reset%2C%20some%20manual&tag=errorcodefixe-20) |  | Rollout switch | Manual-reset; do not bypass |

## When to Call a Pro

Lennox Elite Series furnaces with iComfort communicating systems require Lennox service tools for full diagnostics. Alert Code 540 (control board fault) and any code that returns after a verified repair should be evaluated by a Lennox Premier Dealer. Heat exchanger inspection for rollout switch trips requires camera inspection equipment and combustion analysis.
