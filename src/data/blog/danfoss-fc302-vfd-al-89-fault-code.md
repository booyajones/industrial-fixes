---
title: "Danfoss FC302 AL-89 Fault - Causes & Fix"
description: "AL-89 means Internal Fan Fault: the drive's cooling fan is not spinning or is blocked. Most often a failed fan or dust buildup."
pubDatetime: 2026-06-23T10:09:00Z
modDatetime: 2026-06-23T10:09:00Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 internal cooling fan"
most_likely_cause: "Failed internal cooling fan"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power-cycle the drive (turn off mains, wait five minutes, power back on) to see if the alarm clears temporarily."
  - "Open the enclosure and inspect all fans for dust, debris, or blockage on the heatsink fins."
  - "Verify the fan connector is fully seated on the control card."
part_price: "$40-80"
no_buy_pct: "30%"
---

## What this code means
AL-89 is an Internal Fan Fault on the Danfoss FC302 VFD. The drive has detected that one or more cooling fans are not spinning, are blocked, or have failed electrically. These fans are critical for keeping the power stage and IGBTs cool during operation. If the alarm is ignored, the drive will overheat and may shut down or sustain permanent damage to its components.

The fault is typically triggered by a fan motor that has burned out, heavy dust accumulation on the heatsink or fan blades, a loose wire between the control card and the fan, or ambient temperature exceeding the drive's rating. The drive monitors fan speed or supply voltage, and when it falls outside normal range the AL-89 alarm is posted.

## Before You Replace Anything

Technicians sometimes replace the entire control board when the fault is only a dead fan or a loose fan connector. Always measure voltage at the fan terminals and test fan resistance before ordering a control card.

## Common Causes

- **Failed fan motor (~40%)** The internal cooling fan has burned out or its windings are open, preventing rotation even when voltage is present.
- **Blocked airflow (~25%)** Dust, metal chips, or debris on the heatsink fins or fan blades stops the fan from spinning or reduces airflow below the drive's monitoring threshold.
- **Loose or broken fan wiring (~15%)** The cable or connector between the control card and the fan has come loose, corroded, or broken, cutting power to the fan.
- **High ambient temperature (~10%)** The drive is installed in an enclosed cabinet or hot environment, causing the fan to run continuously and overheat, or ambient temperature exceeds the drive's 50 °C limit.
- **Fan power supply issue (~10%)** The 24 VDC supply on the control board that powers the fan is unstable or absent due to a failed component on the board.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>When you power the drive on, do you hear or see any fans spinning inside?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fan may be spinning but not fast enough, or the drive's fan-speed sensor is faulty. Check for dust buildup and verify ambient temperature is below 50 °C.<br><strong>No:</strong> The fan is either dead, unplugged, or not receiving voltage. Proceed to measure voltage at the fan terminals and test fan resistance.</div>
</details>

<details class="dtree"><summary>Is there heavy dust or debris visible on the heatsink or fan blades?</summary>
<div class="dtree-body"><strong>Yes:</strong> Clean the heatsink and fan with compressed air, then power-cycle the drive. If AL-89 clears, the blockage was the problem.<br><strong>No:</strong> The fan motor or fan wiring is likely the issue. Test voltage and continuity as described in the steps below.</div>
</details>

<details class="dtree"><summary>When you measure voltage at the fan connector, do you read approximately 24 VDC?</summary>
<div class="dtree-body"><strong>Yes:</strong> Voltage is present but the fan is not running, so the fan motor itself is failed. Replace the fan.<br><strong>No:</strong> No voltage means either a loose connector or a failed 24 VDC supply on the control card. Re-seat the connector first, then test the control board if the fault persists.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off AC mains** and wait at least five minutes for capacitors to discharge, then power the drive back on. If AL-89 clears temporarily, the fault may be intermittent or thermal-related.
2. **Open the drive enclosure** and locate all internal cooling fans. On the FC302 there is typically at least one axial fan mounted on or near the heatsink assembly.
3. **Inspect for dust and blockage** on the heatsink fins and fan blades. Use compressed air to blow out any accumulated dust, metal chips, or debris. Clean the filter screens if the drive has them.
4. **Check fan wiring and connectors** on the control card. Verify that the fan cable is fully seated and shows no signs of damage, corrosion, or broken strands.
5. **Measure voltage at the fan terminals** with the drive powered on. The FC302 internal fans run on 24 VDC. If voltage is absent, re-seat the connector. If still absent, the control board's 24 VDC supply circuit may be faulty.
6. **Test fan resistance** by disconnecting the fan and measuring across its motor terminals with a multimeter. A healthy fan typically shows 10 to 50 Ω. If the reading is infinite (open circuit) or near zero, the fan motor is failed.
7. **Replace the fan** if voltage is present but the fan does not spin, or if resistance is out of range. If the fan is good but no voltage is present at the connector, replace or repair the control board.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 internal cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-89-fault-code&k=Danfoss+FC302+internal+cooling+fan&tag=errorcodefixes-20) \| Confirm the exact fan model and voltage (24 VDC) from the drive nameplate or service manual before ordering. |
| Danfoss FC302 control PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-89-fault-code&k=Danfoss+FC302+control+PCB&tag=errorcodefixes-20) \| Only required if the 24 VDC supply to the fan is absent and the fan itself tests good. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician for AL-89 faults. Working inside a variable-frequency drive requires understanding of high-voltage DC bus capacitors, which can hold lethal charge even after AC power is removed. The technician will use a voltmeter to verify safe discharge, test the fan supply, and replace the fan or control board as needed. If your facility does not have personnel trained on VFD servicing, hire a local automation or motor-control shop rather than attempting the repair yourself.

**Rough cost:** A pro service call runs about $150-400.
