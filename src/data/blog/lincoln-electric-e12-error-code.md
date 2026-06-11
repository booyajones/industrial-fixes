---
title: "Lincoln Electric E12 Error Code — Causes & Fix"
description: "What Lincoln Electric E12 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T11:00:00Z
modDatetime: 2026-04-22T11:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - welding
  - lincoln-electric
money_part: "Input contactor"
---

## Lincoln Electric E12 Error Code — What It Means

The E12 fault on Lincoln Electric welders (Power MIG, Power Wave, and Invertec series) indicates an input contactor fault — the main input contactor that connects the primary power circuit to the transformer or inverter either failed to close on startup or opened unexpectedly during operation. Without a functioning contactor, the machine cannot energize its welding circuit.

[Jump to Fix](#fix)

## Common Causes

- **Failed input contactor coil** — The coil that energizes the contactor magnetically draws the contacts closed. A burned or open coil means the contactor never closes.
- **Welded or stuck contactor contacts** — High inrush current on startup can cause contacts to arc and weld together, preventing normal operation in either direction.
- **Control board not firing the contactor** — If the board's contactor drive output has failed, the contactor coil never receives the energize signal.
- **Loose or corroded wiring at the contactor** — High current connections at the contactor terminals can loosen or corrode over time, causing intermittent contact resistance that trips E12.

## Step-by-Step Fix {#fix}

1. **Locate the input contactor** — Open the machine side panel. The input contactor is a relay-style component on the primary power side, before the transformer or inverter module.
2. **Test the coil** — Measure resistance across the contactor coil terminals. An open circuit (infinite resistance) confirms a failed coil. Normal coil resistance varies by model but is typically 50–500Ω.
3. **Inspect the contacts** — With power off and properly locked out, check the contactor contacts for pitting, arcing, or welding. Welded contacts won't release; contacts with heavy pitting need replacement.
4. **Check the control signal** — With a multimeter on the control voltage terminals of the contactor coil, verify the board is sending the energize voltage during startup. No voltage = board fault.
5. **Inspect wiring connections** — Torque all contactor terminal screws to spec. Loose power connections at the contactor are a fire hazard as well as a fault source.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input contactor | [Amazon](https://www.amazon.com/dp/B0CJFZQVPT?ascsubtag=ecf-lincoln-electric-e12-error-code&tag=errorcodefixes-20) \| Match to exact Lincoln part number — coil voltage and contact rating vary |
| Control board | [Amazon](https://www.amazon.com/s?k=Control+board&tag=errorcodefixes-20) \| If board isn't sending energize signal to contactor |
| Input wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lincoln-electric-e12-error-code&k=Input+wiring+harness&tag=errorcodefixes-20) \| If leads to contactor are damaged |
## When to Call a Pro

Input contactor work involves primary AC voltage — always lock out and verify power is off before opening the machine. If you're not confident working on live AC power circuits, have a Lincoln authorized service center handle the repair.
