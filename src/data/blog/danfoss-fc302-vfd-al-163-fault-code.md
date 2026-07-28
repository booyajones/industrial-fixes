---
title: "Danfoss FC302 Alarm 16 (DC Bus Low) - Causes & Fix"
description: "Alarm 16 means DC bus voltage dropped below safe limits. Most often caused by low incoming mains voltage or failed rectifier diodes."
pubDatetime: 2026-06-26T09:54:44Z
modDatetime: 2026-06-26T09:54:44Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Rectifier board (Danfoss FC302 power section)"
most_likely_cause: "low or imbalanced incoming mains voltage"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Measure incoming voltage at L1, L2, and L3 to confirm it is within rated range and balanced within 3%"
  - "Check all input terminal connections (L1, L2, L3) for tightness and signs of arcing or corrosion"
  - "Inspect input fuses in the distribution panel and drive fuse block for opens or blown elements"
---

## What this code means
Alarm 16 on a Danfoss FC302 variable frequency drive indicates that the DC bus voltage inside the drive has fallen below the minimum threshold (typically around 350V for a 400V class unit or 175V for a 230V unit). The drive shuts down to protect the inverter section and connected motor from damage. This fault signals that the rectifier cannot maintain the required DC level, usually because of a problem with the incoming AC power supply or a failure in the rectifier circuit itself.

Note: if you saw "AL-163" on the display, it is likely a misreading of Alarm 16 followed by another parameter code or a display artifact. Danfoss FC302 alarms are numbered 1 through 99, and Alarm 16 is the standard low DC bus voltage fault for this drive family.

## Before You Replace Anything

Technicians sometimes replace the control board or power supply when the real culprit is a failed rectifier diode or loose input terminal. Always test the rectifier diodes and measure input voltage before swapping boards.

## Common Causes

- **Low or imbalanced incoming voltage (~40%)** Mains voltage below the drive's rated range or imbalance greater than 3% prevents the rectifier from charging the DC bus to the minimum threshold.
- **Failed rectifier diode (~30%)** One or more diodes in the input rectifier assembly have shorted or opened, blocking proper DC charging and causing the bus voltage to sag.
- **Blown input fuse (~15%)** An open fuse in the facility panel or drive's internal fuse block cuts power to the rectifier and starves the DC bus.
- **Loose input terminal connections (~10%)** Poor contact at L1, L2, or L3 terminals creates high resistance and voltage drop, preventing the rectifier from seeing full mains voltage.
- **Excessive load or voltage sag on shared circuit (~5%)** Other heavy equipment starting on the same feeder can cause a momentary mains voltage dip that trips the drive.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the incoming voltage at L1, L2, and L3 within the drive's rated range and balanced within 3%?</summary>
<div class="dtree-body"><strong>Yes:</strong> Mains power is good, so focus on the drive's rectifier circuit, input fuses, and terminal connections.<br><strong>No:</strong> Correct the mains voltage issue (add a transformer, balance phases, or upgrade the distribution panel) before troubleshooting the drive itself.</div>
</details>

<details class="dtree"><summary>Are all three input fuses intact and all input terminals tight with no signs of arcing?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem is likely inside the drive, most often a failed rectifier diode or control power supply.<br><strong>No:</strong> Replace any blown fuse and re-torque loose terminals, then reset the drive and test.</div>
</details>

<details class="dtree"><summary>Does the alarm clear and stay off after a reset with no load connected?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive hardware is probably fine and the issue is excessive motor load, long cable runs, or transient voltage sags during operation.<br><strong>No:</strong> The rectifier board or power board has likely failed and needs professional replacement.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify incoming mains voltage** by measuring L1-L2, L2-L3, and L3-L1 with a voltmeter and confirm all three readings are within the drive's rated range and balanced within 3%.
2. **Inspect and test input fuses** in both the facility distribution panel and the drive's internal fuse block, and replace any that are open or blown.
3. **Check input terminal tightness** at L1, L2, and L3 on the drive, re-torque to the manufacturer's specification, and look for signs of arcing, corrosion, or loose wire strands.
4. **Test the rectifier diodes** on the power board using a multimeter in diode-test or resistance mode, checking each diode for forward conduction and reverse blocking, and replace the rectifier assembly if any diode is shorted or open.
5. **Examine DC bus capacitors** for physical swelling, leakage, or bulging, as a weak capacitor bank can cause rapid voltage sag under load even when the rectifier is healthy.
6. **Reset the drive** by cycling control power or using the keypad reset function, and monitor the DC bus voltage parameter (consult your model's parameter list) during a no-load start to confirm it reaches and holds the nominal level.
7. **Call a qualified drive technician** if the rectifier and capacitors test good but the alarm persists, as the control power supply or main control board may have failed and require factory-level diagnostics.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Rectifier board (Danfoss FC302 power section) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-163-fault-code&k=Rectifier+board+%28Danfoss+FC302+power+section%29&tag=errorcodefixes-20) \| Model-specific; consult your drive's frame size and voltage rating before ordering. |
| Input fuse set (drive-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-163-fault-code&k=Input+fuse+set+%28drive-rated%29&tag=errorcodefixes-20) \| Must match the drive's input current rating; check the drive nameplate or manual. |

## When to Call a Pro

Call a professional drive technician or industrial electrician if you are not comfortable working with high-voltage three-phase power, if the incoming mains voltage is correct but the alarm persists, or if testing reveals a failed rectifier or power board that requires replacement. VFD repairs involve lethal voltages (even after power-down, DC bus capacitors can hold a dangerous charge for minutes) and precise torque specifications for terminal connections. A qualified tech will have the correct test equipment, replacement boards, and experience to diagnose control-supply failures or intermittent faults that do not show up on basic voltage checks. If the drive is under warranty or part of a critical production line, always involve the manufacturer's service partner to avoid voiding coverage or causing downtime.

**Rough cost:** A pro service call runs about $200-600.
