---
title: "Navien Error Code E016 — Causes & Fix"
description: "What Navien error code E016 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - boiler
  - navien
---

## Navien Error Code E016 — What It Means

Navien error code E016 indicates a hot surface igniter fault. The control board attempted to verify that the igniter reached operating temperature before opening the gas valve, and the igniter circuit returned an abnormal current or resistance reading. On Navien tankless heaters and combi-boilers, the hot surface igniter (silicon nitride) pre-heats to approximately 1800°F before gas is introduced. If the igniter is cracked, burned out, or the circuit is open, no ignition is possible and E016 is logged. This is one of the most straightforward Navien faults to repair.

[Jump to Fix](#fix)

## Common Causes

- **Cracked or burned-out igniter** — Silicon nitride igniters have a typical service life of 3–7 years under normal cycling. Physical cracks are often visible on inspection; electrically, a failed igniter reads as open circuit (OL on resistance test).
- **Loose igniter wire connector** — The spade or plug connector at the igniter terminal can work loose due to thermal cycling, vibration, or handling during filter maintenance.
- **Igniter circuit wiring fault** — A broken wire or burnt insulation in the igniter harness between the PCB and igniter creates an open circuit the board detects as a failed igniter.
- **Failed igniter drive circuit on PCB** — The relay or triac that switches power to the igniter fails. This is confirmed by verifying correct voltage at the igniter terminals with the board calling for ignition.

## Step-by-Step Fix {#fix}

1. **Locate and inspect the igniter** — With the unit off and cooled, open the burner compartment. The hot surface igniter is adjacent to the burner assembly, often held by one or two screws. Look for visible cracks in the silicon nitride element.
2. **Test igniter resistance** — Disconnect the igniter wires and measure resistance across the two terminals. A good silicon nitride igniter typically reads 40–100 Ω when cold. Open circuit (OL) means the element is failed.
3. **Check the igniter connector and harness** — Inspect the connector and the wire run back to the PCB for any signs of burning, melted insulation, or loose terminals. Repair or replace as needed.
4. **Verify voltage at igniter during ignition sequence** — If resistance tests good, measure voltage at the igniter terminals when the unit should be in pre-heat (listen for the blower to start, then check voltage within a few seconds). No voltage indicates a PCB driver fault.
5. **Replace igniter and test** — Install the replacement igniter, reconnect the harness, and restore power. The unit should progress through preheat, ignite, and run without logging E016.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hot surface igniter (silicon nitride) | [Amazon](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-navien-error-code-e016&tag=errorcodefixes-20) \| Use Navien OEM part or confirmed compatible aftermarket |
| Igniter wire harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-error-code-e016&k=Igniter+wire+harness&tag=errorcodefixes-20) \| Replace if insulation is melted or connector is damaged |
| Control PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-error-code-e016&k=Control+PCB&tag=errorcodefixes-20) \| Replace only if igniter circuit output is confirmed missing |
## When to Call a Pro

If the igniter resistance is within spec and voltage is confirmed at the igniter but the unit still logs E016, the igniter may be failing under thermal load (measuring good cold but open when hot). A technician can perform in-situ resistance monitoring or perform a board-level diagnosis.

## Related Articles

- [Navien Error Code E001 — No Ignition Fix](/posts/navien-error-code-e001/)
- [Navien E002 Error Code — Causes & Fix](/posts/navien-error-code-e002/)
- [Navien Error Code E003 — Ignition Failure Fix](/posts/navien-error-code-e003-ignition-failure/)
- [Navien Error Code E004 — Causes & Fix](/posts/navien-error-code-e004/)
- [Navien E006 Error Code — Causes & Fix](/posts/navien-error-code-e006/)
