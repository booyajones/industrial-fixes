---
title: "Allen-Bradley PowerFlex 525 F043 - Causes & Fix"
description: "F043 means Phase VW Short: excessive current between V and W output terminals. Most often caused by shorted motor leads or damaged cable."
pubDatetime: 2026-06-12T10:17:42Z
modDatetime: 2026-06-12T10:17:42Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - allen-bradley
money_part: "Motor V/W phase leads or complete motor cable"
most_likely_cause: "Shorted motor leads between V and W phases"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Visually inspect V and W output conductors for crushed insulation, abraded jacket, loose terminal screws, or burned wire"
  - "Check for tight, correct terminations at both the drive output terminals and motor junction box"
  - "Look for contamination (metal shavings, moisture, carbon tracking) around output terminals"
---

## Allen-Bradley PowerFlex 525 F043 — What It Means

F043 on the Allen-Bradley PowerFlex 525 VFD indicates a Phase VW Short. The drive has detected excessive current flowing between the V and W output terminals, which means there is a short circuit somewhere in the output phase wiring or the connected motor. This is one of three output short faults (F041 for UV, F042 for UW, and F043 for VW) that protect the drive's power section from damage.

The fault will trip the drive and stop motor operation immediately. Rockwell's documentation directs you to check the motor and drive output terminal wiring for a shorted condition and to replace the drive if the fault cannot be cleared after verifying the external wiring and motor are in good condition.

## Before You Replace Anything

Many technicians replace the VFD immediately without isolating whether the fault is in the motor, cable, or drive. Disconnecting the motor and testing phase-to-phase insulation resistance with a megohmmeter will show whether the short is external to the drive and save an unnecessary drive replacement.

[Jump to Fix](#fix)

## Common Causes

- **Shorted motor leads between V and W (~45%)** Damaged insulation, pinched cable, crushed conductors, or contamination in the motor feeder wiring creates a phase-to-phase short that the drive detects at its output terminals.
- **Shorted motor winding internally (~30%)** Insulation failure inside the motor between the V and W phase windings presents as a phase-to-phase short at the drive output and will cause F043 even if external wiring is perfect.
- **Loose or incorrectly landed output wiring (~15%)** Improperly terminated conductors at the drive or motor terminals can create an intermittent short path, especially under vibration or thermal cycling.
- **Drive power section damage (~10%)** Internal hardware failure in the drive's power card or output stage can cause the fault to persist even after the motor and wiring are proven good, requiring drive replacement.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault appear immediately on power-up, before the motor ever runs?</summary>
<div class="dtree-body"><strong>Yes:</strong> The short is likely hard-wired (damaged cable or internal motor short). Proceed to isolate the motor and test phase-to-phase resistance.<br><strong>No:</strong> The fault may be intermittent or load-dependent. Inspect for loose terminals, vibration damage, or thermal stress on wiring insulation.</div>
</details>

<details class="dtree"><summary>After disconnecting the motor, does the drive power up without F043?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is in the motor or motor cable. Test the motor windings and cable for phase-to-phase shorts.<br><strong>No:</strong> The fault is internal to the drive. The power section is damaged and the drive requires replacement.</div>
</details>

<details class="dtree"><summary>Do you see visible damage, abrasion, or burns on the V or W output conductors?</summary>
<div class="dtree-body"><strong>Yes:</strong> Repair or replace the damaged cable section and re-test. The fault should clear once the short path is removed.<br><strong>No:</strong> The short may be inside the motor or in a hidden section of the cable run. Use insulation-resistance testing to locate it.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Remove all power** and lock out the drive circuit. Verify zero-energy state with a meter before touching any wiring.
2. **Visually inspect the V and W output conductors** from the drive terminals to the motor for abrasion, crushed insulation, loose strands, burned insulation, or contamination.
3. **Check terminal tightness** at both the drive output terminals and the motor junction box. Correct any loose or mis-terminated conductors and look for signs of arcing or overheating.
4. **Disconnect the motor** from the drive output. Isolate the motor and test phase-to-phase insulation resistance between V and W using a megohmmeter to determine whether the short is in the motor winding or external wiring.
5. **If the motor or cable is shorted**, repair or replace the failed component. If insulation damage is found in the cable, replace the entire motor feeder or the damaged section.
6. **If the motor and wiring test good**, reconnect them and clear the fault. If F043 reappears, the drive power section is damaged and the drive must be replaced per Rockwell's guidance.
7. **After repair, clear the fault** code and re-energize the drive. Run the motor unloaded first to confirm stable operation before returning to full production load.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor V/W phase leads or complete motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f043-fault-code&k=Motor+V%2FW+phase+leads+or+complete+motor+cable&tag=errorcodefixes-20) \| Replace if insulation damage or conductor short is found during inspection or testing. |
| Three-phase AC motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f043-fault-code&k=Three-phase+AC+motor&tag=errorcodefixes-20) \| Replace if phase-to-phase winding insulation has failed internally between V and W windings. |
| Allen-Bradley PowerFlex 525 VFD (complete drive assembly) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f043-fault-code&k=Allen-Bradley+PowerFlex+525+VFD+%28complete+drive+assembly%29&tag=errorcodefixes-20) \| Replace if the short fault persists after the external motor and wiring are confirmed good. |

## When to Call a Pro

Call a qualified electrician or industrial technician immediately. F043 involves high-voltage AC output circuits and requires safe lockout/tagout, proper insulation-resistance testing with a megohmmeter, and the ability to distinguish between motor, cable, and drive failures. Incorrect troubleshooting can damage the replacement drive or create an arc-flash hazard. If the drive must be replaced, a technician will verify that all parameters are correctly re-entered and that the replacement unit is properly sized and configured for your motor and application. Do not attempt this repair without appropriate training and test equipment.

**Rough cost:** A pro service call runs about $150-800.

## See Also

- [Allen-Bradley PowerFlex 4M Fault Codes — F2, F4, F5, F7, F12 Fix Guide](/posts/allen-bradley-powerflex-4m-fault-codes/)
- [Allen-Bradley PowerFlex 525 F105 - Causes & Fix](/posts/allen-bradley-powerflex-525-vfd-f105-fault-code/)
- [Allen-Bradley PowerFlex 525 F110 - Causes & Fix](/posts/allen-bradley-powerflex-525-vfd-f110-fault-code/)
- [Allen-Bradley PowerFlex 525 F048 - Causes & Fix](/posts/allen-bradley-powerflex-525-vfd-f048-fault-code/)
