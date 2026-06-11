---
title: "Yaskawa GA800 E85 Fault - Causes & Fix"
description: "E85 on the GA800 is not documented in standard Yaskawa manuals. Check the alarm history screen for the full text and contact Yaskawa support."
pubDatetime: 2026-06-07T10:22:41Z
modDatetime: 2026-06-07T10:22:41Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
diy_or_pro: "pro"
money_part: "Yaskawa GA800 control board (PCB)"
---

## Yaskawa GA800 E85 Fault — What It Means

The E85 fault code does not appear in the verified Yaskawa GA800 maintenance or troubleshooting documentation available from the manufacturer. Yaskawa publishes a specific alarm code list for the GA800 in its user and maintenance manuals, and E85 is not identified in those resources. It is possible that the code is being misread from the keypad, that it is a custom parameter alarm configured by the integrator, or that it appears differently in the drive's alarm history. Yaskawa troubleshooting guidance stresses reading the elementary diagram and verifying the exact alarm code and description before taking corrective action.

Because the exact meaning of E85 cannot be confirmed from manufacturer sources, attempting repair without the correct fault definition risks replacing the wrong component or missing the actual problem. The GA800 maintenance manual states that it covers only fan and control board replacement and does not address more complex internal repairs. Always record the full alarm text from the drive's alarm history menu and have the model number, specification code, and serial number ready when contacting Yaskawa technical support.

## Before You Replace Anything

Technicians sometimes replace the control board or power section without verifying the fault code meaning in the alarm history. Always write down the full alarm text from the drive's menu and cross-check it against the GA800 user manual fault table before ordering parts.

[Jump to Fix](#fix)

## Common Causes

- **Misread or custom alarm** The code may be a user-configured parameter alarm or a display misread that does not match standard Yaskawa fault codes.
- **Alarm history needed** The keypad may show a shortened version of the fault, and the full description is only visible in the drive's alarm history menu.
- **Firmware or parameter mismatch** Custom firmware or application-specific parameter sets can generate non-standard alarm codes not listed in the base manual.
- **Display or keypad error** A failing keypad or corrupted display can show incomplete or incorrect fault codes that do not correspond to the internal alarm log.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drive's alarm history menu show a different code or additional text beyond E85?</summary>
<div class="dtree-body"><strong>Yes:</strong> Write down the full alarm description and look it up in the GA800 user manual fault table, then follow the manufacturer's corrective action for that specific code.<br><strong>No:</strong> The code may not be standard. Proceed to check the parameter list for custom alarms or contact Yaskawa support with your drive's model and serial number.</div>
</details>

<details class="dtree"><summary>Is the drive still running, or is it faulted and stopped?</summary>
<div class="dtree-body"><strong>Yes:</strong> If the drive is running, E85 may be a warning rather than a trip. Check the alarm log to see if it is logged as a fault or an informational message.<br><strong>No:</strong> If the drive is tripped and will not restart, do not attempt to clear the fault repeatedly. Power down, record all alarm history entries, and consult the manual or Yaskawa support before re-energizing.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and the upstream disconnect to make sure the system is safe before inspecting the keypad or accessing alarm menus.
2. **Re-energize the drive** and immediately navigate to the alarm history menu using the keypad. Record the full text of every alarm entry, including any additional codes or descriptions.
3. **Compare the alarm text** to the fault code table in the GA800 user manual or the electronic manual file. If E85 does not appear, note the closest match or any custom parameter alarms.
4. **Check the elementary diagram** supplied with the drive or the machine documentation to see if E85 is referenced as a custom interlock or external fault input.
5. **Gather the drive nameplate data**, including the full model number, specification code, and serial number, and contact Yaskawa technical support or your distributor with the alarm history printout.
6. **Do not replace the control board or power section** until Yaskawa support confirms the fault definition and the corrective action, since the GA800 maintenance manual states it does not cover repairs beyond fan and control board replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e85-fault-code&k=Yaskawa+GA800+control+board+%28PCB%29&tag=errorcodefixes-20) \| Only order after Yaskawa support confirms the fault points to a board failure and provides the correct board part number for your drive's specification. |
| Yaskawa GA800 cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e85-fault-code&k=Yaskawa+GA800+cooling+fan&tag=errorcodefixes-20) \| The maintenance manual lists fan replacement as a field-serviceable task, but an E85 code is not a documented fan alarm. |

## When to Call a Pro

Call a qualified Yaskawa service technician or distributor when the alarm code cannot be found in the user manual, when the drive will not restart after a fault reset, or when the alarm history shows multiple simultaneous faults. The GA800 maintenance and troubleshooting manual explicitly states that it does not cover repairs beyond fan and control board replacement, so any work involving the power section, DC bus, or internal wiring must be performed by trained personnel. Yaskawa technical support requires the drive's model number, specification code, serial number, and the exact alarm history text to provide accurate guidance, so have that information ready before calling.

**Rough cost:** A pro service call runs about $200-500.
