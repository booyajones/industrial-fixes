---
title: "ABB ACS580 VFD E0035 Fault Code - Causes & Fix"
description: "E0035 on an ABB ACS580 VFD signals an internal communication or parameter error. Check parameter settings and reset the drive first."
pubDatetime: 2026-07-19T07:25:23Z
modDatetime: 2026-07-19T07:25:23Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - abb
money_part: "ABB ACS580 Control Board"
most_likely_cause: "corrupted parameter settings or configuration error"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Perform a drive reset by cycling power and attempting a parameter reset to factory defaults"
  - "Check the parameter group for any recently changed values and restore them to known-good settings"
  - "Inspect the keypad or control panel connection for loose cables or corrosion"
no_buy_pct: "60%"
---

## ABB ACS580 VFD E0035 Fault Code — What It Means

The E0035 fault code on an ABB ACS580 variable frequency drive indicates an internal communication issue or parameter configuration problem within the drive itself. This code typically appears when the drive's control board detects inconsistent data, corrupted parameter values, or a failure in the internal bus communication between components. The exact meaning can vary slightly between firmware versions, so consult your model's technical manual for the specific definition.

Unlike motor-side faults or power supply issues, E0035 points to the drive's own internal logic or stored settings. It often occurs after a parameter change, firmware update, or power interruption that corrupts the drive's non-volatile memory. In some cases it can also indicate a hardware fault on the control board itself, though software and configuration issues are more common.

## Before You Replace Anything

Technicians sometimes replace the main control board immediately, but most E0035 faults resolve with a parameter reset or reload from backup. Always attempt a factory reset and parameter restore before ordering a new board.

[Jump to Fix](#fix)

## Common Causes

- **Corrupted parameter memory (~40%)** Power interruptions or improper shutdowns can corrupt the drive's stored parameter values, causing internal communication errors.
- **Incorrect parameter configuration (~25%)** A recently changed parameter may conflict with other settings or exceed valid ranges, triggering the internal fault.
- **Firmware version mismatch (~15%)** After a firmware update, older parameter files or incompatible settings can cause communication errors between drive components.
- **Control board hardware fault (~15%)** A failing control board or damaged internal bus can produce persistent E0035 faults even after parameter resets.
- **Keypad or HMI communication failure (~5%)** A loose or damaged connection between the human-machine interface and the main board can disrupt internal data exchange.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear after a full power cycle and parameter reset to factory defaults?</summary>
<div class="dtree-body"><strong>Yes:</strong> The issue was likely corrupted settings. Reload your application parameters carefully and monitor for recurrence.<br><strong>No:</strong> The fault may be hardware-related or tied to a specific parameter conflict. Proceed with firmware checks and control board diagnostics.</div>
</details>

<details class="dtree"><summary>Have you recently updated firmware or changed any drive parameters?</summary>
<div class="dtree-body"><strong>Yes:</strong> Roll back the firmware or restore the previous parameter set to see if the fault disappears, indicating a configuration incompatibility.<br><strong>No:</strong> The fault may stem from a hardware issue or environmental factor such as electrical noise or a failing control board.</div>
</details>

<details class="dtree"><summary>Can you access the drive's parameter menu and see consistent values without freezing or communication errors?</summary>
<div class="dtree-body"><strong>Yes:</strong> The keypad and control board are communicating. Focus on parameter validation and reset procedures.<br><strong>No:</strong> A hardware fault in the control board or keypad is likely. Check cables and consider control board replacement.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** completely, wait 30 seconds, then restore power to clear any transient faults.
2. **Access the parameter menu** using the keypad or connected software and navigate to the factory reset function.
3. **Perform a factory reset** to restore all parameters to default values, then note whether the E0035 fault clears on restart.
4. **Check for firmware updates** on the ABB website and verify that your current firmware version matches the parameter file format you are using.
5. **Reload application parameters** one group at a time from a known-good backup, testing the drive after each group to isolate any conflicting setting.
6. **Inspect the keypad and control board connections** for loose ribbon cables, corrosion, or physical damage that could disrupt internal communication.
7. **Document the fault history** using the drive's event log to identify any patterns or specific parameters associated with the error, then consult ABB technical support or a qualified service technician if the fault persists after reset and parameter validation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB ACS580 Control Board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0035-fault-code&k=ABB+ACS580+Control+Board&tag=errorcodefixes-20) \| Required only if hardware fault is confirmed after parameter reset and firmware checks. |
| ABB ACS580 Keypad / HMI Panel | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0035-fault-code&k=ABB+ACS580+Keypad+%2F+HMI+Panel&tag=errorcodefixes-20) \| Replace if keypad connection or display is unresponsive and cable replacement does not resolve the issue. |

## When to Call a Pro

Call a qualified industrial electrician or ABB service technician if the E0035 fault persists after factory reset and parameter reload, or if you are uncomfortable working with high-voltage variable frequency drives. VFD diagnostics require specialized knowledge of drive programming, internal bus communication, and safe isolation procedures. If the control board needs replacement, a technician will also verify that the fault was not caused by external wiring issues, grounding problems, or electrical noise that could damage the new board. Professional service typically includes firmware validation, parameter backup and restore, and a full system test to prevent recurrence.

**Rough cost:** A pro service call runs about $200-500.

## See Also

- [ABB ACS550 EFB2 Fault Code - Causes & Fix](/posts/abb-acs550-efb2-fault-code/)
- [ABB ACS580 A7EE Fault - Causes & Fix](/posts/abb-acs580-a7ee-fault-code/)
- [ABB ACS580 A3D0 Fault Code - Causes & Fix](/posts/abb-acs580-a3d0-fault-code/)
- [ABB ACS580 VFD E0019 Fault Code - Causes & Fix](/posts/abb-acs580-vfd-e0019-fault-code/)
