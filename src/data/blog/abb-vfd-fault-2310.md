---
title: "ABB VFD Fault 2310 — Causes & Fix"
description: "What ABB VFD fault 2310 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - abb
---

## ABB VFD Fault 2310 — What It Means

ABB VFD fault 2310 is an earth fault (ground fault). The drive's earth fault detection circuit detected that current is flowing from one or more output phases to earth (ground) at a level above the detection threshold. This indicates that the insulation on the motor winding, output cable, or motor terminal box has broken down and is conducting current to ground. ABB drives detect this condition by monitoring the sum of all three output phase currents — in a healthy system with no ground fault, the vector sum is zero. A non-zero residual current indicates a fault to ground.

[Jump to Fix](#fix)

## Common Causes

- **Motor winding insulation failure** — Insulation breaks down due to age, heat cycling, moisture ingress, or voltage spikes. One or more winding phases develop a resistive path to the motor frame.
- **Damaged output cable** — The cable between the drive and motor has physical insulation damage (abrasion, rodent damage, pinching) that creates a connection between a phase conductor and the conduit, armor, or cable jacket ground.
- **Wet motor terminal box** — Water infiltration into the motor terminal box causes a conductive path from phase terminals to the motor frame, triggering earth fault detection.
- **Very long cable runs** — Distributed capacitance from long motor cables creates significant ground current at the drive's switching frequency. On drives without output reactors, this can exceed the earth fault detection threshold even without a true insulation failure.

## Step-by-Step Fix {#fix}

1. **Disconnect the motor from the drive output** — Remove the motor cable connections at the drive's T1/T2/T3 (U/V/W) output terminals. Attempt to run the drive unloaded (if the drive supports test mode). If fault 2310 clears, the fault is in the motor or cable. If it persists, investigate the drive output section.
2. **Megger test the motor** — With the motor cable disconnected at both the drive and motor ends, perform an insulation resistance test (megger) between each phase terminal and motor frame ground. Values below 1 MΩ indicate degraded insulation. Values below 100 kΩ indicate a serious fault.
3. **Megger test the output cable** — Test each conductor of the output cable against the ground/shield. Any low-resistance reading indicates damaged cable insulation.
4. **Inspect motor terminal box** — Open the motor terminal box and check for moisture, corrosion, tracking marks (carbon paths), or physical damage between phase lugs and the motor body.
5. **Add output reactor for long cable runs** — If no insulation failure is found, install an output line reactor (choke) between the drive and the motor to reduce the capacitive ground current to below the detection threshold.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor (rewind or replace) | [Amazon](https://www.amazon.com/s?k=Motor+%28rewind+or+replace%29&tag=errorcodefixes-20) \| If megger confirms winding fault; rewinding is cost-effective on larger motors |
| Output cable | [Amazon](https://www.amazon.com/s?k=Output+cable&tag=errorcodefixes-20) \| Replace full run if insulation is compromised |
| Output line reactor (choke) | [Amazon](https://www.amazon.com/s?k=Output+line+reactor+%28choke%29&tag=errorcodefixes-20) \| Install when cable run exceeds drive manufacturer's maximum without reactor |
## When to Call a Pro

Megger testing at 500V or 1000V DC on motors connected to high-voltage systems requires proper PPE and lock-out/tag-out procedures. If the motor is part of a hazardous location installation, a licensed electrician must perform the insulation testing and repair.
