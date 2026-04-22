---
title: "Yaskawa VFD Fault LF — Causes & Fix"
description: "What Yaskawa VFD fault LF means, why output phase loss trips the drive, and how to fix it."
pubDatetime: 2026-04-22T10:00:00Z
modDatetime: 2026-04-22T10:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
---

## Yaskawa VFD Fault LF — What It Means

Fault LF on a Yaskawa drive (A1000, V1000, GA700, GA800) stands for Output Phase Loss. The drive's output current monitoring detected that one of the three output phases (U/T1, V/T2, W/T3) has significantly lower current than the others during operation. This indicates either a broken connection between the drive and motor, or an open phase winding inside the motor. The drive trips on LF to prevent motor overheating and bearing damage from single-phasing.

[Jump to Fix](#fix)

## Common Causes

- **Broken output phase wire** — A conductor in the motor cable that has broken internally (common in flexing cable applications) passes the continuity test but opens under vibration and current.
- **Loose output terminal connection** — A terminal at the drive output (U/T1, V/T2, W/T3) or at the motor terminal box that is not fully torqued can arc and fail open at higher load.
- **Open motor winding** — An internal break in one phase of the motor windings. This is a motor failure requiring rewinding or motor replacement.
- **Contactor contact failure between drive and motor** — If a contactor or bypass switch is installed between the drive output and the motor, a failed contact on one pole causes output phase loss.

## Step-by-Step Fix {#fix}

1. **Check output terminal torque** — With power off and lockout/tagout applied, verify that all output terminal screws at the drive and the motor terminal box are torqued to specification. Loose terminals are the most common cause on new or recently serviced installations.
2. **Measure output phase currents** — Using a clamp meter during operation (or the drive's built-in current monitor), compare current on all three output phases. A phase with zero or very low current is the LF-tripping phase.
3. **Test motor winding resistance** — With power off and cable disconnected from the drive, measure resistance between all motor terminal pairs: U-V, V-W, U-W. Readings should be within 5% of each other. Infinite resistance on one pair = open winding.
4. **Test cable continuity** — With cable disconnected at both drive and motor, use a multimeter to confirm continuity on all three conductors. Replace the cable if any conductor is open or has intermittent continuity (wiggle the cable while testing).
5. **Inspect any intermediate contactors** — If a bypass or output contactor is installed, verify all three poles close and make solid contact when energized.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Motor cable (VFD-rated, screened)](https://www.amazon.com/s?k=Motor%20cable%20(VFD-rated%2C%20screened)&tag=errorcodefixe-20) | Replace if any conductor shows intermittent or open continuity |
| [Motor (rewind or replacement)](https://www.amazon.com/s?k=Motor%20(rewind%20or%20replacement)&tag=errorcodefixe-20) | If open winding is confirmed |
| [Output contactor](https://www.amazon.com/s?k=Output%20contactor&tag=errorcodefixe-20) | Replace if single pole fails to make contact |

## When to Call a Pro

Verifying LF fault with a scope or power analyzer provides better data than a clamp meter for intermittent output phase loss. Motor rewinding requires a motor shop. Always use lockout/tagout before working on drive output circuits.
