---
title: "Carrier 34 Error Code — Ignition Proving Failure Fix"
author: "Marcus Webb"
pubDatetime: 2024-03-01T08:00:00Z
modDatetime: 2024-03-01T08:00:00Z
slug: carrier-34-error-code
featured: true
draft: false
tags:
  - hvac
  - carrier
  - furnace
  - ignition
description: "Carrier error code 34 means ignition proving failure — the furnace tried to light but couldn't confirm a flame. Here's how to diagnose and fix it fast."
---

## Error Code: Carrier 34

**What it means:** The furnace attempted ignition, opened the gas valve, but the flame sensor never confirmed a flame was present. The control board tried (typically 3 times) and then locked out. Code 3-4 on the LED diagnostic sequence means the igniter fired, gas was called for, but no flame signal was received within the proving period (usually 4–7 seconds).

## Common Causes

- **Dirty or failed flame sensor** — The #1 cause. Carbon buildup on the sensor rod insulates it and prevents the microamp signal from reaching the control board.
- **Weak or failed hot surface igniter (HSI)** — The igniter may glow but not reach the 1800°F+ needed to light natural gas. Older igniters degrade over 3–5 years.
- **Gas supply issue** — Low gas pressure, closed manual shutoff valve, or a tripped gas meter regulator can prevent ignition even when the igniter works perfectly.
- **Cracked heat exchanger causing flame rollout** — A cracked exchanger disrupts the flame pattern, preventing the sensor from reading a stable flame.
- **Control board or flame sensor wiring fault** — Loose connector at the flame sensor or a failing board that can't read the microamp signal correctly.

## Step-by-Step Fix {#step-by-step-fix}

1. **Kill power and gas to the furnace.** Flip the disconnect switch and turn the gas shutoff to the OFF position. Wait 5 minutes for any residual gas to clear before opening the cabinet.

2. **Locate and remove the flame sensor.** It's a metal rod with a ceramic insulator mounted near the burner assembly, with a single wire connector. Remove the 1/4" hex screw holding it and pull it out.

3. **Clean the flame sensor rod.** Use fine steel wool or a green Scotch-Brite pad to lightly abrade the metal rod — remove any grey or white oxide buildup. Do not use sandpaper (too aggressive) or touch the cleaned rod with bare hands (oils re-contaminate it). Reinstall and tighten.

4. **Check the hot surface igniter for cracks.** With power off, visually inspect the igniter element. Any crack or break means replacement — do not attempt to run a cracked igniter. If it's intact, use a multimeter to measure resistance: a healthy Norton 271N-style igniter reads 40–90 ohms at room temperature.

5. **Verify gas pressure at the manifold.** With a manometer, check manifold gas pressure during a call for heat. Natural gas should read 3.2–3.7" W.C.; LP should read 10–11" W.C. If pressure is low, check the shutoff valve position, then call the gas utility.

6. **Watch the ignition sequence live.** Restore power and gas. Initiate a heat call and watch through the sight glass. You should see the igniter glow orange-hot within 30–60 seconds, then gas should light within 4 seconds of the valve opening. If the igniter glows but gas doesn't light, the gas valve or pressure is suspect. If neither glows nor lights, check igniter wiring continuity.

7. **Measure the flame sensor signal during operation.** With the furnace running, set a multimeter to DC microamps, interrupt the flame sensor wire, and measure in series. A healthy reading is 1.5–4.0 µA. Below 0.5 µA, replace the sensor regardless of visual cleanliness.

8. **Clear the lockout and test.** After any repair, restore power, cycle the thermostat, and watch 2–3 full ignition cycles to confirm the fault doesn't return.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Where to Buy | Typical Cost |
|------|-------------|-------------|
| Flame sensor rod (universal, replaces OEM) | [Amazon](https://www.amazon.com/s?k=Flame+sensor+rod+%28universal%2C+replaces+OEM%29&tag=errorcodefixes-20) \| Carrier dealer, Johnstone Supply, Grainger | $8–$20 |
| Hot surface igniter — Carrier/Bryant OEM (Part #LH33ZS004) | [Amazon](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-carrier-34-error-code&tag=errorcodefixes-20) \| Carrier dealer, HVAC Supply Outlet | $30–$65 |
| Gas valve — White-Rodgers 36E (common Carrier app) | [Amazon](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-carrier-34-error-code&tag=errorcodefixes-20) \| Johnstone Supply, Wittichen Supply | $80–$180 |
| Carrier control board (Part #HK42FZ series) | [Amazon](https://www.amazon.com/s?k=Carrier+control+board+%28Part+%23HK42FZ+series%29&tag=errorcodefixes-20) \| Carrier OEM parts dealer | $150–$300 |
## When to Call a Professional

If you've cleaned the flame sensor, confirmed igniter resistance, and verified gas pressure but the fault persists, you're likely dealing with a cracked heat exchanger or a failing control board. A cracked heat exchanger is a carbon monoxide safety hazard — do not run the furnace. Tell your tech: "I've already cleaned the flame sensor and checked gas pressure. I'm getting code 3-4 and the flame sensor reads under 0.5 microamps even on a clean rod. I want you to check the heat exchanger and the board."

> **Pro tip:** Always check gas pressure *at the manifold* during operation, not just at the meter. A perfectly good gas supply can show low manifold pressure if the combination gas valve regulator is failing — and replacing the flame sensor won't fix that.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)

## See Also

- [Carrier Mini-Split F0 Error Code — Low Refrigerant / Leakage Detection Fix](/posts/carrier-mini-split-f0-error-code/)
- [Carrier Mini-Split P4 Error Code — Inverter Module Overtemperature Fix](/posts/carrier-mini-split-p4-error-code/)
- [Carrier 43 Error Code — Rollout Switch Open Fix](/posts/carrier-43-error-code/)
- [Carrier 33 Error Code — Causes & Fix](/posts/carrier-33-error-code/)
