---
title: "Mitsubishi FR-E800 Fault E6 — Causes & Fix"
description: "What Mitsubishi FR-E800 Fault E6 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T14:00:00Z
modDatetime: 2026-04-22T14:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - mitsubishi
---

## Mitsubishi FR-E800 Fault E6 — What It Means

Fault E6 on the Mitsubishi FR-E800 inverter indicates a brake transistor fault — the internal braking transistor (used to dissipate regenerative energy during deceleration) has failed or is operating outside normal parameters. The FR-E800 monitors the braking transistor duty cycle and temperature; if the transistor shorts or the braking resistor circuit is open, E6 trips to prevent a DC bus overvoltage condition.

[Jump to Fix](#fix)

## Common Causes

- **Failed braking transistor** — The internal brake IGBT can fail short-circuit, triggering E6 immediately on power-up.
- **Braking resistor open or disconnected** — If an external braking resistor is specified and becomes open-circuit or disconnected, the transistor has no path to dissipate energy and the fault trips.
- **Braking resistor overheating/overload** — Excessive regenerative energy from a large inertia load overheats the braking resistor. Most resistors have a thermal switch that opens on overheat.
- **Deceleration time too short** — An aggressive decel ramp on a high-inertia load puts more energy into the braking circuit than it can handle.

## Step-by-Step Fix {#fix}

1. **Check for a shorted braking transistor** — With power off, measure resistance between the P/+ terminal and PR terminal. Near-zero resistance in both directions indicates a shorted transistor.
2. **Inspect the braking resistor** — Measure resistance across the braking resistor terminals (if external resistor installed). Open circuit = burned-out resistor. Check thermal fuse/switch on the resistor.
3. **Extend deceleration time** — Increase Pr.8 (Deceleration Time) to reduce regenerative current per unit time. This is the first parameter fix to try before replacing hardware.
4. **Check wiring to braking resistor** — Verify the resistor is connected between P/+ and PR terminals with correct wire gauge. Loose connections cause intermittent E6.
5. **Reset and test** — After repair, cycle power and run a ramp-down cycle. Confirm E6 does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Braking resistor | Match to FR-E800 frame size and duty cycle requirement |
| FR-E800 inverter unit | If internal brake transistor has failed |

## When to Call a Pro

Internal braking transistor replacement requires drive disassembly and component-level repair. Mitsubishi authorized service handles transistor-level repairs for FR-E800 units.
