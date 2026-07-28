---
title: "Danfoss FC302 Alarm 11 - DC Voltage Too Low Causes & Fix"
description: "Alarm 11 (DC Link Voltage Too Low) means the internal DC bus dropped below minimum. Check input voltage first, then rectifier diodes."
pubDatetime: 2026-06-24T10:07:12Z
modDatetime: 2026-06-24T10:07:12Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 rectifier board"
most_likely_cause: "Low input voltage or voltage imbalance on the AC mains"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Measure incoming three-phase voltage at the drive input terminals and verify all phases are within 3% of each other and within rated range"
  - "Tighten all input terminal screws and inspect for loose, corroded, or discolored connections"
  - "Disconnect the motor and attempt to run the drive in no-load mode to isolate mechanical overload"
no_buy_pct: "60%"
---

## What this code means
Alarm 11 on the Danfoss FC302 VFD means the internal DC link (bus) voltage has fallen below the minimum operational threshold. For 400 VAC models this is typically below 300 V, and for 230 VAC models below 150 V. When the drive detects this condition it immediately trips and stops motor operation to protect internal components from damage.

The DC link is the intermediate high-voltage DC stage inside the drive that feeds the inverter. When this voltage collapses, the drive cannot maintain proper motor control. The fault usually points to input power problems, failed rectifier components, or excessive mechanical load drawing more current than the DC bus can sustain.

## Before You Replace Anything

Technicians sometimes replace the entire power module or IGBT board first. Measure incoming AC voltage and check for blown input fuses or loose input terminals before ordering expensive boards, since most Alarm 11 faults trace to external power or simple rectifier diode failure.

## Common Causes

- **Low or imbalanced input voltage (~40%)** Incoming AC mains voltage is below the drive's rated minimum (for example below 340 VAC for 400 VAC systems) or phases differ by more than 3%, starving the rectifier and collapsing the DC bus.
- **Blown input fuse (~20%)** A blown fuse on one or more input phases prevents full voltage from reaching the rectifier, reducing DC conversion and triggering the low-voltage alarm.
- **Failed rectifier diodes (~15%)** One or more rectifier diodes on the power board are open or shorted, reducing DC conversion efficiency and dropping the DC link voltage below threshold.
- **Excessive mechanical load (~10%)** The motor is overloaded or stalled, causing the drive to draw excessive current and collapse the DC bus voltage under load.
- **Loose or corroded input wiring (~10%)** High-resistance connections at the input terminals cause voltage drop under load, reducing the effective input voltage to the rectifier.
- **Failing control power supply (~5%)** The internal control supply is degrading and causing voltage instability or incorrect DC bus measurement, triggering false low-voltage alarms.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the alarm clear when you disconnect the motor and run the drive in no-load mode?</summary>
<div class="dtree-body"><strong>Yes:</strong> The mechanical load is too high or the motor is stalled. Reduce load, check for seized bearings, or verify motor sizing.<br><strong>No:</strong> The fault is internal to the drive or in the input power supply. Proceed to measure input voltage and check rectifier components.</div>
</details>

<details class="dtree"><summary>Are all three incoming AC phases within 3% of each other and above the rated minimum voltage?</summary>
<div class="dtree-body"><strong>Yes:</strong> Input power is acceptable. The problem is likely failed rectifier diodes, blown internal fuses, or a failing power board.<br><strong>No:</strong> Input power is the problem. Check utility supply, facility fuses, breakers, and input wiring for loose connections or undersized conductors.</div>
</details>

<details class="dtree"><summary>Do you see any blown fuses or discolored terminals at the drive input?</summary>
<div class="dtree-body"><strong>Yes:</strong> Replace blown fuses and clean or tighten corroded terminals. Check for short circuits downstream before restoring power.<br><strong>No:</strong> The fault is inside the drive. Test rectifier diode continuity and inspect the power board for failed components.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Measure input voltage** at all three phases with a voltmeter while the drive is powered. Verify voltage is within the rated range and all phases are within 3% of each other.
2. **Check input fuses** in the facility distribution panel and at the drive input terminals. Replace any blown fuses and investigate the cause before restoring power.
3. **Inspect input terminals** by powering off the drive, removing the cover, and checking that all input terminal screws are tight and connections are clean and free of corrosion.
4. **Disconnect the motor** and attempt to power the drive with no load. If the alarm clears, the mechanical load is too high or the motor is stalled.
5. **Test rectifier diodes** by powering off the drive, removing input mains, and measuring forward and reverse resistance of each diode with a multimeter. Open or shorted diodes indicate rectifier failure.
6. **Inspect the power board** for signs of overheating, burned traces, or failed components such as capacitors or resistors in the DC link circuit.
7. **Replace the rectifier board** or power module if diode testing confirms failure, or call a qualified technician if internal components show damage.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 rectifier board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-110-fault-code&k=Danfoss+FC302+rectifier+board&tag=errorcodefixes-20) \| Match the part number to your drive's frame size and voltage rating |
| Input line fuses | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-110-fault-code&k=Input+line+fuses&tag=errorcodefixes-20) \| Consult the drive nameplate for fuse type and current rating |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician if you are not trained to work with high-voltage DC circuits. The DC link inside the drive can hold lethal voltage even after input power is removed. A technician will safely discharge capacitors, test rectifier components with proper instruments, and replace power boards or modules. Also call a pro if input voltage measurements and fuse checks do not reveal an obvious cause, or if the drive shows signs of internal damage such as burned traces or failed IGBTs.

**Rough cost:** A pro service call runs about $150-600.
