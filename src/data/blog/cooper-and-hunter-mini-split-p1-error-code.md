---
title: "Cooper and Hunter Mini Split P1 Error - Causes & Fix"
description: "P1 means over-voltage or under-voltage protection. Check incoming power at the unit first, then inspect wiring and outdoor boards."
pubDatetime: 2026-05-31T08:46:24Z
modDatetime: 2026-05-31T08:46:24Z
author: "Dana Kowalski"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - cooper-and-hunter
---

## Cooper and Hunter Mini Split P1 Error — What It Means

On Cooper and Hunter mini splits, P1 is an over-voltage or under-voltage protection fault. The indoor or outdoor control system detects supply voltage outside the acceptable range and stops operation to protect the inverter and compressor electronics. The unit may start briefly, then shut down and display P1, because the protection logic is active rather than the fault being a simple display issue. Cooper and Hunter's own troubleshooting material identifies P1 as a voltage protection malfunction caused by an abnormal voltage rise or drop detected by the voltage detection circuit.

[Jump to Fix](#fix)

## Common Causes

- **Incoming power abnormality** Utility fluctuation, storm event, generator instability, or house voltage outside spec causes the unit to detect voltage protection conditions.
- **Loose or damaged wiring** Loose terminals, damaged insulation, incorrect landing, or corrosion at power or communication connections between indoor and outdoor units triggers the fault.
- **Failed IPM or inverter board** The outdoor inverter board or intelligent power module fails and produces abnormal DC bus voltage even when incoming line voltage is correct.
- **Reactor or PFC circuit failure** The reactor or power factor correction circuit in the outdoor unit loses continuity or develops incorrect resistance, causing voltage detection errors.
- **Outdoor main board failure** The outdoor control board itself fails and reports voltage protection even when supply voltage, wiring, and inverter circuits are normal.

## Step-by-Step Fix {#fix}

1. **Power cycle the unit** after a short shutdown to confirm the fault is not a transient utility event before proceeding with diagnostics.
2. **Measure supply voltage at the unit** with a multimeter and verify the incoming power is correct for your model before replacing any parts.
3. **Inspect all power and communication wiring** at the terminal block, looking for loose terminals, damaged insulation, incorrect landing, or corrosion, and repair or replace wiring as needed.
4. **Test the outdoor DC bus voltage** by measuring P-to-N voltage with the unit in standby (should be around 310 V) and during startup (should be about 220 to 400 V according to Cooper and Hunter troubleshooting media).
5. **Check the reactor or PFC circuit** for continuity and resistance (Cooper and Hunter states it should measure around 0 ohms), and replace the reactor if the reading is not correct.
6. **Replace the IPM board** if the DC bus voltage is abnormal and the reactor checks are normal.
7. **Replace the outdoor main board** if all voltage checks, wiring, reactor, and IPM tests are normal but the P1 fault persists.

## Parts Often Needed

| Part | Notes |
|------|-------|
| IPM board (outdoor inverter module) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-cooper-and-hunter-mini-split-p1-error-code&k=IPM+board+%28outdoor+inverter+module%29&tag=errorcodefixes-20) \| Replace if DC bus voltage is abnormal during standby or startup testing. |
| Reactor (PFC reactor / choke) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-cooper-and-hunter-mini-split-p1-error-code&k=Reactor+%28PFC+reactor+%2F+choke%29&tag=errorcodefixes-20) \| Replace if continuity or resistance is not around 0 ohms as specified. |
| Outdoor main control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-cooper-and-hunter-mini-split-p1-error-code&k=Outdoor+main+control+board&tag=errorcodefixes-20) \| Replace if all other voltage and component checks are normal but P1 persists. |
| Power wiring / terminal connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-cooper-and-hunter-mini-split-p1-error-code&k=Power+wiring+%2F+terminal+connectors&tag=errorcodefixes-20) \| Replace any damaged, loose, or corroded wiring or terminal connections found during inspection. |

## When to Call a Pro

Call a licensed HVAC technician if you are not comfortable working with live voltage or if you do not have a multimeter and the knowledge to safely measure AC supply voltage and DC bus voltage. Misdiagnosis can result in unnecessary part replacement or further damage to the inverter electronics. If you have verified that incoming power is correct and all wiring is tight and undamaged, the remaining diagnostics and board replacement require technical skill and proper handling of static-sensitive control boards.
