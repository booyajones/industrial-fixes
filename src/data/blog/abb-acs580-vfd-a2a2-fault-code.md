---
title: "ABB ACS580 A2A2 Fault - Causes & Fix"
description: "A2A2 fault means DC link undervoltage on the ABB ACS580 VFD. Most often caused by low input power or loose AC connections."
pubDatetime: 2026-06-21T10:30:12Z
modDatetime: 2026-06-21T10:30:12Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - abb
money_part: "ABB ACS580 cooling fan (frame-size specific)"
most_likely_cause: "incoming AC power interruption or brown-out"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Measure AC voltage at the drive input terminals (L1, L2, L3) to confirm it is within ±10% of nominal and all three phases are present"
  - "Check for loose or corroded connections at the drive input terminals and tighten if necessary"
  - "Inspect input fuses and breakers for blown fuses or tripped positions and reset or replace as needed"
no_buy_pct: "60%"
---

## ABB ACS580 A2A2 Fault — What It Means

The A2A2 fault code on an ABB ACS580 variable frequency drive signals a DC link undervoltage condition. This means the internal DC bus voltage inside the drive has dropped below the minimum threshold needed for safe operation. The drive detects this either when stopped (if auxiliary power is too low) or during operation if incoming AC power is interrupted or browned out.

Unlike overcurrent or earth faults, A2A2 is strictly a power supply integrity issue. The drive's intermediate circuit relies on stable AC input to maintain the DC link voltage. When incoming voltage sags, disappears, or a phase is lost, the DC bus cannot sustain the required level and the drive trips to protect itself and the connected motor.

## Before You Replace Anything

Technicians sometimes assume the internal control board or DC capacitor has failed when the real problem is a loose input terminal or blown fuse upstream. Always measure input voltage and inspect all three phases before replacing internal drive components.

[Jump to Fix](#fix)

## Common Causes

- **Incoming AC power interruption or sag (~40%)** A brown-out, utility power dip, or complete loss of one or more AC phases at the input causes the DC link to drop below threshold.
- **Loose or corroded input connections (~30%)** Loose wiring terminals at L1, L2, or L3 create voltage drop under load and starve the DC link of stable power.
- **Blown input fuse or tripped breaker (~20%)** A blown fuse or tripped circuit breaker on the input side results in missing phase voltage and insufficient DC link charging.
- **Failed cooling fan or open front cover (~7%)** A stalled cooling fan or missing front cover can disrupt internal power distribution or cause the drive to misinterpret voltage levels.
- **Low auxiliary power supply (~3%)** If the drive relies on a 24V auxiliary supply for control logic, a drop in that supply can trigger the fault when the drive is stopped.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Do you measure correct voltage (within ±10% of nominal) on all three input phases (L1-L2, L2-L3, L3-L1)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Input power is stable. Move to checking internal drive components (fan, front cover, control board) or contact service.<br><strong>No:</strong> You have a power supply problem. Inspect upstream breakers, fuses, and utility service before troubleshooting the drive itself.</div>
</details>

<details class="dtree"><summary>Are all input terminal connections tight and free of corrosion?</summary>
<div class="dtree-body"><strong>Yes:</strong> Wiring is good. Check input protection devices (fuses, breakers) and upstream power quality.<br><strong>No:</strong> Clean and re-tighten all input terminals. Power cycle the drive and test again.</div>
</details>

<details class="dtree"><summary>Is the drive's cooling fan running when the drive is powered?</summary>
<div class="dtree-body"><strong>Yes:</strong> Fan is OK. Verify front cover is in place and parameter group 40 settings allow automatic restart if this is a warning fault.<br><strong>No:</strong> Replace the cooling fan. A stalled fan can cause the drive to shut down and may correlate with power supply issues.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Measure input AC voltage** at the drive's L1, L2, and L3 terminals with a multimeter. Confirm voltage is within ±10% of the drive's nominal rating (for example 400V ±40V or 480V ±48V) and that all three phases are present and balanced.
2. **Check for missing phases** by measuring voltage across all pairs (L1-L2, L2-L3, L3-L1). A missing or weak phase will show zero or very low voltage on one or more pairs.
3. **Inspect input wiring and terminals** for loose connections, corrosion, or burned spots. Re-tighten all terminals and clean any oxidation with contact cleaner.
4. **Inspect input fuses and breakers** upstream of the drive. Replace any blown fuses or reset any tripped circuit breakers. Verify the fuse or breaker rating matches the drive's requirements.
5. **Check the cooling fan** operation. Listen for the fan when the drive is powered. If the fan is not running or sounds labored, replace it with an ABB-approved replacement for your ACS580 frame size.
6. **Verify the front cover** is fully seated and latched. The drive may not operate correctly if the cover is open or loose, affecting internal power distribution.
7. **Power cycle the drive** by turning off the input power, waiting at least five minutes for the DC link capacitors to discharge, then restoring power. Clear the fault from the control panel and attempt to restart.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB ACS580 cooling fan (frame-size specific) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a2a2-fault-code&k=ABB+ACS580+cooling+fan+%28frame-size+specific%29&tag=errorcodefixes-20) \| Consult your drive nameplate for the correct fan part number for your frame size. |
| Input line fuses (rated for VFD service) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a2a2-fault-code&k=Input+line+fuses+%28rated+for+VFD+service%29&tag=errorcodefixes-20) \| Use fuses rated for VFD input duty and the correct amperage for your drive model. |

## When to Call a Pro

Call a qualified electrician or ABB service technician if you measure stable input power (all three phases within ±10% of nominal), all connections are tight, and the fault persists after a power cycle. A persistent A2A2 with good input power usually means an internal control board, DC link capacitor, or power supply circuit has failed. These components require drive disassembly, high-voltage work, and factory parts. Also call a pro if you are not comfortable working with three-phase power, measuring line voltage, or opening a VFD enclosure. VFDs store dangerous DC voltage even after input power is removed, and improper troubleshooting can damage the drive or cause electric shock.

**Rough cost:** A pro service call runs about $150-400 depending on whether it is a wiring fix or component replacement.

## See Also

- [ABB ACS550 EFB3 Fault - Causes & Fix](/posts/abb-acs550-vfd-efb3-fault-code/)
- [ABB ACS550 AI1 LOSS - Causes & Fix](/posts/abb-acs550-vfd-ai1-loss-fault-code/)
- [ABB ACS580 Fault 3220 — DC Undervoltage Fix](/posts/abb-acs580-fault-3220/)
- [ABB ACS580 A7AB Fault - Causes & Fix](/posts/abb-acs580-a7ab-fault-code/)
