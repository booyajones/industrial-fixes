---
title: "Allen-Bradley PowerFlex 525 F015 - Causes & Fix"
description: "F015 means Load Loss: output torque current is too low. Most often a broken coupling, slipped belt, or disconnected mechanical drive."
pubDatetime: 2026-06-11T10:19:15Z
modDatetime: 2026-06-11T10:19:15Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - allen-bradley
money_part: "Motor coupling (jaw, grid, or disc type)"
most_likely_cause: "broken or slipping coupling, belt, chain, or gearbox link between motor and load"
likelihood: "the most common cause"
diy_or_pro: "pro"
---

## What this code means
F015 on an Allen-Bradley PowerFlex 525 is a Load Loss fault. Rockwell defines it as the output torque current falling below the value programmed in parameter A490 (Load Loss Level) for longer than the time programmed in A491 (Load Loss Time). This is not an electrical overcurrent or ground fault. Instead, it means the drive is running and energizing the motor, but the motor is not seeing enough mechanical load to prove it is actually coupled to the driven equipment. In practical terms, the motor is spinning but the process load is missing, slipping, or disconnected.

The fault exists to protect machinery from running uncoupled, which can cause overspeed damage or unsafe conditions. When F015 appears, the drive has detected that the torque current signature does not match a properly loaded motor. The usual culprits are mechanical disconnects like broken couplings, slipped belts, or a driven load that has seized or been removed. Less often, the fault is triggered because A490 and A491 are set too aggressively for a light or variable-load application.

## Before You Replace Anything

Technicians sometimes replace the VFD control board or motor, when in fact the real problem is a purely mechanical disconnect downstream of the motor shaft. Always inspect the coupling, belt, and driven equipment physically before ordering drive electronics.

## Common Causes

- **Broken or slipping coupling, belt, or chain (~50%)** The mechanical link between the motor and the driven load has failed, so the motor spins freely with almost no torque current.
- **Driven load is unloaded or disconnected (~25%)** The process equipment has lost its load (empty conveyor, open valve, disconnected pump impeller), dropping torque current below the A490 threshold.
- **Loose shaft key or decoupled shaft (~15%)** A keyway shear or loose setscrew allows the motor to rotate while the driven shaft does not, presenting almost zero mechanical resistance.
- **Load loss parameters too sensitive (~8%)** A490 (Load Loss Level) or A491 (Load Loss Time) are set lower or shorter than the application requires, triggering false faults during normal light-load operation.
- **Seized component upstream or downstream (~2%)** A bearing, gearbox, or pump has locked up and the motor cannot deliver torque, causing current to drop unexpectedly.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Can you see a broken coupling, missing belt, or disconnected shaft between the motor and the machine?</summary>
<div class="dtree-body"><strong>Yes:</strong> That mechanical disconnect is your F015 cause. Replace or reconnect the failed component and clear the fault.<br><strong>No:</strong> Move to the next check.</div>
</details>

<details class="dtree"><summary>Does the motor shaft spin freely by hand (power off, locked out) with almost no resistance?</summary>
<div class="dtree-body"><strong>Yes:</strong> The load is not mechanically coupled. Inspect couplings, belts, chains, and shafts for slippage or breakage.<br><strong>No:</strong> The coupling is intact. Check whether the driven load itself is missing, empty, or if A490/A491 are set too low for your application.</div>
</details>

<details class="dtree"><summary>Is the driven equipment actually loaded (full conveyor, closed valve, primed pump)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The load is present. Review parameters A490 and A491 to confirm they match your process torque profile, or contact a controls technician.<br><strong>No:</strong> Restore normal process load conditions and retest. If the machine is supposed to run unloaded at times, adjust A490 or A491 accordingly.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Lock out and tag out** the drive and motor per site safety procedures before any inspection.
2. **Inspect the mechanical drivetrain** visually: look for broken couplings, missing or slipped belts, disconnected chains, sheared shaft keys, or loose setscrews between the motor and the driven load.
3. **Rotate the motor shaft by hand** (with power isolated) to confirm the load is mechanically coupled and that resistance is consistent with the driven equipment.
4. **Check the driven equipment** for empty conveyors, open valves, seized bearings, or any condition that would remove or drastically reduce mechanical load on the motor.
5. **Review parameters A490 (Load Loss Level) and A491 (Load Loss Time)** in the PowerFlex 525 to verify they are appropriate for your application and not set so low that normal light-load running triggers the fault.
6. **Correct the mechanical disconnect** (replace coupling, re-tension belt, re-key shaft) or adjust A490/A491 if the fault is a sensitivity issue rather than a real failure.
7. **Clear the F015 fault** from the drive display, restore power under lockout/tagout release, and run the machine under normal load to confirm the fault does not reappear.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor coupling (jaw, grid, or disc type) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f015-fault-code&k=Motor+coupling+%28jaw%2C+grid%2C+or+disc+type%29&tag=errorcodefixes-20) \| Match your motor and driven-equipment shaft sizes and torque rating. |
| V-belt or synchronous belt | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f015-fault-code&k=V-belt+or+synchronous+belt&tag=errorcodefixes-20) \| Confirm belt profile, pitch, and length from the machine nameplate or OEM documentation. |
| Shaft key stock and setscrews | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f015-fault-code&k=Shaft+key+stock+and+setscrews&tag=errorcodefixes-20) \| Replace any sheared keys or stripped setscrews found during inspection. |

## When to Call a Pro

Call a qualified technician or controls integrator if you cannot locate an obvious mechanical disconnect, if the coupling and drivetrain appear intact but the fault persists, or if you are unfamiliar with VFD parameter programming. Adjusting A490 and A491 incorrectly can mask real mechanical failures and lead to equipment damage or safety hazards. A pro can also measure actual torque current under load, compare it to the programmed thresholds, and determine whether the fault is mechanical, a programming mismatch, or (rarely) a drive feedback issue. Do not bypass the load-loss function without understanding why the current signature is low.

**Rough cost:** A pro service call runs about $150–500 depending on mechanical repair.
