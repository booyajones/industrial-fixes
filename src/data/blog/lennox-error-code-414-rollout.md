---
title: "Lennox Error Code 414 Rollout — Causes & Fix"
description: "What Lennox error code 414 rollout means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - lennox
---

## Lennox Error Code 414 Rollout — What It Means

Lennox fault code 414 has two distinct triggers on SureLight control boards: one for gas valve circuit faults (covered in a separate guide) and one specifically for the rollout limit switch circuit. When 414 is paired with a rollout switch trip, the board detected that one or more rollout switches opened during or between heating cycles. Lennox units often have two rollout switches — one per burner bank — and the 414 rollout variant may indicate a single switch tripped or that both switches are in the circuit and one has failed open. This is a safety shutdown condition.

[Jump to Fix](#fix)

## Common Causes

- **Blocked flue causing rollout** — The most critical cause: combustion gases cannot exit the heat exchanger normally and escape out the front of the burner box, contacting the rollout switch. Any flue restriction can cause this.
- **Failed induced draft motor not creating draft** — Without adequate negative draft pressure, combustion gases recirculate inside the furnace cabinet and cause rollout even with an open flue.
- **Single rollout switch failed open (not a rollout event)** — The switch itself fails open without an actual flame rollout. Use a multimeter to test continuity across each switch individually. A switch that reads open at room temperature has failed.
- **High gas manifold pressure** — Excessive gas pressure creates an oversized flame that can exceed heat exchanger capacity and contact the rollout switches located on the burner deck.

## Step-by-Step Fix {#fix}

1. **Identify which rollout switch tripped** — Lennox furnaces typically have two rollout switches on the burner compartment. Test each one individually with a multimeter: continuity = closed (OK), open circuit = tripped or failed.
2. **Reset manual-reset rollout switches** — Press the reset button firmly on each tripped switch. If a switch will not reset after cooling, it has failed and must be replaced.
3. **Confirm no actual rollout conditions exist** — Inspect the flue path and inducer before resetting. Resetting without clearing the root cause will result in immediate re-trip and potential heat exchanger damage.
4. **Check manifold gas pressure** — Connect a manometer to the gas valve test port. Natural gas should read 3.2–3.7" W.C. at the manifold. High pressure (>3.8" W.C.) requires gas valve adjustment or replacement.
5. **Test inducer and pressure switch** — Verify the inducer runs to full speed and the pressure switch closes before allowing the ignition sequence to proceed on the next test cycle.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Rollout limit switch (manual reset) | [Amazon](https://www.amazon.com/s?k=Rollout+limit+switch+%28manual+reset%29&tag=errorcodefixes-20) \| Buy matching pair if replacing one; Lennox uses 190°F or 250°F rated switches depending on position |
| Induced draft motor | [Amazon](https://www.amazon.com/s?k=Induced+draft+motor&tag=errorcodefixes-20) \| Replace if insufficient draft is confirmed cause of rollout |
| Gas valve | [Amazon](https://www.amazon.com/s?k=Gas+valve&tag=errorcodefixes-20) \| Replace only if manifold pressure is non-adjustable and out of spec |
## When to Call a Pro

Rollout events are a carbon monoxide and fire risk. If the switch tripped due to an actual flame rollout rather than a component failure, do not operate the furnace until a technician identifies and corrects the draft or combustion issue. A cracked heat exchanger can produce rollout conditions and is not field-repairable.
