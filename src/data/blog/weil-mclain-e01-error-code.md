---
title: "Weil-McLain Boiler Error Code E01 — Lockout Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-17T08:00:00Z
modDatetime: 2024-03-17T08:00:00Z
slug: weil-mclain-e01-error-code
featured: false
draft: false
tags:
  - hvac
  - boiler
  - weil-mclain
  - lockout
  - commercial
description: "Weil-McLain boiler error code E01 means the boiler locked out after repeated flame failures. This guide covers every cause and fix for E01 on Weil-McLain gas boilers."
---

## Error Code: Weil-McLain E01

**What it means:** Error code E01 on a Weil-McLain boiler indicates a safety lockout caused by flame failure. The boiler attempted to establish a burner flame, the flame sensor either never detected a flame or detected flame loss shortly after ignition, and the burner control board locked out the gas valve as a safety measure.

E01 appears on Weil-McLain Ultra Series, ECO Series, and GV Gold boilers. On some models, E01 is displayed as "Lockout - No Flame" or a series of LED blinks. The lockout is a hard lockout — the boiler will not retry automatically. A manual reset (typically a reset button on the boiler or a power cycle) is required to attempt re-ignition.

This code is one of the most searched Weil-McLain faults because it appears frequently in commercial buildings and multifamily residential properties, and it comes on exactly when the heat is needed most.

## Common Causes

- **Dirty flame sensor** — The flame sensor rod collects oxide deposits that reduce its ability to conduct current through the flame. The burner control board requires a minimum current signal (typically 1.5–2 µA) to confirm flame presence. A dirty sensor produces inadequate signal and the board declares flame failure.
- **Failed igniter** — If the igniter doesn't generate sufficient spark or doesn't glow to the required temperature (on hot surface ignition systems), the burner never lights and the board logs E01 after the ignition trial times out.
- **Gas supply problem** — Low gas pressure, a partially closed manual shutoff, or a simultaneously high-demand gas event (all units in a building calling for heat at once) can starve the burner during the ignition trial.
- **Venting or combustion air obstruction** — Weil-McLain high-efficiency boilers pull combustion air through a dedicated intake pipe. A blocked intake (bird nest, ice, debris) or blocked exhaust flue prevents proper combustion, causing flame instability or failure.
- **Failed gas valve** — A gas valve that doesn't open fully (due to a failed solenoid coil or mechanical failure) delivers insufficient gas for ignition or stable flame.
- **Weak or intermittent flame signal wiring** — A loose connector or cracked wire on the flame sensor signal lead causes the board to intermittently lose the flame signal during operation, even when the flame is physically present.

## Step-by-Step Fix {#step-by-step-fix}

1. **Press the manual reset button.** Locate the reset button on the boiler's burner control (typically a red or gray button on the controller face). Press it once firmly. The boiler will attempt re-ignition within about 30 seconds. If it lights and stays lit, monitor it through one complete heat cycle — E01 may indicate an intermittent problem that needs further diagnosis even if the first reset succeeds.

2. **Observe the ignition sequence.** If the boiler faults again after reset, watch the ignition sequence: does the inducer start? Does the igniter visibly spark or glow? Does gas flow (you may hear the gas valve click)? Does a flame appear? Where in the sequence does it stop? This observation tells you exactly what failed.

3. **Clean the flame sensor.** Shut off power and gas to the boiler. Locate the flame sensor — a small metal rod extending into the burner flame area, with a ceramic insulator and a single wire lead. Disconnect the lead, remove the mounting screw, and carefully extract the sensor. Using a fine abrasive (fine steel wool or a dollar bill), gently buff the rod surface to remove the oxide coating. Reinstall, reconnect, and reset. Weil-McLain flame sensor **383-500-044** is the OEM replacement if cleaning doesn't fully resolve the signal issue (~$35 at HVAC parts suppliers).

4. **Inspect and test the igniter.** Locate the igniter element in the burner assembly. For spark igniters, inspect the electrode tip for fouling or wear — the gap should be approximately 1/8 inch (3mm). For hot surface igniters, inspect for cracks. Test resistance across the igniter terminals: most Weil-McLain igniters should read 40–100 ohms cold. An open circuit means the igniter needs replacement. Weil-McLain igniter **383-500-043** (~$55) is the OEM part for most Ultra and ECO series boilers.

5. **Verify gas supply.** Confirm the manual gas shutoff at the boiler is fully open. If you have a manometer, check inlet pressure at the gas valve test port — Weil-McLain specifies 5–7 inches W.C. minimum for natural gas. If the building has multiple boilers or gas appliances, test during a peak demand period to rule out system-wide pressure drop.

6. **Inspect combustion air intake and exhaust flue.** Go outside and inspect the intake and exhaust terminals. Both must be completely clear. Look for ice formation in cold climates (condensate from the exhaust can ice up the intake), bird nests, wasp nests, or debris. On Weil-McLain boilers, the intake is typically a 2" or 3" white PVC pipe terminating at the exterior wall. Clear any obstruction.

7. **Check the flame sensor signal strength.** If you have a multimeter with microamp measurement capability, clip it into the flame sensor circuit during operation and measure the flame rectification current. A healthy signal is 2–6 µA. A signal below 1.5 µA will cause intermittent E01 lockouts. A reading of 0 µA with a confirmed flame present means the sensor or its wiring is the problem.

8. **Test the gas valve solenoid.** With power off, disconnect the gas valve wiring. Using a multimeter set to ohms, measure resistance across each solenoid coil — most Weil-McLain gas valves have two coils (operator and modulation). An open circuit (OL) on either coil means the valve solenoid has failed. Gas valve replacement requires licensed service in most jurisdictions.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Part Number | Typical Cost | Where to Buy |
|------|------------|-------------|-------------|
| Flame sensor | 383-500-044 | $30–$45 | HVAC Parts / Weil-McLain Distributor |
| Igniter | 383-500-043 | $50–$70 | HVAC Parts / Weil-McLain Distributor |
| Gas valve | 383-500-376 | $200–$350 | Weil-McLain Distributor |
| Burner control module | 383-500-372 | $280–$420 | Weil-McLain Distributor |

## When to Call a Professional

E01 related to the gas valve, burner control module, or persistent flame sensor issues that don't resolve after cleaning and replacement should be diagnosed by a licensed commercial HVAC technician with experience on hydronic systems. Working on commercial boilers involves high-voltage controls, live gas lines, and high-pressure hot water systems. In most states, commercial boiler service requires a licensed boiler technician or HVAC contractor. Additionally, if E01 occurs across multiple boilers in the same building simultaneously, the root cause is almost certainly a building-wide gas supply problem — that diagnosis starts at the gas meter, not at the boilers.

> **Pro tip:** Before resetting E01 on a commercial boiler, write down the exact time and outdoor temperature. If E01 consistently appears at the same time of day or at a specific outdoor temperature, you have a strong clue: morning lockouts at the coldest part of the day usually point to a gas pressure problem (high demand across the building at startup), while random lockouts point to a failing flame sensor or igniter. The pattern is your best diagnostic tool.
