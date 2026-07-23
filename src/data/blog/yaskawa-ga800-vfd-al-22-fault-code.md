---
title: "Yaskawa GA800 VFD AL-22 Fault - Causes & Fix"
description: "AL-22 signals a cooling-fan issue or overheat condition in the drive. Check cabinet ventilation and the internal fan operation first."
pubDatetime: 2026-07-21T07:44:35Z
modDatetime: 2026-07-21T07:44:35Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa GA800 cooling fan assembly"
most_likely_cause: "Blocked ventilation or dirty heatsink fins"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect cabinet intake and exhaust vents for dust, debris, or obstructions and clear any blockages"
  - "Verify the internal cooling fan spins freely and runs when the drive is powered; listen for unusual noise"
  - "Check ambient temperature around the drive cabinet to confirm it is within the manufacturer's rating"
part_price: "$80-150"
---

## Yaskawa GA800 VFD AL-22 Fault — What It Means

The AL-22 alarm on a Yaskawa GA800 variable frequency drive typically indicates a thermal protection event or cooling-system fault. The drive monitors internal temperatures and cooling-fan operation to protect power components from overheating. When the control logic detects insufficient cooling or elevated temperatures exceeding safe thresholds, it triggers AL-22 and may reduce output or stop operation to prevent damage.

This fault can appear after extended run times under load, when ambient temperatures are high, or when airflow through the cabinet is restricted. The drive's cooling fan must run at proper speed and the heatsink fins must remain clean for adequate thermal management. Consult your model's manual for the precise definition of AL-22, as alarm codes can vary between firmware revisions and drive configurations.

## Before You Replace Anything

Technicians sometimes replace the cooling fan when the real problem is a clogged heatsink or blocked cabinet vents. Clean all intake and exhaust openings and verify actual fan rotation before ordering a fan assembly.

[Jump to Fix](#fix)

## Common Causes

- **Blocked ventilation or dirty heatsink fins (~40%)** Dust and debris accumulate on heatsink surfaces and block airflow, reducing heat dissipation and triggering the thermal alarm.
- **Failed or slowing cooling fan (~30%)** The internal axial fan may fail due to bearing wear or electrical fault, preventing adequate airflow over the power components.
- **High ambient temperature (~15%)** Operating the drive in an enclosure with insufficient climate control or near heat-generating equipment raises internal temperatures beyond rated limits.
- **Overloading or excessive duty cycle (~10%)** Running the motor at or above nameplate current for extended periods generates excess heat in the drive's power stage.
- **Thermal sensor drift or failure (~5%)** The internal thermistor or temperature-sensing circuit may provide false readings, causing spurious alarms even when temperatures are safe.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the cooling fan spin when the drive is powered on and running?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fan is operating; proceed to clean the heatsink and check for airflow obstructions in the cabinet.<br><strong>No:</strong> The fan has likely failed or lost power; check fan wiring and replace the fan assembly if necessary.</div>
</details>

<details class="dtree"><summary>Are the heatsink fins visibly clogged with dust or lint?</summary>
<div class="dtree-body"><strong>Yes:</strong> Clean the heatsink thoroughly with compressed air or a soft brush, then reset the alarm and test.<br><strong>No:</strong> Check ambient temperature and verify the drive is not overloaded or cycling too frequently.</div>
</details>

<details class="dtree"><summary>Does the alarm clear after the drive cools down and you reset it?</summary>
<div class="dtree-body"><strong>Yes:</strong> The issue is thermal; improve ventilation, reduce load, or lower ambient temperature.<br><strong>No:</strong> A component fault (fan, sensor, or control board) is likely; call a technician for diagnostic testing.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** to the drive at the main breaker or disconnect switch and verify zero voltage with a multimeter before opening the enclosure.
2. **Remove the drive cover** or access panel following the manufacturer's instructions to expose the heatsink and cooling fan.
3. **Inspect the heatsink fins** for dust, lint, or grease buildup and clean thoroughly using compressed air or a vacuum with a soft brush attachment.
4. **Check the cooling fan** for free rotation by spinning the blades gently by hand and inspect the fan connector and wiring for loose or corroded terminals.
5. **Verify cabinet airflow** by examining intake filters, exhaust vents, and any ductwork for obstructions or damage, and clean or replace filters as needed.
6. **Measure ambient temperature** near the drive with a thermometer and compare it to the drive's rated operating range in the manual.
7. **Restore power and observe** the fan during startup; if it does not run or runs slowly, replace the fan assembly or contact a qualified technician for further diagnostics.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 cooling fan assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-22-fault-code&k=Yaskawa+GA800+cooling+fan+assembly&tag=errorcodefixes-20) \| Match the voltage and CFM rating to your drive frame size; consult the parts list in your manual. |
| Cabinet air filter (if applicable) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-22-fault-code&k=Cabinet+air+filter+%28if+applicable%29&tag=errorcodefixes-20) \| Replace any washable or disposable intake filters per the enclosure manufacturer's schedule. |

## When to Call a Pro

Call a qualified industrial electrician or drive technician if the alarm persists after cleaning and the fan appears to run normally, if you lack experience working inside high-voltage equipment, or if diagnostics point to a failed thermal sensor or internal control board. Working on VFDs requires knowledge of DC bus voltage, which can remain lethal even after input power is removed. A technician can perform temperature measurements, load testing, and component-level troubleshooting to isolate faults that are not obvious during visual inspection.

**Rough cost:** A pro service call runs about $200-500.
