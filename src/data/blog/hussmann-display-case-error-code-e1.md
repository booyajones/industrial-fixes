---
title: "Hussmann Display Case Error Code E1 — Causes & Fix"
description: "What Hussmann display case error code E1 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - refrigeration
  - hussmann
money_part: "Defrost heater"
most_likely_cause: "Open defrost heater"
---

## What this code means
Hussmann display case error code E1 usually indicates a defrost heater fault or a defrost circuit failure on cases using electronic case controllers. The controller commanded a defrost cycle but did not see the expected temperature response at the evaporator sensor, or it detected an open heater circuit. On medium-temp and low-temp supermarket cases, that leaves frost building on the evaporator until airflow falls off and product temperature starts rising. In service, E1 often comes down to an open heater, a failed defrost termination sensor, or a relay problem in the case controller.

## Common Causes

- **Open defrost heater** — The heater element burned open, so the case enters defrost with no heat applied to the evaporator.
- **Failed defrost termination sensor** — The controller cannot verify coil temperature rise during defrost, so it logs the heater circuit as failed.
- **Defrost relay or contactor fault** — The controller sends the command, but the relay never closes and heater voltage never reaches the circuit.
- **Heavy ice load on the evaporator** — If airflow has been restricted for days, the case can carry so much ice that a normal defrost cycle cannot recover temperature as expected.

## Step-by-Step Fix {#fix}

1. **Inspect the evaporator for ice load** — Remove the access panel and look at the coil. A solid block of ice points to a failed defrost circuit or a long-running airflow problem.
2. **Test the defrost heater for continuity** — Lock out power, isolate the heater leads, and ohm the heater. An open circuit means the heater element has failed.
3. **Check heater voltage during a forced defrost** — Put the case controller into manual defrost and measure voltage at the heater terminals. If no voltage is present, move upstream to the relay or controller output.
4. **Test the defrost termination sensor** — Measure sensor resistance and compare it to the Hussmann sensor chart for the current coil temperature. Replace sensors that read open, shorted, or far out of range.
5. **Reset the system** — After replacing the failed component and clearing excess ice, restart the case and verify the next forced defrost heats the coil and clears E1.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Defrost heater | [Amazon](https://www.amazon.com/dp/B07FVP4CY6?ascsubtag=ecf-hussmann-display-case-error-code-e1&tag=errorcodefixes-20) \| Replace if continuity is open or the heater sheath is damaged |
| Defrost termination sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-hussmann-display-case-error-code-e1&k=Defrost+termination+sensor&tag=errorcodefixes-20) \| Replace if temperature response to the controller is wrong |
| Defrost relay or controller output board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-hussmann-display-case-error-code-e1&k=Defrost+relay+or+controller+output+board&tag=errorcodefixes-20) \| Replace if the heater never gets voltage during forced defrost |
## When to Call a Pro

Defrost circuits in supermarket cases often run at line voltage and may tie into rack controls or store EMS controls. If you lose heater power upstream of the case controller, bring in a commercial refrigeration electrician or rack tech.
