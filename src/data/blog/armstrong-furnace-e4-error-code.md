---
title: "Armstrong Furnace E4 Error Code — Causes & Fix"
description: "What Armstrong furnace E4 means, why ignition fails repeatedly, and how to fix it step by step."
pubDatetime: 2026-04-22T10:00:00Z
modDatetime: 2026-04-22T10:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - hvac
  - armstrong
money_part: "Hot surface ignitor"
most_likely_cause: "Failed hot surface ignitor"
---

## Armstrong Furnace E4 Error Code — What It Means

E4 on an Armstrong Air furnace (part of the Allied Air Enterprises family, which also includes Ducane and ADP) typically indicates an ignition failure lockout. The control board attempted the ignition sequence the maximum number of times (usually three tries) and could not confirm a stable flame from the flame sensor. The furnace locks out and displays E4 until the fault is manually cleared.

[Jump to Fix](#fix)

## Common Causes

- **Failed hot surface ignitor** — The ignitor glows red-hot to light the gas but fractures with age or thermal cycling. A cracked or burned-out ignitor won't produce enough heat to reliably ignite the burners.
- **Dirty flame sensor** — Silicon oxide deposits on the flame sensor rod reduce the microamp signal it sends to the control board. A weak signal causes the board to abort the cycle even if the burner lit.
- **No gas or insufficient gas pressure** — A closed manual shutoff valve, a tripped gas meter regulator, or a faulty gas valve prevents fuel from reaching the burners.
- **Failed inducer or pressure switch** — If the draft system doesn't confirm proper airflow, the board won't open the gas valve, making the sequence look like an ignition failure from the outside.

## Step-by-Step Fix {#fix}

1. **Confirm gas supply** — Check that the manual gas shutoff upstream of the furnace is fully open. Verify other gas appliances work normally. Restore gas supply if interrupted.
2. **Inspect the hot surface ignitor** — Power off the furnace. Remove the ignitor (one mounting screw). Inspect for visible cracks. Test resistance with a multimeter — typical range is 40–80 ohms cold. Open circuit means replace it.
3. **Clean the flame sensor** — Remove the sensor rod and clean with 400-grit emery cloth or fine steel wool. Remove all visible oxidation. Reinstall and tighten the terminal connector.
4. **Test the gas valve** — During an ignition attempt, verify 24VAC is present at the gas valve coil terminals when the ignitor is glowing. Voltage present but valve not opening = replace the gas valve.
5. **Clear lockout and test** — Power cycle the furnace for 30 seconds. Restore power and initiate a heat call. Watch the sequence: inducer → pressure switch → ignitor glows → gas valve opens → flame confirmed. If it fails at a specific step, that is the fault.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hot surface ignitor | [Amazon](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-armstrong-furnace-e4-error-code&tag=errorcodefixes-20) \| Verify voltage rating (120V or 80V) and physical dimensions |
| Flame sensor rod | [Amazon](https://www.amazon.com/s?k=Flame+sensor+rod&tag=errorcodefixes-20) \| Clean first; replace if signal remains weak |
| Gas valve | [Amazon](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-armstrong-furnace-e4-error-code&tag=errorcodefixes-20) \| Replace if 24VAC is confirmed at coil but valve won't open |
| Pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-armstrong-furnace-e4-error-code&tag=errorcodefixes-20) \| Replace if draft system is confirmed working but switch stays open |
## When to Call a Pro

Gas valve replacement and gas pressure testing require a licensed HVAC or gas technician. Do not attempt to bypass the gas valve or ignition safety controls under any circumstances.

## Related Articles

- [AirEase Furnace E1 Error Code — Causes & Fix](/posts/airease-furnace-e1-error-code/)
- [Amana Furnace 3 Flash Error Code — Causes & Fix](/posts/amana-furnace-3-flash-error-code/)
- [American Standard Furnace 3 Flash Error Code — Causes & Fix](/posts/american-standard-furnace-3-flash/)
- [AO Smith Water Heater 3 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-3-flashes/)
- [AO Smith Water Heater 4 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-4-flashes/)
