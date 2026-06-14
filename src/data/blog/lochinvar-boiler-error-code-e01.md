---
title: "Lochinvar Boiler Error Code E01 — Causes & Fix"
description: "What Lochinvar boiler error code E01 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - boiler
  - lochinvar
money_part: "Hot surface igniter"
most_likely_cause: "Failed hot surface igniter"
---

## Lochinvar Boiler Error Code E01 — What It Means

Lochinvar boiler error code E01 indicates an ignition lockout — the control module attempted ignition and failed to establish or prove a flame within the required trial-for-ignition period. On Lochinvar's Knight, WHN, and Crest boiler lines, this is a hard lockout that requires a manual reset at the display panel. The board typically makes two to four ignition attempts before logging E01 and locking out. This fault is almost always caused by an ignition system failure (igniter, flame sensor, or gas supply), though inducer and pressure switch faults can also prevent the ignition sequence from completing.

[Jump to Fix](#fix)

## Common Causes

- **Failed hot surface igniter** — The silicon carbide or silicon nitride igniter cracks or loses continuity. No glow means no ignition. Test resistance at room temperature: out-of-range or open circuit confirms failure.
- **Dirty or degraded flame sensor** — Carbon accumulation on the flame sensor rod reduces ionization current below the board's minimum detection threshold (typically 1.5 µA). The board sees no flame even when it's burning.
- **Gas supply issue** — Low gas pressure, a closed manual shutoff valve, or a tripped gas meter safety prevents fuel from reaching the burner. Verify other gas appliances are working.
- **Inducer or pressure switch fault preventing ignition** — If the induced draft blower doesn't come up to speed or the pressure switch doesn't confirm draft, Lochinvar's control module will not allow the ignition sequence to progress.

## Step-by-Step Fix {#fix}

1. **Reset the lockout** — Press and hold the Reset button on the Lochinvar display panel for 3 seconds, or as indicated in the specific model's manual. The unit will attempt a new ignition cycle.
2. **Verify gas supply** — Confirm the manual gas shutoff at the boiler is open. Check inlet gas pressure with a manometer (should be 7" W.C. for natural gas at rest). Confirm other gas appliances in the building are operating.
3. **Inspect the igniter** — Access the burner compartment. Test igniter resistance: silicon carbide should be 40–100 Ω cold; silicon nitride 40–200 Ω. Open circuit (OL) means replacement required.
4. **Clean the flame sensor** — Remove the single-screw flame sensor rod. Lightly polish the metallic rod portion with fine steel wool. Reinstall. Verify microamp signal is above 1.5 µA with flame present using a microamp clamp or board diagnostic display.
5. **Observe the ignition sequence** — After reset, watch and listen: does the inducer start? Do you hear the igniter glow relay click? Do you hear gas ignite? Identify exactly where the sequence stops to narrow down the failed component.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hot surface igniter | [Amazon](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-lochinvar-boiler-error-code-e01&tag=errorcodefixes-20) \| Match OEM part number for the specific Knight or WHN model year |
| Flame sensor | [Amazon](https://www.amazon.com/s?k=Flame+sensor&tag=errorcodefixes-20) \| Often a universal rod; match thread size and terminal type |
| Gas valve | [Amazon](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-lochinvar-boiler-error-code-e01&tag=errorcodefixes-20) \| Replace only after gas supply and ignition components are ruled out |
## When to Call a Pro

Lochinvar boilers serving radiant heat, domestic hot water, or commercial HVAC systems are critical equipment. If E01 persists after checking igniter, flame sensor, and gas supply, a licensed boiler technician should diagnose before the system is offline for an extended period in cold weather.

## Related Articles

- [American Water Heater Error Codes — Complete Guide](/posts/american-water-heater-error-codes/)
- [AO Smith Water Heater 3 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-3-flashes/)
- [AO Smith Water Heater 4 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-4-flashes/)
- [A.O. Smith Water Heater Error Codes Guide](/posts/ao-smith-water-heater-error-codes/)
- [Bradford White Water Heater Error Code 1 — Pilot Outage Fix](/posts/bradford-white-error-code-1/)
