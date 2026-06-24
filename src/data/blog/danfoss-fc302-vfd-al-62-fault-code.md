---
title: "Danfoss FC302 AL-62 - Causes & Fix"
description: "AL-62 means output frequency hit its max limit. Most often the max frequency parameter is set too low. Raise parameter 4-01 to match speed needs."
pubDatetime: 2026-06-22T10:16:19Z
modDatetime: 2026-06-22T10:16:19Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 input rectifier assembly"
most_likely_cause: "Maximum frequency parameter set lower than required speed reference"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Check Parameter 4-01 (Maximum Frequency) and verify it is set at or above the required speed reference"
  - "Measure input voltage across all three phases and confirm imbalance is below 3%"
  - "Compare the speed reference displayed on the LCP against the max frequency setting to see if the reference exceeds the limit"
no_buy_pct: "85%"
---

## Danfoss FC302 AL-62 — What It Means

AL-62 (Warning 62) on the Danfoss FC302 VFD indicates the drive's output frequency has reached the value programmed in the maximum frequency parameter, typically Parameter 4-01 or 4-18. The controller cannot increase frequency further to meet the speed reference. This is a warning, not a trip alarm, so the motor usually continues running at the programmed ceiling rather than stopping. Unlike overcurrent or overvoltage faults, AL-62 reflects a control logic limit rather than a hardware failure.

The warning persists as long as the system demands a higher speed than the configured maximum allows. It can also appear when input voltage is low or imbalanced, causing the drive to restrict performance to protect the motor or DC bus. The code does not signal a catastrophic fault but tells you the drive is clamped at its programmed limit.

## Before You Replace Anything

Technicians sometimes replace the power board or control board when AL-62 appears, but the warning is nearly always a parameter or input voltage issue. Check Parameter 4-01 and measure input phase voltage imbalance before ordering any hardware.

[Jump to Fix](#fix)

## Common Causes

- **Maximum frequency parameter too low (~60%)** Parameter 4-01 or 4-18 is set below the speed reference, so the drive clamps output frequency at the programmed ceiling and issues the warning.
- **Speed reference higher than limit (~20%)** An analog or digital reference signal from a PLC, potentiometer, or control panel exceeds the configured maximum frequency.
- **Low input voltage (~10%)** Supply voltage falls significantly below nominal, causing the drive to limit output frequency to protect the motor or DC bus.
- **Voltage imbalance or missing phase (~8%)** Input phase imbalance greater than 3% or a lost input phase forces the drive to restrict performance and hit the internal frequency limit.
- **Faulty input rectifier or fuse (~2%)** A blown input fuse or failed rectifier assembly drops one phase, creating imbalance and triggering the frequency limit.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the LCP show the speed reference is higher than Parameter 4-01?</summary>
<div class="dtree-body"><strong>Yes:</strong> The reference exceeds the max limit. Raise Parameter 4-01 to match your required speed or lower the reference signal.<br><strong>No:</strong> The parameter is not the blocker. Measure input voltage across all three phases to check for imbalance or low supply.</div>
</details>

<details class="dtree"><summary>Is input phase voltage imbalance greater than 3%?</summary>
<div class="dtree-body"><strong>Yes:</strong> Imbalance is forcing the drive to restrict frequency. Check for a blown fuse, loose wire, or facility supply issue.<br><strong>No:</strong> Input power is balanced. Test with motor disconnected to see if the warning clears at no load, pointing to a load or mechanical issue.</div>
</details>

<details class="dtree"><summary>Does the warning clear when the motor is disconnected?</summary>
<div class="dtree-body"><strong>Yes:</strong> The issue is mechanical overload or motor current limits. Inspect the driven load and verify motor nameplate matches drive settings.<br><strong>No:</strong> The problem is internal to the drive parameters or power board. Review all frequency and limit parameters or contact a VFD technician.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Check Parameter 4-01 (Maximum Frequency)** in the drive menu and verify it matches or exceeds the required operating speed for your application (typically 50.0 Hz or 60.0 Hz).
2. **Compare the speed reference** displayed on the LCP against the maximum frequency setting to confirm the reference is not above the programmed limit.
3. **Measure input voltage** across L1-L2, L2-L3, and L1-L3 using a voltmeter and calculate the percent difference between phases.
4. **Verify voltage imbalance is below 3%** of nominal supply voltage. If imbalance exceeds 3%, inspect incoming power, check for blown fuses, and test the input contactor.
5. **Inspect all input wiring** and connections at the drive terminals. Tighten any loose wires and look for signs of corrosion or damage.
6. **Disconnect the motor** and run the drive at no load. If AL-62 clears, the issue is mechanical overload or motor current limits rather than drive parameters.
7. **Adjust Parameter 4-01** to the correct maximum frequency if it was set too low, then reset the warning and test the drive under normal load conditions.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 input rectifier assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-62-fault-code&k=Danfoss+FC302+input+rectifier+assembly&tag=errorcodefixes-20) \| Only if a phase is missing and the rectifier diodes test shorted or open. |
| Danfoss FC302 control board (IGBT driver card) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-62-fault-code&k=Danfoss+FC302+control+board+%28IGBT+driver+card%29&tag=errorcodefixes-20) \| Rarely needed for AL-62. Replace only after confirming all parameters and input power are correct. |

## When to Call a Pro

Call a VFD technician if you are not comfortable working with 400V or 480V three-phase power, measuring high voltage at the input terminals, or navigating the parameter menu on the LCP. A technician should also handle any replacement of the input rectifier assembly or control board, since those repairs require safe lockout/tagout procedures and knowledge of the drive's internal DC bus. If free checks and parameter adjustments do not clear the warning, or if you see signs of internal arcing or blown components, get professional help before powering the drive again.

**Rough cost:** A pro service call runs about $150-400.

## See Also

- [Danfoss FC302 ALARM 33 - Causes & Fix](/posts/danfoss-fc302-alarm-33-fault-code/)
- [Danfoss FC302 VFD Alarm 80 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-80-fault-code/)
- [Danfoss FC302 Alarm 14 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-14-fault-code/)
- [Danfoss FC302 AL-68 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-68-fault-code/)
