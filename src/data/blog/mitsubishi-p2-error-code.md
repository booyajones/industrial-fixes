---
title: "Mitsubishi Mini Split P2 Error Code — Indoor Pipe Thermistor Fix"
description: "P2 on a Mitsubishi mini split means the indoor liquid-line pipe thermistor (TH2) is reading outside the PCB's acceptable range — almost always because the..."
pubDatetime: 2026-05-20T17:00:00Z
modDatetime: 2026-05-20T17:00:00Z
author: "Dana Kowalski"
slug: mitsubishi-p2-error-code
featured: false
draft: false
tags:
  - mitsubishi
  - hvac
  - error-codes
  - indoor-pipe-thermistor-error
---
## Quick answer

P2 on a Mitsubishi mini split means the indoor liquid-line pipe thermistor (TH2) is reading outside the PCB's acceptable range — almost always because the sensor fell off the copper, the clip broke, the lead got crushed, or the bead failed open. Pop the front cover, find the small thermistor clipped to the liquid-line U-bend on the evaporator, ohm it cold (should read ~10 kΩ at 77 °F), and if it's open, missing, or hanging in mid-air, you've found your problem.

## What P2 means on a Mitsubishi mini split

The Mitsubishi P-code family signals protection events — the indoor controller saw something outside its safe operating window and shut the call down. P2 is specifically the indoor coil pipe thermistor (TH2), which Mitsubishi uses for refrigerant cycle decisions: defrost timing, freeze protection arming, EEV modulation feedback, and the "hot-start" delay that keeps the indoor fan off in heat mode until the coil is warm enough to avoid blowing cold air.

That distinguishes P2 from the closely-related P1 (room thermistor TH1) and P8 (pipe temperature out of expected range during operation). P1 is "I can't read this sensor at all." P2 is the same thing for the coil sensor. P8 is "I can read the sensor fine, but the temperature it's reporting doesn't match what I expect given the refrigerant cycle state." Don't confuse them.

On wall-mount MSZ models (MSZ-FH, MSZ-GL, MSZ-LN), TH2 is a small bead-style NTC thermistor clipped to the liquid-line U-bend on the evaporator coil, usually held on with a spring clip or a stainless band. On MLZ ceiling cassettes the sensor is on the distributor manifold. On SEZ ducted units it sits in a thermistor well brazed to the liquid header. All of them are 10 kΩ at 25 °C / 77 °F, B25/50 = 3380 K — the same thermistor curve Mitsubishi uses for TH1 — but the harness, connector, and PCB pin position are different, so don't try to cross them.

P2 latches the unit off until you cycle power. The remote will not clear it.

## Common causes (ranked by frequency)

1. **Sensor fell off the pipe** — the clip lost tension, the band corroded, or the foam insulation that holds it captive sagged. Sensor is now reading air temp instead of pipe temp, but the bead is fine. This is THE most common cause.
2. **Open thermistor bead** — sensor failed open. Reads OL. Common on units 8+ years old, especially in humid climates.
3. **Harness damage** — the thermistor lead got crushed when somebody reseated the front panel, or rubbed through against the EEV body or coil hairpin.
4. **Connector backed out at the PCB** — CN29 on most M-Series boards; vibration or sloppy reassembly leaves it half-seated.
5. **Wrong sensor installed** — somebody replaced TH2 with a TH1 part. They're the same curve but different lead length and clip — and the wrong clip will fall off.
6. **PCB input failure** — rare, but possible after a brownout or lightning event. Verify with a known-good sensor before condemning the board.

**Field-knowledge nugget:** On MSZ-FH and MSZ-LN heads, the TH2 spring clip relaxes over time as the foam insulation it presses against compresses. By year 6 or 7, the clip is loose enough that any vibration — even just somebody slamming a door near the unit — will let it drift down the U-bend until it's reading the return air bend instead of the liquid line. If you find a P2 and the sensor is still attached but in the wrong spot (look at the foam-impression line on the copper; you can see where it WAS clipped), don't replace it — just re-clip it tight and wrap a fresh zip-tie around the assembly to lock it down. I've cleared dozens of P2s on 6–10 year old MSZ heads with nothing but pliers and a zip-tie.

## Step-by-step fix

You'll need: multimeter with kΩ scale, small Phillips, flashlight, ice water cup, hot water cup with a thermometer, replacement TH2 (have one on the truck), zip-ties, and the unit-specific service manual.

