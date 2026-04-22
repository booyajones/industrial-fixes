---
title: "Crown Boiler E1 Error Code — Lockout Guide"
description: "Crown Boiler E1 error means an ignition lockout. This guide covers Crown Bimini, Aruba, and Sentinel boiler E1 diagnosis, reset, and common causes."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - crown-boiler
  - boiler
  - hvac
  - error-code
  - lockout
---

## Crown Boiler E1 Error — Ignition Lockout

**E1 on a Crown boiler** indicates an **ignition lockout** — the boiler attempted to light and failed after the allowed number of tries. The burner will not attempt to relight until the fault is manually reset.

E1 appears on Crown Bimini (BIMINI), Aruba (ARUBA), and Sentinel (PHNTM) condensing boilers, as well as some legacy Cast Iron models with digital controls.

## What Causes E1

| [Root Cause](https://www.amazon.com/s?k=Root%20Cause&tag=errorcodefixe-20) | Signs |
|---|---|
| [No gas supply](https://www.amazon.com/s?k=No%20gas%20supply&tag=errorcodefixe-20) | No click/no smell during startup |
| [Failed igniter](https://www.amazon.com/s?k=Failed%20igniter&tag=errorcodefixe-20) | No spark or no glow (check through view port) |
| [Failed flame sensor](https://www.amazon.com/s?k=Failed%20flame%20sensor&tag=errorcodefixe-20) | Flame lights, then immediately shuts off |
| [Blocked condensate drain](https://www.amazon.com/s?k=Blocked%20condensate%20drain&tag=errorcodefixe-20) | Boiler attempts ignition but draft fault intervenes |
| [Low gas pressure](https://www.amazon.com/s?k=Low%20gas%20pressure&tag=errorcodefixe-20) | Flame lights weakly, then drops out |
| [Dirty burner](https://www.amazon.com/s?k=Dirty%20burner&tag=errorcodefixe-20) | Delayed ignition, weak flame signal |
| [Control board failure](https://www.amazon.com/s?k=Control%20board%20failure&tag=errorcodefixe-20) | Random lockout with no clear cause |

## How to Reset E1 on Crown Boilers

### Bimini / Aruba / Sentinel (Condensing)

1. Locate the control board — usually behind the front panel
2. Press and hold the **RESET** button (may be labeled RST or marked with ↺ symbol) for 3 seconds
3. The display will clear
4. The boiler starts an ignition sequence within 30 seconds — watch and listen

### Older Cast Iron Models

If you have an older Crown with a Beckett or similar oil burner (rare on gas models), the reset button may be a red button on the primary control (R7184 or similar). Press once firmly.

## Watching the Startup Sequence

When you reset E1, observe carefully:

1. **Inducer fan** — should spin up immediately. Listen for airflow.
2. **Spark** — you may hear clicks (spark ignition) or see a glow through the observation port (hot surface igniter).
3. **Gas valve** — you may hear a faint click when it opens.
4. **Flame** — should appear within 4–7 seconds of igniter energizing.
5. **Stable operation** — after flame is proven, the boiler should run quietly.

If the igniter activates but no flame appears: gas supply issue or gas valve issue.  
If flame appears then immediately shuts off: flame sensor issue.  
If no igniter activity at all: igniter circuit, control board, or inducer/draft fault preventing startup.

## Crown Bimini/Aruba Service Menu

Press and hold the INFO button for 5 seconds to access diagnostic info. This shows:
- Current fault code
- Fault history
- Flame signal (µA reading)
- Sensor temperatures

The flame signal reading is especially useful — below 1.5 µA means a dirty or failed flame sensor.

## Condensate System Check (High Priority on E1)

Crown condensing boilers won't attempt ignition if the condensate drain is flooded, because the draft pressure switch can't close. Check:
- Condensate trap: disconnect, blow clear
- Drain line: must slope continuously to floor drain, no traps or low points
- Freeze protection: in cold spaces, drain lines can freeze solid

## Parts Reference

| Part | Cost |
|---|---|
| [Hot surface igniter](https://www.amazon.com/s?k=Hot%20surface%20igniter&tag=errorcodefixe-20) | $30–80 |
| [Flame sensor](https://www.amazon.com/s?k=Flame%20sensor&tag=errorcodefixe-20) | $15–35 |
| [Gas valve](https://www.amazon.com/s?k=Gas%20valve&tag=errorcodefixe-20) | $150–300 |
| [Condensate trap (Crown OEM)](https://www.amazon.com/s?k=Condensate%20trap%20(Crown%20OEM)&tag=errorcodefixe-20) | $20–40 |
| [Control board](https://www.amazon.com/s?k=Control%20board&tag=errorcodefixe-20) | $200–500 |

## Crown vs. Weil-McLain vs. Burnham E1

Most residential condensing boiler brands use E1 for ignition lockout — it's an industry convention. The diagnosis steps are nearly identical across brands. The key difference is the reset location and service menu interface.
