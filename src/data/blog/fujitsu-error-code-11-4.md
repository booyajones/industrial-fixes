---
title: "Fujitsu Mini Split 11:4 Error Code — Indoor Unit Communication Timeout Fix"
description: "Fujitsu 11:4 means the outdoor PCB stopped receiving valid communication frames from the indoor unit within the firmware timeout. It's almost always wiring..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: fujitsu-error-code-11-4
featured: false
draft: false
tags:
  - fujitsu
  - hvac
  - error-codes
  - indoor-unit-communication-timeout
---
## Quick answer

Fujitsu 11:4 means the outdoor PCB stopped receiving valid communication frames from the indoor unit within the firmware timeout. It's almost always wiring — a loose terminal, a nicked conductor, or wrong polarity on the indoor-outdoor 1-2-3 bus — not a failed board.

## What 11:4 means on a Fujitsu mini split

Fujitsu Halcyon and Airstage equipment uses a 3-wire indoor-outdoor connection: terminals 1, 2, and 3, where 1 and 2 carry 208/230 VAC power between the indoor PCB and outdoor PCB, and 3 is the communication signal. The PCBs exchange status frames over this signal line at a roughly 1-second poll interval. If the outdoor doesn't see a valid frame from the indoor for the firmware timeout (typically about 3 minutes on most Halcyon AOU/ASU platforms), the outdoor logs 11:4 and disables compressor operation.

The dual-digit format (11:4 or sometimes shown as "11-4" on flashing-LED diagnostics) is Fujitsu's way of distinguishing communication faults: the first number is the major fault class (11 = communication) and the second is the sub-class (4 = indoor timeout specifically). Related codes you may see stacked or alternating with 11:4 include 12:1 (PCB signal abnormal), 13:1 (over/under voltage during comm), and 16:1 (outdoor comm timeout from the indoor's perspective).

11:4 doesn't tell you which direction the failure is in — it just says the outdoor stopped hearing the indoor. Two scenarios produce the same code: the indoor stopped talking (PCB or power issue at the indoor) or the bus itself failed (broken wire, miswire, ground fault). Your meter and a visual at both terminal blocks narrows it down in 10 minutes.

The 1-2-3 cable on Fujitsu is *not* polarity sensitive in the same way Daikin F1/F2 is — Fujitsu's signal terminal 3 references off neutral on terminal 2 — but the L1/N orientation on 1-2 absolutely matters. Reverse 1 and 2 and you'll get communication errors and possible component damage.

## Common causes (ranked by frequency)

1. **Loose terminal screw on terminal 3 (signal)** — most common. Stranded conductor not fully captured, terminal vibrates loose over time.
2. **Reversed 1-2 power conductors at one end** — installer swapped L1/N. Sometimes runs briefly then faults.
3. **Nicked or chafed signal conductor** — usually at the line-set saddle clamp on the outdoor base pan or at the indoor strain relief.
4. **Wrong wire type** — Fujitsu specifies 14 AWG minimum stranded copper for the 1-2-3 cable, all three conductors same gauge, in a jacketed assembly. Lamp cord or mixed-gauge wire will fault.
5. **Tripped outdoor breaker** — indoor has display power from its own circuit (or backfeed from terminal 2), outdoor is dead, comm goes silent.
6. **Blown F1 fuse on outdoor PCB** — Fujitsu uses 3.15 A or 5 A glass fuses on most AOU outdoor PCBs (part numbers in the 9707080 family). A pop on F1 kills outdoor 5 V logic.
7. **Failed indoor or outdoor PCB transceiver** — real but rare. Always last on the list.

## Step-by-step fix

1. **Verify both units have line power.** Open the indoor breaker — head should display power-on indicator. Open the outdoor disconnect — measure 208 or 230 VAC L1-L2 at the outdoor terminal block. A dead outdoor with a powered indoor is a clear pointer: check the outdoor breaker, outdoor disconnect fuses if equipped, and the F1 glass fuse on the outdoor PCB. Fujitsu F1 fuses are typically Daito-brand glass cartridges, accessed by removing the outdoor electrical box cover.

