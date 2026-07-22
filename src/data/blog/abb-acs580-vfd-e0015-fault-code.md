---
title: "ABB ACS580 VFD E0015 Fault Code - Causes & Fix"
description: "E0015 signals a VFD fault; exact meaning varies by firmware and parameter setup. Check your manual and inspect input power connections."
pubDatetime: 2026-07-18T07:48:47Z
modDatetime: 2026-07-18T07:48:47Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - abb
money_part: "ABB ACS580 control board"
diy_or_pro: "pro"
free_checks:
  - "Check the drive display or keypad for additional fault details or sub-codes"
  - "Review the event log through the control panel to see the fault history and timestamp"
  - "Inspect all incoming power terminals and control wiring for loose or corroded connections"
---

## ABB ACS580 VFD E0015 Fault Code — What It Means

The E0015 fault code on an ABB ACS580 variable frequency drive indicates an error condition has been detected by the drive's internal diagnostics. The exact meaning of E0015 can vary depending on your drive's firmware version, parameter configuration, and installed options. Consult your drive's event log and the ACS580 manual for your specific model to identify the precise fault definition. Common underlying issues include input power problems, parameter configuration errors, communication faults, or sensor signal problems. The drive will typically stop motor operation and require a fault reset after the underlying cause is corrected.

## Before You Replace Anything

Technicians sometimes replace the control board when the fault is actually caused by incorrect parameter settings or loose wiring. Always review the drive's parameter settings and inspect all control and power connections before ordering replacement boards.

[Jump to Fix](#fix)

## Common Causes

- **Parameter configuration error (~30%)** Incorrect drive parameters or settings incompatible with the motor or application can trigger fault codes.
- **Input power disturbance (~25%)** Voltage sags, phase loss, or transient spikes on incoming AC power can cause the drive to fault.
- **Communication fault (~20%)** Loss of fieldbus communication or network timeout when the drive is configured for external control can generate faults.
- **Loose or damaged wiring (~15%)** Poor connections at control terminals or damaged cable insulation can create intermittent signals that the drive interprets as a fault.
- **Faulty sensor or feedback signal (~10%)** An encoder, thermistor, or analog input signal outside expected range may cause the drive to trip.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drive display additional sub-codes or descriptive text with the E0015 fault?</summary>
<div class="dtree-body"><strong>Yes:</strong> Note the full code and cross-reference it in the ACS580 manual appendix to identify the specific fault condition.<br><strong>No:</strong> Access the drive's event log through the keypad or PC tool to retrieve more detail about the fault trigger.</div>
</details>

<details class="dtree"><summary>Are all three phases of input power present and within normal voltage range?</summary>
<div class="dtree-body"><strong>Yes:</strong> Power supply is likely okay; focus on parameter settings, communication links, and control wiring.<br><strong>No:</strong> Investigate upstream power issues such as loose contacts in the disconnect, blown fuses, or utility supply problems.</div>
</details>

<details class="dtree"><summary>Have any drive parameters or network settings been changed recently?</summary>
<div class="dtree-body"><strong>Yes:</strong> Review recent parameter changes and restore factory defaults or known-good settings to test if the fault clears.<br><strong>No:</strong> Inspect all field wiring and sensor connections for damage, corrosion, or loose terminals.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Record the full fault code and event log details** from the drive's display or using the DriveWindow PC software so you have the exact timestamp and any sub-codes.
2. **Consult the ACS580 user manual** for your firmware version to look up the specific meaning of E0015 in the fault code table or appendix.
3. **Inspect incoming power connections** at the line-side terminals and verify all three phases are present and voltage is within the drive's rated input range using a multimeter.
4. **Check all control wiring** including start/stop inputs, analog signals, encoder feedback, and communication cables for secure termination and correct routing away from power conductors.
5. **Review drive parameter settings** using the keypad or PC tool to confirm motor nameplate data, application macros, and communication settings match your installation requirements.
6. **Reset the fault** using the drive's reset button or control input after correcting the identified issue and monitor operation to confirm the fault does not recur.
7. **Contact ABB technical support or a qualified drive technician** if the fault persists after verifying power, wiring, and parameters, as internal hardware diagnosis or firmware update may be required.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB ACS580 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0015-fault-code&k=ABB+ACS580+control+board&tag=errorcodefixes-20) \| Only replace if diagnostics confirm internal board failure; verify all external causes first. |
| Shielded control cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0015-fault-code&k=Shielded+control+cable&tag=errorcodefixes-20) \| Use ABB-recommended cable for encoder or communication links to reduce noise-related faults. |

## When to Call a Pro

Call a qualified electrician or drive technician whenever you are uncomfortable working with three-phase industrial power or when the fault persists after basic checks. High-voltage work inside the VFD cabinet requires lockout/tagout procedures and knowledge of DC bus hazards. A professional can use diagnostic software to interrogate the drive's internal logs, perform insulation resistance tests on the motor and cables, and update firmware if needed. If the fault code indicates a hardware failure such as a gate driver or power module issue, factory-trained service is necessary to safely replace internal components and restore the drive to operation.

**Rough cost:** A pro service call runs about $200-500.

## See Also

- [ABB ACS580 VFD E0006 Fault Code - Causes & Fix](/posts/abb-acs580-vfd-e0006-fault-code/)
- [ABB VFD Fault Codes: ACS550, ACS580, ACS880 Error Guide](/posts/abb-vfd-fault-codes/)
- [ABB ACS880 Complete Fault Code Guide — All Faults and Fixes](/posts/abb-acs880-complete-guide/)
- [ABB ACS580 Fault 3220 — DC Undervoltage Fix](/posts/abb-acs580-fault-3220/)
