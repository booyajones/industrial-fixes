---
title: "ABB ACS580 A2B4 Fault Code - Causes & Fix"
description: "A2B4 means short circuit in the motor or motor cable. Most often caused by damaged cable insulation or motor winding failure."
pubDatetime: 2026-05-31T11:08:56Z
modDatetime: 2026-05-31T11:08:56Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "Shielded VFD-rated motor cable"
most_likely_cause: "Damaged motor cable insulation"
---

## What this code means
Fault code A2B4 (auxiliary code 2340) on the ABB ACS580 variable frequency drive indicates the drive has detected a short circuit in the motor or motor cable. This fault triggers when the drive senses abnormal current flow caused by phase-to-phase contact, phase-to-ground contact, or internal motor winding failure. The drive shuts down immediately to protect its output stage and prevent further damage to the motor circuit.

## Common Causes

- **Damaged motor cable insulation** Crushed, abraded, or deteriorated cable insulation allows phase conductors to contact each other or ground, creating a short circuit that triggers A2B4.
- **Motor winding failure** Internal motor short circuits from insulation breakdown, moisture ingress, or overheating cause the drive to detect fault current and trip on A2B4.
- **Wiring errors at motor terminal box** Incorrect delta or star connections, reversed phasing, or loose terminal lugs can create short circuit conditions that the drive reads as A2B4.
- **Earth fault in motor or cable** Phase-to-ground faults caused by damaged insulation, moisture, or contamination register as short circuits and generate the A2B4 code.
- **Power factor correction capacitors in motor circuit** Capacitors or surge absorbers installed on the motor side of the drive create current spikes the VFD interprets as short circuits, triggering A2B4.
- **Moisture or contamination at motor terminals** Water, oil, metal debris, or conductive dust bridging motor terminals or cable terminations causes short circuits detected as A2B4.

## Step-by-Step Fix {#fix}

1. **Lock out and tag out** the drive and motor circuit at the main disconnect, then visually inspect the motor, motor cable, and all terminations for burn marks, crushed insulation, loose connections, or signs of moisture and contamination.
2. **Verify motor wiring configuration** at the motor terminal box and drive output terminals, confirming correct delta or star connections match the motor nameplate and that all phase terminations are tight and properly insulated.
3. **Disconnect the motor cable** from both the drive output terminals and the motor, then test the cable and motor separately to isolate whether the fault is in the cable, motor, or termination points.
4. **Measure insulation resistance** of the motor windings and cable using a megohmmeter, testing phase-to-phase and phase-to-ground to check for earth faults or winding insulation breakdown as recommended by ABB.
5. **Remove any power factor correction capacitors or surge absorbers** from the motor circuit if present, as ABB specifically warns these components must not be installed on the motor side of the drive.
6. **Repair or replace** the failed component identified in testing, whether damaged cable, faulty motor with shorted windings, or corroded terminal connections, then reconnect and secure all terminations.
7. **Clear the A2B4 fault** from the drive panel, first test with the motor disconnected to confirm the drive powers up without fault, then reconnect the motor and monitor for immediate reoccurrence, escalating to ABB service support if the code returns with verified good motor and cable.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Shielded VFD-rated motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a2b4-fault-code&k=Shielded+VFD-rated+motor+cable&tag=errorcodefixes-20) \| Replace if insulation is damaged or testing shows phase-to-phase or phase-to-ground shorts. |
| Three-phase AC motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a2b4-fault-code&k=Three-phase+AC+motor&tag=errorcodefixes-20) \| Required if insulation resistance tests fail or internal winding short is confirmed. |
| Motor terminal lug kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a2b4-fault-code&k=Motor+terminal+lug+kit&tag=errorcodefixes-20) \| Use to replace burned, corroded, or loose terminations at motor or drive output. |

## When to Call a Pro

Call a qualified industrial electrician or drive technician if you are not trained in high-voltage lockout/tagout procedures, if insulation testing equipment is unavailable, or if the A2B4 fault returns after verifying the motor and cable are in good condition. Repeated short-circuit faults can damage the drive's output stage (IGBT module), and further troubleshooting may require ABB service support or drive power module replacement. If the motor or cable fault is intermittent or the drive trips immediately on power-up even with the motor disconnected, professional diagnostics are necessary to avoid risking personnel safety or additional equipment damage.
