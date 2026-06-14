---
title: "Siemens G120 F01625 - Causes & Fix"
description: "Siemens G120 F01625 (sign-of-life error in safety data) means the Safety Integrated function detected a communication fault. Causes, steps, parts."
pubDatetime: 2026-05-27T10:48:49Z
modDatetime: 2026-05-27T10:48:49Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "G120 Control Unit (CU) with Safety Integrated"
most_likely_cause: "EMC or cabinet wiring issues"
---

## Siemens G120 F01625 — What It Means

Fault F01625 on a Siemens SINAMICS G120 is a Safety Integrated error that Siemens labels as "sign-of-life error in the safety data." The drive's safety monitoring has detected that the expected cyclic safety sign-of-life exchange between internal processors is invalid, delayed, or missing. This fault typically triggers a STOP A reaction and shuts down the drive to protect against unsafe operation.

In practical terms, the drive's Safety Integrated function constantly checks that its internal safety processors are communicating correctly and exchanging a sign-of-life token. When that exchange fails or times out, the drive throws F01625. This can result from EMC interference, wiring problems on the safety circuits, an internal communication or timing issue within the drive's safety electronics, or a safety configuration that is out of sync after commissioning or parameter changes.

[Jump to Fix](#fix)

## Common Causes

- **EMC or cabinet wiring issues** Poor cable shielding, incorrect routing, or grounding problems can corrupt the safety signal path or internal communication.
- **Inadmissible voltage on safety circuit** Siemens specifically warns to check whether an incorrect voltage (for example, 230 V) has been connected to the safety inputs or outputs.
- **Internal safety processor communication failure** The sign-of-life exchange between the drive's internal safety processors can fail due to a software timing overflow or hardware fault.
- **Safety function state or configuration mismatch** After a parameter change, download, or commissioning step, the safety configuration may not be synchronized or validated correctly.
- **STO (Safe Torque Off) signal fault** A stuck, noisy, or open STO input can prevent the safety system from completing its handshake.

## Step-by-Step Fix {#fix}

1. {'lead': 'Check for additional faults and alarms', 'text': 'on the drive display or via the commissioning software, since F01625 may be secondary to another active issue.'}
2. {'lead': 'Inspect the cabinet layout, cable routing, and EMC compliance', 'text': 'Verify that power and signal cables are segregated, shields are properly grounded at one end, and safety wiring is routed away from high-voltage sources.'}
3. {'lead': 'Verify voltage and continuity on all safety inputs and outputs', 'text': 'Use a multimeter to confirm that no inadmissible voltage is present on the STO or other safety terminals, and check for open or shorted wires.'}
4. {'lead': 'Toggle the Safe Torque Off (STO) function off and back on', 'text': 'according to Siemens safety-function procedure, then observe whether the fault clears.'}
5. {'lead': 'Perform a full POWER ON reset', 'text': 'Switch off all power to the drive, wait for complete de-energization (capacitor discharge), then power back on and monitor the display.'}
6. {'lead': 'Re-check the drive after restart', 'text': 'and confirm whether F01625 returns or whether other safety faults appear in the fault log.'}
7. {'lead': 'Recommission or revalidate the safety configuration', 'text': "if the fault persists, using the drive's commissioning tool to synchronize safety parameters and repeat the safety acceptance test required by your installation."}

## Parts Often Needed

| Part | Notes |
|------|-------|
| G120 Control Unit (CU) with Safety Integrated | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f01625-fault-code&k=G120+Control+Unit+%28CU%29+with+Safety+Integrated&tag=errorcodefixes-20) \| Required if internal safety-processor communication is faulty and wiring checks pass. |
| Shielded STO/safety input cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f01625-fault-code&k=Shielded+STO%2Fsafety+input+cable&tag=errorcodefixes-20) \| Replace if existing cable has damaged shielding, incorrect voltage rating, or poor EMC performance. |
| External safety relay or failsafe controller | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f01625-fault-code&k=External+safety+relay+or+failsafe+controller&tag=errorcodefixes-20) \| Check and replace if your system uses an external device generating the safety telegrams or STO signals. |

## When to Call a Pro

Call a qualified Siemens drive technician or certified functional-safety engineer if the fault returns after wiring corrections and power cycling, if you are not trained in Safety Integrated commissioning, or if your installation is subject to regulatory safety validation (for example, ISO 13849 or IEC 61508). Safety-related faults require proper documentation and acceptance testing, and attempting to bypass or mask F01625 without resolving the root cause can create a serious hazard. A professional with PROFIsafe or Safety Integrated experience can re-validate the configuration, check internal communication with diagnostic software, and replace the control unit if the safety electronics have failed.

## See Also

- [Siemens G120 F01611 - Causes & Fix](/posts/siemens-g120-f01611-fault-code/)
- [Siemens Sinumerik Alarm 25201 — Causes & Fix](/posts/siemens-sinumerik-alarm-25201/)
- [Siemens Micromaster F0011 - Causes & Fix](/posts/siemens-micromaster-f0011-fault-code/)
- [Siemens Micromaster F0024 - Causes & Fix](/posts/siemens-micromaster-f0024-fault-code/)
