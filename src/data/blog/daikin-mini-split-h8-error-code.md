---
title: "Daikin H8 Error Code - Causes & Fix"
description: "H8 means DC current sensor fault in the outdoor unit's inverter. Most common fix: replace the outdoor unit inverter PCB board."
pubDatetime: 2026-06-30T09:56:10Z
modDatetime: 2026-06-30T09:56:10Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - daikin
money_part: "Daikin outdoor unit inverter PCB"
most_likely_cause: "defective outdoor unit PCB (inverter board)"
likelihood: "the most common fix"
diy_or_pro: "pro"
free_checks:
  - "Power-cycle the system: turn off both indoor and outdoor unit breakers for 5 minutes, then restore power to clear any transient faults."
  - "Verify the H8 code using the remote (hold Cancel button 5-6 seconds until 00 appears, then press to scroll through codes and listen for a long beep at H8)."
---

## What this code means
The H8 error code on a Daikin mini-split indicates a DC current sensor fault in the outdoor unit. This means the inverter board detects an abnormality in the current flowing to the compressor. The CT (current transformer) sensor system on the compressor input circuit is defective, or the inverter system is reporting a problem with the power transistor or reactor that the sensor cannot validate correctly.

This is an outdoor unit fault related to the inverter circuit's ability to monitor and control compressor current. The inverter PCB uses the CT sensor to track how much DC current the compressor is drawing. When the sensor signal is missing, erratic, or the power components feeding the compressor are damaged, the board logs an H8 code and shuts down to prevent further damage.

## Before You Replace Anything

Some techs replace the compressor itself when they see a current-related code, but H8 is a sensor or board fault, not a compressor failure. Test the inverter wiring and board first before condemning the compressor.

## Common Causes

- **Defective outdoor unit PCB (inverter board)** The inverter board's CT sensor circuit or signal-processing components fail, causing false or missing current readings.
- **Faulty inverter wiring or loose connections** Loose, corroded, or damaged wiring between the inverter board and compressor or CT sensor disrupts the current-monitoring signal.
- **Defective power transistor in the inverter module** A failed transistor in the inverter causes abnormal current flow that the CT sensor cannot validate, triggering the H8 code.
- **Defective reactor (inductor) in the inverter circuit** The reactor smooths DC current to the compressor, and if it shorts or opens, the CT sensor reports a fault.
- **Failed DC current sensor (CT) itself** The CT sensor can fail outright, producing no output signal even when the inverter and compressor are functioning normally.

## Step-by-Step Fix {#fix}

1. **Turn off power** at the breakers for both the indoor and outdoor units and wait 5 minutes to clear transient faults, then restore power and check if the H8 code returns.
2. **Verify the error code** using the remote control: hold the Cancel button for 5 to 6 seconds until 00 appears on the display, then press Cancel repeatedly to scroll through stored codes and listen for a long beep when H8 is reached.
3. **Inspect the outdoor unit** for visible damage: remove the outdoor unit cover and look for loose wiring at the inverter board, compressor terminals, and CT sensor connections, plus any burn marks, melted insulation, or cracked components on the board.
4. **Test the reactor and power transistors** if you have a multimeter and are comfortable with high-voltage work: measure the reactor resistance (should be roughly 0.5 to 2 ohms, near zero means shorted, infinite means open) and check the DC bus voltage (should be around 300 to 380 VDC for a 230 VAC input system, unstable voltage indicates transistor or reactor failure).
5. **Replace the outdoor unit PCB (inverter board)** if wiring is intact and the code persists, since this is the most common fix for H8 errors on Daikin mini-splits.
6. **Replace the reactor or power transistor module** if you installed a new board but the H8 code returns immediately, indicating a failed inductor or transistor rather than a board fault.
7. **Run a post-repair test** by operating the unit in cooling mode and using a clamp meter to confirm compressor current stays within the model's specification (typically 3 to 15 amps for residential units) and that the H8 code does not reappear.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Daikin outdoor unit inverter PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-mini-split-h8-error-code&k=Daikin+outdoor+unit+inverter+PCB&tag=errorcodefixes-20) \| Match the exact model number on your outdoor unit's label and the part number printed on the existing board. |
| Reactor (inductor) for Daikin inverter | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-mini-split-h8-error-code&k=Reactor+%28inductor%29+for+Daikin+inverter&tag=errorcodefixes-20) \| Needed only if the board is good but H8 persists and reactor tests show a short or open circuit. |
| Power transistor module (IPM) for Daikin inverter | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-mini-split-h8-error-code&k=Power+transistor+module+%28IPM%29+for+Daikin+inverter&tag=errorcodefixes-20) \| Required if visible damage or testing confirms a failed transistor and the reactor tests good. |

## When to Call a Pro

Call a qualified HVAC technician for any H8 error code on a Daikin mini-split. This fault involves high-voltage inverter circuits, DC current sensing, and compressor control systems that require specialized tools (multimeter, clamp meter, DC voltage probes) and training to diagnose safely. Working inside the outdoor unit's electrical compartment carries risk of electric shock (300+ VDC on the bus) and can void warranties if you damage the inverter board or compressor. A tech will test the CT sensor output, measure reactor resistance and DC bus voltage, inspect power transistors for shorts, and replace the inverter PCB or damaged components. DIY replacement of the inverter board is possible if you are experienced with HVAC electrical work and can source the exact part, but incorrect installation or failure to address underlying issues (bad reactor or wiring) will cause the new board to fail immediately.
