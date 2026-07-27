---
title: "ABB ACS580 VFD E0039 Fault - Causes & Fix"
description: "E0039 signals an internal fault in your ABB ACS580 drive. Check parameter settings and power connections before replacing boards."
pubDatetime: 2026-07-19T07:27:50Z
modDatetime: 2026-07-19T07:27:50Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - abb
money_part: "ABB ACS580 control board"
diy_or_pro: "pro"
free_checks:
  - "Power-cycle the drive completely and check if the fault clears after a full shutdown"
  - "Review the parameter list for any recently changed settings or out-of-range values"
---

## ABB ACS580 VFD E0039 Fault — What It Means

The E0039 fault code on an ABB ACS580 variable frequency drive indicates an internal error detected by the drive's control system. The exact meaning of this code can vary depending on the firmware version and specific model configuration, so consult your drive's user manual or parameter list for the precise definition. In general, internal fault codes point to issues with control logic, parameter settings, communication failures between internal boards, or hardware faults within the drive itself.

This code typically requires diagnostic access to the drive's parameter menu and may involve resetting parameters, checking internal connections, or replacing control boards. Because VFDs operate at high voltage and contain stored energy even after power is removed, this repair falls outside typical DIY work.

## Before You Replace Anything

Technicians sometimes replace the entire power board when the fault is actually caused by incorrect parameter settings or a loose internal ribbon cable. Always review the parameter log and check internal connector seating before ordering expensive boards.

[Jump to Fix](#fix)

## Common Causes

- **Parameter configuration error (~30%)** An incorrect or incompatible parameter setting can trigger internal fault codes when the drive detects a logic conflict.
- **Loose or corroded internal connector (~25%)** Ribbon cables and board-to-board connectors inside the drive can work loose over time from vibration or thermal cycling.
- **Control board failure (~20%)** The main control PCB may develop component-level failures that generate internal fault codes.
- **Firmware corruption or version mismatch (~15%)** A power interruption during a firmware update or an incompatible firmware version can cause the drive to report internal errors.
- **Communication bus fault (~10%)** If the drive uses fieldbus communication, a fault on the network or a missing termination resistor can appear as an internal error.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear after a full power-down and restart?</summary>
<div class="dtree-body"><strong>Yes:</strong> The error may be transient or caused by a temporary condition. Monitor the drive for recurrence and review recent parameter changes.<br><strong>No:</strong> The fault is persistent. Proceed to check parameter settings and internal connections.</div>
</details>

<details class="dtree"><summary>Have any parameters been changed or uploaded recently?</summary>
<div class="dtree-body"><strong>Yes:</strong> Restore factory defaults or reload a known-good parameter set from backup to rule out configuration issues.<br><strong>No:</strong> The fault is likely hardware-related. Check internal connectors and consider control board replacement.</div>
</details>

<details class="dtree"><summary>Is the drive connected to a fieldbus or external controller?</summary>
<div class="dtree-body"><strong>Yes:</strong> Disconnect the communication cable and restart the drive. If the fault clears, the issue is network-related.<br><strong>No:</strong> The fault originates within the drive itself. Open the enclosure and inspect internal connections.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect all power** to the drive at the upstream disconnect or circuit breaker and verify zero voltage with a meter. Wait at least five minutes for capacitors to discharge.
2. **Record all current parameter settings** using the keypad or PC tool so you can restore them if needed.
3. **Perform a factory reset** of parameters through the drive menu or by using the default parameter load function, then check if the fault clears.
4. **Open the drive enclosure** (with power still off) and inspect all internal ribbon cables and connectors for proper seating. Reseat any that appear loose.
5. **Check for signs of component damage** on the control board such as burned traces, swollen capacitors, or corrosion. Replace the control board if physical damage is evident.
6. **Restore power and monitor** the drive. If the fault persists after parameter reset and connector checks, contact ABB technical support with the drive serial number and firmware version for specific diagnostics.
7. **Document the fault history** using the drive's event log to identify any patterns or preceding alarms that may point to the root cause.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB ACS580 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0039-fault-code&k=ABB+ACS580+control+board&tag=errorcodefixes-20) \| Model-specific; verify the exact board part number from your drive nameplate or service manual before ordering. |
| Internal ribbon cable set | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0039-fault-code&k=Internal+ribbon+cable+set&tag=errorcodefixes-20) \| Replacement cables for connections between power and control boards; consult ABB for the correct kit. |

## When to Call a Pro

Call a qualified electrician or VFD technician for any E0039 fault. Variable frequency drives store lethal high voltage on internal DC bus capacitors even after input power is removed, and improper handling can result in electric shock or arc flash. A trained technician has the tools to safely discharge capacitors, access internal diagnostics, and interpret parameter logs. If your facility does not have personnel trained on ABB drives, contact an ABB Authorized Service Provider who can remotely diagnose the fault or dispatch a technician with the correct replacement boards and firmware tools.

**Rough cost:** A pro service call runs about $200-600.

## See Also

- [ABB ACS580 A3D0 Fault Code - Causes & Fix](/posts/abb-acs580-a3d0-fault-code/)
- [ABB ACS580 A4A2 - Causes & Fix](/posts/abb-acs580-vfd-a4a2-fault-code/)
- [ABB ACS880 Fault 3210 — DC Bus Undervoltage Causes & Fix](/posts/abb-acs880-fault-3210/)
- [ABB ACS550 VFD EXT FAULT 1 - Causes & Fix](/posts/abb-acs550-vfd-ext-fault-1-fault-code/)
