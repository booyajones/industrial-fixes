---
title: "Danfoss FC302 AL-105 Fault - Causes & Fix"
description: "AL-105 is not an official Danfoss code. If you see 105 under Alarm 38, it means gate driver failure. Power board replacement needed."
pubDatetime: 2026-06-23T10:21:24Z
modDatetime: 2026-06-23T10:21:24Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 power board"
most_likely_cause: "Failed gate driver IC or damaged power board components"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power cycle the drive (disconnect AC mains, wait 5 minutes, reconnect) and see if the fault clears"
  - "Disconnect the motor and run the drive unloaded to rule out motor or cable faults"
  - "Inspect the power board for visible burn marks, cracked components, or loose connectors"
part_price: "$300-900 depending on FC302 frame size"
---

## Danfoss FC302 AL-105 Fault — What It Means

There is no official Danfoss fault code AL-105 for the FC302 VFD. If your display shows 105, it is likely a subcode under Alarm 38 (Internal Fault). Subcode 105 indicates a gate driver fault or IGBT protection circuit failure. The drive has detected a problem in the power module's gate drive circuit that prevents safe switching of the IGBTs (the solid-state switches that create the motor's variable-frequency output).

This fault means the drive cannot operate safely and has shut down to protect itself and the motor. The gate driver circuit sends control signals to the IGBTs, and when this circuit fails the drive cannot regulate power. The fault typically points to a hardware failure on the power board rather than a software or configuration issue.

## Before You Replace Anything

Technicians sometimes replace the entire VFD when only the power board or gate driver IC has failed. Always isolate the motor and cables first, because a shorted motor or bad cable can trigger the same fault code and replacing the drive will not fix the external problem.

[Jump to Fix](#fix)

## Common Causes

- **Failed gate driver IC (~35%)** Overcurrent events, voltage spikes from motor cables, or thermal aging can destroy the gate driver integrated circuit that controls IGBT switching.
- **Moisture or contamination on gate driver circuit (~25%)** Humidity, dust, or conductive debris on the power board can create short circuits or parasitic paths that trip the gate driver protection.
- **Thermal aging of gate driver components (~20%)** Resistors, capacitors, and diodes in the gate driver circuit degrade over time in hot environments, changing their values and causing drive protection to activate.
- **Loose or corroded connections between power module and control board (~10%)** Poor contact between the power board and the control board can interrupt gate driver signals and trigger an internal fault.
- **Voltage spikes from motor cable (~10%)** Long motor cables or cables with inadequate shielding can induce voltage transients that damage the gate driver input stage.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear after disconnecting the motor and power cycling the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor or motor cable is likely causing the fault. Check for motor winding shorts (insulation resistance should be ≥2 MΩ) and inspect cable shield grounding.<br><strong>No:</strong> The power board or gate driver circuit has failed internally and needs repair or replacement.</div>
</details>

<details class="dtree"><summary>Do you see visible burn marks, cracked components, or bulging capacitors on the power board?</summary>
<div class="dtree-body"><strong>Yes:</strong> The power board has sustained physical damage and must be replaced. Do not attempt to operate the drive.<br><strong>No:</strong> The fault may be in the gate driver IC or associated control circuitry, which requires component-level diagnosis or board replacement.</div>
</details>

<details class="dtree"><summary>Are all cooling fans running and heat sinks free of dust?</summary>
<div class="dtree-body"><strong>Yes:</strong> Cooling is adequate. Focus on the gate driver circuit and power board electronics.<br><strong>No:</strong> Clean all heat sinks and replace any failed cooling fans. Overheating accelerates gate driver component failure.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the exact alarm** by checking the display for ALARM 38 with subcode 105, not a standalone AL-105. Consult your FC302 manual's fault table to confirm.
2. **Power cycle the drive** by disconnecting AC mains power, waiting at least 5 minutes for capacitors to discharge, then reconnecting. Check if the fault reappears.
3. **Disconnect the motor** at the VFD output terminals and attempt to run the drive unloaded. If the fault clears, the motor or cable is the problem. If it persists, the power board is faulty.
4. **Inspect the power board** for physical damage such as burn marks, cracked resistors or capacitors, corrosion, or loose connectors between the power module and control board.
5. **Measure gate driver resistance** between IGBT gate and emitter pins if you have component-level skills. Typical values are 10 to 50 Ω. Open or shorted readings indicate a failed gate driver IC.
6. **Check cooling and environment**. Confirm all cooling fans operate, heat sinks are clean, and the enclosure is free of moisture, dust, and conductive debris.
7. **Replace the power board** or gate driver IC with a Danfoss-approved replacement part for your specific FC302 frame size. Record all parameter settings before disconnecting power.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 power board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-105-fault-code&k=Danfoss+FC302+power+board&tag=errorcodefixes-20) \| Includes IGBTs, gate drivers, and DC link capacitors. Must match your drive's frame size and voltage rating. Contact Danfoss for the exact part number. |
| Gate driver IC | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-105-fault-code&k=Gate+driver+IC&tag=errorcodefixes-20) \| For component-level repair. Part number varies by FC302 model. Requires surface-mount soldering skills and board-level diagnostics. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician if you are not trained to work with high-voltage DC bus capacitors (which can hold lethal voltage for minutes after power-off), if you cannot safely isolate and test the motor, or if you lack the tools to measure gate driver circuit parameters. Power board replacement requires knowledge of proper grounding, torque specifications for power terminals, and parameter backup and restore procedures. Component-level repair of the gate driver IC requires surface-mount soldering skills and oscilloscope diagnostics. Mishandling the power board or applying power with a shorted gate driver can destroy the entire VFD and create an arc flash hazard.

**Rough cost:** A pro service call runs about $400-1200 for power board replacement including labor.

## See Also

- [Danfoss FC302 VFD AL-70 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-70-fault-code/)
- [Danfoss FC302 AL-84 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-84-fault-code/)
- [Danfoss FC302 VFD Alarm 41 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-41-fault-code/)
- [Danfoss RX Controller Fault Codes — Troubleshooting Guide](/posts/danfoss-rx-controller-fault/)
