---
title: "Navien Error Code E004 — Causes & Fix"
description: "What Navien error code E004 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - boiler
  - navien
---

## Navien Error Code E004 — What It Means

Navien error code E004 indicates false flame detection — the flame sensor detected a flame signal when the gas valve should be closed and no combustion should be occurring. This is a safety fault. The control board expects the flame sensor to read zero (no ionization signal) before opening the gas valve, as part of its pre-ignition check. If it sees ionization current at that moment, it interprets this as either a flame sensor failure, a gas valve leaking through, or electrical interference on the flame detection circuit. The unit locks out and will not attempt ignition until the fault is cleared.

[Jump to Fix](#fix)

## Common Causes

- **Flame sensor contaminated or shorted** — Carbon deposits, moisture, or a damaged insulator on the flame sensor rod create a false ionization signal. The sensor reads "flame present" even in a cold burner.
- **Gas valve not seating fully** — A pilot leak or main valve seat leak allows a small standing flame or flammable gas presence that produces a real (not false) ionization signal before the ignition sequence starts.
- **Electrical interference on flame circuit** — Grounding issues, a nearby variable frequency drive, or a loose chassis bond can induce voltage on the flame sense lead that mimics ionization current.
- **Failed control board** — The flame sense input circuit on the PCB malfunctions and registers current even with a clean, open-circuit sensor. This is rare but confirmed by testing with a new sensor.

## Step-by-Step Fix {#fix}

1. **Inspect the flame sensor rod and lead** — Locate the flame sensor inside the burner compartment. Check for carbon buildup on the ceramic insulator or the rod tip. Clean the rod with fine emery cloth. Verify the insulator is not cracked.
2. **Check sensor wire routing** — The flame sensor wire must not contact any metal surfaces. A grounded wire mimics ionization. Re-route if chafing is found.
3. **Test sensor isolation** — With the unit off, disconnect the flame sensor wire at the board. Measure resistance from the sensor lead to chassis ground. It should be near infinite. Any measurable resistance indicates a grounding fault.
4. **Confirm gas valve seating** — After the unit shuts down, observe the burner for several seconds with a flashlight. Any visible flame or glow indicates the valve is leaking through and requires replacement.
5. **Reset and monitor** — Clear the fault by pressing the reset button. If E004 clears and the unit ignites and runs normally, the issue was likely a momentary contamination event. If it returns immediately, the gas valve or PCB requires replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame sensor | [Amazon](https://www.amazon.com/dp/B0CZ7M9V4D?ascsubtag=ecf-navien-error-code-e004&tag=errorcodefixes-20) \| Navien units use an integrated sensor/igniter on some models; verify separately serviceable |
| Gas valve assembly | [Amazon](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-navien-error-code-e004&tag=errorcodefixes-20) \| Replace only if confirmed leaking; this is a licensed gas technician job |
| Control PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-error-code-e004&k=Control+PCB&tag=errorcodefixes-20) \| Replace if sensor and valve are confirmed good but fault persists |
## When to Call a Pro

A gas valve that leaks through (allowing gas or flame when closed) is a serious safety hazard. Gas valve replacement must be performed by a licensed plumber or HVAC technician. Do not attempt to operate the unit if you suspect a leaking gas valve.

## Related Articles

- [Navien Error Code E001 — No Ignition Fix](/posts/navien-error-code-e001/)
- [Navien E002 Error Code — Causes & Fix](/posts/navien-error-code-e002/)
- [Navien Error Code E003 — Ignition Failure Fix](/posts/navien-error-code-e003-ignition-failure/)
- [Navien E006 Error Code — Causes & Fix](/posts/navien-error-code-e006/)
- [Navien Error Code E007 — Causes & Fix](/posts/navien-error-code-e007/)

## See Also

- [Navien Error Code E016 — Causes & Fix](/posts/navien-error-code-e016/)
- [Navien Error Code E013 — Causes & Fix](/posts/navien-error-code-e013/)
- [Navien Tankless Water Heater Error Codes — Complete Guide](/posts/navien-error-codes/)
- [Navien NPE/NCB Code E003 — Ignition Failure Fix](/posts/navien-error-code-e003/)
