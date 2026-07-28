---
title: "Daikin U2 Error Code - Causes & Fix"
description: "U2 means power supply voltage too low, too high, or a brief power failure. Most common fix: reset the unit and check outdoor PCB fuses."
pubDatetime: 2026-06-30T09:47:06Z
modDatetime: 2026-06-30T09:47:06Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - daikin
money_part: "Daikin outdoor PCB (model-specific)"
most_likely_cause: "Faulty outdoor PCB after a power surge"
likelihood: "the most common hardware failure"
diy_or_pro: "pro"
free_checks:
  - "Turn off the unit at the breaker, wait 10-15 minutes, then restart to clear a temporary voltage lockout."
  - "Use a multimeter to verify incoming voltage at the outdoor disconnect is within the required range (typically 200-240V)."
  - "Inspect all wiring connections at the outdoor unit terminal block for loose or corroded terminals."
---

## What this code means
The U2 error code indicates a malfunction of the power supply or an instantaneous power failure. Specifically, Daikin defines it as drop voltage or main circuit overvoltage. Your mini split detected abnormal voltage (either too low during a brownout or too high during a surge) or a brief power interruption. The unit has a built-in supply voltage monitor that locks out the system when voltage dips or spikes, even if power is not completely lost.

This is an electrical fault rather than a refrigeration problem. The code tells you the system sensed unstable power and shut down to protect internal components. Most cases trace back to building wiring issues, brief utility brownouts, or damage to the outdoor unit's circuit board from a power surge.

## Before You Replace Anything

Homeowners often assume the indoor unit or refrigerant is at fault. Before replacing any boards, check incoming voltage at the disconnect and test all four fuses on the outdoor PCB for continuity.

## Common Causes

- **Damaged outdoor PCB (~40%)** Power surges blow fuses or destroy the PFC circuit on the outdoor board, leaving 2 of 4 fuses with no continuity.
- **Brownout or low voltage (~25%)** Sustained low voltage from the utility or undersized building wiring triggers the supply voltage monitor.
- **Instantaneous power failure (~15%)** A brief power interruption or surge damages internal components and sets the code.
- **Defective magnetic contactor (~10%)** A faulty K11M magnetic contactor on the A1P board fails to pass power downstream after the fuses.
- **Loose or corroded wiring (~10%)** Bad connections, frayed cables, or loose jacks at the outdoor unit cause voltage drop or intermittent faults.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the error clear after turning off the breaker for 10 minutes and restarting?</summary>
<div class="dtree-body"><strong>Yes:</strong> It was likely a temporary voltage fluctuation. Monitor for recurrence and have an electrician check building voltage if it returns.<br><strong>No:</strong> The fault is persistent. Proceed to check the outdoor PCB fuses and wiring connections.</div>
</details>

<details class="dtree"><summary>Do all four fuses on the outdoor PCB show continuity when tested with a multimeter?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fuses are good. Check the K11M magnetic contactor and look for loose connections or damaged traces on the board.<br><strong>No:</strong> Two or more fuses are blown. The outdoor PCB is damaged and must be replaced.</div>
</details>

<details class="dtree"><summary>Is the incoming voltage at the outdoor disconnect within 200-240V (or your local utility spec)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Building power is stable. The problem is inside the outdoor unit (likely PCB or contactor).<br><strong>No:</strong> Voltage is abnormal. Have an electrician inspect the building wiring, breaker sizing, and utility supply.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power** at the main breaker or disconnect switch for the mini split.
2. **Wait 10-15 minutes** to allow the control board to fully reset and clear any temporary voltage lockout.
3. **Restart the unit** and observe whether the U2 code reappears immediately or after a few minutes of operation.
4. **Measure incoming voltage** at the outdoor disconnect with a multimeter, verifying it is within the required range (typically 200-240V depending on your region).
5. **Open the outdoor unit** cover and locate the outdoor PCB (main control board).
6. **Test all four fuses** on the outdoor PCB for continuity. If two or more fuses show no continuity, the board has been damaged by a surge and must be replaced.
7. **Inspect the K11M magnetic contactor** on the A1P board. If fuses are good but power is missing downstream, the contactor may be defective.
8. **Check all wiring connections** at the outdoor terminal block for loose screws, corrosion, or frayed insulation. Re-tighten and replace damaged wiring as needed.
9. **Examine the PFC circuit** on the outdoor PCB for burnt components, discolored areas, or cracked solder joints, which indicate surge damage.
10. **If external voltage is unstable**, consult a licensed electrician to inspect building wiring, breaker sizing, and utility supply quality.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Daikin outdoor PCB (model-specific) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-mini-split-u2-error-code&k=Daikin+outdoor+PCB+%28model-specific%29&tag=errorcodefixes-20) \| Match the board part number stamped on your existing PCB. |
| K11M magnetic contactor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-mini-split-u2-error-code&k=K11M+magnetic+contactor&tag=errorcodefixes-20) \| Used on the A1P board; verify compatibility with your outdoor unit model. |

## When to Call a Pro

Call a licensed HVAC technician if the error persists after a reset, if you measure abnormal voltage at the disconnect, or if you are uncomfortable working inside the outdoor unit. A pro will open the outdoor unit, test fuses and the magnetic contactor, inspect the outdoor PCB for surge damage, and replace the board or contactor if needed. Because this fault involves high-voltage circuits and refrigerant lines nearby, leave the diagnosis and repair to a technician. If your building voltage is consistently low or fluctuating, also bring in an electrician to inspect the main panel, breaker sizing, and utility supply before replacing any mini split components.

**Rough cost:** A pro service call runs about $200-500 for PCB replacement and labor.
