---
title: "Allen-Bradley PowerFlex Fault F004 — Causes & Fix"
description: "What Allen-Bradley PowerFlex fault F004 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - allen-bradley
---

## Allen-Bradley PowerFlex Fault F004 — What It Means

Allen-Bradley PowerFlex fault F004 is a DC bus undervoltage fault. The drive's DC bus voltage dropped below the minimum operating threshold during operation or startup. PowerFlex drives (40, 525, 755, and others) convert AC input to a DC bus, then invert it to variable-frequency AC for the motor. The DC bus is maintained by the input rectifier and filter capacitors. When bus voltage falls below approximately 60–70% of nominal (the exact threshold depends on drive and nominal voltage), the drive can no longer synthesize the correct output waveform and trips F004 to protect the power electronics.

[Jump to Fix](#fix)

## Common Causes

- **Low AC input voltage** — The utility supply voltage is sagging below the drive's minimum input specification. This is common on long feeder runs, during peak load periods, or after utility disturbances.
- **Input phase loss** — One of the three input phases is missing (blown fuse, open contactor, broken wire). A three-phase drive operating on two phases will show significantly reduced DC bus voltage.
- **Weak or failed DC bus capacitors** — Aged electrolytic capacitors on the DC bus lose capacitance over time and can no longer hold bus voltage stable during load transients, causing the bus to dip and trigger F004.
- **Drive attempting to start into a large motor with a weak supply** — During motor acceleration, the drive draws high input current. On a weak supply, this current draw depresses the input voltage and causes a bus undervoltage trip.

## Step-by-Step Fix {#fix}

1. **Measure input voltage at the drive's L1/L2/L3 terminals** — With the drive powered up, check voltage across all three input phases. Voltage should be within ±10% of the nameplate rating. Also check for voltage balance between phases — greater than 3% imbalance indicates a supply problem.
2. **Check all input fuses and the input disconnect** — Verify every fuse in the input circuit is intact (test with a continuity meter, not visually). A blown fuse on one leg creates phase loss and F004.
3. **Monitor DC bus voltage during a run attempt** — Navigate to the drive's monitoring parameters (on PowerFlex 525: P053 DC Bus Voltage). Observe the bus voltage at rest and during the start attempt. A sharp dip during the start indicates a supply impedance issue.
4. **Check capacitor condition** — On older drives (5+ years in service), check the DC bus capacitors for bulging, leaking electrolyte, or mechanical damage visible through the drive cover. Degraded capacitors require replacement or the drive needs to go to a repair depot.
5. **Add a line reactor** — If supply voltage is low or highly variable, a 3% or 5% input line reactor reduces supply-induced voltage dips and extends drive life.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input fuses (class J or CC) | [Amazon](https://www.amazon.com/s?k=Input+fuses+%28class+J+or+CC%29&tag=errorcodefixes-20) \| Use properly rated fuses; wrong rating will not protect the drive |
| DC bus capacitor kit | [Amazon](https://www.amazon.com/s?k=DC+bus+capacitor+kit&tag=errorcodefixes-20) \| Available from Rockwell or aftermarket repair kits for common models |
| Input line reactor (3–5%) | [Amazon](https://www.amazon.com/s?k=Input+line+reactor+%283%E2%80%935%25%29&tag=errorcodefixes-20) \| Install if supply impedance is causing voltage dips |
## When to Call a Pro

If the input voltage is confirmed within spec and capacitors are not visually degraded but F004 persists, internal capacitance measurement requires capacitor discharge procedures and specialized test equipment. A certified Rockwell service technician or drive repair center should perform this evaluation.

## Related Articles

- [Allen-Bradley MicroLogix 1400 Common Fault Codes](/posts/allen-bradley-micrologix-fault/)
- [Allen-Bradley PowerFlex 40 Complete Fault Code Guide](/posts/allen-bradley-powerflex-40-complete-guide/)
- [Allen Bradley PowerFlex 40 F2 Fault — Causes & Fix](/posts/allen-bradley-powerflex-40-f2-fault/)
- [Allen-Bradley PowerFlex 40 F3 Fault — Power Loss](/posts/allen-bradley-powerflex-40-f3/)
- [Allen Bradley PowerFlex 40 F7 Fault — Causes & Fix](/posts/allen-bradley-powerflex-40-f7-fault/)
