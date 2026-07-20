---
title: "ABB ACS580 VFD E0004 Fault Code - Causes & Fix"
description: "E0004 indicates an overcurrent or short-circuit fault on an ABB ACS580 VFD. Check motor connections and verify proper parameters."
pubDatetime: 2026-07-18T07:38:31Z
modDatetime: 2026-07-18T07:38:31Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - abb
money_part: "VFD-rated shielded motor cable"
most_likely_cause: "Motor cable or connection issues"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect all motor cable connections for tightness and signs of arcing or damage"
  - "Check that motor nameplate data matches drive parameter settings"
  - "Review event log for fault history pattern"
---

## ABB ACS580 VFD E0004 Fault Code — What It Means

The E0004 fault code on an ABB ACS580 variable frequency drive signals an overcurrent condition or short-circuit event detected during motor operation. The drive's protective circuitry has sensed current levels exceeding safe operating limits, which can occur during start-up, steady-state running, or sudden load changes.

This fault triggers an immediate shutdown to protect both the drive and the connected motor from damage. The root cause may lie in the motor circuit, drive parameters, mechanical load, or the drive hardware itself. Clearing the fault and resuming operation requires identifying and correcting the underlying condition that caused the overcurrent event.

## Before You Replace Anything

Many technicians replace the drive power module when the fault stems from incorrect parameter settings or loose motor connections. Always inspect all three motor lead terminations and review acceleration time and current limit parameters before replacing drive components.

[Jump to Fix](#fix)

## Common Causes

- **Loose or damaged motor cable connections (~30%)** Poor terminations at the drive output or motor terminal box create intermittent contact, arcing, and voltage spikes that the drive interprets as overcurrent.
- **Incorrect drive parameter settings (~25%)** Acceleration time set too short, current limit set too low, or motor nameplate data entered incorrectly causes the drive to trip on normal starting current.
- **Motor winding short or ground fault (~20%)** Insulation breakdown inside the motor creates a low-impedance path that draws excessive current whenever the drive attempts to energize the motor.
- **Mechanical overload or seized bearing (~15%)** A jammed load, seized pump bearing, or blocked fan forces the motor to draw locked-rotor current that exceeds the drive's programmed limits.
- **Drive output stage failure (~7%)** Failed IGBT modules or gate driver circuits within the drive produce unbalanced or distorted output waveforms that trigger overcurrent protection.
- **Incorrect motor cable type or length (~3%)** Using unshielded cable, excessive cable length, or cable not rated for VFD duty increases capacitive charging current and reflected wave effects.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault occur immediately on start, or only after the motor has been running?</summary>
<div class="dtree-body"><strong>Yes:</strong> Immediate faults point to motor cable issues, winding shorts, or incorrect parameters. Inspect connections and verify parameter settings.<br><strong>No:</strong> Faults during running suggest mechanical overload, thermal issues, or intermittent connection problems. Check the driven load and measure motor current.</div>
</details>

<details class="dtree"><summary>Can you measure motor winding resistance and verify it is balanced across all three phases?</summary>
<div class="dtree-body"><strong>Yes:</strong> If resistance is balanced and within datasheet range, focus on drive parameters and cable integrity. If unbalanced or low, the motor winding is likely at fault.<br><strong>No:</strong> Without a resistance check you cannot rule out a motor fault. Arrange for megohmmeter testing before replacing the drive.</div>
</details>

<details class="dtree"><summary>Does the drive event log show overcurrent on all three phases or just one?</summary>
<div class="dtree-body"><strong>Yes:</strong> Single-phase overcurrent suggests a phase-specific issue such as a loose connection, cable fault, or motor winding problem on that leg.<br><strong>No:</strong> All-phase overcurrent points to a load problem, incorrect current limit parameter, or drive output stage failure affecting the entire inverter bridge.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** to the drive and follow lockout/tagout procedures before touching any terminals or opening any panels.
2. **Record all parameter settings** by capturing a screenshot or writing down the current configuration so you can restore settings if needed.
3. **Inspect motor cable terminations** at both the drive output terminals and the motor terminal box, tightening all connections to the manufacturer's specified torque.
4. **Measure motor winding resistance** phase-to-phase and phase-to-ground using a megohmmeter to detect shorts, opens, or insulation breakdown.
5. **Verify drive parameter settings** by comparing motor nameplate voltage, current, frequency, and speed against the values programmed in the drive's motor data menu.
6. **Check acceleration and deceleration times** and lengthen them if they are unusually short, allowing the motor more time to ramp without drawing peak current.
7. **Review current limit parameters** and confirm they are set above the motor's full-load current rating by an appropriate margin, typically 110 to 150 percent.
8. **Clear the fault** using the drive keypad or parameter reset command, then attempt a test run under no-load or light-load conditions to isolate mechanical factors.
9. **Monitor real-time current display** on the drive during start-up and running to identify whether current spikes correlate with mechanical events or remain constant.
10. **Consult the drive event log** to determine fault frequency and any patterns that suggest intermittent connections or load cycling issues.
11. **Replace damaged motor cable** if inspection reveals nicks, burns, or insulation damage, using shielded VFD-rated cable of appropriate gauge and length.
12. **Contact a qualified electrician or drive technician** if resistance tests, parameter changes, and cable repairs do not resolve the fault, as internal drive repair or motor rewind may be required.

## Parts Often Needed

| Part | Notes |
|------|-------|
| VFD-rated shielded motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0004-fault-code&k=VFD-rated+shielded+motor+cable&tag=errorcodefixes-20) \| Use cable rated for inverter duty with appropriate gauge for motor current and distance; consult your drive manual for maximum recommended length. |
| Motor terminal lugs and connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0004-fault-code&k=Motor+terminal+lugs+and+connectors&tag=errorcodefixes-20) \| Replace any corroded or burned crimp lugs or compression connectors found during inspection. |

## When to Call a Pro

Call a qualified electrician or drive specialist if you lack the tools to measure motor winding resistance and insulation, if parameter adjustments and connection checks do not clear the fault, or if the drive continues to trip under no-load conditions. Internal drive failures require bench testing and component-level repair that is not safe or practical for most facility staff. A professional can perform detailed current signature analysis, verify gate driver operation, and determine whether the drive inverter section or motor windings need repair or replacement.

**Rough cost:** A pro service call runs about $200-800.

## See Also

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS580 A4A2 - Causes & Fix](/posts/abb-acs580-vfd-a4a2-fault-code/)
- [ABB ACS580 A4A1 Fault - Causes & Fix](/posts/abb-acs580-vfd-a4a1-fault-code/)
- [ABB ACS880 Fault 2310 Overcurrent — Causes & Fix](/posts/abb-acs880-fault-2310-overcurrent/)