1. **Disconnect power at the dedicated disconnect.** Verify dead with NCV at the indoor terminal block. Wait at least 60 seconds for caps to bleed down.
2. **Open the indoor head.** MSZ wall-mount: lift the front intake grille, remove the filter, remove the two screws under the filter slot, pivot the front shell forward and unhook from the top. MLZ cassette: drop the grille on its safety cables. SEZ ducted: remove the return-side service panel.
3. **Locate TH2 on the coil.** It's a small bead with a spring clip or stainless band, clipped to the liquid-line U-bend on the evaporator — usually on the LEFT side of the coil as you face it (the side where the liquid line enters from the lineset). Follow the wire back from the PCB to find it if you're not sure. CN29 on the controller PCB is the standard TH2 landing for MSZ; check your wiring diagram.
4. **First check: is it still on the pipe?** Look for the original foam-impression line on the copper. If the sensor has drifted, you've found your fault — re-clip it tight against the liquid line at the original location, secure with a zip-tie, and you may be done. Power up and verify.
5. **If the sensor is in the right place, disconnect at CN29 and ohm it.** At room temp (77 °F / 25 °C) you should see **~10 kΩ ±5%**. OL = open, replace. Near 0 Ω = shorted, replace.
6. **Verify B-value at two temperatures.** Drop the bead in ice water (32 °F / 0 °C): should read **~22 kΩ**. Drop in 122 °F / 50 °C tap water: should read **~3.6 kΩ**. Off by more than 10% at either point = wrong part or aged-out sensor. Replace.
7. **Wiggle-test the harness.** With sensor disconnected at the board, flex the lead along its run. Reading jumps to OL = chafed conductor somewhere. Common spots: where the harness crosses the EEV body, where it passes through the bulkhead between the evaporator chamber and the control box, and at the strain-relief on the PCB connector.
8. **Replace if needed, reseat connector, restore power.** Use OEM TH2 with the correct clip type for your specific model — MSZ-FH uses a different clip than MSZ-LN. Reseat CN29 firmly until you hear/feel the latch click. Energize, start a cool call, monitor for 20 minutes.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|------|------------|--------------|--------------|
| Indoor pipe thermistor (TH2), MSZ-GL / MSZ-FH | E12 E48 427 | $44–$60 | [HVAC Parts Shop](https://www.hvacpartsshop.com?aff=PLACEHOLDER-HPS), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Indoor pipe thermistor (TH2), MSZ-LN | E27 E48 304 | $48–$64 | [HVAC Parts Shop](https://www.hvacpartsshop.com?aff=PLACEHOLDER-HPS) |
| Indoor pipe thermistor (TH2), MLZ cassette | E22 E45 305 | $50–$66 | [HVAC Parts Shop](https://www.hvacpartsshop.com?aff=PLACEHOLDER-HPS), [Grainger](https://www.grainger.com?aff=PLACEHOLDER-GRAINGER) |
| Indoor pipe thermistor (TH2), SEZ ducted | E12 E47 402 | $46–$62 | [HVAC Parts Shop](https://www.hvacpartsshop.com?aff=PLACEHOLDER-HPS) |
| TH2 spring clip / band (MSZ) | E12 E84 612 | $9–$14 | [HVAC Parts Shop](https://www.hvacpartsshop.com?aff=PLACEHOLDER-HPS) |
| Indoor controller PCB, MSZ-GL15NA | E22 R12 305 | $310–$420 | [HVAC Parts Shop](https://www.hvacpartsshop.com?aff=PLACEHOLDER-HPS), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |

Don't skip the clip. A new sensor on an old, stretched-out clip will just fall off again in 18 months.

## When to call a professional

If the sensor reads correctly, the harness checks out, and the connector is clean and seated — and P2 still comes back — you're either looking at a PCB input failure (rare) or a heat-soak intermittent in the harness that only shows up under runtime conditions. Both are diagnosis-heavy calls. A Mitsubishi Diamond contractor with the M-NET service tool can read live TH2 values during runtime and pinpoint heat-related faults in minutes, where DIY troubleshooting can take hours.

Also call a pro if the unit is multi-zone (MXZ outdoor with two or more indoor heads) and only one zone is throwing P2. The branch box wiring on multi-zone systems has additional thermistor and communication runs, and tracing them without the right docs is a nightmare.

## FAQs

**P2 vs P8: what's the difference?** P2 means the indoor pipe thermistor is electrically out of range — open, shorted, or wildly off-curve. The PCB literally cannot read the sensor. P8 means the sensor reads fine electrically, but the temperature it reports doesn't match what the controller expects during a given operating mode. P2 is a sensor/wiring fault; P8 is usually a refrigerant or airflow fault. Don't replace a thermistor for P8.

**Can I use a TH1 sensor in the TH2 spot?** No. They use the same NTC curve, but the lead length, connector orientation, and clip are different. A TH1 part won't physically install on the liquid-line U-bend, and even if you cable-tie it on, you'll have a service nightmare later.

**The sensor was hanging loose — can I just clip it back on?** Yes, and that's usually the right call. Look for the foam-impression line on the copper to find the original location, clip the sensor tight against the pipe (NOT against the foam — direct copper contact), and secure with a zip-tie. Restore power and verify the code clears.

**Will P2 affect both heat and cool?** Yes. TH2 is used in every operating mode — defrost timing in heat, freeze protection in cool, EEV control in both. A bad TH2 kills the whole system.

**My MUZ outdoor unit isn't communicating — could that cause P2?** No. P2 is purely an indoor-side fault. If you're seeing P2 plus an E-code (E6, E7), treat them as separate issues. Fix P2 first because the indoor unit won't communicate properly until the indoor-side faults are clear.

## Related guides

- [Mitsubishi E6 Error Code — Indoor/Outdoor Communication Fault](/posts/mitsubishi-e6-error-code) (existing guide)
- [Mitsubishi P1 Error Code — Indoor Coil Thermistor (Room) Fix](/posts/mitsubishi-p1-error-code)
- [Mitsubishi P5 Error Code — Drain Pump Overflow Fix](/posts/mitsubishi-p5-error-code)
- [Mitsubishi P6 Error Code — Freeze Protection Fix](/posts/mitsubishi-p6-error-code)
- [Mitsubishi P8 Error Code — Pipe Temperature Out of Range Fix](/posts/mitsubishi-p8-error-code)
