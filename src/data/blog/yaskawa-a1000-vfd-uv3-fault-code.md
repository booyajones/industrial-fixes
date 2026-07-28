---
title: "Yaskawa A1000 Uv3 Fault - Causes & Fix"
description: "Uv3 on a Yaskawa A1000 means the soft-charge bypass relay has failed. Most often the drive needs an internal power board or full replacement."
pubDatetime: 2026-06-12T10:08:00Z
modDatetime: 2026-06-12T10:08:00Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa A1000 power board assembly"
most_likely_cause: "Soft-charge bypass relay or contactor failure inside the drive"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power down the drive completely and allow the DC bus to discharge for at least five minutes, then power it back up to see if the fault clears on its own."
  - "Check drive monitor parameter U4-06 (relay life). If the value is above 90%, the soft-charge relay is at end of life and the drive needs replacement or a new power board."
---

## What this code means
Uv3 on a Yaskawa A1000 is an Undervoltage 3 / Soft-Charge Circuit Fault. The drive has detected a problem in the internal precharge or inrush-prevention bypass path. When you first apply power to a VFD, a resistor limits the surge of current into the DC bus capacitors. After a few milliseconds, a relay or contactor closes to bypass that resistor and allow normal current flow. Uv3 means that relay has failed to close, the bypass circuit is damaged, or the relay contacts are worn out.

This is an internal drive power-stage fault, not a motor overload or a field wiring issue. In most cases, the soft-charge relay itself cannot be serviced as a standalone part in the field. The practical repair is replacement of the control board, the power board assembly, or the entire drive, depending on the severity and age of the unit.

## Before You Replace Anything

Technicians sometimes suspect incoming line voltage or a tripped breaker because the fault name includes 'undervoltage,' but Uv3 is almost always an internal relay or power-board fault. Check the drive's relay-life monitor U4-06 before ordering external line conditioners or transformers.

## Common Causes

- **Soft-charge bypass relay failure (~60%)** The internal contactor that bypasses the inrush-limiting resistor has failed to close or its contacts are worn out, preventing the DC bus from reaching normal voltage.
- **Precharge resistor or bypass circuit damage (~20%)** The resistor or circuit board traces in the soft-charge path are open, shorted, or overheated, blocking the relay from completing its function.
- **Heat or contamination on the power board (~10%)** Dust, moisture, or prolonged high ambient temperature has degraded solder joints, relay coil insulation, or circuit-board connections around the soft-charge assembly.
- **Aging power section at end of service life (~10%)** The drive has accumulated high operating hours and the relay-life monitor shows 90% or more, indicating the entire power stage is worn and should be replaced.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the Uv3 fault clear immediately after a full power-down and restart?</summary>
<div class="dtree-body"><strong>Yes:</strong> The relay may have been stuck temporarily. Log the event and monitor for recurrence. If it happens again within a few weeks, plan for replacement.<br><strong>No:</strong> The fault is persistent. Check the relay-life monitor and prepare to replace the power board or drive.</div>
</details>

<details class="dtree"><summary>Is drive monitor U4-06 (relay life) above 90%?</summary>
<div class="dtree-body"><strong>Yes:</strong> The soft-charge relay is at end of life. Replace the control board, power board, or the entire drive depending on your model and parts availability.<br><strong>No:</strong> The fault is likely a component failure rather than wear. Inspect the power board for visible damage, overheated parts, or loose connections.</div>
</details>

<details class="dtree"><summary>Do you see incoming line voltage at the correct level on the drive's input terminals when the fault occurs?</summary>
<div class="dtree-body"><strong>Yes:</strong> Line voltage is good, so Uv3 is an internal fault. Do not order line conditioners or transformers. Focus on the soft-charge circuit inside the drive.<br><strong>No:</strong> Correct any line-voltage issues first, but remember Uv3 is almost always internal. If the fault persists after line voltage is stable, the relay or power board is still the root cause.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Lock out and tag out the drive**, remove all power, and wait at least five minutes for the DC bus capacitors to discharge completely before opening the enclosure or touching any internal parts.
2. **Power the drive back on** and observe whether the Uv3 fault appears immediately or after a few seconds. If it clears and does not return, log the event and monitor over the next few days.
3. **Check drive monitor parameter U4-06** (relay life) in the keypad menu. A value above 90% indicates the soft-charge relay is at end of life and the drive should be replaced or the power board swapped.
4. **Verify incoming line voltage** at the drive input terminals using a true-RMS multimeter. Uv3 is usually not caused by low line voltage, but you want to rule out external issues before condemning the drive.
5. **Remove the front cover and inspect the power board** for visible signs of overheating, burned components, loose connectors, dust buildup, or moisture. Pay special attention to the relay or contactor area near the DC bus capacitors.
6. **If the fault persists and U4-06 is high or the power board shows damage**, order a replacement power board assembly or a new drive. The soft-charge relay is typically not sold as a standalone field part.
7. **Install the new power board or drive**, verify all connections match the original wiring diagram, restore power, and confirm the Uv3 fault is gone and the drive runs normally under load.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa A1000 power board assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-uv3-fault-code&k=Yaskawa+A1000+power+board+assembly&tag=errorcodefixes-20) \| Match your drive's horsepower and voltage rating. The soft-charge relay is integrated into this board. |
| Yaskawa A1000 complete drive replacement | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-uv3-fault-code&k=Yaskawa+A1000+complete+drive+replacement&tag=errorcodefixes-20) \| Often more cost-effective than a power board if the drive is older or if lead time for the board is long. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician immediately. Uv3 is an internal power-stage fault that requires working inside a high-voltage variable-frequency drive. The DC bus can hold lethal voltage even after input power is removed. Incorrect handling can destroy the new power board, create an arc-flash hazard, or leave the drive in an unsafe state. A technician will safely discharge the bus, verify the relay-life monitor, inspect the power board under proper lockout, and install the correct replacement board or drive for your horsepower and voltage. If your facility does not have a qualified drive repair shop on staff, contact a Yaskawa authorized service center or an experienced motor-control integrator.

**Rough cost:** A pro service call runs about $800-2500 for power board replacement or complete drive swap, 1-3 hours labor.
