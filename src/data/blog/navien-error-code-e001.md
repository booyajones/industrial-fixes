---
title: "Navien Error Code E001 — No Ignition Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-04-07T08:00:00Z
modDatetime: 2024-04-07T08:00:00Z
slug: navien-error-code-e001
featured: false
draft: false
tags:
  - boiler
  - navien
  - ignition
  - tankless
description: "Navien E001 error code means the burner failed to ignite. This guide covers every cause and fix for the Navien tankless water heater and combi-boiler E001 ignition fault."
---

## Error Code: Navien E001

**What it means:** Navien error code E001 indicates a no-ignition fault. The Navien control board initiated an ignition sequence — energizing the igniter and opening the gas valve — but the flame sensor did not detect a confirmed flame within the ignition trial period. After multiple failed attempts, the unit locks out with E001. This code applies to both Navien NR/NRC-series tankless water heaters and NCB-series combi-boilers. The unit will not fire until the fault is reset by pressing the power button or cycling the unit off and on.

## Common Causes

- **No gas supply or closed shutoff** — The most basic cause. Check that the manual gas shutoff on the supply line to the Navien is fully open (handle parallel to pipe). If other gas appliances are working, supply is fine.
- **Low gas pressure** — Navien units require minimum inlet gas pressure of 3.6" W.C. (natural gas) or 8.7" W.C. (propane). Pressure drops during peak demand or from undersized gas piping can prevent ignition.
- **Dirty or failed flame sensor (FR sensor)** — The Navien flame rod accumulates residue and becomes insulating over time. The board does not detect the microamp signal through the contaminated rod.
- **Failed igniter** — The spark igniter can fail to generate adequate spark due to carbon buildup on the electrode tip, incorrect gap, or a cracked ceramic insulator.
- **Air in gas line** — After a gas outage or new installation, air trapped in the gas supply line prevents ignition on the first several attempts. Multiple resets are needed to purge the air.
- **Condensate drain blocked** — On condensing Navien units, a blocked condensate drain can prevent startup as the unit detects a drainage fault and inhibits ignition.

## Diagnosis Steps

1. Check the gas supply: verify the manual shutoff is open. If your home had a gas outage recently, air in the line is likely — reset E001 and attempt startup 3–5 times to purge the line.
2. Check the condensate drain. Trace the small plastic drain line from the unit to the floor drain or drain point. If it is clogged or frozen (outdoor installations in winter), clear it.
3. Inspect the igniter and flame sensor. Access the combustion chamber by removing the front cover (after disconnecting power and gas). The spark igniter has a visible electrode tip — inspect for heavy carbon deposits. Clean with fine sandpaper.
4. Check igniter spark: with the unit attempting ignition, listen for rapid clicking (spark). No clicking = igniter or igniter control circuit failure.
5. If spark is present but no ignition: gas is likely the issue. Confirm gas pressure at the inlet with a manometer.

## Fix

Air purging resolves E001 on new installations and after gas outages — press reset repeatedly (5–10 times) to allow the unit to pull through the air-filled line. Patience is required.

For dirty igniters: clean the spark electrode with 320-grit sandpaper, ensuring the gap between the electrode tip and ground plate is 3–4mm (per Navien spec). For dirty flame rods: clean the rod with emery cloth.

If the igniter electrode is cracked or the flame rod is corroded through: replace the igniter/flame sensor assembly. Navien sells these as a combined assembly for most NR and NCB models.

Low gas pressure requires a licensed plumber or gas tech to inspect the gas piping supply and meter capacity.

## Parts

| Part | Where to Buy |
|------|-------------|
| [Navien igniter / flame sensor assembly](https://www.amazon.com/dp/B0CZ7M9V4D?ascsubtag=ecf-navien-error-code-e001&tag=errorcodefixes-20) | RepairClinic, SupplyHouse |
| [Condensate drain kit](https://www.amazon.com/s?ascsubtag=ecf-navien-error-code-e001&k=Condensate+drain+kit&tag=errorcodefixes-20) | Amazon, SupplyHouse |
| [Gas pressure test kit (manometer)](https://www.amazon.com/s?ascsubtag=ecf-navien-error-code-e001&k=Gas+pressure+test+kit+%28manometer%29&tag=errorcodefixes-20) | Amazon, Grainger |

## When to Call a Technician

If E001 persists after purging air and cleaning the igniter: a licensed plumber (gas-certified) should inspect the gas supply, pressure, and valve operation. Gas valve replacement on Navien units requires a licensed technician.

## Related Articles

- [Navien E002 Error Code — Causes & Fix](/posts/navien-error-code-e002/)
- [Navien Error Code E003 — Ignition Failure Fix](/posts/navien-error-code-e003-ignition-failure/)
- [Navien Error Code E004 — Causes & Fix](/posts/navien-error-code-e004/)
- [Navien E006 Error Code — Causes & Fix](/posts/navien-error-code-e006/)
- [Navien Error Code E007 — Causes & Fix](/posts/navien-error-code-e007/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [Rheem Performance Platinum PDN tankless error codes](/posts/rheem-performance-platinum-pdn-error-codes/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Rinnai code 11 no-ignition fix](/posts/rinnai-error-code-11/)

## See Also

- [Navien Error Code E021 — Cold Water Inlet Thermistor Fault Fix](/posts/navien-error-code-e021/)
- [Navien E002 Error Code — Causes & Fix](/posts/navien-error-code-e002/)
- [Navien Error Code E007 — Causes & Fix](/posts/navien-error-code-e007/)
- [Navien E030 Error Code — Causes & Fix](/posts/navien-error-code-e030/)
