---
title: "Allen-Bradley PowerFlex 525 F013 - Causes & Fix"
description: "F013 means ground fault: current is leaking to earth from the drive output. Most often a damaged motor cable or grounded motor winding."
pubDatetime: 2026-06-11T10:18:25Z
modDatetime: 2026-06-11T10:18:25Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - allen-bradley
money_part: "Motor power cable (shielded VFD-rated cable)"
most_likely_cause: "damaged motor cable insulation or grounded motor winding"
likelihood: "the most common cause"
diy_or_pro: "pro"
---

## What this code means
F013 on a PowerFlex 525 is a ground fault. The drive has detected a current path to earth ground at one or more of the output terminals. In practical terms, the VFD is seeing output current returning through ground instead of only through the motor phases. This fault protects the drive and motor from dangerous leakage current caused by insulation breakdown somewhere between the drive output terminals and the motor frame.

## Before You Replace Anything

Technicians sometimes replace the drive first, but Rockwell's first corrective action is always to inspect the motor and external wiring. Disconnect the motor leads and test the cable and motor separately with an insulation tester to isolate the fault before replacing the drive.

## Common Causes

- **Damaged motor or output cable insulation (~45%)** Abrasion in conduit, pinched conductors, or crushed insulation at terminals creates a leakage path to ground.
- **Grounded motor winding (~30%)** An internal motor fault or winding-to-frame short sends current directly to ground.
- **Moisture or contamination on motor leads (~15%)** Water, oil, or metal dust on terminals or inside junction boxes creates a conductive path to ground.
- **Loose or corroded terminations (~7%)** Poor connections at the drive output or motor junction box can allow current leakage to the enclosure.
- **Drive output stage failure (~3%)** A failed IGBT or internal short in the drive itself can trigger a false ground fault, but this is less common than field-side problems.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault appear immediately when you power up the drive, even before starting the motor?</summary>
<div class="dtree-body"><strong>Yes:</strong> The ground fault is constant, pointing to a hard short in the cable or motor. Lock out and disconnect the motor leads from the drive to isolate the problem.<br><strong>No:</strong> The fault may appear only under load or vibration, suggesting intermittent insulation breakdown. Inspect all connections and flex points in the cable run.</div>
</details>

<details class="dtree"><summary>With motor leads disconnected from the drive, does the fault clear and the drive power up normally?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is in the motor cable or motor itself. Test each cable conductor to ground with a megohmmeter to find the leakage path.<br><strong>No:</strong> The drive output stage may be damaged. Contact a qualified electrician or drive technician to test the drive or consider replacement.</div>
</details>

<details class="dtree"><summary>Does your insulation test show low resistance (below acceptable megohm values) from any motor lead to ground?</summary>
<div class="dtree-body"><strong>Yes:</strong> You have found the grounded conductor. Trace that cable or motor phase to locate and repair the insulation fault.<br><strong>No:</strong> If all cables and the motor test good but the fault persists, the drive may have an internal fault and should be evaluated for replacement.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Lock out and tag out** the equipment and verify the drive is fully de-energized before beginning any inspection or testing.
2. **Inspect the motor leads and output wiring** from the drive output terminals to the motor junction box for cut insulation, pinched conductors, loose terminations, moisture, or contact with grounded metal.
3. **Disconnect the motor leads from the drive** output terminals (U, V, W) to isolate the fault path and prevent damage to the drive during testing.
4. **Test each motor lead to ground** with an insulation-resistance tester (megohmmeter) if available. A grounded reading on any phase identifies the bad cable or motor winding.
5. **Inspect the motor** for winding-to-frame ground if the cable tests good. Check the motor junction box for moisture, loose connections, or signs of internal winding damage.
6. **Correct the failed component** by repairing or replacing the damaged motor cable, repairing or replacing the motor if the winding is grounded, or replacing the drive if the fault cannot be cleared after verifying the motor and wiring are good.
7. **Reassemble all connections**, clear the F013 fault from the drive display, and run a test cycle to verify the fault does not return under load.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor power cable (shielded VFD-rated cable) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f013-fault-code&k=Motor+power+cable+%28shielded+VFD-rated+cable%29&tag=errorcodefixes-20) \| Replace if insulation is damaged, cut, or shows low resistance to ground during testing. |
| Three-phase motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f013-fault-code&k=Three-phase+motor&tag=errorcodefixes-20) \| Replace or rewind if winding-to-frame insulation has failed and the motor tests grounded. |
| Allen-Bradley PowerFlex 525 VFD | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f013-fault-code&k=Allen-Bradley+PowerFlex+525+VFD&tag=errorcodefixes-20) \| Replace only if the fault persists after the motor and all wiring have been verified good and the drive itself is confirmed faulty. |

## When to Call a Pro

Call a qualified electrician or industrial controls technician if you are not trained in lockout/tagout procedures, high-voltage testing, or VFD troubleshooting. Working on energized VFD circuits or performing insulation-resistance tests requires an understanding of electrical safety and proper test equipment. If the motor cable and motor both test good and the fault remains, a technician with drive diagnostics experience should evaluate the PowerFlex 525 for internal faults or replace the drive. Motor rewinding or replacement also typically requires a professional.

**Rough cost:** A pro service call runs about $200-800 depending on whether you need new cable, motor repair, or drive replacement.
