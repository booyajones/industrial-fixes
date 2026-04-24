---
title: "Yaskawa VFD Fault SC — Causes & Fix"
description: "What Yaskawa VFD fault SC means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
---

## Yaskawa VFD Fault SC — What It Means

Yaskawa VFD fault SC (IGBT Short Circuit or Gate Drive Fault) indicates that the drive detected a short circuit condition on its output IGBT (insulated gate bipolar transistor) stage. The gate drive circuit monitors current through each IGBT switch, and when current spikes to a level indicating a short — either between two output phases, from an output phase to the DC bus, or through a failed IGBT itself — the gate drive fires a hardware overcurrent protection and shuts down the drive in microseconds. SC is a hard fault that cannot be cleared by software reset if the hardware fault condition still exists.

[Jump to Fix](#fix)

## Common Causes

- **Phase-to-phase short on output cables** — The cable between the drive and motor develops a short between two conductors, creating a near-zero impedance path that immediately trips SC.
- **Motor winding phase-to-phase short** — Internal motor winding failure where two phases short together, presenting a near-zero load impedance to the drive output.
- **Failed IGBT module** — One or more IGBTs in the drive's output power stage fail in a short-circuit mode (collector-emitter short). This is common after a previous overcurrent or overvoltage event that stressed the devices.
- **Contactor or shorting device on output** — A motor run/bypass contactor that closes while the drive is running can present a short to the drive's output. Never close an output contactor while the drive is supplying voltage.

## Step-by-Step Fix {#fix}

1. **Disconnect the motor cable at the drive output (T1/T2/T3)** — Remove all connections to the drive's output terminals. Measure resistance between each pair of output terminals (T1-T2, T2-T3, T1-T3) with a multimeter. Any near-zero reading with the drive powered off and discharged indicates either a failed IGBT or the measurement includes a parallel path.
2. **Check motor winding resistance** — With the motor cable disconnected from the drive, measure resistance between each motor terminal pair (U-V, V-W, U-W). All three readings should be equal within a few percent. A low or zero reading indicates a phase-to-phase short in the motor.
3. **Megger test motor and cable** — Perform insulation resistance tests at 500V between phase conductors and between phases and ground.
4. **Test drive IGBT modules** — With the drive fully de-energized and DC bus discharged (wait 10+ minutes), use a diode-test mode multimeter to check each IGBT. In one direction you should see a diode drop; in the other, near-infinite resistance. A short in both directions indicates a failed IGBT.
5. **Replace failed component** — Replace the motor, cable, or drive IGBT module (or full drive power module) as indicated by the test results.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Drive IGBT module / power board | [Amazon](https://www.amazon.com/s?k=Drive+IGBT+module+%2F+power+board&tag=errorcodefixes-20) \| Must match drive voltage/current rating; Yaskawa components are model-specific |
| Motor (replace or rewind) | [Amazon](https://www.amazon.com/s?k=Motor+%28replace+or+rewind%29&tag=errorcodefixes-20) \| If winding short is confirmed; rewinding larger motors is cost-effective |
| Output cable | [Amazon](https://www.amazon.com/s?k=Output+cable&tag=errorcodefixes-20) \| Replace if insulation damage or conductor-to-conductor short found |
## When to Call a Pro

SC faults involving failed IGBTs inside the drive require capacitor discharge verification, high-voltage PPE, and component-level knowledge. IGBT module replacement on industrial drives is typically performed by a Yaskawa service technician or certified drive repair center.
