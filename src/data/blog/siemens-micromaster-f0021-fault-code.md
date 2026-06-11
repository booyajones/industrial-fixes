---
title: "Siemens Micromaster F0021 - Causes & Fix"
description: "Siemens Micromaster F0021 means earth fault detected. The drive sees leakage current to ground exceeding 5% of nominal current."
pubDatetime: 2026-05-28T09:16:21Z
modDatetime: 2026-05-28T09:16:21Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Motor output cable (3-conductor shielded VFD-rated)"
---

## Siemens Micromaster F0021 — What It Means

F0021 on a Siemens Micromaster 440 is an earth fault. The drive has detected leakage current flowing to ground instead of staying within the motor windings. Siemens triggers this fault when the sum of the phase currents exceeds 5% of the inverter's nominal current, and it applies to framesizes D to F with three current sensors.

In practical terms, the drive is seeing current imbalance consistent with a path from one or more output phases to earth or ground rather than only through the motor. This usually points to insulation breakdown or physical damage somewhere between the drive output terminals and the motor frame.

[Jump to Fix](#fix)

## Common Causes

- **Motor cable insulation damage** A cut, crushed, or abraded cable jacket allows a conductor to contact grounded metalwork or moisture.
- **Motor winding insulation breakdown** Age, heat, or contamination degrades winding insulation and creates leakage to the motor frame.
- **Loose or contaminated output wiring** Damaged lugs, loose strands, or dirt at U/V/W terminals or the motor terminal box create a path to ground.
- **Moisture or conductive contamination** Water ingress, carbon tracking, or metallic dust in the motor, cable, or terminal box conducts leakage current.
- **Incorrect cable routing** Running power, motor, and control leads in the same conduit or trunking increases susceptibility to faults and noise.

## Step-by-Step Fix {#fix}

1. Isolate power completely and apply lockout/tagout to the drive and motor circuit before beginning any tests or inspections.
2. Inspect the motor cable and terminal box for visible damage, including cuts, crushed insulation, burnt spots, loose strands, water ingress, or carbon tracking.
3. Disconnect the motor from the drive output terminals and use a megohmmeter (insulation resistance tester) to test each motor phase (U, V, W) to earth. There should be no continuity or very high resistance between phases and ground in a healthy motor and cable.
4. Check the drive output terminals and cabinet wiring for contamination, loose terminal lugs, or evidence of a ground fault path at the U, V, or W connections.
5. Verify cable routing and grounding practices so motor output leads are separated from control wiring and supply wiring, and not run in the same conduit or trunking.
6. Replace or repair the failed component identified by your isolation testing, whether motor, cable, terminal box parts, or the drive itself if the fault remains with the motor and wiring disconnected.
7. Clear the F0021 fault from the drive and re-test under controlled conditions after the defective component has been corrected.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor output cable (3-conductor shielded VFD-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-f0021-fault-code&k=Motor+output+cable+%283-conductor+shielded+VFD-rated%29&tag=errorcodefixes-20) \| Replace if insulation is damaged, contaminated, or failed insulation test. |
| Motor terminal box components (terminals, glands, connectors) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-f0021-fault-code&k=Motor+terminal+box+components+%28terminals%2C+glands%2C+connectors%29&tag=errorcodefixes-20) \| Replace if fault is isolated to the terminal box or connections. |
| Three-phase AC motor (matching nameplate rating) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-f0021-fault-code&k=Three-phase+AC+motor+%28matching+nameplate+rating%29&tag=errorcodefixes-20) \| Replace if winding insulation to ground has failed and cannot be rewound economically. |
| Siemens Micromaster 440 drive (matching frame size and power) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-f0021-fault-code&k=Siemens+Micromaster+440+drive+%28matching+frame+size+and+power%29&tag=errorcodefixes-20) \| Replace only if fault persists with motor and cable fully disconnected, indicating internal drive fault. |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not trained in lockout/tagout, high-voltage insulation testing, or VFD diagnostics. If your insulation tests are inconclusive, the fault reappears after replacing cable or motor, or the drive itself shows the fault with all output wiring disconnected, you need professional diagnosis. Misdiagnosing an earth fault can damage the new drive or motor, and working on energized VFD circuits without proper PPE and meters is dangerous.