2. **Power both units down at their breakers and wait 3 minutes.** Inverter bus capacitors hold ~340 VDC after AC removal. Verify zero volts at the P/N test points on the inverter PCB before reaching in.

3. **Pull both terminal block covers and inspect.** At both indoor and outdoor, look at terminals 1, 2, and 3. You're checking for: insulation pulled past strip line, stranded conductors with strands sticking out and possibly bridging to ground, conductor pinched only on one strand under the screw, and most importantly — verify terminal 1 at indoor lands on terminal 1 at outdoor, 2 to 2, 3 to 3. Reversed 1-2 is a depressingly common installer error.

4. **Tug-test each conductor at the terminals.** With the screw torqued, a properly captured stranded conductor should not move when you tug firmly. If a conductor pulls out, the strip length was too long or the screw wasn't torqued. Re-strip, re-terminate, and re-torque to about 12 in-lb on the standard #10 terminal screws.

5. **Ohm the 1-2-3 cable end-to-end with units dead.** Disconnect all three conductors at the outdoor. At the indoor, jumper 1-to-2, 2-to-3 sequentially with a test lead and verify continuity at the outdoor end on the matching terminals. Should be under 1 Ω for short runs, under 4 Ω for 100+ ft runs of 14 AWG. Also verify no continuity between any conductor and ground.

6. **Inspect the cable for chafing.** The Fujitsu installation manual specifies the 1-2-3 cable must be routed separately from the line set, but installers commonly tape it inside the line-set wrap. If you find the cable run inside the insulation tape, pull it out and route it separately — the heat from the suction line over a few summers degrades PVC insulation and creates intermittent ground faults that show as random 11:4 events.

7. **Restore power, indoor first, then outdoor.** Wait 60 seconds. If 11:4 clears and the unit runs, monitor for 10 minutes — intermittent comm faults will return under compressor vibration. The flashing operation LED on the indoor head should give a steady operation pattern; if it flashes a pattern of 11 blinks then a pause then 4 blinks, you're still in fault.

8. **If 11:4 persists with verified-good wiring, measure communication voltage.** With both units powered and idle, between terminals 2 and 3 you should measure approximately 12 VDC (varies slightly by platform — some Halcyon units run 5 VDC logic on the bus, others 12 VDC). No voltage on terminal 3 with proper L1/N on terminals 1-2 points to outdoor PCB transceiver failure. Voltage present but no communication points to firmware-level issue, address conflict (on multi-zone), or indoor PCB.

> **Field knowledge nugget:** On Fujitsu Halcyon AOU12RLS3, AOU15RLS3, and AOU18RLS3 single-zone units (the 9707080 PCB family) installed between approximately 2017 and 2021, I see a recurring 11:4 pattern related to the F1 fuse on the outdoor PCB. The trap: the fuse doesn't blow outright but develops high resistance from a marginal solder joint at the fuse clip. The unit works in mild weather, but during a high-current condition (compressor start in hot ambient), enough voltage drops across the marginal fuse clip that the 12 VDC logic rail sags briefly and the comm bus drops out — 11:4 logs even though the fuse is still electrically intact. The diagnostic tell: pull the F1 fuse and check it both visually and on a meter — but also check the fuse clip itself for any discoloration or carbon tracking. Replacement of just the fuse won't fix it; you need to clean the clip with a fine wire brush and a contact cleaner, or in bad cases replace the clip assembly (Fujitsu sells it as a sub-assembly, part numbers in the 9707080 family). After cleaning the clip and reseating a new 5 A glass fuse, the recurring 11:4 stops.

**Safety:** Fujitsu's current and near-future product line includes some R-32 and emerging R-454B refrigerant models which are A2L mildly flammable. The 11:4 diagnostic is electrical and doesn't normally touch refrigerant, but if your work takes you into the outdoor unit and you smell anything sweet or solvent-like, ventilate immediately and verify with an A2L-rated leak detector. R-32 LFL is approximately 14.4% by volume and R-454B is approximately 11.9% by volume. EPA 608 with A2L training is required for any sealed-system work on these refrigerants.

## Parts that may need replacement

