---
title: "Lennox SLP98V Error Codes — Variable-Speed Furnace Fault Guide"
description: "Lennox SLP98V error codes: iComfort fault codes, flash codes, and variable-speed blower faults for the 98% AFUE SLP98V furnace."
pubDatetime: 2026-04-22T16:00:00Z
modDatetime: 2026-04-22T16:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - lennox
---

## Lennox SLP98V Error Codes — What It Means

The Lennox SLP98V is a two-stage, variable-speed, 98% AFUE gas furnace — one of the most efficient residential furnaces available. It uses the iComfort thermostat communication system and displays detailed fault codes on the thermostat screen rather than simple flash codes. It can also be diagnosed via the control board's LED for technicians without the thermostat.

[Jump to Fix](#fix)

## iComfort Fault Code Quick Reference

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Meaning | Priority | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |---------|---------|
| 103 | [Rollout switch lockout](https://www.amazon.com/s?k=Rollout%20switch%20lockout&tag=errorcodefixe-20) | Critical |
| [204](https://www.amazon.com/s?k=204&tag=errorcodefixe-20) | Ignition lockout | High | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 223 | High-limit open | [Medium](https://www.amazon.com/s?k=Medium&tag=errorcodefixe-20) |  | 225 | [Flame rollout switch open](https://www.amazon.com/s?k=Flame%20rollout%20switch%20open&tag=errorcodefixe-20) | Critical |
| [231](https://www.amazon.com/s?k=231&tag=errorcodefixe-20) | Gas valve fault | Critical | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 292 | Variable-speed blower fault | [Medium](https://www.amazon.com/s?k=Medium&tag=errorcodefixe-20) |  | 327 | [Pressure switch stuck closed](https://www.amazon.com/s?k=Pressure%20switch%20stuck%20closed&tag=errorcodefixe-20) | Medium |
| [332](https://www.amazon.com/s?k=332&tag=errorcodefixe-20) | Inducer motor fault | High | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 411 | Flame sensed without call | [Critical](https://www.amazon.com/s?k=Critical&tag=errorcodefixe-20) |  | 412 | [Flame failure](https://www.amazon.com/s?k=Flame%20failure&tag=errorcodefixe-20) | High |
| [432](https://www.amazon.com/s?k=432&tag=errorcodefixe-20) | Communication fault | Medium | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 434 | Blower motor (ECM) fault | [Medium](https://www.amazon.com/s?k=Medium&tag=errorcodefixe-20) |  | 540 | [Control board fault](https://www.amazon.com/s?k=Control%20board%20fault&tag=errorcodefixe-20) | High |

## SLP98V-Specific Issues

### Code 292: Variable-Speed Blower Fault
The SLP98V uses a Lennox proprietary ECM variable-speed blower motor. Unlike standard ECM motors, the SLP98V motor communicates speed commands digitally with the control board. Common failure modes: motor module failure (the motor control box attached to the motor frame), motor winding failure, or communication harness issues.

**Diagnosis:** The SLP98V motor should ramp from ~30% speed on low-demand calls up to 100% on high heat. If the motor starts but doesn't modulate, or starts slowly and stalls, the motor module is likely failing. Lennox offers the motor module as a separate replacement part — you don't always need to replace the full motor assembly.

### Code 223: High Limit on a 98% Furnace
High limit trips on the SLP98V are especially common when the variable-speed blower operates at low speed settings in high-static ductwork. If the installer set the motor to "minimum static" mode but the duct system has high resistance, the blower doesn't move enough air. A technician can repogram the static pressure setpoint via the iComfort installer menu.

### Code 204: Ignition Lockout
The SLP98V ignition sequence uses a two-stage gas valve with a hot-surface igniter. On failed ignition, check: gas supply valve open, verify 24V at the gas valve terminals on a call for heat, and inspect the igniter. Lennox SLP98V uses a silicon nitride igniter rated 40–90 ohms cold.

### Code 432: Communication Fault
The SLP98V communicates across a 2-wire proprietary bus between the furnace board and the iComfort thermostat. Verify the communication wire is connected at both the thermostat base and the furnace board (usually labeled "COMM" or "BUS"). A loose terminal is the most common cause.

### Code 103: Rollout Switch Lockout
The rollout switch has tripped and the board has exceeded the maximum reset attempts. On the SLP98V, a 10-minute manual lockout applies. Identify the root cause before resetting — common causes include a plugged flue, cracked secondary heat exchanger (rare on new units), or excess gas pressure.

## Step-by-Step Fix {#fix}

**For code 292 (variable-speed blower):**
1. Power off the furnace.
2. Inspect the motor harness connectors — two harnesses connect to the ECM motor module. Unplug and re-seat both.
3. Restore power and attempt a heat call. Observe whether the blower starts and ramps.
4. If the motor hums but doesn't spin, the run capacitor in the motor module may have failed.
5. If the motor doesn't respond at all, test for 120V at the motor line voltage connector.
6. If power is present and the motor still doesn't run, replace the motor module.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [ECM motor module](https://www.amazon.com/s?k=ECM%20motor%20module&tag=errorcodefixe-20) | Lennox 100392-03 or model-specific |
| [Igniter](https://www.amazon.com/s?k=Igniter&tag=errorcodefixe-20) | Lennox 65J6301 |
| [Control board](https://www.amazon.com/s?k=Control%20board&tag=errorcodefixe-20) | Lennox 100390-09 (match to unit label) |
| [Rollout switch](https://www.amazon.com/s?k=Rollout%20switch&tag=errorcodefixe-20) | Lennox 19J6801 |

## When to Call a Pro
The SLP98V's variable-speed ECM motor and iComfort communication system require installer-level diagnostics for anything beyond cleaning and filter replacement. Code 103 (rollout lockout) and code 411 (flame without call) require licensed technician attention before restart.
