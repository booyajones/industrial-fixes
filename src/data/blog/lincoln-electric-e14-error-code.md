---
title: "Lincoln Electric E14 Error Code — Causes & Fix"
description: "What Lincoln Electric E14 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T10:00:00Z
modDatetime: 2026-04-22T10:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - welding
  - lincoln-electric
money_part: "Input voltage selector switch"
---

## Lincoln Electric E14 Error Code — What It Means

The E14 fault on Lincoln Electric welders indicates an input voltage fault — the incoming power supply is outside the machine's acceptable operating range. Lincoln's power electronics monitor incoming line voltage continuously; if it drops too low, spikes too high, or loses a phase (on three-phase machines), E14 trips and disables output to protect the internal components.

[Jump to Fix](#fix)

## Common Causes

- **Low line voltage (brown-out)** — Voltage sag from an undersized circuit, long extension cord, or facility power issues drops input below the machine's minimum. Common cause in shops running multiple large loads simultaneously.
- **Incorrect input voltage setting** — Many Lincoln welders have a voltage selector switch or dual-voltage capability. If the machine is set for 230V and connected to 460V, or vice versa, E14 will trip immediately.
- **Phase loss on three-phase machines** — A tripped breaker on one leg, a loose connection at the disconnect, or a failed contactor contact removes one phase and triggers the fault.
- **Voltage spike or surge** — A power surge from grid events or nearby equipment switching can trip E14. Usually clears on power cycle if no damage occurred.

## Step-by-Step Fix {#fix}

1. **Check the input voltage selector** — Locate the voltage selector switch (usually behind the side panel or near the input terminals). Confirm it matches your supply voltage exactly. Wrong setting = immediate E14.
2. **Measure incoming line voltage** — Use a multimeter at the input terminals or receptacle. Measure all phases if three-phase. Compare to nameplate spec (typically ±10% of rated voltage). Low or unbalanced voltage is the issue.
3. **Check the circuit breaker and connections** — Inspect the dedicated breaker for the welder and the disconnect if present. A tripped breaker on one phase of a three-phase supply causes E14 without being obvious at the panel.
4. **Eliminate extension cords** — If running on an extension cord, check the gauge. A 50-amp welder needs 8AWG or heavier for runs under 25 feet; longer or thinner cords cause voltage drop. Plug directly into the panel if possible.
5. **Power cycle and test** — After correcting the input issue, power cycle the welder. E14 should clear. If it returns immediately, the input power module may have failed.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input voltage selector switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lincoln-electric-e14-error-code&k=Input+voltage+selector+switch&tag=errorcodefixes-20) \| Replace if damaged or contacts are pitted |
| Line filter / EMI filter | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lincoln-electric-e14-error-code&k=Line+filter+%2F+EMI+filter&tag=errorcodefixes-20) \| If power quality is poor and causing recurring E14 |
| Input contactor / rectifier module | [Amazon](https://www.amazon.com/dp/B0CJFZQVPT?ascsubtag=ecf-lincoln-electric-e14-error-code&tag=errorcodefixes-20) \| If fault persists after confirming correct input voltage |
## When to Call a Pro

If input voltage is confirmed correct and E14 still trips, the input rectifier or control board has failed internally. Lincoln Electric authorized service is needed for power module diagnosis and replacement.
