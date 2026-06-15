---
title: "Allen-Bradley PowerFlex 525 F040 - Causes & Fix"
description: "F040 means a phase-to-ground fault on output phase W. Most often caused by damaged motor cable or grounded motor winding insulation."
pubDatetime: 2026-06-12T10:13:24Z
modDatetime: 2026-06-12T10:13:24Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - allen-bradley
money_part: "Motor output cable (U/V/W conductors and ground)"
most_likely_cause: "damaged motor cable or grounded motor winding"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect all output terminal connections at the drive and motor for loose hardware, charring, or exposed copper"
  - "Look for physical damage to the motor cable along its entire run, especially at sharp bends or cable-tray edges"
---

## Allen-Bradley PowerFlex 525 F040 — What It Means

The PowerFlex 525 F040 fault indicates the drive has detected a current path from output phase W to ground. Rockwell defines F040 as "Phase W to Gnd," meaning the drive believes the W motor lead or connected motor circuit is shorted to earth. This is part of the output fault group where the drive monitors for ground faults on each output phase.

The fault typically originates outside the drive itself. The most common sources are a damaged motor cable with exposed conductors touching grounded conduit or metal surfaces, moisture or contamination inside the motor junction box or windings, loose or miswired output wiring at the drive or motor terminals, or degraded insulation in the motor winding that allows W phase to contact the motor frame. Rockwell's documented troubleshooting action is to inspect the drive-to-motor wiring and test the motor for a grounded phase. The fault is almost always a wiring or motor insulation problem rather than a control programming issue.

## Before You Replace Anything

Technicians sometimes replace the drive before isolating the fault. Always disconnect the motor leads at the drive and megger-test the motor and cable separately to confirm whether the fault is in the external circuit or the drive power section.

[Jump to Fix](#fix)

## Common Causes

- **Damaged motor cable (~40%)** A nick, crush, or abrasion in the insulation of the W-phase conductor allows current to leak to grounded conduit, tray, or adjacent metal, triggering the ground-fault detection.
- **Grounded motor winding (~30%)** Moisture, contamination, thermal stress, or age degrades the insulation in the motor's W-phase winding so that it contacts the motor frame or core.
- **Loose or miswired output termination (~15%)** A loose screw at the drive U/V/W terminal block or motor junction box allows the W conductor to touch a grounded surface or adjacent terminal.
- **Moisture or contamination in motor junction box (~10%)** Water, coolant, or conductive dust inside the motor junction box creates a current path from the W terminal to ground.
- **Failed drive power section (output stage) (~5%)** If the fault persists with all motor leads disconnected and no external path to ground is found, the drive's internal output circuitry for phase W may be damaged and the drive must be replaced.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault appear immediately when you power the drive with the motor disconnected?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is internal to the drive power section. Replace the drive after verifying no wiring remains connected to the W output terminal.<br><strong>No:</strong> The fault is in the motor or cable. Proceed with insulation testing of the motor and cable separately.</div>
</details>

<details class="dtree"><summary>Does a megohmmeter show low resistance (below one megohm) from the W motor lead to the motor frame?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor winding is grounded. Repair or replace the motor.<br><strong>No:</strong> The cable or termination is the problem. Inspect and test the cable, then check all terminal connections for damage or contamination.</div>
</details>

<details class="dtree"><summary>Is there visible physical damage, moisture, or contamination on the motor cable or in the junction box?</summary>
<div class="dtree-body"><strong>Yes:</strong> Clean and dry the affected area or replace the damaged section of cable. Re-test with a megohmmeter before reconnecting to the drive.<br><strong>No:</strong> The fault may be intermittent or at a hidden splice. Test the cable under different conditions (flexed, vibrated) and consult the drive manual for any additional diagnostics.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Lock out and tag out** all power to the drive and motor circuit before beginning any inspection or testing.
2. **Disconnect the motor leads** at the drive output terminals (U, V, W) and verify that the drive clears the fault when powered on with no load connected. If the fault persists with no external wiring, the drive power section is damaged and must be replaced.
3. **Megger-test the motor** by connecting an insulation tester between each motor lead and the motor frame, with the motor isolated from the drive. A reading below one megohm on the W phase indicates a grounded winding. Repair or replace the motor.
4. **Megger-test the motor cable** from the drive-end terminals to ground with the motor disconnected. Low resistance on the W conductor indicates cable damage. Inspect the entire cable run for physical damage, paying close attention to areas where the cable passes through sharp edges, bends, or high-vibration zones.
5. **Inspect all output terminals** at both the drive and motor for loose hardware, char marks, exposed copper, moisture, or foreign material. Tighten, clean, or replace damaged terminations and verify proper torque per the drive installation manual.
6. **Re-assemble and re-test** the circuit one section at a time. Reconnect the cable to the drive (with motor still disconnected) and power on. If the fault returns, replace the cable. If clear, reconnect the motor and re-test. If the fault returns, replace the motor.
7. **Replace the failed component** only after isolation testing confirms the source. Most often this will be the motor cable or motor. If all external components test good and the fault appeared with no load connected, replace the drive.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor output cable (U/V/W conductors and ground) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f040-fault-code&k=Motor+output+cable+%28U%2FV%2FW+conductors+and+ground%29&tag=errorcodefixes-20) \| Match the wire gauge and insulation rating to the original installation and the drive's output current specification. |
| Three-phase AC motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f040-fault-code&k=Three-phase+AC+motor&tag=errorcodefixes-20) \| Must match the horsepower, voltage, and frame size of the original motor and the drive nameplate rating. |
| PowerFlex 525 drive assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f040-fault-code&k=PowerFlex+525+drive+assembly&tag=errorcodefixes-20) \| Required only if the fault persists with all motor and cable disconnected. Verify the catalog number and firmware revision match your application. |

## When to Call a Pro

Call a qualified electrician or industrial technician for all PowerFlex 525 F040 troubleshooting and repair. The work requires lock-out/tag-out of three-phase high-voltage circuits, use of a megohmmeter to perform insulation resistance testing on motor windings and cables, and the ability to safely isolate and replace motor cables, motors, or the drive power section. Misdiagnosis can lead to unnecessary replacement of expensive drives when the actual fault is in a motor cable or winding. A trained technician will methodically disconnect and test each section of the output circuit to pinpoint whether the ground fault is in the cable, motor, or drive, and will verify proper termination and grounding practices to prevent recurrence.

**Rough cost:** A pro service call runs about $200-800.

## See Also

- [Allen-Bradley PowerFlex 525 F109 - Causes & Fix](/posts/allen-bradley-powerflex-525-vfd-f109-fault-code/)
- [Allen-Bradley PowerFlex 525 F101 - Causes & Fix](/posts/allen-bradley-powerflex-525-vfd-f101-fault-code/)
- [Allen-Bradley PowerFlex F091 Fault — Encoder Loss Fix](/posts/allen-bradley-powerflex-f091-fault/)
- [Allen-Bradley PowerFlex 525 F013 - Causes & Fix](/posts/allen-bradley-powerflex-525-vfd-f013-fault-code/)
