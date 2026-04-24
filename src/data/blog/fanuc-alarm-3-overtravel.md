---
title: "Fanuc Alarm 3 — Overtravel Minus Hardware Causes & Fix"
description: "What Fanuc alarm 3 overtravel minus means, why the hardware limit trips, and how to fix it step by step."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - cnc
  - fanuc
---

## Fanuc Alarm 3 — Overtravel Minus: What It Means

Fanuc Alarm 3 is an **Overtravel (Minus direction) hardware limit** — an axis has tripped the negative-direction hardware overtravel limit switch. It is the negative-direction counterpart to Alarm 2. The hardware OT switch in the minus direction is typically located at the back stroke of an axis (toward the machine's home position, depending on the axis convention). Tripping Alarm 3 often occurs during homing sequences or when a machine loses position reference and attempts to travel beyond the physical negative boundary.

[Jump to Fix](#fix)

## Common Causes

- **Reference (home) cycle overrun** — If the machine loses its reference position (after a battery failure or parameter loss), the homing cycle can drive the axis past the negative hardware limit switch before slowing down.
- **Program or MDI move to negative coordinates beyond the machine boundary** — A work offset or tool offset error can command an axis to coordinates outside the physical travel range.
- **Soft limit not set or misconfigured** — Parameter 1321 (negative software travel limit) not set correctly allows the axis to reach the hardware limit.
- **OT switch shifted or failed** — The minus OT switch may have physically moved from vibration or deteriorated, causing premature triggering.

## Step-by-Step Fix {#fix}

1. **Activate OT release** — Press and hold the OT Release button on the operator panel (the specific key varies by machine builder). This temporarily bypasses the hardware OT signal and allows controlled movement.
2. **Jog axis in the positive direction** — While holding OT release, jog the axis in the **plus** direction (away from the negative hardware limit). Move enough to clear the switch — approximately 5–10mm.
3. **Release OT release** — After clearing the switch, release the button. Alarm 3 should clear automatically.
4. **Re-reference the machine** — If Alarm 3 occurred during a homing sequence, repeat the reference cycle carefully. Watch that the axis decelerates and stops at the reference mark without re-tripping the OT switch.
5. **Verify parameters** — Check Parameter 1321 (negative travel limit for each axis). Confirm the limit is set so the software trips the axis before it reaches the hardware OT switch.
6. **Inspect the minus OT switch** — Visually check the switch bracket and actuator for physical shift. Check the wiring for damage. Verify the switch is not being triggered by a contaminated or worn cam.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Overtravel limit switch | [Amazon](https://www.amazon.com/s?k=Overtravel+limit+switch&tag=errorcodefixes-20) \| Replace if physically damaged or triggering prematurely |
| Absolute encoder battery | [Amazon](https://www.amazon.com/s?k=Absolute+encoder+battery&tag=errorcodefixes-20) \| Replace if battery failure caused position loss that led to the homing overrun |
## When to Call a Pro

Repeated Alarm 3 during homing may indicate the reference point parameters (Parameter 1240/1241 for grid shift) are incorrectly set, or the encoder battery has failed and the home position is lost. A Fanuc-certified technician should set up the homing parameters to prevent future overruns.
