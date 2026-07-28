---
title: "Fanuc Alarm 424 — Causes & Fix"
description: "What Fanuc Alarm 424 servo axis following error means, why it trips, and how to diagnose and fix it step by step."
pubDatetime: 2026-04-22T13:00:00Z
modDatetime: 2026-04-22T13:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - fanuc
money_part: "Servo amplifier module"
most_likely_cause: "Servo motor or amplifier fault"
---

## What this code means
Fanuc **Alarm 424** is a **Servo Axis Following Error** — specifically, the positional error (the difference between commanded position and actual encoder feedback position) has exceeded the allowable following error limit during movement. The axis in fault is identified in the alarm message (e.g., "424 X AXIS: FOLLOWING ERROR"). This alarm protects the machine from crashing by stopping motion when the servo can't keep up with commanded moves. Alarm 424 often appears alongside 414 (Servo Alarm) and 411 (Servo Axis Error).

## Common Causes

- **Servo motor or amplifier fault** — A degraded servo amplifier or motor winding issue reduces the torque available to track commanded moves, causing position lag.
- **Mechanical binding or excessive load** — Tight ballscrew preload, worn linear guides, or a mechanical obstruction forces the axis to fall behind commanded position.
- **Loose encoder cable or feedback connector** — Intermittent encoder feedback causes the CNC to see large position jumps, triggering the following error check.
- **Following error limit parameter set too tight** — Parameter 1828 (servo following error limit) may be set too conservatively for the programmed feedrate or machine condition.

## Step-by-Step Fix {#fix}

1. **Note which axis is faulted** — The alarm message identifies the axis (X, Y, Z, B, etc.). Physically move that axis by hand (machine off, brake released) to check for binding or unusual resistance.
2. **Check the servo amplifier LED** — Power on the machine (in alarm state) and look at the servo amplifier module for the faulted axis. An ALM LED or display code on the amplifier narrows the fault to drive vs. motor vs. feedback.
3. **Inspect encoder cable and connectors** — Power off and reseat the encoder feedback cable at both the motor and amplifier ends. Look for bent pins, corrosion, or a cable that's been crushed by chip guards.
4. **Check Parameter 1828** — In MDI mode, navigate to Parameter 1828 for the affected axis. Compare to the Fanuc parameter manual spec for your machine. Increase the limit by 20% to see if alarm 424 is a parameter tuning issue.
5. **Reset and test with a slow jog** — After inspections, E-stop reset, then jog the axis slowly (1% override). If 424 clears at slow speed but returns at higher feedrates, the issue is torque-related (amplifier, motor, or mechanical load).

## Parts Often Needed

| Part | Notes |
|------|-------|
| Servo amplifier module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-424&k=Servo+amplifier+module&tag=errorcodefixes-20) \| Replace when amplifier LED shows internal fault or drive current is limited |
| Encoder cable (axis-specific) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-424&k=Encoder+cable+%28axis-specific%29&tag=errorcodefixes-20) \| Replace if cable shows abrasion, kinks, or intermittent continuity |
| Servo motor (axis-specific) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-424&k=Servo+motor+%28axis-specific%29&tag=errorcodefixes-20) \| Replace when motor phase resistance is unbalanced or winding is grounded |
| Ballscrew support bearing | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-424&k=Ballscrew+support+bearing&tag=errorcodefixes-20) \| Replace if manual axis movement is notchy or rough |
## When to Call a Pro

If alarm 424 persists after clearing mechanical binding and reseating all connectors, Fanuc drive diagnostics and servo tuning require parameter adjustment expertise and oscilloscope-level servo trace analysis. A Fanuc-certified service tech or your machine tool dealer's service department should perform this work.
