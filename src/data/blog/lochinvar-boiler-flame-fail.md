---
title: "Lochinvar Boiler F08 Flame Failure Error — Causes and Fix"
author: "James Rutherford"
pubDatetime: 2026-04-26T17:45:00Z
featured: false
draft: false
tags:
  - boiler
  - lochinvar
  - heating
description: "Lochinvar boiler F08 (Flame Failure) error code explained — causes, step-by-step diagnosis including flame sensor, igniter, and gas pressure checks, and fix guide."
---

## What this code means
The **F08 error code** on a Lochinvar boiler (Knight, CREST, WHN series, and commercial models) means **flame failure** — the boiler's control board tried to ignite the burner but did not detect a stable flame signal within the trial-for-ignition period. Lochinvar boilers make two or three ignition attempts. If no flame is confirmed after each attempt, the boiler enters a hard lockout and displays F08 (some models show "Flame Fail" as text rather than the F08 code).

F08 is a safety lockout — the boiler cannot be restarted automatically. A manual reset is required after identifying and correcting the root cause. Pressing RESET without fixing the underlying problem will result in immediate re-lockout on the next ignition attempt.

The F08 fault is functionally identical to flame failure codes on other high-efficiency condensing boilers: Navien E003, Rinnai LC13, and Weil-McLain all use the same ionization-current detection principle to confirm flame presence. Troubleshooting steps for F08 transfer well from experience with those platforms.

## Common Causes

- **Dirty or corroded flame rod** — The flame rod (flame sensor) detects combustion through ionization: the flame conducts a small AC current between the rod and the grounded burner body. Condensate residue, siloxane deposits (from certain cleaning products or well water), or carbon buildup on the rod surface insulate it from the flame. The board sees no ionization current even though the burner is lit, and cuts the gas valve — triggering F08.
- **No gas supply or low gas pressure** — A closed manual shutoff valve upstream of the boiler, a tripped gas regulator, or insufficient supply pressure from the utility prevents ignition from occurring at all. Lochinvar boilers are pressure-sensitive and require specific static and dynamic gas pressure.
- **Failed ignition electrode** — The ignition electrode has developed a crack in its ceramic insulator or the electrode gap has widened over years of thermal cycling. A cracked insulator causes the spark to jump to ground internally rather than crossing the burner gap, preventing ignition.
- **Air in the gas line** — After extended shutdown, new gas line work, or following a utility outage, air trapped in the supply line prevents ignition on the first several attempts. The boiler may lock out on F08 before the air purges.
- **Blocked venting** — A partially blocked intake or exhaust vent increases back pressure in the combustion chamber or reduces combustion air, causing the flame to be unstable or fail to establish.
- **Failed gas valve** — The gas valve solenoid has failed open, partially open, or there is a pressure regulator fault inside the valve preventing proper gas flow to the burner.

## Step-by-Step Fix {#fix}

1. **Verify gas supply** — Before opening the boiler, confirm the manual shutoff valve upstream of the unit is fully open (handle parallel to pipe = open). Check that other gas appliances in the building are working normally — if they are also out, the issue is upstream with the supply or meter. Contact your gas utility.

2. **Clean the flame rod** — This resolves F08 in the majority of cases. Shut off power and close the gas supply. Open the combustion chamber access panel and locate the flame sensor rod — a metal rod with a ceramic insulator extending into the burner area. Remove the single mounting screw and slide the rod out. Lightly polish the metal rod tip with fine steel wool or 400-grit emery cloth until it is shiny. Do not touch the ceramic insulator and do not sand aggressively. Reinstall and test.

3. **Inspect the ignition electrode** — With the combustion chamber open, examine the ignition electrode:
   - Look for cracks in the white ceramic insulator (even hairline cracks cause spark failures)
   - Check the spark gap between the electrode tip and the ground tab — typical Lochinvar gap is 1/8" (3mm). Use a feeler gauge or gap tool.
   - Inspect the high-voltage ignition cable from the ignition transformer to the electrode for cracked insulation or arc marks.
   An electrode with a cracked insulator or out-of-spec gap should be replaced, not cleaned.

4. **Check for air in the gas line** — If the boiler has been shut off for an extended period or gas line work was recently performed, press RESET and watch the ignition sequence carefully. You may hear the spark and see the gas valve open but no ignition for the first attempt. If it ignites on the second or third attempt and runs normally, air in the line was the cause. Run the boiler through several cycles to confirm.

5. **Inspect the vent system** — Go outside and check both the combustion air intake and exhaust vent terminations. Clear any obstruction: bird nests, ice, leaves, or construction debris. Verify the terminations are clear of each other by the required clearance (check the installation manual). Also confirm the exhaust PVC pipe has the correct slope toward the boiler (for condensate drainage) and no sags where condensate can pool and block flow.

6. **Reset the boiler** — Once you've corrected the identified issue, press and hold the RESET button on the boiler's display for 3–5 seconds until the display clears. The boiler will initiate a pre-purge cycle and then attempt ignition. Watch the sequence: fan pre-purge → spark → gas valve click → burner light → F08 clears.

## Parts You May Need

| Part | Notes |
|------|-------|
| Flame rod / ionization sensor | [Amazon](https://www.amazon.com/s?k=Flame+rod+%2F+ionization+sensor&tag=errorcodefixes-20) — Look up part number by model; common Knight series sensors are interchangeable within the series |
| Ignition electrode | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lochinvar-boiler-flame-fail&k=lochinvar+knight+boiler+ignition+electrode&tag=errorcodefixes-20) — Replace when ceramic is cracked or spark gap is out of spec |
| High-voltage ignition cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lochinvar-boiler-flame-fail&k=boiler+high+voltage+ignition+cable&tag=errorcodefixes-20) — Replace if insulation is cracked or arc marks are visible on the cable |
| Gas valve (Honeywell VR series) | [Amazon](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-lochinvar-boiler-flame-fail&tag=errorcodefixes-20) — Replace only after confirming gas supply is adequate and ignition components are good |

## When to Call a Technician

Gas pressure testing requires a manometer and familiarity with the gas train. Any work that involves disconnecting the gas supply line — including gas valve replacement — must be performed by a licensed plumber, HVAC technician, or gas fitter. After any combustion-related repair, the boiler should have combustion performance verified with a calibrated analyzer (CO, CO2, O2, and stack temperature) to confirm safe operation. If F08 persists after cleaning the flame rod and inspecting the electrode, call a Lochinvar-authorized service technician.
