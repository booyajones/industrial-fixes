---
title: "Trane 8 Flashes Error Code — Causes & Fix"
description: "What Trane 8 flash error code means, why the indoor blower faults, and how to fix it step by step."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - trane
---

## Trane 8 Flashes Error Code — What It Means

Eight flashes on a Trane furnace status LED indicates an **indoor blower (circulator) motor fault**. The control board commanded the blower to run but didn't receive confirmation that it reached operating speed within the expected time, or the motor drew excess current and tripped its internal protector. The furnace will shut down on heat calls until the fault is cleared. This is distinct from the inducer (draft) motor — the 8-flash code refers to the main blower that distributes conditioned air through the duct system.

[Jump to Fix](#fix)

## Common Causes

- **Failed blower motor run capacitor** — Capacitor weakness is the most common cause; the motor starts slowly, doesn't reach rated speed, and the board times out.
- **Seized or binding blower wheel** — Debris accumulation on the squirrel cage creates imbalance and drag; the motor overloads and trips thermal protection.
- **Faulty blower motor** — Winding failure or bearing failure causes the motor to stall or draw excessive current.
- **Control board output fault** — The board's blower relay or triac fails and doesn't send proper voltage to the motor.

## Step-by-Step Fix {#fix}

1. **Test the blower manually** — Set the thermostat to Fan-On. If the blower doesn't start or sounds sluggish, proceed to the capacitor.
2. **Check the run capacitor** — Discharge the capacitor, then measure capacitance. If reading is more than 10% below the rated µF, replace it.
3. **Spin the blower wheel by hand** — With power off, reach in and spin the wheel. It should spin freely with minimal resistance. If it's stiff or scrapes, remove and clean the wheel or replace the motor/bearing assembly.
4. **Measure motor voltage and current** — With power on and a call for heat, verify 120V (or 240V on some models) at the motor connector. If voltage is present but motor doesn't run, replace the motor.
5. **Inspect wiring to the blower** — Check for burned connectors or loose terminals at both the motor and the control board.
6. **Reset the system** — Power off for 30 seconds, restore, and call for heat. The blower should energize within 30–60 seconds of ignition.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Blower motor run capacitor | [Amazon](https://www.amazon.com/s?k=Blower+motor+run+capacitor&tag=errorcodefixes-20) \| Match µF and voltage; common sizes are 5 µF, 7.5 µF, 10 µF at 370V |
| ECM blower motor (variable-speed) | [Amazon](https://www.amazon.com/s?k=ECM+blower+motor+%28variable-speed%29&tag=errorcodefixes-20) \| Many Trane units use ECM motors — replacement requires matching module and motor |
| PSC blower motor (single-speed) | [Amazon](https://www.amazon.com/s?k=PSC+blower+motor+%28single-speed%29&tag=errorcodefixes-20) \| Match HP, RPM, frame, and rotation direction |
## When to Call a Pro

ECM (variable-speed) motors on Trane XV and XC series require a matched control module. If you replace an ECM motor without the correct module, the fault will persist. Have a technician confirm the ECM module is communicating properly before condemning the motor.
