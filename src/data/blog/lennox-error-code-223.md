---
title: "Lennox Error Code 223 — Causes & Fix"
description: "What Lennox error code 223 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - lennox
money_part: "Induced draft motor"
most_likely_cause: "Inducer motor failure"
---

## Lennox Error Code 223 — What It Means

Lennox fault code 223 indicates a draft inducer fault — the control board commanded the inducer to run but did not receive confirmation that it started or reached operating speed within the expected time window. On variable-speed inducer systems, this can also mean the inducer ran but could not achieve the RPM target needed to satisfy the pressure switch. The furnace will not proceed to ignition until the inducer is confirmed running, making this fault a hard lockout of the entire ignition sequence.

[Jump to Fix](#fix)

## Common Causes

- **Inducer motor failure** — The motor winding has failed open or the start capacitor has degraded. The motor may hum or fail to start entirely.
- **Blocked inducer wheel** — Debris, corrosion buildup, or a detached wheel blade can prevent the motor from reaching speed or cause intermittent stalls.
- **Pressure switch not closing** — The inducer is running but can't develop enough negative pressure to close the pressure switch, often because of a disconnected or blocked pressure tube, a cracked inducer housing, or excessive flue back pressure.
- **Wiring fault to inducer** — A loose molex connector or broken wire at the inducer motor harness prevents the board from energizing the motor.

## Step-by-Step Fix {#fix}

1. **Confirm inducer is receiving power** — With a call for heat active, measure voltage at the inducer motor terminals. Most inducers run on 120VAC. If voltage is present but the motor doesn't run, the motor or capacitor is failed.
2. **Spin the inducer wheel manually** — With power off, reach into the inducer housing (carefully) and spin the wheel. It should turn freely with minimal resistance. Any grinding, stiffness, or wobble points to a bearing or wheel issue.
3. **Inspect the pressure switch tube** — Locate the small rubber hose connecting the inducer housing port to the pressure switch. Verify it's fully seated on both ends, not kinked, and free of water. Blow through it to confirm it's clear.
4. **Check the inducer run capacitor** — On single-phase inducers with a run capacitor, test capacitance with a meter. A degraded capacitor will allow the motor to hum but fail to start.
5. **Reset and test** — Cycle power and observe the inducer on the next call for heat. Time from call to inducer start should be under 30 seconds. If it starts but shuts back down, revisit pressure switch continuity during operation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Induced draft motor | [Amazon](https://www.amazon.com/dp/B00FDZ90B2?ascsubtag=ecf-lennox-error-code-223&tag=errorcodefixes-20) \| Match exact HP, voltage, and rotation direction |
| Run capacitor | [Amazon](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-lennox-error-code-223&tag=errorcodefixes-20) \| Test before replacing motor — often the actual failure point |
| Pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-lennox-error-code-223&tag=errorcodefixes-20) \| Replace if switch fails to close with confirmed draft present |
## When to Call a Pro

If the inducer motor is confirmed running and the pressure switch still won't close, the furnace may have a blocked or undersized venting system. Flue system evaluation and correction require proper tools and training to avoid creating a carbon monoxide hazard.

## Related Articles

- [Lennox Error Code 292 — Ignition Failure Fix](/posts/lennox-292-error-code/)
- [Lennox EL296V Error Codes — Variable-Speed Furnace Diagnostic Guide](/posts/lennox-el296v-error-codes/)
- [Lennox Elite Series Furnace Error Codes — Fault Code Diagnostic Guide](/posts/lennox-elite-series-furnace-codes/)
- [Lennox 103 Error Code — Causes & Fix](/posts/lennox-error-code-103/)
- [Lennox Error Code 111 — Causes & Fix](/posts/lennox-error-code-111/)

## See Also

- [Lennox Error Code 225 — Causes & Fix](/posts/lennox-error-code-225/)
- [Lennox Furnace Error Codes — Complete Reference Guide](/posts/lennox-furnace-error-codes/)
- [Lennox XP20 Heat Pump Error Codes - Full iComfort Fault Reference](/posts/lennox-xp20-heat-pump-error-codes/)
- [Lennox Error Code 114 — Causes & Fix](/posts/lennox-error-code-114/)
