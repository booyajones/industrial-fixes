---
title: "Danfoss FC302 W66 - Causes & Fix"
description: "W66 means heat sink temperature too low (below 0°C). Most often a failed Power Card sensor circuit. Replace the Power Card or preheat."
pubDatetime: 2026-06-22T10:19:49Z
modDatetime: 2026-06-22T10:19:49Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 Power Card (Power PCB / I/O Card)"
most_likely_cause: "Power Card sensor detection circuit failure"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Check ambient temperature around the drive cabinet and verify it is above the minimum rating (consult your model's table, typically -10°C to -20°C minimum)"
  - "Inspect sensor wiring connections on the IGBT module for corrosion or loose terminals"
  - "Set Parameter 2-00 (DC Hold/Preheat Current) to 5% and Parameter 1-80 (Function at Stop) to enable trickle current, then restart to see if the warning clears"
---

## Danfoss FC302 W66 — What It Means

Warning 66 (W66) on the Danfoss FC302 VFD indicates 'Heat Sink Temperature Low.' The temperature sensor inside the IGBT module reports the heat sink is below the safe operating threshold (typically below 0°C or the manufacturer's minimum). The drive will not start to prevent thermal stress or condensation damage. The FC-302 software will display the temperature as 0 degrees or a negative value when this fault is active.

This warning is triggered by either a genuine cold environment (installation in freezing conditions without preheating) or a failure in the sensor circuit. The sensor is integrated into the IGBT module, and its signal is read by the Power Card. When the card or sensor fails, the drive interprets the fault as a dangerously low temperature even if the ambient environment is warm.

## Before You Replace Anything

Technicians sometimes replace the entire IGBT module when only the Power Card (which reads the sensor signal) is defective. Test sensor resistance and swap the Power Card first before condemning the IGBT module.

[Jump to Fix](#fix)

## Common Causes

- **Power Card sensor detection circuit failure (~50%)** The analog input circuit on the Power Card that reads the IGBT module temperature sensor signal is damaged or has corroded traces, causing a false low-temperature reading even when the heat sink is warm.
- **IGBT module temperature sensor failure (~25%)** The integrated sensor inside the IGBT module is open-circuit (infinite resistance) or shorted, sending an invalid signal to the Power Card and triggering the low-temperature warning.
- **Excessive ambient cold environment (~15%)** The drive is installed in a location where the actual temperature is below the minimum operating rating (typically -10°C to -20°C) without preheating, causing a legitimate low heat sink temperature.
- **Cooling fan contamination causing board corrosion (~10%)** Oil stains or other contaminants on the cooling fan have migrated to the circuit board, corroding the sensor detection circuit on the Power Card and causing faulty temperature readings.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the ambient temperature around the drive below freezing or very cold (below 0°C)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is likely genuine. Increase the ambient temperature or set Parameter 2-00 to 5% to enable preheat current before starting the drive.<br><strong>No:</strong> The environment is warm, so the sensor or detection circuit is faulty. Proceed to test the sensor resistance and Power Card.</div>
</details>

<details class="dtree"><summary>Does the drive display show the heat sink temperature as 0 degrees or a negative value?</summary>
<div class="dtree-body"><strong>Yes:</strong> This confirms the sensor circuit is reading an invalid low temperature. Test the sensor resistance and swap the Power Card.<br><strong>No:</strong> The temperature reading is normal. The warning may be intermittent or a different issue. Monitor the drive and check wiring connections.</div>
</details>

<details class="dtree"><summary>After swapping the Power Card with a known-good unit, does the W66 warning clear?</summary>
<div class="dtree-body"><strong>Yes:</strong> The original Power Card was defective. Replace it and reassemble the drive.<br><strong>No:</strong> The IGBT module sensor is likely failed. Replace the IGBT module or contact a qualified technician.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the VFD** and lock out the main power source. Wait for the DC bus capacitors to discharge (at least five minutes) before opening the enclosure.
2. **Verify the ambient temperature** around the drive. If it is below the minimum operating rating (consult your model's specifications, typically -10°C to -20°C), increase the temperature or move the drive to a warmer location.
3. **Inspect the sensor wiring** on the IGBT module. Look for loose connections, corrosion, or damaged wires at the sensor terminals. Clean or tighten as needed.
4. **Test the temperature sensor resistance** by isolating the sensor leads on the IGBT module and measuring with a multimeter. If the resistance is infinite (open) or near zero (shorted), the sensor inside the IGBT module is defective.
5. **Swap the Power Card** if the sensor resistance is normal. Replace the Power Card with a known-good unit and check if the warning clears. The Power Card contains the detection circuit that reads the sensor signal.
6. **Enable preheat current** if the environment cannot be warmed. Set Parameter 2-00 (DC Hold/Preheat Current) to 5% and Parameter 1-80 (Function at Stop) to apply trickle current when the motor stops, keeping the heat sink above the minimum threshold.
7. **Reassemble the drive** (Power Card, bottom plate, side plate, Control Card, upper cover, LCP) and perform a diode check and ground insulation test before powering on. Clear the fault history and run the drive under load to confirm the warning does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 Power Card (Power PCB / I/O Card) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-66-fault-code&k=Danfoss+FC302+Power+Card+%28Power+PCB+%2F+I%2FO+Card%29&tag=errorcodefixes-20) \| Contains the sensor detection circuit. Most common replacement for W66. |
| Danfoss FC302 IGBT Module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-66-fault-code&k=Danfoss+FC302+IGBT+Module&tag=errorcodefixes-20) \| Replace if the integrated temperature sensor inside the module is physically damaged or open-circuit. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician for W66 repairs. This fault requires high-voltage lockout, DC bus discharge procedures, component-level testing of the Power Card and IGBT module, and careful reassembly with insulation verification. Mistakes can destroy expensive power electronics or create shock hazards. If you are not trained in VFD service or do not have the proper test equipment (multimeter, insulation tester), do not attempt this repair. A pro can also adjust preheat parameters correctly and test the drive under full load to confirm the fix.

**Rough cost:** A pro service call runs about $300-800.
