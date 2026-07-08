---
title: "Danfoss FC302 AL-59 Fault - Causes & Fix"
description: "AL-59 is a Current Limit warning: motor current exceeds parameter 4-18. Most often caused by incorrect motor data or load too high."
pubDatetime: 2026-06-23T09:55:34Z
modDatetime: 2026-06-23T09:55:34Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Three-phase AC motor"
most_likely_cause: "Incorrect motor nameplate data entered in parameters 1-20 to 1-25"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify motor nameplate voltage, current, frequency, speed, and power are entered exactly as shown on the motor label in parameters 1-20 to 1-25"
  - "Check parameter 4-18 (Current Limit) and compare it to the motor's rated full-load current to see if the limit is set too low for your application"
  - "Inspect all three input power connections for loose terminals or blown fuses"
no_buy_pct: "60%"
---

## Danfoss FC302 AL-59 Fault — What It Means

Alarm 59 on a Danfoss FC302 is a Current Limit warning. It means the motor output current has exceeded the threshold set in parameter 4-18 (Current Limit). Unlike a hard trip, this is typically a warning that allows the drive to continue running, though it can be configured to trip if the condition persists. The drive detects that the actual output current is higher than your configured limit, which is often set to protect the motor or process from excessive current during acceleration, overload, or specific operating conditions.

This warning does not always indicate a fault in the drive itself. It can be triggered by incorrect parameter settings, mechanical overload, motor problems, or power supply issues. The drive is functioning correctly by alerting you that the current draw is beyond what you told it to allow.

## Before You Replace Anything

Technicians often replace the drive or motor without first checking that parameter 4-18 is set correctly for the application and that motor nameplate data in parameters 1-20 to 1-25 matches the actual motor. A simple parameter review and clamp-on ammeter measurement can identify the real problem.

[Jump to Fix](#fix)

## Common Causes

- **Incorrect motor data (~35%)** Motor nameplate parameters (1-20 to 1-25) are set incorrectly, causing the drive to calculate and limit current improperly for the actual motor.
- **Current limit set too low (~25%)** Parameter 4-18 is set below the motor's actual full-load current requirement, triggering a false warning during normal operation.
- **Excessive mechanical load (~20%)** Failing motor bearings, a jammed mechanism, improper sheave or gear sizing, or other mechanical issues force the motor to draw too much current.
- **Motor or cable insulation failure (~12%)** Moisture, contamination, thermal aging in motor windings, or damaged cable insulation (from rodents, sharp conduit edges, or wear) creates a short or high-resistance fault that increases current draw.
- **Input power issues (~8%)** Loose input connections, blown fuses, or voltage sags can cause the drive to draw higher current to compensate for poor power quality.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Do parameters 1-20 to 1-25 match the motor nameplate exactly (voltage, current, frequency, speed)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor data is correct. Move on to check parameter 4-18 and measure actual motor current with a clamp meter.<br><strong>No:</strong> Incorrect motor data is likely causing the warning. Enter the correct nameplate values, reset the drive, and test. If the warning clears, the problem is solved.</div>
</details>

<details class="dtree"><summary>Does the motor run smoothly with no unusual noise or vibration when disconnected from the load?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor and drive are functioning. The problem is likely excessive mechanical load (bearings, jam, sheave sizing). Inspect the driven equipment.<br><strong>No:</strong> The motor or motor cable may be faulty. Perform a megohm insulation test on the motor windings and inspect the cable for damage.</div>
</details>

<details class="dtree"><summary>Is the measured motor current (using a clamp meter on all three phases) close to or exceeding the value set in parameter 4-18?</summary>
<div class="dtree-body"><strong>Yes:</strong> The warning is accurate. Either increase parameter 4-18 if the application requires higher current, or reduce the mechanical load on the motor.<br><strong>No:</strong> The drive may be reading current incorrectly (rare), or there is a transient power or logic issue. Check input power quality and reset the drive.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Check motor nameplate data** in parameters 1-20 to 1-25 (motor voltage, current, frequency, speed, power). Compare each setting to the actual motor label and correct any mismatches.
2. **Review parameter 4-18 (Current Limit)**. If it is set below the motor's rated full-load current or the application's normal operating current, increase it to a safe value for your system.
3. **Measure actual motor current** using a clamp-on ammeter on all three output phases (U, V, W). Compare the reading to the drive's display to confirm the drive is reading correctly.
4. **Disconnect the motor from the load** and run the drive. If the warning clears, the issue is mechanical (failing bearings, jammed mechanism, improper sheave sizing). Inspect and repair the driven equipment.
5. **Test motor and cable integrity**. Disconnect the motor cable from the drive output terminals and run the drive. If the warning clears, perform a megohm insulation test on the motor windings to ground. Readings below 2 megohms indicate insulation failure. Inspect cables for damage from rodents, sharp conduit edges, or wear.
6. **Verify input power quality**. Measure voltage between all three input phases and check that imbalance is less than 3 percent. Inspect all input connections for loose terminals, blown fuses, or signs of voltage sag.
7. **Check drive cooling**. Inspect all cooling fans and vents for obstructions. Clean any dust buildup and confirm adequate ambient airflow around the drive enclosure.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Three-phase AC motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-59-fault-code&k=Three-phase+AC+motor&tag=errorcodefixes-20) \| Only if insulation testing shows winding failure or the motor is mechanically seized. |
| Motor power cable (three-conductor shielded) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-59-fault-code&k=Motor+power+cable+%28three-conductor+shielded%29&tag=errorcodefixes-20) \| Only if cable insulation is damaged or megohm test shows a fault in the cable run. |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not trained to work with three-phase power and VFD parameter programming. This code requires systematic troubleshooting with a clamp-on ammeter, megohm tester, and knowledge of motor data entry. If the warning persists after verifying parameters and you suspect a motor or mechanical fault, a technician with vibration analysis tools and insulation test equipment can pinpoint bearing failure, winding shorts, or cable damage. Do not attempt to increase parameter 4-18 beyond the motor's rated current without understanding the mechanical and thermal limits of your system.

**Rough cost:** A pro service call runs about $150-400 depending on whether the fix is parameter adjustment, motor replacement, or mechanical repair.

## See Also

- [Danfoss FC302 Alarm 26 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-26-fault-code/)
- [Danfoss FC302 VFD Alarm 28 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-28-fault-code/)
- [Danfoss FC302 ALARM 28 - Causes & Fix](/posts/danfoss-fc302-alarm-28-fault-code/)
- [Danfoss VFD Fault UL — Causes & Fix](/posts/danfoss-vfd-fault-ul/)
