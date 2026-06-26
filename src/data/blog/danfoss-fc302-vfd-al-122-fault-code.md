---
title: "Danfoss FC302 AL-122 Fault - Causes & Fix"
description: "AL-122 signals motor voltage undervoltage on the DC bus. Check input phase voltage balance and verify motor parameter settings first."
pubDatetime: 2026-06-24T10:18:41Z
modDatetime: 2026-06-24T10:18:41Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 power board / IGBT module"
most_likely_cause: "Low input phase voltage or phase imbalance"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Measure all three input phases with a voltmeter and confirm they are within 3% of each other and match the drive's rated voltage"
  - "Review parameter 1-23 (Motor Nominal Voltage) and parameter 1-24 (Motor Nominal Current) to confirm they match the motor nameplate"
  - "Inspect input terminal tightness and look for signs of overheating or corrosion"
part_price: "$150-400"
no_buy_pct: "40%"
---

## Danfoss FC302 AL-122 Fault — What It Means

Alarm code 122 on the Danfoss FC302 VFD is not a standalone fault but a secondary sub-alarm that appears during Alarm 38 (Internal Fault) or Alarm 4 (Input Phase Loss). It indicates the DC bus voltage has dropped below the minimum threshold required to safely drive the motor at its configured voltage, such as below 200V DC for a 400V motor system. This undervoltage condition risks loss of torque or motor stall and is distinct from overcurrent or short-circuit faults.

The code typically appears in the drive's alarm table (Table 6.1 or Table 28 in older manuals) and points to a voltage deficiency rather than a current overload. The drive detects a mismatch between the configured motor voltage in the parameters and the actual DC bus voltage available to power the motor.

## Before You Replace Anything

Technicians often replace the power board or control card first. Before ordering parts, measure incoming three-phase voltage and verify motor parameter settings in 1-23 and 1-24, which resolves many cases at no cost.

[Jump to Fix](#fix)

## Common Causes

- **Low or imbalanced input phase voltage (~35%)** One or more input phases below rated voltage or phase imbalance greater than 3% causes the DC bus to undercharge and triggers the motor voltage alarm.
- **Incorrect motor parameter settings (~25%)** Motor nominal voltage set too high in parameter 1-23 or parameter 1-24 causes the drive to falsely detect an undervoltage condition even when DC bus voltage is adequate.
- **Loose or corroded input connections (~15%)** High resistance at input terminals or mains fuses reduces voltage delivered to the rectifier and lowers DC bus voltage under load.
- **Failed rectifier diodes (~12%)** Blown or shorted diodes on the power board prevent the DC bus capacitors from charging to full voltage.
- **Failing DC link capacitors (~10%)** Aging or weak large electrolytic capacitors on the power-stage board cannot maintain DC bus voltage under motor load.
- **Overloaded input supply (~3%)** Excess load on the AC line from other equipment starting simultaneously causes voltage sag and temporary DC bus undervoltage.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Are all three input phase voltages within 3% of each other and within 10% of the drive's rated voltage (e.g. 380-440V for a 400V system)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Input power is adequate. Move to motor parameter verification and DC bus voltage measurement.<br><strong>No:</strong> Correct the supply voltage issue (loose connection, utility problem, or overloaded circuit) before proceeding.</div>
</details>

<details class="dtree"><summary>Does parameter 1-23 (Motor Nominal Voltage) exactly match the motor nameplate voltage?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor parameters are correct. The fault is likely hardware related (rectifier, capacitors, or power board).<br><strong>No:</strong> Correct parameter 1-23 to match the motor nameplate, reset the drive, and test operation.</div>
</details>

<details class="dtree"><summary>With the drive powered but not running, does the DC bus voltage measure approximately 1.35 times the incoming AC voltage (e.g. 540V DC for 400V AC)?</summary>
<div class="dtree-body"><strong>Yes:</strong> DC bus is healthy. Review parameter settings and check for transient voltage sags during motor startup.<br><strong>No:</strong> DC bus is undercharged. Inspect rectifier diodes, input fuses, and DC link capacitors for failure.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify input voltage balance.** Power off the drive, lock out the main disconnect, then measure all three input phases (L1-L2, L2-L3, L3-L1) with a true-RMS voltmeter. Confirm voltages are within 3% of each other and within 10% of the drive's rated voltage.
2. **Inspect input connections and fuses.** With power off, check tightness of all input terminals and look for discoloration or corrosion. On larger frames, inspect 4A glass fuses between the DC bus and power card for continuity.
3. **Review motor parameter settings.** Navigate to parameter 1-23 (Motor Nominal Voltage) and parameter 1-24 (Motor Nominal Current) on the keypad. Confirm both values exactly match the motor nameplate. Incorrect settings often trigger false undervoltage alarms.
4. **Measure DC bus voltage.** With the drive powered but in standby (not running), carefully measure DC bus voltage between the + and – terminals on the power board. For a 400V AC system, expect approximately 540V DC. Below 500V DC indicates rectifier or capacitor failure.
5. **Test rectifier diodes.** Power off and disconnect all input power. Remove the power board and use a diode-test meter function to check each rectifier diode for shorts or open circuits. Replace the rectifier board if any diode is faulty.
6. **Inspect DC link capacitors.** Visually inspect the large electrolytic capacitors on the power-stage board for bulging, leakage, or physical damage. Measure capacitance with a capacitance meter if available. Replace the power board or capacitor bank if capacitors are degraded.
7. **Reset and test.** After corrections, reset the alarm using the keypad (navigate to Alarm Log and acknowledge), restore power, and run the motor under load while monitoring DC bus voltage and input phase balance. Document baseline voltages for future reference.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 power board / IGBT module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-122-fault-code&k=Danfoss+FC302+power+board+%2F+IGBT+module&tag=errorcodefixes-20) \| Order by frame size and voltage rating stamped on the board or drive nameplate. Includes rectifier and DC bus capacitors. |
| DC link capacitor bank | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-122-fault-code&k=DC+link+capacitor+bank&tag=errorcodefixes-20) \| Sold separately on some frame sizes. Match voltage rating (typically 450V or 900V) and capacitance (consult service manual). |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician if you are not trained to work with high-voltage DC (the DC bus remains energized at 500-800V even after AC power is removed and requires a controlled discharge procedure). Professional help is also required if input voltage measurements show utility supply problems, if the rectifier or power board needs replacement (which involves desoldering bus bars and torquing high-current terminals to exact specifications), or if the alarm persists after verifying parameters and input power. Work on VFDs above 1 HP involves risk of arc flash and lethal shock and should only be performed by personnel with appropriate PPE and lockout/tagout training.

**Rough cost:** A pro service call runs about $200-600.
