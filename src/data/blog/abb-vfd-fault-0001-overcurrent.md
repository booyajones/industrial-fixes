---
title: "ABB VFD Fault 0001 Overcurrent — Causes & Fix"
description: "What ABB VFD fault 0001 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T08:00:00Z
modDatetime: 2026-04-22T08:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "IGBT power module"
most_likely_cause: "Mechanical jam or overload"
---

## What this code means
ABB fault code 0001 (OVERCURR) means the drive detected output current exceeding the trip limit — typically 2–3× the drive's rated current. This is one of the most common ABB ACS355, ACS550, and ACS880 fault codes. The drive's IGBT output stages are current-limited to protect both the drive and motor; when output current exceeds the trip threshold, the drive shuts off gate signals to all six IGBTs immediately. Fault 0001 can be caused by a mechanical load problem, a motor winding fault, or incorrect drive parameters for the connected motor.

## Common Causes

- **Mechanical jam or overload** — A jammed conveyor, seized pump, or stalled fan creates a locked-rotor condition. The motor draws extreme current trying to overcome the blockage and the drive trips immediately.
- **Acceleration ramp too short** — If the acceleration time (parameter 22.01 in ACS550, Acc Time 1 in ACS355) is set too short, the drive demands more torque than the motor can deliver smoothly, causing current spikes.
- **Motor parameters incorrect** — If the motor nameplate data hasn't been entered correctly (rated current, voltage, frequency), the drive's current limits are miscalibrated. Running motor ID run resolves this.
- **Ground fault or phase-to-phase short in motor cable** — A failed motor or damaged cable causes a short-circuit condition that looks like massive overcurrent to the drive.

## Step-by-Step Fix {#fix}

1. **Check mechanical load** — Before looking at drive parameters, inspect the driven equipment. Try rotating the motor/load by hand with power off. Any resistance means find and clear the mechanical jam first.
2. **Increase acceleration time** — In the drive parameters, find the acceleration ramp time and increase it. A pump or fan that needs 5–10 seconds to accelerate should not be set to 1–2 seconds.
3. **Verify motor nameplate data** — Check parameters for motor rated current, voltage, and frequency. These must match the motor nameplate exactly. Run an ID run (parameter group 99 on ACS series) to let the drive auto-calibrate.
4. **Inspect motor and cable** — With the drive isolated, use a megohm meter to test motor winding insulation to ground. Readings below 1 MΩ indicate insulation breakdown. Check motor leads for damaged insulation.
5. **Reset the system** — After addressing the root cause, reset the fault (usually the RESET button or a digital input mapped to reset). Restart and observe current readout on the display.

## Parts Often Needed

| Part | Notes |
|------|-------|
| IGBT power module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-vfd-fault-0001-overcurrent&k=IGBT+power+module&tag=errorcodefixes-20) \| If the drive was damaged by a severe short; requires drive specialist |
| Motor (replacement) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-vfd-fault-0001-overcurrent&k=Motor+%28replacement%29&tag=errorcodefixes-20) \| If winding insulation tests below 1 MΩ |
| Motor cable (shielded VFD-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-vfd-fault-0001-overcurrent&k=Motor+cable+%28shielded+VFD-rated%29&tag=errorcodefixes-20) \| Replace if any conductor shows insulation damage |
## When to Call a Pro

If the fault appears with no mechanical load, the cable and motor test clean, and parameters are correct, the drive's current sensing circuits or IGBTs may be damaged. ABB-certified drive service is required for internal component repair.
