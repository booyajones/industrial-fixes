---
title: "Mitsubishi FR Series VFD Fault E6 — Causes & Fix"
description: "What Mitsubishi FR series VFD fault E6 means, why the brake transistor fault trips, and how to diagnose and fix it."
pubDatetime: 2026-04-22T11:00:00Z
modDatetime: 2026-04-22T11:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - mitsubishi
---

## Mitsubishi FR Series Fault E6 — What It Means

E6 (or E.6) on a Mitsubishi FR series VFD (FR-A700, FR-A800, FR-E700, FR-E800) indicates a brake transistor fault. The drive detected an anomaly in the built-in brake circuit — either the brake transistor has failed, the braking resistor is open or short-circuited, or the brake circuit detected excessive on-time indicating a thermal protection condition. The drive stops to prevent damage to the brake transistor and resistor.

[Jump to Fix](#fix)

## Common Causes

- **Failed brake transistor (IGBT)** — The internal brake transistor has shorted or opened. A shorted transistor causes continuous resistor current; an open transistor means no braking capability and bus voltage rise.
- **Open or shorted braking resistor** — The external braking resistor has burned out (open circuit) or shorted. An open resistor prevents energy dissipation; a shorted resistor draws excessive continuous current.
- **Braking resistor overload (thermal protection)** — The resistor has been used beyond its duty cycle rating, and the drive's thermal model tripped E6 to protect the resistor from burning out.
- **Wiring fault at the PR/P+ terminals** — A loose or incorrect connection between the drive's brake terminals and the external resistor causes abnormal brake circuit behavior.

## Step-by-Step Fix {#fix}

1. **Power down the drive and wait for DC bus discharge** — Turn off the input breaker and wait at least 5 minutes for the DC bus capacitors to discharge to a safe level before touching internal components.
2. **Measure the braking resistor** — Disconnect the braking resistor from the PR and P+ terminals. Measure resistance with a multimeter. The resistance should match the resistor's rated value (e.g., 20Ω, 40Ω). An open (OL) reading means the resistor has burned out; a very low reading (near 0Ω) means it has shorted.
3. **Inspect the braking resistor for visible damage** — Look for burned windings, melted insulation, or carbonized resistor wire. Any visible damage confirms resistor failure.
4. **Check the PR/P+ wiring** — Verify the wiring between the drive's brake terminals and the resistor is correct, tight, and properly sized for the resistor's current rating.
5. **Test the brake transistor** — If the resistor tests good, the brake transistor (IGBT) may have failed. This requires a technician with power electronics test equipment or a replacement drive for comparison testing.
6. **Reduce braking duty cycle** — If thermal overload is the cause, review the deceleration rate (Pr.8) and the braking duty cycle. Extend the decel time or upgrade to a higher-duty braking resistor.
7. **Reset the fault and test** — After replacing the failed component, restore power, clear E6 via the parameter unit or reset terminal, and test through a full deceleration cycle.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Braking resistor | [Amazon](https://www.amazon.com/s?i=industrial&k=Braking+resistor&tag=errorcodefixes-20) \| Match to Mitsubishi FR drive model; verify Ω rating and wattage |
| Brake transistor / drive power board | [Amazon](https://www.amazon.com/s?i=industrial&k=Brake+transistor+%2F+drive+power+board&tag=errorcodefixes-20) \| Replace if transistor is confirmed failed; typically requires whole board |
| Braking resistor wiring | [Amazon](https://www.amazon.com/s?i=industrial&k=Braking+resistor+wiring&tag=errorcodefixes-20) \| Use wire rated for resistor peak current; keep leads short |
## When to Call a Pro

Brake transistor testing and power board replacement require power electronics expertise. A Mitsubishi Electric-authorized drive service technician can test the brake circuit under load and replace the internal brake components correctly.

## Related Articles

- [Mitsubishi City Multi P8 / E6 Error Codes — Causes & Fix](/posts/mitsubishi-city-multi-error-codes/)
- [Mitsubishi PEX City Multi Error Codes (Indoor Unit): Complete Guide](/posts/mitsubishi-city-multi-pex-error/)
- [Mitsubishi CNC Alarm 500 — Causes & Fix](/posts/mitsubishi-cnc-alarm-500/)
- [Mitsubishi CNC Alarm Y96 — Causes & Fix](/posts/mitsubishi-cnc-alarm-y96/)
- [Mitsubishi E1 Error Code — Indoor/Outdoor Communication Fault Fix](/posts/mitsubishi-e1-error-code/)
