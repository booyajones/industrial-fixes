---
title: "ABB ACS580 A3D0 Fault Code - Causes & Fix"
description: "ABB ACS580 A3D0 means grid ridethrough: incoming voltage fell below threshold. Check transformer secondary and supply wiring."
pubDatetime: 2026-05-27T10:33:52Z
modDatetime: 2026-05-27T10:33:52Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - abb
---

## ABB ACS580 A3D0 Fault Code — What It Means

A3D0 on an ABB ACS580 is the **Grid ridethrough** fault code. It means the incoming line voltage has dropped below the drive's internal threshold, and the drive has automatically entered low-voltage ridethrough mode to protect itself. This is not a motor or internal drive electronics fault. It is a **supply-side undervoltage condition** tied to power quality at the input terminals.

The drive is responding to a voltage sag, brownout, or momentary loss on the AC supply feeding it. ABB directs technicians to check the transformer secondary voltage when this code appears. The drive itself is usually healthy. The root cause is upstream in your electrical distribution.

[Jump to Fix](#fix)

## Common Causes

- **Incoming utility sag or brownout** A momentary voltage dip or sustained undervoltage from the utility grid will trigger ridethrough mode when voltage falls below the drive's threshold.
- **Transformer secondary undervoltage** If your drive is fed from a control transformer or plant distribution transformer, low secondary voltage or a weak transformer can cause A3D0.
- **Loose or corroded supply wiring** High-resistance connections at the input terminals, upstream contactors, or line-side circuit breakers create voltage drop under load.
- **Failing upstream contactor or breaker** Worn contact surfaces or intermittent opens in upstream switching devices interrupt or degrade the supply to the drive.
- **Plant disturbances or large motor starts** Heavy inrush from nearby equipment or plant transfer events can cause transient voltage sags that trip the ridethrough protection.

## Step-by-Step Fix {#fix}

1. **Measure input voltage at the drive terminals** with a multimeter while the fault is active or during start-up to confirm whether line voltage is within the nameplate specification for your ACS580 model.
2. **Check the transformer secondary voltage** if your drive is fed from a step-down or isolation transformer, as ABB's quick guide specifically directs for this code.
3. **Inspect all upstream wiring and terminations** for loose lugs, heat discoloration, corrosion, or signs of arcing at the drive input terminals, contactors, breakers, and disconnect switches.
4. **Tighten all line-side connections** and replace any burned or damaged terminals or wire ends.
5. **Review plant event logs or talk to operators** to see if the fault coincides with large motor starts, utility transfer, or other known power disturbances.
6. **Monitor line voltage over time** with a data-logging meter if the fault is intermittent to capture transient sags or brownouts.
7. **Contact ABB service or a qualified electrician** if supply voltage is confirmed normal and stable but the A3D0 code persists, as further diagnostics or parameter review may be needed.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input power terminals and lugs | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-a3d0-fault-code&k=Input+power+terminals+and+lugs&tag=errorcodefixes-20) \| Replace if burned, corroded, or mechanically damaged from loose connections. |
| Upstream AC contactor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-a3d0-fault-code&k=Upstream+AC+contactor&tag=errorcodefixes-20) \| Replace if contacts are pitted, worn, or show signs of intermittent drop-out. |
| Step-down or isolation transformer | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-a3d0-fault-code&k=Step-down+or+isolation+transformer&tag=errorcodefixes-20) \| Replace or upgrade if secondary voltage is chronically low or the transformer is undersized for the load. |

## When to Call a Pro

Call a licensed electrician or ABB service if you measure correct and stable voltage at the drive input but the A3D0 code continues to appear. Also call a professional if you find burned wiring, signs of arcing, or if you are not trained to work safely inside energized electrical distribution equipment. Intermittent utility-side voltage problems may require coordination with your power company and advanced metering or harmonic analysis that goes beyond basic troubleshooting.
