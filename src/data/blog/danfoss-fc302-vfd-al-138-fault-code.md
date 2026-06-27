---
title: "Danfoss FC302 AL-138 Fault - Causes & Fix"
description: "AL-138 does not exist on FC302 drives. You likely have Alarm 38 (Internal Fault), usually a control board or memory error needing replacement."
pubDatetime: 2026-06-25T09:25:40Z
modDatetime: 2026-06-25T09:25:40Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 Control PCB (I/O Control Card)"
most_likely_cause: "Control board (I/O control card) failure"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power cycle the drive: turn off, wait 5 minutes for capacitors to discharge, then power on again"
  - "Reseat all option cards and internal wiring connections after disconnecting power"
  - "Check input voltage balance across all three phases (must be within 3% difference)"
part_price: "$150-400"
---

## Danfoss FC302 AL-138 Fault — What It Means

The Danfoss FC302 does not have an AL-138 fault code in its official alarm table. The most likely intended code is Alarm 38 (Internal Fault), which indicates an internal hardware or software failure that does not fit other specific categories. Alarm 38 typically points to a communication failure between internal boards, a control board component breakdown, memory corruption, or firmware errors. When triggered, the drive displays a sub-code to specify the exact internal problem.

This alarm often appears after power transients, improper option card installation, or aging control electronics. The drive cannot operate until the underlying fault is cleared, which usually requires component replacement rather than a simple reset.

## Before You Replace Anything

Technicians sometimes replace the entire inverter module when Alarm 38 appears, but most cases are control board failures. Always check the sub-code and reseat option cards before ordering expensive inverter parts.

[Jump to Fix](#fix)

## Common Causes

- **Control board component failure (~45%)** Gate driver circuits or memory chips on the I/O control PCB break down from age, heat, or voltage spikes.
- **Memory or parameter corruption (~25%)** Damaged parameter memory or firmware errors prevent the drive from reading internal settings correctly.
- **Loose or incompatible option cards (~15%)** Poorly seated option cards or internal wiring disconnects interrupt communication between boards.
- **Power transient damage (~10%)** Voltage spikes or surges damage sensitive control components on the PCB.
- **Inverter module communication fault (~5%)** The control card cannot communicate properly with the inverter IGBT module.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drive display a sub-code number after Alarm 38?</summary>
<div class="dtree-body"><strong>Yes:</strong> Write down the sub-code and consult Table 6.1 in the FC302 Operating Instructions to identify the specific fault, then proceed with targeted component testing.<br><strong>No:</strong> The sub-code may not have registered. Power cycle the drive and check again. If no sub-code appears, assume a general control board fault.</div>
</details>

<details class="dtree"><summary>Does the fault clear after a power cycle and option card reseat?</summary>
<div class="dtree-body"><strong>Yes:</strong> The issue was likely a temporary communication glitch or loose card. Monitor the drive for recurring faults.<br><strong>No:</strong> The fault is persistent hardware damage. Proceed to control board or inverter module replacement.</div>
</details>

<details class="dtree"><summary>Is the input voltage balanced within 3% across all three phases?</summary>
<div class="dtree-body"><strong>Yes:</strong> The power supply is acceptable. Focus diagnostics on the control board and internal components.<br><strong>No:</strong> Correct the phase imbalance first. Unbalanced input voltage can trigger internal faults and damage components.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** and lockout the drive. Wait at least 5 minutes for DC bus capacitors to discharge before opening the enclosure.
2. **Record the sub-code** displayed with Alarm 38. Consult Table 6.1 in the FC302 Operating Instructions to identify the specific internal fault.
3. **Reseat all option cards** by removing and firmly reinstalling each card. Check that internal wiring harnesses are secure and not damaged.
4. **Measure input voltage** across all three phases at the drive terminals. Verify that phase-to-phase voltage difference is within 3%.
5. **Power cycle the drive** and observe whether the fault clears. If Alarm 38 persists with the same sub-code, the control board or inverter module has failed.
6. **Replace the control PCB** (I/O control card) if the sub-code points to control or memory faults. make sure the replacement card matches your drive model and firmware version.
7. **Test or replace the inverter module** if the sub-code indicates inverter faults. Use a multimeter to check IGBT gate resistance and look for short circuits before ordering parts.
8. **Contact Danfoss technical support** with your model number, serial number, and sub-code if the fault remains unresolved after component replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 Control PCB (I/O Control Card) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-138-fault-code&k=Danfoss+FC302+Control+PCB+%28I%2FO+Control+Card%29&tag=errorcodefixes-20) \| Match the part number to your drive model and firmware version. Control boards are not universal across all FC302 sizes. |
| Danfoss FC302 Inverter IGBT Module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-138-fault-code&k=Danfoss+FC302+Inverter+IGBT+Module&tag=errorcodefixes-20) \| Only needed if the sub-code indicates inverter faults. Confirm with multimeter testing before ordering. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician if you are not trained in high-voltage DC bus work or do not have the proper discharge tools and PPE. Capacitors in VFDs hold lethal voltage for minutes after power-off. Professional diagnosis is also recommended if you cannot interpret the sub-code or if multiple components appear damaged. Danfoss technical support can provide remote assistance and part number lookup if you provide your drive serial number and sub-code details.

**Rough cost:** A pro service call runs about $300-800.
