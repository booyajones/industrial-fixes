---
title: "Yaskawa A1000 UV Fault - Causes & Fix"
description: "UV means undervoltage: the DC bus or supply voltage is too low to start. Most often caused by incoming phase loss or loose input terminals."
pubDatetime: 2026-06-11T09:57:25Z
modDatetime: 2026-06-11T09:57:25Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa A1000 DC bus capacitor bank"
most_likely_cause: "incoming phase loss or loose input power terminals"
likelihood: "the most common cause"
diy_or_pro: "pro"
---

## Yaskawa A1000 UV Fault — What It Means

The UV fault on a Yaskawa A1000 drive is an undervoltage alarm. It appears when the drive detects that the DC bus voltage has fallen below the threshold set in parameter L2-05, or that the control or power supply voltage is too low at the moment a Run command is given. The drive inhibits operation to protect its power section and control circuits from damage caused by insufficient voltage. This alarm will only trigger if parameter L2-01 is not set to 0 and the DC bus voltage is below the L2-05 threshold.

In practical terms, the drive is telling you it does not have enough incoming or internal voltage to operate safely. The fault can appear at startup, during a run attempt, or if the precharge circuit opens unexpectedly. It is a protective response, not a random error, and points to a real problem in the power supply, wiring, or internal components.

## Before You Replace Anything

Technicians sometimes replace the entire drive or main control board before checking incoming line voltage and terminal torque. Always verify proper three-phase voltage at the drive input terminals and retorque all power connections to the manufacturer's specified torque before swapping any boards.

[Jump to Fix](#fix)

## Common Causes

- **Incoming phase loss or poor wiring (~35%)** A missing phase or damaged input conductor causes the DC bus to collapse when the drive tries to start.
- **Loose or corroded input terminals (~25%)** Poor terminations create voltage drop under load and trigger the undervoltage threshold.
- **Low line voltage or supply sag (~15%)** Actual supply voltage below the drive's input range or a sag when contactors close will trip UV.
- **Undersized transformer or weak upstream source (~10%)** Insufficient transformer capacity or high source impedance causes voltage collapse at energization or acceleration.
- **Aging DC bus capacitors (~10%)** Worn capacitors reduce DC bus hold-up and can trigger UV even with good input power.
- **Failed charge circuit or control board (~5%)** A faulty precharge circuit or control board issue prevents the DC bus from reaching normal voltage.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Do all three incoming phases show proper voltage at the drive input terminals with a multimeter?</summary>
<div class="dtree-body"><strong>Yes:</strong> Line power is present. Move on to check terminal torque and internal drive components.<br><strong>No:</strong> You have a wiring fault, blown fuse, or open breaker upstream. Repair the supply before running the drive.</div>
</details>

<details class="dtree"><summary>Does the CHARGE indicator light on the drive illuminate when power is applied?</summary>
<div class="dtree-body"><strong>Yes:</strong> The precharge circuit is functioning. Focus on line quality, terminal connections, and capacitor condition.<br><strong>No:</strong> The charge circuit or control board may be faulty. Call a qualified technician to inspect the power supply and control circuits.</div>
</details>

<details class="dtree"><summary>Does the UV fault clear after you shut off the drive for 10 minutes and retorque all input terminals?</summary>
<div class="dtree-body"><strong>Yes:</strong> A loose terminal or transient sag was the cause. Monitor the drive and verify stable line voltage under load.<br><strong>No:</strong> The problem is internal (capacitors, power board, or control board) or the incoming supply is persistently weak. Professional diagnosis is required.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the fault code** on the operator display and confirm it reads UV, not a similar code like OV or OH.
2. **Measure incoming line voltage** at the drive's input terminals (L1, L2, L3) with a true-RMS multimeter to confirm all three phases are present and within the drive's specified input range.
3. **Inspect all main-circuit wiring** from the upstream disconnect to the drive input for loose lugs, damaged insulation, or signs of overheating, and retorque all terminals to the torque specification listed in the A1000 installation manual.
4. **Check line voltage under start conditions** by monitoring with the meter while the contactor closes and the drive is commanded to run, watching for any sag or dropout that could trigger the UV threshold.
5. **Review the drive's maintenance monitors**, especially parameter U4-05 (capacitor life indicator), because elevated values point to capacitor wear as a root cause and may require capacitor or drive replacement.
6. **Inspect the CHARGE indicator** and precharge circuit to confirm the DC bus is building voltage normally when power is applied.
7. **If line power is stable but UV persists**, the fault is internal and requires professional service to diagnose and replace the control board, power board, capacitor bank, or the entire drive depending on what the diagnostics reveal.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa A1000 DC bus capacitor bank | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-uv-fault-code&k=Yaskawa+A1000+DC+bus+capacitor+bank&tag=errorcodefixes-20) \| Required if maintenance monitor U4-05 indicates capacitor wear or end of life. |
| Yaskawa A1000 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-uv-fault-code&k=Yaskawa+A1000+control+board&tag=errorcodefixes-20) \| Needed if the CHARGE circuit fails or UV persists with good line power and healthy capacitors. |
| Yaskawa A1000 power supply board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-uv-fault-code&k=Yaskawa+A1000+power+supply+board&tag=errorcodefixes-20) \| Replace if internal supply voltage is low and other components test good. |

## When to Call a Pro

Call a qualified drive technician or industrial electrician any time you lack the tools to safely measure three-phase power, if you are not comfortable working inside a VFD cabinet energized at line voltage, or if the UV fault persists after you have confirmed good incoming power and retorqued all terminals. Internal repairs involving the control board, power board, or capacitor bank require specialized knowledge, proper discharge procedures, and manufacturer service training to perform safely. A technician will use the drive's own diagnostic parameters, measure DC bus voltage directly, check the precharge contactor operation, and determine whether board-level repair or full drive replacement is the most economical path forward.

**Rough cost:** A pro service call runs about $200-800.
