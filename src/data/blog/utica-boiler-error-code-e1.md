---
title: "Utica Boiler Error Code E1 — Causes & Fix"
description: "What Utica boiler error code E1 means, why ignition fails, and how to fix it step by step."
pubDatetime: 2026-04-22T15:00:00Z
modDatetime: 2026-04-22T15:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - boiler
  - utica
---

## Utica Boiler Error Code E1 — What It Means

E1 on a Utica boiler (UB, UBCH, or Combi series) indicates an ignition failure lockout. Utica Boilers (a brand of ECR International, which also makes Dunkirk and Pennco equipment) uses a Honeywell or Fenwall ignition control module. The E1 code fires when the module does not confirm a flame within the trial-for-ignition period. The burner is locked out for safety. The most common causes are gas supply problems, a contaminated flame sensor, or a failed igniter.

[Jump to Fix](#fix)

## Common Causes

- **Dirty flame sensor rod** — A thin layer of oxidation on the flame sensor prevents it from conducting the microamp signal back to the control module, causing it to abort ignition even when the burner briefly lights.
- **Failed hot surface igniter or spark electrode** — Depending on the Utica model, ignition is via a hot surface igniter (HSI) or a spark electrode. A cracked HSI or a worn spark electrode cannot reliably ignite the gas-air mixture.
- **Gas valve not opening** — The gas valve solenoid may fail or the operator may not receive the 24VAC command, resulting in no gas flow during the ignition trial.
- **Low gas pressure** — Gas pressure below the rated inlet pressure (typically 7" WC natural gas) results in a lean mixture that ignites poorly or not at all.

## Step-by-Step Fix {#fix}

1. **Reset the E1 lockout** — Press the reset button on the ignition module (usually red or labeled RESET) or cycle power for 30 seconds.
2. **Observe the startup sequence** — Run a heat call and watch through the sight glass: inducer on → igniter glow or spark → burner light → flame confirmation. Note where the sequence fails.
3. **Clean the flame sensor** — Remove the sensor rod and polish the tip with fine steel wool. Reinstall and retry.
4. **Test the hot surface igniter** — Measure resistance across the HSI leads: 40–200 Ω is serviceable; open circuit means it is failed. Replace with the Utica OEM igniter or an approved cross-reference.
5. **Test spark electrode (if applicable)** — Verify electrode gap is within spec (typically 1/8") and the ceramic is not cracked. Replace if damaged.
6. **Verify gas supply** — Confirm all manual shutoffs upstream of the boiler are open. Test gas pressure at the valve inlet with a manometer.
7. **Restore and run a full cycle** — After repairs, cycle power and run a complete heating call, confirming no recurrence of E1.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame sensor rod | [Amazon](https://www.amazon.com/dp/B0CZ7M9V4D?ascsubtag=ecf-utica-boiler-error-code-e1&tag=errorcodefixes-20) \| Utica/ECR OEM or universal replacement with matching tip geometry |
| Hot surface igniter | [Amazon](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-utica-boiler-error-code-e1&tag=errorcodefixes-20) \| Match wattage and mounting style for the Utica model |
| Gas valve | [Amazon](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-utica-boiler-error-code-e1&tag=errorcodefixes-20) \| Replace only after confirming correct 24VAC input and no gas output |
## When to Call a Pro

If E1 persists after cleaning the flame sensor and verifying gas supply, a technician should measure gas inlet and manifold pressure and inspect the heat exchanger for cracks. Heat exchanger failures cause combustion instability that mimics a flame sensor fault.

## Related Articles

- [Boiler Lockout Error Codes: All Brands Guide](/posts/boiler-lockout-error-codes/)
- [Buderus Boiler Fault Code A1 — Causes & Fix](/posts/buderus-boiler-fault-code-a1/)
- [Burnham Alpine Boiler Error Code Guide — Causes & Fix](/posts/burnham-alpine-error-codes/)
- [Burnham Boiler E1 Lockout Code Fix](/posts/burnham-boiler-e1-lockout-code/)
- [Burnham Boiler E2 Error Code — Causes & Fix](/posts/burnham-boiler-e2-error-code/)
