---
title: "Yaskawa VFD Fault OV — DC Bus Overvoltage Fix"
author: "Dana Kowalski"
pubDatetime: 2024-04-13T08:00:00Z
modDatetime: 2024-04-13T08:00:00Z
slug: yaskawa-vfd-fault-ov
featured: false
draft: false
tags:
  - vfd
  - yaskawa
  - overvoltage
description: "Yaskawa VFD fault OV means the DC bus voltage has exceeded the drive's maximum threshold. This guide covers diagnosis and fixes for the Yaskawa OV overvoltage fault on A1000, V1000, and GA500 drives."
---

## Error Code: Yaskawa OV — DC Bus Overvoltage

**What it means:** Yaskawa fault code OV (Overvoltage) means the DC bus voltage inside the drive has exceeded the maximum allowable threshold. For 460V-class drives, the OV trip threshold is typically 820V DC; for 230V-class drives, it is approximately 410V DC. The DC bus charges through the rectifier from the AC input. OV trips are usually caused by regenerative energy flowing back from the motor into the drive during deceleration — the motor acts as a generator and pumps energy back into the DC bus faster than the drive can dissipate it.

## Common Causes

- **Deceleration ramp too fast** — The most common cause. If the deceleration time (C1-02 or d1-02 depending on Yaskawa model) is set shorter than the mechanical system can decelerate, the motor regenerates energy back into the bus faster than it can be bled off.
- **High inertia load** — Large flywheels, fans, or pump impellers store significant rotational kinetic energy. Stopping them quickly causes high regenerative energy that spikes the DC bus.
- **Missing or failed braking resistor** — Drives configured for dynamic braking require a braking resistor (external) to dissipate regenerative energy as heat. A disconnected or failed resistor leaves the bus with no dissipation path.
- **Overvoltage on the AC input supply** — If the incoming line voltage is already near the top of tolerance (e.g., 504V on a 480V system), the drive's rectified DC bus starts at a high baseline, leaving little headroom before OV trips.
- **Regenerative application without regen-capable drive** — An application with frequent or sustained regenerative loads (cranes, lifts, regenerative conveyors) requires a regenerative drive or braking resistor kit.

## Diagnosis Steps

1. Review the application: is the OV fault occurring during deceleration or at startup/constant speed? OV during decel = classic regeneration issue. OV at constant speed = likely supply voltage issue.
2. Check the deceleration time parameter (C1-02 on A1000). Increase the deceleration ramp time by 50% and test. If the fault clears, the ramp was too fast.
3. If a braking resistor is installed, inspect the resistor connections and measure resistor continuity. An open (OL) braking resistor cannot dissipate energy.
4. If no braking resistor is installed and the load is high inertia: the application needs one. Contact Yaskawa or your drive supplier to size the correct braking resistor for the drive and load.
5. Measure incoming AC line voltage with a true-RMS meter during normal operation. Voltage above 504V on a 480V system leaves minimal DC bus headroom.

## Fix

For fast deceleration ramp: increase C1-02 (deceleration time 1) until OV faults stop. If the application requires fast stops, a braking resistor is necessary.

For a missing or failed braking resistor: install or replace the resistor. Yaskawa publishes braking resistor selection tables for each drive model in the technical manual. Match drive model, braking frequency, and stopping time to select the correct resistor value (ohms) and wattage.

For high incoming line voltage: check with the utility or install a line reactor ahead of the drive to buffer voltage spikes.

## Parts

| Part | Where to Buy |
|------|-------------|
| [Dynamic braking resistor (size per drive model)](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-vfd-fault-ov&k=Dynamic+braking+resistor+%28size+per+drive+model%29&tag=errorcodefixes-20) | Grainger, Amazon |
| [Line reactor (input)](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-vfd-fault-ov&k=Line+reactor+%28input%29&tag=errorcodefixes-20) | Grainger |
| [Braking transistor module (if internal)](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-vfd-fault-ov&k=Braking+transistor+module+%28if+internal%29&tag=errorcodefixes-20) | Contact Yaskawa |

## When to Call a Technician

Braking resistor sizing requires application data (load inertia, stopping frequency, deceleration torque). An incorrectly sized resistor can overheat and become a fire risk. For high-inertia applications or lifts, consult a Yaskawa applications engineer or qualified drive integrator before specifying the braking solution.
