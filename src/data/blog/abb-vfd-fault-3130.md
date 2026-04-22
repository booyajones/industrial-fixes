---
title: "ABB VFD Fault 3130 — Input Phase Loss Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-04-12T08:00:00Z
modDatetime: 2024-04-12T08:00:00Z
slug: abb-vfd-fault-3130
featured: false
draft: false
tags:
  - vfd
  - abb
  - phase-loss
description: "ABB VFD fault 3130 means the drive has detected a missing or unbalanced input phase. This guide covers diagnosis and fixes for the ABB ACS550/ACS580/ACS880 input phase loss fault."
---

## Error Code: ABB 3130 — Input Phase Loss

**What it means:** ABB fault code 3130 (INPUT PHASE LOSS) means the drive's input phase monitor has detected a missing, open, or severely unbalanced phase on the three-phase AC input supply. ABB ACS-series drives continuously monitor the three input phases. When one phase drops out or falls significantly below the others, the DC bus capacitors begin to see asymmetric charging — causing voltage ripple that exceeds the drive's acceptable limit. The drive shuts down to protect its DC bus capacitors and IGBTs from the resulting stress.

## Common Causes

- **Blown input fuse on one phase** — The most common cause. A blown fuse on one of the three input phases removes that phase from the supply. The drive sees a two-phase supply and faults.
- **Open circuit breaker on one phase** — A circuit breaker that has tripped on one phase only (a single-pole trip in a three-pole breaker) removes that phase.
- **Loose or corroded input terminal** — A loose line terminal (L1, L2, or L3) on the drive's power terminal block causes intermittent or full phase loss, especially under vibration.
- **Failed input contactor — one phase** — If a main input contactor is used ahead of the drive, a single failed contact removes one phase.
- **Utility supply issue** — A utility phase loss or downed line on one of the three distribution phases. This is less common but occurs after storms or utility faults.

## Diagnosis Steps

1. With the drive powered down, use a multimeter to measure AC voltage between all three input phase pairs at the drive's input terminals (L1-L2, L2-L3, L1-L3). All three readings should be within 3% of each other. A zero or significantly low reading on any pair identifies the missing phase.
2. Work upstream: measure voltage at the output of the upstream circuit breaker or disconnect. If one phase is missing at the breaker output but present at the input, the breaker has a failed pole.
3. Inspect input fuses if present. Visual inspection of HRC fuses is not always reliable — test fuse continuity with power off using a multimeter across each fuse.
4. Inspect the drive's input terminals (L1, L2, L3) for loose screws, corrosion, or heat discoloration (indicating arcing at a loose connection).
5. If all upstream voltages check out correctly at the drive terminals, the drive's internal phase monitoring circuit may have faulted — but this is rare. Confirm by measuring all three phases under load with a clamp meter.

## Fix

Replace a blown input fuse with the correct rated HRC fuse (match voltage, current, and I²t rating). Reset the tripped circuit breaker pole if accessible. Tighten any loose input terminals to the specified torque (refer to ABB installation manual for terminal torque specs — typically 10–17 Nm for larger drives).

If a failed input contactor is identified: inspect the contactor contacts for pitting or welding and replace the contactor or its contact block.

After fixing the supply issue, clear the fault on the drive (press RESET or cycle power) and confirm all three input phases are balanced before restarting.

## Parts

| Part | Where to Buy |
|------|-------------|
| HRC input fuses (match rating) | Grainger, Amazon |
| Input terminal block (if damaged) | Grainger |
| Three-phase input contactor | Grainger, Amazon |

## When to Call a Technician

Utility phase loss requires contacting the power company. Working inside high-voltage VFD enclosures (above 480V) requires a licensed electrician. For 480V ACS drives: all input-side work should be done by a qualified electrician with the drive fully locked out and tested for zero voltage before touching any terminal.
