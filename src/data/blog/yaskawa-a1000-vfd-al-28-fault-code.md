---
title: "Yaskawa A1000 VFD AL-28 Fault - Causes & Fix"
description: "AL-28 is not a standard A1000 code. You may be seeing SC (output short circuit) or misreading the display. Check motor wiring first."
pubDatetime: 2026-06-29T10:47:00Z
modDatetime: 2026-06-29T10:47:00Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Three-phase AC motor"
most_likely_cause: "Shorted motor winding or damaged output cable"
likelihood: "the most common cause for SC faults"
diy_or_pro: "pro"
free_checks:
  - "Verify the exact fault code on the display and write it down character by character"
  - "Power off the drive, disconnect the motor cables from output terminals U, V, W and visually inspect for burnt or damaged insulation"
  - "Use a multimeter to test continuity between motor windings and between each phase and ground to identify a short"
---

## Yaskawa A1000 VFD AL-28 Fault — What It Means

The code AL-28 does not exist as a standard fault code in the official Yaskawa A1000 manual. You are likely misreading the display or confusing the drive model. The closest valid codes are SC (Output Short Circuit) or CPF28 (Control Circuit Error, found in P1000/U1000 series but not A1000). If the display shows SC, the drive detected a short circuit between output phases U, V, W or between a phase and ground, indicating damaged IGBTs or an external short in the motor or wiring. If the display shows CPF28 (not standard for A1000), it means the control board hardware is damaged and cannot process signals correctly. Verify the exact code on your display and consult your A1000 manual's fault code table to confirm the actual fault before proceeding with any repair.

## Before You Replace Anything

Technicians often replace the entire VFD when they see an output short fault, but the real problem is usually a shorted motor winding or damaged cable between the drive and motor. Isolate the motor and test continuity between phases and to ground before condemning the drive.

[Jump to Fix](#fix)

## Common Causes

- **Damaged motor windings or cable insulation (~50%)** A short circuit in the motor windings or in the power cable between the drive and motor causes the drive to detect an output short and shut down to protect the IGBTs.
- **Motor or cable grounded to enclosure (~25%)** A phase wire touching the motor frame, conduit, or earth ground creates a ground fault that triggers the output short circuit protection.
- **Internal IGBT failure in the drive (~15%)** A shorted insulated gate bipolar transistor inside the drive output stage causes the drive to detect a short circuit and may require drive replacement.
- **Loose or corroded output terminal connections (~5%)** Poor connections at the drive's U, V, W terminals can arc and create intermittent short circuits that trip the fault.
- **Control board hardware failure (if CPF28) (~5%)** If the display actually shows CPF28, the control board or terminal board connection has failed and the drive cannot detect drive unit signals or perform A/D conversion.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the display show exactly SC or does it show a different combination of letters and numbers?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is Output Short Circuit. Proceed to check motor and wiring for shorts or grounds.<br><strong>No:</strong> Write down the exact code and consult your A1000 manual's fault code table. The code AL-28 is not standard and may indicate a misread display or a different drive model.</div>
</details>

<details class="dtree"><summary>With the motor disconnected from the drive, does the fault clear when you power on the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem is in the motor or motor cable. Test the motor windings for shorts and grounds and inspect the cable for damage.<br><strong>No:</strong> The drive's internal output circuitry (IGBTs) is likely damaged. The drive will need professional repair or replacement.</div>
</details>

<details class="dtree"><summary>Does your multimeter show continuity (low resistance) between any motor phase and the motor frame or ground?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor winding is grounded. Repair or replace the motor.<br><strong>No:</strong> Test for shorts between motor phases (U to V, V to W, W to U). If no shorts are found, inspect the drive output terminals and internal components for damage.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Stop and disconnect power** to the drive and motor. Wait for the CHARGE indicator light to go off before touching any terminals.
2. **Write down the exact fault code** displayed on the VFD screen. Verify whether it shows SC, CPF28, or another code and consult your A1000 manual to confirm the fault meaning.
3. **Disconnect the motor cables** from the drive's output terminals U, V, and W. Inspect all wiring for damaged insulation, burnt spots, loose connections, or physical damage.
4. **Test the motor for shorts and grounds** using a multimeter set to continuity or low-resistance mode. Check between each phase pair (U-V, V-W, W-U) and between each phase and the motor frame or ground. Replace the motor if any winding is shorted or grounded.
5. **Inspect the power cable** between the drive and motor for cuts, abrasion, or burnt insulation. Replace any damaged cable.
6. **Power on the drive without the motor connected** (if the motor tests show a fault). If the fault clears, the motor or cable is the problem. If the fault persists, the drive's internal IGBTs are damaged.
7. **Check and reseat control board connections** (if the code is CPF28). Turn off power, open the drive enclosure, and verify the ribbon cable or terminal connections between the control board and drive unit board are firmly seated. Cycle power after reseating.
8. **Replace the drive or control board** if internal damage is confirmed. If the motor and wiring are good but the fault persists with no load, the drive hardware has failed and requires professional replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Three-phase AC motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-28-fault-code&k=Three-phase+AC+motor&tag=errorcodefixes-20) \| Required if motor windings are shorted or grounded. Match voltage, horsepower, and frame size to your application. |
| Shielded VFD-rated motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-28-fault-code&k=Shielded+VFD-rated+motor+cable&tag=errorcodefixes-20) \| Use only VFD-rated cable with proper shielding. Size according to motor current and cable length per NEC tables. |
| Yaskawa A1000 VFD replacement | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-28-fault-code&k=Yaskawa+A1000+VFD+replacement&tag=errorcodefixes-20) \| Required if internal IGBTs or control board are damaged. Match voltage and current rating to your motor and application. |

## When to Call a Pro

Call a professional if you are not comfortable working with high-voltage three-phase power or if you lack the proper test equipment to safely diagnose the drive and motor. A qualified electrician or VFD technician should handle all work inside the drive enclosure, any replacement of the drive unit, and verification that the DC bus voltage and output waveforms are within specification after repair. If the motor or cable is damaged and you are unsure of proper sizing or installation, a professional can make sure the replacement matches your application's voltage, horsepower, and duty cycle requirements. Professional service is also recommended if the drive is part of a critical industrial process where downtime or incorrect repairs could cause safety hazards or production loss.

**Rough cost:** A pro service call runs about $200-600 depending on whether motor or drive requires replacement.

## See Also

- [Yaskawa GA800 E12 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e12-fault-code/)
- [Yaskawa GA800 E18 Fault Code - Causes & Fix](/posts/yaskawa-ga800-vfd-e18-fault-code/)
- [Yaskawa GA800 E30 Fault Code - Causes & Fix](/posts/yaskawa-ga800-vfd-e30-fault-code/)
- [Yaskawa GA800 CPF24 - Causes & Fix](/posts/yaskawa-ga800-vfd-f024-fault-code/)
