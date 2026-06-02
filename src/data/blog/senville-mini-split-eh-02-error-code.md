---
title: "Senville Mini Split EH 02 Error Code - Causes & Fix"
description: "EH 02 means the indoor board isn't detecting the fan motor's zero-crossing signal. Power-cycle the unit, then replace the indoor PCB."
pubDatetime: 2026-05-31T07:49:29Z
modDatetime: 2026-05-31T07:49:29Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - senville
---

## Senville Mini Split EH 02 Error Code — What It Means

EH 02 on Senville mini splits (LETO and AURA series) is a zero-crossing signal detection error on the indoor unit. The indoor control board is not receiving the expected zero-crossing feedback it uses to monitor the AC fan motor. This code applies only to models with an AC fan motor. If your unit uses a DC motor, Senville states the code does not apply and can be ignored.

The error typically points to unstable power, a wiring fault between the indoor PCB and fan-motor circuitry, or a failed indoor main board. Senville's official troubleshooting path centers on a power reset followed by indoor PCB replacement if the code persists.

[Jump to Fix](#fix)

## Common Causes

- **Erratic or unstable incoming power** Voltage fluctuations or poor supply to the indoor unit prevent the board from reading the zero-crossing signal cleanly.
- **Loose or corroded wiring connections** Poor contact between the indoor PCB and fan-motor harness interrupts the signal path.
- **Faulty indoor main board** The PCB's zero-crossing detection circuit has failed and cannot process the feedback even when wiring and power are correct.
- **Incorrect model interpretation** The code appears on a DC-motor unit where EH 02 does not apply and should be disregarded per Senville guidance.

## Step-by-Step Fix {#fix}

1. **Turn off all power** at the breaker or disconnect and wait a full two minutes before restoring power to reset the indoor board.
2. **Observe the display** when power returns. If EH 02 does not reappear, the transient fault has cleared and no further action is needed.
3. **Verify your fan-motor type** in the installation manual or spec sheet. If the indoor unit uses a DC motor, Senville states EH 02 does not apply and you may ignore the code.
4. **Check incoming voltage** at the indoor unit's terminal strip with a multimeter to confirm stable supply within nameplate range and no brownout conditions.
5. **Inspect all connectors and wiring** between the indoor main board and the fan-motor assembly for loose plugs, corrosion, or damaged insulation.
6. **Replace the indoor main board** if the error returns immediately after reset and all wiring and power checks are normal. Senville's troubleshooting video and service guide identify the indoor PCB as the repair component for persistent EH 02.
7. **Test the system** through a full cooling cycle after board replacement to confirm the zero-crossing signal is detected and the code does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Senville indoor main board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-senville-mini-split-eh-02-error-code&k=Senville+indoor+main+board+%28PCB%29&tag=errorcodefixes-20) \| Verify your exact LETO or AURA model and voltage before ordering. This is the primary component Senville identifies for EH 02. |
| Wiring harness (indoor unit) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-senville-mini-split-eh-02-error-code&k=Wiring+harness+%28indoor+unit%29&tag=errorcodefixes-20) \| Order only if you find visible damage to the connectors or wires between the PCB and fan motor during inspection. |

## When to Call a Pro

Call a licensed HVAC technician if the error persists after a power reset and you are not comfortable working inside the indoor unit's electrical enclosure. Replacing the indoor PCB requires disconnecting line voltage, handling static-sensitive components, and transferring communication jumpers or DIP-switch settings. A technician can also verify that the zero-crossing circuit is truly at fault and rule out less common issues such as a failing AC fan motor or main-board grounding problems. If your unit is under warranty, contact Senville support before attempting any board replacement to preserve coverage.
