---
title: "Lennox Error Code 432 — Causes & Fix"
description: "What Lennox error code 432 means, why the blower motor faults, and how to fix it step by step."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - lennox
---

## Lennox Error Code 432 — What It Means

Lennox code 432 is a **blower motor fault** — the control board or communicating system detected that the indoor blower motor failed to start, stalled, or reported an operating fault. On iComfort-enabled systems, the board receives direct communication from the ECM motor and can identify the failure precisely. On standard systems, the board times out waiting for the motor to reach speed. The furnace will not operate until the blower fault is cleared.

[Jump to Fix](#fix)

## Common Causes

- **ECM motor communication fault** — The ECM motor module loses communication with the control board; can be caused by a bad module, wiring issue, or board failure.
- **Failed blower motor** — Motor winding failure or bearing seizure prevents the motor from spinning up.
- **Dirty blower wheel** — Heavy debris buildup overloads the motor on startup, triggering overcurrent protection.
- **Control board relay failure** — The board doesn't send the run command to the motor.

## Step-by-Step Fix {#fix}

1. **Check for fault details on the communicating display** — On iComfort systems, navigate to System Diagnostics to get the sub-code for the 432 fault; it will pinpoint whether it's a motor, module, or communication issue.
2. **Test Fan-Only mode** — Set the thermostat to Fan-On. If the blower runs normally, the fault may be intermittent or heat-call-specific.
3. **Inspect the blower wheel** — With power off, check the wheel for debris accumulation or contact with the housing. Clean and balance as needed.
4. **Check motor wiring** — Inspect all connectors between the motor module and control board. Look for corrosion, pushed-out terminals, or pinched wires.
5. **Test motor module power supply** — Verify 120/240V supply to the motor at the motor connector with the board commanding it to run.
6. **Reset the system** — Power off at the disconnect for 60 seconds, restore, and call for heat. On iComfort systems, also power-cycle the thermostat.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ECM motor module (control module) | [Amazon](https://www.amazon.com/s?k=ECM+motor+module+%28control+module%29&tag=errorcodefixes-20) \| Lennox-specific module — matches the motor's frame and communicating protocol |
| ECM blower motor | [Amazon](https://www.amazon.com/s?k=ECM+blower+motor&tag=errorcodefixes-20) \| Full motor replacement if module tests good but motor still fails |
| Control board | [Amazon](https://www.amazon.com/s?k=Control+board&tag=errorcodefixes-20) \| If board relay is confirmed failed and no signal is reaching the motor |
## When to Call a Pro

ECM motor module replacements on Lennox communicating systems require matching the exact part number. Installing the wrong module can damage the motor. If diagnostics point to the module, confirm the part number before ordering and have a certified Lennox dealer verify the installation.

## Related Articles

- [Lennox Error Code 292 — Ignition Failure Fix](/posts/lennox-292-error-code/)
- [Lennox EL296V Error Codes — Variable-Speed Furnace Diagnostic Guide](/posts/lennox-el296v-error-codes/)
- [Lennox Elite Series Furnace Error Codes — Fault Code Diagnostic Guide](/posts/lennox-elite-series-furnace-codes/)
- [Lennox 103 Error Code — Causes & Fix](/posts/lennox-error-code-103/)
- [Lennox Error Code 111 — Causes & Fix](/posts/lennox-error-code-111/)
