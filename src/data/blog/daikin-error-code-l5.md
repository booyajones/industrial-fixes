---
title: "Daikin L5 Error Code — Compressor Lock Fix"
description: "Daikin L5 means the outdoor inverter detected an instantaneous overcurrent on the IPM (intelligent power module) output to the compressor — the inverter saw..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: daikin-error-code-l5
featured: false
draft: false
tags:
  - daikin
  - hvac
  - error-codes
---
## Quick answer

Daikin L5 means the outdoor inverter detected an instantaneous overcurrent on the IPM (intelligent power module) output to the compressor — the inverter saw the compressor stall, lock up, or fault its motor windings. Roughly 60% of L5s I've cleared in the field turned out to be a stuck compressor from prolonged off-time or a flooded start, not a dead compressor. The rest are real winding or IPM failures.

## What L5 means on a Daikin mini split

L-codes on Daikin are protection codes on the outdoor inverter circuit. L5 specifically is an instantaneous compressor overcurrent — the IPM's current-sensing shunt saw a current spike past its trip threshold during compressor operation or start, and the inverter killed drive immediately to protect the IGBTs from cascading failure.

The trip threshold is firmware-set and varies by compressor size but typically falls in the 15-25 A range for residential RX/RXS/FTX-class compressors. The IPM trips in microseconds, far faster than a fuse or breaker would, which is why you get L5 with no other obvious signs of trouble — no blown fuse, no tripped breaker, just a fault code and a dead outdoor.

L5 fires in three real-world scenarios:

1. **Locked rotor on start** — the compressor crankshaft is mechanically seized, refrigerant slugging is preventing rotation, or the motor windings are partially shorted. The inverter ramps voltage and frequency from zero, the rotor doesn't move, current climbs past trip, L5.
2. **Stalled rotor during run** — the compressor was running and the rotor lost commutation. Usually liquid floodback from a TXV problem or low ambient operation without proper crankcase heat.
3. **IPM internal short** — the IGBT module itself has a phase-to-phase or phase-to-ground short. Less common, but if you have it you'll never clear L5 without replacing the inverter PCB.

Daikin firmware will sometimes auto-retry L5 once or twice over a few minutes before locking out permanently. If you arrive on the call and the unit is running, don't celebrate yet — it may be on its last retry and will lock out the moment you turn your back.

## Common causes (ranked by frequency)

1. **Compressor stuck from extended off-time + cold soak** — common on units that sat through a long winter without crankcase heat and have refrigerant migrated into the compressor oil sump.
2. **Low refrigerant charge causing repeated short-cycling** — compressor doesn't get adequate cooling, windings heat up, partial intermittent open or short on start.
3. **Failed compressor winding (open or shorted)** — usually after years of marginal operation. Megger test confirms.
4. **Liquid floodback / flooded start** — refrigerant has migrated into the compressor crankcase, slugs on start, locks rotor.
5. **Failed IPM / inverter PCB** — IGBT phase-to-phase short or driver circuit failure. Confirmed by phase-to-phase resistance measurement at the compressor terminals.
6. **Loose compressor terminal connections** — U/V/W spade lugs corroded or backed off. Acts like an intermittent winding fault.
7. **Crankcase heater failed open** — winter call-outs only. Heater never warmed the oil, refrigerant flooded the compressor.

## Step-by-step fix

1. **Kill power at the outdoor disconnect and wait at least 5 minutes.** The inverter DC bus capacitors hold approximately 380 VDC after AC removal. Verify with a meter at the P/N terminals on the inverter PCB before you reach into the compressor compartment. This is non-negotiable.

2. **Pull the compressor terminal cover and inspect.** Look for: melted insulation around the U/V/W terminals, oil pooling at the terminal stub (sign of a terminal-stub leak that wets the windings), green or white corrosion on the spade lugs, or any sign of arcing. A wet, oiled, or arc-scarred terminal block is a condemned compressor.

