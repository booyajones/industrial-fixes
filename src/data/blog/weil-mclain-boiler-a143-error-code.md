---
title: "Weil-McLain Boiler A143 Error - Causes & Fix"
description: "A143 is not a standard Weil-McLain fault code. Check your boiler's diagnostics menu for the actual stored fault name and consult the manual."
pubDatetime: 2026-06-18T09:52:37Z
modDatetime: 2026-06-18T09:52:37Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
money_part: "Flame rod / flame sensor"
diy_or_pro: "pro"
free_checks:
  - "Enter the boiler diagnostics or contractor menu and write down the exact fault name from the error history."
  - "Inspect all wire terminals and connectors at the control board, gas valve, flame sensor, and limit switches for corrosion or looseness."
  - "Check that the thermostat or zone controller is calling for heat and that the circulator pump is running."
---

## Weil-McLain Boiler A143 Error — What It Means

The code A143 does not appear in verified Weil-McLain manufacturer documentation as a standard fault or lockout identifier. Weil-McLain boilers store fault history in the contractor diagnostics menu, and the displayed event identifier may vary by control type and firmware. The string you see may be a timestamp, event number, or display artifact rather than the actual fault name.

To diagnose correctly, enter the boiler's contractor or diagnostics menu, navigate to Errors, Past Errors, or Fault History, and record the full fault description. Match that fault to the troubleshooting chart in your boiler's installation and service manual. Common lockout causes on Weil-McLain boilers include ignition and flame-sensing problems, gas-pressure issues, sensor faults, circulator or flow problems, low-water cutoff trips, limit-circuit faults, and loose or corroded wiring connections.

## Before You Replace Anything

Many technicians replace the boiler control board first when they see an unfamiliar code. Always retrieve the stored fault history from the diagnostics menu and test the specific circuit or sensor named in that fault before changing the board.

[Jump to Fix](#fix)

## Common Causes

- **Ignition or flame-sensing failure (~30%)** A dirty or misaligned flame rod, cracked ignitor, or poor ground connection prevents the control from proving flame and triggers a lockout.
- **Gas-pressure or gas-valve fault (~20%)** Low inlet pressure, a stuck gas valve, or incorrect valve wiring stops the burner from lighting or holding flame.
- **Sensor or limit-circuit problem (~20%)** A faulty high-limit switch, blocked vent switch, low-water cutoff, or temperature sensor opens the safety circuit and locks out the boiler.
- **Circulator or flow issue (~15%)** A seized circulator pump, closed valve, air lock, or low system pressure prevents water flow and trips the boiler's internal limits.
- **Wiring or connection fault (~10%)** Loose terminal blocks, corroded spade connectors, or damaged thermostat wiring cause intermittent or missing signals that the control interprets as a fault.
- **Control-board or firmware glitch (~5%)** A corrupted fault log, power brownout, or failing board memory may display a non-standard code that does not match the actual fault.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the diagnostics menu show a clear fault name like 'Ignition Failure' or 'Low Water Cutoff'?</summary>
<div class="dtree-body"><strong>Yes:</strong> Follow the manual's troubleshooting steps for that specific fault and test the named component or circuit first.<br><strong>No:</strong> The displayed code may be a history event number or artifact. Power-cycle the boiler, re-enter diagnostics, and record all stored faults. If none appear, call a technician to inspect the control board and wiring.</div>
</details>

<details class="dtree"><summary>Is the circulator pump running when the thermostat calls for heat?</summary>
<div class="dtree-body"><strong>Yes:</strong> Flow is likely present. Check flame-sensing, gas pressure, and limit circuits next.<br><strong>No:</strong> Inspect the circulator for power, check the zone valves or relays, and verify system pressure is above the low-water cutoff threshold.</div>
</details>

<details class="dtree"><summary>Can you see a flame through the sight glass during a call for heat?</summary>
<div class="dtree-body"><strong>Yes:</strong> The burner is firing. A sensor, limit switch, or wiring fault is likely causing the lockout after ignition.<br><strong>No:</strong> No flame means an ignition, gas-supply, or gas-valve problem. Check inlet gas pressure and inspect the ignitor and flame rod.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power** to the boiler at the circuit breaker and wait 30 seconds before restoring it to clear any transient fault.
2. **Enter the diagnostics menu** by pressing and holding the appropriate button combination on the control (consult your model's manual for the exact sequence).
3. **Navigate to Errors, Past Errors, or Fault History** and write down every stored fault code and description exactly as displayed.
4. **Match each fault** to the troubleshooting table in the boiler's installation and service manual to identify the failed component or open circuit.
5. **Inspect the identified circuit or sensor** for loose connections, corrosion, damaged wiring, or component failure, and test resistance or continuity as specified in the manual.
6. **Repair or replace the faulty part**, reconnect all wiring, restore power, and initiate a call for heat to verify the boiler ignites and runs without a new lockout.
7. **Monitor the fault history** over the next few heating cycles to confirm the error does not return and that the stored faults list remains clear.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame rod / flame sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a143-error-code&k=Flame+rod+%2F+flame+sensor&tag=errorcodefixes-20) \| Order the sensor specified for your exact Weil-McLain model and control. |
| Hot-surface ignitor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a143-error-code&k=Hot-surface+ignitor&tag=errorcodefixes-20) \| Verify the ignitor style (flat ceramic or round) and voltage rating before ordering. |
| Gas valve | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a143-error-code&k=Gas+valve&tag=errorcodefixes-20) \| Match the valve model number on the data plate and confirm gas type (natural or LP). |
| Boiler control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a143-error-code&k=Boiler+control+board&tag=errorcodefixes-20) \| Only replace after confirming all sensors, limits, and wiring are intact and the stored fault points to the board itself. |

## When to Call a Pro

Call a licensed heating technician if you cannot access the diagnostics menu, if the stored fault history is empty or displays non-standard characters, or if you lack a gas-pressure gauge and multimeter to test components safely. Gas-fired boiler work requires knowledge of combustion, venting, and electrical control circuits. A technician will retrieve the full fault log, measure gas inlet and manifold pressure, test flame rectification current, verify limit and sensor operation, and inspect the heat exchanger and vent system for blockages or damage. Professional diagnosis prevents misdiagnosis, avoids unnecessary part replacement, and ensures the boiler operates safely and within code.

**Rough cost:** A pro service call runs about $150-350.
