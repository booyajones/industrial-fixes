---
title: "Burnham Boiler E1 Lockout Code Fix"
author: "James Rutherford"
pubDatetime: 2024-03-15T08:00:00Z
modDatetime: 2024-03-15T08:00:00Z
slug: burnham-boiler-e1-lockout-code
featured: false
draft: false
tags:
  - hvac
  - burnham
  - boiler
  - lockout
  - ignition
description: "Burnham boiler E1 lockout means the burner failed to ignite after the maximum number of attempts. This guide covers every cause and fix — gas, ignition, and control board."
---

## Error Code: Burnham Boiler E1

**What it means:** E1 on Burnham boilers (including the ES2, Alpine, and Mega-Stor series) is an ignition lockout. The boiler's integrated ignition module attempted to light the burner, failed to prove a flame within the allowed time window, and after the configured number of retries, locked out. The boiler will display E1 (sometimes E01) and will not attempt another ignition cycle until the lockout is manually cleared.

On Burnham boilers, lockout is a safety feature — repeated ignition failures could fill the combustion chamber with unburned gas. The lockout prevents dangerous accumulations.

## Common Causes

- **Failed or dirty igniter/electrode** — The spark electrode is the most common cause of ignition lockout. Carbon buildup on the electrode tip prevents proper spark, and a cracked ceramic insulator causes current to arc to ground instead of across the gap.
- **Gas supply interruption** — Low gas pressure, a closed manual shutoff valve, a tripped regulator at the meter, or simultaneous high demand from multiple appliances can reduce gas supply enough to prevent ignition.
- **Failed gas valve** — The gas valve solenoid receives the ignition signal but fails to open, so no gas reaches the burner. The igniter fires, nothing lights, and lockout follows.
- **Flue or combustion air problem** — A blocked flue, closed combustion air damper, or inadequate combustion air supply prevents the burner from establishing proper flame.
- **Flame sensor failure** — The ionization rod that proves flame presence is corroded, coated, or positioned incorrectly. The burner may actually light briefly, but the control can't confirm the flame and shuts off the gas.
- **Control board fault** — The integrated boiler controller fails to properly sequence the ignition cycle.

## Step-by-Step Fix {#step-by-step-fix}

1. **Clear the lockout and observe the startup sequence.** Press and hold the reset button on the boiler control (typically 3–5 seconds, or consult your specific boiler's manual). Stand back and listen: you should hear the pre-purge fan (if equipped) run, then a clicking igniter, then the burner lighting within 4–7 seconds. If you hear clicking but no ignition, gas supply is suspect. If you hear nothing, the control or igniter wiring is suspect.

2. **Check the gas supply.** Confirm the manual shutoff valve at the boiler is fully open (handle parallel to the pipe = open; perpendicular = closed). If other gas appliances in the home are working normally, gas supply is likely fine. If nothing gas-powered is working, call the gas utility.

3. **Inspect the igniter electrode.** Turn off gas and power. Locate the igniter electrode at the burner — it's a ceramic-mounted rod positioned near the burner ports with a high-voltage wire connected to it. Inspect the ceramic insulator for cracks (cracks = current to ground = no spark at tip). Check the electrode tip for carbon buildup — clean with fine sandpaper if coated. Verify the electrode gap is 1/8" (3mm) as specified in Burnham's service manual.

4. **Check the flame sensor/ionization rod.** Many Burnham boilers use a separate ionization rod for flame sensing (distinct from the ignition electrode). It's a simple rod positioned in the burner flame path. With power off, remove it and clean the rod with fine steel wool. Measure resistance to ground with a multimeter — should show infinite resistance (no short to ground through the ceramic insulator).

5. **Verify gas valve operation.** During the ignition sequence (with a clear view of the boiler and power/gas restored), listen for the audible click of the gas valve solenoid opening during the trial for ignition period. No click = electrical signal not reaching the valve, or valve solenoid failed. Click but no gas = valve mechanism failed internally.

6. **Check flue and combustion air.** Inspect the flue pipe from the boiler to the exhaust termination. Look for blockages, disconnected joints, or excessive condensate accumulation (on high-efficiency boilers with PVC flue). Confirm the combustion air intake (if direct-vented) is clear of debris, snow, or ice at the exterior termination.

7. **Verify 24V to the gas valve.** With a multimeter, during the ignition sequence, measure the voltage at the gas valve wiring terminals. Should read 24V AC during the trial for ignition period. No voltage = control board output failure or wiring fault.

8. **After repair, run 3 complete heat cycles.** Confirm E1 does not return before returning the boiler to unattended operation.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Where to Buy | Typical Cost |
|------|-------------|-------------|
| Ignition electrode (Burnham OEM, e.g., 7-2-0801) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-burnham-boiler-e1-lockout-code&k=Ignition+electrode+%28Burnham+OEM%2C+e.g.%2C+7-2-0801%29&tag=errorcodefixes-20) \| Burnham dealer, HeatersPlus | $25–$60 |
| Flame sensor / ionization rod (OEM) | [Amazon](https://www.amazon.com/s?k=Flame+sensor+%2F+ionization+rod+%28OEM%29&tag=errorcodefixes-20) \| Burnham dealer, eComfort | $20–$50 |
| Gas valve (Honeywell VR8205, common Burnham app) | [Amazon](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-burnham-boiler-e1-lockout-code&tag=errorcodefixes-20) \| Burnham dealer, Johnstone Supply | $100–$250 |
| Burnham integrated control board | [Amazon](https://www.amazon.com/s?k=Burnham+integrated+control+board&tag=errorcodefixes-20) \| Burnham dealer, eComfort | $150–$400 |
## When to Call a Professional

If you've checked the gas supply, cleaned the electrode and flame sensor, and confirmed 24V to the gas valve — call a licensed HVAC/boiler technician. Boiler combustion diagnosis requires CO testing, combustion analysis, and gas pressure measurement at the manifold. Working on a gas appliance without proper training and equipment carries serious risks including CO poisoning and fire. Tell the tech: "Burnham [model], E1 lockout. Gas supply is confirmed, electrode is clean, flame sensor tested good. I need manifold pressure and combustion analysis."

> **Pro tip:** Burnham boilers store lockout history in some models — check the control display for a multi-fault history mode (hold the info or diagnostic button). If E1 has been occurring sporadically over days or weeks without you noticing, the fault history will show you how many lockouts occurred and roughly when. Intermittent lockouts that only happen during very cold weather often point to gas supply pressure droop during peak demand — a gas utility or regulator issue, not a boiler fault.
