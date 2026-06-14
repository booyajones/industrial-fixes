---
title: "Allen-Bradley PowerFlex 525 F042 - Causes & Fix"
description: "F042 means Phase UW Short: excessive current between output terminals U and W. Check motor leads and cable for shorts first."
pubDatetime: 2026-06-12T10:15:44Z
modDatetime: 2026-06-12T10:15:44Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - allen-bradley
money_part: "Motor output cable (U, V, W power conductors)"
most_likely_cause: "Shorted motor leads or damaged output cable insulation"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Visually inspect motor output terminals U and W and the cable run for crushed insulation, pinched conductors, or scorching at connection points"
---

## Allen-Bradley PowerFlex 525 F042 — What It Means

The Allen-Bradley PowerFlex 525 F042 fault code means Phase UW Short. The drive has detected excessive current flowing between output terminals U and W. This is a phase-to-phase short fault on the inverter output, not a general overload. Rockwell's fault table instructs technicians to check the motor and drive output terminal wiring for a shorted condition and to replace the drive if the fault cannot be cleared.

In practice, this fault points to a short between the U and W motor leads, a short inside the motor winding itself, damaged output cable insulation where conductors touch, or a failed output stage inside the drive. The fault is specific to the U and W phases. It requires careful isolation testing to find whether the problem is in the cable, the motor, or the drive power section.

## Before You Replace Anything

Technicians sometimes replace the entire drive before isolating the motor and testing the cable. Disconnect the motor leads at the drive and megger-test the motor and cable separately to confirm whether the short is downstream or in the drive output stage.

[Jump to Fix](#fix)

## Common Causes

- **Shorted or damaged motor output cable (~40%)** Insulation breakdown between U and W conductors at conduit entries, motor junction boxes, or vibration points causes phase-to-phase current flow that trips F042.
- **Shorted motor windings (~30%)** Contamination, moisture, or insulation failure inside the motor creates a phase-to-phase fault between the U and W windings.
- **Failed drive output stage (IGBT module) (~20%)** Internal short in the drive's power section causes F042 even when the motor is disconnected, indicating the drive itself needs replacement.
- **Loose or poorly terminated output lugs (~10%)** Frayed strands or bare wire at the U or W terminals can bridge phases or touch adjacent conductors under vibration.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault appear immediately on power-up before the drive runs?</summary>
<div class="dtree-body"><strong>Yes:</strong> The short is likely present at rest in the cable, motor, or drive output stage. Proceed to disconnect and test each component.<br><strong>No:</strong> The short may develop under load due to vibration or heating. Inspect cable routing and motor terminal tightness carefully.</div>
</details>

<details class="dtree"><summary>Does the fault clear when you disconnect the motor leads at the drive output terminals U, V, and W?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem is downstream in the motor or cable, not the drive. Megger-test the motor and cable to find the short.<br><strong>No:</strong> The drive output stage is likely damaged. Replace the drive per Rockwell's guidance if the fault cannot be cleared.</div>
</details>

<details class="dtree"><summary>Do you see physical damage, oil contamination, or scorching on the U or W motor leads or terminals?</summary>
<div class="dtree-body"><strong>Yes:</strong> Replace the damaged cable section and reterminate. Clear the fault and test under no-load before returning to service.<br><strong>No:</strong> Perform insulation resistance testing on the motor and cable to identify hidden phase-to-phase or phase-to-ground faults.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Lock out and tag out power** to the drive and wait for the DC bus capacitors to discharge completely before opening any panels or touching terminals.
2. **Inspect the motor output cable path** from the drive terminals through conduit, cable trays, and the motor junction box for crushed insulation, pinched wires, oil damage, or loose lugs at U and W.
3. **Disconnect the motor leads** at the drive output terminals U, V, and W, then clear the fault and power the drive briefly to see if F042 reappears without a motor connected.
4. **Perform insulation resistance (megger) testing** on the motor windings phase-to-phase (U to W especially) and phase-to-ground to identify shorts or low insulation resistance that would cause the fault.
5. **Test the output cable separately** by disconnecting it at both ends and meggering conductor-to-conductor and conductor-to-ground to confirm the cable is not shorted.
6. **If the motor and cable test good**, the drive output stage is likely failed. Replace the PowerFlex 525 drive per Rockwell's published guidance that the drive should be replaced if the fault cannot be cleared.
7. **After repairs, reterminate all output wiring** with proper torque, verify correct motor phasing and rotation, clear the fault code, and test the drive under no-load conditions before returning to full operation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor output cable (U, V, W power conductors) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f042-fault-code&k=Motor+output+cable+%28U%2C+V%2C+W+power+conductors%29&tag=errorcodefixes-20) \| Replace if insulation testing shows a short or if physical damage is visible between the drive and motor. |
| Motor (with shorted U/W windings) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f042-fault-code&k=Motor+%28with+shorted+U%2FW+windings%29&tag=errorcodefixes-20) \| Rewind or replace if megger testing confirms a phase-to-phase winding short that cannot be cleared. |
| Allen-Bradley PowerFlex 525 drive | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f042-fault-code&k=Allen-Bradley+PowerFlex+525+drive&tag=errorcodefixes-20) \| Replace the entire drive if F042 persists with the motor disconnected, indicating a failed output power section. |

## When to Call a Pro

Call a qualified electrician or drive technician immediately. F042 involves high-voltage AC output wiring and requires lockout/tagout, insulation resistance testing with a megohmmeter, and the ability to safely isolate and test the drive power section. Misdiagnosis can lead to expensive drive replacement when the real problem is a damaged cable or motor. A technician will disconnect the motor, perform megger tests on both the motor and cable, and determine whether the fault is in the wiring, the motor windings, or the drive output stage before ordering parts. If the drive output stage has failed, replacement requires matching the frame size, voltage rating, and parameter setup to your application.

**Rough cost:** A pro service call runs about $200-800 depending on whether the fix is cable replacement, motor winding repair, or drive replacement.
