---
title: "Navien Error Code E024 — Overheat / High Temperature Cutoff"
description: "Navien tankless water heater Error Code E024 means the unit has detected an overheat condition. Learn causes, diagnostic steps, and how to fix Navien E024."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - plumbing
  - navien
  - tankless-water-heater
  - overheat
---

# Navien Error Code E024 — Overheat / High Temperature Cutoff

**Error Code E024** on Navien tankless water heaters (NPE and NPN series) means the unit has detected an overtemperature condition — the heat exchanger or outgoing water has exceeded the safe operating limit, and the unit has shut down to prevent damage or scalding.

## Jump to Fix

- [Most Likely Cause](#most-likely-cause)
- [Diagnosis Steps](#diagnosis)
- [Parts](#parts)

## What Is the E024 Limit

Navien units shut down on E024 when the heat exchanger temperature exceeds the thermal fuse limit or when the outlet water temperature rises above the maximum setpoint (typically above 185°F on most models). The thermal fuse is a one-shot device — if it has blown, it must be replaced.

## Common Causes {#most-likely-cause}

| Cause | Likelihood |
|---|---|
| Scaled/blocked heat exchanger (calcium buildup) | Very High |
| Low water flow rate | High |
| Thermostat setpoint too high | High |
| Blown thermal fuse | Medium |
| Failed thermistor reading too low (false overheat) | Medium |
| Recirculation pump running without flow | Low |
| Failed gas modulation (burner stuck at high fire) | Low |

## Step-by-Step Diagnosis {#diagnosis}

**Step 1 — Check temperature setpoint**
- Press the UP/DOWN buttons on the unit display
- Default recommended setting is 120°F
- Settings above 140°F approach the E024 limit rapidly in low-flow conditions

**Step 2 — Check water flow rate**
- Navien units require minimum flow to operate safely: NPE series minimum is 0.5 GPM
- Partially closed shutoff valves or clogged inlet filter screen reduce flow
- Remove and clean the inlet filter screen (behind the cold water inlet)

**Step 3 — Descale the heat exchanger**
- Scale buildup is the #1 cause of E024 in hard water areas
- Descale using white vinegar or commercial descaling solution:
  1. Connect a pump and hoses to the service ports (cold in, hot out)
  2. Circulate descaling solution for 45–60 minutes
  3. Flush with clean water
- After descaling, the heat exchanger transfers heat more efficiently and E024 should resolve

**Step 4 — Check the thermal fuse**
- The thermal fuse is a one-time-trip safety device on the heat exchanger
- With power off, locate the thermal fuse (round white device wired to the heat exchanger)
- Check continuity with a multimeter — open = blown fuse, must replace
- The fuse blowing is a symptom — fix the root cause (scale, flow) before replacing

**Step 5 — Check the outlet thermistor**
- The outlet thermistor measures water temperature
- Measure resistance and compare to a reference temperature
- If the thermistor reads low (reports water is cooler than it is), the board may allow overheating before tripping

## E024 Reset Procedure

1. Fix the root cause (descale, flow, setpoint)
2. Press and hold the POWER button for 3 seconds to reset the error
3. If E024 returns immediately: thermal fuse is blown — replace

## Replacement Parts {#parts}

| Part | Notes |
|---|---|
| Thermal fuse | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-error-code-e024&k=Thermal+fuse&tag=errorcodefixes-20) \| Navien part B001-41 or equivalent — match temperature rating |
| Outlet thermistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-error-code-e024&k=Outlet+thermistor&tag=errorcodefixes-20) \| Navien part — check resistance at known temperature |
| Inlet filter screen | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-error-code-e024&k=Inlet+filter+screen&tag=errorcodefixes-20) \| Stainless mesh — clean every 6 months in hard water areas |
| Descaling kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-error-code-e024&k=Descaling+kit&tag=errorcodefixes-20) \| Pump + hoses + solution — available from Navien or plumbing supply |
> **Warning:** E024 is a safety shutdown. Never bypass or disable the thermal fuse. If E024 occurs repeatedly after descaling, the heat exchanger may be permanently damaged and require replacement.

## Related Articles

- [Navien Error Code E001 — No Ignition Fix](/posts/navien-error-code-e001/)
- [Navien E002 Error Code — Causes & Fix](/posts/navien-error-code-e002/)
- [Navien Error Code E003 — Ignition Failure Fix](/posts/navien-error-code-e003-ignition-failure/)
- [Navien Error Code E004 — Causes & Fix](/posts/navien-error-code-e004/)
- [Navien E006 Error Code — Causes & Fix](/posts/navien-error-code-e006/)
