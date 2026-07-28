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

## What this code means
F043 on the Allen-Bradley PowerFlex 525 VFD indicates a Phase VW Short. The drive has detected excessive current flowing between the V and W output terminals, which means there is a short circuit somewhere in the output phase wiring or the connected motor. This is one of three output short faults (F041 for UV, F042 for UW, and F043 for VW) that protect the drive's power section from damage.

The fault will trip the drive and stop motor operation immediately. Rockwell's documentation directs you to check the motor and drive output terminal wiring for a shorted condition and to replace the drive if the fault cannot be cleared after verifying the external wiring and motor are in good condition.

## Before You Replace Anything

Many technicians replace the VFD immediately without isolating whether the fault is in the motor, cable, or drive. Disconnecting the motor and testing phase-to-phase insulation resistance with a megohmmeter will show whether the short is external to the drive and save an unnecessary drive replacement.

## Common Causes

- **Shorted motor leads between V and W** Damaged insulation, pinched cable, crushed conductors, or contamination in the motor feeder wiring creates a phase-to-phase short that the drive detects at its output terminals.
- **Shorted motor winding internally** Insulation failure inside the motor between the V and W phase windings presents as a phase-to-phase short at the drive output and will cause F043 even if external wiring is perfect.
- **Loose or incorrectly landed output wiring** Improperly terminated conductors at the drive or motor terminals can create an intermittent short path, especially under vibration or thermal cycling.
- **Drive power section damage** Internal hardware failure in the drive's power card or output stage can cause the fault to persist even after the motor and wiring are proven good, requiring drive replacement.

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
