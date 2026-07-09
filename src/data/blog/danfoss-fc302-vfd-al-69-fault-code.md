---
title: "Danfoss FC302 AL-69 - Causes & Fix"
description: "AL-69 means power card temperature is out of range. Most often blocked airflow or a failed cooling fan. Clean heatsink and filters first."
pubDatetime: 2026-06-22T10:22:08Z
modDatetime: 2026-06-22T10:22:08Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 cooling fan"
most_likely_cause: "Blocked airflow or clogged filters on the heatsink"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Clean all air filters and remove dust buildup on the heatsink and internal fins"
  - "Verify intake and exhaust vents are not blocked by debris or enclosures"
  - "Power cycle the drive (turn OFF, wait for displays to clear, then turn ON) to reset temporary glitches"
no_buy_pct: "60%"
---

## Danfoss FC302 AL-69 — What It Means

Alarm 69 on a Danfoss FC302 VFD indicates a power card temperature fault. The temperature sensor on the power card (also called the power board) has detected a value outside the safe operating range, either too hot or too cold. This is an alarm signaling that the drive's thermal protection system is active due to sensor data.

In the FC302 series, this sensor is physically located on the power card near the heatsink to monitor the temperature of the power electronics. The alarm can trigger if the drive is overheating due to blocked airflow, a failed cooling fan, or excessive ambient temperature. In rare cases it can also occur if the ambient temperature is extremely cold or if the sensor itself has failed.

## Before You Replace Anything

Technicians sometimes replace the power card before checking the cooling fan and cleaning the heatsink. Always verify the fan spins and airflow is clear before ordering a new power card.

[Jump to Fix](#fix)

## Common Causes

- **Blocked airflow or clogged filters (~40%)** Dust buildup on the heatsink, clogged air filters, or obstructed intake and exhaust vents prevent proper cooling of the power card.
- **Failed cooling fan (~30%)** The internal cooling fan is defective, not spinning, or spinning too slowly to move air across the heatsink.
- **High ambient temperature (~15%)** The environment surrounding the drive exceeds the specified limit (typically above 40°C or 104°F for standard units) or the drive is installed in an enclosed cabinet without adequate ventilation.
- **Failed temperature sensor (~10%)** The temperature sensor itself (thermistor or IC) is defective or has an open or short circuit.
- **Failed power card (~5%)** Internal malfunction of the power card circuitry causes incorrect temperature readings or actual overheating.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the cooling fan spin when the drive is powered on?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fan is working. Check for blocked vents and clean the heatsink of dust buildup.<br><strong>No:</strong> The fan is likely defective. Replace the cooling fan and check if the alarm clears.</div>
</details>

<details class="dtree"><summary>Is the drive installed in a hot environment or enclosed cabinet?</summary>
<div class="dtree-body"><strong>Yes:</strong> Improve ventilation around the drive or add external cooling to bring ambient temperature within spec.<br><strong>No:</strong> The problem is likely internal. Clean all filters and check the temperature sensor and power card.</div>
</details>

<details class="dtree"><summary>Does the alarm clear after a power cycle and cleaning?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was temporary due to dust or a thermal event. Monitor the drive for recurring alarms.<br><strong>No:</strong> The sensor or power card is likely faulty. Contact a qualified technician for advanced diagnostics.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Check ambient environment** around the drive and verify the surrounding temperature is within the manufacturer's specified operating range (consult your model's manual for specific limits).
2. **Inspect airflow and filters** by removing and cleaning any clogged air filters, checking for dust accumulation on the heatsink and internal fins, and verifying intake and exhaust vents are not blocked.
3. **Verify cooling fan operation** by powering the drive on (if safe) and observing if the fan spins, then power off and manually check if the fan spins freely without obstruction.
4. **Replace the cooling fan** immediately if the fan is defective, not spinning, or obstructed.
5. **Perform a power cycle** by turning the drive OFF, waiting for displays to clear, then turning ON, and use the Reset button on the keypad (LCP) followed by Auto On.
6. **Monitor temperature readings** through the drive display (if available) to see if the real-time temperature parameter remains out of range after cleaning and resetting.
7. **Disconnect the motor** and run the drive unloaded to rule out motor overload causing excessive heat, then check internal sensor continuity or replace the power card if the alarm persists despite verified airflow and fan operation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-69-fault-code&k=Danfoss+FC302+cooling+fan&tag=errorcodefixes-20) \| Match the voltage and part number to your specific FC302 model |
| Danfoss FC302 power card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-69-fault-code&k=Danfoss+FC302+power+card&tag=errorcodefixes-20) \| Only replace after verifying fan and airflow are correct |

## When to Call a Pro

Call a qualified technician if you are not comfortable working with variable frequency drives or high-voltage equipment. A professional should handle replacement of the power card, diagnostics of the temperature sensor, or any work that requires disassembly of the drive's internal components. If the alarm persists after cleaning filters and replacing the cooling fan, advanced diagnostics and testing of the power card are required. Professional service is also recommended if the drive is part of a critical industrial process where downtime must be minimized.

**Rough cost:** A pro service call runs about $150-400.

## See Also

- [Danfoss VFD Fault Codes — FC301, FC302, FC102 Reference](/posts/danfoss-vfd-fault-codes/)
- [Danfoss FC302 AL-83 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-83-fault-code/)
- [Danfoss FC302 Alarm 31 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-31-fault-code/)
- [Danfoss FC302 VFD Alarm 16 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-16-fault-code/)
