---
title: "LG Mini-Split CH05 Error Code — Causes & Fix"
description: "What LG mini-split CH05 means, why communication fails between indoor and outdoor units, and how to fix it."
pubDatetime: 2026-04-22T10:00:00Z
modDatetime: 2026-04-22T10:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - mini-split
  - lg
---

## LG Mini-Split CH05 Error Code — What It Means

CH05 on an LG mini-split system indicates a communication error between the indoor unit and the outdoor unit. The two units communicate over a serial data line (typically a two- or three-conductor signal wire running alongside the power wires). When the control boards on either end stop receiving valid signals from each other, CH05 is displayed and the system shuts down to prevent operating in an unknown state.

[Jump to Fix](#fix)

## Common Causes

- **Loose, damaged, or miswired communication wire** — The signal wire (labeled "S" or "C" on LG systems) is fragile compared to power conductors. A loose terminal, nicked insulation, or reversed polarity will break communication.
- **Power supply interruption to outdoor unit** — If the outdoor unit loses power, the indoor unit loses communication and shows CH05. Check outdoor unit power before assuming a wiring fault.
- **Failed indoor or outdoor control board** — A board with a damaged communication IC or UART circuit cannot send or receive serial data.
- **Electrical interference** — Running the communication wire in the same conduit as high-voltage power wiring (without shielding) can introduce noise that corrupts the serial signal.

## Step-by-Step Fix {#fix}

1. **Check outdoor unit power** — Confirm the outdoor unit disconnect is on and the breaker is not tripped. The outdoor unit must be powered for communication to occur.
2. **Inspect communication wiring at both ends** — Power off both units. At the indoor unit terminal block and the outdoor unit terminal block, check that the communication wire (terminal S or C) is seated firmly. Look for discoloration, corrosion, or damaged insulation.
3. **Verify correct terminal connections** — Confirm the indoor and outdoor unit terminal designations match (LG uses 1, 2, 3 or L1, L2, S labeling). A crossed wire or swapped terminal breaks communication completely.
4. **Test the communication wire for continuity** — With power off, use a multimeter to check end-to-end continuity of the signal wire. Infinite resistance = wire break; replace the wire run.
5. **Power cycle both units** — With all connections verified, restore outdoor power first, wait 30 seconds, then restore indoor power. CH05 should clear if the wiring was the cause.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Communication wire (2 or 3-conductor) | [Amazon](https://www.amazon.com/s?k=Communication+wire+%282+or+3-conductor%29&tag=errorcodefixes-20) \| 18-22 AWG; run separately from power wiring |
| Indoor unit control board | [Amazon](https://www.amazon.com/s?k=Indoor+unit+control+board&tag=errorcodefixes-20) \| Replace if board communication IC is confirmed failed |
| Outdoor unit control board | [Amazon](https://www.amazon.com/s?k=Outdoor+unit+control+board&tag=errorcodefixes-20) \| Replace if outdoor board is the confirmed fault |
| Terminal block connectors | [Amazon](https://www.amazon.com/s?k=Terminal+block+connectors&tag=errorcodefixes-20) \| Replace corroded terminals before replacing boards |
## When to Call a Pro

If wiring is confirmed correct and power is present at both units but CH05 persists, a licensed HVAC technician with LG service tools can pull diagnostic logs from the control boards to identify which board is the communication fault source.

## Related Articles

- [Bosch Heat Pump E1 Error Code — Causes & Fix](/posts/bosch-heat-pump-e1-error-code/)
- [Carrier 24ANA Heat Pump Error Codes — Performance Series Diagnostic Guide](/posts/carrier-24ana-heat-pump-error-codes/)
- [Carrier Heat Pump E1 Error Code — Causes & Fix](/posts/carrier-heat-pump-e1-error-code/)
- [Carrier Heat Pump E4 Error Code — Causes & Fix](/posts/carrier-heat-pump-e4-error-code/)
- [Carrier Heat Pump E5 Error Code — Defrost Fault: Causes & Fix](/posts/carrier-heat-pump-e5-error-code/)
