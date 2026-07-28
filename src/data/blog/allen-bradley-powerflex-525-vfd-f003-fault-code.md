---
title: "Allen-Bradley PowerFlex 525 F003 - Causes & Fix"
description: "F003 means Power Loss: the drive detected single-phase operation under load. Most often a blown input fuse or loose line connection."
pubDatetime: 2026-06-11T10:13:43Z
modDatetime: 2026-06-11T10:13:43Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - allen-bradley
money_part: "Input line fuses (class CC, J, or T as specified by installation)"
most_likely_cause: "blown input fuse on one phase"
likelihood: "the most common cause"
diy_or_pro: "pro"
---

## What this code means
F003 on a PowerFlex 525 indicates Power Loss. The drive has detected single-phase operation while the motor is under load, typically caused by the loss of one incoming AC line phase, a low-voltage sag, or an interruption on the input power side. Rockwell Automation's fault table describes the cause as single phase operation detected with excessive load and directs you to check the incoming AC line, input fuses, and load.

In the field this usually means a blown input fuse on one phase, a loose or burned incoming power connection, a utility brownout or brief line interruption while the motor is demanding torque, or a supply problem that leaves the drive effectively single-phased. Less commonly it can point to a load heavy enough that a marginal supply condition trips the drive. The fault is a power-input condition, not a drive internal failure, so the first step is always to inspect the line side.

## Before You Replace Anything

Technicians sometimes replace the drive itself when F003 appears repeatedly, but the fault is almost always an external supply or termination issue. Measure all three incoming line voltages at the drive terminals under load before ordering drive hardware.

## Common Causes

- **Blown input fuse on one phase** A single open fuse leaves the drive running on two phases, which immediately triggers the power-loss detection when load is applied.
- **Loose, burned, or intermittently open incoming power connection** A termination that opens under vibration or heat drops one phase and causes the fault to appear during start or acceleration.
- **Utility sag, brownout, or brief line interruption under load** A voltage dip from the feeder or transformer that coincides with motor torque demand will trip the drive as a single-phase condition.
- **Upstream contactor or disconnect dropping one phase intermittently** A failing contactor contact or disconnect blade can create a high-resistance path that appears as a missing phase when current rises.
- **Excessive mechanical load combined with marginal supply voltage** A motor load that is too high for the feeder capacity can push the drive into the fault zone even if all three phases are technically present.

## Step-by-Step Fix {#fix}

1. **Verify fault repeatability and note when it occurs.** Observe whether the trip happens on start, during acceleration, or under steady load. This tells you whether the supply problem is constant or load-dependent.
2. **Measure all three input phases at the drive line terminals.** Use a multimeter to check line-to-line voltage on L1-L2, L2-L3, and L3-L1 while the drive is attempting to start or run. Look for a missing phase or a voltage more than a few percent lower than the others.
3. **Inspect and test upstream input fuses.** Pull each fuse and check continuity with a meter. A single open fuse is the most common cause of F003 and is easy to miss on a visual inspection alone.
4. **Check all line-side terminations for looseness, heat damage, or discoloration.** Torque all terminal screws to the manufacturer's specification and look for burned lugs or arcing marks that indicate intermittent contact.
5. **Examine the disconnect, contactor, or feeder components.** If the fuses and terminations are good, trace the incoming power back through any contactors or disconnect switches and verify each phase has low resistance and no intermittent opening.
6. **Correct the source issue before reapplying the drive.** Replace failed fuses, tighten loose connections, or repair feeder damage. Do not clear the fault and restart until the root cause is fixed, or you risk damage to the motor or drive.
7. **Clear the fault and confirm normal operation under load.** After the line-side repair, reset the drive and run the motor through a full duty cycle. Monitor the input voltages and verify the fault does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input line fuses (class CC, J, or T as specified by installation) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f003-fault-code&k=Input+line+fuses+%28class+CC%2C+J%2C+or+T+as+specified+by+installation%29&tag=errorcodefixes-20) \| Match the amperage and interrupt rating to your drive nameplate and branch-circuit design. Consult your installation drawings for fuse class. |
| Crimp lugs or compression terminals for incoming line conductors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f003-fault-code&k=Crimp+lugs+or+compression+terminals+for+incoming+line+conductors&tag=errorcodefixes-20) \| Use only UL-listed lugs rated for the conductor size and the drive terminal barrel. Replace any lug showing heat damage or discoloration. |

## When to Call a Pro

Call a qualified electrician or drive technician for F003 work. Diagnosing the fault requires live measurement of three-phase line voltage, inspection of energized terminations, and tracing the supply back through fuses, disconnects, and feeders. The work is high-voltage and must follow lockout-tagout and arc-flash safety rules. A technician will measure all three phases under load, identify the missing or weak phase, and repair the upstream fuse, termination, or feeder component. If the supply is confirmed good and the fault still appears, the technician will verify the mechanical load is not excessive and check for a rare drive internal issue. Do not attempt to clear and restart the drive repeatedly without finding the root cause, because single-phasing under load can overheat the motor windings or damage the drive power stage.