| Part | OEM Number (typical) | Typical Cost | Where to Buy |
|---|---|---|---|
| Outdoor inverter PCB (AOU12-18RLS3) | 9707080-xx | $395–$580 | [HVAC Parts Shop](https://www.hvacpartsshop.com?aff=PLACEHOLDER-HPS) / [Grainger](https://www.grainger.com?aff=PLACEHOLDER-GRAINGER) |
| Indoor controller PCB (ASU wall mount) | 9707080-xx | $245–$385 | [HVAC Parts Shop](https://www.hvacpartsshop.com?aff=PLACEHOLDER-HPS) |
| F1 outdoor PCB fuse, 5A 250V glass | 9707080 series | $8–$18 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) / [Grainger](https://www.grainger.com?aff=PLACEHOLDER-GRAINGER) |
| 1-2-3 indoor-outdoor cable, 14/3 stranded jacketed, 50 ft | Southwire | $55–$95 | [Home Depot](https://www.homedepot.com?aff=PLACEHOLDER-HD) |
| Line-set rubber grommet kit | Rectorseal | $12–$22 | [Home Depot](https://www.homedepot.com?aff=PLACEHOLDER-HD) / [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |

Order replacement PCBs with the gasket and clip kit — Fujitsu boards ship in protective bags but the small thermal pad on the bridge rectifier sometimes doesn't come with the basic part.

## When to call a professional

Call a NATE-certified mini-split tech if:

- The wiring checks clean and 11:4 persists with verified PCB voltage rails. PCB replacement on an inverter unit benefits from someone who's done it before.
- You find any sign of moisture, corrosion, or pest damage inside either unit. Rodent damage to communication wiring is a recurring Fujitsu service call and chasing it without taking the cabinet apart is futile.
- The system is on R-32 or R-454B refrigerant and you don't have A2L certification and equipment.
- You see L1/N reversed at one terminal block and the unit has been running that way for a while — there may be additional board damage from the miswire and a tech should verify.
- The unit is under the original Fujitsu warranty (Fujitsu offers 7-12 year parts coverage depending on installation registration). Warranty service requires an authorized Fujitsu servicer.

## FAQs

**Will Fujitsu 11:4 clear on its own?**
On a transient fault (a momentary breaker trip, a brief power blip), 11:4 can clear and stay clear. On any persistent wiring or PCB fault, 11:4 returns within minutes. Don't keep cycling power without diagnosing.

**Can I use 18 AWG thermostat wire for the Fujitsu 1-2-3 cable?**
No. Fujitsu specifies 14 AWG minimum for the 1-2-3 cable because it carries 240 V power between the units plus signal. 18 AWG is undersized for the power conductors and will create voltage drop and possible heat-up issues. Use 14/3 stranded jacketed.

**Why does my Fujitsu 11:4 only happen when the compressor starts?**
Classic chafed-conductor symptom. Compressor inrush vibrates the line set and the cable, and a damaged conductor briefly opens or shorts. Pull the cable inspection and look at the saddle clamps on the outdoor base pan.

**Is 11:4 the same on Fujitsu Airstage VRF as on Halcyon residential?**
The code class is the same (communication) but the bus topology differs. Airstage VRF uses an addressed multi-drop bus with termination resistors and is significantly more complex. 11:4 on Airstage may point to an address conflict, a missing termination resistor, or a broken trunk run. Different diagnostic discipline.

**What does the LED flash pattern look like for 11:4?**
On most Fujitsu Halcyon indoor heads, 11:4 displays as 11 flashes of the operation LED, a pause of about 2 seconds, then 4 flashes of the timer LED, with the whole pattern repeating. On indoor heads with a digital display (some ducted ASU models), it shows as text: "11:4" or "E:11:4".

## Related guides

- [Fujitsu Mini Split 14:1 Error Code — High Pressure Fix](/posts/fujitsu-error-code-14-1)
- [Fujitsu Mini Split 15:1 Error Code — Low Pressure Fix](/posts/fujitsu-error-code-15-1)
- [Mitsubishi P5 Error Code — Indoor-Outdoor Communication Fix](/posts/mitsubishi-p5-error-code)
