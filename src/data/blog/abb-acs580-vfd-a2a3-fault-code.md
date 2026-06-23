---
title: "ABB ACS580 A2A3 Fault Code - Causes & Fix"
description: "A2A3 is not a valid ABB ACS580 code; you likely see A2B3 (earth leakage in motor/cable) or A3A2 (DC link undervoltage). Check motor insulation."
pubDatetime: 2026-06-21T10:31:02Z
modDatetime: 2026-06-21T10:31:02Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - abb
money_part: "3-phase motor power cable"
most_likely_cause: "Motor winding insulation breakdown creating a path to ground"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify the exact fault code on the drive display (A2B3 or A3A2) and note it precisely"
  - "Check for any external power-factor-correction capacitors or surge absorbers on the motor cable and disconnect them"
  - "Inspect motor cable for visible damage, abrasion, or moisture at terminals and along the run"
part_price: "$150-600 for motor cable replacement or motor rewind"
---

## ABB ACS580 A2A3 Fault Code — What It Means

The fault code A2A3 does not exist in the official ABB ACS580 fault list. You are most likely seeing A2B3, which indicates earth leakage caused by a ground fault in the motor or motor cable. The drive has detected an unbalanced load because current is flowing from one or more output phases to ground instead of through the motor windings. Alternatively, the code could be A3A2, which signals DC link undervoltage and points to an incoming power problem or internal DC bus fault. If the display shows A2B3, the issue is almost always failed motor insulation, a damaged output cable, or external components like power-factor-correction capacitors connected to the motor circuit. If the code is A3A2, the drive is not receiving enough DC voltage on its internal bus, usually due to incoming AC power loss, loose connections, or a failing internal rectifier.

## Before You Replace Anything

Technicians often replace the VFD itself without testing the motor and cable insulation first. A megohmmeter test between each motor phase and ground (should read above 1 MΩ) identifies the real fault in minutes.

[Jump to Fix](#fix)

## Common Causes

- **Motor winding insulation failure (~45%)** A break in the motor winding insulation allows current to flow to the motor frame (ground), triggering earth leakage detection.
- **Damaged or wet motor cable (~30%)** Abrasion, pinch points, or moisture ingress in the cable from drive to motor exposes a conductor to ground or the cable sheath.
- **Power-factor-correction capacitors or surge absorbers (~15%)** External components connected to the motor circuit create a capacitive path to ground that the drive interprets as an earth fault.
- **Loose or corroded output terminals (~7%)** Poor connections at the drive output (T1, T2, T3) or motor terminal block allow stray current to ground.
- **Contactors in motor circuit (~3%)** Contactors opening or closing in the motor cable during operation cause phase unbalance that appears as earth leakage.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault code on the drive display read exactly A2B3?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is earth leakage. Proceed with motor and cable insulation testing (megohmmeter check).<br><strong>No:</strong> If the code reads A3A2, the fault is DC link undervoltage. Check incoming AC power, line fuses, and DC bus voltage at the drive.</div>
</details>

<details class="dtree"><summary>With the motor cable disconnected from the drive, does the fault clear when you power on the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is in the motor or motor cable. Test motor winding insulation to ground with a megohmmeter (should be above 1 MΩ).<br><strong>No:</strong> The fault is internal to the drive or caused by parameter settings. Check parameter 99.13 (current measurement calibration) or contact ABB support.</div>
</details>

<details class="dtree"><summary>Are there any capacitors or surge absorbers visible on the motor cable or motor terminal box?</summary>
<div class="dtree-body"><strong>Yes:</strong> Remove the external components. They create a false earth-leakage signal. Restart the drive and check if the fault clears.<br><strong>No:</strong> Proceed with megohmmeter testing of the motor windings and cable insulation to locate the ground path.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down and lock out** the drive and incoming power supply. Verify 0V at the drive output terminals T1, T2, and T3 with a multimeter.
2. **Photograph the fault code** on the drive display to confirm whether it reads A2B3, A3A2, or another code before clearing it.
3. **Disconnect the motor cable** from the drive output terminals (T1, T2, T3). Label each wire for reconnection.
4. **Perform a megohmmeter test** on the motor. Measure resistance between each motor phase (U, V, W) and the motor frame (ground). Readings should be above 1 MΩ. If any phase reads below 0.5 MΩ or near 0 Ω, the motor winding is grounded and requires rewind or replacement.
5. **Test the motor cable insulation** separately. Disconnect the cable from the motor and measure resistance between each conductor and the cable sheath or ground. Replace the cable if any conductor shows low resistance to ground.
6. **Inspect for external components**. Remove any power-factor-correction capacitors, surge absorbers, or contactors from the motor circuit. These components cause false earth-leakage faults.
7. **Reconnect the motor cable** to the drive and motor if insulation tests pass. Restore power, clear the fault, and run the drive. Monitor for fault recurrence.

## Parts Often Needed

| Part | Notes |
|------|-------|
| 3-phase motor power cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a2a3-fault-code&k=3-phase+motor+power+cable&tag=errorcodefixes-20) \| Choose cable rated for VFD use (shielded or armored) and match the original gauge and length. |
| Motor rewind service or replacement motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a2a3-fault-code&k=Motor+rewind+service+or+replacement+motor&tag=errorcodefixes-20) \| If motor insulation is failed, a rewind is often more economical than replacement for motors above 5 HP. |

## When to Call a Pro

Call a qualified electrician or motor technician if you do not own a megohmmeter or are not trained in high-voltage isolation and testing. The fault involves AC output circuits that can exceed 480V on larger drives, and improper testing can damage the drive or create a shock hazard. A technician will perform insulation testing, identify whether the fault is in the motor or cable, and coordinate motor rewind or cable replacement. If the fault code is A3A2 (DC link undervoltage) instead of A2B3, internal drive diagnostics and DC bus measurements are required, which are beyond typical in-house capability.

**Rough cost:** A pro service call runs about $200-800 depending on motor rewind or cable replacement.

## See Also

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS580 A0 Fault Code - Causes & Fix](/posts/abb-acs580-vfd-a0-fault-code/)
- [ABB VFD Fault 3210 — Causes & Fix](/posts/abb-vfd-fault-3210/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
