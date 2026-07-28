---
title: "Danfoss FC302 AL-78 Fault - Causes & Fix"
description: "AL-78 means Tracking Error: motor speed can't follow setpoint. Most often caused by mechanical overload or incorrect motor parameters."
pubDatetime: 2026-06-22T10:29:39Z
modDatetime: 2026-06-22T10:29:39Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Motor output cable (shielded VFD-rated)"
most_likely_cause: "mechanical overload or motor jam"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Check for mechanical binding or jam in the motor shaft and load by hand"
  - "Verify input voltage on all three phases is balanced within 3% and within rated range"
  - "Review parameter 1-20 through 1-25 and confirm motor nameplate data matches drive settings"
---

## What this code means
Alarm 78 on a Danfoss FC302 VFD indicates a Tracking Error. The drive has detected that the actual motor speed is deviating from the commanded setpoint by more than the allowable threshold set in parameter 4-106 (Tracking Error Trip Level). This is not an overcurrent or short circuit alarm. Instead, it signals that the drive is losing control authority and cannot make the motor follow the speed reference. The fault trips when the difference between desired and actual speed exceeds the programmed limit.

This condition can arise from mechanical problems preventing the motor from reaching speed, incorrect drive configuration that misestimates torque requirements, power supply issues limiting output capability, or electrical faults in the motor or cabling. The drive is designed to protect itself and the motor by shutting down when it detects this loss of synchronization.

## Before You Replace Anything

Technicians often replace the VFD itself when the fault is actually in the motor or mechanical load. Always disconnect the motor and run the drive unloaded first to isolate whether the problem is in the drive or downstream.

## Common Causes

- **Mechanical overload or jam (~35%)** The motor is unable to accelerate to the setpoint because the load is too heavy, the shaft is binding, or something is physically blocking rotation.
- **Incorrect motor parameters (~25%)** Parameters 1-20 to 1-25 (nominal voltage, current, power, frequency) do not match the actual motor nameplate, causing the drive to miscalculate required torque.
- **Low or unbalanced input voltage (~20%)** Input line voltage is below rated value or phase imbalance exceeds 3%, preventing the drive from generating enough output torque.
- **Ground fault or short circuit in motor or cables (~12%)** A ground fault or short in the motor windings or output cables limits drive current and causes speed loss.
- **Unstable reference or feedback signal (~8%)** External speed reference on terminals 53/54 is noisy or an encoder feedback device is sending intermittent signals.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the motor shaft spin freely by hand with power off?</summary>
<div class="dtree-body"><strong>Yes:</strong> Mechanical load is not jammed. Move on to check drive parameters and input power.<br><strong>No:</strong> Mechanical binding or overload is present. Inspect coupling, bearings, and load for obstruction or excessive friction.</div>
</details>

<details class="dtree"><summary>Does the fault clear when the motor is disconnected and the drive runs unloaded?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem is in the motor, cables, or mechanical load. Inspect motor for ground faults and mechanical issues.<br><strong>No:</strong> The drive itself may have a configuration error or internal fault. Check parameter settings and input power quality.</div>
</details>

<details class="dtree"><summary>Are all three input line voltages within 3% of each other?</summary>
<div class="dtree-body"><strong>Yes:</strong> Input power is balanced. Focus on motor parameters, cables, and load issues.<br><strong>No:</strong> Phase imbalance is present. Correct the upstream supply or check for loose connections at the drive input.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect the motor** from the VFD output terminals and attempt to run the drive in test mode with no load connected. If Alarm 78 clears, the fault is downstream in the motor or mechanical system.
2. **Inspect the mechanical load** for binding, jams, or excessive friction. Rotate the motor shaft by hand to confirm it spins freely. Check coupling alignment and bearing condition.
3. **Verify motor nameplate data** against drive parameters 1-20 (Motor Nominal Voltage), 1-21 (Motor Nominal Frequency), 1-22 (Motor Nominal Current), 1-23 (Motor Nominal Speed), and 1-24 (Motor Nominal Power). Enter the exact nameplate values.
4. **Measure input line voltage** on all three phases at the drive input terminals with a multimeter. Confirm voltages are balanced within 3% of each other and within the drive's rated range.
5. **Test motor and cable insulation** using a megohmmeter (megger). Measure resistance to ground on each motor winding and cable phase. Infinite resistance is normal. Any measurable resistance indicates a ground fault requiring cable or motor replacement.
6. **Check the speed reference signal** if using an external analog input on terminals 53/54. Use a multimeter to verify the signal is stable and within the expected range (typically 0-10V or 4-20mA).
7. **Adjust parameter 4-106** (Tracking Error Trip Level) as a temporary diagnostic test. Increase the value slightly and re-test. If the fault clears but motor performance is poor, the underlying cause is still present and must be corrected rather than masked.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor output cable (shielded VFD-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-78-fault-code&k=Motor+output+cable+%28shielded+VFD-rated%29&tag=errorcodefixes-20) \| Replace if a ground fault is found in the cable insulation during megger testing. |
| Three-phase AC motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-78-fault-code&k=Three-phase+AC+motor&tag=errorcodefixes-20) \| Replace if motor windings show a ground fault or if mechanical damage (seized bearings, damaged rotor) is confirmed. |

## When to Call a Pro

Call a qualified electrician or VFD technician if you are not trained to work with three-phase industrial power or variable frequency drives. Diagnosing AL-78 requires measuring line voltages, testing motor insulation with a megohmmeter, and editing drive parameters. Incorrect settings can damage the motor or drive. A professional will isolate whether the fault is in the drive configuration, the power supply, the motor, or the mechanical load, and will have the tools to perform insulation resistance testing and phase imbalance measurements. If a ground fault or motor winding failure is confirmed, the technician can safely replace cables or the motor and verify proper operation under load.

**Rough cost:** A pro service call runs about $200-800 depending on root cause.
