---
title: "Siemens SINAMICS G120 F00001 Fault — Causes & Fix"
description: "What Siemens SINAMICS G120 F00001 overcurrent fault means, why it trips, and how to diagnose and fix it step by step."
pubDatetime: 2026-04-22T13:00:00Z
modDatetime: 2026-04-22T13:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "VFD-rated motor cable"
most_likely_cause: "Motor winding or cable short"
---

## What this code means
The Siemens SINAMICS G120 **F00001 fault** is an **overcurrent trip**. The control unit has detected output current above the safe threshold for the power module, usually during startup, acceleration, or a short-circuit event. The drive shuts down immediately to protect the IGBTs and DC bus components. On G120 systems this can be caused by motor issues, cable faults, aggressive ramp settings, or a mechanical jam in the driven load.

## Common Causes

- **Motor winding or cable short** — A phase-to-phase or phase-to-ground fault on the motor side creates an instantaneous current spike.
- **Acceleration ramp too short** — Heavy loads like fans, conveyors, or pumps may demand more current than the module can supply when the ramp is too aggressive.
- **Mechanical jam** — A seized gearbox, binding bearing, or jammed process load forces the motor toward locked-rotor current.
- **Incorrect motor data** — If the drive was commissioned with the wrong motor nameplate values, current control can behave poorly and nuisance-trip.

## Step-by-Step Fix {#fix}

1. **Isolate the motor circuit** — Lock out power, disconnect the motor leads, and check phase-to-phase and phase-to-ground resistance on both the cable and motor.
2. **Review commissioning parameters** — Confirm motor voltage, current, frequency, and power in the G120 parameter set match the motor nameplate exactly.
3. **Increase ramp-up time** — Extend the acceleration time and test again. If the trip disappears, the original ramp was too fast for the load.
4. **Check the driven machine** — Turn the load manually if possible and inspect for mechanical drag, seized bearings, or a jammed conveyor, pump, or fan.
5. **Reset the system** — Clear the fault through the operator panel or by cycling control power, then test with the motor uncoupled if possible to separate electrical from mechanical causes.

## Parts Often Needed

| Part | Notes |
|------|-------|
| VFD-rated motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-sinamics-g120-fault-f00001&k=VFD-rated+motor+cable&tag=errorcodefixes-20) \| Replace if insulation is damaged or leakage to ground is found |
| Motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-sinamics-g120-fault-f00001&k=Motor&tag=errorcodefixes-20) \| Replace when winding insulation is weak or winding resistance is unbalanced |
| Siemens power module or control unit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-sinamics-g120-fault-f00001&k=Siemens+power+module+or+control+unit&tag=errorcodefixes-20) \| Replace only after external motor and cable faults are ruled out |
## When to Call a Pro

If F00001 persists with the motor disconnected or after commissioning values are corrected, the G120 power module may be damaged internally. Siemens drive service or a qualified industrial electrician should handle module-level diagnosis and replacement.
