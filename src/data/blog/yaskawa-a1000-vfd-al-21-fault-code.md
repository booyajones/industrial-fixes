---
title: "Yaskawa A1000 CPF21 (often misread as AL-21) - Causes & Fix"
description: "CPF21 means control circuit hardware failure inside the drive. Most likely fix: power cycle, then replace the control board or entire drive."
pubDatetime: 2026-06-30T09:44:55Z
modDatetime: 2026-06-30T09:44:55Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa A1000 Control Board"
most_likely_cause: "Damaged control board hardware"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Turn off the drive, wait 5 minutes for full discharge, then restart to see if CPF21 clears (transient fault)"
  - "Power off and disconnect, then reconnect the terminal board to the control board and inspect pins for corrosion or looseness"
---

## Yaskawa A1000 CPF21 (often misread as AL-21) — What It Means

The Yaskawa A1000 does not have an 'AL-21' fault code. The error you are seeing is almost certainly CPF21, which is often misread as AL-21 due to display formatting. CPF21 indicates a Control Circuit Error, meaning the drive's internal control hardware is damaged or the control circuitry responsible for managing drive operation is faulty. This is not a motor feedback, encoder, or parameter problem. It is a failure of the drive's own control board or associated circuitry.

The fault means the microcontroller, A/D converter, or other components on the control board have failed, or the connections between the control board and terminal board have become loose or corroded. Yaskawa documentation confirms CPF21 as a hardware damage fault and recommends power cycling, reseating connections, replacing the control board, or replacing the entire drive. Do not attempt component-level repair by soldering chips or other internal parts.

## Before You Replace Anything

Technicians sometimes replace the digital operator or check motor connections first, but CPF21 is a control board fault, not a motor or display problem. Power cycle and reseat the terminal board before ordering parts.

[Jump to Fix](#fix)

## Common Causes

- **Damaged control board hardware (~60%)** Failed microcontroller, burnt A/D converter, or other component failure on the control board triggers CPF21.
- **Loose or corroded terminal board connection (~20%)** Poor contact between the control board and terminal board can disrupt control circuitry and trigger the fault.
- **Power supply issues to control circuit (~10%)** Unstable DC voltage from the main circuit (should be 24V DC, acceptable 22 to 28V) can corrupt control logic.
- **Overheating damage (~5%)** Internal drive temperature above 60°C can damage control board components over time.
- **Environmental stress (~5%)** Moisture, dust, or contaminants on the control board can cause short circuits or component degradation.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear after a full power cycle (off for 5 minutes, then restart)?</summary>
<div class="dtree-body"><strong>Yes:</strong> It was likely a transient issue. Monitor the drive and check ventilation to prevent overheating.<br><strong>No:</strong> The control board or connections are damaged. Proceed to reseat the terminal board and inspect for corrosion.</div>
</details>

<details class="dtree"><summary>Is the terminal board connection to the control board firmly seated and free of corrosion?</summary>
<div class="dtree-body"><strong>Yes:</strong> The control board itself is likely damaged. Replace the control board or entire drive.<br><strong>No:</strong> Clean and reseat the connection, then restart. If CPF21 persists, replace the control board.</div>
</details>

<details class="dtree"><summary>Is the drive mounted in a hot location or is internal temperature above 60°C?</summary>
<div class="dtree-body"><strong>Yes:</strong> Overheating may have damaged the control board. Improve ventilation and replace the control board if fault remains.<br><strong>No:</strong> The fault is hardware failure, not environmental. Replace the control board or drive.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off the drive** at the main disconnect and wait 5 minutes for all capacitors to discharge fully before opening the enclosure.
2. **Cycle power** by restarting the drive. If CPF21 clears and does not return, monitor operation and check ambient temperature and ventilation.
3. **Power off again** and disconnect the terminal board from the control board. Inspect the connector pins and socket for corrosion, bent pins, or loose fit.
4. **Reconnect the terminal board** firmly and restart. If CPF21 persists, the control board is damaged.
5. **Measure DC voltage** at the control circuit input (typically 24V DC). If it is outside 22 to 28V, check the power supply circuit and replace if needed.
6. **Replace the control board** with a model-specific unit (check your A1000 model number for the correct control board part). If CPF21 returns, the main circuit or power supply is also damaged.
7. **Replace the entire drive** if control board replacement does not resolve the fault, as multiple internal circuits are likely compromised.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa A1000 Control Board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-21-fault-code&k=Yaskawa+A1000+Control+Board&tag=errorcodefixes-20) \| Model-specific (e.g. for A1000-4030 or your exact drive model). Contact Yaskawa or a distributor for the correct part number. |
| Yaskawa A1000 VFD (complete drive unit) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-21-fault-code&k=Yaskawa+A1000+VFD+%28complete+drive+unit%29&tag=errorcodefixes-20) \| Required if control board replacement fails or main circuit is also damaged. Match horsepower and voltage to your motor. |

## When to Call a Pro

Call a qualified industrial electrician or VFD technician if you are not trained in high-voltage electrical work or VFD troubleshooting. CPF21 requires opening the drive enclosure, working near lethal DC bus voltages (even after disconnect), and replacing internal boards. Improper handling can destroy the replacement board, damage the motor, or cause electrical shock. A technician will safely discharge the drive, measure control circuit voltages, source the correct control board for your A1000 model, and replace the board or entire drive. If your facility does not have in-house electrical staff, contact a Yaskawa-authorized service center for board repair or drive replacement.

**Rough cost:** A pro service call runs about $300-800 for control board replacement, $1,000-3,000+ for full drive replacement depending on model and horsepower.

## See Also

- [Yaskawa GA800 E26 Fault Code - Causes & Fix](/posts/yaskawa-ga800-e26-fault-code/)
- [Yaskawa GA800 E23 Fault Code - Causes & Fix](/posts/yaskawa-ga800-vfd-e23-fault-code/)
- [Yaskawa GA800 E01 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e01-fault-code/)
- [Yaskawa A1000 AL-26 Fault - Causes & Fix](/posts/yaskawa-a1000-vfd-al-26-fault-code/)
