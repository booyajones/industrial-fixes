---
title: "Lennox Elite Series Furnace Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to Lennox Elite Series furnace error codes, LED flash sequences, alert codes, common fault causes, and step-by-step repair procedures."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - lennox
  - furnace
money_part: "SureLight igniter"
---

## Lennox Elite Series Furnace Error Codes — What They Mean

The Lennox Elite Series includes several residential gas furnace models: the EL195E, EL180E, EL296V, and G61MPV among others. These furnaces use Lennox's SureLight control board system, which reports faults through a status LED (flash codes) on non-communicating models or through three-digit alert codes on iComfort-enabled systems. Elite Series furnaces range from 80% to 96% AFUE and include single-stage, two-stage, and variable-speed variants.

[Jump to Fix](#fix)

## Lennox Elite Series Flash Code / Alert Code Reference

| Flash Code | Alert Code | Fault |
|---|---|---|
| 2 flashes | 111 | Pressure switch stuck open |
| 3 flashes | 112 | Pressure switch stuck closed |
| 4 flashes | 223 | Open high-limit device |
| 5 flashes | 224 | Rollout switch open |
| 6 flashes | 225 | Flame not established at end of trial |
| 7 flashes | 411 | Ignition lockout — 3 retries failed |
| 8 flashes | 412 | Flame sensed without gas valve call |
| 9 flashes | 414 | Low gas pressure |
| 10 flashes | 431 | Communication fault (iComfort) |
| 11 flashes | 432 | Blower fault |
| 12 flashes | 434 | Inducer motor fault |
| Rapid | 540 | Control board fault |

## Common Causes by Code

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

## Parts Often Needed

| Part | Notes |
|---|---|
| SureLight igniter | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lennox-elite-series-furnace-codes&k=SureLight+igniter&tag=errorcodefixes-20) \| Silicon nitride; part number varies by model |
| Flame sensor | [Amazon](https://www.amazon.com/s?k=Flame+sensor&tag=errorcodefixes-20) \| Clean with fine steel wool; measure µA output |
| Pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-lennox-elite-series-furnace-codes&tag=errorcodefixes-20) \| Single or dual switch depending on model |
| ECM blower motor module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lennox-elite-series-furnace-codes&k=ECM+blower+motor+module&tag=errorcodefixes-20) \| Replace module only if motor spins freely |
| High-limit switch | [Amazon](https://www.amazon.com/dp/B0BN3TRG9R?ascsubtag=ecf-lennox-elite-series-furnace-codes&tag=errorcodefixes-20) \| Check reset button — some are auto-reset, some manual |
| Rollout switch | [Amazon](https://www.amazon.com/dp/B0BN3TRG9R?ascsubtag=ecf-lennox-elite-series-furnace-codes&tag=errorcodefixes-20) \| Manual-reset; do not bypass |
## When to Call a Pro

Lennox Elite Series furnaces with iComfort communicating systems require Lennox service tools for full diagnostics. Alert Code 540 (control board fault) and any code that returns after a verified repair should be evaluated by a Lennox Premier Dealer. Heat exchanger inspection for rollout switch trips requires camera inspection equipment and combustion analysis.

## See Also

- [Lennox Error Code 540 — Causes & Fix](/posts/lennox-error-code-540/)
- [Lennox Harmony III Zoning System Error Codes — Complete Guide](/posts/lennox-harmony-iii-error-codes/)
- [Lennox Error Code 231 — Causes & Fix](/posts/lennox-error-code-231/)
- [Lennox Error Code 111 — Causes & Fix](/posts/lennox-error-code-111/)

## Related Articles

- [Lennox Error Code 292 — Ignition Failure Fix](/posts/lennox-292-error-code/)
- [Lennox EL296V Error Codes — Variable-Speed Furnace Diagnostic Guide](/posts/lennox-el296v-error-codes/)
- [Lennox 103 Error Code — Causes & Fix](/posts/lennox-error-code-103/)
- [Lennox Error Code 111 — Causes & Fix](/posts/lennox-error-code-111/)
- [Lennox Error Code 114 — Causes & Fix](/posts/lennox-error-code-114/)
