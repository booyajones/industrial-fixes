---
title: "Daikin U4 Error Code — Indoor-Outdoor Communication Fix"
description: "Daikin U4 means the indoor head and the outdoor condenser stopped talking on the F1/F2 communication bus. Nine times out of ten it's a wiring problem — a..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: daikin-error-code-u4
featured: false
draft: false
tags:
  - daikin
  - hvac
  - error-codes
  - indoor-outdoor-communication
---
## Quick answer

Daikin U4 means the indoor head and the outdoor condenser stopped talking on the F1/F2 communication bus. Nine times out of ten it's a wiring problem — a backstabbed terminal, reversed F1/F2 polarity, or a nicked conductor under the saddle clamp at the outdoor unit — not a failed PCB.

## What U4 means on a Daikin mini split

U4 (sometimes shown as "U4-XX" on the BRC1E remote or the outdoor 7-segment display) is a communication-error code that covers the entire half-duplex serial link between the indoor PCB and the outdoor inverter PCB. Daikin runs the indoor and outdoor units on a polarity-sensitive two-wire bus labeled F1 (positive) and F2 (negative). The indoor head transmits a poll, the outdoor responds with its status frame, and if the indoor doesn't see a valid frame back within the firmware timeout window — generally about 3 minutes of continuous silence on most RA, RX, and FTXS platforms — the indoor logs U4 and parks the call.

On VRV and Sky Air commercial equipment, U4 also covers the F1/F2 link between outdoor units in a multi-module condenser group, and on RXYQ series VRV systems it can include the Q1/Q2 link to the BS box or BRC controller. For residential RX/RXS/RXL split systems and the FTX/CTX wall-mount and ducted heads, U4 is almost always the simple two-wire indoor-outdoor link.

Daikin's U4 doesn't tell you *which* direction the link broke. The indoor could be transmitting fine and not hearing the outdoor, or the outdoor could be deaf to the indoor. Your meter and a few minutes at each terminal block answers that question faster than swapping boards.

## Common causes (ranked by frequency)

1. **Loose or backstabbed F1/F2 terminal** — most common on installations where the installer pushed the conductor in past the strip line or didn't fully torque the terminal screw.
2. **Reversed F1/F2 polarity** — Daikin is polarity sensitive. F1 to F1, F2 to F2. Reverse them and you get U4 even with a perfect wire run.
3. **Nicked or pinched communication conductor** — typically at the saddle clamp where the line set passes through the outdoor base pan or at the strain relief on the indoor head.
4. **Wrong wire type** — stranded thermostat wire under 18 AWG, untwisted pairs, or shielded cable with the shield grounded at both ends will all give intermittent U4 once the run gets past about 50 feet.
5. **Tripped outdoor breaker or blown F1U fuse on the outdoor PCB** — the indoor still has power and a display, the outdoor is dark, so the link goes silent and U4 latches.
6. **Failed indoor or outdoor PCB transceiver** — real but rare. Always last on the list, never first.
7. **Lightning or surge damage** — line surge that took out the optocoupler on one or both transceiver circuits. Usually accompanied by an L5 or other compressor-side code on top of U4.

## Step-by-step fix

1. **Verify both units have line power and the outdoor breaker is on.** Sounds dumb, takes 30 seconds, and rules out half the U4 calls I get. Open the outdoor disconnect, check for 208/230 VAC at L1-L2 on the outdoor terminal block. Open the indoor breaker, confirm the indoor head is energized and displaying U4 (a dead display points to a different problem entirely). On RX series outdoor units, also verify the F1U glass fuse on the inverter PCB — it's typically a 3.15 A 250 V fast-acting, Daikin part 4017019 series, and a pop on F1U kills outdoor power and gives U4 at the indoor.

2. **Power both units down at the breakers and let them sit for at least 3 minutes.** The inverter capacitors take that long to bleed off, and you do not want to be probing live terminals on a Daikin inverter PCB. The bus capacitor can hold 380 VDC after AC is removed.

