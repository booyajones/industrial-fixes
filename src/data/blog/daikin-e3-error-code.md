---
title: "Daikin E3 Error Code — Causes & Fix"
description: "What Daikin E3 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T08:00:00Z
modDatetime: 2026-04-22T08:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - mini-split
  - daikin
---

## Daikin E3 Error Code — What It Means

Daikin error code E3 indicates a fan motor fault — specifically, the indoor unit fan motor has stopped or is running at a speed the control board can't verify. Daikin uses Hall-effect feedback on the fan motor to continuously monitor RPM. When actual speed deviates from commanded speed beyond the allowed tolerance, or when no feedback signal arrives at the PCB, the board triggers E3 and shuts the unit down. This protects the motor from running against a blocked condition and protects the refrigerant circuit from operating with poor airflow.

[Jump to Fix](#fix)

## Common Causes

- **Obstructed or dirty indoor coil and fan** — A heavily fouled evaporator coil or a fan wheel clogged with dust and lint creates enough resistance to overload or stall the fan motor.
- **Failed fan motor** — Daikin indoor fan motors are brushless DC (BLDC) types that can fail outright or lose their feedback encoder signal. A motor that spins slowly or intermittently triggers E3.
- **Faulty fan motor capacitor** — On older Daikin split models using AC induction indoor fans (rarer), a failed capacitor prevents startup and triggers the fault.
- **PCB failure** — The main indoor PCB drives the fan motor via an IPM (Intelligent Power Module). A shorted IPM or failed driver circuit can prevent the motor from receiving correct drive voltage.

## Step-by-Step Fix {#fix}

1. **Inspect and clean the indoor unit** — Remove the front panel and filter. Look at the fan wheel and evaporator coil. If the wheel is packed with lint or the coil is caked with dust, clean both before any other diagnosis.
2. **Manually spin the fan wheel** — With power off, push the fan wheel by hand. It should spin freely with minimal resistance. Stiffness or grinding indicates a seized bearing — replace the motor.
3. **Check for obstructions** — Look for anything physically blocking the fan wheel: a plastic bag sucked in, a loose panel piece, debris.
4. **Power cycle the unit** — Clear the fault at the indoor PCB by cutting power for 30 seconds. If E3 returns immediately, the motor or PCB is faulty.
5. **Reset the system** — If the motor is confirmed good and no obstruction exists, reset power. If E3 clears and stays clear through a cooling cycle, it was a transient overload.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Indoor fan motor (BLDC) | [Amazon](https://www.amazon.com/s?k=Indoor+fan+motor+%28BLDC%29&tag=errorcodefixes-20) \| Model-specific; Daikin part numbers vary widely by series |
| Indoor PCB (main board) | [Amazon](https://www.amazon.com/s?k=Indoor+PCB+%28main+board%29&tag=errorcodefixes-20) \| If the motor tests good but E3 persists, PCB fan driver may be shorted |
| Fan wheel (cross-flow) | [Amazon](https://www.amazon.com/s?k=Fan+wheel+%28cross-flow%29&tag=errorcodefixes-20) \| Replace if heavily worn or permanently fouled |
## When to Call a Pro

BLDC motor diagnosis requires measuring drive voltage output from the PCB with an oscilloscope or specialized Daikin service tool. If the motor tests mechanically sound but E3 persists, a tech with Daikin equipment can isolate board vs. motor faults quickly.
