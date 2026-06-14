---
title: "Yaskawa A1000 Fault UV1, DC Bus Undervoltage Causes & Fix"
description: "What Yaskawa A1000 UV1 means, why the drive sees DC bus undervoltage, and how to diagnose input power, contactor, and weak-supply problems."
pubDatetime: 2026-04-24T23:50:00Z
modDatetime: 2026-04-24T23:50:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
  - a1000
money_part: "Class J or semiconductor input fuses"
most_likely_cause: "Low incoming three-phase voltage"
---

## Yaskawa A1000 Fault UV1, What It Means

Yaskawa A1000 **Fault UV1** means the drive detected **DC bus undervoltage**. In practice, the inverter's main circuit voltage has dropped below the minimum level needed for stable operation. On the plant floor, UV1 usually points to missing input phase, brownout conditions, loose power wiring, a dropping line contactor, or a supply that sags hard when the motor tries to accelerate.

UV1 is often intermittent at first. Operators will report that the line ran fine yesterday, but now the drive trips on startup, during acceleration, or whenever another large load comes online.

[Jump to Fix](#fix)

## Common Causes

- **Low incoming three-phase voltage**. Utility sag or undersized plant distribution is a classic UV1 trigger.
- **Single phasing or blown input fuse**. The drive may still power up but will collapse under load.
- **Loose input terminals or a weak disconnect/contactor**. Heat-discolored lugs and pitted contacts are common finds.
- **Acceleration too aggressive for a weak supply**. The bus dips when the drive draws hard current on startup.
- **Undersized transformer or long feeder run**. Voltage drop becomes visible during acceleration or high torque demand.
- **Aging internal capacitors or precharge issues**. Less common, but possible on older A1000 drives.

## Step-by-Step Fix {#fix}

1. **Measure the input voltage at the drive while it is trying to run**. Check all three phase-to-phase readings both at idle and during acceleration. If voltage collapses under load, you are chasing a real supply problem, not a nuisance code.
2. **Check for single phasing**. Inspect upstream fuses, breaker poles, disconnects, and any line contactor feeding the drive. A missing phase is one of the fastest ways to create UV1.
3. **Torque and inspect input terminals**. Loose lugs cause heat, voltage drop, and intermittent UV1 trips. Look for discoloration, melted insulation, or signs of arcing.
4. **Lengthen the acceleration time**. If the supply is marginal, a softer ramp reduces bus sag during startup and can confirm the root cause.
5. **Check for other large loads starting on the same feeder**. Compressors, welders, and big across-the-line motors can pull the incoming voltage down enough to trip the A1000.
6. **Verify feeder and transformer sizing**. Long conductor runs or a transformer that is too small for the application can look fine at idle and fail only under production load.
7. **Review the event history**. If UV1 happens after power interruptions, during utility transfer, or at shift start, the timing matters. Tie the trip to a plant event, not just the drive.
8. **If input power is solid, suspect the drive**. Stable input voltage with repeated UV1 faults can point to failing bus capacitors, a precharge problem, or internal sensing issues.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Class J or semiconductor input fuses | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-fault-uv1&k=class+j+fuse+480v+motor+drive&tag=errorcodefixes-20) \| Replace blown or heat-damaged line protection after finding the cause |
| Three-pole contactor | [Amazon](https://www.amazon.com/dp/B0CJFZQVPT?ascsubtag=ecf-yaskawa-a1000-fault-uv1&tag=errorcodefixes-20) \| Weak or pitted contacts can create intermittent voltage drop |
| 3% line reactor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-fault-uv1&k=3%25+line+reactor+480v+drive&tag=errorcodefixes-20) \| Helps stabilize weak or noisy incoming power |
| Power quality meter | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-fault-uv1&k=three+phase+power+quality+analyzer&tag=errorcodefixes-20) \| Best way to prove supply sag during startup |
| Terminal block and ferrule kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-fault-uv1&k=din+terminal+block+ferrule+kit&tag=errorcodefixes-20) \| Useful when loose or overheated line-side terminations caused the fault |

## When to Call a Professional

Call a drive technician or electrician if UV1 persists with verified balanced input voltage at the drive terminals. At that point you may be dealing with failing DC bus capacitors, a bad precharge circuit, or a deeper power-distribution problem upstream of the drive.

## See Also

- [Yaskawa GA700 Fault UV1, Causes and Fix](/posts/yaskawa-ga700-fault-uv1/)
- [Yaskawa VFD Fault UV1, Undervoltage Guide](/posts/yaskawa-vfd-fault-uv1/)
- [Yaskawa A1000 OC Fault Code, Overcurrent Troubleshooting](/posts/yaskawa-a1000-oc-fault-code/)
- [Yaskawa VFD Fault PF, Input Phase Loss Guide](/posts/yaskawa-vfd-fault-pf/)

## Related Articles

- [Yaskawa A1000 OC Fault — Overcurrent](/posts/yaskawa-a1000-fault-oc/)
- [Yaskawa A1000 Fault Code OC — Overcurrent Diagnosis & Fix](/posts/yaskawa-a1000-oc-fault-code/)
- [Yaskawa GA700 OC Fault — Overcurrent Fix](/posts/yaskawa-ga700-fault-oc/)
- [Yaskawa GA700 Fault UV1 — Main Circuit Undervoltage Causes & Fix](/posts/yaskawa-ga700-fault-uv1/)
- [Yaskawa Sigma-7 SGD7S Servo Drive Alarm Codes — Diagnosis & Fix](/posts/yaskawa-sigma7-sgd7s-alarm-codes/)
