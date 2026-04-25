---
title: "ABB ACS580 Fault 2330 Earth Leakage, Causes & Fix"
description: "What ABB ACS580 Fault 2330 Earth Leakage means, why it trips, and how to isolate the motor, cable, or drive problem step by step."
pubDatetime: 2026-04-24T23:50:00Z
modDatetime: 2026-04-24T23:50:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - abb
  - acs580
---

## ABB ACS580 Fault 2330, What It Means

ABB ACS580 **Fault 2330** is an **Earth Leakage / Ground Fault** trip. The drive has detected current leaking from one of the output phases to ground, or a phase-current imbalance severe enough to look like a grounded motor circuit. In real plants, Fault 2330 usually means moisture in the motor, damaged VFD cable insulation, contamination in the motor junction box, or a winding starting to fail under PWM stress.

This is not a nuisance fault to keep resetting. If you keep restarting into a grounded motor circuit, you can take out the drive's output transistors.

[Jump to Fix](#fix)

## Common Causes

- **Moisture in the motor or peckerhead**. Washdown areas, cooling tower pumps, rooftop fans, and outdoor conveyors often trip 2330 after water intrusion.
- **Damaged VFD output cable**. Nicked insulation, tray abrasion, or liquid ingress into splices can leak current to ground.
- **Motor winding insulation breakdown**. Older motors may ohm out "fine" with a basic meter but fail a proper megger test.
- **Contamination in the terminal box**. Carbon dust, oil, coolant mist, or conductive residue can create a leakage path.
- **Output components wired incorrectly**. Output reactors, sine filters, or brake wiring issues can mimic a ground-fault condition.
- **Internal drive damage**. If 2330 remains with the motor leads removed, the output stage or current sensing circuit may be damaged.

## Step-by-Step Fix {#fix}

1. **Lock out power and disconnect the motor leads from the drive**. Remove U, V, and W from the ACS580 output terminals before testing. Never megger a motor circuit while it is still connected to the drive.
2. **Megger the motor cable to ground**. Test each phase conductor to ground at 500V or 1000V, depending on the motor and plant standard. A weak or unstable reading points to cable damage or moisture contamination.
3. **Megger the motor separately**. Isolate the motor from the cable and test the windings phase-to-ground. If the cable passes but the motor fails, you found the problem. For many maintenance teams, anything under 1 MΩ on a production motor is already a serious red flag.
4. **Inspect the motor junction box and conduit entries**. Look for condensation, oil, cracked grommets, loose lugs, or carbon tracking. Dry and clean the box before retesting.
5. **Check for cable routing and shielding issues**. VFD cable run next to sharp metal edges or sitting in wet tray is a common repeat offender. Replace damaged sections with proper VFD-rated cable.
6. **Power the drive with the motor still disconnected**. If Fault 2330 clears with the motor circuit removed, the fault is downstream of the drive. If 2330 remains, suspect the ACS580 output stage or sensing hardware.
7. **Inspect any output reactor or filter**. If the installation uses an output choke, du/dt filter, or sine filter, inspect those components and their wiring for insulation breakdown.
8. **Reconnect and test under no-load conditions**. If possible, uncouple the motor from the load and run at low speed first. Watch for the fault returning as the motor heats up, which often points to winding insulation failure.

## Parts Often Needed

| Part | Notes |
|------|-------|
| VFD-rated motor cable | [Amazon](https://www.amazon.com/s?k=VFD+rated+motor+cable&tag=errorcodefixes-20) \| Replace damaged or moisture-soaked output cable |
| Insulation resistance tester (megohmmeter) | [Amazon](https://www.amazon.com/s?k=megohmmeter+insulation+tester&tag=errorcodefixes-20) \| Required to prove whether the cable or motor is leaking to ground |
| Replacement 3-phase motor | [Amazon](https://www.amazon.com/s?k=3+phase+motor+480v&tag=errorcodefixes-20) \| Needed when winding insulation is breaking down |
| Motor terminal block / junction box parts | [Amazon](https://www.amazon.com/s?k=motor+junction+box+terminal+block&tag=errorcodefixes-20) \| Useful when the fault is caused by contamination or loose terminals |
| Output reactor | [Amazon](https://www.amazon.com/s?k=output+reactor+vfd&tag=errorcodefixes-20) \| Helps protect long motor leads and reduces stress on older motors |

## When to Call a Professional

Call an ABB drive specialist if Fault 2330 stays active with the motor leads removed, if the drive faults immediately at enable with a known-good motor circuit, or if you suspect an IGBT failure. At that point you are beyond normal field wiring troubleshooting and into bench-level drive diagnostics.

## See Also

- [ABB ACS355 Fault 2330, Earth Leakage Causes and Fix](/posts/abb-acs355-fault-2330/)
- [ABB ACS580 Fault 3130, DC Bus Undervoltage Fix](/posts/abb-acs580-fault-3130/)
- [ABB ACS880 Fault 2310 Overcurrent, Causes and Fix](/posts/abb-acs880-fault-2310-overcurrent/)
- [ABB VFD Fault 3210, Output Phase Loss Guide](/posts/abb-vfd-fault-3210/)

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
