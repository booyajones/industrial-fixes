---
title: "Carrier 11 Error Code — Causes & Fix"
description: "What Carrier error code 11 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - carrier
money_part: "Hot surface igniter (silicon nitride)"
most_likely_cause: "Failed hot surface igniter"
---

## What this code means
Carrier fault code 11 indicates no ignition — the furnace attempted a trial for ignition and failed to establish flame. The control board made at least one attempt (sometimes two or three depending on board revision) to light the burner, confirmed no flame signal from the flame sensor, and locked the igniter circuit. This is one of the most common Carrier fault codes and almost always traces back to a failed igniter, a weak flame sensor, a gas supply issue, or a dirty burner assembly.

## Common Causes

- **Failed hot surface igniter** — The igniter cracks or burns out over time and no longer reaches ignition temperature. Resistance out of range (typically >200 Ω on silicon nitride igniters) is a reliable indicator.
- **Weak or contaminated flame sensor** — Carbon buildup on the flame sensor rod prevents it from detecting the established flame, causing the board to cut gas and log code 11.
- **Gas supply interrupted** — Low inlet gas pressure, a closed manual shutoff valve, or a tripped gas meter safety will prevent combustion regardless of igniter condition.
- **Dirty or restricted burner orifices** — Rust scale, debris, or spider nests in the burner tubes block gas flow and produce erratic ignition or no ignition at all.

## Step-by-Step Fix {#fix}

1. **Verify gas supply** — Confirm the manual gas shutoff upstream of the furnace is open. Check other gas appliances (water heater, range) to verify line pressure is present.
2. **Inspect the hot surface igniter** — Set meter to resistance (Ω). A silicon nitride igniter should read 40–200 Ω cold; silicon carbide typically 40–75 Ω. An open circuit (OL) means the igniter is failed. Visually inspect for cracks.
3. **Clean the flame sensor** — Remove the single-screw sensor rod and lightly polish the metal rod with fine steel wool or emery cloth. Reinstall and verify the microamp signal is 1.5–4 µA in flame; below 1 µA causes nuisance trips.
4. **Inspect burner tubes** — Remove the burner assembly access panel. Look for debris, rust blockage, or misalignment. Vacuum and blow out each burner port with compressed air.
5. **Reset the system** — Cycle power at the disconnect or breaker for 30 seconds. Restore power and observe the ignition sequence. Confirm flame establishes and the fault clears.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hot surface igniter (silicon nitride) | [Amazon](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-carrier-11-error-code&tag=errorcodefixes-20) \| Match OEM part number; Carrier uses several variants across model years |
| Flame sensor rod | [Amazon](https://www.amazon.com/s?k=Flame+sensor+rod&tag=errorcodefixes-20) \| Usually a generic 1/4" rod; verify terminal type matches |
| Gas valve | [Amazon](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-carrier-11-error-code&tag=errorcodefixes-20) \| Replace only after confirming proper inlet pressure and wiring |
## When to Call a Pro

If gas supply, igniter, and flame sensor all check out but the furnace still fails ignition, the issue may be a failed gas valve or a cracked heat exchanger affecting draft — both require a licensed HVAC technician to diagnose and repair safely.
