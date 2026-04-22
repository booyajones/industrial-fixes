---
title: "Yaskawa A1000 OC Fault — Overcurrent"
description: "Yaskawa A1000 drive OC fault means overcurrent on the output. Learn causes, how to diagnose OCA, OCb, OCC variants, parameter fixes, and hardware checks."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
  - a1000
  - overcurrent
---

# Yaskawa A1000 OC Fault — Overcurrent

The **OC fault** on the Yaskawa A1000 high-performance vector drive means output current has exceeded approximately 200% of rated drive current (instantaneous trip). The drive shuts down immediately. The A1000 is Yaskawa's medium-heavy-duty drive used in demanding applications including conveyors, compressors, fans, and pumps.

## A1000 OC Fault Variants

| Code | Phase | Description |
|---|---|---|
| OCA | Acceleration | Overcurrent during speed ramp-up |
| OCb | Deceleration | Overcurrent during speed ramp-down |
| OCC | Constant speed | Overcurrent at steady state |
| OC | At stop | Overcurrent at zero speed (short circuit suspect) |

## Jump to Fix

- [Most Likely Cause](#most-likely-cause)
- [Diagnosis](#diagnosis)
- [Parameters](#parameters)

## Common Causes {#most-likely-cause}

| Cause | Fault Variant | Likelihood |
|---|---|---|
| Acceleration ramp too aggressive | OCA | Very High |
| Mechanical load jam or seized bearing | OCC | High |
| Deceleration ramp too fast (high inertia load) | OCb | High |
| Incorrect V/f or vector control tuning | OCA | Medium |
| Short circuit in motor cable or motor | OCA / OC | Medium |
| Failed output IGBT | OCA | Medium |
| Load demand spike (starting against back-pressure) | OCA | Medium |

## Step-by-Step Diagnosis {#diagnosis}

**Step 1 — Identify the fault type**
Check the A1000 fault log (U2-01 through U2-10 store recent faults with conditions):
- OCA: increase acceleration time (C1-01) — start with 2x the current setting
- OCb: increase deceleration time (C1-02) or enable braking resistor if high-inertia load
- OCC: check for mechanical jam, load spike, or insufficient torque limit setting

**Step 2 — Extend ramp times (OCA / OCb)**
- C1-01 (Acceleration Time 1): default 10 sec — try 20–30 sec for heavy loads
- C1-02 (Deceleration Time 1): increase if high-inertia loads cause OCb

**Step 3 — Check mechanical system**
- With power off: rotate the load by hand
- Any binding, stiffness, or inability to turn = mechanical issue causing stall

**Step 4 — Run motor auto-tune**
- A1000 auto-tune: T1-01 = 1 (Rotational auto-tune — motor spins)
- Auto-tune optimizes vector control for the specific motor
- Eliminates excess magnetizing current that causes OCA

**Step 5 — Megger test motor and cable**
- With drive output disconnected: megger each phase to ground
- Below 1 MΩ: insulation fault — may read as overcurrent

**Step 6 — Check IGBT output stage**
- Power off — wait 5 minutes for DC bus discharge
- Diode test from U, V, W to DC+ and DC-
- Short in either direction = failed IGBT — drive repair required

## Key A1000 Parameters for OC Faults

| Parameter | Function | OC-Relevant Setting |
|---|---|---|
| C1-01 | Acceleration Time 1 | Increase for OCA |
| C1-02 | Deceleration Time 1 | Increase for OCb |
| L3-01 | Stall Prevention — acceleration | 1 (enabled) for variable loads |
| L3-04 | Stall Prevention — constant speed | 1 (enabled) |
| L3-06 | Stall Prevention — deceleration | Adjust for high-inertia loads |
| E1-01 | Input voltage setting | Must match actual supply |
| T1-01 | Auto-tune selection | Run after new motor or OC fault |

## A1000 vs V1000 OC Comparison

| Feature | V1000 | A1000 |
|---|---|---|
| Frame size | 0.5–20 HP | 1–600+ HP |
| Torque control | V/f + Basic closed loop | Full closed-loop vector |
| OC trip level | 200% rated | 200% rated |
| Braking resistor | Optional | Standard on most frames |

> **Pro tip:** The A1000 supports S-curve acceleration (C2-01 through C2-04) which smooths the ramp profile. Enabling S-curve significantly reduces OCA faults on applications with high starting torque requirements like conveyors or compressors.
