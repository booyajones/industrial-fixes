---
title: "Navien E002 Error Code — Causes & Fix"
description: "What Navien E002 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T08:00:00Z
modDatetime: 2026-04-22T08:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - boiler
  - navien
---

## Navien E002 Error Code — What It Means

Navien error code E002 means ignition failure — the unit attempted to ignite the burner but could not establish a stable flame within the trial period. Navien tankless water heaters and boilers try to ignite 3 times before locking out with E002. Each ignition attempt involves spark, gas valve opening, and flame confirmation via ionization. If any part of this chain fails — no spark, no gas, or no ionization signal — the attempt fails and the board counts it. After 3 failures, E002 locks the unit until manually reset.

[Jump to Fix](#fix)

## Common Causes

- **Gas supply issue** — If the gas meter, regulator, or manual shutoff isn't fully delivering gas, the burner won't ignite. This is especially common after utility work, extended shutoffs, or in cold weather when regulators can freeze.
- **Dirty or failed igniter** — The spark electrode can carbon-foul or crack with age. A fouled igniter produces a weak or no spark. Electrode gap should be approximately 3–4mm.
- **Clogged burner** — A dirty burner from mineral deposits or debris produces a weak, unstable flame that doesn't confirm on the ionization sensor and triggers an E002 lockout.
- **Venting blockage** — Even if the burner would light, if the fan-pressure-proving circuit doesn't close first, ignition is never attempted and the board logs it as an ignition failure.

## Step-by-Step Fix {#fix}

1. **Check gas supply** — Verify the manual gas shutoff at the unit is fully open (handle parallel to pipe). If gas was off recently, open a nearby hot water faucet and hold for 30 seconds to purge air from the line, then retry.
2. **Reset the unit** — Press and hold the Reset button for 3 seconds. Watch the ignition attempt: listen for the fan to start, then the spark sound (rapid clicking), then the burner flame igniting.
3. **Inspect the igniter electrode** — Access the burner compartment (service panel). Look at the spark electrode. Clean carbon deposits with fine sandpaper. Confirm the 3–4mm gap from the electrode tip to the burner surface.
4. **Inspect the vent system** — Check for blocked intake or exhaust at the termination outside. A blocked vent prevents the fan pressure switch from proving and halts ignition.
5. **Reset the system** — After clearing the root cause, press Reset and run a hot water draw. The unit should ignite within the first attempt.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Igniter/electrode assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-error-code-e002&k=Igniter%2Felectrode+assembly&tag=errorcodefixes-20) \| Navien 30004277A (NCB series) or model-specific — verify |
| Gas valve | [Amazon](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-navien-error-code-e002&tag=errorcodefixes-20) \| Replace only if confirmed — 24V at valve terminals, no gas output |
| Fan pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-navien-error-code-e002&tag=errorcodefixes-20) \| Test if fan runs but E002 persists without ignition attempt |
## When to Call a Pro

Gas valve diagnosis and adjustment requires a licensed gas tech. If the igniter is clean and gas is confirmed available but E002 persists, a tech should check gas manifold pressure and valve operation.

## Related Articles

- [Navien Error Code E001 — No Ignition Fix](/posts/navien-error-code-e001/)
- [Navien Error Code E003 — Ignition Failure Fix](/posts/navien-error-code-e003-ignition-failure/)
- [Navien Error Code E004 — Causes & Fix](/posts/navien-error-code-e004/)
- [Navien E006 Error Code — Causes & Fix](/posts/navien-error-code-e006/)
- [Navien Error Code E007 — Causes & Fix](/posts/navien-error-code-e007/)

## See Also

- [Navien E302 Error Code — Causes & Fix](/posts/navien-error-code-e302/)
- [Navien Error Code E021 — Cold Water Inlet Thermistor Fault Fix](/posts/navien-error-code-e021/)
- [Navien NFC Combi Boiler Error Codes: Complete Guide](/posts/navien-nfc-error-codes/)
- [Navien Error Code E003 — Ignition Failure Fix](/posts/navien-error-code-e003-ignition-failure/)