3. **Inspect both terminal blocks visually first.** Pull the service covers on the outdoor unit and the front grille on the indoor head. Look at the F1/F2/ground terminal block on both ends. You're looking for: insulation pulled past the strip line, conductor strands sticking out and bridging to ground, daisy chains pinched under a single screw, or — and I see this every other week — F1 and F2 reversed between the two ends. Verify F1 at indoor lands on F1 at outdoor.

4. **Ohm out the F1/F2 conductors with the units dead.** Disconnect F1 and F2 at the outdoor terminal block. At the indoor, jumper F1 to F2 with a piece of wire. Back at the outdoor, you should read continuity (under 1 Ω for short runs, 2-4 Ω for 100+ foot runs of 18 AWG) between F1 and F2. Remove the jumper and you should read open between F1 and F2, and open between either conductor and ground. Anything else points to a wire fault between the two units.

5. **Inspect the saddle clamps and strain reliefs.** This is where I find the actual fault on maybe 30% of U4 calls. The line-set saddle on the outdoor base pan is sharp metal, and if the installer routed the comm cable under it without a grommet, the insulation eventually wears through and one conductor grounds out. Pull the cable out of the saddle, inspect every inch under good light, and re-route with a rubber grommet or a piece of split loom.

6. **Verify wire type and gauge.** Daikin specifies a 16-18 AWG twisted-pair shielded cable for runs over 50 feet, and ungrounded shield (shield connects at one end only, normally outdoor). Untwisted lamp cord or doorbell wire will work on a 20-foot run and fail intermittently at 60 feet. If the installer used the wrong wire, you're chasing your tail until you replace it.

7. **Restore power, indoor first, then outdoor, wait 3 minutes.** Watch the outdoor 7-segment display (if equipped) and the indoor BRC1E or wall remote. If U4 clears, run a cooling call and watch for 10 minutes — intermittent U4 will come back under vibration when the compressor starts.

8. **If U4 persists with verified wiring and power at both ends, check transceiver supply voltage.** With the units powered and idle, you should measure approximately 16 VDC ± 2 V between F1 and F2 at either terminal block, polarity F1 positive. No voltage means the outdoor transceiver isn't sourcing the bus — outdoor PCB is suspect. Voltage present but no communication means the indoor isn't responding — indoor PCB or a logic-level issue. Daikin publishes specific PCB part numbers by model; the RX series outdoor PCBs commonly are 5009566 family and the indoor controllers vary by head style.

> **Field knowledge nugget:** On Daikin RX-S and FTX-N series installed between roughly 2018 and 2022, I've seen a specific U4 failure pattern where the installer used 4-conductor 18 AWG stranded with PVC jacket and ran it bundled inside the line-set insulation tape. Heat from the suction line raises the cable temperature, the PVC softens, and over two summers the insulation between F1 and the ground/chassis conductor eventually breaks down. The unit runs fine all winter, throws U4 intermittently in July and August, and the fault clears when ambient drops below 80 °F. If you have an RX-N installed under taped line-set insulation and seasonal U4s, plan on pulling new comm cable through new conduit outside the line-set wrap, not inside it. Daikin specifies the cable should be separately routed.

**Safety:** Newer Daikin residential equipment shipped after January 2025 (most RX-V and several Quaternity heat-pump models) uses **R-454B refrigerant, which is an A2L mildly flammable refrigerant**. U4 work is electrical and doesn't normally touch the refrigerant circuit, but if you end up brazing or opening service ports on an R-454B unit, you must follow UL 60335-2-40 charge-limit rules, ensure ventilation, kill all ignition sources within the room volume, and use spark-resistant tools. Standard R-410A practices are *not* sufficient. The lower flammability limit for R-454B is approximately 11.9% by volume, and a 1.5 lb leak in a small mechanical closet can hit LFL quickly. EPA 608 certification with A2L training is now required.

## Parts that may need replacement

