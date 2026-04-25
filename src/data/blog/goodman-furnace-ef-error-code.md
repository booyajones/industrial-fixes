---
title: "Goodman Furnace EF Error Code — Invalid Flame Signal"
description: "Goodman furnace EF error code: what EF means, causes of invalid flame signal, and step-by-step fixes for Goodman GMSS, GMEC, and AMANA furnaces."
pubDatetime: 2026-04-22T19:00:00Z
modDatetime: 2026-04-22T19:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - goodman
  - furnace
---

## Goodman Furnace EF Error Code — What It Means

Goodman furnace error code **EF** stands for **Invalid Flame Signal** — also described as "flame sensed out of sequence." EF means the furnace control board detected a flame signal when it was NOT commanding the gas valve to open, or the flame signal disappeared unexpectedly during an active heating cycle.

EF is a safety-critical code. The control board is designed to detect flame outside of the expected ignition window because this can indicate gas valve leakage, a failed control board, or a wiring fault that poses a combustion safety risk.

EF appears on Goodman GMSS96, GMEC96, GMVC96, GMVC80, and Amana AMSS, AMVC series furnaces. It is displayed on furnaces with diagnostic LED displays as "EF" or equivalent flash sequence.

## Causes of EF Error Code

| Cause | Likelihood | Test |
|-------|-----------|------|
| [Flame sensor picking up stray EMI](https://www.amazon.com/s?k=Flame+sensor+picking+up+stray+EMI&tag=errorcodefixes-20) | High | Check sensor wiring routing |
| [Leaking gas valve (gas valve not fully closing)](https://www.amazon.com/s?k=Leaking+gas+valve+%28gas+valve+not+fully+closing%29&tag=errorcodefixes-20) | Medium-High | Listen/smell for gas after shutdown |
| [Flame sensor wiring shorted to chassis](https://www.amazon.com/s?k=Flame+sensor+wiring+shorted+to+chassis&tag=errorcodefixes-20) | Medium | Inspect flame sensor wire insulation |
| [Control board fault — false flame sense input](https://www.amazon.com/s?k=Control+board+fault+%E2%80%94+false+flame+sense+input&tag=errorcodefixes-20) | Medium | Swap control board to test |
| [HSI (hot surface igniter) generating voltage](https://www.amazon.com/s?k=HSI+%28hot+surface+igniter%29+generating+voltage&tag=errorcodefixes-20) | Lower | Disconnect igniter lead; retest |
| [Gas valve stuck partially open](https://www.amazon.com/s?k=Gas+valve+stuck+partially+open&tag=errorcodefixes-20) | Lower | Verify valve closes fully |

## Step-by-Step Diagnosis

**Step 1: Verify the sequence**
Confirm whether EF appears during startup (before ignition commanded) or during shutdown (after the gas valve should have closed). This distinction is critical:
- EF before ignition = stray electrical signal or board input fault
- EF after shutdown = gas valve not fully closing OR residual flame on sensor

**Step 2: Inspect flame sensor wire routing**
The flame sensor wire carries a micro-amp signal that is extremely susceptible to interference. The wire must not run parallel to 115VAC wires. If the wire is bundled with line-voltage wires inside the furnace, separate them. Replace the wire with the original routing per the wiring diagram inside the furnace door.

**Step 3: Check for a leaking gas valve**
Turn the furnace off. After 5 minutes, carefully smell the flue pipe and burner area for any residual gas odor. A gas valve that leaks slightly when de-energized can keep a small flame alive after shutdown — enough to trip EF. If you detect any gas odor with the valve off, shut off the main gas supply and call a technician immediately.

**Step 4: Inspect flame sensor insulation**
The flame sensor is a metal rod that extends into the burner flame. Its ceramic insulator keeps the sensing circuit isolated from the burner chassis ground. If the ceramic is cracked or the wire insulation is burned through at the furnace chassis, the control board may see a permanent low-level signal. Inspect the sensor rod's ceramic mount and the wire from the sensor to the board.

**Step 5: Test with the control board**
If all wiring and components test normal, the control board's flame sense input circuit may have failed — reading a false flame signal. A Goodman-certified technician can measure the flame sense microamp signal directly to verify whether the fault is real or a board misread.

## Quick Fix Summary

- **Most common fix:** Re-route flame sensor wire away from 115VAC line-voltage wires
- **Second most common:** Replace flame sensor rod if ceramic is cracked
- **If gas odor after shutdown:** Gas valve replacement — call a technician

## When to Call a Pro
Any indication of gas leakage is an immediate service call. Do not operate a furnace with a suspected leaking gas valve. EF codes that persist after wiring corrections require a technician to measure the flame microamp signal and inspect the gas valve coil resistance.
