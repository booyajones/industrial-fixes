---
title: "Yaskawa VFD Fault PF — Causes & Fix"
description: "What Yaskawa VFD fault PF means, why input phase loss trips the drive, and how to fix it."
pubDatetime: 2026-04-22T10:00:00Z
modDatetime: 2026-04-22T10:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
---

## Yaskawa VFD Fault PF — What It Means

Fault PF on a Yaskawa drive (A1000, V1000, GA700, GA800 series) stands for Input Phase Loss. The drive's input monitoring circuit detected that one or more of the three input AC phases (R/L1, S/L2, T/L3) is absent or significantly unbalanced relative to the others. The drive trips to prevent the DC bus capacitors and rectifier diodes from being overloaded by single-phase or unbalanced input.

[Jump to Fix](#fix)

## Common Causes

- **Blown fuse or tripped circuit breaker on one phase** — A fuse upstream of the drive that opens on one phase leaves the drive on two-phase input, which the PF detection immediately catches.
- **Loose or corroded input terminal** — A loose wire on one input phase terminal causes high resistance and intermittent phase loss, often appearing as PF at higher load conditions.
- **Contactor or disconnect failure** — A single-phase welded or failed-open contact in an upstream contactor causes permanent or intermittent phase loss.
- **Utility power phase imbalance** — An unbalanced utility supply (more than 2–3% voltage imbalance between phases) can trigger PF on drives with sensitive phase-loss detection, even without a complete phase loss.

## Step-by-Step Fix {#fix}

1. **Measure input voltage with main power on** — Use a true-RMS multimeter and measure voltage between all three phase pairs at the drive input terminals: R-S, S-T, and R-T. All three readings should be within 2% of each other and within the drive's input voltage range.
2. **Check upstream fuses** — Inspect the input fuses or circuit breaker for the drive. A blown fuse on one phase is confirmed by measuring voltage on both sides of the fuse — voltage before, zero after = blown. Replace blown fuses; investigate why they blew before restarting.
3. **Tighten input terminals** — With power off and lockout/tagout applied, check the torque on the input terminal block screws (R/L1, S/L2, T/L3). Tighten to the drive's specification (typically 1.2–2.5 Nm depending on wire size).
4. **Inspect the upstream disconnect and contactor** — Check that all three contacts of the main disconnect and any series contactors make and break cleanly. Measure voltage downstream of the contactor on each phase while it is closed.
5. **Clear the PF fault and restart** — After correcting the cause, reset the fault via the keypad or digital input and attempt to restart. Monitor input voltages during startup.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input fuses (class J or similar) | Match voltage, ampacity, and interrupt rating for the drive kW |
| Main contactor (3-pole) | Replace if contacts show burning or one pole fails to make |
| Input terminal block | Replace if terminals are corroded or cracked |

## When to Call a Pro

Phase imbalance from the utility supply requires contacting the utility or a licensed electrician to investigate the power system. Single-phase loss events that repeatedly blow fuses indicate a fault in the upstream distribution system requiring a qualified electrician.
