---
title: "Daikin Mini Split PJ-01 Error - Causes & Fix"
description: "PJ-01 on Daikin mini splits points to a communication fault between indoor and outdoor units. Check wiring connections first."
pubDatetime: 2026-07-25T08:03:48Z
modDatetime: 2026-07-25T08:03:48Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - daikin
money_part: "Indoor unit control board (PCB assembly)"
most_likely_cause: "loose or corroded terminal connections on the control wiring"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power off the system at both disconnect boxes, then inspect every terminal on the indoor and outdoor control blocks for tightness and corrosion"
  - "Verify that both indoor and outdoor units are receiving the correct supply voltage by checking at their respective disconnects"
---

## Daikin Mini Split PJ-01 Error — What It Means

The PJ-01 error code on a Daikin mini split system indicates a communication problem between the indoor air handler and the outdoor condensing unit. The two units exchange control signals over low-voltage wiring, and when that signal is interrupted, weak, or garbled, the system halts and displays this code.

Communication errors can stem from loose or corroded terminals, damaged control wire, incorrect voltage supply to one of the units, or a failed control board. Because the exact definition of PJ-01 can vary slightly across Daikin model families, always consult your installation manual or wiring diagram to confirm the code's meaning for your specific system. In most cases, the problem lies in the field wiring rather than in the electronics themselves.

## Before You Replace Anything

Many people replace the indoor control board first, only to find the real issue is a loose terminal screw or a pinched wire in the line-set chase. Inspect and re-seat every terminal connection before ordering any board.

[Jump to Fix](#fix)

## Common Causes

- **Loose or corroded terminal connections (~40%)** Vibration, moisture, or improper installation can loosen screw terminals on the control blocks, breaking the communication path.
- **Damaged or pinched control wire (~25%)** The low-voltage conductors running between units may be nicked, crushed, or shorted inside the line-set chase or wall penetration.
- **Incorrect supply voltage to one unit (~15%)** A tripped breaker, blown fuse, or voltage sag can starve the outdoor unit's transformer and prevent it from powering the communication circuit.
- **Failed indoor control board (~10%)** The PCB in the air handler may have a faulty relay or microcontroller that cannot send or receive the serial signal.
- **Failed outdoor control board (~10%)** The condensing unit's main board may have a damaged communication driver or corrupted firmware.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Are both the indoor and outdoor units receiving power when you check at their disconnect boxes?</summary>
<div class="dtree-body"><strong>Yes:</strong> Power supply is intact, so focus on the control wiring terminals and continuity between units.<br><strong>No:</strong> Restore power by resetting the breaker or replacing the fuse, then check if the code clears after a restart.</div>
</details>

<details class="dtree"><summary>When you inspect the terminal blocks at both units, do you see any loose screws, green corrosion, or burnt marks?</summary>
<div class="dtree-body"><strong>Yes:</strong> Clean corrosion with contact cleaner, tighten every screw, and replace any visibly charred wire ends.<br><strong>No:</strong> The terminals are sound, so test the control wire for continuity and shorts with a multimeter.</div>
</details>

<details class="dtree"><summary>Does the error clear after you power-cycle both units by turning off their disconnects for two minutes?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault may have been transient noise or a soft lock, but monitor the system for a week to confirm stability.<br><strong>No:</strong> A persistent code points to a wiring fault or board failure that needs professional diagnosis.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power** at both the indoor and outdoor disconnect boxes to make sure safe work on control circuits.
2. **Remove the cover** from the indoor unit's control compartment and locate the terminal strip where the thin control wires land.
3. **Inspect and tighten** every screw terminal, looking for green corrosion, burnt insulation, or loose strands.
4. **Repeat the inspection** at the outdoor unit's control board, paying special attention to terminals marked with communication labels or numbers that match your wiring diagram.
5. **Check continuity** of each control wire from indoor to outdoor using a multimeter set to resistance mode, verifying no breaks or shorts to ground.
6. **Restore power** to both units and observe the display; if the code persists, measure the DC voltage across the communication terminals as specified in your service manual.
7. **Call a technician** if wiring and voltage checks pass but the error remains, since further diagnosis requires board-level testing and potential refrigerant work if components must be replaced.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Indoor unit control board (PCB assembly) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-mini-split-pj-01-error-code&k=Indoor+unit+control+board+%28PCB+assembly%29&tag=errorcodefixes-20) \| Match the exact model and revision number printed on your existing board. |
| Outdoor unit control board (main PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-mini-split-pj-01-error-code&k=Outdoor+unit+control+board+%28main+PCB%29&tag=errorcodefixes-20) \| Confirm compatibility with your condenser model and serial number range. |

## When to Call a Pro

Call a licensed HVAC technician whenever you are uncomfortable working with line-voltage electrical panels, when terminal inspection and power checks do not resolve the code, or when you suspect a board failure. Replacing a mini split control board often requires recovering refrigerant, brazing new fittings, and programming system parameters that are not accessible to homeowners. A qualified tech will carry a laptop interface to read detailed fault logs, test communication signals with an oscilloscope, and verify that replacement boards are flashed with the correct firmware for your model. Attempting board swaps without proper tools can void your warranty and introduce refrigerant leaks.

**Rough cost:** A pro service call runs about $150-400.
