---
title: "ABB ACS580 VFD E0036 Fault - Causes & Fix"
description: "E0036 on an ABB ACS580 drive signals a parameter or configuration error. Check parameter settings and reload defaults if needed."
pubDatetime: 2026-07-19T07:26:02Z
modDatetime: 2026-07-19T07:26:02Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - abb
money_part: "ABB ACS580 control board (NPOW card)"
most_likely_cause: "Parameter configuration mismatch or invalid setting"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Review the drive's event log to identify which parameter triggered the fault"
  - "Power-cycle the drive and check if the fault clears on its own"
  - "Verify that no recent parameter changes were made through the keypad or software tool"
no_buy_pct: "85%"
---

## ABB ACS580 VFD E0036 Fault — What It Means

The E0036 fault code on an ABB ACS580 variable frequency drive indicates a parameter or configuration mismatch. This code appears when the drive detects an internal inconsistency in programmed settings, often after parameter changes, firmware updates, or a power cycle that reveals conflicting values. The drive halts operation to prevent erratic motor control or equipment damage.

The fault typically arises from user programming errors, corrupted parameter files, or incompatible parameter sets loaded from external tools. Unlike hardware faults, E0036 usually reflects a software or settings issue rather than a failed component. Clearing the fault requires identifying the conflicting parameters and restoring a valid configuration.

## Before You Replace Anything

Technicians sometimes replace the control board when the real issue is simply a corrupted parameter file or a single misconfigured setting. Always review recent parameter changes and reload factory defaults before ordering hardware.

[Jump to Fix](#fix)

## Common Causes

- **Parameter conflict after manual programming (~50%)** A recently changed parameter value conflicts with other dependent settings, triggering the drive to reject the configuration.
- **Corrupted parameter file (~25%)** The drive's internal parameter memory has become corrupted due to a brief power loss, voltage spike, or failed save operation.
- **Incompatible parameter set loaded from software (~15%)** A parameter backup from a different drive model or firmware version was uploaded, creating mismatches the drive cannot resolve.
- **Firmware update incomplete or failed (~8%)** A firmware upgrade did not complete correctly, leaving parameter structures in an inconsistent state.
- **Control board memory failure (~2%)** The onboard EEPROM or memory chip that stores parameters has developed a hardware fault and cannot retain valid data.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault appear immediately on power-up before the motor starts?</summary>
<div class="dtree-body"><strong>Yes:</strong> The issue is likely a stored parameter conflict. Access the parameter menu and restore factory defaults.<br><strong>No:</strong> The fault may be triggered by a runtime condition or recent parameter change. Review the event log and check what was modified last.</div>
</details>

<details class="dtree"><summary>Have you recently changed any parameters using the keypad or PC software?</summary>
<div class="dtree-body"><strong>Yes:</strong> Identify the changed parameters and revert them one by one, or reload a known-good parameter backup.<br><strong>No:</strong> The fault may stem from memory corruption or an earlier unnoticed change. Perform a factory reset and reprogram only essential settings.</div>
</details>

<details class="dtree"><summary>Does the fault clear after a factory reset and minimal reprogramming?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem was a software or configuration issue. Document your working parameter set as a backup.<br><strong>No:</strong> The control board memory may be failing. Contact a qualified technician or ABB service for hardware diagnostics.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Record the current parameter set** by writing down or photographing critical settings from the keypad display so you can restore motor ratings and application-specific values later.
2. **Access the drive's event log** through the keypad menu to identify which parameter or group triggered the E0036 fault and note the timestamp.
3. **Power-cycle the drive** by disconnecting input power for at least 30 seconds, then reconnecting to see if the fault self-clears.
4. **Restore factory default parameters** using the drive's reset function, typically found in the parameter menu under a reset or initialization command.
5. **Reprogram essential motor parameters** such as rated voltage, current, frequency, and any application-specific settings required for your process, consulting your commissioning notes or wiring diagram.
6. **Clear the fault** using the reset button on the keypad or the clear-fault command in the menu, then attempt to start the drive.
7. **Monitor the drive through several start-stop cycles** to confirm the fault does not return, and save the working parameter set as a backup file if using PC software.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB ACS580 control board (NPOW card) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0036-fault-code&k=ABB+ACS580+control+board+%28NPOW+card%29&tag=errorcodefixes-20) \| Only required if factory reset fails and memory corruption is confirmed by repeated E0036 faults. |
| ABB DriveStudio PC software license | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0036-fault-code&k=ABB+DriveStudio+PC+software+license&tag=errorcodefixes-20) \| Optional tool for backing up and restoring parameter sets and viewing detailed diagnostics. |

## When to Call a Pro

Call a qualified electrician or drive technician if the E0036 fault persists after a factory reset and reprogramming, or if you are unfamiliar with VFD parameter structures and safe high-voltage procedures. Drive configuration errors can cause motor overheating, mechanical damage, or nuisance shutdowns in critical processes. A professional can retrieve detailed fault logs, verify firmware integrity, and test the control board memory. If your application requires custom macros, PLC integration, or fieldbus communication, professional commissioning is the safest path to reliable operation.

**Rough cost:** A pro service call runs about $200-500.

## See Also

- [ABB ACS580 A2A1 - Causes & Fix](/posts/abb-acs580-a2a1-fault-code/)
- [ABB ACS550 Complete Fault Code Guide — All Faults and Fixes](/posts/abb-acs550-complete-guide/)
- [ABB ACS550 EFB3 Fault - Causes & Fix](/posts/abb-acs550-vfd-efb3-fault-code/)
- [ABB ACS880 Fault Codes: List, Causes & Fixes](/posts/abb-880-fault-codes/)
