---
title: "Midea Mini Split Error Code E3 — Causes & Fix"
description: "What Midea mini split error code E3 means, why communication fails between units, and how to fix it step by step."
pubDatetime: 2026-04-22T15:00:00Z
modDatetime: 2026-04-22T15:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - mini-split
  - midea
---

## Midea Mini Split Error Code E3 — What It Means

E3 on a Midea mini split signals a communication error between the indoor evaporator unit and the outdoor condensing unit. Midea's control system relies on a dedicated signal wire (often labeled S, 3, or SL) to pass status and command data between the two PCBs. If that signal is interrupted for more than a brief period, the indoor unit stops operating and displays E3. Midea's communication protocol is also used by many OEM brands including Pioneer (budget tier), Carrier Comfort (select models), and numerous private-label units.

[Jump to Fix](#fix)

## Common Causes

- **Loose or corroded S-wire connection** — Vibration from the outdoor unit loosens the communication wire at the terminal block. Moisture corrosion at the outdoor terminals is also common in coastal or high-humidity climates.
- **Damaged communication wire in the line set** — The signal wire can be cut, kinked inside conduit, or damaged by UV exposure on an exterior run.
- **Power supply imbalance** — Certain Midea models report E3 when the outdoor unit's power supply drops below minimum voltage, which starves the control board's communication circuit.
- **Failed indoor or outdoor PCB** — A lightning surge or voltage spike can damage the communication IC on either board, breaking the signal even with good wiring.

## Step-by-Step Fix {#fix}

1. **Cut power at the breaker** — Disconnect both the indoor and outdoor units and wait 2 minutes for capacitors to discharge.
2. **Check the outdoor terminal block** — Open the outdoor unit and inspect the terminal labeled S (or 3 or SL). It must be secure and free of corrosion. Clean with electrical contact cleaner if needed.
3. **Check the indoor terminal block** — Open the indoor unit wiring compartment and verify the same S terminal is tight and corrosion-free.
4. **Test the communication wire** — Disconnect at both ends and use a multimeter to check continuity (should be near 0 Ω) and no short to ground or other conductors.
5. **Verify supply voltage** — Confirm the outdoor unit is receiving the correct voltage (usually 208–230 VAC, single phase) within ±10%.
6. **Restore power and observe** — Power on both units. E3 should clear within 30 seconds if the wiring was the problem. Allow a full cooling or heating cycle to confirm stability.
7. **Replace boards if wiring is confirmed good** — If E3 persists with verified good wiring and correct voltage, replace the outdoor PCB first, then the indoor PCB if the problem continues.

## Parts Often Needed

| Part | Notes |
|------|-------|
| S-wire / communication wire | [Amazon](https://www.amazon.com/s?k=S-wire+%2F+communication+wire&tag=errorcodefixes-20) \| 18 AWG, 2–3 conductor; length to match the run |
| Outdoor control PCB | [Amazon](https://www.amazon.com/s?k=Outdoor+control+PCB&tag=errorcodefixes-20) \| Match Midea model number |
| Indoor control PCB | [Amazon](https://www.amazon.com/s?k=Indoor+control+PCB&tag=errorcodefixes-20) \| Replace if outdoor board swap does not resolve the fault |
## When to Call a Pro

If the line set wiring is enclosed in conduit or runs through multiple stories of a building, an HVAC technician with mini-split certification can trace and replace the communication wire without damaging the refrigerant lines.

## Related Articles

- [Bosch Heat Pump E1 Error Code — Causes & Fix](/posts/bosch-heat-pump-e1-error-code/)
- [Carrier 24ANA Heat Pump Error Codes — Performance Series Diagnostic Guide](/posts/carrier-24ana-heat-pump-error-codes/)
- [Carrier Heat Pump E1 Error Code — Causes & Fix](/posts/carrier-heat-pump-e1-error-code/)
- [Carrier Heat Pump E4 Error Code — Causes & Fix](/posts/carrier-heat-pump-e4-error-code/)
- [Carrier Heat Pump E5 Error Code — Defrost Fault: Causes & Fix](/posts/carrier-heat-pump-e5-error-code/)
