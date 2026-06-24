---
title: "Danfoss FC302 AL-65 Fault - Causes & Fix"
description: "AL-65 means Control Card Over Temperature on the Danfoss FC302 VFD. Most common fix: clean blocked vents and check cooling fan."
pubDatetime: 2026-06-22T10:18:50Z
modDatetime: 2026-06-22T10:18:50Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss VFD internal cooling fan"
most_likely_cause: "Blocked airflow or dirty cooling vents"
likelihood: "the most frequent cause"
diy_or_pro: "diy"
free_checks:
  - "Inspect and clean all intake and exhaust vents for dust, debris, or obstructions blocking airflow to the control card"
  - "Measure ambient temperature around the drive to confirm it is below the rated operating limit (typically 40°C continuous)"
  - "Power on the drive and listen for the internal cooling fan to spin up audibly and continuously"
part_price: "$18-45"
no_buy_pct: "60%"
---

## Danfoss FC302 AL-65 Fault — What It Means

Alarm 65 on a Danfoss FC302 VFD indicates Control Card Over Temperature. The temperature of the drive's control card (logic board) has exceeded its upper safety limit, triggering a trip to protect the electronics from damage. This is distinct from main power heatsink or motor overheat faults. The control card has a thermal sensor that monitors internal temperature and shuts down the drive when the cutout threshold is exceeded.

The fault typically places the drive in a Trip state with red and yellow LEDs illuminated. Danfoss groups Alarm 65 with other thermal alarms (29 and 66) and specifically recommends checking for airflow obstructions as a primary diagnostic step. The fault can result from environmental conditions, mechanical cooling failure, or component-level issues on the control card itself.

## Before You Replace Anything

Technicians often replace the control card immediately without checking the cooling fan and airflow path. Test the fan and clean all vents first, as a failed or obstructed fan is often the root cause while the control card itself is still good.

[Jump to Fix](#fix)

## Common Causes

- **Blocked airflow or dirty filters (~40%)** Dust, debris, or physical obstructions block the cooling vents or fan intake, preventing air from reaching the control card and causing temperature buildup.
- **Failed cooling fan (~30%)** The internal fan that cools the control card has stopped working or is running at reduced speed, eliminating active cooling for the logic board.
- **High ambient temperature (~15%)** The surrounding environment exceeds the drive's rated operating temperature (typically above 40°C or 50°C depending on model and cooling class).
- **Defective control card thermal sensor (~10%)** The temperature sensor on the control card is faulty and reports a false over-temperature condition even when the card is cool.
- **Control card internal fault (~5%)** An internal component failure on the control card causes excessive power dissipation and genuine heat generation, triggering the thermal cutout.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Can you feel warm or hot air coming from the drive's exhaust vent?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fan is working but airflow may be restricted. Clean all intake and exhaust vents thoroughly and verify ambient temperature is below 40°C.<br><strong>No:</strong> The cooling fan has likely failed or the intake is completely blocked. Check for obstructions and test the fan by powering on the drive and listening for fan noise.</div>
</details>

<details class="dtree"><summary>Does the cooling fan spin immediately and audibly when you power on the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fan is working. Check ambient temperature and inspect the control card for visible damage or component failures. The thermal sensor or card may be defective.<br><strong>No:</strong> The cooling fan has failed. Replace the internal cooling fan and reset the drive. If the fault persists after fan replacement, suspect the control card.</div>
</details>

<details class="dtree"><summary>Does the fault clear after cleaning vents and running the drive in a cooler location?</summary>
<div class="dtree-body"><strong>Yes:</strong> The issue was environmental (poor airflow or high ambient temperature). Improve ventilation and maintain clean filters to prevent recurrence.<br><strong>No:</strong> The fault is internal to the drive. Test the cooling fan operation and consider replacing the control card if the fan is confirmed working and vents are clear.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** to the drive and wait for all LEDs and the cooling fan to stop completely.
2. **Inspect all vents** on the drive enclosure for dust, debris, or obstructions. Use compressed air or a vacuum to clean intake and exhaust openings thoroughly.
3. **Measure ambient temperature** near the drive using a thermometer. Confirm it is below the drive's rated limit (consult your model's specification table, typically 40°C continuous or 50°C reduced duty).
4. **Power on the drive** (without connecting a load) and immediately listen for the internal cooling fan. The fan should spin up audibly within seconds. If silent or making grinding noises, the fan has failed.
5. **Test fan operation** by feeling for airflow at the exhaust vent while the drive is powered. If no airflow is present despite fan noise, the fan may be mechanically jammed or the ductwork blocked.
6. **Replace the cooling fan** if it does not operate correctly. Remove the drive cover, disconnect the fan power connector, install a new fan (match voltage and size), and reassemble.
7. **Reset the alarm** by pressing the Reset key on the drive keypad. If the drive shows a Trip Lock (red and yellow LEDs both on), disconnect all power for 30 seconds before reconnecting and resetting.
8. **Monitor under load** after clearing the fault. Run the drive with a typical load and observe for 20-30 minutes. If Alarm 65 returns quickly, suspect a defective control card or thermal sensor and consider card replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss VFD internal cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-65-fault-code&k=Danfoss+VFD+internal+cooling+fan&tag=errorcodefixes-20) \| Match the voltage (typically 12V or 24V DC) and physical dimensions to the original fan; consult the drive model nameplate or service manual for exact specifications. |
| Danfoss FC302 control card (logic board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-65-fault-code&k=Danfoss+FC302+control+card+%28logic+board%29&tag=errorcodefixes-20) \| Replace if the thermal sensor is faulty or internal circuitry is damaged; verify the card part number matches your specific FC302 model and firmware revision. |

## When to Call a Pro

Call a qualified industrial controls technician if you are uncomfortable working inside the VFD enclosure, if the fault persists after replacing the cooling fan and cleaning all vents, or if you need to replace the control card and transfer parameter settings. A professional can safely test the control card thermal sensor, verify internal power supply voltages, and perform a controlled card swap while preserving your drive configuration. Also call a pro if the drive is part of a critical process system where downtime must be minimized or if the fault returns immediately after reset, suggesting a more complex internal failure that requires specialized diagnostic equipment.

**Rough cost:** DIY runs about $15-50 in parts (fan or filters), 20-45 min. A pro service call runs about $120-280 service call.
