---
title: "Danfoss FC302 AL-150 Fault - Causes & Fix"
description: "AL-150 is not a standard Danfoss FC302 fault code. Most likely you are seeing Alarm 13 (overcurrent from motor overload or bad parameters)."
pubDatetime: 2026-06-25T09:35:52Z
modDatetime: 2026-06-25T09:35:52Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 IGBT module"
most_likely_cause: "Mechanical overload on the motor shaft or incorrect motor parameter settings"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify parameter 1-24 (Nominal Motor Current) matches the motor nameplate rating exactly"
  - "Check that all cooling fans are running and vents are clear of dust and obstructions"
  - "Inspect motor cable connections at the drive and motor for loose or corroded terminals"
---

## Danfoss FC302 AL-150 Fault — What It Means

There is no official AL-150 fault code documented in the Danfoss FC302 VFD alarm table. The FC302 uses alarm numbers 1 through 80, and AL-150 does not appear in manufacturer documentation. You may be seeing Alarm 13 (Overcurrent), which indicates the drive output current exceeded safe thresholds (typically 150 to 160 percent of nominal motor current for several seconds). This is not an instantaneous short circuit but a gradual overcurrent buildup from overload or component problems.

If your display shows "AL:38" followed by a secondary number like 150, that secondary code is an internal diagnostic sub-code defined in the FC302 Operating Instructions table 6.1. Alarm 38 is an internal fault that requires professional interpretation. If you are reading Alarm 13, the drive is protecting itself from sustained high current caused by mechanical overload, incorrect motor parameter settings, or failing components in the motor or drive itself.

## Before You Replace Anything

Technicians often replace IGBT modules before checking motor parameters and mechanical load. Verify parameter 1-24 (Nominal Motor Current) matches the motor nameplate and disconnect the motor to test if the alarm persists unloaded before ordering drive components.

[Jump to Fix](#fix)

## Common Causes

- **Mechanical overload on the motor (~35%)** A jammed pump, seized bearing, or stuck load forces the motor to draw excessive current during operation or acceleration.
- **Incorrect motor parameter settings (~25%)** Parameter 1-24 (Nominal Motor Current) set too high or motor data parameters 1-20 through 1-25 not matching the actual motor causes the drive to allow dangerous current levels.
- **Partial motor winding short or insulation breakdown (~15%)** Aging motor windings develop internal shorts or insulation failures that create unbalanced current draw and overcurrent trips.
- **Loose or corroded motor cable connections (~10%)** Poor connections create resistance and current spikes that trigger the overcurrent protection.
- **Aging or damaged IGBT modules (~10%)** Failed or degraded IGBT modules in the drive lose the ability to regulate current properly and trip on overcurrent.
- **Insufficient cooling airflow (~5%)** Blocked vents or failed cooling fans cause thermal stress on IGBTs and internal components, leading to current regulation failure.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the alarm clear when you disconnect the motor and run the drive unloaded?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem is external to the drive (motor, load, or wiring). Check motor connections, test motor windings for balance, and inspect the mechanical load.<br><strong>No:</strong> The drive has an internal component failure (IGBT modules, DC bus, or control board). Call a Danfoss-certified technician for drive repair or replacement.</div>
</details>

<details class="dtree"><summary>Are all three motor cable phases tight and free of corrosion at both the drive and motor terminals?</summary>
<div class="dtree-body"><strong>Yes:</strong> Wiring is not the cause. Move to motor parameter verification and mechanical load testing.<br><strong>No:</strong> Clean and tighten all motor terminals. Corroded or loose connections cause current spikes and overcurrent trips.</div>
</details>

<details class="dtree"><summary>Is parameter 1-24 set exactly to the motor nameplate current rating?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor parameters are correct. Focus on mechanical load and motor winding health.<br><strong>No:</strong> Set parameter 1-24 to match the motor nameplate current exactly, then run Automatic Motor Adaptation (AMA) in parameter 129 to recalibrate.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the system** and lock out the disconnect, then wait at least five minutes for the DC bus capacitors to discharge fully before opening the drive or touching any terminals.
2. **Verify the displayed alarm** in the FC302 control panel and write down the exact alarm number and any secondary codes shown in the alarm log history menu.
3. **Check motor parameters** by navigating to parameter 1-24 (Nominal Motor Current) and confirming it matches the motor nameplate rating, then verify parameters 1-20 through 1-25 are set correctly for your motor.
4. **Disconnect the motor** from the drive output terminals and reset the alarm, then attempt to run the drive unloaded in hand mode to determine if the fault is internal to the drive or external in the motor and load.
5. **Inspect motor wiring** by checking all three motor cable connections at both the drive output and motor terminal box for tightness, corrosion, and damage, then measure motor winding resistance across all three phases to verify balanced windings.
6. **Check cooling and ventilation** by confirming all drive cooling fans are running, cleaning dust and debris from vents and heat sinks, and verifying the drive is not mounted in an enclosed space without adequate airflow.
7. **Run Automatic Motor Adaptation** by setting parameter 129 and allowing the drive to recalibrate motor thermal and electrical characteristics if you have corrected motor parameters or replaced the motor.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 IGBT module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-150-fault-code&k=Danfoss+FC302+IGBT+module&tag=errorcodefixes-20) \| Requires model-specific part number from drive nameplate and professional installation with thermal compound and torque specs |
| Danfoss FC302 cooling fan assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-150-fault-code&k=Danfoss+FC302+cooling+fan+assembly&tag=errorcodefixes-20) \| Match fan voltage and connector type to your drive serial number |

## When to Call a Pro

Call a Danfoss-certified VFD technician if the alarm persists with the motor disconnected, which indicates internal drive failure. Professional help is also needed if you lack the metering equipment to safely measure motor winding resistance and DC bus voltage, or if internal component testing reveals failed IGBT modules or DC bus capacitors. High-voltage work inside the drive requires specialized training and safety procedures. If you are unfamiliar with VFD parameter programming or do not have access to the FC302 Operating Instructions for your specific drive model, a technician can verify motor settings and run diagnostics using Danfoss MCT software.

**Rough cost:** A pro service call runs about $300-900.

## See Also

- [Danfoss FC302 VFD Alarm 46 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-46-fault-code/)
- [Danfoss FC302 AL-64 - Causes & Fix](/posts/danfoss-fc302-vfd-al-64-fault-code/)
- [Danfoss FC302 ALARM 45 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-45-fault-code/)
- [Danfoss FC302 AL-111 - Causes & Fix](/posts/danfoss-fc302-vfd-al-111-fault-code/)
