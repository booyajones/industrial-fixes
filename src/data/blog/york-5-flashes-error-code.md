---
title: "York 5 Flashes Error Code — Causes & Fix"
description: "What York 5 flashes means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T08:00:00Z
modDatetime: 2026-04-22T08:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - york
---

## York 5 Flashes Error Code — What It Means

Five flashes on a York furnace LED means a flame sense fault — the furnace ignited (or attempted to ignite) but the control board lost flame signal before the heating cycle should have ended, or never detected adequate flame current despite ignition. The board requires a microamp current through the flame sensor rod to confirm combustion. When this signal drops below threshold, the board closes the gas valve and counts an attempt. After multiple failed attempts, it locks out. This code is a direct indicator to inspect the flame sensor and verify gas pressure.

[Jump to Fix](#fix)

## Common Causes

- **Oxidized flame sensor rod** — The most frequent cause. The stainless rod develops a non-conductive oxide layer that prevents the small flame rectification current from flowing, even when the burner is lit.
- **Flame sensor positioned incorrectly** — If the rod isn't sitting in the main burner flame envelope, it won't see enough ionization current. This can happen if the sensor bracket was bent during a previous service.
- **Marginal gas pressure** — Low manifold pressure produces a thin, lazy flame that provides insufficient ionization. Check manifold pressure with a manometer.
- **Cracked sensor insulator** — A cracked ceramic around the sensor rod allows current to leak to ground. The board sees a low or intermittent signal and closes the gas valve.

## Step-by-Step Fix {#fix}

1. **Remove and clean the flame sensor** — Single screw, single wire. Pull the rod and lightly sand it with 400-grit sandpaper or fine steel wool until bare metal shows. Do not touch the rod with your fingers after cleaning.
2. **Inspect sensor position** — Reinstall and confirm the rod tip sits inside the burner flame. If the bracket is bent outward, carefully bend it back until the rod is roughly 1/2 inch into the flame envelope.
3. **Check the ceramic insulator** — Hold the sensor up to a light. Any crack in the white ceramic means replace it — cleaning won't help.
4. **Verify gas pressure if possible** — If you have a manometer, check manifold pressure during operation. Natural gas should be 3.2–3.8" WC; LP 10–11" WC.
5. **Reset the system** — Power cycle and observe two complete heating cycles. If no 5-flash fault, the sensor fix resolved it.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame sensor | [Amazon](https://www.amazon.com/s?k=Flame+sensor&tag=errorcodefixes-20) \| Match York OEM; universal versions also work |
| Sandpaper (400-grit) or steel wool | [Amazon](https://www.amazon.com/s?k=Sandpaper+%28400-grit%29+or+steel+wool&tag=errorcodefixes-20) \| For sensor cleaning |
| Gas valve | [Amazon](https://www.amazon.com/s?k=Gas+valve&tag=errorcodefixes-20) \| Replace only after confirming correct voltage at valve terminals with no output |
## When to Call a Pro

If the sensor is clean and correctly positioned but the fault persists, gas valve or combustion diagnosis requires a licensed tech. Adjusting gas pressure requires a manometer and gas certification.
