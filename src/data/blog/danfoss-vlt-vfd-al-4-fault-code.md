---
title: "Danfoss VLT AL 4 Fault - Causes & Fix"
description: "AL 4 on a Danfoss VLT drive means Mains phase loss. Check for a missing or imbalanced incoming supply phase at the drive input terminals."
pubDatetime: 2026-06-04T09:20:58Z
modDatetime: 2026-06-04T09:20:58Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Three-pole contactor"
---

## Danfoss VLT AL 4 Fault — What It Means

Alarm 4 on a Danfoss VLT variable frequency drive signals a mains phase loss condition. The drive has detected either a missing supply phase or a voltage imbalance between phases that exceeds its allowed limit. According to Danfoss documentation, the phase-to-phase voltage difference must not exceed 3% of the nominal supply voltage. This alarm protects the drive from damage caused by unbalanced or incomplete incoming power. The fault originates on the supply side of the drive, not the motor side, so your diagnostic work should focus on the incoming line connections and upstream power distribution components.

[Jump to Fix](#fix)

## Common Causes

- **Lost incoming phase upstream** One of the three supply phases has dropped out due to a blown fuse, open disconnect, failed contactor pole, or loose terminal connection before the drive.
- **Supply voltage imbalance** The voltage difference between any two phases exceeds the drive's 3% tolerance, often caused by uneven loading or utility supply problems.
- **Intermittent upstream connection** A weak or corroded connection upstream shows acceptable voltage when the drive is off but drops a phase under load.
- **Defective contactor pole** One pole of a three-pole contactor feeding the drive has failed or makes poor contact, interrupting one phase.
- **Failed drive input rectifier** If the fault stays with the same drive terminal after swapping incoming leads, the drive's internal rectifier or power section has failed.

## Step-by-Step Fix {#fix}

1. **Lock out all power** to the drive and follow your facility's electrical safety procedures before opening the enclosure or touching any terminals.
2. **Measure phase-to-phase voltage** at the drive's input terminals (L1-L2, L2-L3, L3-L1) with a true-RMS multimeter to confirm all three phases are present and balanced within 3%.
3. **Check input current on all three phases** with a clamp meter while the drive is running at the operating point where the alarm occurs, looking for one phase with significantly lower current than the other two.
4. **Swap one incoming power lead** with another phase at the drive input terminals, then repeat the current measurement to see if the low-current condition follows the incoming wire or stays with the drive terminal.
5. **Trace the problem upstream** if the low current follows the same incoming wire, inspecting the disconnect, contactor, fuses, and terminal connections feeding that phase for damage, corrosion, or looseness.
6. **Inspect all incoming terminals** at the drive for tightness and clean contact, re-torque to the manufacturer's specification, and check for signs of overheating or arcing.
7. **Replace the defective component** (fuse, contactor, or conductor) if the fault is upstream, or contact Danfoss service if the fault stays with the drive terminal, indicating an internal rectifier failure.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Three-pole contactor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-vlt-vfd-al-4-fault-code&k=Three-pole+contactor&tag=errorcodefixes-20) \| Match the coil voltage and contact rating to your existing unit if one pole has failed. |
| Input fuses | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-vlt-vfd-al-4-fault-code&k=Input+fuses&tag=errorcodefixes-20) \| Use only the amp rating and interrupting capacity specified on the drive nameplate or wiring diagram. |
| Power input terminals and lugs | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-vlt-vfd-al-4-fault-code&k=Power+input+terminals+and+lugs&tag=errorcodefixes-20) \| Replace any terminals showing heat damage, corrosion, or mechanical deformation. |

## When to Call a Pro

Call a qualified industrial electrician or drive technician if you are not trained in three-phase power diagnostics, if the fault remains after you have verified balanced incoming voltage and tight connections, or if your lead-swapping test indicates the problem is inside the drive itself. Internal rectifier and power-section repairs require factory parts, specialized test equipment, and knowledge of high-voltage DC bus safety. Also call a professional if the alarm returns intermittently under load, which often points to a complex upstream distribution problem that requires load analysis and infrared scanning.