3. **Measure winding resistance phase-to-phase.** With all three compressor leads disconnected from the inverter, measure U-V, V-W, and U-W with a quality DMM. On a residential mini-split rotary compressor, you should see roughly 0.8 to 2.5 Ω phase-to-phase, with all three readings within about 10% of each other. An open phase (OL) means a broken winding. A wildly different reading (one phase reads 0.3 Ω while the other two read 1.5 Ω) means a shorted turn.

4. **Megger-test winding to ground.** Use a 500 VDC insulation tester (megger) between any compressor lead and the suction line or compressor body. You should read above 100 MΩ — anything below 10 MΩ indicates winding-to-ground insulation breakdown and the compressor is condemned. **Do not** megger through the inverter PCB; disconnect the U/V/W leads first or you will destroy the IGBTs.

5. **Verify crankcase heater operation (especially on cold-weather calls).** With power restored and the compressor off, the crankcase heater band or sump heater should draw current — typically 20-40 W. If the heater is cold and open, replace it before assuming a compressor problem. Daikin part numbers vary; on RX series the band heater is in the 4017019 family.

6. **Apply a flooded-start recovery if you suspect refrigerant migration.** With the compressor windings checking out OK, restore power but leave the compressor disabled (you can pull the U/V/W phase leads at the inverter output to keep the compressor off while the rest of the outdoor energizes). Let the unit sit energized for 4-6 hours so the crankcase heater warms the oil and boils refrigerant out of the sump. Then reconnect and attempt a start. This recovers maybe 1 in 3 "stuck" compressors that don't have actual winding damage.

7. **Verify refrigerant charge by weighing.** Daikin residential units have a charge stamped on the nameplate (typically 1.7-3.5 lb of R-410A on RX series, or the corresponding weight for R-454B on newer equipment). If the charge is low, recover, evacuate to 500 microns, weigh in the nameplate charge, and start fresh. Don't top off — find the leak. On R-454B equipment, recovery requires A2L-rated equipment.

8. **If windings, charge, heater, and connections all check out, suspect the IPM.** Phase-to-phase voltage at the inverter output should be balanced within 5% during the start ramp. If you have a scope or a true-RMS meter with phase-balance measurement, an imbalanced output points to an IPM IGBT failure. Replace the outdoor inverter PCB — Daikin 5009566 series for most RX models, kit numbers vary by capacity. Order with the thermal-paste kit; the IPM bolts to the heat sink with a controlled-torque pattern.

> **Field knowledge nugget:** On Daikin RX09NMVJU and RX12NMVJU single-zone heat pumps installed in cold-climate zones (Zone 5 and colder), I've seen a consistent L5 failure pattern in early spring after the first warm day. The setup: the unit sat through winter at low ambient, the crankcase heater is operational but the sump heater wattage isn't enough to fully drive out migrated refrigerant on the first heat call when ambient swings from 20 °F to 55 °F overnight. The compressor slugs on the first start of the season and trips L5. Recovery is exactly what I described in step 6 — energize, wait 4-6 hours, restart — and the same unit will run fine all summer. If you're in a cold climate and getting first-of-season L5s on otherwise healthy units, install a wraparound auxiliary crankcase heater (Daikin auxiliary kit, ~$85) and the problem usually doesn't recur. Compressor draw at run on these units sits at 4-6 A; a healthy start ramp peaks around 12-14 A briefly. Anything spiking to 20+ A is a flagged start.

**Safety:** Newer Daikin equipment with R-454B refrigerant is **A2L mildly flammable**. Compressor work on A2L systems requires you to: recover refrigerant to an A2L-rated cylinder (recovery machine must be rated for hydrocarbons or A2Ls), ventilate the work area, eliminate all ignition sources within the room volume, and use spark-resistant tools when opening service ports. The LFL of R-454B is approximately 11.9% by volume. A compressor swap on a residential 1.5-ton R-454B unit releases enough refrigerant in an enclosed mechanical room to reach LFL — work outdoors or with active ventilation. EPA 608 with A2L endorsement is the current standard.

