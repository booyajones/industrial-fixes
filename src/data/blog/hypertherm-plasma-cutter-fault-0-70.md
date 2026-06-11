---
title: "Hypertherm Plasma Cutter Fault 0-70 — Causes & Fix"
description: "What Hypertherm fault code 0-70 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - welding
  - hypertherm
money_part: "Input capacitor bank"
---

## Hypertherm Plasma Cutter Fault 0-70 — What It Means

Fault 0-70 on Hypertherm Powermax plasma cutters indicates a DC bus undervoltage — the internal DC bus voltage dropped below the minimum threshold required for safe operation. The inverter cannot fire the pilot arc without adequate DC bus voltage, so the machine shuts down to protect the power electronics. This fault can appear on startup or mid-cut.

[Jump to Fix](#fix)

## Common Causes

- **Low input voltage** — If the incoming line voltage is below spec (Powermax units typically need 200–240V single-phase or 200–480V three-phase depending on model), the DC bus can't charge to the required level.
- **Long or undersized extension cord** — Voltage drop under the high inrush current of plasma startup causes the bus to undervolt before the arc fires.
- **Weak or failing power factor correction (PFC) circuit** — The internal PFC stage that boosts and regulates the DC bus can degrade, causing undervoltage even with correct input voltage.
- **Input filter capacitor degradation** — The electrolytic capacitors in the input filter stage lose capacitance with age and heat, reducing their ability to sustain bus voltage.

## Step-by-Step Fix {#fix}

1. **Measure input voltage at the machine** — Use a multimeter at the input plug or terminals while the machine is running. Compare to the nameplate spec. Voltage sagging more than 10% under load indicates a supply problem.
2. **Eliminate extension cords** — Plug directly into a properly rated outlet. If you must use an extension, use minimum 10 AWG for 30-amp circuits and keep the run under 25 feet.
3. **Verify the circuit breaker rating** — The branch circuit breaker must match the machine's input amperage requirements. An undersized breaker causes voltage drop under load.
4. **Power cycle the machine** — If the fault was caused by a momentary voltage sag, power cycling will clear it. If it returns consistently, the internal PFC or capacitor circuit needs evaluation.
5. **Contact Hypertherm service** — If input voltage is confirmed correct and the fault persists, the PFC module or input capacitors have failed. Hypertherm authorized service is needed.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input capacitor bank | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-hypertherm-plasma-cutter-fault-0-70&k=Input+capacitor+bank&tag=errorcodefixes-20) \| Degrades with age; requires authorized service to replace |
| PFC module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-hypertherm-plasma-cutter-fault-0-70&k=PFC+module&tag=errorcodefixes-20) \| Fails on heavily used machines; authorized service only |
| Input power cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-hypertherm-plasma-cutter-fault-0-70&k=Input+power+cable&tag=errorcodefixes-20) \| Replace if cord is damaged or plug is corroded |
## When to Call a Pro

DC bus and PFC circuit repair requires working inside the power supply with capacitors that hold charge even after power is removed. This is authorized-service-only territory — do not open the machine yourself to address 0-70.
