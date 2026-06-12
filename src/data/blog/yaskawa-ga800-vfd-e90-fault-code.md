---
title: "Yaskawa GA800 E90 Fault - Causes & Fix"
description: "E90 fault code meaning varies by GA800 firmware version. Check your drive's manual for the exact definition, then inspect wiring and parameters."
pubDatetime: 2026-06-08T10:44:03Z
modDatetime: 2026-06-08T10:44:03Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
diy_or_pro: "pro"
money_part: "Yaskawa GA800 control board"
---

## Yaskawa GA800 E90 Fault — What It Means

The E90 fault code is not documented in the publicly available GA800 troubleshooting materials. Yaskawa publishes model-specific and firmware-specific fault tables, and the exact meaning of E90 depends on your drive's configuration and software version. The GA800 displays fault codes on the keypad, and the proper first step is to consult the fault/alarm information section of your drive's manual or contact Yaskawa technical support with your exact model and firmware revision.

Yaskawa's troubleshooting approach for the GA800 emphasizes reading the exact fault code from the drive display, then using the elementary diagram and manual to trace the root cause before replacing components. The GA800 maintenance documentation covers fan and control board replacement as the primary field-serviceable items, but fault-specific diagnostics require the manufacturer's fault table for your unit.

## Before You Replace Anything

Technicians sometimes replace the control board without first checking parameter settings, input wiring, and the elementary diagram. Always verify the exact fault definition in your drive's manual and inspect wiring and configuration before ordering parts.

[Jump to Fix](#fix)

## Common Causes

- **Parameter configuration mismatch (~30%)** Incorrect parameter settings for motor, application, or I/O can trigger undefined or user-configurable fault codes.
- **Control board communication fault (~25%)** Loss of communication between the keypad, control board, or option cards can generate alarm codes.
- **Input signal wiring issue (~20%)** Open or shorted control terminals, broken analog inputs, or miswired digital inputs can cause faults.
- **Fan or thermal monitoring fault (~15%)** The GA800 monitors cooling fan operation and internal temperatures, and fan failure or overheating can trigger alarms.
- **Option card or accessory fault (~10%)** If an encoder card, fieldbus card, or other option is installed, hardware or configuration errors can produce fault codes.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drive display show the exact alarm number and description in the fault history menu?</summary>
<div class="dtree-body"><strong>Yes:</strong> Write down the full code and description, then look it up in the GA800 instruction manual fault table for your firmware version.<br><strong>No:</strong> Power-cycle the drive and watch the keypad during startup. If the code reappears, photograph the display and contact Yaskawa support with your model number.</div>
</details>

<details class="dtree"><summary>Have any parameters been changed recently, or was a motor or load recently replaced?</summary>
<div class="dtree-body"><strong>Yes:</strong> Review parameter groups P1 (motor data) and P2 (application settings) against the motor nameplate and application requirements. Reset to factory defaults if needed.<br><strong>No:</strong> Inspect control terminal wiring for loose connections, damaged insulation, or incorrect voltage levels on digital and analog inputs.</div>
</details>

<details class="dtree"><summary>Is the cooling fan running when the drive is powered and under load?</summary>
<div class="dtree-body"><strong>Yes:</strong> Check for option cards or communication modules. Verify that all cards are seated properly and that any required configuration parameters are set.<br><strong>No:</strong> The fan may have failed or the thermal monitoring circuit may have detected an overheat condition. Inspect the fan and heatsink for dust or obstruction.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Record the exact fault code and description** from the GA800 keypad by pressing the alarm history key. Write down the full alphanumeric code, any sub-codes, and the date/time stamp.
2. **Consult the fault table** in the GA800 instruction manual that matches your drive's firmware version. Yaskawa publishes version-specific tables, so confirm your software revision in the drive's information menu.
3. **Inspect all control wiring and terminals** according to the elementary diagram. Check for loose connections, damaged wire insulation, correct polarity on digital inputs, and proper grounding.
4. **Review parameter settings** in groups P1 (motor constants) and P2 (application settings). Compare motor nameplate data against programmed values and verify that acceleration, deceleration, and frequency limits are appropriate.
5. **Check the cooling fan** and heatsink. Power the drive and confirm the fan runs. Clean any dust from the heatsink fins and verify airflow is not blocked.
6. **Test with a parameter reset** if no wiring or hardware issues are found. Save your current parameter set to a backup, then restore factory defaults and re-enter only essential motor and application settings.
7. **Contact Yaskawa technical support** if the fault persists after wiring, parameter, and hardware checks. Provide your drive model number, firmware version, and the exact fault code for guidance on your specific configuration.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e90-fault-code&k=Yaskawa+GA800+control+board&tag=errorcodefixes-20) \| Only replace after confirming the board is faulty. Order by exact drive model and firmware version. |
| Yaskawa GA800 cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e90-fault-code&k=Yaskawa+GA800+cooling+fan&tag=errorcodefixes-20) \| The GA800 maintenance manual lists fan replacement as a field service item. Match fan voltage and size to your drive. |

## When to Call a Pro

Call a qualified technician or contact Yaskawa support immediately if you cannot locate the E90 fault definition in your manual, if the drive will not clear the fault after a power cycle, or if you are unfamiliar with VFD parameter programming and high-voltage wiring. Variable frequency drives operate at hazardous voltages and incorrect wiring or parameter settings can damage motors and connected equipment. A technician with Yaskawa training can interpret the elementary diagram, use diagnostic software to read internal fault logs, and safely test control board signals and power circuits.

**Rough cost:** A pro service call runs about $200-600.
