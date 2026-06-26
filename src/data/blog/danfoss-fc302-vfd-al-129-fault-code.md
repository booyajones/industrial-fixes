---
title: "Danfoss FC302 AL-129 Fault - Causes & Fix"
description: "AL-129 does not exist in FC302 logs. You likely see Alarm 29 (heat sink overtemp). Most common fix: clean heatsink and replace cooling fan."
pubDatetime: 2026-06-24T10:24:53Z
modDatetime: 2026-06-24T10:24:53Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 cooling fan assembly"
most_likely_cause: "failed or blocked cooling fan"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power down and visually inspect the heatsink fins for dust, metal chips, or blockage"
  - "Check that the internal cooling fan spins freely by hand when the drive is off"
  - "Measure the ambient temperature in the cabinet to confirm it is below 45°C"
part_price: "$25-60 for a replacement cooling fan assembly"
no_buy_pct: "40%"
---

## Danfoss FC302 AL-129 Fault — What It Means

The code AL-129 does not appear in the Danfoss FC302 error catalog. You are probably seeing Alarm 29 (also labeled Error 36), which is a drive overtemperature fault. This alarm trips when the power board heatsink reaches 90 to 95°C, forcing the drive into Trip A state to protect the IGBT modules from thermal damage. The drive stops motor operation immediately to prevent destroying the inverter semiconductors.

If your display shows a different pattern or if 129 refers to a parameter number rather than an alarm, consult your drive's manual. The steps below assume Alarm 29 overtemperature, which is the fault technicians encounter when a three-digit code in the 29 or 129 range appears on FC302 units.

## Before You Replace Anything

Technicians often replace the inverter board or IGBT modules first. Before swapping electronics, clean the heatsink and verify the cooling fan spins freely under power. A $30 fan fix solves most overtemperature trips.

[Jump to Fix](#fix)

## Common Causes

- **Failed or blocked cooling fan (~45%)** The internal fan is dead, jammed, or obstructed by debris so the heatsink cannot shed heat.
- **Clogged heatsink fins (~25%)** Dust and metal particles accumulate on the heatsink, insulating it and preventing airflow from cooling the IGBTs.
- **High ambient temperature (~15%)** The enclosure or room temperature exceeds the drive's continuous rating of 40 to 45°C, overwhelming the cooling system.
- **Overloaded drive operation (~10%)** The motor load exceeds the drive's continuous current rating for extended periods, causing IGBT heating beyond the cooling capacity.
- **Shorted IGBT module (~5%)** A failing inverter IGBT generates excessive internal heat even at low loads, triggering the thermal trip.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the cooling fan spin when the drive powers on?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fan works. Proceed to clean the heatsink and check ambient temperature.<br><strong>No:</strong> Fan is faulty or obstructed. Replace the fan assembly or clear any debris blocking the impeller.</div>
</details>

<details class="dtree"><summary>Does the alarm trip immediately at startup with no motor load?</summary>
<div class="dtree-body"><strong>Yes:</strong> Likely a shorted IGBT or a stuck heatsink sensor. Test the inverter board diodes or replace the power stack.<br><strong>No:</strong> The fault occurs under load. Check for motor overload, high ambient temp, or insufficient ventilation in the enclosure.</div>
</details>

<details class="dtree"><summary>Is the enclosure ambient temperature above 40°C?</summary>
<div class="dtree-body"><strong>Yes:</strong> Add forced ventilation or move the drive to a cooler location. The drive cannot operate continuously above its rated ambient limit.<br><strong>No:</strong> Temperature is within spec. Focus on cleaning, fan replacement, or checking for IGBT faults.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** from AC mains and DC-link circuits, then wait for the capacitors to discharge per the manual's safety table before opening the enclosure.
2. **Inspect the cooling fan** visually and by hand rotation to confirm it spins freely and is not jammed by debris or bearing failure.
3. **Clean the heatsink fins** with compressed air or a soft brush, removing all dust, metal chips, and contamination that block airflow paths.
4. **Measure ambient temperature** inside the cabinet using a thermometer to verify it stays below 45°C during operation.
5. **Power up the drive** and observe the fan. If it does not spin or runs intermittently, replace the fan assembly immediately.
6. **Check input voltage balance** across all three phases. Imbalance greater than 3 percent can contribute to uneven heating and thermal trips.
7. **Test IGBT modules** using a multimeter in diode mode if the alarm persists at no load. A shorted IGBT shows near zero ohms between collector and emitter. Replace the inverter board or power stack if any IGBT is shorted.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 cooling fan assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-129-fault-code&k=Danfoss+FC302+cooling+fan+assembly&tag=errorcodefixes-20) \| Match the voltage rating (typically 24V DC or 230V AC) and CFM to your drive frame size. |
| Danfoss FC302 inverter board or power stack | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-129-fault-code&k=Danfoss+FC302+inverter+board+or+power+stack&tag=errorcodefixes-20) \| Required only if IGBT modules test shorted. Verify the exact board part number from your drive nameplate. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician if you lack the tools to safely discharge high-voltage capacitors, if IGBT testing shows a short requiring board replacement, or if the alarm returns after cleaning and fan replacement. High-voltage DC-link circuits and IGBT modules require proper test equipment and lock-out procedures. A technician will also verify input power quality, check for phase imbalance, update drive firmware if needed, and recommend cabinet ventilation upgrades when ambient conditions exceed the drive's continuous rating.

**Rough cost:** A pro service call runs about $150-400 for cleaning, fan replacement, and cabinet ventilation improvements.
