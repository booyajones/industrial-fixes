---
title: "Cooper & Hunter Mini-Split P0 Error - Causes & Fix"
description: "P0 means outdoor inverter/power-module fault. Most often fixed by checking supply voltage, tightening wiring, or replacing the IPM board."
pubDatetime: 2026-05-31T08:45:59Z
modDatetime: 2026-05-31T08:45:59Z
author: "Dana Kowalski"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - cooper-and-hunter
money_part: "Cooper & Hunter outdoor main PCB / inverter control board"
most_likely_cause: "Incorrect or unstable supply voltage"
---

## Cooper & Hunter Mini-Split P0 Error — What It Means

The P0 code on a Cooper & Hunter mini-split signals a fault in the outdoor unit's inverter power section, specifically the IPM (Intelligent Power Module) or IGBT drive circuit that controls the compressor. This protection trips when the outdoor control board detects over-current, over-voltage, or another electrical anomaly in the inverter section that drives the compressor motor.

The code typically points to a problem in the outdoor unit rather than the indoor air handler. It can be triggered by unstable incoming power, damaged wiring, a failed inverter board, compressor electrical failure, or overheating of the inverter module due to poor ventilation or a non-running outdoor fan.

[Jump to Fix](#fix)

## Common Causes

- **Incorrect or unstable supply voltage** Incoming voltage at the outdoor unit is outside the acceptable range or fluctuating, preventing the inverter from operating safely.
- **Loose, burnt, or corroded wiring** Power leads, communication wires, compressor terminals, or board connectors are damaged, loose, or corroded, disrupting current flow.
- **Failed IPM or inverter board** The outdoor unit's intelligent power module or main inverter control board has shorted, overheated, or otherwise failed electronically.
- **Compressor electrical fault** The compressor windings show abnormal resistance, an open circuit, or a short to ground, causing the inverter to protect itself.
- **Outdoor fan or ventilation problem** The outdoor fan does not run or airflow is blocked, causing the inverter section to overheat and trip the protection circuit.
- **PFC circuit defect** A fault in the power-factor-correction section of the outdoor inverter prevents the module from generating the correct DC bus voltage.

## Step-by-Step Fix {#fix}

1. **Turn off power** to both indoor and outdoor units at the breaker or disconnect, wait three to five minutes, then restore power and check whether the code clears.
2. **Measure incoming voltage** at the outdoor unit's L1/L2 (230 V systems, expect about 240 V) or L/N (115 V systems, expect about 120 V) terminals with a multimeter to confirm supply is within ±10% of nominal.
3. **Inspect all wiring and connections** for heat damage, burn marks, corrosion, or looseness at the outdoor disconnect, control-board terminals, compressor leads, and indoor-to-outdoor communication cable, then tighten or repair as needed.
4. **Verify outdoor-fan operation** by powering the unit and confirming the fan spins freely and airflow is not blocked by debris or recirculation, since poor cooling can overheat the inverter module.
5. **Check the outdoor inverter board** for visible damage, burnt components, or overheating, and note any diagnostic LEDs that may indicate a board-level fault.
6. **Test the compressor terminals** by isolating the compressor electrically and measuring phase-to-phase resistance between U, V, and W with a multimeter; readings should be roughly equal and in the megohm range when checked against ground, and any unequal or zero readings suggest compressor failure.
7. **Replace the IPM board or outdoor main PCB** if compressor tests pass but the fault persists, or if visual inspection and multimeter checks of the inverter module (P to U/V/W and N to U/V/W, expecting megohm symmetry) reveal a failed power section.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Cooper & Hunter outdoor main PCB / inverter control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-cooper-and-hunter-mini-split-p0-error-code&k=Cooper+%26+Hunter+outdoor+main+PCB+%2F+inverter+control+board&tag=errorcodefixes-20) \| Match the exact model and board part number printed on your existing outdoor-unit control board. |
| IPM / intelligent power module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-cooper-and-hunter-mini-split-p0-error-code&k=IPM+%2F+intelligent+power+module&tag=errorcodefixes-20) \| Standalone module if your design separates the IPM from the main board; confirm compatibility by model. |
| Compressor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-cooper-and-hunter-mini-split-p0-error-code&k=Compressor&tag=errorcodefixes-20) \| Required only if terminal resistance tests show a short, open, or imbalanced windings; verify tonnage and refrigerant type. |

## When to Call a Pro

Call a licensed HVAC technician if you are not comfortable working with live high voltage, if the fault returns immediately after a power cycle, or if you lack a multimeter and the experience to safely measure compressor windings and inverter-board circuits. Inverter and IPM diagnostics require specialized knowledge of three-phase drive circuits, and misdiagnosis can lead to expensive part swaps. A pro can also recover refrigerant properly, perform a compressor change-out if needed, and make sure the replacement board is programmed and commissioned correctly for your model.
