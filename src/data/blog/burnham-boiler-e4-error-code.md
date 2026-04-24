---
title: "Burnham Boiler E4 Error Code — Flame Loss During Operation"
description: "Burnham boiler E4 error means the flame went out during operation. Learn the common causes — gas pressure, flame sensor, and draft — and how to fix it."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - burnham
  - boiler
  - hvac
  - error-code
  - flame-loss
---

## Burnham Boiler E4 Error — Flame Loss

**E4 on a Burnham boiler** means the **flame was established at startup but extinguished during operation** — this is called a "flame loss" or "nuisance lockout" condition. Unlike E2 (ignition failure where flame never established) or E1 (hard lockout), E4 means the burner lit successfully but then the flame dropped out while the boiler was running.

E4 appears on Burnham Alpine (ALP), K2, K2-Fibre, and Revolution series boilers.

## Why Flame Goes Out Mid-Operation

| Cause | Details |
|---|---|
| Low gas pressure | Pressure drops when other appliances draw gas simultaneously |
| Dirty flame sensor | Flame signal becomes too weak to sustain proven status |
| Draft fluctuations | Wind, pressure changes cause draft to momentarily drop |
| Gas valve flutter | Valve partially closing due to coil degradation |
| Air in gas line | Especially after gas service interruption |
| Blocked condensate | Builds up during operation, eventually stalls draft |
| Inducer motor degrading | Motor speed drops under thermal load |

## Why E4 Is Tricky

E4 is intermittent by nature — the boiler lights fine, runs for a while (5 minutes to 2 hours), then drops out. This makes it harder to catch than E1 or E2. Look for patterns:
- Does it happen when multiple gas appliances run? (Gas dryer + range + boiler = pressure drop)
- Does it happen during high wind? (Flue pressure disruption)
- Does it happen always at the same point in the heating cycle?
- Does it happen more in cold weather? (Condensate freezing)

## Step-by-Step Diagnosis

**Step 1 — Check the flame sensor signal strength.** Many Burnham Alpine controllers display the flame signal in microamps (µA) on the diagnostic menu. Navigate to: Menu → Service → Flame Signal. Normal is 2–5 µA. Below 1.5 µA, the board is likely to nuisance-trip during operation.

Clean the flame sensor rod with fine steel wool if below 2 µA. This is the most common fix for E4.

**Step 2 — Verify gas pressure under load.** Have a tech install a manometer at the gas valve inlet. Call for heat and watch pressure — it should hold at minimum 5" WC upstream (natural gas) throughout operation. If it drops when other appliances run, you need a larger gas line or regulator upgrade.

**Step 3 — Check condensate drain.** The drain may be clear at startup but accumulate during operation. Inspect the trap and condensate hoses while the boiler is running (carefully). Any gurgling or water bubbles back toward the inducer indicates a drain restriction.

**Step 4 — Check flue for wind effects.** If E4 happens on windy days, install a wind-resistant flue terminal. Most Alpine and K2 models use 2" or 3" PVC terminations — aftermarket wind-resistant terminals are available.

**Step 5 — Log fault history.** Burnham Alpine controllers maintain a fault history log (Menu → Service → Fault Log). Note the flame signal reading at the time of the E4 trip — if it shows a sudden drop to 0, it's a real flame-out. If it shows a gradual decline, it's sensor drift.

## Parts Reference

| Part | Cost |
|---|---|
| Flame sensor rod | $15–35 |
| Gas valve (Alpine) | $200–400 |
| Inducer motor | $150–350 |
| Condensate trap | $15–30 |
| Flue wind cap | $20–60 |

## Resetting E4

Press and hold the Reset button on the boiler control panel for 3 seconds. The boiler will attempt ignition again. If E4 returns within a short time, the underlying cause hasn't been addressed. More than 3 resets in 24 hours without repair = time for a service call.

## Related Burnham Error Codes

| Code | Meaning |
|---|---|
| E1 | Hard ignition lockout |
| E2 | Failed ignition attempt |
| E3 | High limit tripped |
| E4 | Flame loss during operation (this post) |
| E5 | Low water cutoff |
| E6 | Blocked flue fault |
