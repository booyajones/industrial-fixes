---
title: "Siemens Micromaster F0060 - Causes & Fix"
description: "F0060 means ASIC timeout, an internal drive electronics failure. Most likely fix: reset the drive. If it returns, replace the inverter."
pubDatetime: 2026-06-02T10:37:36Z
modDatetime: 2026-06-02T10:37:36Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - siemens
---

## Siemens Micromaster F0060 — What It Means

F0060 on a Siemens Micromaster drive stands for ASIC Timeout. This fault indicates that the drive's internal application-specific integrated circuit (ASIC) did not complete its processing or communication task in the expected time window. It is an internal electronics failure in the drive's control section, not a motor overload, wiring fault, or external device problem. Siemens documentation confirms this code points to a failure within the inverter's control electronics.

[Jump to Fix](#fix)

## Common Causes

- **Internal control electronics failure** The drive's ASIC or supporting circuits have stopped responding correctly due to hardware degradation or component failure.
- **Temporary firmware or processing hang** A one-time software glitch or internal logic error prevented the ASIC from completing its cycle on time.
- **Power supply disturbance during operation** A brief voltage sag, spike, or noise event disrupted the internal processor, causing it to miss its timeout deadline.
- **Accumulated electromagnetic interference (EMI)** Electrical noise from surrounding equipment coupled into the drive's control circuits and disrupted ASIC communication.
- **Overheating of control board components** High ambient temperature or blocked ventilation caused control-board components to operate outside specification and fail to respond in time.
- **Drive age or manufacturing defect** Older units or a batch-specific hardware defect in the ASIC or control board can trigger persistent timeout faults.

## Step-by-Step Fix {#fix}

1. **Record the fault** and operating conditions (load, temperature, runtime) in your maintenance log before taking any action.
2. **Reset the drive** using one of three methods: cycle the control power off and back on, use the keypad reset function, or send a digital reset command if your control system supports it.
3. **Monitor for recurrence** by running the drive under normal load for at least one full duty cycle to see if F0060 reappears.
4. **Inspect the enclosure and ventilation** to confirm the drive is not overheating and that intake and exhaust vents are clear of dust and obstructions.
5. **Check supply power quality** at the input terminals with a multimeter or power-quality meter to rule out voltage sags, surges, or high line noise that might stress the control board.
6. **Verify all control wiring and terminal connections** for tightness, corrosion, or signs of arcing, even though this fault is internal, to eliminate any contributing external factors.
7. **Replace the inverter** if the fault returns after reset and environmental checks are normal, as Siemens service documentation specifies inverter replacement as the corrective action for persistent F0060 faults.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens Micromaster inverter/converter assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0060-fault-code&k=Siemens+Micromaster+inverter%2Fconverter+assembly&tag=errorcodefixes-20) \| Match the exact model, frame size, and voltage rating to your original drive. Siemens specifies inverter replacement for persistent F0060. |
| Replacement control board (if available separately) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0060-fault-code&k=Replacement+control+board+%28if+available+separately%29&tag=errorcodefixes-20) \| Some Micromaster models offer field-replaceable control boards. Verify availability and compatibility with Siemens or an authorized distributor. |

## When to Call a Pro

Call a qualified drives technician or contact Siemens service if the F0060 fault returns after a simple reset, if you lack experience working inside variable-frequency drives, or if your process cannot tolerate downtime for trial-and-error troubleshooting. Persistent ASIC timeout faults require inverter replacement or board-level repair that is best handled by factory-trained personnel with access to Siemens diagnostic tools and genuine replacement parts. If the drive is under warranty or part of a critical industrial process, involve your Siemens representative or a certified integrator immediately to avoid voiding coverage or risking further equipment damage.
