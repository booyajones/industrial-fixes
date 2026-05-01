---
title: "Lennox Error Code 111 — Causes & Fix"
description: "What Lennox error code 111 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - lennox
---

## Lennox Error Code 111 — What It Means

Lennox fault code 111 (three flashes on the diagnostic LED, or displayed as "111" on SureLight boards) indicates the rollout switch has opened. The rollout switch is a thermal fuse-type safety device positioned near the burner orifices or heat exchanger opening. It trips when combustion gases or flame exit the heat exchanger in an uncontrolled direction — a condition called flame rollout. This is a hard safety event: the furnace shuts down completely and will not restart until the switch is manually reset and the root cause is addressed.

[Jump to Fix](#fix)

## Common Causes

- **Restricted flue or venting** — A partially blocked or fully blocked flue prevents combustion gases from exiting normally, creating back pressure that reverses flow and causes rollout.
- **Induced draft motor failure** — If the inducer wheel is broken, the motor is failing, or the bearing is worn, draft is insufficient to keep combustion contained within the heat exchanger.
- **Cracked heat exchanger** — Cracks in the primary or secondary heat exchanger allow combustion gases to bypass the normal flow path and contact the rollout switch. A critical safety finding.
- **Incorrect gas pressure** — High manifold gas pressure produces an oversized flame that can exceed the heat exchanger capacity and roll out past the burner opening.

## Step-by-Step Fix {#fix}

1. **Let the switch cool before reset** — The rollout switch is temperature-actuated. It won't reset until it drops below its reset threshold (typically well below 200°F). Wait at least 10–15 minutes after shutdown.
2. **Inspect the flue from furnace to termination** — Check PVC vent pipes on 90%+ units or metal flue on 80% units. Look for sagging pipe that traps condensate, blocked termination screens, or critter intrusion.
3. **Verify inducer operation** — Start the furnace and observe the inducer. It should ramp up and reach full speed within a few seconds. Sluggish start or intermittent operation indicates a motor or capacitor problem.
4. **Reset the rollout switch** — Locate the manual-reset button (often red) on the burner compartment wall near the heat exchanger opening. Press firmly until it clicks.
5. **Check manifold gas pressure** — Connect a manometer to the gas valve outlet port. Verify pressure matches the spec on the furnace rating plate (typically 3.5" W.C. for natural gas).

## Parts Often Needed

| Part | Notes |
|------|-------|
| Rollout limit switch | [Amazon](https://www.amazon.com/dp/B0BN3TRG9R?tag=errorcodefixes-20) \| Verify correct temp rating — Lennox uses several setpoints |
| Induced draft motor with wheel | [Amazon](https://www.amazon.com/dp/B00FDZ90B2?tag=errorcodefixes-20) \| Replace as assembly if wheel is cracked or motor bearing is worn |
| Vent pipe elbow or section | [Amazon](https://www.amazon.com/s?k=Vent+pipe+elbow+or+section&tag=errorcodefixes-20) \| Replace cracked or blocked PVC sections on 90%+ units |
## When to Call a Pro

Flame rollout combined with a cracked heat exchanger is a carbon monoxide hazard. If you cannot identify a clear venting or draft cause for the rollout trip, stop operating the furnace and have a technician perform a full combustion and heat exchanger inspection before restart.

## See Also

- [Lennox Error Code 114 — Causes & Fix](/posts/lennox-error-code-114/)
- [Lennox Error Code 231 — Causes & Fix](/posts/lennox-error-code-231/)
- [Lennox Error Code 223 — Causes & Fix](/posts/lennox-error-code-223/)
- [Lennox G60UHV Furnace Error Codes — Flash Code Diagnostic Guide](/posts/lennox-g60uhv-error-codes/)

## Related Articles

- [Lennox Error Code 292 — Ignition Failure Fix](/posts/lennox-292-error-code/)
- [Lennox EL296V Error Codes — Variable-Speed Furnace Diagnostic Guide](/posts/lennox-el296v-error-codes/)
- [Lennox Elite Series Furnace Error Codes — Fault Code Diagnostic Guide](/posts/lennox-elite-series-furnace-codes/)
- [Lennox 103 Error Code — Causes & Fix](/posts/lennox-error-code-103/)
- [Lennox Error Code 114 — Causes & Fix](/posts/lennox-error-code-114/)
