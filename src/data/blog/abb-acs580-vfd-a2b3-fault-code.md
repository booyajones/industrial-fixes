---
title: "ABB ACS580 A2B3 Fault - Causes & Fix"
description: "A2B3 means earth leakage detected. The drive found unbalanced current caused by an earth fault in the motor or motor cable."
pubDatetime: 2026-05-31T11:08:21Z
modDatetime: 2026-05-31T11:08:21Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "Motor"
most_likely_cause: "Motor insulation breakdown to ground"
---

## What this code means
A2B3 on an ABB ACS580 drive signals an earth leakage fault. The drive has detected unbalanced motor output current, typically caused by an earth fault in the motor or motor cable. ABB's documentation assigns auxiliary code 2330 to this fault condition. The drive is protecting itself and the motor from a ground fault somewhere in the load circuit. Most often the problem is insulation breakdown in the motor windings, damaged cable insulation allowing conductors to contact ground, or moisture intrusion in conduit, junction boxes, or the motor terminal box.

## Common Causes

- **Motor insulation breakdown to ground** Winding insulation deteriorates over time or from overheating, creating a path to the motor frame.
- **Damaged motor cable insulation** Nicked, abraded, or crushed cable insulation allows conductors to contact conduit or ground.
- **Moisture or water intrusion** ABB warns that water in conduit, junction boxes, or motor terminal boxes increases the likelihood of VFD faults and warnings.
- **Conductive contamination** Dust, oil, or chemical residue in the motor or wiring path creates a leakage path to ground.
- **Power-factor correction capacitors or surge absorbers in the motor cable** ABB explicitly instructs technicians to verify these components are not present in the motor cable path.

## Step-by-Step Fix {#fix}

1. **Stop and isolate the drive.** Lock out and tag out power, then visually inspect the motor, cable, and all output terminations for damage, moisture, contamination, or loose connections.
2. **Inspect the motor cable route** for pinches, abrasion, crushed conduit, or water ingress, especially in outdoor or washdown areas.
3. **Check the motor and motor cable insulation resistance with a megohmmeter.** ABB instructs technicians to measure insulation resistance of the motor and motor cable when troubleshooting A2B3 conditions.
4. **Verify there are no power-factor correction capacitors or surge absorbers in the motor cable.** ABB specifically calls these out as items to check and remove if found.
5. **Inspect the motor itself** for winding-to-frame leakage, terminal box contamination, or overheating damage that could have compromised insulation.
6. **Repair the failed component.** Replace damaged cable, repair termination issues, dry and clean contaminated components, or replace the motor if insulation is defective.
7. **Clear the fault and retest** after the insulation problem is corrected. If the fault persists after good insulation and clean wiring are verified, escalate for drive and motor-system review.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a2b3-fault-code&k=Motor&tag=errorcodefixes-20) \| Replace if winding insulation to frame has failed and cannot be repaired. |
| Motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a2b3-fault-code&k=Motor+cable&tag=errorcodefixes-20) \| Replace if insulation is damaged or leakage to ground is found during megohmmeter testing. |
| Cable terminations, lugs, and glands | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a2b3-fault-code&k=Cable+terminations%2C+lugs%2C+and+glands&tag=errorcodefixes-20) \| Replace if moisture, contamination, or physical damage is present at the cable ends. |

## When to Call a Pro

Call a qualified electrician or motor technician if you are not trained in high-voltage isolation, lockout/tagout procedures, or insulation-resistance testing. A2B3 faults point to earth leakage in the motor or cable, and misdiagnosis can damage the drive or create a shock hazard. If you have replaced the motor cable, verified no capacitors or surge absorbers are present, and confirmed good insulation resistance but the fault returns, the issue may involve drive configuration, grounding system design, or an intermittent fault that requires advanced diagnostics.
