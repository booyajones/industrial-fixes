---
title: "Danfoss FC302 AL-164 - Causes & Fix"
description: "AL-164 is not a valid FC302 fault code. Check your display again-you likely have Alarm 13 (overcurrent) or Alarm 16 (DC undervoltage)."
pubDatetime: 2026-06-26T09:55:29Z
modDatetime: 2026-06-26T09:55:29Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 IGBT module or power board"
most_likely_cause: "Misread alarm number or confusion with sub-code"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Re-read the display carefully and write down the exact alarm number and any sub-code in parameter 15-32."
  - "Power down, wait for capacitor discharge (consult your model's table), then visually inspect all motor cable connections for looseness or corrosion."
  - "Disconnect the motor leads from the drive and run the drive unloaded to see if the alarm clears."
---

## Danfoss FC302 AL-164 — What It Means

The code AL-164 does not exist in the Danfoss FC302 alarm list. Valid FC302 alarms typically range from Alarm 1 through Alarm 39 for standard faults, or Alarm 5376–65535 for internal faults with specific sub-codes displayed in parameter 15-32. You may be misreading the display or confusing the alarm number with a sub-code inside an internal fault parameter. Common alarms that technicians mistake for AL-164 include Alarm 13 (Overcurrent), which triggers when the drive output current exceeds the peak limit due to a motor short or load spike, and Alarm 16 (DC Undervoltage), which appears when the DC bus voltage drops below the minimum threshold (around 200V). If your display shows a three-digit number preceded by "AL," double-check the exact digits and consult the alarm list in your FC302 manual.

If you are actually seeing Alarm 13, the drive has detected excessive output current to the motor. This is the most common severe fault on the FC302 and usually points to a shorted motor winding, a sudden mechanical overload, loose cable connections, or a failed IGBT module inside the drive. If the alarm is Alarm 16, the drive's DC link voltage fell too low, often caused by a blown input fuse, failed rectifier, or unstable incoming AC supply. Before attempting any repair, verify the exact alarm number and record any sub-code displayed in parameter 15-32, as that will guide your troubleshooting.

## Before You Replace Anything

Technicians sometimes replace the entire drive when the fault is actually a shorted motor or loose cable. Always disconnect the motor and run the drive unloaded to isolate whether the problem is internal or external.

[Jump to Fix](#fix)

## Common Causes

- **Misread or incorrect alarm number (~40%)** AL-164 does not exist in the FC302 alarm list, so the display may show Alarm 13, 16, or 38 instead.
- **Motor winding short (if Alarm 13) (~25%)** A partial or total short in the motor windings creates excessive current draw and triggers an overcurrent fault.
- **Loose or corroded motor cable connections (if Alarm 13) (~15%)** Poor contact between the drive and motor creates resistance spikes that the drive reads as overcurrent.
- **Failed IGBT module (if Alarm 13) (~10%)** Aging or damaged IGBT modules inside the drive can no longer regulate current properly and trigger false overcurrent alarms.
- **Blown input fuse or failed rectifier (if Alarm 16) (~10%)** A blown input fuse or failed rectifier assembly causes the DC bus voltage to drop below the minimum threshold.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the display actually show AL-164, or could it be AL-13 or AL-16?</summary>
<div class="dtree-body"><strong>Yes:</strong> Write down the exact number and sub-code (parameter 15-32), then consult the alarm list in your FC302 manual to confirm the real fault.<br><strong>No:</strong> If you are certain the display shows AL-164, the drive may have a display fault or corrupted firmware-call a Danfoss service technician.</div>
</details>

<details class="dtree"><summary>Does the alarm clear when you disconnect the motor and run the drive unloaded?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is in the motor or cable-test motor insulation with a megohm meter (readings below 2 megohms indicate a problem) and inspect all cable connections.<br><strong>No:</strong> The fault is internal to the drive-the IGBT module, power board, or rectifier has likely failed and requires professional repair or board replacement.</div>
</details>

<details class="dtree"><summary>Are all three input phases present and balanced (measured with a voltmeter)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The incoming power is good, so focus on the motor circuit and internal drive components.<br><strong>No:</strong> Check for blown input fuses, tripped breakers, or a failed rectifier assembly before troubleshooting downstream.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down and disconnect** the drive from AC mains, then wait for capacitor discharge (consult your model's discharge-time table in the manual).
2. **Re-read the display** carefully and write down the exact alarm number and any sub-code shown in parameter 15-32.
3. **Consult the alarm list** in your FC302 manual to identify the correct fault (most likely Alarm 13, 16, or 38).
4. **Disconnect the motor leads** from the drive output terminals (U, V, W) and run the drive unloaded to see if the alarm persists.
5. **If the alarm clears**, test the motor insulation using a megohm meter (readings below 2 megohms indicate a short or insulation failure), and inspect all motor cable connections for looseness or corrosion.
6. **If the alarm persists** with the motor disconnected, the drive has an internal component failure (IGBT, power board, or rectifier)—stop operation and arrange for professional repair or board replacement.
7. **Check input power** by measuring all three phases with a voltmeter and inspecting input fuses for signs of failure or imbalance.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 IGBT module or power board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-164-fault-code&k=Danfoss+FC302+IGBT+module+or+power+board&tag=errorcodefixes-20) \| Model-specific; requires exact drive rating and serial number to order. |
| Input fuse set for FC302 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-164-fault-code&k=Input+fuse+set+for+FC302&tag=errorcodefixes-20) \| Check your model's fuse rating table; typically fast-acting fuses rated for the drive's input current. |

## When to Call a Pro

Call a qualified VFD technician or Danfoss service partner immediately if the alarm persists with the motor disconnected, as this indicates an internal drive failure requiring specialized diagnostic equipment and replacement of high-voltage components like IGBT modules or power boards. Also call a pro if you lack the training or tools to perform a megohm test on the motor, measure three-phase input power, or safely discharge the drive's capacitors. Any work inside the drive enclosure involves dangerous DC bus voltages that remain present even after AC power is removed, so only trained personnel should open the unit or replace internal boards.

**Rough cost:** A pro service call runs about $300-800 for motor insulation testing, cable repair, or IGBT module replacement.
