---
title: "Yaskawa A1000 VFD E60 Fault - Causes & Fix"
description: "E60 indicates a ground fault detected between the drive output and the motor. Most often a motor winding or cable insulation failure."
pubDatetime: 2026-07-24T07:33:31Z
modDatetime: 2026-07-24T07:33:31Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "VFD-rated shielded motor cable"
most_likely_cause: "motor winding insulation breakdown"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Visually inspect output cable insulation and terminations for visible damage, moisture, or contamination"
  - "Check the motor terminal box for water intrusion, dust buildup, or loose wire strands touching ground"
---

## Yaskawa A1000 VFD E60 Fault — What It Means

The E60 fault code on a Yaskawa A1000 variable frequency drive signals that the drive has detected a ground fault somewhere between its output terminals and the motor. The drive's internal ground-fault detection circuit monitors for leakage current flowing to ground through damaged insulation in the motor windings, output cables, or connections. When this leakage exceeds the drive's threshold, the drive trips to protect both itself and personnel from electrical hazards.

This fault can occur immediately at startup or develop over time as insulation degrades from heat, moisture, vibration, or contamination. The drive will not restart until the fault is cleared and the underlying ground path is identified and repaired. Because the fault involves potentially dangerous leakage current, troubleshooting requires careful isolation of the motor and cables and measurement with an insulation resistance tester (megohmmeter).

## Before You Replace Anything

Technicians sometimes replace the VFD itself when the fault actually lies in the motor or cable. Always megger-test the motor windings and output cables to ground before condemning the drive.

[Jump to Fix](#fix)

## Common Causes

- **Motor winding insulation failure (~50%)** Heat cycling, moisture, or contamination breaks down the insulation between motor windings and the frame, creating a path to ground.
- **Damaged output cable insulation (~25%)** Physical damage, pinching, or wear on the VFD output cables allows current to leak to conduit or ground.
- **Moisture in motor or cable connections (~15%)** Water intrusion into the motor terminal box or cable glands creates a conductive path to ground through dirt or corrosion.
- **Incorrect grounding or wiring (~7%)** Shared neutral or ground paths, missing PE wire, or improper shielded-cable grounding can trigger false ground-fault detection.
- **VFD ground-fault detection circuit failure (~3%)** The drive's internal current-sensing or detection circuitry malfunctions and reports a false ground fault.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault occur immediately when you power up the drive, even with the motor disconnected?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive itself or its internal ground-fault circuit may be faulty. Consult a qualified technician or contact Yaskawa support.<br><strong>No:</strong> The fault is downstream in the motor or output cables. Proceed with insulation resistance testing.</div>
</details>

<details class="dtree"><summary>Is the motor terminal box or cable entry wet, corroded, or contaminated with dust or oil?</summary>
<div class="dtree-body"><strong>Yes:</strong> Clean and dry the connections thoroughly, then retest. If the fault persists, megger-test the motor windings to ground.<br><strong>No:</strong> Perform megger testing on both the output cables and motor windings separately to isolate the fault.</div>
</details>

<details class="dtree"><summary>Does the insulation resistance from motor windings to ground measure below 1 megohm (or the threshold in your drive's manual)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor winding insulation has failed. The motor requires rewinding or replacement.<br><strong>No:</strong> Check output cable insulation and connections, verify proper PE grounding, and review drive parameter settings for ground-fault sensitivity.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Lock out and tag out** all power to the VFD and motor, following your facility's safety procedures.
2. **Disconnect the motor cables** from the VFD output terminals (U, V, W) and label them for reinstallation.
3. **Power up the VFD** without the motor connected and observe whether the E60 fault reappears; if it does, the drive may be defective.
4. **Inspect the motor terminal box** and cable entry points for moisture, dirt, or physical damage to insulation.
5. **Use an insulation resistance tester** (megohmmeter) set to 500 V DC or 1000 V DC (consult your model's documentation) to measure resistance from each motor winding (U, V, W) to the motor frame and to ground; readings below 1 megohm typically indicate insulation failure.
6. **Test the output cables** separately by disconnecting them at both ends and meggering each conductor to the cable shield and ground; replace any cable with low insulation resistance.
7. **Verify proper grounding** by checking that the motor frame, VFD chassis, and protective earth (PE) conductor are all bonded and that no shared neutral or improper shielding ground exists.
8. **Reconnect all wiring** if tests pass, clear the fault in the drive's display or parameter menu, and restart; if the fault returns, consult the drive manual for advanced parameter adjustments to ground-fault sensitivity or contact a Yaskawa-certified technician.

## Parts Often Needed

| Part | Notes |
|------|-------|
| VFD-rated shielded motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-e60-fault-code&k=VFD-rated+shielded+motor+cable&tag=errorcodefixes-20) \| Use cable rated for VFD service with continuous flex and proper grounding; consult cable length and gauge tables in the A1000 manual. |
| Replacement motor (matching horsepower and voltage) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-e60-fault-code&k=Replacement+motor+%28matching+horsepower+and+voltage%29&tag=errorcodefixes-20) \| Required if motor winding insulation has failed and rewinding is not economical. |

## When to Call a Pro

Call a qualified electrician or VFD technician if you lack a megohmmeter or experience with high-voltage insulation testing. Ground-fault diagnosis involves working around hazardous voltages and interpreting insulation resistance measurements that vary with motor size and voltage class. A professional can perform comprehensive testing of the motor, cables, and drive, adjust sensitivity parameters if needed, and determine whether a motor rewind or drive repair is the most cost-effective solution. Always involve a pro if the fault persists after basic inspections or if your facility's safety policy requires certified personnel for VFD work.

**Rough cost:** A pro service call runs about $200-800.
