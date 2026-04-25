---
title: "Yaskawa VFD Fault BB — Causes & Fix"
description: "What Yaskawa VFD fault BB (Baseblock) means, why it's different from a hard fault, and when action is needed."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
---

## Yaskawa VFD Fault BB — What It Means

Yaskawa BB stands for **Baseblock** — this is **not a hard fault**. Baseblock is a controlled safe state where the drive's output transistors are disabled (gate signals are blocked), stopping current flow to the motor without an actual hardware failure. The drive enters BB when it receives an external baseblock command via a digital input configured for that function (typically terminal S5 or H1-xx = 8). The motor coasts to a stop; the drive remains powered and ready. BB displays as an alarm, not a fault, and clears automatically when the baseblock signal is removed.

**Key distinction:** A hard fault (like OC, OV, or GF) requires a manual reset. BB clears on its own when the baseblock input goes inactive. If you're seeing BB and the drive won't run, the issue is almost always the external control signal — not the drive itself.

[Jump to Fix](#fix)

## Common Causes

- **Baseblock input signal stuck active** — The digital input wired to baseblock is held low (or high, depending on configuration), keeping the drive in baseblock indefinitely.
- **Wiring fault at the baseblock terminal** — A loose wire or unintended short to the common terminal activates the baseblock input.
- **PLC or safety relay holding baseblock** — The upstream control system (PLC, safety relay, or E-stop circuit) is intentionally or unintentionally holding the baseblock command active.
- **Incorrect parameter setting** — A digital input terminal is accidentally configured for baseblock (H1-xx = 8) when it should be configured for another function.

## Step-by-Step Fix {#fix}

1. **Identify the baseblock input terminal** — Check the parameter group H1-01 through H1-10 (digital input settings). Find which terminal is set to value 8 (baseblock). Note which physical terminal number this corresponds to.
2. **Check the terminal signal** — With a multimeter, measure the voltage between the baseblock terminal and the drive's common (SC) terminal. If it reads 0V (for sink logic) or is otherwise in the active state, the input is being commanded.
3. **Trace the signal source** — Follow the wire from the baseblock terminal back to its source (PLC output, safety relay, or external switch). Determine if the source is intentionally held active or if there's a wiring/hardware issue.
4. **Verify the wiring** — Check for loose terminals, broken wires, or unintended shorts between the baseblock terminal and the common.
5. **Check parameter configuration** — If no external device should be holding baseblock, confirm that the H1 parameter for that terminal is correctly set. Reassign it to 0F (not used) if the baseblock input is not needed.
6. **Remove the baseblock signal** — Once the source is identified and corrected, removing the baseblock command will immediately clear BB and allow the drive to run.

## Parts Often Needed

| Part | Notes |
|------|-------|
| No parts typically needed | [Amazon](https://www.amazon.com/s?k=No+parts+typically+needed&tag=errorcodefixes-20) \| BB is a control signal issue, not a hardware failure |
| Terminal block or wiring | [Amazon](https://www.amazon.com/s?k=Terminal+block+or+wiring&tag=errorcodefixes-20) \| If the baseblock input terminal is damaged or wiring has failed |
## When to Call a Pro

If BB is being commanded by a safety system or E-stop circuit and you don't know why the safety device is activating, do not bypass it. Have a controls engineer investigate the safety circuit logic before overriding the baseblock command.

## Related Articles

- [Yaskawa A1000 OC Fault — Overcurrent](/posts/yaskawa-a1000-fault-oc/)
- [Yaskawa A1000 Fault UV1, DC Bus Undervoltage Causes & Fix](/posts/yaskawa-a1000-fault-uv1/)
- [Yaskawa A1000 Fault Code OC — Overcurrent Diagnosis & Fix](/posts/yaskawa-a1000-oc-fault-code/)
- [Yaskawa GA700 OC Fault — Overcurrent Fix](/posts/yaskawa-ga700-fault-oc/)
- [Yaskawa GA700 Fault UV1 — Main Circuit Undervoltage Causes & Fix](/posts/yaskawa-ga700-fault-uv1/)
