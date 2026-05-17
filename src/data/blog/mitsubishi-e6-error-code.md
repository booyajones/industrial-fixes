---
title: "Mitsubishi Mini Split E6 Error Code Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-07T08:00:00Z
modDatetime: 2024-03-07T08:00:00Z
slug: mitsubishi-e6-error-code
featured: true
draft: false
tags:
  - hvac
  - mitsubishi
  - mini-split
  - communication
  - wiring
description: "Mitsubishi mini split E6 error code means a communication failure between the indoor and outdoor units. Here's how to diagnose wiring, boards, and connection issues."
---

## Error Code: Mitsubishi Mini Split E6

**What it means:** E6 is a serial communication error between the indoor air handler and the outdoor condensing unit. The two units communicate over a dedicated signal wire (typically the S-wire, terminal 3 on most Mitsubishi linesets). When the indoor unit stops receiving data packets from the outdoor unit — or vice versa — the system throws E6 and shuts down to prevent operation in an unknown state.

E6 is a wiring or board issue, not a refrigerant or mechanical issue. The fix is almost always electrical.

## Common Causes

- **Damaged or disconnected communication wire** — The S-wire (control wire, typically white or brown in the interconnecting cable) was nicked, stapled through, or disconnected during installation or a service call. This is the leading cause of E6 on new installations.
- **Reversed or incorrect wiring at one of the terminal blocks** — Terminals 1, 2, and 3 must be correctly matched between indoor and outdoor units. A single wire on the wrong terminal kills communication.
- **Power surge or lightning strike** — A surge can damage the communication circuitry on one or both control boards while leaving the rest of the system intact.
- **Failed outdoor unit control board** — The outdoor PCB is responsible for initiating the communication protocol. A failed board transmits nothing, and the indoor unit throws E6.
- **Failed indoor unit PCB** — Less common, but the indoor board can also fail to receive or transmit correctly.
- **Loose terminal connections** — Vibration over years of operation can loosen terminal screws, creating intermittent contact that causes E6 faults that come and go.

## Step-by-Step Fix {#step-by-step-fix}

1. **Kill power to both indoor and outdoor units.** Flip the outdoor disconnect and the indoor breaker. Wait 60 seconds for capacitors to discharge.

2. **Inspect the communication wire at both ends.** At the indoor unit, remove the service panel and find the terminal block (usually labeled 1, 2, 3 or L1, L2, S). Confirm each wire is secured, not corroded, and on the correct terminal. Photograph the wiring before touching anything. Repeat at the outdoor unit terminal block.

3. **Check for physical wire damage along the lineset.** Walk the entire run of the control wire from indoor to outdoor. Look for staples through the wire, pinched sections under cladding, cuts, or rodent damage. A wire damaged mid-run will need a splice or full replacement.

4. **Verify terminal tightness.** With a small flathead, gently tighten each terminal screw at both ends. Loose terminals on the communication wire are a documented cause of intermittent E6 faults that worsen over time.

5. **Measure continuity on the S-wire.** With both units powered off and the S-wire disconnected at the outdoor unit terminal block, use a multimeter to measure continuity from the S-wire indoor terminal to the loose S-wire end at the outdoor unit. Should show near-zero resistance. High resistance or open circuit = wire damage.

6. **Swap the communication wire if damaged.** The control wire is typically 14/3 or 14/4 stranded wire. If damaged, run a new wire alongside the existing lineset. Ensure it's not bundled tightly against the refrigerant lines for long runs (interference is rare but documented).

7. **Restore power and observe startup.** Power on both units. The outdoor unit should start communicating within 30 seconds of power restoration. E6 should clear. If it clears and then returns after a few minutes of operation, the board is likely failing intermittently under load.

8. **If wiring is confirmed good, test the outdoor PCB.** With a licensed tech and service documentation, verify the outdoor board is transmitting on the S-wire using an oscilloscope or Mitsubishi service tool. A board that shows no signal output needs replacement.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Where to Buy | Typical Cost |
|------|-------------|-------------|
| Outdoor unit main PCB (model-specific, e.g., T7WE24032) | [Amazon](https://www.amazon.com/s?i=industrial&k=Outdoor+unit+main+PCB+%28model-specific%2C+e.g.%2C+T7WE24032%29&tag=errorcodefixes-20) \| HVAC Parts Shop, eBay OEM | $180–$400 |
| Indoor unit main PCB (model-specific) | [Amazon](https://www.amazon.com/s?i=industrial&k=Indoor+unit+main+PCB+%28model-specific%29&tag=errorcodefixes-20) \| HVAC Parts Shop, Mitsubishi dealer | $120–$350 |
| 14/3 communication wire (per foot) | [Amazon](https://www.amazon.com/s?i=industrial&k=14%2F3+communication+wire+%28per+foot%29&tag=errorcodefixes-20) \| Home Depot, Lowes | $0.50–$1.50/ft |
| Terminal block connector set | [Amazon](https://www.amazon.com/s?i=industrial&k=Terminal+block+connector+set&tag=errorcodefixes-20) \| Amazon, Grainger | $10–$25 |
## When to Call a Professional

If you've confirmed all wiring is correct and tight, continuity checks out on the communication wire, and E6 still appears — you need a tech with Mitsubishi service documentation and ideally a MelcoBEMS or oscilloscope to diagnose board-level communication. Board replacement is a straightforward swap but requires model-specific parts and confirmation that the replacement board has compatible firmware. Tell the tech: "E6 comm fault, wiring is confirmed correct at both terminal blocks, continuity is good on the S-wire. I suspect an outdoor board failure."

> **Pro tip:** On multi-zone Mitsubishi systems (one outdoor, multiple indoor units), E6 on a single indoor unit usually points to the individual zone's communication wire or its indoor PCB — not the outdoor unit. If all zones throw E6 simultaneously, the outdoor unit's board or power supply is the first thing to check.

## Related Articles

- [Mitsubishi City Multi P8 / E6 Error Codes — Causes & Fix](/posts/mitsubishi-city-multi-error-codes/)
- [Mitsubishi PEX City Multi Error Codes (Indoor Unit): Complete Guide](/posts/mitsubishi-city-multi-pex-error/)
- [Mitsubishi CNC Alarm 500 — Causes & Fix](/posts/mitsubishi-cnc-alarm-500/)
- [Mitsubishi CNC Alarm Y96 — Causes & Fix](/posts/mitsubishi-cnc-alarm-y96/)
- [Mitsubishi E1 Error Code — Indoor/Outdoor Communication Fault Fix](/posts/mitsubishi-e1-error-code/)