| Part | OEM Number (typical) | Typical Cost | Where to Buy |
|---|---|---|---|
| Outdoor inverter PCB (RX series) | 5009566-xx (varies by sub-model) | $385–$620 | [HVAC Parts Shop](https://www.hvacpartsshop.com) / [Grainger](https://www.grainger.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=daikin-error-code-u4) |
| Indoor controller PCB (FTX wall mount) | 4017019-xx (varies) | $245–$380 | [HVAC Parts Shop](https://www.hvacpartsshop.com) / [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| F1U fuse 3.15A 250V fast | 4017019 series glass fuse kit | $8–$18 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) / [Grainger](https://www.grainger.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=daikin-error-code-u4) |
| Communication cable, 18/2 twisted shielded, 100 ft | Honeywell Genesis 2110 | $65–$95 | [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=daikin-error-code-u4) / [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Line-set rubber grommet kit | Rectorseal Kit | $12–$22 | [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=daikin-error-code-u4) |

Always order the gasket and harness clips with a PCB — Daikin board kits sometimes ship without and you need both for warranty.

## When to call a professional

Call a NATE-certified mini-split tech if any of these apply:

- The unit uses R-454B and you don't have A2L training and certification.
- You measure 16 VDC F1-F2 at the outdoor terminal block but zero at the indoor, with confirmed good wire. That's an open in the run between, and finding it inside a finished wall is a job for someone with a tone-and-probe set.
- The outdoor inverter PCB has any visible scorching, swelling on the bus capacitors, or smells of burnt varnish. That's a Daikin warranty job — opening it yourself voids the 10-year parts coverage on residential units.
- You see L5, L4, F3, or any P-code stacked on top of the U4. Multiple codes mean a power-section problem, not a comm problem, and that's a refrigerant-side diagnosis.
- The system is a VRV or Sky Air multi-zone — VRV F1/F2 with addressing and termination resistors is its own discipline and worth a phone call to Daikin tech support before guessing.

## FAQs

**Will resetting the breaker clear a Daikin U4 by itself?**
Only if the underlying fault was transient (a brief surge, a momentary breaker trip). If the wiring or PCB is the actual problem, U4 will come back within 3 minutes of power-up. Don't keep cycling the breaker — repeated power cycling stresses the inverter bus capacitors.

**Can I use thermostat wire for the Daikin F1/F2 link?**
For runs under 50 feet, 18 AWG stranded thermostat wire works. Over 50 feet, Daikin specifies twisted-pair shielded comm cable, and you'll have intermittent U4 issues with plain thermostat wire on longer runs, especially near AC line voltage or fluorescent ballasts.

**Why does my Daikin U4 only show up when the compressor starts?**
That's a classic chafed-conductor symptom. Compressor inrush vibrates the line set, the line set moves slightly in the saddle clamp, and the damaged conductor briefly shorts or opens. Pull the cable out of the saddle and inspect it.

**Is U4 the same on Daikin VRV as on residential split systems?**
The code name is the same but the bus is different. VRV uses F1/F2 between outdoor modules and Q1/Q2 to controllers, with addressing and a 100 Ω termination resistor at the end of the chain. Residential RX/FTX systems are simple point-to-point F1/F2 with no addressing. A U4 on VRV could be a termination resistor missing or an address conflict, neither of which exists on residential.

**Does U4 indicate refrigerant problems?**
No. U4 is purely a communication fault. If you have U4 stacked with an L-series or P-series code, the L or P is the refrigerant or compressor problem and U4 is collateral damage from the outdoor PCB losing its mind. Fix the L/P first, U4 usually clears.

## Related guides

- [Daikin UA Error Code — Mismatched Indoor/Outdoor Unit Fix](/posts/daikin-error-code-uA)
- [Daikin L5 Error Code — Compressor Lock Fix](/posts/daikin-error-code-l5)
- [Daikin C4 Error Code — Indoor Heat Exchanger Thermistor Fix](/posts/daikin-error-code-c4)

## See Also

- [Daikin RXYQ VRV System Error Codes — Complete Fault Code Guide](/posts/daikin-rxyq-error-codes/)
- [Daikin U2 Error Code — Causes & Fix](/posts/daikin-u2-error-code/)
- [Daikin R-32 System U4 Error Code — Communication Fault Fix](/posts/daikin-r32-error-code-u4/)
- [Daikin E7 Error Code — Outdoor Fan Motor Fault Fix](/posts/daikin-e7-error-code/)
