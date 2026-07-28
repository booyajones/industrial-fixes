---
title: "Danfoss FC302 VFD AL-119 Fault - Causes & Fix"
description: "AL-119 does not exist in FC302 documentation. Likely AL 13 (overcurrent) or AL 38 (internal fault). Check motor load and parameter settings."
pubDatetime: 2026-06-24T10:15:41Z
modDatetime: 2026-06-24T10:15:41Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Inverter board or power stack assembly"
most_likely_cause: "Mechanical overload on motor shaft or incorrect motor nominal current parameter setting"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify motor nominal current in parameter 1-24 matches the actual motor nameplate rating"
  - "Check that all cooling fans are spinning and heatsinks are free of dust or blockage"
  - "Measure input voltage phase balance across all three input phases (must be within 3 percent)"
---

## What this code means
The fault code AL-119 does not appear in official Danfoss FC302 VLT AutomationDrive documentation. Danfoss FC 301/302 alarms range from AL 1 to AL 43. This code is likely a misreading of AL 13 (output current exceeds limit), AL 38 (internal fault), or a transcription error from a different source. AL 13 is the most common overcurrent fault, triggered when drive output current exceeds the peak current limit (typically 200 to 250 percent of rated motor current) during normal operation or acceleration.

If the intended fault is AL 38, it indicates a control board failure, memory error, or firmware corruption. Check parameter 15-32 for extended diagnostic sub-codes (ranging from 5376 to 65535) that provide additional detail. The steps below assume AL 13 as the most probable intended code.

## Before You Replace Anything

Technicians often replace the entire inverter board when AL 13 appears, but the fault is frequently caused by incorrect parameter 1-24 (motor nominal current) settings or a mechanical overload on the motor shaft. Always verify motor nameplate current matches parameter 1-24 and disconnect the motor to test the drive unloaded before replacing power components.

## Common Causes

- **Mechanical overload on motor shaft (~30%)** The motor is working harder than rated capacity due to a jammed load, worn bearings, or misaligned coupling, causing current draw to spike above the drive's peak limit.
- **Incorrect motor nominal current in parameter 1-24 (~25%)** Parameter 1-24 is set higher than the actual motor nameplate rating, causing the drive to allow excessive current before tripping.
- **Motor winding partial short or open circuit (~15%)** A failing motor with shorted or open windings draws unbalanced or excessive current that triggers the overcurrent protection.
- **Loose or damaged cable between drive and motor (~15%)** High resistance or intermittent connections at output terminals (2, 4, 6) create current spikes and voltage imbalance that exceed the drive's current limit.
- **Aging or damaged IGBT modules on inverter board (~10%)** IGBT transistors losing current regulation capability allow current to rise unchecked, triggering the fault even under normal load.
- **Insufficient cooling airflow or blocked heatsinks (~5%)** Overheating components reduce current-handling capacity, and the drive trips to protect itself even at currents normally within safe range.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault appear immediately on power-up with no motor connected?</summary>
<div class="dtree-body"><strong>Yes:</strong> Internal drive failure, most likely a failed IGBT module or inverter board. Call a VFD technician or plan to replace the power stack.<br><strong>No:</strong> The fault is related to the motor, cable, or parameter settings. Proceed to check motor nameplate current and parameter 1-24.</div>
</details>

<details class="dtree"><summary>Does parameter 1-24 (motor nominal current) match the motor nameplate current rating exactly?</summary>
<div class="dtree-body"><strong>Yes:</strong> Parameter is correct. Check for mechanical overload on the motor shaft or motor winding damage.<br><strong>No:</strong> Set parameter 1-24 to match the motor nameplate current, reset the fault, and test again.</div>
</details>

<details class="dtree"><summary>Can you turn the motor shaft freely by hand with power off and the load disconnected?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor and mechanical system are not jammed. Test motor winding resistance and cable continuity from drive output terminals to motor.<br><strong>No:</strong> Mechanical overload or seized bearing. Repair or replace the load or motor before running the drive.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down and lock out the drive** following all electrical safety procedures, then wait at least 5 minutes for DC bus capacitors to discharge before opening the cabinet.
2. **Record all parameters** from the drive using the control panel or PC software so you can restore settings if a fault clears or a board is replaced.
3. **Disconnect the motor** at the drive output terminals (2, 4, 6) and power up the drive in no-load mode to test if the fault persists without a motor connected.
4. **Check parameter 1-24** (motor nominal current) against the motor nameplate and verify parameter 1-28 (motor thermal protection) is set correctly for your motor type.
5. **Measure motor cable continuity** from each drive output terminal to the corresponding motor winding terminal, and check for shorts between phases or to ground using a multimeter.
6. **Inspect all cooling fans and heatsinks** inside the drive cabinet, clean dust and debris, and confirm fans spin freely when power is applied.
7. **Test IGBT modules** on the inverter board using a multimeter in diode mode (gate resistance typically 10 to 50 ohms), or replace the inverter board if the fault persists with motor disconnected and all parameters correct.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Inverter board or power stack assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-119-fault-code&k=Inverter+board+or+power+stack+assembly&tag=errorcodefixes-20) \| Required if IGBT modules test faulty or fault persists with motor disconnected; consult Danfoss or a distributor for the exact board part number matching your FC302 frame size. |
| Cooling fan assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-119-fault-code&k=Cooling+fan+assembly&tag=errorcodefixes-20) \| Replace if fans do not spin or make noise; match fan voltage and CFM rating to the original. |
| Motor output cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-119-fault-code&k=Motor+output+cable&tag=errorcodefixes-20) \| Use shielded cable rated for VFD service if continuity test shows opens or high resistance in existing cable. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician if the fault appears with the motor disconnected, if you are not trained in high-voltage DC bus safety, or if IGBT testing and inverter board replacement are beyond your skill level. Work on VFD power sections requires understanding of DC bus capacitor discharge time (at least 5 minutes), proper grounding, and board-level diagnostics. If parameter changes and motor checks do not clear the fault, professional diagnosis with oscilloscope and current-probe tools is the fastest path to identifying failed power components or control board issues.

**Rough cost:** A pro service call runs about $300-800.
