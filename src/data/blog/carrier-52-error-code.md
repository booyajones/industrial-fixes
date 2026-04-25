---
title: "Carrier 52 Error Code — Causes & Fix"
description: "What Carrier error code 52 means, why the high limit trips into soft lockout, and how to fix it step by step."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - carrier
---

## Carrier 52 Error Code — What It Means

Carrier code 52 is a **soft lockout due to repeated high-limit trips**. The furnace tripped the high-limit switch multiple times within a short period, and the control board entered a soft lockout to protect the heat exchanger from thermal stress. Unlike a hard lockout, a soft lockout will auto-reset after a timed wait (typically 1 hour), but the root cause must be fixed or it will return. The LED shows 5 long flashes followed by 2 short.

[Jump to Fix](#fix)

## Common Causes

- **Restricted airflow** — Dirty air filter is the single most common cause; reduced airflow causes heat to build up past the limit threshold.
- **Blocked supply or return registers** — Closed vents or furniture blocking return air reduces airflow even with a clean filter.
- **Failed blower motor or capacitor** — Blower runs slow or not at all; heat piles up in the heat exchanger and trips the limit.
- **High-limit switch failing closed/open** — A weakened limit switch may trip at lower-than-spec temperatures, causing nuisance lockouts without true overheating.

## Step-by-Step Fix {#fix}

1. **Replace the air filter** — Check the filter first. If it's heavily loaded, replace it and allow the furnace to auto-reset after the lockout timer expires (up to 1 hour).
2. **Walk all registers** — Confirm all supply and return registers are open and unobstructed. Check for furniture, rugs, or debris blocking returns.
3. **Test the blower** — Set the thermostat to Fan-On. The blower should run continuously and feel strong at registers. Weak airflow points to a bad capacitor or failing motor.
4. **Check the run capacitor** — Measure capacitance with a capacitor tester. A capacitor reading 10–20% below rating will cause the blower to run under-speed.
5. **Inspect the high-limit switch** — With power off, check continuity across the limit switch terminals with a multimeter. It should be closed (continuous) at room temperature. An open reading at room temp means a failed switch.
6. **Reset the system** — After repairs, power the furnace off for 30 seconds, then restore. Call for heat and confirm the blower comes on promptly and runs at full speed.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Blower run capacitor | [Amazon](https://www.amazon.com/s?k=Blower+run+capacitor&tag=errorcodefixes-20) \| Match µF and VAC rating exactly; typically 5–10 µF on most Carrier units |
| High-limit switch | [Amazon](https://www.amazon.com/s?k=High-limit+switch&tag=errorcodefixes-20) \| Order by temperature rating (e.g., 160°F or 200°F) printed on the old switch |
| Air filter | [Amazon](https://www.amazon.com/s?k=Air+filter&tag=errorcodefixes-20) \| 1" or 4" media filter — replace every 1–3 months depending on load |
## When to Call a Pro

If the blower runs strong, airflow is unrestricted, and the furnace still trips the limit repeatedly, suspect a cracked heat exchanger allowing combustion gases to recirculate. This is a carbon monoxide hazard — shut the unit off and call a licensed HVAC technician immediately.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)
