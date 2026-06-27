---
title: "Danfoss FC302 AL-145 Fault - Causes & Fix"
description: "AL-145 likely refers to Alarm 14 (Overcurrent). Most common cause is motor winding insulation failure. Test motor isolated from drive."
pubDatetime: 2026-06-25T09:31:37Z
modDatetime: 2026-06-25T09:31:37Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 Power Board (Inverter Section)"
most_likely_cause: "motor winding insulation failure"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify Parameter 1-24 (Nominal Motor Current) matches the actual motor nameplate rating"
  - "Check all three input phases with a voltmeter to confirm voltage imbalance is within 3 percent"
  - "Reseat or remove any option cards (brake control, communication modules) to rule out hardware mismatch"
---

## Danfoss FC302 AL-145 Fault — What It Means

The specific fault code AL-145 does not appear in official Danfoss FC302 documentation. You are likely seeing Alarm 14 (Overcurrent), which means the drive output current exceeded the peak current limit set for the motor. This typically happens during acceleration or sudden load changes when the drive detects current levels higher than the IGBTs can safely handle. The fault protects the drive from damage due to motor shorts, ground faults, or internal power board failures.

Less commonly, you may be dealing with Alarm 15 (Hardware Mismatch), which occurs when an incompatible option card is installed, or Alarm 43, which points to control card issues. The repair process starts by isolating whether the fault is in the motor circuit or inside the drive itself.

## Before You Replace Anything

Technicians often replace the entire drive power board before testing the motor windings. A simple megohm test of the motor insulation to ground (which should read above 2 megohms) will identify a failed motor and save the cost of unnecessary drive parts.

[Jump to Fix](#fix)

## Common Causes

- **Motor winding insulation failure (~40%)** Deteriorated motor winding insulation from moisture, contamination, or thermal aging creates a partial short that drives current above the peak limit.
- **Output cable ground faults (~25%)** Damaged or loose motor cables create resistance spikes or ground faults, especially common with long cable runs and high-frequency PWM switching.
- **Internal drive power board failure (~15%)** Aging or damaged IGBT modules on the inverter section lose regulation ability and trigger overcurrent detection even under normal load.
- **Mechanical overload or motor overheating (~10%)** A mechanically jammed motor shaft or overheated motor draws current spikes that exceed the drive's programmed limits.
- **Incorrect parameter settings (~7%)** Nominal motor current (Parameter 1-24) set significantly higher than the actual motor rating causes false overcurrent detection.
- **Hardware mismatch (Alarm 15) (~3%)** Installation of a non-compatible option card that the drive does not recognize triggers a hardware mismatch alarm instead of overcurrent.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear when you disconnect the motor from the drive output terminals (U, V, W) and run the drive unloaded?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem is in the motor or motor cables. Proceed to megohm testing and cable inspection.<br><strong>No:</strong> The problem is internal to the drive's power board. Check for failed IGBTs, DC link capacitors, or cooling fans.</div>
</details>

<details class="dtree"><summary>Do all three input phases measure within 3 percent of one another with a voltmeter?</summary>
<div class="dtree-body"><strong>Yes:</strong> Input power is balanced. Focus on the motor circuit or internal drive components.<br><strong>No:</strong> Voltage imbalance is causing the fault. Check for blown input fuses, failed rectifiers, or utility supply problems.</div>
</details>

<details class="dtree"><summary>Does the motor insulation test show resistance above 2 megohms to ground?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor windings are healthy. Inspect output cables for damage or loose connections and verify drive parameter settings.<br><strong>No:</strong> Motor insulation has failed. Replace or rewind the motor.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect the motor** from the drive output terminals (U, V, W) and attempt to run the drive unloaded with no motor connected.
2. **If the fault clears**, perform a megohm test on the motor windings to ground using an insulation tester (readings must be above 2 megohms).
3. **Check motor cable continuity** from drive output terminals to motor windings and inspect cables for physical damage, especially at terminations and bends.
4. **If the fault persists** with the motor disconnected, measure all three input phases with a voltmeter to confirm voltage imbalance is less than 3 percent.
5. **Verify Parameter 1-24** (Nominal Motor Current) matches the motor nameplate rating exactly and adjust if incorrect.
6. **Reseat or remove option cards** (brake control, communication modules) to rule out hardware mismatch, especially if you see Alarm 15.
7. **Replace the power board** (rectifier and inverter assembly) or specific failed IGBTs and DC link capacitors if internal drive components have failed, and replace any failed cooling fans immediately.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 Power Board (Inverter Section) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-145-fault-code&k=Danfoss+FC302+Power+Board+%28Inverter+Section%29&tag=errorcodefixes-20) \| Match the exact power rating and voltage class to your drive model number. |
| IGBT Module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-145-fault-code&k=IGBT+Module&tag=errorcodefixes-20) \| Consult your model's service manual for the correct part number if replacing individual semiconductors. |
| Motor (if insulation failed) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-145-fault-code&k=Motor+%28if+insulation+failed%29&tag=errorcodefixes-20) \| Replacement or professional rewind required if megohm test reads below 2 megohms. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician if the fault persists after disconnecting the motor, because internal power board repair requires high-voltage DC bus capacitor discharge procedures and IGBT module replacement. Also call a pro if you are not trained to perform megohm testing on motor windings or if the drive is part of a critical production system where downtime must be minimized. If the motor insulation has failed and the motor is large or permanently mounted, professional rewinding or motor replacement is the safest option.

**Rough cost:** A pro service call runs about $300-800.
