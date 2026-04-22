---
title: "Lincoln Electric E13 Error Code — Causes & Fix"
description: "What Lincoln Electric E13 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - welding
  - lincoln-electric
---

## Lincoln Electric E13 Error Code — What It Means

The E13 fault on Lincoln Electric welders (Power MIG and Power Wave series) indicates an output contactor fault — the contactor that connects the welding output to the torch/electrode circuit either failed to close on an arc-start command or opened unexpectedly during a weld. This contactor is what physically enables welding output; if it won't close, no arc can be struck regardless of other settings.

[Jump to Fix](#fix)

## Common Causes

- **Worn or pitted output contactor contacts** — The output contactor switches on every arc start. High-frequency operation causes contact wear and eventually a contact that won't close or closes intermittently.
- **Failed contactor coil** — The electromagnetic coil that pulls the contacts closed can fail open, leaving the contactor permanently open.
- **Control board not triggering the contactor** — If the board's output contactor drive circuit has failed, the coil never receives the energize signal on arc start.
- **Wiring fault at the contactor** — A broken lead or loose terminal at the contactor coil input interrupts the drive signal.

## Step-by-Step Fix {#fix}

1. **Lock out and open the machine** — Disconnect input power and verify with a multimeter before opening the case. The output contactor is on the secondary (low-voltage output) side but input is still dangerous.
2. **Locate the output contactor** — It's a relay-style component on the output side, between the transformer/inverter and the welding terminals. Usually visible once the side panel is removed.
3. **Test the contactor coil** — Measure resistance across the coil terminals. Open circuit = failed coil. Typical coil resistance is 50–200Ω depending on model.
4. **Inspect the contacts** — Check contactor contacts for heavy pitting, burning, or welding together. Contacts in poor condition need replacement even if the coil tests good.
5. **Check the control drive signal** — With a multimeter on the coil input terminals, verify the board sends the energize voltage when an arc-start is triggered. No signal = board fault.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Output contactor](https://www.amazon.com/s?k=Output%20contactor&tag=errorcodefixe-20) | Match to Lincoln part number — coil voltage and contact current rating vary by model |
| [Control board](https://www.amazon.com/s?k=Control%20board&tag=errorcodefixe-20) | If no drive signal reaches the contactor coil |
| [Contactor wiring harness](https://www.amazon.com/s?k=Contactor%20wiring%20harness&tag=errorcodefixe-20) | If leads are damaged or terminals are corroded |

## When to Call a Pro

Output contactor replacement is straightforward for an experienced technician, but the work involves high-current connections. Lincoln Electric authorized service centers can diagnose whether the contactor or the board is the root cause before ordering parts.
