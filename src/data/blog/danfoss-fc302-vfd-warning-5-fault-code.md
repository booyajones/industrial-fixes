---
title: "Danfoss FC302 VFD WARNING 5 - Causes & Fix"
description: "WARNING 5 on a Danfoss FC302 VFD signals a drive condition that needs attention. Check your manual for the exact meaning and reset."
pubDatetime: 2026-07-20T07:27:39Z
modDatetime: 2026-07-20T07:27:39Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 control board"
diy_or_pro: "pro"
free_checks:
  - "Check the drive display or keypad for the event log to see what triggered WARNING 5"
  - "Verify that all motor and power connections are tight and that no terminals show signs of overheating"
  - "Review recent changes to load or operating speed that might push the motor closer to a programmed warning threshold"
---

## Danfoss FC302 VFD WARNING 5 — What It Means

WARNING 5 on a Danfoss FC302 variable frequency drive indicates that the drive has detected a condition that does not yet require a full shutdown but needs operator attention. The exact meaning of WARNING 5 varies by firmware version and parameter configuration on the FC302. It can represent a range of conditions from motor overload approaching a trip threshold to communication warnings or custom user-defined alerts. Because Danfoss allows programmable warning thresholds and custom fault assignments, you must consult your specific FC302 manual or the drive's parameter list to identify what WARNING 5 represents in your installation. The drive will typically continue to operate under a warning condition but may reduce performance or log the event for review.

## Before You Replace Anything

Technicians sometimes replace the main control board when WARNING 5 appears, but the warning is often a threshold or parameter setting issue. Check the drive's event log and parameter settings first to identify the exact trigger before ordering any hardware.

[Jump to Fix](#fix)

## Common Causes

- **Motor current approaching overload threshold (~30%)** The drive monitors motor current and will issue a warning when load current climbs near the programmed overload trip point, often due to mechanical binding or increased process load.
- **DC bus voltage deviation (~20%)** Incoming supply voltage that drifts outside the acceptable range can trigger a voltage warning before the drive trips on overvoltage or undervoltage fault.
- **Communication timeout or network error (~15%)** If the drive is configured for network control and loses contact with the master controller, it may log a communication warning depending on parameter settings.
- **Motor temperature sensor nearing limit (~15%)** When a motor thermistor or PT100 sensor is wired to the drive and the reading climbs toward the programmed warning level, the drive will issue an early alert.
- **Custom parameter warning set by installer (~10%)** The FC302 allows users to define custom warning conditions tied to analog inputs, speed limits, or other monitored parameters, so WARNING 5 may be a site-specific alert.
- **Drive internal temperature elevated (~10%)** Restricted airflow or high ambient temperature can cause the drive heatsink to warm above the warning threshold, signaling that cooling may be inadequate.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drive display show an event log or alarm history that explains WARNING 5?</summary>
<div class="dtree-body"><strong>Yes:</strong> Note the logged parameter or condition and cross-reference it in the FC302 manual to understand the threshold that was crossed.<br><strong>No:</strong> Access the drive menu and navigate to the alarm history or status parameters to retrieve the stored event code.</div>
</details>

<details class="dtree"><summary>Has the motor load or operating speed changed recently?</summary>
<div class="dtree-body"><strong>Yes:</strong> Increased load or prolonged high-speed operation may be pushing motor current or temperature toward warning limits; verify parameter settings match the new duty cycle.<br><strong>No:</strong> Check for mechanical issues such as bearing wear or belt tension that could raise motor current without a change in setpoint.</div>
</details>

<details class="dtree"><summary>Are supply voltage and all power connections stable and clean?</summary>
<div class="dtree-body"><strong>Yes:</strong> The warning is likely related to motor, communication, or temperature monitoring rather than incoming power.<br><strong>No:</strong> Measure incoming line voltage under load and inspect all power terminals for looseness or corrosion that could cause voltage sags.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power** to the VFD at the disconnect or circuit breaker and follow lockout-tagout procedures before opening the enclosure or accessing terminals.
2. **Access the drive display** or connect a programming tool to view the event log and identify the exact parameter or condition that triggered WARNING 5.
3. **Consult the FC302 manual** for your firmware version to decode the warning number and locate the associated parameter group and threshold setting.
4. **Inspect all motor and power wiring** for tight connections, signs of overheating, or damaged insulation that could introduce noise or voltage drop.
5. **Check the motor** for mechanical binding, bearing noise, or abnormal temperature that would explain elevated current or thermal readings.
6. **Review parameter settings** related to overload, voltage limits, communication timeout, and any custom warnings to make sure they match your application and motor nameplate data.
7. **Clear the warning** from the drive menu or by cycling power, then monitor operation to see if the warning recurs under normal load.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-warning-5-fault-code&k=Danfoss+FC302+control+board&tag=errorcodefixes-20) \| Only required if diagnostics confirm a hardware fault; most WARNING 5 events are parameter or wiring issues. |
| Motor thermistor or PT100 sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-warning-5-fault-code&k=Motor+thermistor+or+PT100+sensor&tag=errorcodefixes-20) \| Replace if the sensor reads erratically or is shorted, triggering false temperature warnings. |

## When to Call a Pro

Call a qualified electrician or drives technician if you are not familiar with VFD programming, high-voltage three-phase wiring, or parameter configuration. WARNING 5 often requires interpreting the drive's event log and adjusting threshold settings to match motor and load characteristics. A technician with Danfoss training can quickly identify whether the warning points to a real overload condition, a communication setup error, or a parameter that needs recalibration. Professional service is also required if the drive shows signs of internal component damage or if the motor itself needs electrical or mechanical evaluation.

**Rough cost:** A pro service call runs about $150-400.

## See Also

- [Danfoss FC302 Alarm 51 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-51-fault-code/)
- [Danfoss FC302 AL-99 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-99-fault-code/)
- [Danfoss FC302 AL-107 Fault Code - Causes & Fix](/posts/danfoss-fc302-vfd-al-107-fault-code/)
- [Danfoss FC302 AL-147 - Causes & Fix](/posts/danfoss-fc302-vfd-al-147-fault-code/)
