---
title: "ABB ACS580 A4A1 Fault - Causes & Fix"
description: "A4A1 means IGBT overtemperature in your ABB ACS580 drive. Most often caused by blocked cooling fins or a failed fan. Clean heatsink first."
pubDatetime: 2026-06-21T10:36:49Z
modDatetime: 2026-06-21T10:36:49Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "ABB ACS580 cooling fan assembly (frame-specific)"
most_likely_cause: "blocked or dirty heatsink fins preventing heat dissipation"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify ambient temperature around the drive is below 40°C (104°F) for frames R5-R9 or 50°C (122°F) for smaller frames"
  - "Power down and visually inspect heatsink fins for dust, lint, or debris blocking airflow"
  - "Check if the internal cooling fan spins freely by hand when powered off"
no_buy_pct: "60%"
---

## What this code means
Fault code A4A1 on an ABB ACS580 VFD signals IGBT overtemperature. The drive's internal power transistors (IGBTs) that switch motor current are exceeding their safe thermal limits. The drive estimates IGBT temperature using an internal algorithm based on load and cooling conditions rather than a direct sensor on the IGBT itself.

This fault trips when the estimated temperature climbs too high, protecting the drive from permanent damage. It does not always mean the IGBT has failed. In most cases the fault is triggered by poor cooling, dirty heatsinks, or an environment that exceeds the drive's ambient temperature rating.

## Before You Replace Anything

Technicians sometimes replace the entire drive thinking the IGBT module has failed, when in fact a failed cooling fan or clogged heatsink is the real problem. Always verify fan operation and clean the heatsink before ordering a new drive.

## Common Causes

- **Blocked or dirty heatsink fins (~40%)** Dust, dirt, or debris accumulates on the heatsink fins and prevents heat from escaping, causing the IGBT temperature estimate to rise.
- **Failed or obstructed cooling fan (~25%)** The internal cooling fan stops spinning or is blocked by foreign material, eliminating forced airflow through the heatsink.
- **Excessive ambient temperature (~15%)** The drive is installed in an enclosure or room where ambient temperature exceeds the rated limit (often 40°C or 50°C depending on frame size).
- **Drive overload (~10%)** The motor draws more current than the drive is rated for, either because the motor is too large or the mechanical load is excessive.
- **Poor enclosure ventilation (~7%)** The drive is mounted in a confined space with inadequate clearance (less than 10-15 mm around the unit) or no exhaust airflow.
- **High PWM switching frequency (~3%)** The drive is configured with an elevated switching frequency, increasing IGBT stress and heat generation beyond normal operating levels.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the cooling fan running when the drive is powered on?</summary>
<div class="dtree-body"><strong>Yes:</strong> Fan is working. Move on to checking for blocked airflow and dirty heatsink fins.<br><strong>No:</strong> Fan has failed or power is not reaching it. Replace the cooling fan assembly for your drive frame size.</div>
</details>

<details class="dtree"><summary>Are the heatsink fins clogged with dust or debris?</summary>
<div class="dtree-body"><strong>Yes:</strong> Clean the fins with compressed air or a soft brush and retest. Most A4A1 faults clear after cleaning.<br><strong>No:</strong> Check ambient temperature and verify the drive is not overloaded (motor current exceeds drive rating).</div>
</details>

<details class="dtree"><summary>Is the ambient temperature in the enclosure above 40°C (104°F)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Add enclosure ventilation, relocate the drive, or install an exhaust fan to bring ambient temperature down.<br><strong>No:</strong> Verify motor load current against drive rating using parameter 99.05 (Motor Nominal Current). If current is too high, reduce mechanical load or upsize the drive.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive completely** and lock out the supply breaker to eliminate shock hazard.
2. **Inspect the cooling fan** by manually spinning the blades to check for free movement and no obstructions.
3. **Clean the heatsink fins** using compressed air or a soft brush to remove dust, lint, and debris from all surfaces.
4. **Check ambient temperature** in the enclosure or room with a thermometer and compare to the drive's rated limit (consult your model's table for frame-specific limits).
5. **Verify clearance around the drive** is at least 10-15 mm on all sides to allow unobstructed airflow through the heatsink.
6. **Power up and monitor fan operation** by listening for the fan to spin and feeling for airflow exiting the drive.
7. **Check motor load current** in the drive's parameter menu (often parameter 31.xx or 99.05) and compare to the drive's rated output current to confirm the drive is not overloaded.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB ACS580 cooling fan assembly (frame-specific) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a4a1-fault-code&k=ABB+ACS580+cooling+fan+assembly+%28frame-specific%29&tag=errorcodefixes-20) \| Verify your drive frame size (R0-R9) before ordering; fan assemblies are not interchangeable between frames. |
| ABB ACS580 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a4a1-fault-code&k=ABB+ACS580+control+board&tag=errorcodefixes-20) \| Needed only in rare cases where the IGBT temperature estimation algorithm is corrupted; confirm with ABB tech support first. |

## When to Call a Pro

Call a qualified electrician or VFD technician if cleaning the heatsink and replacing the fan do not clear the A4A1 fault. The drive may have internal thermal degradation or a failing IGBT module that requires factory repair or replacement. If the drive is overloaded, a technician can verify motor parameters, check for mechanical binding, and recommend a properly sized replacement drive. High-voltage work on VFDs carries shock and arc-flash risk, so any troubleshooting beyond cleaning and visual inspection should be done by trained personnel with appropriate personal protective equipment.

**Rough cost:** A pro service call runs about $150-400 depending on parts and labor.
