---
title: "Yaskawa GA800 A.118 Fault - Causes & Fix"
description: "A.118 is a non-fault alarm on the GA800 VFD. Check your manual's alarm table for the exact meaning, then verify wiring and option cards."
pubDatetime: 2026-06-08T11:14:10Z
modDatetime: 2026-06-08T11:14:10Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
diy_or_pro: "pro"
---

## Yaskawa GA800 A.118 Fault — What It Means

A.118 on a Yaskawa GA800 is a non-fault alarm code, not a hardware trip fault. The exact meaning must be verified against the GA800 alarm list for your specific manual revision. On Yaskawa drives, an alarm code is typically shown with the ALM indicator flashing, whereas a fault is more severe and requires the issue to be removed before reset. The GA800 troubleshooting material distinguishes alarms from faults in this way. Because the exact A.118 definition is not available in standard manufacturer excerpts, consult your GA800 manual's alarm table to confirm whether it relates to configuration, communication, an option card, or another setting-related condition.

For GA800 alarm-type issues in general, common technician checks start with wiring, option cards, motor and drive compatibility, and whether the drive is correctly initialized and configured. Yaskawa's installation guidance specifically says to verify model code, correct drive selection, and drive and motor compatibility in multi-drive systems. If A.118 is a configuration or communication-related alarm, the general Yaskawa troubleshooting pattern is to check option card seating, signal wiring, connector condition, and the associated setup parameters.

## Before You Replace Anything

Technicians sometimes replace the control board or option card before checking connector seating and wiring. Reseat the option card and inspect all connectors and signal cables first, which costs nothing and resolves many alarm codes.

[Jump to Fix](#fix)

## Common Causes

- **Loose or unseated option card (~30%)** Communication and option cards in the GA800 can work loose during shipment or vibration, triggering setting-related alarms.
- **Damaged signal wiring or connectors (~25%)** Broken pins, corroded terminals, or damaged cable runs between the drive and external devices can cause configuration and communication alarms.
- **Incorrect drive or motor compatibility (~20%)** In multi-drive systems or after replacement, a drive model mismatch or motor parameter error can trigger an alarm during initialization.
- **Missing or incorrect parameter setup (~15%)** If the drive has not been correctly initialized or a critical parameter is out of range, a setting-related alarm may appear.
- **Communication network fault (~10%)** If the drive is networked via an option card, bus errors or device address conflicts can generate alarms.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is an option card (communication or I/O module) installed in the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> Power down the drive, reseat the option card firmly in its slot, inspect the connector pins for damage, and restore power. If the alarm clears, the card was loose.<br><strong>No:</strong> The alarm is likely configuration or wiring related. Check all signal-cable connections at the drive terminals for tightness and correct wiring per the diagram.</div>
</details>

<details class="dtree"><summary>Does the alarm clear after you press RESET on the keypad?</summary>
<div class="dtree-body"><strong>Yes:</strong> The cause was transient or has been corrected. Monitor the drive during operation to confirm it does not return.<br><strong>No:</strong> The underlying condition is still present. Review the drive nameplate and model code to verify the catalog code matches your application, and consult the GA800 alarm table in your manual.</div>
</details>

<details class="dtree"><summary>Has the drive or motor been recently replaced or moved?</summary>
<div class="dtree-body"><strong>Yes:</strong> Verify drive and motor compatibility in the installation manual, check that all parameter settings match the new equipment, and confirm the model code in the C/C section on the nameplate.<br><strong>No:</strong> Inspect for physical damage, loose connectors, or environmental changes (vibration, temperature, moisture) that may have disrupted wiring or the option card.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Identify the exact code and state.** Confirm whether the display shows an alarm or a fault and record the code exactly as shown on the keypad.
2. **Check the drive nameplate and model code.** Verify the catalog code in the C/C section matches the installed unit and application requirements.
3. **Inspect for obvious physical issues.** Look for missing parts, shipping damage, loose connectors, and damaged wiring at the drive terminals and motor connection.
4. **Review wiring and compatibility.** Confirm drive and motor compatibility, especially if multiple drives are present in the system, and verify all signal-cable connections against the wiring diagram.
5. **Check option boards and communications hardware.** Power down the drive, reseat the option card, inspect connectors and pins for corrosion or damage, and verify cabling and device setup if a communication network is installed.
6. **Correct the cause, then reset.** Remove the cause of the alarm and then press RESET on the keypad while the code is displayed.
7. **If the code returns, contact support.** Document the serial number, model and spec number, fault or alarm code, and application details before contacting Yaskawa technical support for the exact A.118 definition and advanced troubleshooting.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 option card (communication or I/O module) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-118-fault-code&k=Yaskawa+GA800+option+card+%28communication+or+I%2FO+module%29&tag=errorcodefixes-20) \| Match the part number to your installed option kit and application protocol. |
| Yaskawa GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-118-fault-code&k=Yaskawa+GA800+control+board&tag=errorcodefixes-20) \| Only if diagnostics confirm board failure after wiring and option card checks. |

## When to Call a Pro

Call a qualified VFD technician or system integrator if you are not familiar with industrial drive wiring, communication networks, or parameter programming. Variable-frequency drives operate at high DC bus voltages (up to 800 VDC on the GA800) and incorrect wiring or parameter changes can damage motors and machinery. A professional can consult the GA800 alarm table for your specific manual revision, perform continuity and insulation-resistance tests on signal cables, verify option-card firmware and configuration, and make sure drive and motor parameters match your application. If the alarm returns after reset and basic checks, document the drive nameplate data and contact Yaskawa technical support or an authorized service center for model-specific diagnostics.

**Rough cost:** A pro service call runs about $150-400 for diagnostic visit and configuration check, more if an option card or board requires replacement.
