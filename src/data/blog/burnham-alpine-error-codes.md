---
title: "Burnham Alpine Boiler Error Code Guide — Causes & Fix"
description: "Burnham Alpine boiler error codes explained — what each fault means, why it happens, and how to fix it."
pubDatetime: 2026-04-22T15:00:00Z
modDatetime: 2026-04-22T15:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - boiler
  - burnham
---

## Burnham Alpine Boiler Error Codes — What They Mean

The Burnham Alpine is a high-efficiency modulating condensing boiler using the IBC Controls platform (Burnham uses the IBC HC Series controls on the ALP series). The boiler displays fault codes on a backlit LCD control panel. Codes use an alphanumeric format: "E" codes are hard lockouts requiring manual reset; "W" codes are warnings that may self-clear. The Alpine is available in 80–300 MBH input sizes and fires on natural gas or propane.

[Jump to Fix](#fix)

## Common Error Codes and Causes

- **E01 — Ignition Failure** — The burner failed to light after the maximum number of tries. Most common causes: failed igniter, dirty or failed flame sensor, gas supply issue, or incorrect gas pressure. Clean the flame sensor rod and test the igniter before replacing components.
- **E02 — Flame Lost During Operation** — The burner lit but the flame was lost unexpectedly. Causes: contaminated flame sensor, gas supply fluctuation, or a cracked heat exchanger causing combustion instability.
- **E03 — High Limit Tripped** — The boiler's high-limit safety opened because water temperature exceeded the limit set-point. Causes: failed circulator pump, air-locked system, or a stuck zone valve. Bleed air from the system and verify all circulators are running.
- **E04 — Low Water Condition** — The low-water cutoff (LWCO) has detected inadequate water in the system. Check system pressure (should be 12–25 PSI cold), inspect for leaks, and check the automatic fill valve if installed.
- **E05 — Pressure Switch Fault** — The inducer pressure switch did not prove draft within the startup window. See the pressure switch diagnosis steps below.
- **W06 — Service Reminder** — The Alpine has accumulated the set number of run hours and is requesting routine service. Not a fault — reset via the service menu after completing maintenance.
- **E08 — Flue Gas Temperature High** — The flue temperature exceeded the safe limit. Check that the vent is the correct size, all joints are sealed, and the boiler is not short-cycling excessively.

## Step-by-Step Fix {#fix}

1. **Read and record the code** — Note the exact code and any supporting data (water temp, status) shown on the Alpine's LCD before resetting.
2. **For E01/E02 (ignition/flame faults)** — Inspect the flame sensor rod for oxidation and polish with steel wool. Check gas supply pressure at the manifold (should be 3.5" WC natural gas, 10" WC LP). If the igniter does not glow during trial, test its resistance.
3. **For E03 (high limit)** — Verify system pressure is normal (15–20 PSI operating). Check that all zone valves are open and all circulators run during a call for heat.
4. **For E04 (low water)** — Check the boiler pressure gauge. Add water via the fill valve until pressure reaches 15 PSI and the LWCO clears. Inspect all visible piping for leaks.
5. **For E05 (pressure switch)** — Inspect the pressure switch hose for blockage and the condensate drain for a backup. Test the inducer and pressure switch as described in the burnham-boiler-e2 guide.
6. **Reset the boiler** — After addressing the root cause, hold the reset button for 3 seconds or cycle power. The Alpine should restart and complete a normal firing sequence.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame sensor rod | Clean first; replace if resistance is abnormally high or the tip is pitted |
| Gas valve | Replace only after confirming 24VAC input and correct gas pressure |
| Pressure switch | Match WC rating for the Alpine model size |
| Circulator pump (Taco, Grundfos) | Required if pump is failed and E03 is caused by no-flow |

## When to Call a Pro

Alpine boilers operate at high efficiency by modulating gas input, and incorrect setup of gas pressure, combustion analysis (CO/CO2), or control parameters can cause safety hazards. For persistent E01/E02 faults or any combustion analysis work, call a licensed technician with Alpine experience.
