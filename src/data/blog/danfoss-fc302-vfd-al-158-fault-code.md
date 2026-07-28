---
title: "Danfoss FC302 AL-158 Fault - Causes & Fix"
description: "AL-158 is not a documented Danfoss FC302 code. Likely Alarm 13/14/16 (DC bus undervoltage). Check input power and motor windings first."
pubDatetime: 2026-06-26T09:50:46Z
modDatetime: 2026-06-26T09:50:46Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 power board assembly"
most_likely_cause: "incoming power supply issue or loose input terminal"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify incoming line voltage at input terminals during operation and startup for voltage sags or drops"
  - "Inspect all input and output terminal connections for looseness or corrosion and tighten if needed"
  - "Check parameter 1-24 (motor current) matches the actual motor nameplate rating"
---

## What this code means
There is no specific AL-158 fault code documented for the Danfoss FC302 VLT AutomationDrive. Danfoss FC302 alarms are numbered sequentially (for example Alarm 13, 14, 16, 38, 60) and do not include 158. The code may be a misread or typo. The most likely match is Alarm 13, 14, or 16, which indicates DC bus undervoltage. This means the DC bus voltage has dropped below the minimum threshold (typically around 200V) required for proper motor control. The drive shuts down to protect itself and the motor from damage caused by insufficient voltage.

## Before You Replace Anything

Technicians often replace the power board or IGBT modules before testing the motor windings. A simple megohm test (reading below 2 MΩ to ground indicates motor insulation failure) and running the drive unloaded can isolate whether the fault is internal to the drive or in the motor and cabling.

## Common Causes

- **Incoming power supply issues (~35%)** Loose input terminals, blown fuses, or voltage sags from other equipment starting on the same transformer can drop the DC bus below 200V.
- **Motor winding insulation failure (~25%)** A partial short or insulation breakdown (megohm test reading below 2 MΩ to ground) causes excessive current draw and voltage drop.
- **Incorrect motor parameter settings (~15%)** Parameter 1-24 (nominal motor current) set too high for the actual motor draws excessive current and triggers undervoltage protection.
- **Loose or corroded motor wiring (~10%)** High resistance in motor cables or connections increases current spikes and voltage drop during acceleration or load changes.
- **Mechanical overload on motor shaft (~10%)** A seized bearing, jammed load, or excessive mechanical resistance forces the motor to draw more current than the supply can sustain.
- **Failed IGBT modules or DC link capacitors (~5%)** Aging or damaged power board components lose the ability to regulate current and maintain stable DC bus voltage.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the alarm persist when you run the drive with the motor disconnected?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is internal to the drive (power board, IGBTs, or DC link capacitors). Call a VFD technician for power board diagnostics.<br><strong>No:</strong> The problem is in the motor, motor cables, or load. Proceed to test motor winding insulation and cable continuity.</div>
</details>

<details class="dtree"><summary>Does a megohm test show motor winding resistance to ground below 2 MΩ?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor insulation has failed. Replace or rewind the motor.<br><strong>No:</strong> Motor windings are intact. Check cable connections, input voltage during startup, and parameter 1-24 for correct motor current rating.</div>
</details>

<details class="dtree"><summary>Does input line voltage drop below the rated minimum during motor startup?</summary>
<div class="dtree-body"><strong>Yes:</strong> Incoming power supply is inadequate or shared with high-draw equipment. Upgrade supply or isolate the VFD on a dedicated circuit.<br><strong>No:</strong> Check for mechanical overload, loose output connections, or incorrect torque limit settings in parameter 14-25.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the VFD** and lock out the main disconnect. Wait at least 5 minutes for DC bus capacitors to discharge before opening the enclosure.
2. **Disconnect the motor** from the VFD output terminals (U, V, W). Run the drive unloaded and observe if the alarm clears. If the fault persists, the issue is internal to the drive.
3. **Perform a megohm test** on the motor windings to ground using an insulation tester. Readings below 2 MΩ indicate insulation failure and require motor replacement or rewinding.
4. **Measure incoming line voltage** at the VFD input terminals during operation and motor startup. Look for voltage sags or drops below the rated minimum (consult your model's input voltage range).
5. **Inspect all terminal connections** at the input, output, and control terminals. Tighten any loose connections and clean corroded terminals with electrical contact cleaner.
6. **Verify parameter 1-24** (motor nominal current) matches the motor nameplate rating exactly. Incorrect settings cause the VFD to draw excessive current.
7. **Check parameter 15-32** for extended alarm codes that provide additional diagnostic information. Cross-reference with the FC302 manual for specific fault details.
8. **Test output to motor for short circuits**. With the motor disconnected, measure resistance from each output terminal (U, V, W) to ground. Any low resistance indicates a shorted power board or output stage.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 power board assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-158-fault-code&k=Danfoss+FC302+power+board+assembly&tag=errorcodefixes-20) \| Rectifier and inverter section with IGBT modules and DC link capacitors. Required if internal fault persists with motor disconnected. |
| IGBT module set | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-158-fault-code&k=IGBT+module+set&tag=errorcodefixes-20) \| Individual replacement IGBTs for the inverter section. Consult your drive model and power rating for correct part number. |

## When to Call a Pro

Call a VFD technician if the alarm persists with the motor disconnected (indicating internal drive failure), if you are not comfortable working with high-voltage DC and AC circuits, or if you lack the tools to perform megohm testing and DC bus diagnostics. Power board and IGBT replacement requires precise component matching, proper thermal compound application, and testing under load. Technicians can also perform parameter optimization and input power quality analysis to prevent future faults. If the motor has failed insulation, a motor shop can perform rewinding or you may need a replacement motor matched to the drive's power and voltage rating.

**Rough cost:** A pro service call runs about $300-800.
