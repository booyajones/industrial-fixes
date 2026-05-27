---
title: "Carrier Error Code 56 — IFC Fault (Induced Draft Motor)"
description: "Carrier furnace fault code 56 points to a problem with the induced draft blower or its proving circuit. Here's how to diagnose and fix it."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - carrier
  - furnace
  - hvac
  - error-code
---

## Carrier Fault Code 56 — Induced Draft Motor Fault

Fault code 56 on a Carrier furnace indicates the **Integrated Furnace Control (IFC) board has detected a problem with the induced draft (ID) blower circuit**. The IFC expects the ID blower to reach speed and close its pressure switch before allowing ignition. If that sequence fails, code 56 is stored.

## What the IFC Is Checking

The induced draft blower (also called inducer or draft motor) pulls combustion gases through the heat exchanger and out the flue. The IFC monitors it via:

1. **Pressure switch** — a diaphragm switch that closes when draft is established
2. **Motor current feedback** — on some models
3. **Timing** — if pressure switch doesn't close within a set window, fault trips

## Common Causes of Code 56

| Cause | Likelihood |
|---|---|
| Blocked or frozen condensate drain | High |
| Cracked or disconnected pressure switch hose | High |
| Failed pressure switch | Medium |
| Inducer motor failed or seized | Medium |
| Blocked flue/intake pipe | Medium |
| Faulty IFC board | Low |

## Step-by-Step Diagnosis

**Step 1 — Check the condensate drain.** On high-efficiency furnaces (90%+), condensate backs up and can block the pressure switch port or drown the inducer housing. Disconnect the drain at the trap and blow it clear.

**Step 2 — Inspect pressure switch hoses.** Trace the small rubber hoses from the inducer housing to the pressure switch. Look for cracks, kinks, or disconnected ends. Replace any damaged hose with 3/16" ID tubing.

**Step 3 — Test the pressure switch.** With power off, use a multimeter on continuity. The switch should be open at rest and close when you apply suction to the port (use a vacuum gauge or carefully blow on the port). A switch that doesn't close under suction is failed — replace it.

**Step 4 — Spin the inducer motor.** With power off, reach in and spin the inducer wheel by hand. It should spin freely. A seized or stiff bearing will prevent the motor from reaching draft pressure.

**Step 5 — Check the flue and intake pipes.** Go outside and inspect both PVC pipes (on 90%+ efficiency) or the single metal flue (80%). Bird nests, ice, or debris will block draft entirely.

## Parts to Have Ready

| Part | Cost Estimate |
|---|---|
| Pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-carrier-56-error-code&tag=errorcodefixes-20) \| $25–60 |
| Pressure switch hose kit | [Amazon](https://www.amazon.com/dp/B0CPTHML1N?ascsubtag=ecf-carrier-56-error-code&tag=errorcodefixes-20) \| $5–15 |
| Inducer motor assembly | [Amazon](https://www.amazon.com/dp/B00FDZ90B2?ascsubtag=ecf-carrier-56-error-code&tag=errorcodefixes-20) \| $150–350 |
| IFC board (last resort) | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-carrier-56-error-code&tag=errorcodefixes-20) \| $100–300 |
## Pro Tip

Before replacing anything, cycle the thermostat off and back on. Watch the inducer: it should spin up immediately when the call for heat starts. If it doesn't spin at all, the motor is failed or the IFC isn't outputting voltage to it. Use a multimeter to check voltage at the inducer motor terminals during startup — if you see 120V and the motor doesn't spin, it's the motor. If you see 0V, suspect the IFC or a safety interlock upstream.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)

## See Also

- [Carrier 43 Error Code — Rollout Switch Open Fix](/posts/carrier-43-error-code/)
- [Carrier 24ACC6 Heat Pump Error Codes: Complete Diagnostic Guide](/posts/carrier-24acc6-heat-pump-error-codes/)
- [Carrier Zone Controller Error Codes — Complete Guide](/posts/carrier-zone-controller-error-codes/)
- [Carrier 52 Error Code — Causes & Fix](/posts/carrier-52-error-code/)
