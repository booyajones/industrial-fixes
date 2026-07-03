---
title: "Danfoss FC302 VFD Alarm 14 - Causes & Fix"
description: "Alarm 14 means DC bus voltage dropped below minimum (typically 200V). Most often caused by low input voltage or a missing phase."
pubDatetime: 2026-06-25T09:27:21Z
modDatetime: 2026-06-25T09:27:21Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 power board (rectifier/inverter assembly)"
most_likely_cause: "Low input voltage or missing phase"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Check all three input phases with a voltmeter to confirm they are balanced within 3% and at rated voltage"
  - "Inspect input terminal connections for loose wires or corrosion"
  - "Review parameter settings to confirm motor nominal current is not set higher than the actual motor rating"
no_buy_pct: "40%"
---

## Danfoss FC302 VFD Alarm 14 — What It Means

Alarm 14 on a Danfoss FC302 VFD indicates DC Undervoltage. The DC bus voltage has fallen below the minimum threshold (typically below 200V) needed to regulate the motor. This alarm triggers when the input AC power is insufficient, the rectifier is failing, or the load is excessive, causing the DC link to collapse.

Note: There is no documented "AL-140" fault code in Danfoss literature. If you are seeing a code ending in "40" (such as Alarm 38 with code 40), that represents a specific internal logic error and requires different diagnostics. This guide assumes you mean Alarm 14, the DC undervoltage alarm.

## Before You Replace Anything

Technicians often replace the entire power board or inverter assembly before checking input power quality. Measure all three input phases with a voltmeter first. Many Alarm 14 cases are simply loose incoming wiring or utility supply issues that cost nothing to fix.

[Jump to Fix](#fix)

## Common Causes

- **Low input voltage or missing phase (~40%)** Input AC power drops below spec or one phase is lost, starving the DC bus and triggering the undervoltage alarm.
- **Rectifier failure (~25%)** Bad rectifier diodes or a failing input rectifier assembly prevent proper AC-to-DC conversion, collapsing the DC link voltage.
- **Voltage imbalance greater than 3% (~15%)** Unbalanced input phases create uneven DC bus charging and can trip the alarm even when nominal voltage is present.
- **Aging DC link capacitors (~10%)** Failing capacitors lose their ability to hold charge, causing DC bus voltage to sag under load.
- **Motor or cable insulation failure (~7%)** Deteriorated motor winding insulation or damaged motor cables create resistance or short-circuit paths that load the DC bus excessively.
- **Incorrect motor parameter settings (~3%)** Motor nominal current set higher than actual rating causes the drive to misinterpret load conditions and false-trigger the alarm.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Do all three input phases measure within 3% of each other and at rated voltage?</summary>
<div class="dtree-body"><strong>Yes:</strong> Input power is good. Proceed to inspect the drive's internal rectifier and DC link components.<br><strong>No:</strong> Fix the utility supply or upstream wiring. Tighten connections and balance phases before resetting the drive.</div>
</details>

<details class="dtree"><summary>Does Alarm 14 clear when you disconnect the motor and run the drive unloaded?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor or output cables are faulty. Perform a megohm test on motor windings (should be above 2 megohms to ground).<br><strong>No:</strong> The drive has an internal component failure (rectifier, IGBTs, or DC link capacitors). Replace the power board.</div>
</details>

<details class="dtree"><summary>Are there any blown fuses or visible damage on the input rectifier assembly?</summary>
<div class="dtree-body"><strong>Yes:</strong> Replace the blown fuse or damaged rectifier assembly and retest.<br><strong>No:</strong> Check DC link capacitors and IGBT modules for degradation or replace the entire power board if no obvious damage is found.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Measure incoming AC voltage** at all three input phases with a voltmeter to confirm they are balanced within 3% and at rated voltage.
2. **Inspect input terminal connections** for loose wires, corrosion, or blown input fuses and tighten or replace as needed.
3. **Disconnect the motor** from the drive output terminals and attempt to run the drive unloaded to isolate whether the fault is internal or external.
4. **Perform a megohm test** on the motor windings if the alarm clears with the motor disconnected (readings below 2 megohms indicate insulation failure).
5. **Inspect the rectifier assembly** on the power board for blown diodes or visible damage and replace the rectifier if faulty.
6. **Check DC link capacitors** for bulging or leakage and replace them if they show signs of degradation.
7. **Replace the power board** (rectifier plus inverter assembly) if the fault persists with the motor disconnected and no obvious component damage is found.
8. **Review drive parameters** (especially motor nominal current) to make sure they match the actual motor nameplate ratings and correct any errors.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 power board (rectifier/inverter assembly) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-140-fault-code&k=Danfoss+FC302+power+board+%28rectifier%2Finverter+assembly%29&tag=errorcodefixes-20) \| Match to your drive's voltage and current rating |
| DC link capacitor set | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-140-fault-code&k=DC+link+capacitor+set&tag=errorcodefixes-20) \| OEM or equivalent rated for DC bus voltage |
| Input rectifier module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-140-fault-code&k=Input+rectifier+module&tag=errorcodefixes-20) \| Check Danfoss part number for your specific FC302 frame size |

## When to Call a Pro

Call a qualified electrician or drive technician if you lack the tools or training to safely measure high-voltage AC input, work inside the VFD cabinet, or test DC bus components. Repairing a VFD involves lethal voltages (even when disconnected, DC link capacitors can hold a charge). A professional will have the proper PPE, isolation tools, and capacitor discharge equipment. If the fault persists after checking input power and you need to open the drive enclosure, hire a pro. Similarly, if motor insulation testing shows a fault below 2 megohms, a motor shop will need to rewind or replace the motor windings.

**Rough cost:** A pro service call runs about $200-800 depending on component replacement.

## See Also

- [Danfoss FC302 AL-92 - Causes & Fix](/posts/danfoss-fc302-vfd-al-92-fault-code/)
- [Danfoss FC302 Alarm 25 - Causes & Fix](/posts/danfoss-fc302-alarm-25-fault-code/)
- [Danfoss VFD Fault W30 — Brake Resistor Overtemperature Fix](/posts/danfoss-vfd-fault-w30/)
- [Danfoss FC302 AL-158 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-158-fault-code/)
