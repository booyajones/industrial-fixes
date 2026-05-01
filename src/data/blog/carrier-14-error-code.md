---
title: "Carrier 14 Error Code — Causes & Fix"
description: "What Carrier error code 14 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - carrier
---

## Carrier 14 Error Code — What It Means

Carrier fault code 14 is an ignition lockout. After exhausting the allowed ignition attempts (typically 3–5 trials depending on the board revision), the control board locks out the ignition circuit entirely and requires a manual reset. Code 14 is downstream of code 11 — the board tried, failed repeatedly, and now refuses to try again. This is a safety interlock, not a separate component failure. The root cause is almost always the same set of ignition-related faults: bad igniter, dirty flame sensor, gas supply issue, or a failed inducer not establishing draft.

[Jump to Fix](#fix)

## Common Causes

- **Repeated ignition failure (code 11 escalated)** — The most common path: code 11 fires multiple times and the board escalates to a hard lockout (code 14) after exhausting retries.
- **Draft inducer fault** — If the inducer motor is weak or failing, negative pressure in the heat exchanger is insufficient to open the pressure switch, which blocks the ignition sequence before the igniter even fires.
- **Control board lockout logic** — Some Carrier boards require a 3-hour auto-reset or a manual power cycle to clear code 14. Verify which lockout type applies to your model.
- **Wiring fault to igniter circuit** — A loose molex connector or burnt wire on the igniter harness can cause intermittent failures that accumulate into a lockout.

## Step-by-Step Fix {#fix}

1. **Manually reset the lockout** — Cut power at the furnace disconnect or breaker for 30 seconds, then restore. Some boards also have a reset button on the board itself. This clears the lockout counter; if the root cause is not fixed, it will lock out again.
2. **Work through code 11 diagnostics** — Inspect the hot surface igniter (resistance check), clean the flame sensor, and confirm gas supply. See the Carrier 11 error code guide for full detail.
3. **Check the draft inducer** — Start a call for heat and listen: the inducer should spin up before the igniter glows. If it doesn't start, or if it runs slowly, check the inducer motor and pressure switch.
4. **Inspect wiring at the igniter connector** — Pull the molex connector at the igniter and check for melted insulation, pushed-back pins, or corrosion. Reseat firmly.
5. **Reset the system and monitor** — After correcting the root cause, restore power and run through a complete heat cycle. Confirm no fault LEDs after ignition.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hot surface igniter | [Amazon](https://www.amazon.com/dp/B00BTLLJ40?tag=errorcodefixes-20) \| Most common root cause leading to lockout |
| Draft inducer motor | [Amazon](https://www.amazon.com/dp/B00FDZ90B2?tag=errorcodefixes-20) \| Replace if motor is noisy, slow, or fails to start |
| Flame sensor | [Amazon](https://www.amazon.com/dp/B0CZ7M9V4D?tag=errorcodefixes-20) \| Inexpensive; replace if cleaning doesn't restore signal |
## When to Call a Pro

If the furnace locks out again within the first heat cycle after reset, or if you suspect a cracked heat exchanger or failed gas valve, contact a licensed HVAC technician. Repeated lockouts without a clear component failure can indicate combustion or venting problems.

## See Also

- [Carrier Furnace E1 Error Code — Causes & Fix](/posts/carrier-furnace-error-code-e1/)
- [Carrier 34 Error Code — Ignition Proving Failure Fix](/posts/carrier-34-error-code/)
- [Carrier Error Code 58 — Causes & Fix](/posts/carrier-58-error-code/)
- [Carrier Error Code 56 — IFC Fault (Induced Draft Motor)](/posts/carrier-56-error-code/)

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 21 Error Code — Gas Heating Lockout Fix](/posts/carrier-21-error-code/)
