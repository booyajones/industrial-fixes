---
title: "Carrier 25 Error Code — Causes & Fix"
description: "What Carrier error code 25 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - carrier
money_part: "Flame sensor"
most_likely_cause: "Grounded flame sensor rod"
---

## What this code means
Carrier fault code 25 indicates a flame sense fault — the control board detected a flame signal when no flame should be present, or it detected a false flame signal before the igniter fired. This is distinct from code 11 (no ignition) because the board is seeing a signal it doesn't expect rather than seeing no signal at all. The primary suspects are a shorted or grounded flame sensor rod, stray electrical interference, or a gas valve that isn't closing completely between cycles.

## Common Causes

- **Grounded flame sensor rod** — If the flame sensor wire or rod is touching the burner box, it creates a false ground signal the board interprets as flame. Check for chafing against sheet metal.
- **Gas valve not closing fully** — A gas valve with a leaking seat allows a small flame to persist after the call for heat ends. The board senses this residual flame and flags a fault.
- **Contaminated sensor insulator** — Carbon or moisture bridging the ceramic insulator on the sensor rod can create a false microamp signal without actual flame.
- **Electrical interference** — In rare cases, variable speed motors or nearby equipment inject noise onto the flame sense circuit. Check for proper grounding of the furnace cabinet.

## Step-by-Step Fix {#fix}

1. **Inspect flame sensor rod and harness** — Trace the wire from the board to the sensor. Look for any contact with the burner box, cabinet walls, or sheet metal edges. The ceramic insulator must be intact and isolated.
2. **Clean the insulator on the sensor** — Use a dry cloth to clean the ceramic portion of the flame sensor. Carbon bridging the insulator is a common cause of false signals.
3. **Observe gas valve operation** — After the burner shuts down, watch the burner for a few seconds. Any residual flame means the gas valve isn't closing. Confirm 24V is being removed from the valve at end of call.
4. **Check furnace cabinet ground** — Verify the furnace cabinet is properly bonded to earth ground. A floating chassis can induce electrical noise on the sense circuit.
5. **Reset and monitor** — Cycle power and run the furnace through 2–3 heat cycles. If code 25 doesn't return, the issue was likely a grounding or contamination problem that's now resolved.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame sensor | [Amazon](https://www.amazon.com/s?k=Flame+sensor&tag=errorcodefixes-20) \| Replace if insulator is cracked or sensor rod is pitted |
| Gas valve | [Amazon](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-carrier-25-error-code&tag=errorcodefixes-20) \| Replace only if confirmed leaking through after shutdown |
| Control board | [Amazon](https://www.amazon.com/s?k=Control+board&tag=errorcodefixes-20) \| Last resort if sense circuit is defective on board itself |
## When to Call a Pro

A leaking gas valve requires replacement by a licensed technician — this involves breaking into the gas line. If you're not certified to handle gas work, stop at the diagnosis step and call a pro.