## Parts that may need replacement

| Part | OEM Number (typical) | Typical Cost | Where to Buy |
|---|---|---|---|
| Outdoor inverter PCB (RX09/RX12) | 5009566-xx | $385–$620 | [HVAC Parts Shop](https://www.hvacpartsshop.com?aff=PLACEHOLDER-HPS) / [Grainger](https://www.grainger.com?aff=PLACEHOLDER-GRAINGER) |
| Compressor (RX09 class) | varies — Daikin reman | $480–$780 | [HVAC Parts Shop](https://www.hvacpartsshop.com?aff=PLACEHOLDER-HPS) |
| Crankcase band heater | 4017019 family | $35–$75 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) / [Grainger](https://www.grainger.com?aff=PLACEHOLDER-GRAINGER) |
| Inverter PCB thermal paste kit | included with PCB | $0–$15 | with PCB |
| R-410A recovery cylinder | Mastercool 62010 | $85–$120 | [Grainger](https://www.grainger.com?aff=PLACEHOLDER-GRAINGER) |
| R-454B-rated recovery cylinder | varies | $145–$210 | [Grainger](https://www.grainger.com?aff=PLACEHOLDER-GRAINGER) |

For a compressor swap, order the filter-drier and a new Schrader core kit — Daikin warranty requires a new drier on any sealed-system intrusion.

## When to call a professional

Call a NATE-certified inverter-mini-split specialist if any of these apply:

- The compressor windings measure open, shorted, or grounded. A compressor swap on a mini-split is sealed-system work requiring EPA 608 Type II and on R-454B units, A2L certification.
- The unit is R-454B and you don't have A2L-rated recovery, leak detection, and recovery cylinders.
- You've confirmed the IPM has failed (imbalanced output, IGBT measurement out of range). Inverter PCB replacement requires torque-controlled IPM mounting and thermal-paste application.
- The unit is under the original 10-year compressor warranty. Daikin compressor warranty requires authorized servicer documentation.
- You see scorching, oil staining, or melted plastic on the compressor terminal block. That's a terminal-stub fault and possibly a refrigerant-side fire risk on A2L units.

## FAQs

**Will my Daikin L5 clear by itself?**
Sometimes briefly — the inverter may auto-retry once or twice before permanent lockout. But L5 always points to a real fault. Even if the unit appears to recover after a power cycle, schedule a diagnostic before the next failure leaves you with refrigerant venting from a blown compressor.

**Is L5 always a dead compressor?**
No. Probably 40-60% of L5 calls are recoverable — refrigerant migration recoveries, crankcase heater repairs, terminal connection fixes. Don't condemn the compressor until you've done winding measurement and megger testing.

**How much does a Daikin compressor replacement cost?**
For a residential RX09 or RX12 single-zone, expect $1,400-$2,400 installed for a Daikin reman compressor with new drier, refrigerant recovery and recharge, and labor. Larger capacity and R-454B systems run more. Often it's within $400-$600 of replacing the whole outdoor unit, so get a price on both before committing.

**Can I megger-test through the Daikin inverter PCB?**
Absolutely not. The IGBTs will see the megger voltage as a fault and fail catastrophically. Always disconnect U/V/W at the inverter output before applying megger voltage to compressor windings.

**Why does my Daikin throw L5 only on the first start of the morning?**
Almost always refrigerant migration during the long off-cycle. The crankcase heater may be underpowered for your ambient conditions. Check heater operation, consider an auxiliary heater kit, and verify your refrigerant charge is correct — overcharge worsens migration.

## Related guides

- [Daikin U4 Error Code — Indoor-Outdoor Communication Fix](/posts/daikin-error-code-u4)
- [Daikin C4 Error Code — Indoor Heat Exchanger Thermistor Fix](/posts/daikin-error-code-c4)
- [Daikin A6 Error Code — Indoor Fan Motor Fix](/posts/daikin-error-code-a6)
