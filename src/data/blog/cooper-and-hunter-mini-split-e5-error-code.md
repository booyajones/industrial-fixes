---
title: "Cooper & Hunter Mini Split E5 Error - Causes & Fix"
description: "E5 on Cooper & Hunter mini splits points to outdoor unit power or inverter trouble. Restart first, then check wiring and voltage."
pubDatetime: 2026-05-31T08:45:18Z
modDatetime: 2026-05-31T08:45:18Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - cooper-and-hunter
---

## Cooper & Hunter Mini Split E5 Error — What It Means

Cooper & Hunter does not publish a single universal definition for E5 across all mini split models. The manufacturer's manual instructs you to restart the unit and see if the code clears. If it returns, you should contact your dealer or a qualified technician. Cooper & Hunter's own troubleshooting content shows that E5 typically involves the outdoor unit's power electronics and inverter drive circuit, not a simple indoor sensor fault.

Because Cooper & Hunter uses multiple platforms, the exact trigger can vary by model. The common thread is trouble in the outdoor unit's power supply path, inverter board, or related components. Always check your model-specific service literature for the controlling definition.

[Jump to Fix](#fix)

## Common Causes

- **Abnormal supply voltage** Incoming line voltage at the outdoor unit is too high, too low, or unstable.
- **Incorrect outdoor terminal wiring** Line and neutral are swapped or loosely connected at the outdoor unit terminal block.
- **Failed bridge rectifier** One or more diodes in the rectifier have shorted or opened, blocking DC bus voltage.
- **Faulty IPM or outdoor main PCB** The intelligent power module or combined main board has failed and cannot drive the compressor.
- **Faulty PFC module or reactor** The power-factor-correction circuit or its inductance coil is open or miswired.

## Step-by-Step Fix {#fix}

1. **Turn off power** at the breaker, wait 30 seconds, then restore power and observe whether E5 clears after a full restart.
2. **Measure incoming voltage** at the outdoor unit terminal block with a multimeter and confirm it matches the nameplate rating.
3. **Inspect and verify outdoor wiring** to confirm line and neutral are landed correctly and all connections are tight.
4. **Test the bridge rectifier** by disconnecting power, measuring each diode junction with a multimeter in diode mode, and replacing the rectifier if any diode reads zero or open in both directions.
5. **Measure DC bus voltage** between the P and N terminals on the inverter side and compare it to your supply voltage to confirm the rectifier and PFC circuits are working.
6. **Check the reactor or inductance coil** for correct wiring and measure its resistance. Replace it if the reading is infinite or abnormal.
7. **Replace the IPM board or outdoor main PCB** if all power-section components test normal but the fault persists. On integrated designs, replace the entire outdoor main board.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Cooper & Hunter outdoor main PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-cooper-and-hunter-mini-split-e5-error-code&k=Cooper+%26+Hunter+outdoor+main+PCB&tag=errorcodefixes-20) \| Match the part number on your existing board label. On some models the IPM is integrated into this board. |
| Bridge rectifier module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-cooper-and-hunter-mini-split-e5-error-code&k=Bridge+rectifier+module&tag=errorcodefixes-20) \| Order by model number or measure the mounting holes and terminal layout if the label is worn. |
| PFC module or reactor coil | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-cooper-and-hunter-mini-split-e5-error-code&k=PFC+module+or+reactor+coil&tag=errorcodefixes-20) \| Check your model's parts diagram. Not all Cooper & Hunter platforms use a separate PFC stage. |

## When to Call a Pro

If the code does not clear after a restart, or if you are not comfortable working inside a live outdoor unit with high DC bus voltages, call a licensed HVAC technician. Diagnosing E5 requires measuring line voltage, testing rectifier diodes, and verifying DC bus levels. Mistakes can destroy expensive inverter boards or create a shock hazard. Because Cooper & Hunter does not publish detailed fault definitions in consumer manuals, a technician with access to model-specific service literature and the right meters will save you time and avoid parts-swapping guesswork.
